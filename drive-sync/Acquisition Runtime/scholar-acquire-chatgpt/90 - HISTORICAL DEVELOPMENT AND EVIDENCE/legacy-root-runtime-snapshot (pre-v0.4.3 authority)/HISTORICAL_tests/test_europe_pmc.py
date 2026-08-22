import json
import httpx

from scholar_acquire.cache import DiskCache
from scholar_acquire.config import Settings
from scholar_acquire.http import CachedHttpClient
from scholar_acquire.models import AcquisitionPolicy, ResolvedIds
from scholar_acquire.providers.base import AcquisitionContext
from scholar_acquire.providers.europe_pmc import EuropePmcProvider


def test_europe_pmc_resolves_and_fetches_jats(tmp_path):
    def handler(request: httpx.Request):
        if request.url.path.endswith("/search"):
            body = {"resultList": {"result": [{"pmid": "123", "pmcid": "PMC999", "doi": "10.1/x", "title": "T"}]}}
            return httpx.Response(200, json=body)
        if request.url.path.endswith("/PMC999/fullTextXML"):
            return httpx.Response(200, content=b"<article><front/><body><p>Hello</p></body></article>", headers={"content-type": "application/xml"})
        return httpx.Response(404)

    cache = DiskCache(tmp_path / "cache")
    http = CachedHttpClient(cache, "test", transport=httpx.MockTransport(handler), sleeper=lambda _: None)
    ctx = AcquisitionContext(ResolvedIds(pmid="123"), AcquisitionPolicy(), http, cache, Settings(cache_dir=tmp_path / "cache"), [])
    out = EuropePmcProvider().run(ctx)
    assert out.ids.pmcid == "PMC999"
    assert out.ids.doi == "10.1/x"
    assert len(out.artifacts) == 1
    assert out.artifacts[0].structured
