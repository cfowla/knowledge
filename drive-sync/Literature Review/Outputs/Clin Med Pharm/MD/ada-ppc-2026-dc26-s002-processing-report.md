# Processing report: 2. Diagnosis and Classification of Diabetes: Standards of Care in Diabetes—2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s002.pdf`  
DOI: `10.2337/dc26-S002`  
SHA-256: `18788684cf8b12802e39d33929bf6e230fc2d120cf34b62a290608188c73412b`

## ATOM

- LiteratureAtoms: 109
- Shared publication ID: `d37d8ce3-f4e8-536d-8a61-4c15d025eff6`
- Atom counts by kind: `{"author_conclusion": 50, "limitation": 5, "other": 40, "quantitative_result": 14}`
- Semantic extraction runs: `{"ada-ppc-2026-dc26-s002-cancer-v1": 6, "ada-ppc-2026-dc26-s002-classification-v1": 1, "ada-ppc-2026-dc26-s002-diagnosis-v1": 6, "ada-ppc-2026-dc26-s002-evidence-v1": 30, "ada-ppc-2026-dc26-s002-figure-v1": 1, "ada-ppc-2026-dc26-s002-gdm-v1": 8, "ada-ppc-2026-dc26-s002-monogenic-v1": 3, "ada-ppc-2026-dc26-s002-pancreatic-v1": 5, "ada-ppc-2026-dc26-s002-tables-v1": 28, "ada-ppc-2026-dc26-s002-transplant-v1": 3, "ada-ppc-2026-dc26-s002-type1-v1": 7, "ada-ppc-2026-dc26-s002-type2-v1": 11}`
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate canonical statements: 0
- Duplicate statement-anchor pairs: 0

Guideline boundary: recommendations are represented as panel/guideline statements (`author_conclusion` plus `guideline_recommendation` tags). Quantitative effects reported from trials, cohorts, reviews, and registries are tagged `secondary_reported_result`; the chapter is not represented as if it enrolled those populations.

## SEA

- Source type: clinical practice guideline / Standards chapter
- Substantive coverage: S27–S44
- Figures reconciled: 1/1 (Figure 2.1)
- Tables reconciled: 8/8 (Tables 2.1–2.8)
- Algorithms/workflows reconciled: 1/1 (Figure 2.1)
- External methodology document: not supplied; limitation preserved
- Verdict: `Read first`
- SEA QA: PASS

## Reference queue

- Bibliography entries extracted: 236
- P0 direct support for central diagnostic/prognostic/quantitative or screening-strategy claims: 88
- P1 current high-value supporting evidence: 109
- P2 contextual/historical/supporting evidence: 39

## Extraction limitations / schema gaps

- The LiteratureAtom schema has no dedicated `guideline_recommendation` atom kind, so recommendations use `author_conclusion` with descriptive tags as permitted by the large-source workflow.
- The current quantitative-result schema is oriented toward primary studies; secondary narrative ranges that do not map cleanly to a single estimate were preserved as `other` atoms rather than forcing artificial numeric structure.
- The ADA evidence-grade definitions and full guideline-development method are delegated to the separate Introduction and Methodology and were not supplied in this input.
- Bibliography entries were not atomized; they were preserved as a reference task queue.
- No external verification was performed; this workflow is grounded in the supplied source and project protocols.

## Protocol/version note

The project designates `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing SEA source. The file's internal heading identifies Integrated Compact v3; the workflow follows the v4-named project source as authoritative and records the mismatch rather than silently reconciling it.

## Drive lifecycle

- ATOM/validation/coverage/crosswalk/SEA-QA JSON files: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`.
- SEA HTML: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`.
- Reference task queue and processing report: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`.
- `dc26s002.pdf` moved from `10 - Active Literature / 1 - American Diabetes Association 2026` to `90 - Processed / Clinical Medicine & Pharmacy / 47 - American Diabetes Association 2026`; the destination parent was verified after the move.
- The active ADA folder retains 14 unprocessed section PDFs after this completion.
- `TBR - Current Task Queue` was updated from 15 to 14 remaining ADA section PDFs in both the Active Literature snapshot and Actionable work list.
