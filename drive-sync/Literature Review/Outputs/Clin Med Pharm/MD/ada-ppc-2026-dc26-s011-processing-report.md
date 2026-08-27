# Processing report: 11. Chronic Kidney Disease and Risk Management: Standards of Care in Diabetes—2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s011.pdf`  
Drive file ID: `1EPrRFZURpJCSViy6knv9bRnTCxLZlPLW`  
DOI: `10.2337/dc26-S011`  
SHA-256: `e7074ab840ff25a020f64edbf0baf39d68783a701c557fe410289459a76b1568`

## Prewalk

- Source verified as a direct child of `10 - Active Literature / 1 - American Diabetes Association 2026`: PASS.
- Exact GitHub searches for `dc26s011` and `dc26-s011` found no pre-existing Section 11 output family suitable for reuse.
- Historical ADA section outputs were used only to confirm current directory/serialization conventions, not as substantive content or completion evidence.

## ATOM

- LiteratureAtoms: 110
- Shared publication ID: `7d4d850a-699a-5af0-8988-772b4c4bc2cf`
- Atom counts by kind: `{"adverse_event": 2, "author_conclusion": 25, "limitation": 5, "method": 1, "other": 61, "quantitative_result": 16}`
- Semantic extraction runs: `{"ada-ppc-2026-dc26-s011-aki-v1": 4, "ada-ppc-2026-dc26-s011-assessment-v1": 5, "ada-ppc-2026-dc26-s011-blood-pressure-v1": 2, "ada-ppc-2026-dc26-s011-combination-v1": 4, "ada-ppc-2026-dc26-s011-diagnosis-v1": 1, "ada-ppc-2026-dc26-s011-dialysis-v1": 5, "ada-ppc-2026-dc26-s011-direct-kidney-effects-v1": 2, "ada-ppc-2026-dc26-s011-figures-v1": 8, "ada-ppc-2026-dc26-s011-finerenone-v1": 9, "ada-ppc-2026-dc26-s011-general-v1": 1, "ada-ppc-2026-dc26-s011-glycemia-v1": 3, "ada-ppc-2026-dc26-s011-nutrition-v1": 2, "ada-ppc-2026-dc26-s011-pregnancy-v1": 2, "ada-ppc-2026-dc26-s011-prevention-v1": 2, "ada-ppc-2026-dc26-s011-ras-v1": 3, "ada-ppc-2026-dc26-s011-recommendations-v1": 25, "ada-ppc-2026-dc26-s011-referral-v1": 2, "ada-ppc-2026-dc26-s011-severe-ckd-v1": 2, "ada-ppc-2026-dc26-s011-sglt2-glp1-evidence-v1": 11, "ada-ppc-2026-dc26-s011-staging-v1": 2, "ada-ppc-2026-dc26-s011-surveillance-v1": 2, "ada-ppc-2026-dc26-s011-tables-v1": 13}`
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate canonical statements: 0
- Duplicate statement-anchor pairs: 0

Guideline boundary: recommendations are represented as panel/guideline statements (`author_conclusion` plus `guideline_recommendation` tags). Trial, cohort, meta-analysis, and registry findings reported by the chapter are tagged `secondary_reported_result`; the chapter is not represented as if it enrolled those populations.

## SEA and reconciliation

- Source type: clinical practice guideline / Standards chapter
- Substantive coverage: S246–S257
- Numbered recommendation statements reconciled: 19/19
- Figures reconciled: 2/2 (Figures 11.1–11.2)
- Tables reconciled: 3/3 (Tables 11.1–11.3)
- Algorithms/workflows reconciled: 1/1 (Figure 11.2 holistic treatment workflow)
- Bibliography references reconciled: 159/159
- Crosswalk: PASS
- SEA QA: PASS
- Verdict: `Read first`

## Reference queue

- Bibliography entries extracted: 159
- P0 direct support for central CKD assessment/monitoring, BP/RAS, SGLT2/GLP-1, finerenone/combination, severe-CKD/dialysis/referral, or quantitative claims: 86
- P1 current high-value supporting evidence: 34
- P2 contextual/historical/supporting evidence: 39

## Extraction limitations / schema gaps

- The LiteratureAtom schema has no dedicated `guideline_recommendation` atom kind, so recommendations use `author_conclusion` with descriptive tags as permitted by the large-source workflow.
- The quantitative-result schema is oriented toward primary-study effect structures; secondary narrative ranges, surrogate changes, and comparisons without a clean single effect estimate are preserved as `other` or `limitation` atoms rather than forcing artificial numeric structure.
- Cited primary studies were not independently read in this pass; all study results remain secondary reports anchored to `dc26s011.pdf`.
- ADA evidence-grade definitions and the full guideline-development method are delegated to the separate Introduction and Methodology and were not supplied in this source packet.
- No external verification was performed; the workflow is grounded in the supplied chapter and project sources.

## Protocol/version note

The project designates `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing SEA source. The file's internal heading identifies Integrated Compact v3; the v4-named project source was treated as authoritative according to project precedence and the mismatch was recorded rather than silently reconciled.

## Output locations

- JSON: `drive-sync/Literature Review/Outputs/Clin Med Pharm/JSON/ada-ppc-2026-dc26-s011-atoms.json`, `-validation.json`, `-coverage.json`, `-crosswalk.json`, `-sea-qa.json`
- HTML: `drive-sync/Literature Review/Outputs/Clin Med Pharm/HTML/ada-ppc-2026-dc26-s011-sea.html`
- Markdown: `drive-sync/Literature Review/Outputs/Clin Med Pharm/MD/ada-ppc-2026-dc26-s011-reference-task-queue.md`, `-processing-report.md`

## Publication gate / lifecycle state

- Analytical gate: **PASS**
- Pre-promotion state: `READY FOR PROMOTION`
- Source remains in Active at this report revision.
- Target processed folder verified by Drive ID `1YSKH6Oqj52tYPN402sa9mxs_RFzGhNlG` under the existing processed Clinical Medicine & Pharmacy hierarchy.
- Lifecycle move: **NOT YET EXECUTED**. Move is permitted only after GitHub write/readback verification of the exact Section 11 output family.
