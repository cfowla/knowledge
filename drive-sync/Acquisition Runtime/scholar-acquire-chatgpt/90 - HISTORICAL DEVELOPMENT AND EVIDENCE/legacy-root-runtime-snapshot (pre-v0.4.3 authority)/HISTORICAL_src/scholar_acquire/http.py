from __future__ import annotations

import json
import random
import time
from dataclasses import dataclass
from typing import Any, Callable, Protocol

import httpx

from .cache import DiskCache
from .errors import NetworkError, RateLimitError

_RETRY_STATUS = {429, 500, 502, 503, 504}


@dataclass
class FetchResponse:
    status_code: int
    headers: dict[str, str]
    content: bytes
    url: str
    from_cache: bool
    body_sha256: str
    object_path: Any

    def json(self) -> Any:
        return json.loads(self.content)

    @property
    def text(self) -> str:
        encoding = "utf-8"
        ctype = self.headers.get("content-type", "")
        if "charset=" in ctype:
            encoding = ctype.split("charset=", 1)[1].split(";", 1)[0].strip()
        return self.content.decode(encoding, errors="replace")


class HttpClient(Protocol):
    def close(self) -> None:
        ...

    def get(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        cache_ttl_seconds: int | None = 86400,
        max_bytes: int | None = None,
    ) -> FetchResponse:
        ...


class CachedHttpClient:
    def __init__(
        self,
        cache: DiskCache,
        user_agent: str,
        timeout_seconds: float = 30.0,
        max_retries: int = 4,
        transport: httpx.BaseTransport | None = None,
        sleeper: Callable[[float], None] = time.sleep,
    ):
        self.cache = cache
        self.max_retries = max_retries
        self.sleeper = sleeper
        self.client = httpx.Client(
            follow_redirects=True,
            timeout=timeout_seconds,
            headers={
                "User-Agent": user_agent,
                "Accept-Encoding": "gzip, deflate",
            },
            transport=transport,
        )

    def close(self) -> None:
        self.client.close()

    def __enter__(self) -> "CachedHttpClient":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    def get(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        cache_ttl_seconds: int | None = 86400,
        max_bytes: int | None = None,
    ) -> FetchResponse:
        request = self.client.build_request("GET", url, params=params, headers=headers)
        full_url = str(request.url)
        cached = self.cache.get("GET", full_url)
        if cached:
            body = cached.object_path.read_bytes()
            return FetchResponse(cached.status_code, cached.headers, body, cached.url_redacted, True, cached.body_sha256, cached.object_path)

        last_exc: Exception | None = None
        for attempt in range(self.max_retries + 1):
            try:
                response = self.client.send(request)
                content = response.content
                if max_bytes is not None and len(content) > max_bytes:
                    raise NetworkError(f"Response exceeded max_content_bytes ({len(content)} > {max_bytes})")
                if response.status_code in _RETRY_STATUS and attempt < self.max_retries:
                    delay = self._retry_delay(response, attempt)
                    self.sleeper(delay)
                    continue
                if response.status_code == 429:
                    raise RateLimitError(f"Rate limited by {response.url}")
                effective_ttl = cache_ttl_seconds if 200 <= response.status_code < 300 else 300
                entry = self.cache.put("GET", full_url, response.status_code, response.headers, content, effective_ttl)
                return FetchResponse(response.status_code, dict(response.headers), content, self.cache.redact_url(str(response.url)), False, entry.body_sha256, entry.object_path)
            except (httpx.TransportError, httpx.TimeoutException) as exc:
                last_exc = exc
                if attempt >= self.max_retries:
                    break
                self.sleeper(min(30.0, (2**attempt) + random.random()))
        raise NetworkError(f"GET failed after retries: {self.cache.redact_url(full_url)}") from last_exc

    @staticmethod
    def _retry_delay(response: httpx.Response, attempt: int) -> float:
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                return min(60.0, max(0.0, float(retry_after)))
            except ValueError:
                pass
        return min(30.0, (2**attempt) + random.random())
