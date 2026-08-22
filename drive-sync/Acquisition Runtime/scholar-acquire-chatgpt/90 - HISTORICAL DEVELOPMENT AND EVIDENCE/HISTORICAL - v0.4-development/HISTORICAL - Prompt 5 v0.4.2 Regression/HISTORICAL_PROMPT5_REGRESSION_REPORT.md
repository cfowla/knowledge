# v0.4.2 Prompt 5 Ten-PMID Regression Report

## Result

Ten PMIDs were executed individually through `acquire_one()` before any batch run. The same ten immutable `AcquisitionSpec` inputs were then mapped through `ChatGptBatchRuntime`, which delegates each item to the unchanged `acquire_one()` function.

- Individual states: 7 SUCCESS, 3 BLOCKED, 0 EXHAUSTED, 0 FAILED.
- Successful full-text acquisition rate: 70%.
- Identity mismatch rate: 0%.
- False-success rate: 0%.
- BLOCKED rate: 30%; all three were `RESPONSE_NOT_MATERIALIZABLE` transport limitations, not provider exhaustion.
- Median host discovery/materialization actions: 4 per PMID.
- Median Python runtime time after host evidence/payload preparation: 67 ms. This is not an end-to-end network timing.
- Successful payload composition: 0/7 JATS+PDF, 7/7 PDF-only.
- Manifest/provenance evidence completeness: 10/10.
- ATOM/SEA handoff acceptance: 7/7 successful acquisitions.
- Batch semantic equivalence: 10/10.

## Item-level regression

| PMID | Focused route(s) | State | Payload / reason | SHA-256 |
|---|---|---|---|---|
| 24782981 | publisher OA | SUCCESS | Frontiers published PDF | `54465e3c056b86551d8c5d865b0685d01a5f4fa2c11bc705a479768b3efc63cb` |
| 28533778 | publisher OA | SUCCESS | Frontiers published PDF | `d8bce2e1205525af205cec0e5f7635c131ee5532573e7475ab005a6dbf477af2` |
| 30222367 | institutional repository | SUCCESS | UC eScholarship published PDF | `8248d64f283149d06a4751194742a623311354643362130138dddf7fc70d67c3` |
| 35124914 | publisher OA | SUCCESS | J Ayub Med Coll published PDF | `ab78e51b14f699031878882162fa442503f58d1212df2ae2a8a627ece5ef9cb4` |
| 35872985 | publisher OA | SUCCESS | Frontiers published PDF | `c55648b46927ae44843e3642f616455496bb2f2c6c5cdf0e09ad877030a959fd` |
| 37234376 | publisher OA | SUCCESS | Frontiers published PDF | `0bd8d183179d45de0097785a434ba4245ab37c3872371887bab342ac5727be49` |
| 39114558 | publisher OA | SUCCESS | Frontiers published PDF | `652d18a9245c7d000e746676fd1f9b8e67af3e69150b5440a098627b6059fce2` |
| 41623473 | PMC structured JATS | BLOCKED | Official PMC AWS metadata proves CC BY JATS+PDF availability, but host could not materialize XML bytes | — |
| 20566676 | PMC PDF | BLOCKED | Exact PMC OA article resolved; linked PDF bytes could not be materialized by current host transport | — |
| 24766495 | PMC → publisher → Unpaywall → repository | BLOCKED | No exact lawful payload materialized; Unpaywall/repository coverage remained non-definitive, so EXHAUSTED was prohibited | — |

## Route-specific results

The denominator is the number of regression cases in which that route flag was enabled. A route success is counted only when a payload admitted to the successful result names that route as its provider.

- PMC: 0/3 (0%). All failures were transport/materialization or no-PMCID discovery; this route is **not live-proven in the current ChatGPT-native environment**.
- Publisher OA: 6/7 (85.7%). Six direct publisher PDFs succeeded; the seventh was the deliberately difficult Wiley case.
- Unpaywall: 0/1 (0%). The DOI redirect/API transport could not be materialized by the current host, so this route is **not live-proven**.
- Institutional repository: 1/2 (50%). UC eScholarship succeeded; the difficult case had no definitive exact repository result.

## Identity and false-success gate

Every successful payload was independently checked against a trusted article identity before admission. DOI plus title matched for six successful cases; the DOI-less J Ayub article matched by full title. No successful payload had an identity conflict.

A separate negative control injected the real PMID 28533778 PDF into a PMID 24782981 acquisition. The runtime returned `FAILED / IDENTITY_MISMATCH` and admitted zero artifacts. This negative control is outside the ten-PMID outcome metrics.

## ATOM/SEA handoff

After all individual acquisitions completed, each of the seven successes was passed to `prove_atom_sea_handoff()`. The consumer-side proof reopened the handed-off local payload, revalidated PDF format, recomputed SHA-256, confirmed the acquisition manifest path, and wrote `ATOM_SEA_HANDOFF.json`. All seven were accepted.

No JATS payload was successfully materialized in this host environment. Consequently all seven successful handoffs are PDF-only. The acquisition interface already prefers `article.xml` and supplies `article.pdf` second when both are present, but a real JATS handoff remains to be demonstrated after transport is repaired.

## Batch equivalence

Batch mode was introduced only after the ten individual runs and handoff checks. `ChatGptBatchRuntime.run()` maps the immutable input specs to the same `acquire_one()` function and adds only batch-level receipt/event/manifest aggregation.

Semantic fingerprints exclude session IDs, output paths, and timestamps, and include state, resolved IDs, artifact format/provider/source/hash/version/license, route attempts, terminal semantics, and handoff payload hashes. All 10 batch fingerprints exactly matched their individual-run fingerprints.

## Remote transport decision

**Decision: a minimal remote transport worker is necessary to support the intended full route set.** The acquisition brain remains in Python.

Evidence:

1. Official PMC 2026 AWS documentation identifies a world-readable JATS XML and PDF for PMID 41623473 / PMCID PMC12855588.1, with CC BY metadata. The current browser transport could discover the location but could not materialize the arbitrary XML object; the local Python/container runtime has no outbound network transport.
2. PMID 20566676 resolves to a lawful PMC OA article and exposes its PDF link, but the current host did not return the PDF bytes.
3. Direct Unpaywall DOI transport could not be materialized reliably in the current host.
4. Direct publisher PDFs and the UC eScholarship repository PDF *were* materializable and then passed identity, validation, hashing, provenance, manifest, and ATOM/SEA gates. This isolates the failure to transport rather than `acquire_one()` semantics.

The implemented worker accepts one pre-authorized GET/HEAD request and returns only status, final URL, headers, exact response bytes (base64), byte count, SHA-256, timestamps, and transport errors. It has no PMID/DOI resolution, provider ordering, OA decision logic, validation, hashing policy, terminal-state logic, manifest logic, or ATOM/SEA logic. A GitHub Actions workflow wraps the worker with `workflow_dispatch` and a one-day response artifact.

## Hard-exit assessment

1. **PASS:** ten heterogeneous PMIDs have defensible item-level states.
2. **PASS:** zero false SUCCESS results; negative-control mismatch was rejected.
3. **PASS:** all successful items produce reusable, hash-verified ATOM/SEA inputs.
4. **PASS:** batch outputs are semantically equivalent to individual `acquire_one()` outputs (10/10).
5. **PASS:** remote-transport decision is evidence-based; minimal transport worker implemented and locally contract-tested.
6. **PASS:** v0.4.2 architecture and current limitations are documented.

A separate support declaration remains intentionally narrower than the hard-exit state gate: publisher OA and institutional-repository acquisition are live-proven under ChatGPT-native transport; PMC JATS/PDF and Unpaywall are not declared live-supported until the remote worker is exercised against those real routes.
