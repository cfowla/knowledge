from __future__ import annotations

from urllib.parse import quote

from ..models import Artifact, ArtifactFormat, Attempt, ProviderOutcome, ResolvedIds, SourceVersion
from ..utils import extract_jats_article, s3_to_https, validate_pdf
from .base import AcquisitionContext


class PmcProvider:
    name = "pmc"
    idconv = "https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/"
    oai = "https://pmc.ncbi.nlm.nih.gov/api/oai/v1/mh/"
    s3_https = "https://pmc-oa-opendata.s3.amazonaws.com"

    def run(self, ctx: AcquisitionContext) -> ProviderOutcome:
        out = ProviderOutcome()
        ident = ctx.ids.versioned_pmcid or ctx.ids.pmcid or ctx.ids.pmid or ctx.ids.doi
        if not ident:
            ctx.add_attempt(Attempt(provider=self.name, action="id_converter", outcome="skipped", message="No identifier"))
            return out

        params = {"ids": ident, "format": "json", "versions": "yes", "showaiid": "yes"}
        if ctx.settings.contact_email:
            params.update({"tool": "scholar_acquire", "email": ctx.settings.contact_email})
        resp = ctx.http.get(self.idconv, params=params, cache_ttl_seconds=ctx.policy.api_cache_ttl_seconds)
        if resp.status_code != 200:
            ctx.add_attempt(Attempt(provider=self.name, action="id_converter", url=resp.url, outcome="miss", http_status=resp.status_code))
            return out
        records = resp.json().get("records") or []
        if not records or records[0].get("status") == "error":
            ctx.add_attempt(Attempt(provider=self.name, action="id_converter", url=resp.url, outcome="miss", http_status=200, message="Not in PMC"))
            return out
        rec = records[0]
        versions = rec.get("versions") or []
        current = None
        for v in versions:
            if v.get("current") in (True, "true", "yes", "Y", "1"):
                current = v
                break
        if current is None and versions:
            current = sorted(versions, key=lambda x: self._version_num(x.get("pmcid")), reverse=True)[0]
        versioned = (current or {}).get("pmcid")
        current_is_manuscript = bool((current or {}).get("mid"))
        pmcid = rec.get("pmcid") or ctx.ids.pmcid
        out.ids = ResolvedIds(
            pmid=rec.get("pmid") or ctx.ids.pmid,
            doi=rec.get("doi") or ctx.ids.doi,
            pmcid=pmcid,
            versioned_pmcid=versioned,
        )
        ctx.add_attempt(Attempt(provider=self.name, action="id_converter", url=resp.url, outcome="cached" if resp.from_cache else "success", http_status=200, metadata={"versioned_pmcid": versioned}))

        # Preferred 2026+ PMC dataset path: per-version metadata in the world-readable AWS bucket.
        if versioned:
            meta = self._fetch_aws_metadata(ctx, versioned)
            if meta:
                out.metadata.update(meta)
                if ctx.policy.want_structured and meta.get("xml_url"):
                    art = self._fetch_xml(ctx, s3_to_https(meta["xml_url"]), meta)
                    if art:
                        out.artifacts.append(art)
                if ctx.policy.want_pdf and meta.get("pdf_url"):
                    art = self._fetch_pdf(ctx, s3_to_https(meta["pdf_url"]), meta)
                    if art:
                        out.artifacts.append(art)

        # OAI-PMH remains the sanctioned fallback for reusable full-text XML.
        if ctx.policy.want_structured and not any(a.structured for a in out.artifacts) and pmcid:
            numeric = pmcid.upper().removeprefix("PMC").split(".", 1)[0]
            oai = ctx.http.get(
                self.oai,
                params={
                    "verb": "GetRecord",
                    "identifier": f"oai:pubmedcentral.nih.gov:{numeric}",
                    "metadataPrefix": "pmc",
                },
                cache_ttl_seconds=None,
                max_bytes=ctx.policy.max_content_bytes,
            )
            if oai.status_code == 200 and b"<error" not in oai.content[:4096]:
                try:
                    article = extract_jats_article(oai.content)
                    digest, path = ctx.cache.store_object(article)
                    out.artifacts.append(Artifact(
                        format=ArtifactFormat.JATS_XML,
                        provider=self.name,
                        source_url=oai.url,
                        local_path=path,
                        sha256=digest,
                        size_bytes=len(article),
                        media_type="application/xml",
                        version=SourceVersion.ACCEPTED if current_is_manuscript else SourceVersion.PUBLISHED,
                        structured=True,
                        metadata={"pmcid": pmcid, "route": "oai-pmh", "is_manuscript": current_is_manuscript},
                    ))
                    ctx.add_attempt(Attempt(provider=self.name, action="oai_fulltext_xml", url=oai.url, outcome="cached" if oai.from_cache else "success", http_status=200))
                except Exception as exc:
                    ctx.add_attempt(Attempt(provider=self.name, action="oai_fulltext_xml", url=oai.url, outcome="error", http_status=200, message=str(exc)))
            else:
                ctx.add_attempt(Attempt(provider=self.name, action="oai_fulltext_xml", url=oai.url, outcome="miss", http_status=oai.status_code))
        return out

    def _fetch_aws_metadata(self, ctx: AcquisitionContext, versioned: str) -> dict | None:
        candidates = [
            f"{self.s3_https}/metadata/{versioned}.json",
            f"{self.s3_https}/{versioned}/{versioned}.json",
        ]
        for url in candidates:
            resp = ctx.http.get(url, cache_ttl_seconds=ctx.policy.api_cache_ttl_seconds)
            if resp.status_code == 200:
                try:
                    data = resp.json()
                except Exception as exc:
                    ctx.add_attempt(Attempt(provider=self.name, action="aws_metadata", url=resp.url, outcome="error", http_status=200, message=str(exc)))
                    continue
                ctx.add_attempt(Attempt(provider=self.name, action="aws_metadata", url=resp.url, outcome="cached" if resp.from_cache else "success", http_status=200))
                return data
            ctx.add_attempt(Attempt(provider=self.name, action="aws_metadata", url=resp.url, outcome="miss", http_status=resp.status_code))
        return None

    def _fetch_xml(self, ctx: AcquisitionContext, url: str, meta: dict) -> Artifact | None:
        resp = ctx.http.get(url, cache_ttl_seconds=None, max_bytes=ctx.policy.max_content_bytes)
        if resp.status_code != 200:
            ctx.add_attempt(Attempt(provider=self.name, action="aws_xml", url=resp.url, outcome="miss", http_status=resp.status_code))
            return None
        try:
            article = extract_jats_article(resp.content)
        except Exception as exc:
            ctx.add_attempt(Attempt(provider=self.name, action="aws_xml", url=resp.url, outcome="error", http_status=200, message=str(exc)))
            return None
        digest, path = ctx.cache.store_object(article)
        ctx.add_attempt(Attempt(provider=self.name, action="aws_xml", url=resp.url, outcome="cached" if resp.from_cache else "success", http_status=200))
        return Artifact(
            format=ArtifactFormat.JATS_XML, provider=self.name, source_url=resp.url, local_path=path,
            sha256=digest, size_bytes=len(article), media_type="application/xml", structured=True,
            version=SourceVersion.ACCEPTED if meta.get("is_manuscript") else SourceVersion.PUBLISHED,
            license=meta.get("license_code"), metadata={"route": "pmc-aws", "is_manuscript": bool(meta.get("is_manuscript"))},
        )

    def _fetch_pdf(self, ctx: AcquisitionContext, url: str, meta: dict) -> Artifact | None:
        resp = ctx.http.get(url, cache_ttl_seconds=None, max_bytes=ctx.policy.max_content_bytes)
        if resp.status_code != 200:
            ctx.add_attempt(Attempt(provider=self.name, action="aws_pdf", url=resp.url, outcome="miss", http_status=resp.status_code))
            return None
        try:
            validate_pdf(resp.content, resp.headers.get("content-type"))
        except Exception as exc:
            ctx.add_attempt(Attempt(provider=self.name, action="aws_pdf", url=resp.url, outcome="error", http_status=200, message=str(exc)))
            return None
        digest, path = ctx.cache.store_object(resp.content)
        ctx.add_attempt(Attempt(provider=self.name, action="aws_pdf", url=resp.url, outcome="cached" if resp.from_cache else "success", http_status=200))
        return Artifact(
            format=ArtifactFormat.PDF, provider=self.name, source_url=resp.url, local_path=path,
            sha256=digest, size_bytes=len(resp.content), media_type="application/pdf", structured=False,
            version=SourceVersion.PUBLISHED, license=meta.get("license_code"), metadata={"route": "pmc-aws"},
        )

    @staticmethod
    def _version_num(pmcid: str | None) -> int:
        if not pmcid or "." not in pmcid:
            return 0
        try:
            return int(pmcid.rsplit(".", 1)[1])
        except ValueError:
            return 0
