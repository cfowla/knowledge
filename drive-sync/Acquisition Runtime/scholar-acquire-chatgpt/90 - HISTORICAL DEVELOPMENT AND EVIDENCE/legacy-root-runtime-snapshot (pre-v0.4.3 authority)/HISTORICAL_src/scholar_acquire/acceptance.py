from __future__ import annotations

import json
import tempfile
from pathlib import Path

from .errors import RuntimeProtocolError
from .models import AcquisitionPolicy, Artifact, ArtifactFormat, ProviderOutcome, RuntimeState, SourceVersion
from .runtime import ChatGptAcquisitionRuntime
from .utils import validate_pdf


class _AcceptanceProvider:
    name = "acceptance_fixture"

    def run(self, ctx):
        response = ctx.http.get(
            "https://example.org/runtime-acceptance.pdf",
            headers={"Accept": "application/pdf"},
            cache_ttl_seconds=None,
            max_bytes=10000,
        )
        validate_pdf(response.content, response.headers.get("content-type"))
        digest, path = ctx.cache.store_object(response.content)
        return ProviderOutcome(artifacts=[Artifact(
            format=ArtifactFormat.PDF,
            provider=self.name,
            source_url=response.url,
            local_path=path,
            sha256=digest,
            size_bytes=len(response.content),
            media_type="application/pdf",
            version=SourceVersion.PUBLISHED,
        )])


def run_acceptance(root: Path | None = None) -> dict:
    """Exercise the proof-of-execution contract without external network access."""
    owned_tmp = None
    if root is None:
        owned_tmp = tempfile.TemporaryDirectory(prefix="scholar-acquire-acceptance-")
        root = Path(owned_tmp.name)
    root = Path(root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    runtime = ChatGptAcquisitionRuntime.create(
        "PMID:12345678",
        root / "sessions",
        policy=AcquisitionPolicy(want_structured=False, want_pdf=True),
        providers=[_AcceptanceProvider()],
    )
    first = runtime.step()
    assert first.state == RuntimeState.NEEDS_FETCH and first.pending_request

    # The runtime must reject an uncorrelated response before accepting the real one.
    correlation_rejected = False
    try:
        runtime.ingest_bytes(
            b"bad",
            request_id=first.pending_request.request_id,
            ingest_token="wrong-token",
        )
    except RuntimeProtocolError:
        correlation_rejected = True
    if not correlation_rejected:
        raise AssertionError("Runtime accepted a response with the wrong ingest token")

    pdf = b"%PDF-1.4\n" + (b"x" * 2048) + b"\n%%EOF"
    record = runtime.ingest_bytes(
        pdf,
        request_id=first.pending_request.request_id,
        ingest_token=first.pending_request.ingest_token,
        headers={"content-type": "application/pdf"},
    )
    final = runtime.step()
    if final.state != RuntimeState.SUCCESS:
        raise AssertionError(f"Acceptance runtime did not terminate SUCCESS: {final.state}")

    events = [json.loads(line) for line in runtime.events_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    names = [x["event"] for x in events]
    required = [
        "runtime_integrity_verified",
        "runtime_initialized",
        "external_fetch_requested",
        "external_response_ingested",
        "artifact_validated",
        "terminal_success",
    ]
    missing = [x for x in required if x not in names]
    if missing:
        raise AssertionError(f"Acceptance event journal missing: {missing}")

    receipt = json.loads(runtime.receipt_path.read_text(encoding="utf-8"))
    report = {
        "schema_version": "1",
        "passed": True,
        "session_id": runtime.session.session_id,
        "runtime_state": final.state.value,
        "receipt_path": str(runtime.receipt_path),
        "event_journal": str(runtime.events_path),
        "result_manifest": str(runtime.session.result_manifest),
        "integrity_verified": receipt["integrity_verified"],
        "package_tree_sha256": receipt["package_tree_sha256"],
        "request_id": first.pending_request.request_id,
        "response_sha256": record.body_sha256,
        "correlation_rejection_verified": correlation_rejected,
        "required_events_verified": True,
        "network_used_by_python": False,
    }
    report_path = root / "ACCEPTANCE_REPORT.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    report["report_path"] = str(report_path)
    # Keep temp alive until return; files may be removed after caller inspects report values.
    if owned_tmp is not None:
        report["ephemeral"] = True
        owned_tmp.cleanup()
    return report
