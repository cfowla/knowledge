from pathlib import Path

from scholar_acquire.config import Settings
from scholar_acquire.models import Artifact, ArtifactFormat, ProviderOutcome, ResolvedIds, SourceVersion
from scholar_acquire.orchestrator import AcquisitionOrchestrator


class StructuredProvider:
    name = "structured"
    def run(self, ctx):
        digest, path = ctx.cache.store_object(b"<article/>")
        return ProviderOutcome(ids=ResolvedIds(doi="10.1/x"), artifacts=[Artifact(format=ArtifactFormat.JATS_XML, provider=self.name, source_url="https://x/xml", local_path=path, sha256=digest, size_bytes=10, structured=True, version=SourceVersion.PUBLISHED)])


class PdfProvider:
    name = "pdf"
    def run(self, ctx):
        body = b"%PDF-1.4\n" + b"x" * 1024 + b"\n%%EOF"
        digest, path = ctx.cache.store_object(body)
        return ProviderOutcome(artifacts=[Artifact(format=ArtifactFormat.PDF, provider=self.name, source_url="https://x/pdf", local_path=path, sha256=digest, size_bytes=len(body), media_type="application/pdf")])


class ShouldNotRun:
    name = "late"
    def run(self, ctx):
        raise AssertionError("provider order did not stop after requirements were satisfied")


def test_orchestrator_order_and_handoff(tmp_path):
    settings = Settings(cache_dir=tmp_path / "cache")
    orch = AcquisitionOrchestrator(settings=settings, providers=[StructuredProvider(), PdfProvider(), ShouldNotRun()])
    try:
        result = orch.fetch("12345", tmp_path / "out")
    finally:
        orch.close()
    assert result.has_structured and result.has_pdf
    assert result.manifest_path and result.manifest_path.exists()
    assert result.handoff and result.handoff.preferred_structured_path.exists()
    assert result.handoff.preferred_pdf_path.exists()
