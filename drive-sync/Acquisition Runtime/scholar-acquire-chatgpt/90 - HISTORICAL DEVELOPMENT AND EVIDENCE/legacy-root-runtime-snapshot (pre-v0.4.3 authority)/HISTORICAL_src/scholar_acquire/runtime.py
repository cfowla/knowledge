from __future__ import annotations

import hashlib
import json
import mimetypes
import platform
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping

from .cache import DiskCache
from .config import Settings
from .errors import ContentValidationError, FetchRequired, RuntimeProtocolError
from .integrity import verify_build_manifest
from .models import (
    AcquisitionPolicy,
    AcquisitionSeed,
    ArticleIdentifier,
    Artifact,
    ArtifactFormat,
    ChatGptRuntimeSession,
    ExternalFetchRecord,
    LocationCandidate,
    ResolvedIds,
    RuntimeEvent,
    RuntimeFailureCode,
    RuntimeReceipt,
    RuntimeState,
    RuntimeStep,
    RuntimeTerminalOutcome,
    SourceVersion,
)
from .orchestrator import AcquisitionOrchestrator
from .providers.base import Provider
from .tool_transport import ToolMediatedHttpClient
from .utils import assert_allowed_url, extract_jats_article, looks_like_fulltext_html, validate_pdf


class ChatGptAcquisitionRuntime:
    """Resumable, network-free execution runtime for ChatGPT tool environments.

    `step()` runs until the acquisition code needs an uncached URL. Instead of
    opening a socket it returns a deterministic ExternalFetchRequest. The host
    (ChatGPT, another agent, or a human) retrieves that URL and calls an ingest
    method. Calling `step()` again resumes from the cache.
    """

    session_filename = "session.json"
    pending_filename = "pending_fetch.json"
    status_filename = "runtime_status.json"
    receipt_filename = "RUN_RECEIPT.json"
    events_filename = "runtime_events.jsonl"
    terminal_filename = "terminal_outcome.json"

    def __init__(
        self,
        session: ChatGptRuntimeSession,
        *,
        settings: Settings | None = None,
        providers: list[Provider] | None = None,
    ):
        self.session = session
        self.settings = settings or Settings(cache_dir=session.cache_dir)
        self.settings.cache_dir = session.cache_dir
        self.providers = providers
        self.build_identity = verify_build_manifest()
        self.cache = DiskCache(session.cache_dir)
        self.transport = ToolMediatedHttpClient(self.cache, self.settings.user_agent())

    @classmethod
    def create(
        cls,
        identifier: str | ArticleIdentifier,
        root: Path,
        *,
        output_dir: Path | None = None,
        cache_dir: Path | None = None,
        policy: AcquisitionPolicy | None = None,
        settings: Settings | None = None,
        providers: list[Provider] | None = None,
    ) -> "ChatGptAcquisitionRuntime":
        ident = identifier if isinstance(identifier, ArticleIdentifier) else ArticleIdentifier.parse(identifier)
        root = root.resolve()
        session_id = uuid.uuid4().hex[:12]
        session_dir = root / f"session-{session_id}"
        session_dir.mkdir(parents=True, exist_ok=False)
        out = (output_dir or (session_dir / "output")).resolve()
        cache = (cache_dir or (session_dir / "cache")).resolve()
        out.mkdir(parents=True, exist_ok=True)
        cache.mkdir(parents=True, exist_ok=True)
        session = ChatGptRuntimeSession(
            session_id=session_id,
            identifier=ident,
            session_dir=session_dir,
            output_dir=out,
            cache_dir=cache,
            policy=policy or AcquisitionPolicy(),
        )
        runtime = cls(session, settings=settings, providers=providers)
        runtime._write_receipt()
        runtime._event("runtime_integrity_verified", data={"package_tree_sha256": runtime.build_identity["actual_package_tree_sha256"]})
        runtime._event("runtime_initialized", data={"execution_mode": "tool-mediated", "network_in_python": False})
        runtime._save()
        return runtime

    @classmethod
    def load(
        cls,
        path: Path,
        *,
        settings: Settings | None = None,
        providers: list[Provider] | None = None,
    ) -> "ChatGptAcquisitionRuntime":
        path = path.resolve()
        session_path = path / cls.session_filename if path.is_dir() else path
        if not session_path.exists():
            raise RuntimeProtocolError(f"Runtime session not found: {session_path}")
        session = ChatGptRuntimeSession.model_validate_json(session_path.read_text(encoding="utf-8"))
        return cls(session, settings=settings, providers=providers)

    @property
    def session_path(self) -> Path:
        return self.session.session_dir / self.session_filename

    def step(self) -> RuntimeStep:
        if self.session.state in {RuntimeState.SUCCESS, RuntimeState.COMPLETE} and self.session.result_manifest:
            result = self._load_result()
            return RuntimeStep(
                state=RuntimeState.SUCCESS,
                session_path=self.session_path,
                result=result,
                terminal_outcome=self.session.terminal_outcome,
                message="Acquisition already successful",
            )

        if self.session.state == RuntimeState.EXHAUSTED:
            return RuntimeStep(
                state=RuntimeState.EXHAUSTED,
                session_path=self.session_path,
                terminal_outcome=self.session.terminal_outcome,
                message=self.session.terminal_outcome.message if self.session.terminal_outcome else "Provider policy exhausted",
            )

        if self.session.state == RuntimeState.BLOCKED and self.session.pending_request is not None:
            return RuntimeStep(
                state=RuntimeState.BLOCKED,
                session_path=self.session_path,
                pending_request=self.session.pending_request,
                terminal_outcome=self.session.terminal_outcome,
                message=self.session.terminal_outcome.message if self.session.terminal_outcome else "External fetch blocked",
            )

        if self.session.pending_request is not None:
            return RuntimeStep(
                state=RuntimeState.NEEDS_FETCH,
                session_path=self.session_path,
                pending_request=self.session.pending_request,
                message="Ingest the pending response before stepping again",
            )

        self._event("step_started", data={"state": self.session.state.value})
        seed = self.session.seed.model_copy(deep=True)
        runtime_meta = dict(seed.metadata.get("chatgpt_runtime") or {})
        runtime_meta.update(
            {
                "session_id": self.session.session_id,
                "transport": "tool-mediated",
                "network_in_python": False,
                "run_receipt": str(self.session.receipt_path) if self.session.receipt_path else None,
                "event_journal": str(self.session.session_dir / self.events_filename),
                "fetch_history": [r.model_dump(mode="json") for r in self.session.fetch_history],
            }
        )
        seed.metadata["chatgpt_runtime"] = runtime_meta

        orchestrator = AcquisitionOrchestrator(
            settings=self.settings,
            policy=self.session.policy,
            providers=self.providers,
            http=self.transport,
        )
        provider_policy = [getattr(p, "name", p.__class__.__name__) for p in orchestrator.providers]
        try:
            result = orchestrator.fetch(self.session.identifier, self.session.output_dir, seed=seed)
        except FetchRequired as exc:
            self.session.state = RuntimeState.NEEDS_FETCH
            self.session.pending_request = exc.request
            self.session.error = None
            self.session.terminal_outcome = None
            self._event(
                "external_fetch_requested",
                request_id=exc.request.request_id,
                provider=exc.request.provider,
                data={
                    "method": exc.request.method,
                    "redacted_url": exc.request.redacted_url,
                    "max_bytes": exc.request.max_bytes,
                    "ingest_token_sha256": hashlib.sha256(exc.request.ingest_token.encode()).hexdigest(),
                },
            )
            self._save()
            return RuntimeStep(
                state=RuntimeState.NEEDS_FETCH,
                session_path=self.session_path,
                pending_request=exc.request,
                message="External retrieval required; response must be correlated with request_id and ingest_token",
            )
        except Exception as exc:
            code = RuntimeFailureCode.RUNTIME_PROTOCOL_ERROR if isinstance(exc, RuntimeProtocolError) else RuntimeFailureCode.UNKNOWN
            outcome = RuntimeTerminalOutcome(
                state=RuntimeState.FAILED,
                reason_code=code,
                message=f"{type(exc).__name__}: {exc}",
                provider_policy=provider_policy,
                provider_exhaustion_confirmed=False,
            )
            self._set_terminal(outcome)
            self._event("terminal_failed", data={"reason_code": code.value, "message": outcome.message})
            self._save()
            return RuntimeStep(
                state=RuntimeState.FAILED,
                session_path=self.session_path,
                terminal_outcome=outcome,
                message=outcome.message,
            )
        finally:
            orchestrator.close()

        for attempt in result.attempts:
            self._event(
                "provider_result",
                provider=attempt.provider,
                data={
                    "action": attempt.action,
                    "outcome": attempt.outcome,
                    "http_status": attempt.http_status,
                    "message": attempt.message,
                },
            )
        for artifact in result.artifacts:
            self._event(
                "artifact_validated",
                provider=artifact.provider,
                data={
                    "format": artifact.format.value,
                    "sha256": artifact.sha256,
                    "size_bytes": artifact.size_bytes,
                    "structured": artifact.structured,
                    "version": artifact.version.value,
                },
            )

        provider_errors = [a for a in result.attempts if a.outcome == "error"]
        satisfied = self._policy_satisfied(result.artifacts)
        if satisfied:
            state = RuntimeState.SUCCESS
            outcome = RuntimeTerminalOutcome(
                state=state,
                message="Acquisition policy satisfied with validated payloads",
                provider_policy=provider_policy,
                provider_attempts=result.attempts,
                provider_exhaustion_confirmed=False,
                artifact_sha256=[a.sha256 for a in result.artifacts],
            )
            terminal_event = "terminal_success"
        elif provider_errors:
            state = RuntimeState.FAILED
            outcome = RuntimeTerminalOutcome(
                state=state,
                reason_code=RuntimeFailureCode.PROVIDER_ERROR,
                message="Provider execution ended with errors before exhaustion could be proven",
                provider_policy=provider_policy,
                provider_attempts=result.attempts,
                provider_exhaustion_confirmed=False,
                artifact_sha256=[a.sha256 for a in result.artifacts],
            )
            terminal_event = "terminal_failed"
        else:
            state = RuntimeState.EXHAUSTED
            outcome = RuntimeTerminalOutcome(
                state=state,
                message="Configured lawful provider policy exhausted without satisfying the acquisition policy",
                provider_policy=provider_policy,
                provider_attempts=result.attempts,
                provider_exhaustion_confirmed=True,
                artifact_sha256=[a.sha256 for a in result.artifacts],
            )
            terminal_event = "terminal_exhausted"

        runtime_meta = dict(result.metadata.get("chatgpt_runtime") or {})
        runtime_meta.update(
            {
                "terminal_state": state.value,
                "provider_policy": provider_policy,
                "provider_exhaustion_confirmed": outcome.provider_exhaustion_confirmed,
                "run_receipt": str(self.session.receipt_path) if self.session.receipt_path else None,
                "event_journal": str(self.session.session_dir / self.events_filename),
                "fetch_history": [r.model_dump(mode="json") for r in self.session.fetch_history],
            }
        )
        result.metadata["chatgpt_runtime"] = runtime_meta
        if result.manifest_path:
            result.manifest_path.write_text(
                json.dumps(result.model_dump(mode="json"), indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

        self.session.state = state
        self.session.pending_request = None
        self.session.result_manifest = result.manifest_path
        self.session.error = outcome.message if state == RuntimeState.FAILED else None
        self.session.terminal_outcome = outcome
        self._event(terminal_event, data={
            "state": state.value,
            "reason_code": outcome.reason_code.value if outcome.reason_code else None,
            "provider_exhaustion_confirmed": outcome.provider_exhaustion_confirmed,
            "artifact_sha256": outcome.artifact_sha256,
        })
        self._save()
        return RuntimeStep(
            state=state,
            session_path=self.session_path,
            result=result,
            terminal_outcome=outcome,
            message=outcome.message,
        )

    def ingest_file(
        self,
        path: Path,
        *,
        request_id: str,
        ingest_token: str,
        status_code: int = 200,
        content_type: str | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> ExternalFetchRecord:
        path = path.resolve()
        if not path.exists() or not path.is_file():
            raise RuntimeProtocolError(f"Fetched response file not found: {path}")
        merged_headers = dict(headers or {})
        if content_type:
            merged_headers["content-type"] = content_type
        elif "content-type" not in {k.lower() for k in merged_headers}:
            guessed, _ = mimetypes.guess_type(path.name)
            if guessed:
                merged_headers["content-type"] = guessed
        return self.ingest_bytes(
            path.read_bytes(),
            request_id=request_id,
            ingest_token=ingest_token,
            status_code=status_code,
            headers=merged_headers,
        )

    def ingest_bytes(
        self,
        content: bytes,
        *,
        request_id: str,
        ingest_token: str,
        status_code: int = 200,
        headers: Mapping[str, str] | None = None,
    ) -> ExternalFetchRecord:
        request = self._require_pending(request_id, ingest_token)
        response = self.transport.ingest_bytes(request, content, status_code=status_code, headers=headers)
        header_map = {k.lower(): v for k, v in (headers or {}).items()}
        record = ExternalFetchRecord(
            request_id=request.request_id,
            redacted_url=request.redacted_url,
            provider=request.provider,
            status_code=status_code,
            body_sha256=response.body_sha256,
            size_bytes=len(content),
            content_type=header_map.get("content-type"),
            cache_object_path=response.object_path,
        )
        self.session.fetch_history.append(record)
        self.session.pending_request = None
        self.session.state = RuntimeState.READY
        self.session.error = None
        self.session.terminal_outcome = None
        self._event(
            "external_response_ingested",
            request_id=request.request_id,
            provider=request.provider,
            data={
                "status_code": status_code,
                "body_sha256": response.body_sha256,
                "size_bytes": len(content),
                "content_type": header_map.get("content-type"),
                "cache_object_path": str(response.object_path),
            },
        )
        self._save()
        return record

    def import_artifact(
        self,
        path: Path,
        *,
        source_url: str | None = None,
        provider: str = "chatgpt_import",
        artifact_format: ArtifactFormat | str | None = None,
        version: SourceVersion | str = SourceVersion.UNKNOWN,
        license: str | None = None,
        structured: bool | None = None,
        metadata: dict | None = None,
    ) -> Artifact:
        path = path.resolve()
        if not path.exists() or not path.is_file():
            raise RuntimeProtocolError(f"Artifact file not found: {path}")
        body = path.read_bytes()
        fmt = ArtifactFormat(artifact_format) if artifact_format is not None else self._detect_format(path, body)
        normalized = body
        is_structured = bool(structured)
        media_type: str | None = None

        if fmt == ArtifactFormat.PDF:
            validate_pdf(body)
            media_type = "application/pdf"
            is_structured = False if structured is None else bool(structured)
        elif fmt == ArtifactFormat.JATS_XML:
            normalized = extract_jats_article(body)
            media_type = "application/xml"
            is_structured = True
        elif fmt == ArtifactFormat.HTML:
            if not looks_like_fulltext_html(body, "text/html"):
                raise ContentValidationError("Imported HTML does not look like scholarly full text")
            media_type = "text/html"
            is_structured = True if structured is None else bool(structured)
        elif fmt == ArtifactFormat.TEXT:
            if not body.strip():
                raise ContentValidationError("Imported text artifact is empty")
            media_type = "text/plain"
            is_structured = False if structured is None else bool(structured)

        digest, object_path = self.cache.store_object(normalized)
        artifact = Artifact(
            format=fmt,
            provider=provider,
            source_url=source_url or f"chatgpt://import/{path.name}",
            local_path=object_path,
            sha256=digest,
            size_bytes=len(normalized),
            media_type=media_type,
            version=SourceVersion(version),
            license=license,
            structured=is_structured,
            metadata={"imported_from": str(path), **(metadata or {})},
        )
        if not any(a.sha256 == artifact.sha256 for a in self.session.seed.artifacts):
            self.session.seed.artifacts.append(artifact)
        self.session.state = RuntimeState.READY
        self.session.result_manifest = None
        self.session.terminal_outcome = None
        self._event(
            "artifact_imported",
            provider=provider,
            data={"format": fmt.value, "sha256": artifact.sha256, "size_bytes": artifact.size_bytes},
        )
        self._save()
        return artifact

    def add_location(
        self,
        *,
        url: str,
        host_type: str,
        landing_page_url: str | None = None,
        pdf_url: str | None = None,
        version: SourceVersion | str = SourceVersion.UNKNOWN,
        license: str | None = None,
        source_name: str | None = None,
        discovered_by: str = "chatgpt_tool",
    ) -> LocationCandidate:
        if host_type not in {"publisher", "repository"}:
            raise RuntimeProtocolError("host_type must be 'publisher' or 'repository'")
        for candidate_url in (url, landing_page_url, pdf_url):
            if candidate_url:
                assert_allowed_url(candidate_url)
        candidate = LocationCandidate(
            url=url,
            landing_page_url=landing_page_url,
            pdf_url=pdf_url,
            host_type=host_type,
            version=version,
            license=license,
            source_name=source_name,
            discovered_by=discovered_by,
        )
        target = (
            self.session.seed.publisher_locations
            if host_type == "publisher"
            else self.session.seed.repository_locations
        )
        key = candidate.pdf_url or candidate.url
        if not any((x.pdf_url or x.url) == key for x in target):
            target.append(candidate)
        self.session.state = RuntimeState.READY
        self.session.result_manifest = None
        self._save()
        return candidate

    def add_resolved_ids(
        self,
        *,
        pmid: str | None = None,
        doi: str | None = None,
        pmcid: str | None = None,
        versioned_pmcid: str | None = None,
    ) -> ResolvedIds:
        self.session.seed.ids.merge(
            ResolvedIds(pmid=pmid, doi=doi, pmcid=pmcid, versioned_pmcid=versioned_pmcid)
        )
        self.session.state = RuntimeState.READY
        self.session.result_manifest = None
        self._save()
        return self.session.seed.ids

    def _require_pending(self, request_id: str, ingest_token: str):
        request = self.session.pending_request
        if request is None:
            raise RuntimeProtocolError("No pending external fetch")
        if request_id != request.request_id:
            raise RuntimeProtocolError(
                f"request_id mismatch: expected {request.request_id}, got {request_id}"
            )
        if ingest_token != request.ingest_token:
            raise RuntimeProtocolError("ingest_token mismatch; response is not correlated to the emitted request")
        return request

    def mark_fetch_blocked(
        self,
        *,
        request_id: str,
        ingest_token: str,
        message: str,
        reason_code: RuntimeFailureCode = RuntimeFailureCode.EXTERNAL_FETCH_BLOCKED,
    ) -> RuntimeTerminalOutcome:
        request = self._require_pending(request_id, ingest_token)
        outcome = RuntimeTerminalOutcome(
            state=RuntimeState.BLOCKED,
            reason_code=reason_code,
            message=message,
            provider_policy=self._provider_policy(),
            provider_exhaustion_confirmed=False,
            pending_request_id=request.request_id,
        )
        self.session.state = RuntimeState.BLOCKED
        self.session.terminal_outcome = outcome
        self.session.error = message
        self._event(
            "external_fetch_blocked",
            request_id=request.request_id,
            provider=request.provider,
            data={"reason_code": reason_code.value, "message": message},
        )
        self._save()
        return outcome

    @property
    def receipt_path(self) -> Path:
        return self.session.session_dir / self.receipt_filename

    @property
    def events_path(self) -> Path:
        return self.session.session_dir / self.events_filename

    def _write_receipt(self) -> RuntimeReceipt:
        if self.receipt_path.exists():
            receipt = RuntimeReceipt.model_validate_json(self.receipt_path.read_text(encoding="utf-8"))
            self.session.receipt_path = self.receipt_path
            return receipt
        build_path = Path(self.build_identity["manifest_path"])
        receipt = RuntimeReceipt(
            run_id=f"acq-{self.session.session_id}",
            session_id=self.session.session_id,
            identifier=self.session.identifier,
            version=str(self.build_identity.get("version", "unknown")),
            runtime_class=self.__class__.__name__,
            imported_from=Path(__file__).resolve(),
            package_tree_sha256=self.build_identity["actual_package_tree_sha256"],
            expected_package_tree_sha256=self.build_identity["package_tree_sha256"],
            integrity_verified=True,
            build_manifest_path=build_path,
            python_version=sys.version.split()[0],
            platform=platform.platform(),
        )
        self.receipt_path.write_text(
            json.dumps(receipt.model_dump(mode="json"), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        self.session.receipt_path = self.receipt_path
        return receipt

    def _event(
        self,
        event: str,
        *,
        request_id: str | None = None,
        provider: str | None = None,
        data: dict | None = None,
    ) -> RuntimeEvent:
        self.session.event_seq += 1
        item = RuntimeEvent(
            seq=self.session.event_seq,
            event=event,
            session_id=self.session.session_id,
            request_id=request_id,
            provider=provider,
            data=data or {},
        )
        self.events_path.parent.mkdir(parents=True, exist_ok=True)
        with self.events_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(item.model_dump(mode="json"), ensure_ascii=False) + "\n")
        return item

    def _set_terminal(self, outcome: RuntimeTerminalOutcome) -> None:
        self.session.state = outcome.state
        self.session.terminal_outcome = outcome
        self.session.error = outcome.message
        self.session.pending_request = None if outcome.state != RuntimeState.BLOCKED else self.session.pending_request

    def _provider_policy(self) -> list[str]:
        if self.providers is not None:
            return [getattr(p, "name", p.__class__.__name__) for p in self.providers]
        return ["europe_pmc", "pmc", "unpaywall", "publisher_oa", "repository"]

    def _policy_satisfied(self, artifacts: list[Artifact]) -> bool:
        has_structured = any(a.structured for a in artifacts)
        has_pdf = any(a.format == ArtifactFormat.PDF for a in artifacts)
        return (not self.session.policy.want_structured or has_structured) and (
            not self.session.policy.want_pdf or has_pdf
        )

    def _load_result(self):
        from .models import AcquisitionResult

        if not self.session.result_manifest or not self.session.result_manifest.exists():
            raise RuntimeProtocolError("Completed session manifest is missing")
        return AcquisitionResult.model_validate_json(
            self.session.result_manifest.read_text(encoding="utf-8")
        )

    def _save(self) -> None:
        self.session.updated_at = datetime.now(timezone.utc)
        self.session.session_dir.mkdir(parents=True, exist_ok=True)
        temp = self.session_path.with_suffix(".json.tmp")
        temp.write_text(
            json.dumps(self.session.model_dump(mode="json"), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        temp.replace(self.session_path)

        pending_path = self.session.session_dir / self.pending_filename
        if self.session.pending_request is not None:
            pending_path.write_text(
                json.dumps(self.session.pending_request.model_dump(mode="json"), indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
        elif pending_path.exists():
            pending_path.unlink()

        safe = {
            "schema_version": self.session.schema_version,
            "session_id": self.session.session_id,
            "identifier": self.session.identifier.model_dump(mode="json"),
            "state": self.session.state.value,
            "pending_request": (
                {
                    "request_id": self.session.pending_request.request_id,
                    "method": self.session.pending_request.method,
                    "redacted_url": self.session.pending_request.redacted_url,
                    "provider": self.session.pending_request.provider,
                    "max_bytes": self.session.pending_request.max_bytes,
                }
                if self.session.pending_request
                else None
            ),
            "fetches_ingested": len(self.session.fetch_history),
            "run_receipt": str(self.session.receipt_path) if self.session.receipt_path else None,
            "event_journal": str(self.events_path),
            "terminal_outcome": self.session.terminal_outcome.model_dump(mode="json") if self.session.terminal_outcome else None,
            "result_manifest": str(self.session.result_manifest) if self.session.result_manifest else None,
            "error": self.session.error,
            "updated_at": self.session.updated_at.isoformat(),
        }
        terminal_path = self.session.session_dir / self.terminal_filename
        if self.session.terminal_outcome is not None:
            terminal_path.write_text(
                json.dumps(self.session.terminal_outcome.model_dump(mode="json"), indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
        elif terminal_path.exists():
            terminal_path.unlink()

        (self.session.session_dir / self.status_filename).write_text(
            json.dumps(safe, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    @staticmethod
    def _detect_format(path: Path, body: bytes) -> ArtifactFormat:
        if body.lstrip().startswith(b"%PDF-"):
            return ArtifactFormat.PDF
        if path.suffix.lower() in {".xml", ".nxml"} or body.lstrip().startswith(b"<"):
            try:
                extract_jats_article(body)
                return ArtifactFormat.JATS_XML
            except ContentValidationError:
                pass
        lower = body[:8192].lower()
        if b"<html" in lower or b"<!doctype html" in lower:
            return ArtifactFormat.HTML
        return ArtifactFormat.TEXT
