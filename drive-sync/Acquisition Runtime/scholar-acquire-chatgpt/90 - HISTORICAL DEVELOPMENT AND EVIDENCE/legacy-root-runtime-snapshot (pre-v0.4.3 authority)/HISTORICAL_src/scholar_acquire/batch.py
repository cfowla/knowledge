from __future__ import annotations

import json
import platform
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Mapping

from .config import Settings
from .integrity import verify_build_manifest
from .models import AcquisitionPolicy, ArticleIdentifier, RuntimeFailureCode, RuntimeState, RuntimeStep
from .providers.base import Provider
from .runtime import ChatGptAcquisitionRuntime

_TERMINAL = {RuntimeState.SUCCESS, RuntimeState.EXHAUSTED, RuntimeState.BLOCKED, RuntimeState.FAILED, RuntimeState.COMPLETE}


class ChatGptBatchRuntime:
    """Persistent batch controller whose manifest is the source of truth.

    It never performs network I/O. Each item is a normal
    ChatGptAcquisitionRuntime session, and every external response must still be
    correlated to that item's emitted request_id + ingest_token.
    """

    state_filename = "batch_state.json"
    receipt_filename = "BATCH_RUN_RECEIPT.json"
    manifest_filename = "batch_manifest.json"
    events_filename = "batch_events.jsonl"

    def __init__(
        self,
        batch_dir: Path,
        *,
        settings: Settings | None = None,
        providers: list[Provider] | None = None,
    ):
        self.batch_dir = batch_dir.resolve()
        self.settings = settings
        self.providers = providers
        self.build_identity = verify_build_manifest()
        self.state_path = self.batch_dir / self.state_filename
        if not self.state_path.exists():
            raise FileNotFoundError(f"Batch state not found: {self.state_path}")
        self.state = json.loads(self.state_path.read_text(encoding="utf-8"))

    @classmethod
    def create(
        cls,
        identifiers: Iterable[str | ArticleIdentifier],
        root: Path,
        *,
        policy: AcquisitionPolicy | None = None,
        settings: Settings | None = None,
        providers: list[Provider] | None = None,
    ) -> "ChatGptBatchRuntime":
        identity = verify_build_manifest()
        parsed = [x if isinstance(x, ArticleIdentifier) else ArticleIdentifier.parse(x) for x in identifiers]
        if not parsed:
            raise ValueError("At least one PMID/PMCID/DOI is required")
        batch_id = uuid.uuid4().hex[:12]
        root = root.resolve()
        batch_dir = root / f"batch-{batch_id}"
        items_root = batch_dir / "items"
        items_root.mkdir(parents=True, exist_ok=False)

        records = []
        for ident in parsed:
            runtime = ChatGptAcquisitionRuntime.create(
                ident,
                items_root,
                policy=policy,
                settings=settings,
                providers=providers,
            )
            records.append({
                "identifier": ident.model_dump(mode="json"),
                "session_id": runtime.session.session_id,
                "session_path": str(runtime.session_path),
            })

        state = {
            "schema_version": "1",
            "batch_id": batch_id,
            "run_id": f"acq-batch-{batch_id}",
            "items": records,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
        (batch_dir / cls.state_filename).write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
        receipt = {
            "schema_version": "1",
            "run_id": state["run_id"],
            "batch_id": batch_id,
            "package": "scholar-acquire-chatgpt",
            "version": identity["version"],
            "runtime_class": cls.__name__,
            "package_tree_sha256": identity["actual_package_tree_sha256"],
            "expected_package_tree_sha256": identity["package_tree_sha256"],
            "integrity_verified": True,
            "build_manifest_path": identity["manifest_path"],
            "python_version": sys.version.split()[0],
            "platform": platform.platform(),
            "execution_mode": "tool-mediated",
            "network_in_python": False,
            "identifiers": [x.model_dump(mode="json") for x in parsed],
            "started_at": datetime.now(timezone.utc).isoformat(),
        }
        (batch_dir / cls.receipt_filename).write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        batch = cls(batch_dir, settings=settings, providers=providers)
        batch._event("batch_initialized", {"item_count": len(records), "package_tree_sha256": identity["actual_package_tree_sha256"]})
        batch.refresh_manifest()
        return batch

    @classmethod
    def load(cls, path: Path, **kwargs) -> "ChatGptBatchRuntime":
        path = path.resolve()
        batch_dir = path if path.is_dir() else path.parent
        return cls(batch_dir, **kwargs)

    def _load_item(self, record: dict) -> ChatGptAcquisitionRuntime:
        return ChatGptAcquisitionRuntime.load(Path(record["session_path"]), settings=self.settings, providers=self.providers)

    def step(self, session_id: str | None = None) -> RuntimeStep:
        target = None
        for record in self.state["items"]:
            if session_id and record["session_id"] != session_id:
                continue
            runtime = self._load_item(record)
            if session_id or runtime.session.state not in _TERMINAL:
                target = runtime
                break
        if target is None:
            raise StopIteration("No non-terminal batch items remain")
        step = target.step()
        self._event("item_step", {"session_id": target.session.session_id, "state": step.state.value})
        self.refresh_manifest()
        return step

    def ingest_file(
        self,
        path: Path,
        *,
        request_id: str,
        ingest_token: str,
        status_code: int = 200,
        content_type: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        runtime = self._runtime_for_request(request_id)
        record = runtime.ingest_file(
            path,
            request_id=request_id,
            ingest_token=ingest_token,
            status_code=status_code,
            content_type=content_type,
            headers=headers,
        )
        self._event("item_response_ingested", {"session_id": runtime.session.session_id, "request_id": request_id, "sha256": record.body_sha256})
        self.refresh_manifest()
        return record

    def mark_fetch_blocked(
        self,
        *,
        request_id: str,
        ingest_token: str,
        message: str,
        reason_code: RuntimeFailureCode = RuntimeFailureCode.EXTERNAL_FETCH_BLOCKED,
    ):
        runtime = self._runtime_for_request(request_id)
        outcome = runtime.mark_fetch_blocked(
            request_id=request_id,
            ingest_token=ingest_token,
            message=message,
            reason_code=reason_code,
        )
        self._event("item_blocked", {"session_id": runtime.session.session_id, "request_id": request_id, "reason_code": reason_code.value})
        self.refresh_manifest()
        return outcome

    def _runtime_for_request(self, request_id: str) -> ChatGptAcquisitionRuntime:
        for record in self.state["items"]:
            runtime = self._load_item(record)
            pending = runtime.session.pending_request
            if pending and pending.request_id == request_id:
                return runtime
        raise KeyError(f"No pending batch request with request_id={request_id}")

    def refresh_manifest(self) -> Path:
        items = []
        counts: dict[str, int] = {}
        for record in self.state["items"]:
            runtime = self._load_item(record)
            state = RuntimeState.SUCCESS if runtime.session.state == RuntimeState.COMPLETE else runtime.session.state
            counts[state.value] = counts.get(state.value, 0) + 1
            terminal = runtime.session.terminal_outcome
            items.append({
                "identifier": runtime.session.identifier.model_dump(mode="json"),
                "session_id": runtime.session.session_id,
                "state": state.value,
                "session_path": str(runtime.session_path),
                "run_receipt": str(runtime.receipt_path),
                "event_journal": str(runtime.events_path),
                "result_manifest": str(runtime.session.result_manifest) if runtime.session.result_manifest else None,
                "terminal_outcome": terminal.model_dump(mode="json") if terminal else None,
                "pending_request_id": runtime.session.pending_request.request_id if runtime.session.pending_request else None,
                "fetches_ingested": len(runtime.session.fetch_history),
            })
        manifest = {
            "schema_version": "1",
            "batch_id": self.state["batch_id"],
            "run_id": self.state["run_id"],
            "source_of_truth": "runtime-generated",
            "package_tree_sha256": self.build_identity["actual_package_tree_sha256"],
            "counts": counts,
            "items": items,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
        path = self.batch_dir / self.manifest_filename
        path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        self.state["updated_at"] = manifest["updated_at"]
        self.state_path.write_text(json.dumps(self.state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return path

    def _event(self, event: str, data: dict) -> None:
        path = self.batch_dir / self.events_filename
        item = {"event": event, "batch_id": self.state["batch_id"], "data": data, "at": datetime.now(timezone.utc).isoformat()}
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(item, ensure_ascii=False) + "\n")
