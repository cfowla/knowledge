from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from .errors import ContentValidationError, RuntimeProtocolError
from .integration import build_atom_sea_handoff
from .models import (
    AcquisitionPolicy,
    AcquisitionResult,
    ArticleIdentifier,
    Artifact,
    ArtifactFormat,
    IdentifierKind,
    ResolvedIds,
    RuntimeFailureCode,
    RuntimeState,
    RuntimeStep,
    RuntimeTerminalOutcome,
    SourceVersion,
)
from .runtime import ChatGptAcquisitionRuntime
from .utils import assert_allowed_url, link_or_copy, validate_pdf


class ChatGptVerticalSliceRuntime(ChatGptAcquisitionRuntime):
    """v0.4 PMID-to-PDF vertical slice.

    This runtime deliberately does not execute provider orchestration. ChatGPT or
    another host tool discovers and materializes a lawful OA PDF, then Python
    admits it through ``import_artifact`` and remains authoritative for PDF
    validation, SHA-256 integrity, provenance persistence, manifest generation,
    ATOM/SEA handoff construction, and terminal state.
    """

    contract_version = "0.4.0"
    provider_name = "chatgpt_native_import"

    @classmethod
    def create(
        cls,
        identifier: str | ArticleIdentifier,
        root: Path,
        *,
        output_dir: Path | None = None,
        cache_dir: Path | None = None,
        settings=None,
    ) -> "ChatGptVerticalSliceRuntime":
        ident = identifier if isinstance(identifier, ArticleIdentifier) else ArticleIdentifier.parse(identifier)
        if ident.kind != IdentifierKind.PMID:
            raise RuntimeProtocolError("v0.4 vertical-slice sessions require a PMID")
        policy = AcquisitionPolicy(
            want_structured=False,
            want_pdf=True,
            max_retries=0,
        )
        runtime = super().create(
            ident,
            root,
            output_dir=output_dir,
            cache_dir=cache_dir,
            policy=policy,
            settings=settings,
            providers=[],
        )
        runtime.session.seed.ids.pmid = ident.value
        runtime.session.seed.metadata["v0_4_vertical_slice"] = {
            "contract_version": cls.contract_version,
            "requested_identifier": ident.model_dump(mode="json"),
            "provider_orchestration": False,
            "fallback_providers": False,
            "batching": False,
            "raw_http_in_python": False,
            "retries": False,
            "automatic_provider_exhaustion": False,
            "accepted_artifact_formats": [ArtifactFormat.PDF.value],
        }
        runtime._event(
            "v0_4_vertical_slice_initialized",
            data={
                "requested_pmid": ident.value,
                "provider_orchestration": False,
                "fallback_providers": False,
            },
        )
        runtime._save()
        return runtime

    def import_artifact(
        self,
        path: Path,
        *,
        source_url: str,
        discovery_provenance: Mapping[str, Any],
        acquisition_context: Mapping[str, Any],
        version: SourceVersion | str = SourceVersion.UNKNOWN,
        license: str | None = None,
    ) -> Artifact:
        """Admit one ChatGPT-materialized lawful OA PDF under the v0.4 contract."""
        if not source_url or not source_url.strip():
            raise RuntimeProtocolError("v0.4 import requires source_url")
        assert_allowed_url(source_url)
        if not discovery_provenance:
            raise RuntimeProtocolError("v0.4 import requires non-empty discovery_provenance")
        if not acquisition_context:
            raise RuntimeProtocolError("v0.4 import requires non-empty acquisition_context")
        lawful_basis = acquisition_context.get("lawful_access_basis")
        if not isinstance(lawful_basis, str) or not lawful_basis.strip():
            raise RuntimeProtocolError("v0.4 acquisition_context requires lawful_access_basis")
        if acquisition_context.get("open_access") is not True:
            raise RuntimeProtocolError("v0.4 acquisition_context requires open_access=true")

        requested = self.session.identifier
        if requested.kind != IdentifierKind.PMID:
            raise RuntimeProtocolError("v0.4 vertical-slice session identity is not a PMID")

        contract_metadata = {
            "contract_version": self.contract_version,
            "requested_identifier": requested.model_dump(mode="json"),
            "source_url": source_url,
            "discovery_provenance": dict(discovery_provenance),
            "acquisition_context": dict(acquisition_context),
        }
        artifact = super().import_artifact(
            path,
            source_url=source_url,
            provider=self.provider_name,
            artifact_format=ArtifactFormat.PDF,
            version=version,
            license=license,
            structured=False,
            metadata={"v0_4": contract_metadata},
        )
        self._event(
            "artifact_validated",
            provider=self.provider_name,
            data={
                "format": ArtifactFormat.PDF.value,
                "sha256": artifact.sha256,
                "size_bytes": artifact.size_bytes,
                "source_url": source_url,
                "requested_pmid": requested.value,
                "version": artifact.version.value,
                "license": artifact.license,
            },
        )
        self._save()
        return artifact

    def add_resolved_ids(
        self,
        *,
        pmid: str | None = None,
        doi: str | None = None,
        pmcid: str | None = None,
        versioned_pmcid: str | None = None,
    ) -> ResolvedIds:
        requested_pmid = self.session.identifier.value
        if pmid is not None and pmid != requested_pmid:
            raise RuntimeProtocolError(
                f"Resolved PMID {pmid} conflicts with requested PMID {requested_pmid}"
            )
        return super().add_resolved_ids(
            pmid=requested_pmid,
            doi=doi,
            pmcid=pmcid,
            versioned_pmcid=versioned_pmcid,
        )

    def mark_blocked(
        self,
        *,
        message: str,
        reason_code: RuntimeFailureCode = RuntimeFailureCode.EXTERNAL_FETCH_BLOCKED,
    ) -> RuntimeTerminalOutcome:
        """Record host-side inability to materialize a lawful PDF without claiming exhaustion."""
        outcome = RuntimeTerminalOutcome(
            state=RuntimeState.BLOCKED,
            reason_code=reason_code,
            message=message,
            provider_policy=[],
            provider_attempts=[],
            provider_exhaustion_confirmed=False,
            artifact_sha256=[a.sha256 for a in self.session.seed.artifacts],
        )
        self._set_terminal(outcome)
        self._event(
            "terminal_blocked",
            data={
                "reason_code": reason_code.value,
                "provider_exhaustion_confirmed": False,
                "message": message,
            },
        )
        self._save()
        return outcome

    def step(self) -> RuntimeStep:
        if self.session.state in {RuntimeState.SUCCESS, RuntimeState.COMPLETE} and self.session.result_manifest:
            result = self._load_result()
            return RuntimeStep(
                state=RuntimeState.SUCCESS,
                session_path=self.session_path,
                result=result,
                terminal_outcome=self.session.terminal_outcome,
                message="v0.4 acquisition already successful",
            )
        if self.session.state == RuntimeState.BLOCKED:
            return RuntimeStep(
                state=RuntimeState.BLOCKED,
                session_path=self.session_path,
                terminal_outcome=self.session.terminal_outcome,
                message=self.session.terminal_outcome.message if self.session.terminal_outcome else "Artifact materialization blocked",
            )
        if self.session.state == RuntimeState.FAILED:
            return RuntimeStep(
                state=RuntimeState.FAILED,
                session_path=self.session_path,
                terminal_outcome=self.session.terminal_outcome,
                message=self.session.terminal_outcome.message if self.session.terminal_outcome else "v0.4 runtime failed",
            )
        if self.session.state == RuntimeState.EXHAUSTED:
            return self._fail(
                RuntimeFailureCode.RUNTIME_PROTOCOL_ERROR,
                "EXHAUSTED is invalid in the v0.4 vertical slice because no provider policy is executed",
            )
        if self.session.pending_request is not None:
            return self._fail(
                RuntimeFailureCode.RUNTIME_PROTOCOL_ERROR,
                "ExternalFetchRequest is invalid in the v0.4 vertical-slice acceptance path",
            )

        pdfs = [a for a in self.session.seed.artifacts if a.format == ArtifactFormat.PDF]
        if not pdfs:
            self.session.state = RuntimeState.READY
            self.session.terminal_outcome = None
            self.session.error = None
            self._event(
                "awaiting_artifact_import",
                data={
                    "required_format": ArtifactFormat.PDF.value,
                    "provider_orchestration": False,
                },
            )
            self._save()
            return RuntimeStep(
                state=RuntimeState.READY,
                session_path=self.session_path,
                message="Awaiting ChatGPT-materialized lawful OA PDF via runtime.import_artifact(); no provider orchestration will run",
            )

        artifact = pdfs[0]
        try:
            body = artifact.local_path.read_bytes()
            validate_pdf(body)
            digest = hashlib.sha256(body).hexdigest()
            if digest != artifact.sha256:
                raise ContentValidationError(
                    f"Imported artifact SHA-256 mismatch: manifest={artifact.sha256} actual={digest}"
                )
            self._validate_import_contract(artifact)
            result = self._finalize_success(artifact)
        except Exception as exc:
            code = (
                RuntimeFailureCode.INVALID_RESPONSE
                if isinstance(exc, ContentValidationError)
                else RuntimeFailureCode.RUNTIME_PROTOCOL_ERROR
            )
            return self._fail(code, f"{type(exc).__name__}: {exc}")

        outcome = RuntimeTerminalOutcome(
            state=RuntimeState.SUCCESS,
            message="v0.4 vertical-slice contract satisfied with one validated lawful OA PDF",
            provider_policy=[],
            provider_attempts=[],
            provider_exhaustion_confirmed=False,
            artifact_sha256=[artifact.sha256],
        )
        self.session.state = RuntimeState.SUCCESS
        self.session.pending_request = None
        self.session.result_manifest = result.manifest_path
        self.session.error = None
        self.session.terminal_outcome = outcome
        self._event(
            "terminal_success",
            data={
                "state": RuntimeState.SUCCESS.value,
                "provider_orchestration": False,
                "provider_exhaustion_confirmed": False,
                "artifact_sha256": [artifact.sha256],
            },
        )
        self._save()
        return RuntimeStep(
            state=RuntimeState.SUCCESS,
            session_path=self.session_path,
            result=result,
            terminal_outcome=outcome,
            message=outcome.message,
        )

    def _validate_import_contract(self, artifact: Artifact) -> None:
        if artifact.provider != self.provider_name:
            raise RuntimeProtocolError("v0.4 success requires a chatgpt_native_import artifact")
        if artifact.format != ArtifactFormat.PDF:
            raise RuntimeProtocolError("v0.4 success requires a PDF")
        assert_allowed_url(artifact.source_url)
        metadata = artifact.metadata.get("v0_4")
        if not isinstance(metadata, dict):
            raise RuntimeProtocolError("v0.4 import provenance metadata is missing")
        requested = metadata.get("requested_identifier") or {}
        if requested.get("kind") != IdentifierKind.PMID.value or requested.get("value") != self.session.identifier.value:
            raise RuntimeProtocolError("v0.4 imported artifact is not bound to the requested PMID")
        if metadata.get("source_url") != artifact.source_url:
            raise RuntimeProtocolError("v0.4 artifact source URL metadata mismatch")
        if not metadata.get("discovery_provenance"):
            raise RuntimeProtocolError("v0.4 discovery provenance is missing")
        context = metadata.get("acquisition_context") or {}
        if context.get("open_access") is not True or not context.get("lawful_access_basis"):
            raise RuntimeProtocolError("v0.4 lawful OA acquisition context is missing")
        resolved_pmid = self.session.seed.ids.pmid
        if resolved_pmid and resolved_pmid != self.session.identifier.value:
            raise RuntimeProtocolError(
                f"Resolved PMID {resolved_pmid} conflicts with requested PMID {self.session.identifier.value}"
            )

    def _finalize_success(self, artifact: Artifact) -> AcquisitionResult:
        requested_pmid = self.session.identifier.value
        resolved = self.session.seed.ids.model_copy(deep=True)
        if resolved.pmid and resolved.pmid != requested_pmid:
            raise RuntimeProtocolError(
                f"Resolved PMID {resolved.pmid} conflicts with requested PMID {requested_pmid}"
            )
        resolved.pmid = requested_pmid

        workdir = self.session.output_dir / requested_pmid
        workdir.mkdir(parents=True, exist_ok=True)
        dest = workdir / "fulltext.chatgpt_native_import.pdf"
        if artifact.local_path.resolve() != dest.resolve():
            link_or_copy(artifact.local_path, dest)
        materialized = artifact.model_copy(deep=True)
        materialized.local_path = dest

        runtime_metadata = {
            "contract_version": self.contract_version,
            "critical_path": [
                "pmid",
                "chatgpt_lawful_oa_discovery_and_materialization",
                "runtime.import_artifact",
                "pdf_validation",
                "sha256",
                "manifest",
                "success",
            ],
            "provider_orchestration": False,
            "fallback_providers": False,
            "batching": False,
            "raw_http_in_python": False,
            "retries": False,
            "automatic_provider_exhaustion": False,
            "artifact_formats_in_acceptance_path": [ArtifactFormat.PDF.value],
            "run_receipt": str(self.session.receipt_path) if self.session.receipt_path else None,
            "event_journal": str(self.events_path),
        }
        result = AcquisitionResult(
            identifier=self.session.identifier,
            resolved_ids=resolved,
            artifacts=[materialized],
            attempts=[],
            metadata={
                "v0_4_vertical_slice": runtime_metadata,
                "discovery_provenance": artifact.metadata["v0_4"]["discovery_provenance"],
                "acquisition_context": artifact.metadata["v0_4"]["acquisition_context"],
                "source_url": artifact.source_url,
                "source_version": artifact.version.value,
                "license": artifact.license,
            },
        )
        manifest_path = workdir / "manifest.json"
        result.manifest_path = manifest_path
        result.handoff = build_atom_sea_handoff(result, manifest_path)
        manifest_path.write_text(
            json.dumps(result.model_dump(mode="json"), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        self._event(
            "manifest_written",
            data={
                "manifest_path": str(manifest_path),
                "pdf_sha256": materialized.sha256,
                "preferred_pdf_path": str(result.handoff.preferred_pdf_path),
            },
        )
        return result

    def _fail(self, reason_code: RuntimeFailureCode, message: str) -> RuntimeStep:
        outcome = RuntimeTerminalOutcome(
            state=RuntimeState.FAILED,
            reason_code=reason_code,
            message=message,
            provider_policy=[],
            provider_attempts=[],
            provider_exhaustion_confirmed=False,
            artifact_sha256=[a.sha256 for a in self.session.seed.artifacts],
        )
        self._set_terminal(outcome)
        self._event(
            "terminal_failed",
            data={
                "reason_code": reason_code.value,
                "provider_exhaustion_confirmed": False,
                "message": message,
            },
        )
        self._save()
        return RuntimeStep(
            state=RuntimeState.FAILED,
            session_path=self.session_path,
            terminal_outcome=outcome,
            message=message,
        )

    def _provider_policy(self) -> list[str]:
        return []
