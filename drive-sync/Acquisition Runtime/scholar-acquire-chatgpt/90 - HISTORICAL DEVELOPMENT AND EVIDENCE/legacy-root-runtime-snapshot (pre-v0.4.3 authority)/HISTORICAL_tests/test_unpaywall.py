import httpx

from scholar_acquire.cache import DiskCache
from scholar_acquire.config import Settings
from scholar_acquire.http import CachedHttpClient
from scholar_acquire.models import AcquisitionPolicy, ResolvedIds, SourceVersion
from scholar_acquire.providers.base import AcquisitionContext
from scholar_acquire.providers.unpaywall import UnpaywallProvider


def test_unpaywall_splits_locations(tmp_path):
    payload = {"is_oa": True, "oa_locations": [
        {"url": "https://pub.test/a", "url_for_pdf": "https://pub.test/a.pdf", "host_type": "publisher", "version": "publishedVersion", "license": "cc-by"},
        {"url": "https://repo.test/a", "url_for_pdf": "https://repo.test/a.pdf", "host_type": "repository", "version": "acceptedVersion", "repository_institution": "Example University"},
    ]}
    def handler(request):
        return httpx.Response(200, json=payload)
    cache = DiskCache(tmp_path / "cache")
    http = CachedHttpClient(cache, "test", transport=httpx.MockTransport(handler), sleeper=lambda _: None)
    settings = Settings(contact_email="x@example.org", cache_dir=tmp_path / "cache")
    ctx = AcquisitionContext(ResolvedIds(doi="10.1/x"), AcquisitionPolicy(), http, cache, settings, [])
    out = UnpaywallProvider().run(ctx)
    assert len(out.publisher_locations) == 1
    assert len(out.repository_locations) == 1
    assert out.repository_locations[0].version == SourceVersion.ACCEPTED
