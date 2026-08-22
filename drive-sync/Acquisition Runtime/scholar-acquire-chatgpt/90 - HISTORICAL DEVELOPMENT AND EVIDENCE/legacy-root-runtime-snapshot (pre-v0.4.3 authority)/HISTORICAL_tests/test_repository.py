import httpx

from scholar_acquire.cache import DiskCache
from scholar_acquire.config import Settings
from scholar_acquire.http import CachedHttpClient
from scholar_acquire.models import AcquisitionPolicy, ArtifactFormat, ResolvedIds
from scholar_acquire.providers.base import AcquisitionContext
from scholar_acquire.providers.repository import RepositoryProvider


PDF = b"%PDF-1.7\n" + b"x" * 1200 + b"\n%%EOF"


def test_repository_prefers_accepted_and_excludes_submitted(tmp_path):
    work = {"locations": [
        {"is_oa": True, "pdf_url": "https://preprint.test/a.pdf", "landing_page_url": None, "version": "submittedVersion", "source": {"type": "repository", "display_name": "arXiv"}},
        {"is_oa": True, "pdf_url": "https://repo.test/a.pdf", "landing_page_url": None, "version": "acceptedVersion", "source": {"type": "repository", "display_name": "Example University Repository"}},
    ]}
    def handler(request):
        if request.url.host == "api.openalex.org":
            return httpx.Response(200, json=work)
        if request.url.host == "repo.test":
            return httpx.Response(200, content=PDF, headers={"content-type": "application/pdf"})
        return httpx.Response(404)
    cache = DiskCache(tmp_path / "cache")
    http = CachedHttpClient(cache, "test", transport=httpx.MockTransport(handler), sleeper=lambda _: None)
    ctx = AcquisitionContext(ResolvedIds(doi="10.1/x"), AcquisitionPolicy(allow_submitted=False), http, cache, Settings(cache_dir=tmp_path / "cache"), [])
    out = RepositoryProvider().run(ctx)
    assert len(out.artifacts) == 1
    assert out.artifacts[0].format == ArtifactFormat.PDF
    assert out.artifacts[0].metadata["repository"] == "Example University Repository"
