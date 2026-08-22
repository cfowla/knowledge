# v0.4.3 Prompt 2 — Integrated Transport and Remote Execution Proof

## Result

**Hard gate: PASS.** Prompt 2 is complete. The repaired production controller now uses one schema-v2 transport request/response contract for native exact-byte materialization and remote execution. The remote executor is transport-only. Production `acquire_one()` can suspend on a correlated transport request and `resume_acquire_one()` can continue the same serialized acquisition after a correlated response arrives.

PMC remains **experimental**. This prompt proves transport, not route support; provider promotion is reserved for Prompt 3.

## Contract and controller changes

- Added `TransportRequest` and `TransportResponse` with request/correlation IDs, URL/method/headers/timeout, expected media type, route/provenance context, exact bytes or materialized path, byte count, transport SHA-256, timestamps, and transport errors.
- Added native and remote transport kinds behind the same `TransportRegistry`.
- Native exact-byte materialization is attempted first. A native no-bytes result records `not_materialized` and falls through to remote. A deferred remote request suspends the acquisition as `NEEDS_FETCH`.
- Added `resume_acquire_one()` for correlated response ingestion into the existing production session.
- Python retains all scholarly decisions: identity, OA/lawful admission, provider/route selection, media validation, PDF/JATS validation, SHA-256, terminal state, receipt/journal/manifest, and handoff construction.
- Wired existing `AcquisitionConfig.want_structured` and `want_pdf` flags into actual production policy.

## Real transport check 1 — native/remote parity

PMID **24782981** (`PMC3995050`, DOI `10.3389/fonc.2014.00064`) was used for an ordinary publisher-hosted OA PDF.

| Property | Native | Remote GitHub Actions |
|---|---:|---:|
| HTTP status | 200 | 200 |
| Bytes | 810,232 | 810,232 |
| SHA-256 | `54465e3c056b86551d8c5d865b0685d01a5f4fa2c11bc705a479768b3efc63cb` | `54465e3c056b86551d8c5d865b0685d01a5f4fa2c11bc705a479768b3efc63cb` |

Exact byte parity: **true**. The native production acquisition independently validated identity/PDF content and returned `SUCCESS`.

## Real transport check 2 — previously blocked machine endpoint

The production controller selected the PMC structured-full-text location:

`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3995050/fullTextXML`

Native materialization returned no exact bytes, so the registry fell through to the GitHub Actions remote transport. `acquire_one()` serialized a `NEEDS_FETCH` session. The remote worker returned HTTP 200 with **131,980 bytes** and transport SHA-256:

`f5be043577f1f27a2403586b269eeb66570fbc27f79c3f1fa1efa391c9199185`

`resume_acquire_one()` correlated and ingested that response. Python independently recomputed the same raw SHA-256, extracted/normalized the JATS `<article>`, verified DOI + PMID + PMCID + title with title similarity **1.0**, validated the structured payload, and wrote a canonical **120,534-byte** `article.xml` with SHA-256:

`0c637ff86f8582ca96341efe2ac21ad3162d352108ae3039cfef00fe750a8000`

The resumed acquisition ended in `SUCCESS`. The raw transport hash and normalized scholarly artifact hash are intentionally preserved separately.

## Remote execution proof

Remote execution occurred in GitHub Actions in `cfowla/Projects`, branch `acquisition-runtime-v043-prompt2-proof`, via draft PR #1. Final proof run **32540936432**, job **96950686843**, completed successfully on a hosted Ubuntu 24.04 runner. The preserved Actions artifact is ID **9466985839** with archive SHA-256:

`10d0542daa707ee9776bc021c50d494603db49fec1df71552da1d605d1988a32`

The worker performs transport only: GET/HEAD execution, response/header capture, exact bytes, byte count, checksum, timing, and transport-error serialization. It performs no identifier resolution, provider choice, OA determination, scholarly validation, terminal-state assignment, or acquisition-manifest generation.

## Tests

`PYTHONPATH=src pytest -q` → **20 passed, 0 failed**.

Coverage includes correlation failure, transport checksum failure, transport error → non-EXHAUSTED behavior, native-to-remote fallback, deferred suspension, resume with a correlated response, and remote-worker contract behavior.

## Hard gate

All eight Prompt 2 exit gates pass. Runtime-generated evidence is under `evidence/`, including portable native and remote session copies, request/response records, raw transport payloads, manifests, receipts, event journals, test output, source diff, and GitHub Actions artifact evidence.

## Discrepancies

1. **Prompt 1 transport metadata shape — fixed.** Prompt 1 stored `v0_4.transport` as the scalar `chatgpt_native`; Prompt 2 needs structured evidence. The scalar is migrated compatibly and retained as `legacy_transport_label`.
2. **Prompt 1 policy flags were inert — fixed.** `want_structured` and `want_pdf` existed but did not control acquisition policy. They now do.
3. **Initial native fallback semantics — fixed.** A native no-bytes result initially suspended instead of falling through. Native non-materialization now continues to remote; remote deferral is what suspends.
4. **Legacy transport API remains.** The older provider engine still contains schema-v1 `ExternalFetchRequest` for compatibility. It is outside the repaired production `acquire_one()` transport path. Removing it is a later compatibility cleanup, not a Prompt 2 gate failure.
5. **GitHub connector visibility.** The available connected action did not expose the initial push-triggered workflow run. A draft PR trigger was used so the live run, logs, and artifact could be retrieved and preserved.
6. **Raw XML and final JATS hashes differ by design.** Europe PMC transport bytes include the response form received from the endpoint; Python canonicalizes/extracts `<article>` before final artifact admission. Both hashes are retained and independently verified.
