from scholar_acquire.cache import DiskCache


def test_cache_stores_content_addressed_object(tmp_path):
    cache = DiskCache(tmp_path)
    e = cache.put("GET", "https://example.org/x?email=a@example.org", 200, {"content-type": "text/plain"}, b"abc", None)
    assert e.object_path.read_bytes() == b"abc"
    got = cache.get("GET", "https://example.org/x?email=a@example.org")
    assert got is not None
    assert "a%40example.org" not in got.url_redacted
    assert "REDACTED" in got.url_redacted
