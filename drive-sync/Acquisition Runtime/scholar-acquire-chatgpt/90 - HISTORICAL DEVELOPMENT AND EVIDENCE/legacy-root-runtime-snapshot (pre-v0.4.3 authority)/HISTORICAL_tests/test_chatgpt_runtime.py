from pathlib import Path

from scholar_acquire.models import (
    AcquisitionPolicy,
    Artifact,
    ArtifactFormat,
    ProviderOutcome,
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


class MustNotRunProvider:
    name = "must_not_run"

    def run(self, ctx):
        raise AssertionError("seed artifact should have satisfied the policy")


def test_runtime_deferred_fetch_roundtrip_and_persistence(tmp_path):
    policy = AcquisitionPolicy(want_structured=False, want_pdf=True)
    runtime = ChatGptAcquisitionRuntime.create(
        "10.1234/example",
        tmp_path / "sessions",
        policy=policy,
        providers=[DeferredPdfProvider()],
    )

    first = runtime.step()
    assert first.state == RuntimeState.NEEDS_FETCH
    assert first.pending_request is not None
    assert first.pending_request.provider == "deferred_pdf"
    request_id = first.pending_request.request_id

    # Simulate a new ChatGPT/Python invocation loading the resumable session.
    runtime = ChatGptAcquisitionRuntime.load(runtime.session_path, providers=[DeferredPdfProvider()])
    record = runtime.ingest_bytes(
        PDF,
        request_id=request_id,
        ingest_token=first.pending_request.ingest_token,
        headers={"content-type": "application/pdf"},
    )
    assert record.size_bytes == len(PDF)

    final = runtime.step()
    assert final.state == RuntimeState.SUCCESS
    assert final.result is not None and final.result.has_pdf
    assert final.result.handoff and final.result.handoff.preferred_pdf_path.exists()
    assert final.result.metadata["chatgpt_runtime"]["network_in_python"] is False
    assert len(final.result.metadata["chatgpt_runtime"]["fetch_history"]) == 1


def test_imported_pdf_can_satisfy_runtime_without_network(tmp_path):
    path = tmp_path / "uploaded.pdf"
    path.write_bytes(PDF)
    policy = AcquisitionPolicy(want_structured=False, want_pdf=True)
    runtime = ChatGptAcquisitionRuntime.create(
        "123456",
        tmp_path / "sessions",
        policy=policy,
        providers=[MustNotRunProvider()],
    )
    artifact = runtime.import_artifact(path, source_url="chatgpt://user-upload/article.pdf")
    assert artifact.format == ArtifactFormat.PDF

    result = runtime.step()
    assert result.state == RuntimeState.SUCCESS
    assert result.result and result.result.has_pdf


def test_runtime_status_redacts_sensitive_query_values(tmp_path):
    class QueryProvider:
        name = "query"
        def run(self, ctx):
            ctx.http.get("https://api.example.org/item", params={"email": "person@example.org", "api_key": "secret"})
            return ProviderOutcome()

    runtime = ChatGptAcquisitionRuntime.create(
        "10.1234/example",
        tmp_path / "sessions",
        policy=AcquisitionPolicy(want_structured=False, want_pdf=True),
        providers=[QueryProvider()],
    )
    step = runtime.step()
    assert step.state == RuntimeState.NEEDS_FETCH
    status = (runtime.session.session_dir / runtime.status_filename).read_text()
    assert "person%40example.org" not in status
    assert "secret" not in status
    assert "REDACTED" in status


def test_runtime_session_writes_machine_readable_pending_request(tmp_path):
    runtime = ChatGptAcquisitionRuntime.create(
        "10.1234/example",
        tmp_path / "sessions",
        policy=AcquisitionPolicy(want_structured=False, want_pdf=True),
        providers=[DeferredPdfProvider()],
    )
    step = runtime.step()
    pending = runtime.session.session_dir / runtime.pending_filename
    assert step.state == RuntimeState.NEEDS_FETCH
    assert pending.exists()
    assert step.pending_request.request_id in pending.read_text()
