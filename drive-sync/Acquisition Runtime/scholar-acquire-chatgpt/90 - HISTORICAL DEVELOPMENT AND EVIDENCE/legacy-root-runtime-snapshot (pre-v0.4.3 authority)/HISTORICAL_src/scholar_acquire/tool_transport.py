from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import httpx

from .cache import DiskCache
from .errors import FetchRequired, NetworkError, RuntimeProtocolError
from .http import FetchResponse
from .models import ExternalFetchRequest


class ToolMediatedHttpClient:
    """HTTP-shaped client that never performs network I/O.

    Cache hits are returned normally. Cache misses become ExternalFetchRequest
    objects that the ChatGPT/tool layer must satisfy and ingest before rerunning.
    This lets the existing provider code remain deterministic and testable while
    moving network access outside the Python sandbox.
    """

    def __init__(self, cache: DiskCache, user_agent: str):
        self.cache = cache
        self.user_agent = user_agent
        self.current_provider: str | None = None

    def close(self) -> None:
        return None

    def set_provider(self, provider: str | None) -> None:
        self.current_provider = provider

    def get(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        cache_ttl_seconds: int | None = 86400,
        max_bytes: int | None = None,
    ) -> FetchResponse:
        full_url = str(httpx.URL(url).copy_merge_params(params or {}))
        cached = self.cache.get("GET", full_url)
        if cached:
            body = cached.object_path.read_bytes()
            if max_bytes is not None and len(body) > max_bytes:
                raise NetworkError(f"Cached response exceeded max_content_bytes ({len(body)} > {max_bytes})")
            return FetchResponse(
                cached.status_code,
                cached.headers,
                body,
                cached.url_redacted,
                True,
                cached.body_sha256,
                cached.object_path,
            )

        request_headers = {"User-Agent": self.user_agent}
        if headers:
            request_headers.update(headers)
        request = ExternalFetchRequest.build(
            url=full_url,
            redacted_url=self.cache.redact_url(full_url),
            headers=request_headers,
            max_bytes=max_bytes,
            cache_ttl_seconds=cache_ttl_seconds,
            provider=self.current_provider,
        )
        raise FetchRequired(request)

    def ingest_bytes(
        self,
        request: ExternalFetchRequest,
        content: bytes,
        *,
        status_code: int = 200,
        headers: Mapping[str, str] | None = None,
    ) -> FetchResponse:
        if request.method != "GET":
            raise RuntimeProtocolError(f"Unsupported method: {request.method}")
        if request.max_bytes is not None and len(content) > request.max_bytes:
            raise RuntimeProtocolError(
                f"Fetched content exceeds request max_bytes ({len(content)} > {request.max_bytes})"
            )
        response_headers = dict(headers or {})
        ttl = request.cache_ttl_seconds if 200 <= status_code < 300 else 300
        entry = self.cache.put("GET", request.url, status_code, response_headers, content, ttl)
        return FetchResponse(
            status_code=status_code,
            headers=response_headers,
            content=content,
            url=entry.url_redacted,
            from_cache=False,
            body_sha256=entry.body_sha256,
            object_path=entry.object_path,
        )

    def ingest_file(
        self,
        request: ExternalFetchRequest,
        path: Path,
        *,
        status_code: int = 200,
        headers: Mapping[str, str] | None = None,
    ) -> FetchResponse:
        return self.ingest_bytes(request, path.read_bytes(), status_code=status_code, headers=headers)
