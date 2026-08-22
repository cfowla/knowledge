# ChatGPT Scholarly Acquisition Runtime Protocol — v0.3.1

## Mandatory execution contract

1. Materialize `scholar-acquire-chatgpt` before scholarly lookup.
2. Run the package integrity preflight. If it reports `RUNTIME_UNAVAILABLE` or `RUNTIME_INTEGRITY_MISMATCH`, stop. Do not substitute browser research or manual retrieval.
3. Instantiate `ChatGptAcquisitionRuntime` or `ChatGptBatchRuntime` with the requested PMID/PMCID/DOI.
4. The Python runtime controls provider order and identity resolution.
5. External retrieval tools may only satisfy an `ExternalFetchRequest` emitted by the runtime, unless importing an artifact explicitly supplied by the user.
6. Every externally retrieved response used by the pipeline must be returned through `ingest_file()` or `ingest_bytes()` with the exact emitted `request_id` and `ingest_token`.
7. Resume with `step()` after ingest. Repeat until the runtime reaches a terminal state.
8. Do not use independent web/search reasoning to classify `SUCCESS`, `EXHAUSTED`, `BLOCKED`, or `FAILED`.
9. `SUCCESS` is valid only when the runtime returns terminal success with validated payload hashes.
10. `EXHAUSTED` is valid only when the runtime returns terminal exhaustion with `provider_exhaustion_confirmed=true`.
11. Host retrieval failure is `BLOCKED`, never “no OA copy found.” Preserve the session for resume.
12. Preserve `RUN_RECEIPT.json`, `runtime_events.jsonl`, `session.json`, terminal outcome, payloads, acquisition manifest, and cache provenance.
13. Prefer structured JATS for ATOM/SEA; retain PDF when available.
14. Never use Sci-Hub or bypass access controls.

## Required evidence before reporting an acquisition

A valid run must expose:

- runtime version and imported path;
- expected and actual package-tree SHA-256;
- `integrity_verified=true`;
- session/run ID;
- runtime-generated external request IDs;
- matching response-ingest events and body SHA-256 values;
- terminal runtime state;
- provider attempts and provider-exhaustion flag;
- artifact SHA-256 values for successes.

If these artifacts do not exist, report that the runtime was not successfully executed.

## Allowed host actions

The host may:

- retrieve the exact runtime-generated URL using lawful web/API tools;
- save raw response bytes;
- pass status/content type/headers and bytes back to the runtime;
- explicitly mark an emitted request blocked when the tool layer cannot materialize it;
- import a user-uploaded or otherwise already-materialized lawful payload with source provenance;
- seed resolved identifiers or lawful publisher/repository locations discovered by a tool, while retaining the discovery source.

The host may not:

- manually traverse providers and declare the result authoritative;
- replace the requested article with a title-similar article;
- infer provider exhaustion from search-engine absence;
- call a transport limitation a paywall or availability failure;
- silently bypass the Python controller.

## Terminal semantics

### SUCCESS
Validated payload(s) satisfy the active `AcquisitionPolicy`.

### EXHAUSTED
All configured lawful providers completed without unresolved provider execution errors, and the policy is still unsatisfied.

### BLOCKED
Execution cannot continue because the host cannot satisfy the current external request. `provider_exhaustion_confirmed` must remain false and the pending request must remain resumable.

### FAILED
Runtime/protocol/provider execution is invalid or incomplete. `provider_exhaustion_confirmed` must remain false.

## Standard batch acceptance gate

Before a substantive PMID test batch:

1. `chatgpt verify` passes.
2. `chatgpt acceptance` passes without Python network I/O.
3. Full unit test suite passes.
4. The build package/wheel SHA-256 values are recorded.
5. Every real identifier receives its own runtime receipt and event journal.
6. Batch results are read from `batch_manifest.json`.
