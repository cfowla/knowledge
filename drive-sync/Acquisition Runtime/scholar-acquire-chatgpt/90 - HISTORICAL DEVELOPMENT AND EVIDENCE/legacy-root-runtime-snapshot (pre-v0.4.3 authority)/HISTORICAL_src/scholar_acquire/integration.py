from __future__ import annotations

from pathlib import Path

from .models import AcquisitionResult, ArtifactFormat, AtomSeaHandoff


def build_atom_sea_handoff(result: AcquisitionResult, manifest_path: Path | None = None) -> AtomSeaHandoff:
    structured = next((a for a in result.artifacts if a.format == ArtifactFormat.JATS_XML), None)
    if structured is None:
        structured = next((a for a in result.artifacts if a.structured), None)
    pdf = next((a for a in result.artifacts if a.format == ArtifactFormat.PDF), None)
    return AtomSeaHandoff(
        identifier=result.identifier,
        resolved_ids=result.resolved_ids,
        preferred_structured_path=structured.local_path if structured else None,
        preferred_pdf_path=pdf.local_path if pdf else None,
        structured_sha256=structured.sha256 if structured else None,
        pdf_sha256=pdf.sha256 if pdf else None,
        manifest_path=manifest_path,
    )
