from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from scholar_acquire.models import RuntimeState, SourceVersion
from scholar_acquire.vertical_slice import ChatGptVerticalSliceRuntime


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the v0.4 real-PDF vertical-slice acceptance gate."
    )
    parser.add_argument("--pmid", required=True)
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--discovery-provenance-json", required=True)
    parser.add_argument("--acquisition-context-json", required=True)
    parser.add_argument("--version", default=SourceVersion.UNKNOWN.value)
    parser.add_argument("--license", default=None)
    parser.add_argument("--report", type=Path, default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    discovery = json.loads(args.discovery_provenance_json)
    context = json.loads(args.acquisition_context_json)

    runtime = ChatGptVerticalSliceRuntime.create(args.pmid, args.root)
    artifact = runtime.import_artifact(
        args.pdf,
        source_url=args.source_url,
        discovery_provenance=discovery,
        acquisition_context=context,
        version=args.version,
        license=args.license,
    )
    step = runtime.step()

    manifest = (
        json.loads(step.result.manifest_path.read_text(encoding="utf-8"))
        if step.result and step.result.manifest_path and step.result.manifest_path.exists()
        else None
    )
    receipt = (
        json.loads(runtime.receipt_path.read_text(encoding="utf-8"))
        if runtime.receipt_path.exists()
        else None
    )
    events = (
        [json.loads(line) for line in runtime.events_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if runtime.events_path.exists()
        else []
    )
    event_names = [event.get("event") for event in events]
    required_events = {
        "runtime_integrity_verified",
        "artifact_imported",
        "artifact_validated",
        "manifest_written",
        "terminal_success",
    }
    manifest_meta = (manifest or {}).get("metadata", {})
    manifest_artifacts = (manifest or {}).get("artifacts", [])
    manifest_artifact = manifest_artifacts[0] if len(manifest_artifacts) == 1 else None

    checks = {
        "requested_identifier_is_pmid": runtime.session.identifier.kind.value == "pmid",
        "terminal_success": step.state == RuntimeState.SUCCESS,
        "manifest_exists": manifest is not None,
        "receipt_exists": receipt is not None,
        "event_journal_exists": bool(events),
        "receipt_integrity_verified": bool(
            receipt
            and receipt.get("integrity_verified") is True
            and receipt.get("package_tree_sha256") == receipt.get("expected_package_tree_sha256")
            and receipt.get("runtime_class") == "ChatGptVerticalSliceRuntime"
        ),
        "provider_attempts_absent": bool(step.result is not None and step.result.attempts == []),
        "provider_policy_absent": bool(step.terminal_outcome is not None and step.terminal_outcome.provider_policy == []),
        "provider_exhaustion_false": bool(step.terminal_outcome is not None and not step.terminal_outcome.provider_exhaustion_confirmed),
        "pending_fetch_absent": runtime.session.pending_request is None,
        "python_fetch_history_empty": runtime.session.fetch_history == [],
        "external_fetch_event_absent": "external_fetch_requested" not in event_names and "external_response_ingested" not in event_names,
        "required_events_present": required_events.issubset(set(event_names)),
        "single_pdf_artifact": bool(
            step.result
            and len(step.result.artifacts) == 1
            and step.result.artifacts[0].format.value == "pdf"
            and len(manifest_artifacts) == 1
            and manifest_artifact
            and manifest_artifact.get("format") == "pdf"
        ),
        "manifest_identifier_matches_pmid": bool(
            manifest
            and manifest.get("identifier") == {"kind": "pmid", "value": args.pmid}
            and (manifest.get("resolved_ids") or {}).get("pmid") == args.pmid
        ),
        "manifest_records_source_and_provenance": bool(
            manifest
            and manifest_meta.get("source_url") == args.source_url
            and manifest_meta.get("discovery_provenance") == discovery
            and manifest_meta.get("acquisition_context") == context
            and manifest_artifact
            and manifest_artifact.get("source_url") == args.source_url
            and ((manifest_artifact.get("metadata") or {}).get("v0_4") or {}).get("discovery_provenance") == discovery
            and ((manifest_artifact.get("metadata") or {}).get("v0_4") or {}).get("acquisition_context") == context
        ),
        "manifest_records_version_and_license": bool(
            manifest
            and manifest_meta.get("source_version") == artifact.version.value
            and manifest_meta.get("license") == artifact.license
        ),
        "pdf_hash_matches_materialized_file": bool(
            step.result
            and step.result.handoff
            and step.result.handoff.preferred_pdf_path
            and hashlib.sha256(step.result.handoff.preferred_pdf_path.read_bytes()).hexdigest() == artifact.sha256
            and manifest_artifact
            and manifest_artifact.get("sha256") == artifact.sha256
        ),
        "atom_sea_pdf_handoff_present": bool(
            step.result
            and step.result.handoff
            and step.result.handoff.preferred_pdf_path
            and step.result.handoff.pdf_sha256 == artifact.sha256
            and step.result.handoff.preferred_structured_path is None
        ),
    }
    passed = all(checks.values())
    report = {
        "schema_version": "1",
        "contract_version": "0.4.0",
        "passed": passed,
        "pmid": args.pmid,
        "source_url": args.source_url,
        "pdf_input": str(args.pdf.resolve()),
        "pdf_sha256": artifact.sha256,
        "artifact_version": artifact.version.value,
        "license": artifact.license,
        "discovery_provenance": discovery,
        "acquisition_context": context,
        "session_id": runtime.session.session_id,
        "run_receipt": str(runtime.receipt_path),
        "event_journal": str(runtime.events_path),
        "manifest": str(step.result.manifest_path) if step.result else None,
        "terminal_state": step.state.value,
        "checks": checks,
    }
    report_path = args.report or (runtime.session.session_dir / "V0.4_ACCEPTANCE_REPORT.json")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
