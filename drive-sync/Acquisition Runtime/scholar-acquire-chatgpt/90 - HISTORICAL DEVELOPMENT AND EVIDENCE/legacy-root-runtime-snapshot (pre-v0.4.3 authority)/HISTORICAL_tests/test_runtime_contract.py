import json
from pathlib import Path

import pytest

from scholar_acquire.acceptance import run_acceptance
from scholar_acquire.errors import RuntimeIntegrityError, RuntimeProtocolError, RuntimeUnavailableError
from scholar_acquire.integrity import verify_build_manifest, write_build_manifest
from scholar_acquire.models import AcquisitionPolicy, ProviderOutcome, RuntimeFailureCode, RuntimeState
from scholar_acquire.runtime import ChatGptAcquisitionRuntime


class DeferredProvider:
    name = "deferred"
    def run(self, ctx):
        ctx.http.get("https://example.org/object", cache_ttl_seconds=None)
        return ProviderOutcome()


def test_run_receipt_events_and_blocked_are_machine_generated(tmp_path):
    runtime = ChatGptAcquisitionRuntime.create(
        "123456",
        tmp_path / "sessions",
        policy=AcquisitionPolicy(want_structured=False, want_pdf=True),
        providers=[DeferredProvider()],
    )
    step = runtime.step()
    assert step.state == RuntimeState.NEEDS_FETCH
    request = step.pending_request
    assert request
    outcome = runtime.mark_fetch_blocked(
        request_id=request.request_id,
        ingest_token=request.ingest_token,
        message="host transport unavailable",
    )
    assert outcome.state == RuntimeState.BLOCKED
    assert outcome.reason_code == RuntimeFailureCode.EXTERNAL_FETCH_BLOCKED
    assert outcome.provider_exhaustion_confirmed is False
    assert runtime.session.pending_request is not None  # resumable
    receipt = json.loads(runtime.receipt_path.read_text())
    assert receipt["integrity_verified"] is True
    events = runtime.events_path.read_text()
    assert "runtime_integrity_verified" in events
    assert "external_fetch_requested" in events
    assert "external_fetch_blocked" in events


def test_response_correlation_is_fail_closed(tmp_path):
    runtime = ChatGptAcquisitionRuntime.create(
        "123456",
        tmp_path / "sessions",
        policy=AcquisitionPolicy(want_structured=False, want_pdf=True),
        providers=[DeferredProvider()],
    )
    request = runtime.step().pending_request
    assert request
    with pytest.raises(RuntimeProtocolError):
        runtime.ingest_bytes(b"x", request_id=request.request_id, ingest_token="wrong")
    with pytest.raises(RuntimeProtocolError):
        runtime.ingest_bytes(b"x", request_id="wrong-id", ingest_token=request.ingest_token)


def test_integrity_manifest_missing_and_tampering_fail_closed(tmp_path):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "a.py").write_text("x=1\n")
    with pytest.raises(RuntimeUnavailableError):
        verify_build_manifest(pkg)
    write_build_manifest(pkg, version="test")
    assert verify_build_manifest(pkg)["integrity_verified"] is True
    (pkg / "a.py").write_text("x=2\n")
    with pytest.raises(RuntimeIntegrityError):
        verify_build_manifest(pkg)


def test_synthetic_acceptance_proves_full_runtime_loop(tmp_path):
    report = run_acceptance(tmp_path / "acceptance")
    assert report["passed"] is True
    assert report["runtime_state"] == "success"
    assert report["integrity_verified"] is True
    assert report["correlation_rejection_verified"] is True
    assert report["required_events_verified"] is True
    assert report["network_used_by_python"] is False
    assert Path(report["report_path"]).exists()
