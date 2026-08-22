import json
from pathlib import Path

import pytest

from scholar_acquire.batch import ChatGptBatchRuntime
from scholar_acquire.errors import RuntimeProtocolError
from scholar_acquire.integrity import verify_build_manifest
from scholar_acquire.models import (
    AcquisitionPolicy,
    Artifact,
    ArtifactFormat,
    ProviderOutcome,
    RuntimeFailureCode,
    RuntimeState,
    SourceVersion,
)
from scholar_acquire.runtime import ChatGptAcquisitionRuntime
from scholar_acquire.utils import validate_pdf

PDF = b"%PDF-1.4\n" + b"x" * 2048 + b"\n%%EOF"


class DeferredPdfProvider:
    name = "deferred_pdf"

    def run(self, ctx):
        resp = ctx.http.get(
            "https://example.org/article.pdf",
            headers={"Accept": "application/pdf"},
            cache_ttl_seconds=None,
            max_bytes=10_000,
        )
        if resp.status_code != 200:
            return ProviderOutcome()
        validate_pdf(resp.content, resp.headers.get("content-type"))
        digest, path = ctx.cache.store_object(resp.content)
        return ProviderOutcome(
            artifacts=[
                Artifact(
                    format=ArtifactFormat.PDF,
                    provider=self.name,
                    source_url=resp.url,
                    local_path=path,
                    sha256=digest,
                    size_bytes=len(resp.content),
                    media_type="application/pdf",
                    version=SourceVersion.PUBLISHED,
                )
            ]
        )


class EmptyProvider:
    name = "empty"
    def run(self, ctx):
        return ProviderOutcome()


class ErrorProvider:
    name = "error"
    def run(self, ctx):
        raise RuntimeError("provider exploded")


def make_runtime(tmp_path, provider=None):
    return ChatGptAcquisitionRuntime.create(
        "10.1234/example",
        tmp_path / "sessions",
        policy=AcquisitionPolicy(want_structured=False, want_pdf=True),
        providers=[provider or DeferredPdfProvider()],
    )


def test_runtime_receipt_and_integrity_are_present_before_fetch(tmp_path):
    build = verify_build_manifest()
    runtime = make_runtime(tmp_path)
    receipt = json.loads(runtime.receipt_path.read_text())
    assert receipt["integrity_verified"] is True
    assert receipt["package_tree_sha256"] == build["package_tree_sha256"]
    assert receipt["runtime_class"] == "ChatGptAcquisitionRuntime"
    assert receipt["network_in_python"] is False
    step = runtime.step()
    assert step.state == RuntimeState.NEEDS_FETCH
    assert runtime.receipt_path.stat().st_mtime_ns <= runtime.events_path.stat().st_mtime_ns


def test_ingest_requires_exact_request_id_and_capability_token(tmp_path):
    runtime = make_runtime(tmp_path)
    step = runtime.step()
    req = step.pending_request
    assert req is not None
    with pytest.raises(RuntimeProtocolError):
        runtime.ingest_bytes(PDF, request_id=req.request_id, ingest_token="wrong")
    with pytest.raises(RuntimeProtocolError):
        runtime.ingest_bytes(PDF, request_id="wrong", ingest_token=req.ingest_token)
    record = runtime.ingest_bytes(
        PDF,
        request_id=req.request_id,
        ingest_token=req.ingest_token,
        headers={"content-type": "application/pdf"},
    )
    assert record.cache_object_path and record.cache_object_path.exists()


def test_blocked_fetch_is_not_exhausted_and_can_resume(tmp_path):
    runtime = make_runtime(tmp_path)
    step = runtime.step()
    req = step.pending_request
    outcome = runtime.mark_fetch_blocked(
        request_id=req.request_id,
        ingest_token=req.ingest_token,
        message="host could not materialize response",
    )
    assert outcome.state == RuntimeState.BLOCKED
    assert outcome.reason_code == RuntimeFailureCode.EXTERNAL_FETCH_BLOCKED
    assert outcome.provider_exhaustion_confirmed is False
    assert (runtime.session.session_dir / runtime.pending_filename).exists()
    assert runtime.step().state == RuntimeState.BLOCKED

    runtime.ingest_bytes(
        PDF,
        request_id=req.request_id,
        ingest_token=req.ingest_token,
        headers={"content-type": "application/pdf"},
    )
    final = runtime.step()
    assert final.state == RuntimeState.SUCCESS
    assert not (runtime.session.session_dir / runtime.pending_filename).exists()


def test_clean_provider_exhaustion_is_explicit(tmp_path):
    runtime = make_runtime(tmp_path, EmptyProvider())
    final = runtime.step()
    assert final.state == RuntimeState.EXHAUSTED
    assert final.terminal_outcome.provider_exhaustion_confirmed is True
    assert final.terminal_outcome.reason_code is None


def test_provider_error_cannot_be_reported_as_exhaustion(tmp_path):
    runtime = make_runtime(tmp_path, ErrorProvider())
    final = runtime.step()
    assert final.state == RuntimeState.FAILED
    assert final.terminal_outcome.reason_code == RuntimeFailureCode.PROVIDER_ERROR
    assert final.terminal_outcome.provider_exhaustion_confirmed is False


def test_event_journal_proves_step_fetch_ingest_step_bridge(tmp_path):
    runtime = make_runtime(tmp_path)
    first = runtime.step()
    req = first.pending_request
    runtime.ingest_bytes(
        PDF,
        request_id=req.request_id,
        ingest_token=req.ingest_token,
        headers={"content-type": "application/pdf"},
    )
    runtime.step()
    events = [json.loads(line) for line in runtime.events_path.read_text().splitlines()]
    names = [x["event"] for x in events]
    assert "runtime_integrity_verified" in names
    assert "external_fetch_requested" in names
    assert "external_response_ingested" in names
    assert "artifact_validated" in names
    assert "terminal_success" in names
    requested = next(x for x in events if x["event"] == "external_fetch_requested")
    ingested = next(x for x in events if x["event"] == "external_response_ingested")
    assert requested["request_id"] == ingested["request_id"] == req.request_id
    journal_text = runtime.events_path.read_text()
    assert req.ingest_token not in journal_text


def test_batch_receipt_and_manifest_are_runtime_derived(tmp_path):
    batch = ChatGptBatchRuntime.create(
        ["20566676", "23963895"],
        tmp_path / "batches",
        policy=AcquisitionPolicy(want_structured=False, want_pdf=True),
        providers=[EmptyProvider()],
    )
    receipt_before = batch.receipt_path.read_bytes()
    for i in range(2):
        runtime = batch.load_runtime(i, providers=[EmptyProvider()])
        assert runtime.step().state == RuntimeState.EXHAUSTED
    manifest = batch.refresh_manifest()
    assert batch.receipt_path.read_bytes() == receipt_before
    assert manifest.evidence_complete is True
    assert manifest.counts[RuntimeState.EXHAUSTED.value] == 2
    assert all(item.run_receipt and Path(item.run_receipt).exists() for item in manifest.items)
