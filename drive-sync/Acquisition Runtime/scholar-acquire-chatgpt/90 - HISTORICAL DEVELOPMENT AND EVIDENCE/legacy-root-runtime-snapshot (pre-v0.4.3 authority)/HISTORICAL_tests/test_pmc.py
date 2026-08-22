import httpx

from scholar_acquire.cache import DiskCache
from scholar_acquire.config import Settings
from scholar_acquire.http import CachedHttpClient
from scholar_acquire.models import AcquisitionPolicy, ArtifactFormat, ResolvedIds
from scholar_acquire.providers.base import AcquisitionContext
from scholar_acquire.providers.pmc import PmcProvider


PDF = b"%PDF-1.4\n" + b"0" * 1200 + b"\n%%EOF"


def test_pmc_uses_versioned_aws_metadata(tmp_path):
    def handler(request: httpx.Request):
        p = request.url.path
        if "idconv" in p:
            return httpx.Response(200, json={"records": [{"pmid": "123", "pmcid": "PMC999", "doi": "10.1/x", "versions": [{"pmcid": "PMC999.2", "current": True}]}]})
        if p == "/metadata/PMC999.2.json":
            return httpx.Response(200, json={
                "pmcid": "PMC999", "version": 2, "license_code": "CC BY", "is_manuscript": False,
                "xml_url": "https://files.test/PMC999.2.xml", "pdf_url": "https://files.test/PMC999.2.pdf",
            })
        if p.endswith("PMC999.2.xml"):
            return httpx.Response(200, content=b"<article><front/><body><p>x</p></body></article>")
        if p.endswith("PMC999.2.pdf"):
            return httpx.Response(200, content=PDF, headers={"content-type": "application/pdf"})
        return httpx.Response(404)

    cache = DiskCache(tmp_path / "cache")
    http = CachedHttpClient(cache, "test", transport=httpx.MockTransport(handler), sleeper=lambda _: None)
    ctx = AcquisitionContext(ResolvedIds(pmid="123"), AcquisitionPolicy(), http, cache, Settings(cache_dir=tmp_path / "cache"), [])
    out = PmcProvider().run(ctx)
    assert out.ids.versioned_pmcid == "PMC999.2"
    assert {a.format for a in out.artifacts} == {ArtifactFormat.JATS_XML, ArtifactFormat.PDF}
