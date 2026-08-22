# scholar-acquire-chatgpt 0.4.0 development line

## v0.4 vertical slice

v0.4 adds `ChatGptVerticalSliceRuntime`. Its acceptance path is intentionally narrow: PMID, host-discovered lawful OA PDF, `runtime.import_artifact()`, Python validation and SHA-256, manifest, ATOM/SEA handoff, then `SUCCESS`.

The v0.3.1 provider stack remains in the tree for historical compatibility, but it is not called by the v0.4 vertical-slice runtime. See `V0.3.1_FREEZE.md`, `V0.4_EXECUTION_CONTRACT.md`, and `V0.4_ACCEPTANCE_TEST.md`. Exact v0.3.1 contract documents are preserved under `contracts/v0.3.1/`.

```python
from pathlib import Path
from scholar_acquire import ChatGptVerticalSliceRuntime

runtime = ChatGptVerticalSliceRuntime.create("24782981", Path("./runtime"))
runtime.import_artifact(
    Path("/path/to/materialized-open-access.pdf"),
    source_url="https://lawful.example/article.pdf",
    discovery_provenance={"discovered_by": "chatgpt_web", "source_record": "..."},
    acquisition_context={
        "open_access": True,
        "lawful_access_basis": "publisher open-access full text",
    },
    version="publishedVersion",
    license="CC-BY-4.0",
)
step = runtime.step()
assert step.state.value == "success"
```

The example source URL is illustrative only. The primary acceptance harness requires a real acquired OA PDF and its actual source record.

## Preserved v0.3.1 runtime

A fail-closed, tool-mediated runtime for lawful scholarly full-text acquisition from PMID, PMCID, or DOI identifiers.

## Operating model

The Python runtime is the controller. ChatGPT or another host is only the external I/O adapter.

```text
PMID / PMCID / DOI
        |
ChatGptAcquisitionRuntime
        |
step()
        |
ExternalFetchRequest  <---- no Python network I/O
        |
Host retrieval tool
        |
ingest_file()/ingest_bytes(request_id + ingest_token)
        |
step() resumes
        |
SUCCESS / EXHAUSTED / BLOCKED / FAILED
```

The default lawful provider policy is:

1. Europe PMC
2. PMC
3. Unpaywall
4. publisher open access
5. institutional repository / accepted manuscript

Sci-Hub and access-control bypasses are prohibited by source policy.

## Proof of execution

Every item session produces:

- `RUN_RECEIPT.json` — package version, imported runtime path, Python/platform, expected and actual package-tree SHA-256, integrity status, run/session IDs.
- `runtime_events.jsonl` — append-only execution journal.
- `session.json` — resumable runtime state.
- `pending_fetch.json` — current runtime-generated request when external I/O is needed.
- `runtime_status.json` — safe/redacted status for host inspection.
- `terminal_outcome.json` — typed terminal disposition.
- acquisition manifest and payload(s) on success.

No receipt means no valid acquisition run.

## Fail-closed integrity

`RUNTIME_BUILD.json` is packaged with the code. `ChatGptAcquisitionRuntime` verifies the materialized Python package tree before it creates or resumes a session. Missing build evidence raises `RuntimeUnavailableError`; a hash mismatch raises `RuntimeIntegrityError`. Hosts must not replace either condition with manual/web acquisition.

Preflight:

```bash
scholar-acquire-chatgpt chatgpt verify
```

Synthetic proof-of-execution test with no network access:

```bash
scholar-acquire-chatgpt chatgpt acceptance --root ./acceptance
```

## Tool-mediated use

Start:

```bash
scholar-acquire-chatgpt chatgpt begin "PMID:20566676" --root ./runs
```

If `state` is `needs_fetch`, retrieve exactly the emitted request through the available external tool layer. Then ingest its raw body using the emitted correlation values:

```bash
scholar-acquire-chatgpt chatgpt ingest SESSION RESPONSE_FILE \
  --request-id REQUEST_ID \
  --ingest-token INGEST_TOKEN \
  --status 200 \
  --content-type application/xml
```

The runtime rejects a mismatched `request_id` or `ingest_token`.

If the host cannot satisfy the request, preserve the session and mark it blocked:

```bash
scholar-acquire-chatgpt chatgpt block SESSION \
  --request-id REQUEST_ID \
  --ingest-token INGEST_TOKEN \
  --message "external retrieval transport unavailable"
```

A blocked request remains resumable. It is not equivalent to provider exhaustion.

## Terminal states

- `SUCCESS`: validated payload(s) satisfy the requested acquisition policy.
- `EXHAUSTED`: the configured lawful provider hierarchy completed without provider errors and did not satisfy the policy; `provider_exhaustion_confirmed=true`.
- `BLOCKED`: an external dependency prevented the runtime from completing; the session remains resumable.
- `FAILED`: runtime/provider execution failed such that lawful provider exhaustion cannot be proven.

The assistant must not independently upgrade `BLOCKED` or `FAILED` to “no lawful full text exists.”

## Structured full text

JATS XML is a first-class success payload and is preferred for ATOM/SEA when available. PDF acquisition is independent. A session may succeed with JATS only, PDF only, or both depending on `AcquisitionPolicy`.

## Batch runs

`ChatGptBatchRuntime` creates a runtime session for every identifier and writes:

- `BATCH_RUN_RECEIPT.json`
- `batch_state.json`
- `batch_events.jsonl`
- `batch_manifest.json`

`batch_manifest.json` is explicitly marked `source_of_truth: runtime-generated`. Human/assistant summaries should be derived from it rather than inventing item states.

## Development

```bash
python scripts/build_runtime.py
PYTHONPATH=src pytest
```

The build manifest must be regenerated after any package-source change and before packaging.
