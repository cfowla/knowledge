# API Contracts

## `ChatGptAcquisitionRuntime.create(identifier, root, ...)`

Creates a resumable session only after `RUNTIME_BUILD.json` verifies against the materialized package tree. Emits `RUN_RECEIPT.json` before provider execution.

## `step() -> RuntimeStep`

Runs deterministic provider logic until one of:

- `needs_fetch` with `pending_request`;
- `success`;
- `exhausted`;
- `blocked`;
- `failed`.

The tool-mediated HTTP client never opens sockets. A cache miss raises an internal `FetchRequired` which becomes `RuntimeStep(state=needs_fetch)`.

## `ExternalFetchRequest`

Required fields include:

- `request_id`: deterministic request correlation identifier;
- `url` and `redacted_url`;
- request headers / content-size limit;
- provider;
- `ingest_token`: unpredictable per-emission capability token.

`request_id` alone is insufficient to ingest a response.

## `ingest_bytes()` / `ingest_file()`

Both require exact `request_id` + `ingest_token`. On success the response is stored in the content-addressed cache and `external_response_ingested` records status, media type, byte length, SHA-256, and cache object path.

## `mark_fetch_blocked()`

Creates a `BLOCKED` terminal outcome while retaining the pending request for future resume. It must not set provider exhaustion.

## `RUN_RECEIPT.json`

Proof that a specific package tree was instantiated. It contains expected and actual package-tree hashes and the runtime import path.

## `runtime_events.jsonl`

Append-only evidence stream. Required critical event types include runtime integrity verification, runtime initialization, external fetch requests, external response ingestion, artifact validation, and terminal outcome.

## `RuntimeTerminalOutcome`

The authoritative result classification. `provider_exhaustion_confirmed` is true only for `EXHAUSTED`.

## `ChatGptBatchRuntime`

Creates independent item sessions and writes a runtime-generated `batch_manifest.json`. Assistant-visible summaries must be derived from that manifest.
