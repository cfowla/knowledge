# Processing report: 5. Facilitating Positive Health Behaviors and Well-being to Improve Health Outcomes: Standards of Care in Diabetes—2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s005.pdf`  
DOI: `10.2337/dc26-S005`  
SHA-256: `e8470b3ec50b2c1481ecb3535986197483f611093dbcb6639bd642d5430b63de`

## ATOM

- LiteratureAtoms: 114
- Shared publication ID: `b4510273-634c-5715-8e0e-94ec91dd3ab4`
- Atom counts by kind: `{"author_conclusion": 72, "limitation": 2, "other": 40}`
- Semantic extraction runs: `{"ada-ppc-2026-dc26-s005-dsmes-v1": 14, "ada-ppc-2026-dc26-s005-fasting-v1": 4, "ada-ppc-2026-dc26-s005-general-v1": 2, "ada-ppc-2026-dc26-s005-mental-health-sleep-v1": 15, "ada-ppc-2026-dc26-s005-nutrition-v1": 33, "ada-ppc-2026-dc26-s005-physical-activity-v1": 13, "ada-ppc-2026-dc26-s005-psychosocial-v1": 17, "ada-ppc-2026-dc26-s005-tobacco-cannabis-v1": 7, "ada-ppc-2026-dc26-s005-visuals-v1": 9}`
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate canonical statements: 0
- Duplicate statement-anchor pairs: 0

Guideline boundary: recommendations are represented as panel/guideline statements (`author_conclusion` plus `guideline_recommendation` tags). Quantitative and qualitative effects reported from trials, cohorts, reviews, and registries are tagged `secondary_reported_result`; this chapter is not represented as if it enrolled those populations.

## SEA

- Source type: clinical practice guideline / Standards chapter
- Substantive coverage: S89–S116
- Figures reconciled: 2/2 (Figures 5.1–5.2)
- Tables reconciled: 7/7 (Tables 5.1–5.7)
- Algorithms/workflows reconciled: 0 formal algorithms; Table 5.3 risk scoring and Table 5.4 medication-adjustment tool reconciled as structured tables
- Numbered recommendation blocks reconciled: 57/57
- External ADA methodology document: not supplied; limitation preserved
- Verdict: `Read first`
- SEA QA: PASS

## Reference queue

- Bibliography entries extracted: 633
- P0 high-leverage systematic-review/trial/consensus/guideline sources: 287
- P1 current high-value supporting evidence: 227
- P2 contextual/historical/supporting evidence: 119

## Extraction limitations / schema gaps

- The LiteratureAtom schema has no dedicated `guideline_recommendation` atom kind, so recommendations use `author_conclusion` with descriptive tags as permitted by the large-source workflow.
- The current quantitative-result schema is oriented toward primary studies; secondary narrative ranges and summarized effect estimates that do not expose full population/exposure/comparator/outcome context in this chapter were preserved as `other` atoms rather than forcing artificial primary-study structure.
- The ADA evidence-grade definitions and full guideline-development method are delegated to separate Standards methodology material and were not supplied in this input.
- Bibliography entries were not atomized; they were preserved as a reference task queue.
- No external evidence verification was used to change source-derived claims; the workflow is grounded in the supplied chapter and project protocols.

## Protocol/version note

The project designates `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing SEA source. The file's internal heading identifies Integrated Compact v3; the workflow follows the v4-named project source as authoritative and records the mismatch rather than silently reconciling it.

## Drive lifecycle

- ATOM/validation/coverage/crosswalk/SEA-QA JSON files: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`.
- SEA HTML: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`.
- Reference task queue and processing report: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`.
- `dc26s005.pdf` was moved from `10 - Active Literature / 1 - American Diabetes Association 2026` to `90 - Processed / Clinical Medicine & Pharmacy / 47 - American Diabetes Association 2026`.
- `TBR - Current Task Queue` was re-read after the move. Concurrent ADA section workers changed the document during this run; final verification showed both the Active Literature snapshot and Actionable work list reconciled to **8 remaining ADA section PDFs**, matching the live remaining set (`dc26s010.pdf` through `dc26s017.pdf`). Stale-count writes from this run were rejected by revision control rather than overwriting newer state.
