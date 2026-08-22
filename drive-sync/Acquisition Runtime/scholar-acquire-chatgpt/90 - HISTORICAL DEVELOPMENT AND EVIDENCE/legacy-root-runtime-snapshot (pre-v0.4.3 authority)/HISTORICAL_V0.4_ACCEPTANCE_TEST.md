# v0.4 Primary Acceptance Test

The v0.4 primary acceptance test is a real full-text acquisition. Synthetic controller execution is not acceptance.

## Acceptance input

Choose one PMID with a lawful open-access full-text PDF. Using ChatGPT retrieval tools outside Python:

1. resolve or confirm the PMID;
2. discover a lawful open-access PDF;
3. materialize the actual PDF bytes to a local file;
4. record the source URL, discovery provenance, lawful access basis, OA status, source version, and license when known.

Do not invoke fallback providers. One successful source is sufficient for this vertical slice.

## Acceptance command

```bash
PYTHONPATH=src python scripts/v04_acceptance.py \
  --pmid <PMID> \
  --pdf /path/to/real-full-text.pdf \
  --source-url '<LAWFUL_OA_PDF_URL>' \
  --root ./v04-acceptance \
  --discovery-provenance-json '<JSON_OBJECT>' \
  --acquisition-context-json '{"open_access":true,"lawful_access_basis":"<basis>"}' \
  --version publishedVersion \
  --license '<license-if-known>'
```

## Exact pass contract

The run passes only when all conditions below are true:

1. The requested identifier is a PMID.
2. The input file is the real acquired full-text PDF, not a generated fixture or mocked response.
3. `runtime.import_artifact()` receives `source_url`, non-empty `discovery_provenance`, and `acquisition_context` with `open_access=true` and a non-empty `lawful_access_basis`.
4. Python accepts the URL under the source safety policy and validates the PDF bytes.
5. Python computes the artifact SHA-256 and later recomputes it before finalization with an exact match.
6. The result contains exactly the admitted PDF in the v0.4 acceptance path and has zero provider attempts.
7. No `ExternalFetchRequest` is emitted or ingested, Python fetch history is empty, and no provider orchestration executes.
8. `manifest.json` records the requested PMID, source URL, discovery provenance, acquisition context, source version, license when supplied, local artifact path, and SHA-256.
9. `RUN_RECEIPT.json` and `runtime_events.jsonl` exist. The journal records artifact import, artifact validation, manifest write, and terminal success.
10. The ATOM/SEA handoff has `preferred_pdf_path` and `pdf_sha256`, and its hash equals the manifest artifact hash.
11. The terminal state is `SUCCESS`.
12. The terminal outcome has an empty provider policy, zero provider attempts, and `provider_exhaustion_confirmed=false`.

If any condition fails, the v0.4 acceptance gate fails.

## Required negative regression checks

The unit suite must also verify that v0.4 rejects a non-PDF import, rejects missing source/provenance/OA context, rejects an explicitly conflicting resolved PMID, never calls provider orchestration, and preserves `BLOCKED != EXHAUSTED`.

## What does not count

The v0.3.1 synthetic acceptance test remains useful as a historical controller regression. It does not satisfy the v0.4 primary acceptance gate. A mocked PDF, a fabricated PDF fixture, a provider-loop `SUCCESS`, or successful Python execution without a real acquired full-text PDF also does not satisfy the gate.
