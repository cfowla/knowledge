# Processing report: 6. Glycemic Goals, Hypoglycemia, and Hyperglycemic Crises: Standards of Care in Diabetes—2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s006.pdf`  
DOI: `10.2337/dc26-S006`  
SHA-256: `b1c48fc72307878f099a5b5cce152807fe26aa87df12c8aaa7eae0f085b1479b`

## ATOM

- LiteratureAtoms: 138
- Shared publication ID: `e87718de-009e-5fed-9854-7e71a1257896`
- Atom counts by kind: `{"author_conclusion": 53, "conflict_of_interest": 1, "limitation": 5, "method": 1, "other": 71, "quantitative_result": 6, "study_objective": 1}`
- Semantic extraction runs: `{"ada-ppc-2026-dc26-s006-assessment-v1": 15, "ada-ppc-2026-dc26-s006-crises-v1": 16, "ada-ppc-2026-dc26-s006-evidence-v1": 16, "ada-ppc-2026-dc26-s006-figure-v1": 7, "ada-ppc-2026-dc26-s006-general-v1": 3, "ada-ppc-2026-dc26-s006-goals-v1": 13, "ada-ppc-2026-dc26-s006-hypoglycemia-v1": 27, "ada-ppc-2026-dc26-s006-tables-v1": 41}`
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate canonical statements: 0
- Duplicate statement-anchor pairs: 0

Guideline boundary: recommendations are represented as panel/guideline statements (`author_conclusion` plus `guideline_recommendation` tags). Quantitative effects reported from trials, cohorts, reviews, and registries are tagged `secondary_reported_result`; the chapter is not represented as if it enrolled those populations.

## SEA

- Source type: clinical practice guideline / Standards chapter
- Substantive coverage: S132–S144
- Figures reconciled: 1/1 (Figure 6.1)
- Tables reconciled: 8/8 (Tables 6.1–6.8)
- Algorithms/workflows reconciled: 1/1 (Figure 6.1 decision framework)
- External methodology document: not supplied; limitation preserved
- Verdict: `Read first`
- SEA QA: PASS

## Reference queue

- Bibliography entries extracted: 198
- P0 direct support for central glycemic-target, hypoglycemia, hyperglycemic-crisis, management, or quantitative claims: 109
- P1 current high-value supporting evidence: 67
- P2 contextual/historical/supporting evidence: 22

## Extraction limitations / schema gaps

- The LiteratureAtom schema has no dedicated `guideline_recommendation` atom kind, so recommendations use `author_conclusion` with descriptive tags as permitted by the large-source workflow.
- The current quantitative-result schema is oriented toward primary studies and one numeric effect estimate; secondary narrative ranges and operational thresholds that do not map cleanly were preserved as `other` atoms rather than forcing artificial numeric structures.
- ADA evidence-grade definitions and the full guideline-development method are delegated to the separate Introduction and Methodology and were not supplied in this input.
- Bibliography entries were not atomized; they were preserved as a reference task queue.
- No external verification was performed; this workflow is grounded in the supplied chapter and project protocols.
- Table 6.6 prices are explicitly source-dated to 1 July 2025 and were preserved as reported, not treated as current August 2026 pricing.

## Protocol/version note

The project designates `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing SEA source. The file's internal heading identifies Integrated Compact v3; the workflow follows the v4-named project source as authoritative and records the mismatch rather than silently reconciling it.

## Drive lifecycle

- ATOM/validation/coverage/crosswalk/SEA-QA JSON files: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`.
- SEA HTML: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`.
- Reference task queue and processing report: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`.
- Output upload/readback verification: PASS.
- `dc26s006.pdf` moved from `10 - Active Literature / 1 - American Diabetes Association 2026` to `90 - Processed / Clinical Medicine & Pharmacy / 47 - American Diabetes Association 2026`: PASS.
- Post-move active ADA folder contains 8 remaining section PDFs at final verification.
- `TBR - Current Task Queue` readback is reconciled to 8 remaining ADA section PDFs in both the Active Literature snapshot and Actionable work list. Multiple concurrent ADA processing runs completed during this task; the final state was verified against the authoritative folder rather than applying a stale decrement.
