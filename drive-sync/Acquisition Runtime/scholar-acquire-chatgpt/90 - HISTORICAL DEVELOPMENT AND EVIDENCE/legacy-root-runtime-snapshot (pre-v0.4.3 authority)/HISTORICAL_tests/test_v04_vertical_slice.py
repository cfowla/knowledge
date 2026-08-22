import json
from pathlib import Path

import pytest

from scholar_acquire.errors import ContentValidationError, RuntimeProtocolError
from scholar_acquire.models import RuntimeState, SourceVersion
from scholar_acquire.vertical_slice import ChatGptVerticalSliceRuntime


def _pdf_bytes() -> bytes:
    return b"%PDF-1.4\n1 0 obj\n<<>>\nendobj\n" + (b"x" * 1200) + b"\n%%EOF\n"


def _contract_kwargs():
    return {
        "source_url": "https://example.org/open/article.pdf",
        "discovery_provenance": {
            "discovered_by": "test_host_tool",
            "record": "fixture-only unit test",
        },
        "acquisition_context": {
            "open_access": True,
            "lawful_access_basis": "public OA test fixture",
        },
        "version": SourceVersion.PUBLISHED,
        "license": "CC-BY-4.0",
    }


def test_v04_requires_pmid(tmp_path: Path):
    with pytest.raises(RuntimeProtocolError, match="require a PMID"):
        ChatGptVerticalSliceRuntime.create("10.1234/example", tmp_path)


def test_v04_waits_for_import_without_provider_orchestration(tmp_path: Path, monkeypatch):
    runtime = ChatGptVerticalSliceRuntime.create("12345678", tmp_path)

    def forbidden(*args, **kwargs):
        raise AssertionError("provider orchestration must not execute in v0.4")

    monkeypatch.setattr("scholar_acquire.runtime.AcquisitionOrchestrator.fetch", forbidden)
    step = runtime.step()
    assert step.state == RuntimeState.READY
    assert runtime.session.pending_request is None
    assert runtime.session.fetch_history == []
    assert runtime._provider_policy() == []


def test_v04_import_requires_source_provenance_and_lawful_oa_context(tmp_path: Path):
    runtime = ChatGptVerticalSliceRuntime.create("12345678", tmp_path / "runtime")
    pdf = tmp_path / "article.pdf"
    pdf.write_bytes(_pdf_bytes())

    with pytest.raises(RuntimeProtocolError, match="source_url"):
        runtime.import_artifact(
            pdf,
            source_url="",
            discovery_provenance={"tool": "fixture"},
            acquisition_context={"open_access": True, "lawful_access_basis": "fixture"},
        )
    with pytest.raises(RuntimeProtocolError, match="discovery_provenance"):
        runtime.import_artifact(
            pdf,
            source_url="https://example.org/article.pdf",
            discovery_provenance={},
            acquisition_context={"open_access": True, "lawful_access_basis": "fixture"},
        )
    with pytest.raises(RuntimeProtocolError, match="open_access=true"):
        runtime.import_artifact(
            pdf,
            source_url="https://example.org/article.pdf",
            discovery_provenance={"tool": "fixture"},
            acquisition_context={"open_access": False, "lawful_access_basis": "fixture"},
        )


def test_v04_rejects_non_pdf(tmp_path: Path):
    runtime = ChatGptVerticalSliceRuntime.create("12345678", tmp_path / "runtime")
    not_pdf = tmp_path / "article.html"
    not_pdf.write_text("<html>not a pdf</html>", encoding="utf-8")
    with pytest.raises(ContentValidationError, match="Expected PDF"):
        runtime.import_artifact(not_pdf, **_contract_kwargs())


def test_v04_rejects_conflicting_resolved_pmid(tmp_path: Path):
    runtime = ChatGptVerticalSliceRuntime.create("12345678", tmp_path)
    with pytest.raises(RuntimeProtocolError, match="conflicts"):
        runtime.add_resolved_ids(pmid="87654321")


def test_v04_success_is_import_validation_hash_manifest_handoff_only(tmp_path: Path, monkeypatch):
    runtime = ChatGptVerticalSliceRuntime.create("12345678", tmp_path / "runtime")
    pdf = tmp_path / "article.pdf"
    pdf.write_bytes(_pdf_bytes())

    def forbidden(*args, **kwargs):
        raise AssertionError("provider orchestration must not execute in v0.4")

    monkeypatch.setattr("scholar_acquire.runtime.AcquisitionOrchestrator.fetch", forbidden)
    artifact = runtime.import_artifact(pdf, **_contract_kwargs())
    step = runtime.step()

    assert step.state == RuntimeState.SUCCESS
    assert step.result is not None
    assert step.result.attempts == []
    assert step.terminal_outcome is not None
    assert step.terminal_outcome.provider_policy == []
    assert step.terminal_outcome.provider_exhaustion_confirmed is False
    assert step.result.resolved_ids.pmid == "12345678"
    assert step.result.handoff is not None
    assert step.result.handoff.pdf_sha256 == artifact.sha256
    assert step.result.handoff.preferred_pdf_path is not None
    assert step.result.handoff.preferred_pdf_path.read_bytes() == pdf.read_bytes()
    assert step.result.handoff.preferred_structured_path is None

    manifest = json.loads(step.result.manifest_path.read_text(encoding="utf-8"))
    assert manifest["identifier"] == {"kind": "pmid", "value": "12345678"}
    assert manifest["attempts"] == []
    assert manifest["artifacts"][0]["sha256"] == artifact.sha256
    assert manifest["artifacts"][0]["source_url"] == _contract_kwargs()["source_url"]
    assert manifest["metadata"]["v0_4_vertical_slice"]["provider_orchestration"] is False
    assert manifest["metadata"]["v0_4_vertical_slice"]["fallback_providers"] is False
    assert manifest["metadata"]["discovery_provenance"]
    assert manifest["metadata"]["acquisition_context"]["open_access"] is True

    events = [json.loads(line) for line in runtime.events_path.read_text(encoding="utf-8").splitlines()]
    names = [event["event"] for event in events]
    assert "artifact_imported" in names
    assert "artifact_validated" in names
    assert "manifest_written" in names
    assert "terminal_success" in names
    assert "external_fetch_requested" not in names


def test_v04_blocked_is_not_exhausted(tmp_path: Path):
    runtime = ChatGptVerticalSliceRuntime.create("12345678", tmp_path)
    outcome = runtime.mark_blocked(message="Host could not materialize the discovered OA PDF")
    assert outcome.state == RuntimeState.BLOCKED
    assert outcome.provider_exhaustion_confirmed is False
    assert outcome.provider_policy == []
    assert runtime.step().state == RuntimeState.BLOCKED
