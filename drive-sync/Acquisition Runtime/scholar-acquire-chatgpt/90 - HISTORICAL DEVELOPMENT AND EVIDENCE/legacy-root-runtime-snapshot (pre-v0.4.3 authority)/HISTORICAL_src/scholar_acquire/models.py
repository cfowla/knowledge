from __future__ import annotations

import hashlib
import re
import secrets
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .errors import IdentifierError

_DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.I)
_PMID_RE = re.compile(r"^\d{1,12}$")
_PMCID_RE = re.compile(r"^PMC\d+(?:\.\d+)?$", re.I)


class IdentifierKind(str, Enum):
    PMID = "pmid"
    DOI = "doi"
    PMCID = "pmcid"


class ArticleIdentifier(BaseModel):
    model_config = ConfigDict(frozen=True)
    kind: IdentifierKind
    value: str

    @classmethod
    def parse(cls, raw: str) -> "ArticleIdentifier":
        value = raw.strip()
        low = value.lower()
        for prefix in ("https://doi.org/", "http://doi.org/", "http://dx.doi.org/", "https://dx.doi.org/"):
            if low.startswith(prefix):
                value = value[len(prefix):]
                low = value.lower()
                break
        if low.startswith("doi:"):
            value = value[4:].strip()
        elif low.startswith("pmid:"):
            value = value[5:].strip()
            if not _PMID_RE.fullmatch(value):
                raise IdentifierError(f"Invalid PMID: {raw}")
            return cls(kind=IdentifierKind.PMID, value=value)
        elif low.startswith("pmcid:"):
            value = value[6:].strip()
            if not _PMCID_RE.fullmatch(value):
                raise IdentifierError(f"Invalid PMCID: {raw}")
            return cls(kind=IdentifierKind.PMCID, value=value.upper())

        value = value.rstrip(".,;)")
        if _PMID_RE.fullmatch(value):
            return cls(kind=IdentifierKind.PMID, value=value)
        if _PMCID_RE.fullmatch(value):
            return cls(kind=IdentifierKind.PMCID, value=value.upper())
        if _DOI_RE.fullmatch(value):
            return cls(kind=IdentifierKind.DOI, value=value.lower())
        raise IdentifierError(f"Expected a PMID, PMCID, or DOI; got: {raw}")


class SourceVersion(str, Enum):
    PUBLISHED = "publishedVersion"
    ACCEPTED = "acceptedVersion"
    SUBMITTED = "submittedVersion"
    UNKNOWN = "unknown"


class ArtifactFormat(str, Enum):
    JATS_XML = "jats_xml"
    PDF = "pdf"
    HTML = "html"
    TEXT = "text"


class ResolvedIds(BaseModel):
    pmid: str | None = None
    doi: str | None = None
    pmcid: str | None = None
    versioned_pmcid: str | None = None

    def merge(self, other: "ResolvedIds") -> None:
        for field in ("pmid", "doi", "pmcid", "versioned_pmcid"):
            value = getattr(other, field)
            if value and not getattr(self, field):
                setattr(self, field, value)


class LocationCandidate(BaseModel):
    url: str
    landing_page_url: str | None = None
    pdf_url: str | None = None
    host_type: Literal["publisher", "repository", "unknown"] = "unknown"
    version: SourceVersion = SourceVersion.UNKNOWN
    license: str | None = None
    source_name: str | None = None
    discovered_by: str

    @field_validator("version", mode="before")
    @classmethod
    def normalize_version(cls, v: Any) -> SourceVersion:
        if v in (None, ""):
            return SourceVersion.UNKNOWN
        try:
            return SourceVersion(v)
        except ValueError:
            return SourceVersion.UNKNOWN


class Artifact(BaseModel):
    format: ArtifactFormat
    provider: str
    source_url: str
    local_path: Path
    sha256: str
    size_bytes: int
    media_type: str | None = None
    version: SourceVersion = SourceVersion.UNKNOWN
    license: str | None = None
    structured: bool = False
    retrieved_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: dict[str, Any] = Field(default_factory=dict)


class Attempt(BaseModel):
    provider: str
    action: str
    url: str | None = None
    outcome: Literal["success", "miss", "error", "skipped", "cached"]
    http_status: int | None = None
    message: str | None = None
    elapsed_ms: int | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
    at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class AcquisitionPolicy(BaseModel):
    want_structured: bool = True
    want_pdf: bool = True
    allow_submitted: bool = False
    max_content_bytes: int = 100 * 1024 * 1024
    api_cache_ttl_seconds: int = 24 * 60 * 60
    landing_cache_ttl_seconds: int = 60 * 60
    max_retries: int = 4
    timeout_seconds: float = 30.0


class ProviderOutcome(BaseModel):
    artifacts: list[Artifact] = Field(default_factory=list)
    ids: ResolvedIds = Field(default_factory=ResolvedIds)
    publisher_locations: list[LocationCandidate] = Field(default_factory=list)
    repository_locations: list[LocationCandidate] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class AcquisitionSeed(BaseModel):
    """Tool- or user-supplied facts/artifacts available before provider execution."""

    ids: ResolvedIds = Field(default_factory=ResolvedIds)
    artifacts: list[Artifact] = Field(default_factory=list)
    publisher_locations: list[LocationCandidate] = Field(default_factory=list)
    repository_locations: list[LocationCandidate] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class AtomSeaHandoff(BaseModel):
    schema_version: str = "1"
    identifier: ArticleIdentifier
    resolved_ids: ResolvedIds
    preferred_structured_path: Path | None = None
    preferred_pdf_path: Path | None = None
    structured_sha256: str | None = None
    pdf_sha256: str | None = None
    manifest_path: Path | None = None


class AcquisitionResult(BaseModel):
    schema_version: str = "1"
    identifier: ArticleIdentifier
    resolved_ids: ResolvedIds
    artifacts: list[Artifact]
    attempts: list[Attempt]
    metadata: dict[str, Any] = Field(default_factory=dict)
    manifest_path: Path | None = None
    handoff: AtomSeaHandoff | None = None

    @property
    def has_structured(self) -> bool:
        return any(a.structured for a in self.artifacts)

    @property
    def has_pdf(self) -> bool:
        return any(a.format == ArtifactFormat.PDF for a in self.artifacts)


class ExternalFetchRequest(BaseModel):
    """A deterministic GET request for an external ChatGPT retrieval tool to satisfy."""

    schema_version: str = "1"
    request_id: str
    method: Literal["GET"] = "GET"
    url: str
    redacted_url: str
    headers: dict[str, str] = Field(default_factory=dict)
    max_bytes: int | None = None
    cache_ttl_seconds: int | None = None
    provider: str | None = None
    ingest_token: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @classmethod
    def build(
        cls,
        *,
        url: str,
        redacted_url: str,
        headers: dict[str, str] | None = None,
        max_bytes: int | None = None,
        cache_ttl_seconds: int | None = None,
        provider: str | None = None,
        ingest_token: str | None = None,
    ) -> "ExternalFetchRequest":
        canonical_headers = {k.lower(): v for k, v in sorted((headers or {}).items())}
        material = f"GET\n{url}\n{canonical_headers}\n{max_bytes}".encode()
        request_id = hashlib.sha256(material).hexdigest()[:24]
        return cls(
            request_id=request_id,
            url=url,
            redacted_url=redacted_url,
            headers=headers or {},
            max_bytes=max_bytes,
            cache_ttl_seconds=cache_ttl_seconds,
            provider=provider,
            ingest_token=ingest_token or secrets.token_urlsafe(32),
        )


class ExternalFetchRecord(BaseModel):
    request_id: str
    redacted_url: str
    provider: str | None = None
    status_code: int
    body_sha256: str
    size_bytes: int
    content_type: str | None = None
    cache_object_path: Path | None = None
    ingested_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class RuntimeState(str, Enum):
    READY = "ready"
    NEEDS_FETCH = "needs_fetch"
    SUCCESS = "success"
    EXHAUSTED = "exhausted"
    BLOCKED = "blocked"
    FAILED = "failed"
    COMPLETE = "complete"  # legacy 0.2.x terminal success


class RuntimeFailureCode(str, Enum):
    RUNTIME_UNAVAILABLE = "RUNTIME_UNAVAILABLE"
    RUNTIME_INTEGRITY_MISMATCH = "RUNTIME_INTEGRITY_MISMATCH"
    EXTERNAL_FETCH_BLOCKED = "EXTERNAL_FETCH_BLOCKED"
    RESPONSE_NOT_MATERIALIZABLE = "RESPONSE_NOT_MATERIALIZABLE"
    INDEX_PROPAGATION_PENDING = "INDEX_PROPAGATION_PENDING"
    INVALID_RESPONSE = "INVALID_RESPONSE"
    TOOL_FAILURE = "TOOL_FAILURE"
    RUNTIME_PROTOCOL_ERROR = "RUNTIME_PROTOCOL_ERROR"
    PROVIDER_ERROR = "PROVIDER_ERROR"
    UNKNOWN = "UNKNOWN"


class RuntimeEvent(BaseModel):
    schema_version: str = "1"
    seq: int
    event: str
    session_id: str
    request_id: str | None = None
    provider: str | None = None
    data: dict[str, Any] = Field(default_factory=dict)
    at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class RuntimeReceipt(BaseModel):
    schema_version: str = "1"
    run_id: str
    session_id: str
    identifier: ArticleIdentifier
    package: str = "scholar-acquire-chatgpt"
    version: str
    runtime_class: str = "ChatGptAcquisitionRuntime"
    imported_from: Path
    package_tree_sha256: str
    expected_package_tree_sha256: str
    integrity_verified: bool
    build_manifest_path: Path
    python_version: str
    platform: str
    execution_mode: Literal["tool-mediated"] = "tool-mediated"
    network_in_python: bool = False
    started_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class RuntimeTerminalOutcome(BaseModel):
    schema_version: str = "1"
    state: RuntimeState
    reason_code: RuntimeFailureCode | None = None
    message: str | None = None
    provider_policy: list[str] = Field(default_factory=list)
    provider_attempts: list[Attempt] = Field(default_factory=list)
    provider_exhaustion_confirmed: bool = False
    artifact_sha256: list[str] = Field(default_factory=list)
    pending_request_id: str | None = None
    at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ChatGptRuntimeSession(BaseModel):
    schema_version: str = "2"
    session_id: str
    identifier: ArticleIdentifier
    session_dir: Path
    output_dir: Path
    cache_dir: Path
    policy: AcquisitionPolicy = Field(default_factory=AcquisitionPolicy)
    seed: AcquisitionSeed = Field(default_factory=AcquisitionSeed)
    state: RuntimeState = RuntimeState.READY
    pending_request: ExternalFetchRequest | None = None
    fetch_history: list[ExternalFetchRecord] = Field(default_factory=list)
    result_manifest: Path | None = None
    error: str | None = None
    event_seq: int = 0
    receipt_path: Path | None = None
    terminal_outcome: RuntimeTerminalOutcome | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class RuntimeStep(BaseModel):
    state: RuntimeState
    session_path: Path
    pending_request: ExternalFetchRequest | None = None
    result: AcquisitionResult | None = None
    terminal_outcome: RuntimeTerminalOutcome | None = None
    message: str | None = None
