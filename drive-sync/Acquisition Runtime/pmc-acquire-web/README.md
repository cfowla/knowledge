# PMC Acquire Web

A deliberately small PMC-only scholarly acquisition application with a browser interface.

It is intentionally separate from the authoritative `scholar-acquire-chatgpt` runtime. The goal is to prove one acquisition route end to end before adding orchestration.

## Contract

```text
PMID
  -> PMC identity/version resolution
  -> PMC Article Dataset
  -> JATS XML + PDF when available
  -> validation
  -> MD5 check when supplied
  -> SHA-256
  -> manifest.json + events.jsonl
  -> SUCCESS / BLOCKED / EXHAUSTED / FAILED
```

The browser is only a control panel. `pmc_acquire.py` remains the acquisition implementation.

## Requirements

- Python 3.10+
- Internet access to NCBI/PMC and the anonymous PMC article dataset
- No third-party Python packages

## Run the browser UI

```bash
cd "drive-sync/Acquisition Runtime/pmc-acquire-web"
export NCBI_EMAIL="you@example.com"   # optional if entered in the UI
python server.py
```

Open <http://127.0.0.1:8000>.

The page accepts one PMID, executes the acquisition, displays identity/provenance/validation/hashes, and exposes downloads for acquired XML/PDF plus the manifest.

## Run from the terminal

The standalone CLI remains available:

```bash
python pmc_acquire.py 35124914 --email you@example.com
```

## Output

Each acquisition creates its own directory under `runs/`:

```text
runs/
└── PMID_35124914_<run-id>/
    ├── article.xml       # when available
    ├── article.pdf       # when available
    ├── manifest.json
    └── events.jsonl
```

When JATS exists it is the preferred ATOM/SEA input. PDF is secondary when both exist.

## Tests

```bash
python -m unittest discover -s tests -v
```

The smoke tests do not make live network requests.

## Non-goals

This first version intentionally has no provider fallback, batching, retries, caching, generalized transport layer, or provider registry. Additional providers should be implemented and proven independently before they are orchestrated.
