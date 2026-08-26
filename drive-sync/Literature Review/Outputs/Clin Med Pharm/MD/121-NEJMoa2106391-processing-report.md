# 121 - NEJMoa2106391 processing report

Status: `PASS - ATOM/SEA VERIFIED`

Audit scope: exactly one publication packet.

## Source audit

- Primary source: `NEJMoa2106391.pdf`, Drive ID `1IGKRhSSAL2Xu266gG0R6zouEUm-sTNmK`, 12 pages, SHA-256 `f4c1b20e7a003d50b197a85a02129b233b80a132f50d65230b16610f2ff9e573`. The PDF is usable and complete for the published article.
- Identity: Adjuvant Pembrolizumab after Nephrectomy in Renal-Cell Carcinoma.
- Citation: N Engl J Med. 2021;385:683-694.
- DOI: `10.1056/NEJMoa2106391`.
- Trial registration: `NCT03142334`.
- Supplementary appendix: `nejmoa2106391_appendix.pdf`, Drive ID `1UMNM92DHGOzg6pDf7GwlzejKsRXqDNHT`, 41 pages, SHA-256 `e91d5705a00e799a75d4ef2a8e9d23a48c6cc4c2bfe31f94363efafeb35b1a97`.
- Protocol package: `nejmoa2106391_protocol.pdf`, Drive ID `1dwfMfrKlGHTqPUGaeQiq9SBo2MyA-QHi`, 270 pages, SHA-256 `67df17697c171e658edf8c9878b3974a55aebfc7fac4fa0b7dceffdb2b5019ff`. It contains the initial protocol and final protocol amendment 564-04 dated October 13, 2020.
- Combined packet SHA-256: `488dc0dcfb5a9fede64c6c5f17dcfe2f0801b671711d63f36fc9f5fca73656f2`.
- No identity-matched prior ATOM, SEA, validation, coverage, reference, or processing output was found before regeneration. Searches used the exact title, DOI, trial identifier, article identifier, packet number, source metadata, and content. Unrelated citation mentions were rejected.

## ATOM validation

- Atoms: 76.
- Shared publication ID: `fb65cd18-38d0-58d6-b888-5df30254bb38`.
- Atom IDs are unique.
- Required order executed: `literature(1).py` Pydantic structural validation, `literature_atom.schema.json` JSON Schema validation, then `literature_atoms(1).py` atom-kind sufficiency validation.
- The supplied authoritative validator files were executed directly. No reconstructed validation contract was used.
- Structural errors: 0.
- JSON Schema errors: 0.
- Sufficiency errors: 0.
- Sufficiency warnings: 0.
- Provenance, source anchors, packet hash integrity, and merge integrity: pass.
- Model-extracted atoms remain `needs_review` because no independent human reviewer identity is represented. This does not change the zero-error structural and sufficiency result.

Direct semantic checks passed for the primary DFS result, 24-month DFS estimates, OS estimate, treatment-related grade 3 to 5 adverse events, Figure 1 subgroup estimates, and the supplementary DFS sensitivity analysis.

## SEA and source coverage

- SEA HTML parses cleanly and contains source metadata, trial design and methods, main claims, quantitative findings, limitations and uncertainty, appraisal, visual reconciliation, and provenance.
- Primary article: 12 of 12 pages rendered and visually scanned. Figure 1 and Figure 2 were reconciled. Tables 1 through 3 were reconciled.
- Supplementary appendix: 41 of 41 pages rendered and visually scanned. Figures S1 through S5 and Tables S1 through S8 were reconciled. The investigator roster was inspected but not reproduced.
- Protocol package: 270 of 270 pages text-mapped. Sixty-five material pages were rendered and visually inspected. The final protocol synopsis, eligibility, treatment assignment, recurrence assessment, censoring rules, analysis strategies, interim timing, multiplicity graph, and efficacy boundaries were represented. Historical duplicate operational material was mapped but not reproduced.
- Semantic checks passed for the primary DFS conclusion, a numerical safety claim, the immature OS and follow-up limitation, a Figure 1 subgroup estimate, a supplement-derived safety claim, and protocol-derived censoring and multiplicity methods.

## Source-integrity findings

1. The final 564-04 amendment change summary says all imaging should receive blinded independent central review. Final protocol section 9.2.1 still says a blinded audit for a subset, while section 10.2 uses the all-imaging wording. This does not alter investigator-assessed DFS as the reported primary endpoint.
2. The final protocol expected the first DFS interim analysis near 265 events and shows an expected-event one-sided boundary of p=0.0122. The article analyzed 260 qualifying DFS events and reports the actual one-sided boundary of 0.0114. The protocol says boundaries are adjusted to the actual event count. The packet does not otherwise narrate the event-count difference.
3. Supplement Tables S1 and S2 identify small numbers of protocol violations in the M0 and M1 NED strata. They remain explicit in the artifacts rather than being silently normalized.

No consequential contradiction between ATOM and SEA requires repair. Both use the same source packet, hashes, publication identity, and source-integrity treatment.

## Reference processing

- Main article references: 40 of 40 reconciled.
- Supplement references: 5 of 5 reconciled. Three supplement references duplicate main references, leaving 42 unique cited works in the packet.
- Every unique cited work has a recorded source role, priority, and downstream action.
- The reference-processing step for this publication packet is complete. Unchecked queue items are downstream cited-publication work and do not mean this packet's bibliography reconciliation is incomplete.

## Artifact locations

- ATOM JSON: https://drive.google.com/file/d/1int9tcYH1MKULjkDE1d6_3BJag0S_yHB/view?usp=drivesdk
- ATOM validation JSON: https://drive.google.com/file/d/1UUcwXGlEfhoRjAdEq2W4MJeze0nT56uq/view?usp=drivesdk
- Coverage JSON: https://drive.google.com/file/d/10blJmVFW5ZqDH-yIsnun4cQpWuZl6Ywm/view?usp=drivesdk
- SEA QA JSON: https://drive.google.com/file/d/1yPbvMtZrn2Dt4eeYYahBPqSDrUPcjcJM/view?usp=drivesdk
- SEA HTML: https://drive.google.com/file/d/1OM5AAJwBxNw_mpBEAMlIHOLvruEJh8Pw/view?usp=drivesdk
- Reference task queue: https://drive.google.com/file/d/1zNDw0z32wI4rdu6BSTaqhb8tNfCk5_rU/view?usp=drivesdk

All six core artifacts were fetched back from Drive after upload and matched the locally validated files byte for byte.

## Governing sources

- ATOM structural validation: `literature(1).py`.
- ATOM serialization: `literature_atom.schema.json`.
- ATOM sufficiency: `literature_atoms(1).py`.
- Workflow intent: `README(2).md`.
- Example atom: illustrative only.
- SEA: `summary-evaluation-appraisal-protocol-v4-compact.md`.
- Large-source coverage: `large-source-ATOM-SEA.md`.
- Historical SEA v3 HTML: reference only.
- Prose control: `unslop.skill.md`.
- External web verification: not used.

## Lifecycle

- Eligibility: all current source, ATOM, SEA, coverage, reference, report, and Drive-readback gates pass.
- Action: `MOVED AND VERIFIED` in `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`.
- Folder name preserved: `121 - NEJMoa2106391`.
- Folder Drive ID preserved: `1Rvtg3jCzfLqWyY6tjvn5AjpRFwmB8s8S`.
- Previous parent: `1wA_mmV9fJvfM7ILPwPuc-Uac1SJ1hpk0`.
- New parent: `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`.
- Verification: folder metadata shows only the Processed Clinical Medicine & Pharmacy parent. Exact-name search finds the packet under Processed and no result under the former Active parent.
- Processing report JSON: https://drive.google.com/file/d/1CMc3PJUnsmNpEQ7WBukeMBjjbbx4-7LO/view?usp=drivesdk
- Processing report Markdown: https://drive.google.com/file/d/1Op3QdbJr_tnUZZL6dFO9v1QLRtOVsp7k/view?usp=drivesdk
- Exact remaining task: none for this publication packet. Reference-queue items are downstream cited-publication work outside this closed packet.

Finalized: 2026-08-25T09:56:10Z.
