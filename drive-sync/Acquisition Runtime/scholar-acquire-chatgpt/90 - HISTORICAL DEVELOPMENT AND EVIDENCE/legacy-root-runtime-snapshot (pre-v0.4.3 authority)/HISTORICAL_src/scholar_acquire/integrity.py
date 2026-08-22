from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .errors import RuntimeIntegrityError, RuntimeUnavailableError

BUILD_MANIFEST_NAME = "RUNTIME_BUILD.json"
_MANIFEST_SCHEMA = "1"


def _package_dir(package_dir: Path | None = None) -> Path:
    return (package_dir or Path(__file__).resolve().parent).resolve()


def _source_files(package_dir: Path) -> list[Path]:
    return sorted(
        (
            p
            for p in package_dir.rglob("*.py")
            if "__pycache__" not in p.parts and p.is_file()
        ),
        key=lambda p: p.relative_to(package_dir).as_posix(),
    )


def compute_package_identity(package_dir: Path | None = None) -> dict[str, Any]:
    """Return deterministic hashes for the importable Python package tree.

    RUNTIME_BUILD.json is intentionally excluded from the tree hash, avoiding a
    self-referential digest. The tree digest commits to both relative paths and
    each file's SHA-256, so moved/renamed/modified code changes the identity.
    """
    root = _package_dir(package_dir)
    if not root.exists() or not root.is_dir():
        raise RuntimeUnavailableError(f"Runtime package directory not found: {root}")

    files: dict[str, str] = {}
    tree = hashlib.sha256()
    for path in _source_files(root):
        rel = path.relative_to(root).as_posix()
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        files[rel] = digest
        tree.update(rel.encode("utf-8"))
        tree.update(b"\0")
        tree.update(digest.encode("ascii"))
        tree.update(b"\n")
    if not files:
        raise RuntimeUnavailableError(f"Runtime package contains no Python sources: {root}")
    return {
        "actual_package_tree_sha256": tree.hexdigest(),
        "files": files,
        "package_dir": str(root),
    }


def write_build_manifest(
    package_dir: Path,
    *,
    version: str,
    build_id: str | None = None,
) -> Path:
    """Create/replace the canonical build manifest for a materialized runtime."""
    root = _package_dir(package_dir)
    identity = compute_package_identity(root)
    manifest = {
        "schema_version": _MANIFEST_SCHEMA,
        "package": "scholar-acquire-chatgpt",
        "version": version,
        "build_id": build_id or f"scholar-acquire-chatgpt-{version}",
        "package_tree_sha256": identity["actual_package_tree_sha256"],
        "files": identity["files"],
        "hash_algorithm": "sha256",
        "tree_algorithm": "sha256(relative_path\\0file_sha256\\n)",
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    path = root / BUILD_MANIFEST_NAME
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def verify_build_manifest(package_dir: Path | None = None) -> dict[str, Any]:
    """Fail closed unless the materialized package matches RUNTIME_BUILD.json."""
    root = _package_dir(package_dir)
    manifest_path = root / BUILD_MANIFEST_NAME
    if not manifest_path.exists():
        raise RuntimeUnavailableError(
            f"Canonical runtime build manifest is missing: {manifest_path}. "
            "Do not substitute manual/web acquisition."
        )
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise RuntimeUnavailableError(f"Unreadable runtime build manifest: {manifest_path}") from exc

    if manifest.get("package") != "scholar-acquire-chatgpt" or not manifest.get("version"):
        raise RuntimeUnavailableError("Runtime build manifest has invalid package/version metadata")
    expected = manifest.get("package_tree_sha256")
    if not isinstance(expected, str) or len(expected) != 64:
        raise RuntimeUnavailableError("Runtime build manifest is missing a valid package_tree_sha256")

    actual = compute_package_identity(root)
    if actual["actual_package_tree_sha256"] != expected:
        expected_files = manifest.get("files") or {}
        changed = sorted(
            set(expected_files) | set(actual["files"])
        )
        changed = [p for p in changed if expected_files.get(p) != actual["files"].get(p)]
        suffix = f" Changed paths: {', '.join(changed[:12])}" if changed else ""
        raise RuntimeIntegrityError(
            "Materialized runtime does not match canonical build manifest."
            f" expected={expected} actual={actual['actual_package_tree_sha256']}.{suffix}"
        )

    return {
        **manifest,
        **actual,
        "manifest_path": str(manifest_path),
        "integrity_verified": True,
    }


def runtime_healthcheck(package_dir: Path | None = None) -> dict[str, Any]:
    """Machine-readable preflight used by hosts before any scholarly lookup."""
    try:
        identity = verify_build_manifest(package_dir)
        return {
            "ok": True,
            "state": "READY",
            "reason_code": None,
            "package": identity["package"],
            "version": identity["version"],
            "package_tree_sha256": identity["actual_package_tree_sha256"],
            "manifest_path": identity["manifest_path"],
        }
    except RuntimeUnavailableError as exc:
        return {"ok": False, "state": "BLOCKED", "reason_code": "RUNTIME_UNAVAILABLE", "message": str(exc)}
    except RuntimeIntegrityError as exc:
        return {"ok": False, "state": "BLOCKED", "reason_code": "RUNTIME_INTEGRITY_MISMATCH", "message": str(exc)}
