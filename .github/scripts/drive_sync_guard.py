#!/usr/bin/env python3
"""Apply a staged Google Drive import without overwriting GitHub-owned paths."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

EXCLUDED_SUFFIXES = {".mp4", ".mov", ".avi", ".mkv", ".iso"}


@dataclass(frozen=True)
class CommitOwner:
    sha: str
    author_name: str
    author_email: str


@dataclass(frozen=True)
class Conflict:
    path: Path
    owner: CommitOwner | None
    destination_sha256: str
    staged_sha256: str


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_excluded(relative_path: Path) -> bool:
    return relative_path.suffix.lower() in EXCLUDED_SUFFIXES or ".git" in relative_path.parts


def last_modifying_commit(repo_root: Path, repository_path: Path) -> CommitOwner | None:
    result = subprocess.run(
        [
            "git",
            "-C",
            str(repo_root),
            "log",
            "-1",
            "--format=%H%x00%an%x00%ae",
            "--",
            repository_path.as_posix(),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    output = result.stdout.rstrip("\n")
    if not output:
        return None
    sha, author_name, author_email = output.split("\0", 2)
    return CommitOwner(sha=sha, author_name=author_name, author_email=author_email)


def atomic_copy(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(f".{destination.name}.drive-import-{os.getpid()}")
    try:
        shutil.copy2(source, temporary)
        os.replace(temporary, destination)
    finally:
        if temporary.exists():
            temporary.unlink()


def write_conflict_report(report_path: Path, conflicts: list[Conflict], sync_author: str) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        "# Google Drive import conflict",
        "",
        f"Generated: `{generated}`",
        "",
        "The Drive import was blocked before any staged file was written into `drive-sync`.",
        f"Only paths whose latest modifying commit is authored by `{sync_author}` may be replaced automatically.",
        "",
        "| Path | Latest modifying commit | Author | Destination SHA-256 | Staged SHA-256 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for conflict in conflicts:
        if conflict.owner is None:
            commit = "(no commit found)"
            author = "(unknown)"
        else:
            commit = f"`{conflict.owner.sha}`"
            author = f"{conflict.owner.author_name} <{conflict.owner.author_email}>"
        lines.append(
            f"| `{conflict.path.as_posix()}` | {commit} | {author} | "
            f"`{conflict.destination_sha256}` | `{conflict.staged_sha256}` |"
        )
    lines.extend(
        [
            "",
            "Manual reconciliation is required. Preserve the GitHub-authored version unless the staged Drive version is explicitly accepted.",
            "",
        ]
    )
    report_path.write_text("\n".join(lines), encoding="utf-8")


def run_import(
    *,
    repo_root: Path,
    stage_root: Path,
    destination_root: Path,
    conflict_report: Path,
    sync_author: str,
) -> int:
    repo_root = repo_root.resolve()
    stage_root = stage_root.resolve()
    destination_root = destination_root.resolve()

    try:
        destination_relative = destination_root.relative_to(repo_root)
    except ValueError as exc:
        raise ValueError("destination must be inside the repository") from exc

    if not stage_root.is_dir():
        raise ValueError(f"staging directory does not exist: {stage_root}")

    planned: list[tuple[Path, Path, str]] = []
    conflicts: list[Conflict] = []
    excluded = 0
    unchanged = 0

    for staged in sorted(path for path in stage_root.rglob("*") if path.is_file()):
        relative = staged.relative_to(stage_root)
        if is_excluded(relative):
            excluded += 1
            continue

        destination = destination_root / relative
        staged_hash = sha256_file(staged)
        if not destination.exists():
            planned.append((staged, destination, "add"))
            continue
        if not destination.is_file():
            conflicts.append(
                Conflict(
                    path=destination_relative / relative,
                    owner=None,
                    destination_sha256="(not a regular file)",
                    staged_sha256=staged_hash,
                )
            )
            continue

        destination_hash = sha256_file(destination)
        if destination_hash == staged_hash:
            unchanged += 1
            continue

        repository_path = destination_relative / relative
        owner = last_modifying_commit(repo_root, repository_path)
        if owner is None or owner.author_name != sync_author:
            conflicts.append(
                Conflict(
                    path=repository_path,
                    owner=owner,
                    destination_sha256=destination_hash,
                    staged_sha256=staged_hash,
                )
            )
            continue
        planned.append((staged, destination, "update"))

    if conflicts:
        write_conflict_report(conflict_report, conflicts, sync_author)
        print(f"Drive import blocked: {len(conflicts)} same-path conflict(s).", file=sys.stderr)
        print(f"Conflict report: {conflict_report}", file=sys.stderr)
        return 2

    added = 0
    updated = 0
    for staged, destination, action in planned:
        atomic_copy(staged, destination)
        if action == "add":
            added += 1
        else:
            updated += 1

    print(
        f"Drive import applied: added={added} updated={updated} "
        f"unchanged={unchanged} excluded={excluded}"
    )
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--stage", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--conflict-report", type=Path, required=True)
    parser.add_argument("--sync-author", default="google-drive-sync[bot]")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    destination = args.destination
    if not destination.is_absolute():
        destination = repo_root / destination
    report = args.conflict_report
    if not report.is_absolute():
        report = repo_root / report
    return run_import(
        repo_root=repo_root,
        stage_root=args.stage,
        destination_root=destination,
        conflict_report=report,
        sync_author=args.sync_author,
    )


if __name__ == "__main__":
    raise SystemExit(main())
