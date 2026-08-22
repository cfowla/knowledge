import httpx

from scholar_acquire.cache import DiskCache
from scholar_acquire.http import CachedHttpClient


def test_retries_transient_status_then_succeeds(tmp_path):
    calls = {"n": 0}
    sleeps = []
    def handler(request):
        calls["n"] += 1
        if calls["n"] == 1:
            return httpx.Response(503, headers={"Retry-After": "0"})
        return httpx.Response(200, content=b"ok")
    client = CachedHttpClient(DiskCache(tmp_path), "test", max_retries=2, transport=httpx.MockTransport(handler), sleeper=sleeps.append)
    try:
        resp = client.get("https://example.test/x")
    finally:
        client.close()
    assert resp.status_code == 200
    assert calls["n"] == 2
    assert sleeps == [0.0]


def test_success_response_is_served_from_cache(tmp_path):
    calls = {"n": 0}
    def handler(request):
        calls["n"] += 1
        return httpx.Response(200, content=b"cached")
    client = CachedHttpClient(DiskCache(tmp_path), "test", transport=httpx.MockTransport(handler), sleeper=lambda _: None)
    try:
        first = client.get("https://example.test/x", cache_ttl_seconds=None)
        second = client.get("https://example.test/x", cache_ttl_seconds=None)
    finally:
        client.close()
    assert not first.from_cache
    assert second.from_cache
    assert calls["n"] == 1
