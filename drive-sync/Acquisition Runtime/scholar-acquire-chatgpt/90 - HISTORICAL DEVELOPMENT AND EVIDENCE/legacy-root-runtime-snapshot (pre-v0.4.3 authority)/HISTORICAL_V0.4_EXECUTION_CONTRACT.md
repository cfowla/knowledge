# v0.4 ChatGPT-Native Artifact Import Execution Contract

This contract is normative only for `ChatGptVerticalSliceRuntime` in the v0.4 development line. The v0.3.1 contract remains preserved in `contracts/v0.3.1/` and in the frozen v0.3.1 source archive.

## Objective

The only v0.4 acceptance path is:

```text
PMID
  -> ChatGPT discovers a lawful open-access PDF
  -> ChatGPT materializes the PDF as a local artifact
  -> runtime.import_artifact()
  -> Python PDF validation
  -> Python SHA-256
  -> Python provenance and manifest generation
  -> Python ATOM/SEA handoff
  -> SUCCESS
```

A controller loop reaching `SUCCESS` without a real acquired full-text PDF does not satisfy v0.4 acceptance.

## Authority boundary

ChatGPT or another host retrieval tool may discover and materialize a lawful open-access PDF without first receiving a raw HTTP request from Python. The host retrieval layer is responsible for discovery and byte materialization only.

Python remains authoritative for:

- accepting only a PMID as the requested identifier for this vertical slice;
- admitting the artifact through `runtime.import_artifact()`;
- source URL safety checks;
- PDF validation;
- SHA-256 calculation and integrity checks;
- provenance persistence;
- requested PMID binding and rejection of an explicitly conflicting resolved PMID;
- source version and license metadata persistence when supplied;
- run receipt and event journal generation;
- result manifest generation;
- ATOM/SEA PDF handoff generation;
- `SUCCESS`, `BLOCKED`, `FAILED`, and any future `EXHAUSTED` classification.

The current v0.4 slice does not claim full bibliographic identity validation from PDF contents. When stronger identity validation is added, it must remain a Python gate before `SUCCESS`.

## Required import record

`runtime.import_artifact()` must receive all of the following for v0.4:

```text
path                    local path to the materialized PDF
source_url              lawful source URL for the acquired PDF
discovery_provenance    non-empty record of how the source was discovered
acquisition_context     non-empty record containing:
                          open_access = true
                          lawful_access_basis = non-empty string
version                 publishedVersion, acceptedVersion, submittedVersion, or unknown
license                 license string when known, otherwise null
```

The runtime records the requested PMID itself. The artifact metadata binds the requested PMID, source URL, discovery provenance, and acquisition context to the SHA-256-addressed artifact.

## Critical-path exclusions

The following mechanisms are not part of the v0.4 acceptance path and must not run during a successful v0.4 vertical-slice acquisition:

- arbitrary raw HTTP fetching from Python;
- `ExternalFetchRequest` provider loops;
- batching;
- HTTP retries;
- provider-response caching as an acquisition mechanism;
- automatic provider exhaustion;
- Unpaywall;
- publisher crawling;
- institutional repository discovery;
- fallback provider selection;
- JATS, HTML, or plain-text artifact admission for acceptance;
- synthetic controller success as the primary acceptance criterion.

The existing v0.3.1 modules that implement those behaviors remain in the source tree for recoverability and regression compatibility. `ChatGptVerticalSliceRuntime.step()` does not call them.

Content-addressed local storage may continue to use the existing `DiskCache.store_object()` primitive. In the v0.4 slice that primitive is an artifact store for validated bytes, not a provider-response cache or retrieval strategy.

## Terminal-state rules

`SUCCESS` is permitted only after a v0.4 import record passes contract validation, the PDF bytes validate, the SHA-256 is recomputed and matches the admitted artifact, the manifest is written, and the ATOM/SEA PDF handoff is present.

`BLOCKED` means the host could not materialize or admit the required lawful OA PDF. `BLOCKED` never means provider exhaustion.

`FAILED` means the runtime contract, validation, integrity, or another Python-controlled step failed.

`EXHAUSTED` cannot be produced by the current v0.4 vertical slice. No provider policy is executed, so exhaustion cannot be proven. If an `EXHAUSTED` session state reaches `ChatGptVerticalSliceRuntime.step()`, the runtime converts it to `FAILED` as a protocol error.

## Provenance and evidence

A successful v0.4 run must preserve at least:

```text
RUN_RECEIPT.json
runtime_events.jsonl
session.json
runtime_status.json
terminal_outcome.json
output/<PMID>/fulltext.chatgpt_native_import.pdf
output/<PMID>/manifest.json
```

The manifest and journal must carry the artifact SHA-256 and recorded source/provenance context. Runtime-generated evidence outranks an assistant-written summary.

## Access policy

Only lawful open-access material may be admitted under this contract. Sci-Hub, credential bypass, paywall circumvention, and access-control circumvention are forbidden.
