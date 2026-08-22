from __future__ import annotations

from urllib.parse import quote

from ..models import Artifact, ArtifactFormat, Attempt, LocationCandidate, ProviderOutcome, SourceVersion
from ..utils import assert_allowed_url, looks_like_fulltext_html, pdf_links_from_html, validate_pdf
from .base import AcquisitionContext


class PublisherProvider:
    name = "publisher_oa"

    def run(self, ctx: AcquisitionContext) -> ProviderOutcome:
        out = ProviderOutcome()
        candidates = list(ctx.publisher_locations)
        if not candidates and ctx.ids.doi:
            candidates.append(LocationCandidate(
                url=f"https://doi.org/{quote(ctx.ids.doi, safe='/')}",
                landing_page_url=f"https://doi.org/{quote(ctx.ids.doi, safe='/')}",
                host_type="publisher",
                version=SourceVersion.PUBLISHED,
                discovered_by="doi_resolver",
            ))
        if not candidates:
            ctx.add_attempt(Attempt(provider=self.name, action="publisher_fulltext", outcome="skipped", message="No DOI/publisher location"))
            return out
        for candidate in candidates:
            if ctx.policy.want_pdf and candidate.pdf_url:
                art = self._try_pdf(ctx, candidate.pdf_url, candidate)
                if art:
                    out.artifacts.append(art)
                    if not ctx.policy.want_structured:
                        return out
            landing = candidate.landing_page_url or candidate.url
            art_html, art_pdf = self._inspect_landing(ctx, landing, candidate)
            if art_html:
                out.artifacts.append(art_html)
            if art_pdf:
                out.artifacts.append(art_pdf)
            if self._satisfied(ctx, out):
                return out
        return out

    def _try_pdf(self, ctx: AcquisitionContext, url: str, candidate: LocationCandidate) -> Artifact | None:
        assert_allowed_url(url)
        resp = ctx.http.get(url, cache_ttl_seconds=None, max_bytes=ctx.policy.max_content_bytes, headers={"Accept": "application/pdf,*/*;q=0.8"})
        if resp.status_code != 200:
            ctx.add_attempt(Attempt(provider=self.name, action="pdf", url=resp.url, outcome="miss", http_status=resp.status_code))
            return None
        try:
            validate_pdf(resp.content, resp.headers.get("content-type"))
        except Exception as exc:
            ctx.add_attempt(Attempt(provider=self.name, action="pdf", url=resp.url, outcome="error", http_status=200, message=str(exc)))
            return None
        digest, path = ctx.cache.store_object(resp.content)
        ctx.add_attempt(Attempt(provider=self.name, action="pdf", url=resp.url, outcome="cached" if resp.from_cache else "success", http_status=200))
        return Artifact(format=ArtifactFormat.PDF, provider=self.name, source_url=resp.url, local_path=path, sha256=digest, size_bytes=len(resp.content), media_type="application/pdf", version=candidate.version, license=candidate.license)

    def _inspect_landing(self, ctx: AcquisitionContext, url: str, candidate: LocationCandidate) -> tuple[Artifact | None, Artifact | None]:
        assert_allowed_url(url)
        resp = ctx.http.get(url, cache_ttl_seconds=ctx.policy.landing_cache_ttl_seconds, max_bytes=ctx.policy.max_content_bytes, headers={"Accept": "text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.5"})
        if resp.status_code != 200:
            ctx.add_attempt(Attempt(provider=self.name, action="landing", url=resp.url, outcome="miss", http_status=resp.status_code))
            return None, None
        ctype = resp.headers.get("content-type")
        if ctx.policy.want_pdf:
            try:
                validate_pdf(resp.content, ctype)
                digest, path = ctx.cache.store_object(resp.content)
                art = Artifact(format=ArtifactFormat.PDF, provider=self.name, source_url=resp.url, local_path=path, sha256=digest, size_bytes=len(resp.content), media_type="application/pdf", version=candidate.version, license=candidate.license)
                ctx.add_attempt(Attempt(provider=self.name, action="landing_pdf", url=resp.url, outcome="cached" if resp.from_cache else "success", http_status=200))
                return None, art
            except Exception:
                pass
        html_art = None
        if ctx.policy.want_structured and looks_like_fulltext_html(resp.content, ctype):
            digest, path = ctx.cache.store_object(resp.content)
            html_art = Artifact(format=ArtifactFormat.HTML, provider=self.name, source_url=resp.url, local_path=path, sha256=digest, size_bytes=len(resp.content), media_type=ctype or "text/html", version=candidate.version, license=candidate.license, structured=True)
            ctx.add_attempt(Attempt(provider=self.name, action="html_fulltext", url=resp.url, outcome="cached" if resp.from_cache else "success", http_status=200))
        pdf_art = None
        if ctx.policy.want_pdf:
            for pdf_url in pdf_links_from_html(str(resp.url), resp.content)[:8]:
                pdf_art = self._try_pdf(ctx, pdf_url, candidate)
                if pdf_art:
                    break
        if not html_art and not pdf_art:
            ctx.add_attempt(Attempt(provider=self.name, action="landing", url=resp.url, outcome="miss", http_status=200, message="No openly retrievable full text detected"))
        return html_art, pdf_art

    @staticmethod
    def _satisfied(ctx: AcquisitionContext, out: ProviderOutcome) -> bool:
        has_pdf = any(a.format == ArtifactFormat.PDF for a in out.artifacts)
        has_structured = any(a.structured for a in out.artifacts)
        return (not ctx.policy.want_pdf or has_pdf) and (not ctx.policy.want_structured or has_structured)
