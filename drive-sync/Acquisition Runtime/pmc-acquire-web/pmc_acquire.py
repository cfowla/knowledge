#!/usr/bin/env python3
"""One-provider PMC acquisition: PMID -> validated JATS/PDF -> hashes -> manifest."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import uuid
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urlparse
from urllib.request import Request, urlopen

IDCONV_URL = "https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/"
DATA_ROOT = "https://pmc-oa-opendata.s3.amazonaws.com"
DEFAULT_TIMEOUT = 30
SUCCESS, BLOCKED, EXHAUSTED, FAILED = "SUCCESS", "BLOCKED", "EXHAUSTED", "FAILED"


class AcquisitionError(Exception):
    pass


class BlockedError(AcquisitionError):
    pass


class ExhaustedError(AcquisitionError):
    pass


class FailedError(AcquisitionError):
    pass


@dataclass
class Identity:
    requested_pmid: str
    pmid: str
    pmcid: str
    versioned_pmcid: str
    version: int
    doi: str | None = None
    manuscript_id: str | None = None
    release_date: str | None = None


@dataclass
class Artifact:
    kind: str
    path: str
    source_url: str
    byte_size: int
    sha256: str
    md5_expected: str | None
    md5_actual: str
    md5_match: bool | None
    valid: bool
    validation: dict[str, Any]


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def clean_pmid(value: str) -> str:
    value = value.strip()
    if not re.fullmatch(r"\d+", value):
        raise ValueError("PMID must contain digits only.")
    return value


class Journal:
    def __init__(self, path: Path, run_id: str):
        self.path, self.run_id = path, run_id

    def emit(self, event: str, **data: Any) -> None:
        record = {"timestamp_utc": now(), "run_id": self.run_id, "event": event, **data}
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def get(url: str, *, email: str, tool: str, timeout: int) -> tuple[bytes, dict[str, str]]:
    request = Request(url, headers={"User-Agent": f"{tool}/1.0 ({email})", "Accept-Encoding": "identity"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return response.read(), {k.lower(): v for k, v in response.headers.items()}
    except HTTPError as e:
        if e.code in (401, 403):
            raise BlockedError(f"HTTP {e.code} for {url}") from e
        if e.code == 404:
            raise ExhaustedError(f"HTTP 404 for {url}") from e
        raise FailedError(f"HTTP {e.code} for {url}") from e
    except URLError as e:
        raise FailedError(f"Network error for {url}: {e.reason}") from e


def resolve_identity(pmid: str, *, email: str, tool: str, timeout: int, journal: Journal) -> Identity:
    query = urlencode({"ids": pmid, "idtype": "pmid", "format": "csv", "versions": "yes", "tool": tool, "email": email})
    url = f"{IDCONV_URL}?{query}"
    journal.emit("identity.request", url=url, requested_pmid=pmid)
    raw, _ = get(url, email=email, tool=tool, timeout=timeout)
    rows = list(csv.DictReader(raw.decode("utf-8-sig", errors="replace").splitlines()))
    usable = []
    for row in rows:
        if (row.get("ErrorMessage") or "").strip():
            continue
        row_pmid = (row.get("PMID") or "").strip()
        if row_pmid and row_pmid != pmid:
            raise FailedError(f"Identity mismatch: requested PMID {pmid}, got {row_pmid}.")
        if not (row.get("PMCID") or "").strip() or not (row.get("Version") or "").strip():
            continue
        if (row.get("IsLive") or "").strip().lower() in {"0", "false", "no"}:
            continue
        usable.append(row)
    if not usable:
        raise ExhaustedError(f"PMID {pmid} has no live PMC full-text version.")
    current = [r for r in usable if (r.get("IsCurrent") or "").strip().lower() in {"1", "true", "yes"}]
    row = current[0] if current else usable[-1]
    pmcid, versioned = (row.get("PMCID") or "").strip(), (row.get("Version") or "").strip()
    match = re.fullmatch(r"(PMC\d+)\.(\d+)", versioned)
    if not match or match.group(1) != pmcid:
        raise FailedError(f"Unexpected PMC version identity: {pmcid!r} / {versioned!r}.")
    identity = Identity(
        requested_pmid=pmid,
        pmid=(row.get("PMID") or pmid).strip(),
        pmcid=pmcid,
        versioned_pmcid=versioned,
        version=int(match.group(2)),
        doi=(row.get("DOI") or "").strip() or None,
        manuscript_id=(row.get("MID") or "").strip() or None,
        release_date=(row.get("ReleaseDate") or "").strip() or None,
    )
    journal.emit("identity.resolved", identity=asdict(identity))
    return identity


def load_metadata(identity: Identity, *, email: str, tool: str, timeout: int, journal: Journal) -> tuple[dict[str, Any], str]:
    url = f"{DATA_ROOT}/{identity.versioned_pmcid}/{identity.versioned_pmcid}.json"
    journal.emit("dataset_metadata.request", url=url)
    try:
        raw, _ = get(url, email=email, tool=tool, timeout=timeout)
    except ExhaustedError as e:
        raise ExhaustedError(f"{identity.versioned_pmcid} is not available in the automated PMC Article Dataset.") from e
    try:
        meta = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise FailedError("PMC dataset metadata was not valid JSON.") from e
    if str(meta.get("pmcid") or "") != identity.pmcid:
        raise FailedError("PMC dataset PMCID mismatch.")
    if str(meta.get("version")) != str(identity.version):
        raise FailedError("PMC dataset version mismatch.")
    if meta.get("pmid") and str(meta["pmid"]) != identity.pmid:
        raise FailedError("PMC dataset PMID mismatch.")
    journal.emit("dataset_metadata.resolved", url=url, title=meta.get("title"), license_code=meta.get("license_code"), xml_available=bool(meta.get("xml_url")), pdf_available=bool(meta.get("pdf_url")))
    return meta, url


def dataset_https(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme == "https":
        return url
    if parsed.scheme != "s3" or parsed.netloc != "pmc-oa-opendata":
        raise FailedError(f"Unexpected PMC dataset URL: {url}")
    result = f"{DATA_ROOT}/{parsed.path.lstrip('/')}"
    return result + (f"?{parsed.query}" if parsed.query else "")


def expected_md5(url: str) -> str | None:
    values = parse_qs(urlparse(url).query).get("md5")
    if not values:
        return None
    value = values[0].lower().strip()
    return value if re.fullmatch(r"[0-9a-f]{32}", value) else None


def validate_xml(data: bytes, identity: Identity) -> dict[str, Any]:
    result: dict[str, Any] = {"format": "jats_xml", "xml_parseable": False, "root_is_article": False, "pmcid_matches": False}
    try:
        root = ET.fromstring(data)
    except ET.ParseError as e:
        result["error"] = str(e)
        result["valid"] = False
        return result
    result["xml_parseable"] = True
    result["root_is_article"] = root.tag.rsplit("}", 1)[-1] == "article"
    pmcids = []
    for element in root.iter():
        if element.tag.rsplit("}", 1)[-1] != "article-id":
            continue
        if (element.attrib.get("pub-id-type") or "").lower() not in {"pmcid", "pmcaid", "pmc"}:
            continue
        value = (element.text or "").strip().upper()
        if value:
            pmcids.append(value if value.startswith("PMC") else f"PMC{value}")
    result["pmcid_found"] = pmcids or None
    result["pmcid_matches"] = identity.pmcid.upper() in pmcids
    result["valid"] = result["xml_parseable"] and result["root_is_article"] and result["pmcid_matches"]
    return result


def validate_pdf(data: bytes) -> dict[str, Any]:
    result = {
        "format": "pdf",
        "starts_with_pdf_magic": data.startswith(b"%PDF-"),
        "eof_marker_near_end": b"%%EOF" in data[-4096:] if data else False,
        "byte_size_at_least_1024": len(data) >= 1024,
    }
    result["valid"] = all(result[k] for k in ("starts_with_pdf_magic", "eof_marker_near_end", "byte_size_at_least_1024"))
    return result


def acquire_artifact(kind: str, raw_url: str, destination: Path, identity: Identity, *, email: str, tool: str, timeout: int, journal: Journal) -> Artifact:
    url = dataset_https(raw_url)
    journal.emit("artifact.request", kind=kind, url=url)
    data, headers = get(url, email=email, tool=tool, timeout=timeout)
    sha256 = hashlib.sha256(data).hexdigest()
    md5_actual = hashlib.md5(data).hexdigest()  # nosec B324: integrity comparison only
    md5_wanted = expected_md5(raw_url)
    md5_match = None if md5_wanted is None else md5_actual == md5_wanted
    if md5_match is False:
        raise FailedError(f"PMC dataset MD5 mismatch for {kind}.")
    validation = validate_xml(data, identity) if kind == "xml" else validate_pdf(data)
    if not validation.get("valid"):
        raise FailedError(f"{kind.upper()} validation failed: {validation}")
    destination.write_bytes(data)
    artifact = Artifact(kind, str(destination), url, len(data), sha256, md5_wanted, md5_actual, md5_match, True, validation)
    journal.emit("artifact.acquired", kind=kind, path=str(destination), byte_size=len(data), sha256=sha256, content_type=headers.get("content-type"), validation=validation)
    return artifact


def write_manifest(path: Path, manifest: dict[str, Any]) -> None:
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def run(pmid: str, *, email: str, tool: str, out_root: Path, timeout: int) -> tuple[str, Path]:
    run_id = str(uuid.uuid4())
    run_dir = out_root / f"PMID_{pmid}_{run_id[:8]}"
    run_dir.mkdir(parents=True, exist_ok=False)
    journal_path, manifest_path = run_dir / "events.jsonl", run_dir / "manifest.json"
    journal = Journal(journal_path, run_id)
    manifest: dict[str, Any] = {
        "schema_version": "pmc-acquire-basic-1",
        "run_id": run_id,
        "started_at_utc": now(),
        "provider": "PubMed Central",
        "provider_route": "PMC ID Converter -> PMC Article Dataset",
        "requested": {"pmid": pmid},
        "resolved_identity": None,
        "dataset_metadata": None,
        "artifacts": [],
        "atom_sea_handoff": {"preferred_input": None, "secondary_input": None},
        "terminal_state": None,
        "terminal_reason": None,
        "event_journal": str(journal_path),
    }
    journal.emit("run.started", requested_pmid=pmid, run_dir=str(run_dir))
    try:
        identity = resolve_identity(pmid, email=email, tool=tool, timeout=timeout, journal=journal)
        manifest["resolved_identity"] = asdict(identity)
        meta, meta_url = load_metadata(identity, email=email, tool=tool, timeout=timeout, journal=journal)
        manifest["dataset_metadata"] = {k: meta.get(k) for k in ("pmcid", "version", "pmid", "doi", "title", "citation", "license_code", "is_pmc_openaccess", "is_manuscript", "is_historical_ocr", "is_retracted", "xml_url", "pdf_url")}
        manifest["dataset_metadata"]["metadata_url"] = meta_url
        artifacts, errors = [], []
        for kind, filename in (("xml", "article.xml"), ("pdf", "article.pdf")):
            raw_url = meta.get(f"{kind}_url")
            if not raw_url:
                continue
            try:
                artifacts.append(acquire_artifact(kind, str(raw_url), run_dir / filename, identity, email=email, tool=tool, timeout=timeout, journal=journal))
            except AcquisitionError as e:
                errors.append({"kind": kind, "error": str(e)})
                journal.emit("artifact.error", kind=kind, error=str(e))
        manifest["artifacts"] = [asdict(a) for a in artifacts]
        if errors:
            manifest["artifact_errors"] = errors
        xml = next((a for a in artifacts if a.kind == "xml"), None)
        pdf = next((a for a in artifacts if a.kind == "pdf"), None)
        if xml:
            manifest["atom_sea_handoff"]["preferred_input"] = xml.path
            if pdf:
                manifest["atom_sea_handoff"]["secondary_input"] = pdf.path
        elif pdf:
            manifest["atom_sea_handoff"]["preferred_input"] = pdf.path
        if not artifacts:
            if not meta.get("xml_url") and not meta.get("pdf_url"):
                raise ExhaustedError(f"PMC dataset metadata for {identity.versioned_pmcid} exposes neither XML nor PDF.")
            reason = "; ".join(f"{e['kind']}: {e['error']}" for e in errors)
            if any("HTTP 401" in e["error"] or "HTTP 403" in e["error"] for e in errors):
                raise BlockedError(reason)
            raise FailedError(reason or "No valid artifact was materialized.")
        manifest["terminal_state"] = SUCCESS
        manifest["terminal_reason"] = "At least one validated PMC full-text artifact was materialized."
    except BlockedError as e:
        manifest["terminal_state"], manifest["terminal_reason"] = BLOCKED, str(e)
    except ExhaustedError as e:
        manifest["terminal_state"], manifest["terminal_reason"] = EXHAUSTED, str(e)
    except (FailedError, ValueError, OSError) as e:
        manifest["terminal_state"], manifest["terminal_reason"] = FAILED, str(e)
    except Exception as e:
        manifest["terminal_state"], manifest["terminal_reason"] = FAILED, f"Unhandled {type(e).__name__}: {e}"
    journal.emit("run.finished", terminal_state=manifest["terminal_state"], reason=manifest["terminal_reason"])
    manifest["finished_at_utc"] = now()
    write_manifest(manifest_path, manifest)
    return str(manifest["terminal_state"]), manifest_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Acquire lawful reusable full text from PMC for one PMID.")
    parser.add_argument("pmid")
    parser.add_argument("--email", default=os.environ.get("NCBI_EMAIL"))
    parser.add_argument("--tool", default="pmc_acquire_basic")
    parser.add_argument("--out", type=Path, default=Path("runs"))
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        pmid = clean_pmid(args.pmid)
    except ValueError as e:
        raise SystemExit(str(e)) from e
    if not args.email:
        raise SystemExit("Provide --email or set NCBI_EMAIL.")
    if args.timeout <= 0:
        raise SystemExit("--timeout must be greater than zero.")
    state, manifest = run(pmid, email=args.email, tool=args.tool, out_root=args.out, timeout=args.timeout)
    print(state)
    print(manifest)
    return {SUCCESS: 0, EXHAUSTED: 2, BLOCKED: 3, FAILED: 1}.get(state, 1)


if __name__ == "__main__":
    sys.exit(main())
