from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated

import typer

from .cache import DiskCache
from .acceptance import run_acceptance
from .integrity import runtime_healthcheck
from .config import Settings
from .models import AcquisitionPolicy, ArtifactFormat, RuntimeFailureCode, SourceVersion
from .orchestrator import AcquisitionOrchestrator
from .runtime import ChatGptAcquisitionRuntime

app = typer.Typer(no_args_is_help=True, help="Acquire lawful scholarly full text from PMID/DOI identifiers.")
cache_app = typer.Typer(no_args_is_help=True)
chatgpt_app = typer.Typer(no_args_is_help=True, help="Tool-mediated runtime for ChatGPT or other agent sandboxes.")
app.add_typer(cache_app, name="cache")
app.add_typer(chatgpt_app, name="chatgpt")


@app.command()
def fetch(
    identifier: Annotated[str, typer.Argument(help="PMID, PMCID, DOI, or doi.org URL")],
    out: Annotated[Path, typer.Option("--out", "-o", help="Output directory")] = Path("scholar-fetch-out"),
    email: Annotated[str | None, typer.Option("--email", help="Contact email for NCBI/Unpaywall; overrides env")] = None,
    openalex_key: Annotated[str | None, typer.Option("--openalex-key", help="OpenAlex API key; overrides env")] = None,
    structured: Annotated[bool, typer.Option("--structured/--no-structured")] = True,
    pdf: Annotated[bool, typer.Option("--pdf/--no-pdf")] = True,
    allow_submitted: Annotated[bool, typer.Option("--allow-submitted", help="Allow pre-peer-review repository copies")] = False,
    json_output: Annotated[bool, typer.Option("--json", help="Print result JSON to stdout")] = False,
) -> None:
    settings = Settings()
    if email:
        settings.contact_email = email
    if openalex_key:
        settings.openalex_api_key = openalex_key
    policy = AcquisitionPolicy(want_structured=structured, want_pdf=pdf, allow_submitted=allow_submitted)
    orchestrator = AcquisitionOrchestrator(settings=settings, policy=policy)
    try:
        result = orchestrator.fetch(identifier, out)
    finally:
        orchestrator.close()
    if json_output:
        typer.echo(json.dumps(result.model_dump(mode="json"), indent=2))
    else:
        typer.echo(f"manifest: {result.manifest_path}")
        typer.echo(f"artifacts: {len(result.artifacts)}")
        for artifact in result.artifacts:
            typer.echo(f"- {artifact.format.value}: {artifact.local_path} [{artifact.sha256[:12]}]")
    if not result.artifacts:
        raise typer.Exit(code=2)


@chatgpt_app.command("verify")
def chatgpt_verify() -> None:
    """Fail-closed runtime integrity preflight; performs no scholarly lookup."""
    payload = runtime_healthcheck()
    typer.echo(json.dumps(payload, indent=2))
    if not payload["ok"]:
        raise typer.Exit(code=3)


@chatgpt_app.command("acceptance")
def chatgpt_acceptance(
    root: Annotated[Path, typer.Option("--root", "-r")] = Path("scholar-acquire-acceptance"),
) -> None:
    """Exercise receipt -> request -> ingest -> terminal-success without network I/O."""
    payload = run_acceptance(root)
    typer.echo(json.dumps(payload, indent=2))


@chatgpt_app.command("begin")
def chatgpt_begin(
    identifier: Annotated[str, typer.Argument(help="PMID, PMCID, DOI, or doi.org URL")],
    root: Annotated[Path, typer.Option("--root", "-r", help="Directory in which to create the resumable session")] = Path("scholar-chatgpt-runtime"),
    structured: Annotated[bool, typer.Option("--structured/--no-structured")] = True,
    pdf: Annotated[bool, typer.Option("--pdf/--no-pdf")] = True,
    allow_submitted: Annotated[bool, typer.Option("--allow-submitted")] = False,
) -> None:
    policy = AcquisitionPolicy(want_structured=structured, want_pdf=pdf, allow_submitted=allow_submitted)
    runtime = ChatGptAcquisitionRuntime.create(identifier, root, policy=policy)
    step = runtime.step()
    _print_runtime_step(step)


@chatgpt_app.command("step")
def chatgpt_step(
    session: Annotated[Path, typer.Argument(help="Session directory or session.json")],
) -> None:
    runtime = ChatGptAcquisitionRuntime.load(session)
    _print_runtime_step(runtime.step())


@chatgpt_app.command("ingest")
def chatgpt_ingest(
    session: Annotated[Path, typer.Argument(help="Session directory or session.json")],
    response_file: Annotated[Path, typer.Argument(help="Raw response body retrieved by the host tool")],
    request_id: Annotated[str, typer.Option("--request-id")],
    ingest_token: Annotated[str, typer.Option("--ingest-token")],
    status_code: Annotated[int, typer.Option("--status")] = 200,
    content_type: Annotated[str | None, typer.Option("--content-type")] = None,
    advance: Annotated[bool, typer.Option("--advance/--no-advance")] = True,
) -> None:
    runtime = ChatGptAcquisitionRuntime.load(session)
    record = runtime.ingest_file(
        response_file,
        request_id=request_id,
        ingest_token=ingest_token,
        status_code=status_code,
        content_type=content_type,
    )
    typer.echo(json.dumps(record.model_dump(mode="json"), indent=2))
    if advance:
        _print_runtime_step(runtime.step())


@chatgpt_app.command("block")
def chatgpt_block(
    session: Annotated[Path, typer.Argument(help="Session directory or session.json")],
    request_id: Annotated[str, typer.Option("--request-id")],
    ingest_token: Annotated[str, typer.Option("--ingest-token")],
    message: Annotated[str, typer.Option("--message")],
    reason_code: Annotated[RuntimeFailureCode, typer.Option("--reason-code")] = RuntimeFailureCode.EXTERNAL_FETCH_BLOCKED,
) -> None:
    runtime = ChatGptAcquisitionRuntime.load(session)
    outcome = runtime.mark_fetch_blocked(
        request_id=request_id, ingest_token=ingest_token, message=message, reason_code=reason_code
    )
    typer.echo(json.dumps(outcome.model_dump(mode="json"), indent=2))


@chatgpt_app.command("receipt")
def chatgpt_receipt(
    session: Annotated[Path, typer.Argument(help="Session directory or session.json")],
) -> None:
    runtime = ChatGptAcquisitionRuntime.load(session)
    typer.echo(runtime.receipt_path.read_text(encoding="utf-8"), nl=False)


@chatgpt_app.command("import-artifact")
def chatgpt_import_artifact(
    session: Annotated[Path, typer.Argument(help="Session directory or session.json")],
    artifact_file: Annotated[Path, typer.Argument(help="PDF, JATS XML, HTML, or text file")],
    source_url: Annotated[str | None, typer.Option("--source-url")] = None,
    provider: Annotated[str, typer.Option("--provider")] = "chatgpt_import",
    format_name: Annotated[str | None, typer.Option("--format", help="pdf, jats_xml, html, or text")] = None,
    version: Annotated[SourceVersion, typer.Option("--version")] = SourceVersion.UNKNOWN,
    license: Annotated[str | None, typer.Option("--license")] = None,
    advance: Annotated[bool, typer.Option("--advance/--no-advance")] = True,
) -> None:
    runtime = ChatGptAcquisitionRuntime.load(session)
    fmt = ArtifactFormat(format_name) if format_name else None
    artifact = runtime.import_artifact(
        artifact_file,
        source_url=source_url,
        provider=provider,
        artifact_format=fmt,
        version=version,
        license=license,
    )
    typer.echo(json.dumps(artifact.model_dump(mode="json"), indent=2))
    if advance:
        _print_runtime_step(runtime.step())


@chatgpt_app.command("add-location")
def chatgpt_add_location(
    session: Annotated[Path, typer.Argument(help="Session directory or session.json")],
    url: Annotated[str, typer.Argument(help="Canonical landing or content URL")],
    host_type: Annotated[str, typer.Option("--host-type", help="publisher or repository")],
    landing_page_url: Annotated[str | None, typer.Option("--landing-url")] = None,
    pdf_url: Annotated[str | None, typer.Option("--pdf-url")] = None,
    version: Annotated[SourceVersion, typer.Option("--version")] = SourceVersion.UNKNOWN,
    license: Annotated[str | None, typer.Option("--license")] = None,
    source_name: Annotated[str | None, typer.Option("--source-name")] = None,
) -> None:
    runtime = ChatGptAcquisitionRuntime.load(session)
    candidate = runtime.add_location(
        url=url,
        host_type=host_type,
        landing_page_url=landing_page_url,
        pdf_url=pdf_url,
        version=version,
        license=license,
        source_name=source_name,
    )
    typer.echo(json.dumps(candidate.model_dump(mode="json"), indent=2))


@chatgpt_app.command("add-ids")
def chatgpt_add_ids(
    session: Annotated[Path, typer.Argument(help="Session directory or session.json")],
    pmid: Annotated[str | None, typer.Option("--pmid")] = None,
    doi: Annotated[str | None, typer.Option("--doi")] = None,
    pmcid: Annotated[str | None, typer.Option("--pmcid")] = None,
    versioned_pmcid: Annotated[str | None, typer.Option("--versioned-pmcid")] = None,
) -> None:
    runtime = ChatGptAcquisitionRuntime.load(session)
    ids = runtime.add_resolved_ids(pmid=pmid, doi=doi, pmcid=pmcid, versioned_pmcid=versioned_pmcid)
    typer.echo(json.dumps(ids.model_dump(mode="json"), indent=2))


@chatgpt_app.command("status")
def chatgpt_status(
    session: Annotated[Path, typer.Argument(help="Session directory or session.json")],
) -> None:
    runtime = ChatGptAcquisitionRuntime.load(session)
    safe_path = runtime.session.session_dir / runtime.status_filename
    typer.echo(safe_path.read_text(encoding="utf-8"), nl=False)


@cache_app.command("stats")
def cache_stats() -> None:
    settings = Settings()
    stats = DiskCache(settings.cache_dir).stats()
    typer.echo(json.dumps(stats, indent=2))


def _print_runtime_step(step) -> None:
    payload = {
        "state": step.state.value,
        "session_path": str(step.session_path),
        "message": step.message,
        "pending_request": step.pending_request.model_dump(mode="json") if step.pending_request else None,
        "manifest_path": str(step.result.manifest_path) if step.result and step.result.manifest_path else None,
        "terminal_outcome": step.terminal_outcome.model_dump(mode="json") if step.terminal_outcome else None,
        "handoff": step.result.handoff.model_dump(mode="json") if step.result and step.result.handoff else None,
    }
    typer.echo(json.dumps(payload, indent=2))


if __name__ == "__main__":
    app()
