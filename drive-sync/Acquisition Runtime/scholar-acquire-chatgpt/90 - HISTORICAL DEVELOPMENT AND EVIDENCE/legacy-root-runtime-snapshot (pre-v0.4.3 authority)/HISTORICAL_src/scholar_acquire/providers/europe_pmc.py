from __future__ import annotations

import time

from ..models import Artifact, ArtifactFormat, Attempt, ProviderOutcome, ResolvedIds, SourceVersion
from ..utils import extract_jats_article
from .base import AcquisitionContext


class EuropePmcProvider:
    name = "europe_pmc"
    base = "https://www.ebi.ac.uk/europepmc/webservices/rest"

    def run(self, ctx: AcquisitionContext) -> ProviderOutcome:
        out = ProviderOutcome()
        query = None
        if ctx.ids.pmid:
            query = f"EXT_ID:{ctx.ids.pmid} AND SRC:MED"
        elif ctx.ids.doi:
            query = f'DOI:"{ctx.ids.doi}"'
        elif ctx.ids.pmcid:
            query = f"PMCID:{ctx.ids.pmcid}"
        if not query:
            ctx.add_attempt(Attempt(provider=self.name, action="metadata", outcome="skipped", message="No supported identifier"))
            return out

        started = time.perf_counter()
        resp = ctx.http.get(
            f"{self.base}/search",
            params={"query": query, "format": "json", "resultType": "core", "pageSize": 1},
            cache_ttl_seconds=ctx.policy.api_cache_ttl_seconds,
        )
        elapsed = int((time.perf_counter() - started) * 1000)
        if resp.status_code != 200:
            ctx.add_attempt(Attempt(provider=self.name, action="metadata", url=resp.url, outcome="miss", http_status=resp.status_code, elapsed_ms=elapsed))
            return out
        data = resp.json()
        results = (data.get("resultList") or {}).get("result") or []
        if not results:
            ctx.add_attempt(Attempt(provider=self.name, action="metadata", url=resp.url, outcome="miss", http_status=200, elapsed_ms=elapsed, message="No Europe PMC match"))
            return out
        row = results[0]
        out.ids = ResolvedIds(
            pmid=row.get("pmid") or ctx.ids.pmid,
            doi=(row.get("doi") or ctx.ids.doi or None),
            pmcid=(row.get("pmcid") or ctx.ids.pmcid or None),
        )
        out.metadata = {k: row.get(k) for k in ("title", "journalTitle", "pubYear", "isOpenAccess", "inEPMC") if row.get(k) is not None}
        ctx.add_attempt(Attempt(provider=self.name, action="metadata", url=resp.url, outcome="cached" if resp.from_cache else "success", http_status=200, elapsed_ms=elapsed))

        pmcid = out.ids.pmcid
        if not (ctx.policy.want_structured and pmcid):
            return out
        full = ctx.http.get(
            f"{self.base}/{pmcid}/fullTextXML",
            cache_ttl_seconds=None,
            max_bytes=ctx.policy.max_content_bytes,
            headers={"Accept": "application/xml,text/xml;q=0.9,*/*;q=0.1"},
        )
        if full.status_code != 200 or not full.content:
            ctx.add_attempt(Attempt(provider=self.name, action="fulltext_xml", url=full.url, outcome="miss", http_status=full.status_code))
            return out
        try:
            article = extract_jats_article(full.content)
        except Exception as exc:
            ctx.add_attempt(Attempt(provider=self.name, action="fulltext_xml", url=full.url, outcome="error", http_status=200, message=str(exc)))
            return out
        digest, path = ctx.cache.store_object(article)
        out.artifacts.append(
            Artifact(
                format=ArtifactFormat.JATS_XML,
                provider=self.name,
                source_url=full.url,
                local_path=path,
                sha256=digest,
                size_bytes=len(article),
                media_type="application/xml",
                version=SourceVersion.PUBLISHED,
                structured=True,
                metadata={"pmcid": pmcid},
            )
        )
        ctx.add_attempt(Attempt(provider=self.name, action="fulltext_xml", url=full.url, outcome="cached" if full.from_cache else "success", http_status=200))
        return out
