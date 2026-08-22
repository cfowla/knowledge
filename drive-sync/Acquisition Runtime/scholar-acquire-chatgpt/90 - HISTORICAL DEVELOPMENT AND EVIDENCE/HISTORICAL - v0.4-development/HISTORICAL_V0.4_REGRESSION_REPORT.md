# v0.4 Prompt 5 Regression Report

Run date: 2026-08-21

## Exit-gate result

The ten-PMID regression completed with defensible item-level states and zero false successes. Five articles produced validated, hashed full-text PDFs. Five were BLOCKED by transport/access barriers that prevented a defensible exhaustion claim. No item was marked EXHAUSTED or FAILED.

| Metric | Result |
|---|---:|
| PMIDs | 10 |
| SUCCESS | 5 (50%) |
| BLOCKED | 5 (50%) |
| EXHAUSTED | 0 |
| FAILED | 0 |
| Identity mismatch rate | 0% |
| False-success rate | 0% |
| Item manifest/provenance completeness | 100% |
| Successful-item manifest/provenance completeness | 100% |
| Median recorded route/tool actions per PMID | 2 |
| Median Python evidence-replay/finalization time | 9.078 ms |
| End-to-end discovery time | Not consistently measurable from host tooling |
| JATS + PDF successes | 0/5 |
| PDF-only successes | 5/5 (100%) |
| ATOM/SEA handoff ready | 5/5 successes |
| Batch-equivalent to individual runs | 10/10 |

## Ten-PMID set

| PMID | Resolved identity | Terminal state | Payload / blocking evidence | Successful route |
|---|---|---|---|---|
| 38330007 | DOI 10.1371/journal.pone.0297969; PMCID PMC10852342 | SUCCESS | Published PLOS PDF; JATS endpoint returned XML but host materializer rejected XML MIME | publisher_oa |
| 39110712 | DOI 10.1371/journal.pone.0304519; PMCID PMC11305534 | SUCCESS | Published PLOS PDF | publisher_oa |
| 36897886 | DOI 10.1371/journal.pone.0280342; PMCID PMC10004557 | SUCCESS | Published PLOS PDF | publisher_oa |
| 24678906 | DOI 10.1186/1475-2840-13-65; PMCID PMC4021346 | SUCCESS | Published Springer/BMC PDF, CC BY 2.0 | publisher_oa |
| 29595130 | DOI 10.1136/bmjebm-2018-110919 | SUCCESS | UCL accepted manuscript PDF | repository |
| 30377149 | DOI 10.1136/bmjebm-2018-111018 | BLOCKED | Accepted-manuscript repository location identified; file response 403 | — |
| 20566676 | DOI 10.2337/dc10-0612; PMCID PMC2945163 | BLOCKED | PMC transport challenge; publisher OA retrieval 403 | — |
| 39254529 | DOI 10.1093/jamia/ocae236; PMCID PMC11631140 | BLOCKED | PMC reCAPTCHA; OUP OA HTML readable but JATS/PDF not materializable through host | — |
| 24929430 | DOI 10.2337/dc13-3055 | BLOCKED | Publisher identified as OA but host retrieval returned 403 | — |
| 24622369 | DOI 10.1016/S2213-8587(13)70084-6 | BLOCKED | Publisher full text not established as OA; Unpaywall route could not be executed, so repository exhaustion was not asserted | — |

## Route performance

| Route | Items attempted | Successful items | Success rate among attempted |
|---|---:|---:|---:|
| PMC | 10 | 0 | 0% |
| Publisher OA | 10 | 4 | 40% |
| Unpaywall | 3 | 0 | 0% |
| Institutional repository | 2 | 1 | 50% |

The zero PMC and Unpaywall success rates are transport findings, not evidence that the scholarly sources lack content. PMC's supported machine services provide reusable JATS/XML and PDFs for eligible content, and PLOS exposes individual JATS XML by DOI. The regression therefore treats these unresolved routes as BLOCKED where appropriate rather than EXHAUSTED.

## BLOCKED categories

- `repository_http_403`: 1
- `publisher_http_403`: 2
- `response_not_materializable`: 1
- `unpaywall_transport_or_configuration`: 1

## ATOM/SEA handoff

Every SUCCESS produced an `AtomSeaHandoff` object with a real preferred PDF path, matching SHA-256, and a manifest path. Fresh readback hashes matched all five handoff hashes. No successful item produced structured JATS in the ChatGPT-native first pass, so all five reusable handoffs are PDF-only.

## Batch equivalence

The batch implementation is a mapping wrapper over the same `replay_case -> acquire_one()` semantics. The ten individual semantic signatures were compared against the ten batch signatures. All 10 were equal. Batch mode introduced no item-level acquisition policy and did not change identity, attempts, artifacts, hashes, handoff hashes, or terminal semantics.

## Evidence artifacts

Machine-readable evidence is in the Prompt 5 evidence bundle:

- `regression_cases.json`
- `individual_report.json`
- `individual_integrity_checks.json`
- `atom_sea_handoff_evidence.json`
- `final_regression_report.json`
- `batch_equivalence.json`
- all individual session receipts, event journals, manifests, and successful payloads
- batch manifest and item sessions
