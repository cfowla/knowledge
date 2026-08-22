from __future__ import annotations

import hashlib
import json
import sqlite3
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

_SENSITIVE_QUERY_KEYS = {"email", "api_key", "apikey", "key", "token", "access_token"}


@dataclass(frozen=True)
class CacheEntry:
    key: str
    status_code: int
    headers: dict[str, str]
    body_sha256: str
    object_path: Path
    retrieved_at: float
    expires_at: float | None
    url_redacted: str

    @property
    def fresh(self) -> bool:
        return self.expires_at is None or self.expires_at > time.time()


class DiskCache:
    def __init__(self, root: Path):
        self.root = root
        self.objects = root / "objects" / "sha256"
        self.db_path = root / "index.sqlite3"
        self.objects.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS responses (
                    cache_key TEXT PRIMARY KEY,
                    method TEXT NOT NULL,
                    url_redacted TEXT NOT NULL,
                    status_code INTEGER NOT NULL,
                    headers_json TEXT NOT NULL,
                    body_sha256 TEXT NOT NULL,
                    retrieved_at REAL NOT NULL,
                    expires_at REAL
                )
                """
            )

    @staticmethod
    def redact_url(url: str) -> str:
        parts = urlsplit(url)
        query = []
        for key, value in parse_qsl(parts.query, keep_blank_values=True):
            query.append((key, "REDACTED" if key.lower() in _SENSITIVE_QUERY_KEYS else value))
        return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))

    @staticmethod
    def request_key(method: str, url: str) -> str:
        return hashlib.sha256(f"{method.upper()}\n{url}".encode()).hexdigest()

    def store_object(self, body: bytes) -> tuple[str, Path]:
        digest = hashlib.sha256(body).hexdigest()
        path = self.objects / digest[:2] / digest
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            tmp = path.with_suffix(".tmp")
            tmp.write_bytes(body)
            tmp.replace(path)
        return digest, path

    def get(self, method: str, url: str) -> CacheEntry | None:
        key = self.request_key(method, url)
        with self._connect() as conn:
            row = conn.execute("SELECT * FROM responses WHERE cache_key = ?", (key,)).fetchone()
        if not row:
            return None
        path = self.objects / row["body_sha256"][:2] / row["body_sha256"]
        if not path.exists():
            return None
        entry = CacheEntry(
            key=key,
            status_code=row["status_code"],
            headers=json.loads(row["headers_json"]),
            body_sha256=row["body_sha256"],
            object_path=path,
            retrieved_at=row["retrieved_at"],
            expires_at=row["expires_at"],
            url_redacted=row["url_redacted"],
        )
        return entry if entry.fresh else None

    def put(self, method: str, url: str, status_code: int, headers: Mapping[str, str], body: bytes, ttl_seconds: int | None) -> CacheEntry:
        digest, path = self.store_object(body)
        now = time.time()
        expires = None if ttl_seconds is None else now + ttl_seconds
        key = self.request_key(method, url)
        redacted = self.redact_url(url)
        with self._connect() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO responses
                (cache_key, method, url_redacted, status_code, headers_json, body_sha256, retrieved_at, expires_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (key, method.upper(), redacted, status_code, json.dumps(dict(headers)), digest, now, expires),
            )
        return CacheEntry(key, status_code, dict(headers), digest, path, now, expires, redacted)

    def stats(self) -> dict[str, int]:
        with self._connect() as conn:
            responses = conn.execute("SELECT COUNT(*) FROM responses").fetchone()[0]
        objects = sum(1 for p in self.objects.rglob("*") if p.is_file())
        bytes_total = sum(p.stat().st_size for p in self.objects.rglob("*") if p.is_file())
        return {"responses": responses, "objects": objects, "bytes": bytes_total}
