# Processing report: 8. Obesity and Weight Management for the Prevention and Treatment of Diabetes: Standards of Care in Diabetes–2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s008.pdf`  
DOI: `10.2337/dc26-S008`  
SHA-256: `90f795ee4d77e537827cb099de04bfde415b1f18a21ee2a4eb8e1f0fc8bf4859`

## ATOM

- LiteratureAtoms: 91
- Shared publication ID: `05e529a7-cc09-5371-8460-9a6181294538`
- Atom counts by kind: `{"author_conclusion": 31, "limitation": 10, "other": 27, "quantitative_result": 23}`
- Semantic extraction runs: `{"ada-ppc-2026-dc26-s008-assessment-v1": 32, "ada-ppc-2026-dc26-s008-general-v1": 1, "ada-ppc-2026-dc26-s008-lifestyle-v1": 11, "ada-ppc-2026-dc26-s008-pharmacotherapy-v1": 12, "ada-ppc-2026-dc26-s008-surgery-v1": 13, "ada-ppc-2026-dc26-s008-tables-v1": 15, "ada-ppc-2026-dc26-s008-type1-v1": 7}`
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate canonical statements: 0
- Duplicate statement-anchor pairs: 0

Guideline boundary: recommendations are represented as panel/guideline statements using `author_conclusion` plus `guideline_recommendation` tags. Quantitative effects summarized from trials, cohorts, reviews, and registries are tagged `secondary_reported_result`; the chapter is not represented as if it enrolled those populations.

## SEA

- Source type: clinical practice guideline / Standards chapter
- Substantive coverage: S166-S177
- Figures reconciled: 0/0
- Tables reconciled: 2/2 (Tables 8.1-8.2)
- Algorithms/workflows reconciled: 0/0
- External methodology document: not supplied; limitation preserved
- Verdict: `Read first`
- SEA QA: PASS

## Reference queue

- Bibliography entries extracted: 191
- P0 direct support for central weight-management, pharmacotherapy, surgery, safety, or type 1 diabetes claims: 60
- P1 current high-value supporting evidence: 75
- P2 contextual/historical/supporting evidence: 56

## Extraction limitations / schema gaps

- The LiteratureAtom schema has no dedicated `guideline_recommendation` atom kind, so recommendations use `author_conclusion` with descriptive tags as permitted by the large-source workflow.
- The current quantitative-result schema is oriented toward primary studies; secondary narrative ranges and dated price snapshots that do not map cleanly to a single estimate were preserved as `other` atoms rather than forcing artificial numeric structure.
- The ADA evidence-grade definitions and full guideline-development method are delegated to the separate Introduction and Methodology and were not supplied in this input.
- Bibliography entries were not atomized; they were preserved as a reference task queue.
- No external verification was performed; this workflow is grounded in the supplied source and project protocols.

## Protocol/version note

The project designates `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing SEA source. The file's internal heading identifies Integrated Compact v3; the workflow follows the v4-named project source as authoritative and records the mismatch rather than silently reconciling it.

## Drive lifecycle

- ATOM/validation/coverage/crosswalk/SEA-QA JSON files: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`.
- SEA HTML: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`.
- Reference task queue and processing report: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`.
- `dc26s008.pdf` was moved from `10 - Active Literature / 1 - American Diabetes Association 2026` to `90 - Processed / Clinical Medicine & Pharmacy / 47 - American Diabetes Association 2026`; the destination parent was verified after the move.
- Concurrent ADA processing was active during this run. At final reconciliation, the live active ADA folder contained 8 remaining section PDFs, and `TBR - Current Task Queue` was reconciled to 8 in both the Active Literature snapshot and Actionable work list.
