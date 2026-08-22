from __future__ import annotations

from urllib.parse import quote

from ..models import Artifact, ArtifactFormat, Attempt, LocationCandidate, ProviderOutcome, SourceVersion
from ..utils import assert_allowed_url, pdf_links_from_html, validate_pdf
from .base import AcquisitionContext


class RepositoryProvider:
    name = "repository"
    openalex = "https://api.openalex.org/works"

    def run(self, ctx: AcquisitionContext) -> ProviderOutcome:
        out = ProviderOutcome()
        candidates = [c for c in ctx.repository_locations if self._eligible(ctx, c)]
        candidates.extend(self._openalex_locations(ctx))
        candidates = self._dedupe_sort(ctx, candidates)
        if not candidates:
            ctx.add_attempt(Attempt(provider=self.name, action="repository_fulltext", outcome="miss", message="No eligible accepted/published repository copy"))
            return out
        for candidate in candidates:
            if candidate.pdf_url:
                art = self._try_pdf(ctx, candidate.pdf_url, candidate)
                if art:
                    out.artifacts.append(art)
                    return out
            landing = candidate.landing_page_url or candidate.url
            if landing:
                art = self._inspect_landing(ctx, landing, candidate)
                if art:
                    out.artifacts.append(art)
                    return out
        return out

    def _openalex_locations(self, ctx: AcquisitionContext) -> list[LocationCandidate]:
        ident = None
        if ctx.ids.doi:
            ident = f"doi:{ctx.ids.doi}"
        elif ctx.ids.pmid:
            ident = f"pmid:{ctx.ids.pmid}"
        if not ident:
            return []
        path_ident = quote(ident, safe=":")
        params = {}
        if ctx.settings.openalex_api_key:
            params["api_key"] = ctx.settings.openalex_api_key
        resp = ctx.http.get(f"{self.openalex}/{path_ident}", params=params, cache_ttl_seconds=ctx.policy.api_cache_ttl_seconds)
        if resp.status_code != 200:
            ctx.add_attempt(Attempt(provider=self.name, action="openalex_locations", url=resp.url, outcome="miss", http_status=resp.status_code))
            return []
        data = resp.json()
        found: list[LocationCandidate] = []
        for loc in data.get("locations") or []:
            source = loc.get("source") or {}
            if source.get("type") != "repository" or not loc.get("is_oa"):
                continue
            url = loc.get("pdf_url") or loc.get("landing_page_url")
            if not url:
                continue
            candidate = LocationCandidate(
                url=url,
                landing_page_url=loc.get("landing_page_url"),
                pdf_url=loc.get("pdf_url"),
                host_type="repository",
                version=loc.get("version") or SourceVersion.UNKNOWN,
                license=loc.get("license"),
                source_name=source.get("display_name"),
                discovered_by="openalex",
            )
            if self._eligible(ctx, candidate):
                found.append(candidate)
        ctx.add_attempt(Attempt(provider=self.name, action="openalex_locations", url=resp.url, outcome="cached" if resp.from_cache else "success", http_status=200, metadata={"eligible_locations": len(found)}))
        return found

    def _eligible(self, ctx: AcquisitionContext, c: LocationCandidate) -> bool:
        name = (c.source_name or "").lower()
        if "pubmed central" in name or "europe pmc" in name:
            return False
        if c.version == SourceVersion.SUBMITTED and not ctx.policy.allow_submitted:
            return False
        if c.version == SourceVersion.UNKNOWN and not ctx.policy.allow_submitted:
            # Keep unknown institutional repositories as a last resort; don't treat named preprint servers as accepted manuscripts.
            if any(x in name for x in ("arxiv", "biorxiv", "medrxiv", "research square", "ssrn")):
                return False
        return True

    def _try_pdf(self, ctx: AcquisitionContext, url: str, candidate: LocationCandidate) -> Artifact | None:
        assert_allowed_url(url)
        resp = ctx.http.get(url, cache_ttl_seconds=None, max_bytes=ctx.policy.max_content_bytes, headers={"Accept": "application/pdf,*/*;q=0.8"})
        if resp.status_code != 200:
            ctx.add_attempt(Attempt(provider=self.name, action="repository_pdf", url=resp.url, outcome="miss", http_status=resp.status_code))
            return None
        try:
            validate_pdf(resp.content, resp.headers.get("content-type"))
        except Exception as exc:
            ctx.add_attempt(Attempt(provider=self.name, action="repository_pdf", url=resp.url, outcome="error", http_status=200, message=str(exc)))
            return None
        digest, path = ctx.cache.store_object(resp.content)
        ctx.add_attempt(Attempt(provider=self.name, action="repository_pdf", url=resp.url, outcome="cached" if resp.from_cache else "success", http_status=200))
        return Artifact(format=ArtifactFormat.PDF, provider=self.name, source_url=resp.url, local_path=path, sha256=digest, size_bytes=len(resp.content), media_type="application/pdf", version=candidate.version, license=candidate.license, metadata={"repository": candidate.source_name, "discovered_by": candidate.discovered_by})

    def _inspect_landing(self, ctx: AcquisitionContext, url: str, candidate: LocationCandidate) -> Artifact | None:
        assert_allowed_url(url)
        resp = ctx.http.get(url, cache_ttl_seconds=ctx.policy.landing_cache_ttl_seconds, max_bytes=ctx.policy.max_content_bytes)
        if resp.status_code != 200:
            ctx.add_attempt(Attempt(provider=self.name, action="repository_landing", url=resp.url, outcome="miss", http_status=resp.status_code))
            return None
        for pdf_url in pdf_links_from_html(str(resp.url), resp.content)[:12]:
            art = self._try_pdf(ctx, pdf_url, candidate)
            if art:
                return art
        ctx.add_attempt(Attempt(provider=self.name, action="repository_landing", url=resp.url, outcome="miss", http_status=200, message="No PDF link discovered"))
        return None

    def _dedupe_sort(self, ctx: AcquisitionContext, candidates: list[LocationCandidate]) -> list[LocationCandidate]:
        seen: set[str] = set()
        out: list[LocationCandidate] = []
        for c in candidates:
            key = c.pdf_url or c.url
            if key not in seen and self._eligible(ctx, c):
                seen.add(key)
                out.append(c)
        rank = {SourceVersion.PUBLISHED: 0, SourceVersion.ACCEPTED: 1, SourceVersion.UNKNOWN: 2, SourceVersion.SUBMITTED: 3}
        out.sort(key=lambda c: (rank[c.version], 0 if c.pdf_url else 1))
        return out
