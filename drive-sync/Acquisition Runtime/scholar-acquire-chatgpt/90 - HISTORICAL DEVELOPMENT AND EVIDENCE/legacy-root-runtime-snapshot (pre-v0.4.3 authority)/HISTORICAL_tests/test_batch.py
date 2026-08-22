import json

from scholar_acquire.batch import ChatGptBatchRuntime
from scholar_acquire.models import AcquisitionPolicy, ProviderOutcome, RuntimeState


class DeferredProvider:
    name = "deferred"
    def run(self, ctx):
        ctx.http.get("https://example.org/batch-object", cache_ttl_seconds=None)
        return ProviderOutcome()


def test_batch_manifest_is_runtime_generated_source_of_truth(tmp_path):
    batch = ChatGptBatchRuntime.create(
        ["111", "222"],
        tmp_path,
        policy=AcquisitionPolicy(want_structured=False, want_pdf=True),
        providers=[DeferredProvider()],
    )
    step = batch.step()
    assert step.state == RuntimeState.NEEDS_FETCH
    manifest = json.loads((batch.batch_dir / batch.manifest_filename).read_text())
    assert manifest["source_of_truth"] == "runtime-generated"
    assert manifest["counts"]["needs_fetch"] == 1
    assert manifest["counts"]["ready"] == 1
    receipt = json.loads((batch.batch_dir / batch.receipt_filename).read_text())
    assert receipt["integrity_verified"] is True
    assert receipt["network_in_python"] is False
