# scholar-acquire

A lawful, cache-aware scholarly full-text acquisition pipeline for PMID, PMCID, and DOI inputs.

Acquisition order:

1. Europe PMC metadata + OA JATS XML
2. PubMed Central ID conversion + current PMC AWS Article Dataset objects; PMC OAI-PMH JATS fallback
3. Unpaywall OA-location discovery
4. Publisher-hosted OA PDF/HTML retrieval
5. Institutional/repository accepted or published manuscript retrieval, with OpenAlex as a repository-location fallback

Sci-Hub is not used and matching Sci-Hub domains are explicitly rejected.

## Install

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -e .
```

Set a contact email. NCBI requests it for programmatic ID-converter use, and Unpaywall requires it.

```bash
export SCHOLAR_FETCH_EMAIL="you@example.org"
# optional, recommended for a larger OpenAlex request budget
export OPENALEX_API_KEY="..."
```

## CLI

```bash
scholar-acquire fetch 12345678 --out ./fulltext
scholar-acquire fetch 10.1000/example --out ./fulltext --json
scholar-acquire fetch 10.1000/example --allow-submitted
scholar-acquire cache stats
```

By default the pipeline requests both a structured full-text artifact and a PDF. It stops once both are found.

Each acquisition creates a directory containing artifacts plus `manifest.json`. The manifest records resolved IDs, hashes, source URLs, licenses/version information when available, cache-aware provider attempts, and an `handoff` section with the preferred structured/PDF inputs for downstream ATOM/SEA processing.

## Python API

```python
from pathlib import Path
from scholar_acquire import AcquisitionOrchestrator

acquirer = AcquisitionOrchestrator()
try:
    result = acquirer.fetch("PMID: 12345678", Path("./fulltext"))
finally:
    acquirer.close()

print(result.handoff.preferred_structured_path)
print(result.handoff.preferred_pdf_path)
```

## Caching and integrity

HTTP responses are indexed in SQLite. Bodies are stored content-addressed under SHA-256 paths. API metadata uses a finite TTL; full-text content uses an indefinite cache entry. Output files are hard-linked from the content store when possible and copied otherwise. Every artifact records its SHA-256 digest and byte count.

## Access policy

The pipeline does not bypass authentication, CAPTCHAs, subscription controls, or technical access restrictions. Repository preprints/submitted manuscripts are excluded by default; pass `--allow-submitted` to opt in. License metadata is recorded but not interpreted as legal advice; users remain responsible for complying with source terms and article licenses.

## Tests

```bash
pip install -e '.[dev]'
pytest
```

The test suite uses `httpx.MockTransport`, so normal tests make no external requests.
