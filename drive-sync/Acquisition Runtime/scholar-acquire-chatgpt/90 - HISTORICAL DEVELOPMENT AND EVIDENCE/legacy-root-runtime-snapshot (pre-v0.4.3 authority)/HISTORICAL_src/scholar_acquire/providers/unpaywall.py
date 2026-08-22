from __future__ import annotations

from ..models import Attempt, LocationCandidate, ProviderOutcome, SourceVersion
from .base import AcquisitionContext


class UnpaywallProvider:
    name = "unpaywall"
    base = "https://api.unpaywall.org/v2"

    def run(self, ctx: AcquisitionContext) -> ProviderOutcome:
        out = ProviderOutcome()
        if not ctx.ids.doi:
            ctx.add_attempt(Attempt(provider=self.name, action="oa_locations", outcome="skipped", message="DOI unavailable"))
            return out
        if not ctx.settings.contact_email:
            ctx.add_attempt(Attempt(provider=self.name, action="oa_locations", outcome="skipped", message="Set SCHOLAR_FETCH_EMAIL for Unpaywall"))
            return out
        resp = ctx.http.get(
            f"{self.base}/{ctx.ids.doi}",
            params={"email": ctx.settings.contact_email},
            cache_ttl_seconds=ctx.policy.api_cache_ttl_seconds,
        )
        if resp.status_code != 200:
            ctx.add_attempt(Attempt(provider=self.name, action="oa_locations", url=resp.url, outcome="miss", http_status=resp.status_code))
            return out
        data = resp.json()
        out.metadata = {k: data.get(k) for k in ("title", "publisher", "journal_name", "oa_status", "is_oa", "published_date") if data.get(k) is not None}
        for loc in data.get("oa_locations") or []:
            candidate = self._candidate(loc)
            if not candidate:
                continue
            if candidate.host_type == "publisher":
                out.publisher_locations.append(candidate)
            elif candidate.host_type == "repository":
                out.repository_locations.append(candidate)
        out.publisher_locations.sort(key=self._rank)
        out.repository_locations.sort(key=self._rank)
        ctx.add_attempt(Attempt(provider=self.name, action="oa_locations", url=resp.url, outcome="cached" if resp.from_cache else "success", http_status=200, metadata={"publisher_locations": len(out.publisher_locations), "repository_locations": len(out.repository_locations)}))
        return out

    def _candidate(self, loc: dict) -> LocationCandidate | None:
        url = loc.get("url") or loc.get("url_for_pdf") or loc.get("url_for_landing_page")
        if not url:
            return None
        host_type = loc.get("host_type") if loc.get("host_type") in {"publisher", "repository"} else "unknown"
        return LocationCandidate(
            url=url,
            landing_page_url=loc.get("url_for_landing_page"),
            pdf_url=loc.get("url_for_pdf"),
            host_type=host_type,
            version=loc.get("version") or SourceVersion.UNKNOWN,
            license=loc.get("license"),
            source_name=loc.get("repository_institution"),
            discovered_by=self.name,
        )

    @staticmethod
    def _rank(loc: LocationCandidate) -> tuple[int, int]:
        version_rank = {SourceVersion.PUBLISHED: 0, SourceVersion.ACCEPTED: 1, SourceVersion.SUBMITTED: 2, SourceVersion.UNKNOWN: 3}
        return (version_rank[loc.version], 0 if loc.pdf_url else 1)
