from __future__ import annotations

import json
import re
from pathlib import Path

from .cache import DiskCache
from .config import Settings
from .errors import FetchRequired
from .http import CachedHttpClient, HttpClient
from .integration import build_atom_sea_handoff
from .models import (
    AcquisitionPolicy,
    AcquisitionResult,
    AcquisitionSeed,
    ArticleIdentifier,
    Artifact,
    ArtifactFormat,
    Attempt,
    ResolvedIds,
)
from .providers.base import AcquisitionContext, Provider
from .providers.europe_pmc import EuropePmcProvider
from .providers.pmc import PmcProvider
from .providers.publisher import PublisherProvider
from .providers.repository import RepositoryProvider
from .providers.unpaywall import UnpaywallProvider
from .utils import link_or_copy


class AcquisitionOrchestrator:
    def __init__(
        self,
        settings: Settings | None = None,
        policy: AcquisitionPolicy | None = None,
        providers: list[Provider] | None = None,
        http: HttpClient | None = None,
    ):
        self.settings = settings or Settings()
        self.policy = policy or AcquisitionPolicy()
        self.cache = DiskCache(self.settings.cache_dir)
        self._owns_http = http is None
        self.http = http or CachedHttpClient(
            cache=self.cache,
            user_agent=self.settings.user_agent(),
            timeout_seconds=self.policy.timeout_seconds,
            max_retries=self.policy.max_retries,
        )
        self.providers = providers or [
            EuropePmcProvider(),
            PmcProvider(),
            UnpaywallProvider(),
            PublisherProvider(),
            RepositoryProvider(),
        ]

    def close(self) -> None:
        if self._owns_http:
            self.http.close()

    def fetch(
        self,
        identifier: str | ArticleIdentifier,
        output_dir: Path,
        *,
        seed: AcquisitionSeed | None = None,
    ) -> AcquisitionResult:
        ident = identifier if isinstance(identifier, ArticleIdentifier) else ArticleIdentifier.parse(identifier)
        seed = seed or AcquisitionSeed()
        ids = ResolvedIds()
        if ident.kind.value == "pmid":
            ids.pmid = ident.value
        elif ident.kind.value == "doi":
            ids.doi = ident.value
        else:
            ids.pmcid = ident.value.split(".", 1)[0]
            if "." in ident.value:
                ids.versioned_pmcid = ident.value
        ids.merge(seed.ids)

        attempts: list[Attempt] = []
        ctx = AcquisitionContext(
            ids=ids,
            policy=self.policy,
            http=self.http,
            cache=self.cache,
            settings=self.settings,
            attempts=attempts,
            publisher_locations=list(seed.publisher_locations),
            repository_locations=list(seed.repository_locations),
            metadata=dict(seed.metadata),
        )
        artifacts: list[Artifact] = list(seed.artifacts)

        if not self._satisfied(artifacts):
            for provider in self.providers:
                if hasattr(self.http, "set_provider"):
                    self.http.set_provider(getattr(provider, "name", provider.__class__.__name__))
                try:
                    outcome = provider.run(ctx)
                except FetchRequired:
                    raise
                except Exception as exc:
                    attempts.append(
                        Attempt(
                            provider=getattr(provider, "name", provider.__class__.__name__),
                            action="provider",
                            outcome="error",
                            message=f"{type(exc).__name__}: {exc}",
                        )
                    )
                    continue
                ctx.ids.merge(outcome.ids)
                ctx.publisher_locations.extend(outcome.publisher_locations)
                ctx.repository_locations.extend(outcome.repository_locations)
                ctx.metadata.update({k: v for k, v in outcome.metadata.items() if v is not None})
                artifacts = self._merge_artifacts(artifacts, outcome.artifacts)
                if self._satisfied(artifacts):
                    break
        if hasattr(self.http, "set_provider"):
            self.http.set_provider(None)

        workdir = output_dir / self._slug(ident, ctx.ids)
        workdir.mkdir(parents=True, exist_ok=True)
        artifacts = self._materialize(artifacts, workdir)
        result = AcquisitionResult(
            identifier=ident,
            resolved_ids=ctx.ids,
            artifacts=artifacts,
            attempts=attempts,
            metadata=ctx.metadata,
        )
        manifest_path = workdir / "manifest.json"
        result.manifest_path = manifest_path
        result.handoff = build_atom_sea_handoff(result, manifest_path)
        manifest_path.write_text(
            json.dumps(result.model_dump(mode="json"), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        return result

    def _satisfied(self, artifacts: list[Artifact]) -> bool:
        has_structured = any(a.structured for a in artifacts)
        has_pdf = any(a.format == ArtifactFormat.PDF for a in artifacts)
        return (not self.policy.want_structured or has_structured) and (not self.policy.want_pdf or has_pdf)

    @staticmethod
    def _merge_artifacts(existing: list[Artifact], new: list[Artifact]) -> list[Artifact]:
        seen = {a.sha256 for a in existing}
        for artifact in new:
            if artifact.sha256 not in seen:
                existing.append(artifact)
                seen.add(artifact.sha256)
        return existing

    def _materialize(self, artifacts: list[Artifact], workdir: Path) -> list[Artifact]:
        counters: dict[str, int] = {}
        for artifact in artifacts:
            ext = {
                ArtifactFormat.JATS_XML: ".xml",
                ArtifactFormat.PDF: ".pdf",
                ArtifactFormat.HTML: ".html",
                ArtifactFormat.TEXT: ".txt",
            }[artifact.format]
            key = f"{artifact.format.value}.{artifact.provider}"
            counters[key] = counters.get(key, 0) + 1
            suffix = "" if counters[key] == 1 else f".{counters[key]}"
            name = f"{artifact.format.value}.{artifact.provider}{suffix}{ext}"
            dest = workdir / name
            if artifact.local_path.resolve() != dest.resolve():
                link_or_copy(artifact.local_path, dest)
            artifact.local_path = dest
        return artifacts

    @staticmethod
    def _slug(ident: ArticleIdentifier, ids: ResolvedIds) -> str:
        base = ids.pmid or ids.pmcid or ids.doi or ident.value
        return re.sub(r"[^A-Za-z0-9._-]+", "_", base)[:120]
