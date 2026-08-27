#!/usr/bin/env python3
"""Tiny browser/API wrapper around the standalone PMC acquisition program."""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import re
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

import pmc_acquire

APP_ROOT = Path(__file__).resolve().parent
STATIC_ROOT = APP_ROOT / "static"
RUNS_ROOT = APP_ROOT / "runs"
RUN_NAME_RE = re.compile(r"^PMID_\d+_[0-9a-f]{8}$")
ARTIFACT_NAMES = {"article.xml", "article.pdf", "manifest.json", "events.jsonl"}


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _safe_run_dir(run_name: str) -> Path:
    if not RUN_NAME_RE.fullmatch(run_name):
        raise ValueError("Invalid run identifier.")
    candidate = (RUNS_ROOT / run_name).resolve()
    if candidate.parent != RUNS_ROOT.resolve():
        raise ValueError("Invalid run path.")
    return candidate


def _api_manifest(manifest_path: Path) -> dict:
    manifest = _read_json(manifest_path)
    run_name = manifest_path.parent.name
    artifacts = []
    for artifact in manifest.get("artifacts", []):
        item = dict(artifact)
        filename = Path(str(item.get("path", ""))).name
        if filename in ARTIFACT_NAMES:
            item["download_url"] = f"/api/runs/{run_name}/files/{filename}"
        artifacts.append(item)
    manifest["artifacts"] = artifacts
    manifest["manifest_url"] = f"/api/runs/{run_name}/files/manifest.json"
    manifest["events_url"] = f"/api/runs/{run_name}/files/events.jsonl"
    return manifest


class AppHandler(SimpleHTTPRequestHandler):
    server_version = "PMCAcquireWeb/0.1"

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"[web] {self.address_string()} - {fmt % args}")

    def _send_json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path: Path, *, download_name: str | None = None) -> None:
        if not path.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        content_type, _ = mimetypes.guess_type(path.name)
        if path.suffix == ".xml":
            content_type = "application/xml"
        elif path.suffix == ".jsonl":
            content_type = "application/x-ndjson"
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type or "application/octet-stream")
        self.send_header("Content-Length", str(path.stat().st_size))
        self.send_header("Cache-Control", "no-store")
        if download_name:
            self.send_header("Content-Disposition", f'attachment; filename="{download_name}"')
        self.end_headers()
        with path.open("rb") as f:
            while chunk := f.read(1024 * 1024):
                self.wfile.write(chunk)

    def do_POST(self) -> None:  # noqa: N802
        if urlparse(self.path).path != "/api/acquire":
            self.send_error(HTTPStatus.NOT_FOUND)
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 16_384:
                raise ValueError("Request body is missing or too large.")
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            pmid = pmc_acquire.clean_pmid(str(payload.get("pmid", "")))
            email = str(payload.get("email") or os.environ.get("NCBI_EMAIL") or "").strip()
            if not email:
                raise ValueError("Provide an email address or set NCBI_EMAIL on the server.")
            timeout = int(payload.get("timeout") or pmc_acquire.DEFAULT_TIMEOUT)
            if timeout <= 0 or timeout > 300:
                raise ValueError("Timeout must be between 1 and 300 seconds.")

            RUNS_ROOT.mkdir(parents=True, exist_ok=True)
            state, manifest_path = pmc_acquire.run(
                pmid,
                email=email,
                tool="pmc_acquire_web",
                out_root=RUNS_ROOT,
                timeout=timeout,
            )
            manifest = _api_manifest(manifest_path)
            self._send_json({"ok": state == pmc_acquire.SUCCESS, "state": state, "manifest": manifest})
        except (ValueError, json.JSONDecodeError) as exc:
            self._send_json({"ok": False, "error": str(exc)}, status=HTTPStatus.BAD_REQUEST)
        except Exception as exc:
            self._send_json(
                {"ok": False, "error": f"Unhandled {type(exc).__name__}: {exc}"},
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
            )

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        path = unquote(parsed.path)

        if path == "/api/health":
            self._send_json({"ok": True, "service": "pmc-acquire-web", "version": "0.1"})
            return

        match = re.fullmatch(r"/api/runs/([^/]+)/files/([^/]+)", path)
        if match:
            run_name, filename = match.groups()
            try:
                if filename not in ARTIFACT_NAMES:
                    raise ValueError("Unsupported run file.")
                run_dir = _safe_run_dir(run_name)
            except ValueError as exc:
                self._send_json({"ok": False, "error": str(exc)}, status=HTTPStatus.BAD_REQUEST)
                return
            self._send_file(run_dir / filename, download_name=filename)
            return

        if path.startswith("/api/"):
            self.send_error(HTTPStatus.NOT_FOUND)
            return

        requested = "index.html" if path in {"", "/"} else path.lstrip("/")
        candidate = (STATIC_ROOT / requested).resolve()
        try:
            candidate.relative_to(STATIC_ROOT.resolve())
        except ValueError:
            self.send_error(HTTPStatus.FORBIDDEN)
            return
        self._send_file(candidate)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the PMC acquisition browser interface.")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host. Default: 127.0.0.1")
    parser.add_argument("--port", type=int, default=8000, help="Bind port. Default: 8000")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if not (1 <= args.port <= 65535):
        raise SystemExit("--port must be between 1 and 65535")
    RUNS_ROOT.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer((args.host, args.port), AppHandler)
    print(f"PMC Acquisition UI: http://{args.host}:{args.port}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
