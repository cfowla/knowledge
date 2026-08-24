# Processing report: 4. Comprehensive Medical Evaluation and Assessment of Comorbidities: Standards of Care in Diabetes—2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s004.pdf`  
DOI: `10.2337/dc26-S004`  
SHA-256: `2edd69478203db7a24b323562d874c4d9030965997ebf4c0d55b59b2947c949b`

## ATOM

- LiteratureAtoms: 87
- Shared publication ID: `8ce8cf86-1fea-53cf-b4b3-2127d088e7fc`
- Atom counts by kind: `{"author_conclusion": 56, "limitation": 1, "other": 16, "quantitative_result": 14}`
- Semantic extraction runs: `{"ada-ppc-2026-dc26-s004-autoimmune-disease-v1": 2, "ada-ppc-2026-dc26-s004-bone-health-evidence-v1": 5, "ada-ppc-2026-dc26-s004-bone-health-v1": 9, "ada-ppc-2026-dc26-s004-cognitive-impairment-evidence-v1": 1, "ada-ppc-2026-dc26-s004-cognitive-impairment-v1": 1, "ada-ppc-2026-dc26-s004-comprehensive-evaluation-v1": 9, "ada-ppc-2026-dc26-s004-dental-care-evidence-v1": 1, "ada-ppc-2026-dc26-s004-dental-care-v1": 2, "ada-ppc-2026-dc26-s004-disability-evidence-v1": 1, "ada-ppc-2026-dc26-s004-disability-v1": 2, "ada-ppc-2026-dc26-s004-frontmatter-v1": 1, "ada-ppc-2026-dc26-s004-hepatitis-c-evidence-v1": 1, "ada-ppc-2026-dc26-s004-immunizations-v1": 1, "ada-ppc-2026-dc26-s004-masld-management-evidence-v1": 9, "ada-ppc-2026-dc26-s004-masld-management-v1": 19, "ada-ppc-2026-dc26-s004-masld-screening-evidence-v1": 4, "ada-ppc-2026-dc26-s004-masld-screening-v1": 4, "ada-ppc-2026-dc26-s004-pancreatitis-evidence-v1": 3, "ada-ppc-2026-dc26-s004-person-centered-care-v1": 2, "ada-ppc-2026-dc26-s004-sensory-impairment-evidence-v1": 2, "ada-ppc-2026-dc26-s004-sexual-health-men-evidence-v1": 1, "ada-ppc-2026-dc26-s004-sexual-health-men-v1": 3, "ada-ppc-2026-dc26-s004-sexual-health-women-evidence-v1": 2, "ada-ppc-2026-dc26-s004-sexual-health-women-v1": 2}`
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate canonical statements: 0
- Duplicate statement-anchor pairs: 0

Guideline boundary: recommendations are represented as panel/guideline statements (`author_conclusion` plus `guideline_recommendation` tags). Quantitative effects reported from trials, systematic reviews, surveillance sources, and programs are tagged `secondary_reported_result`; the chapter is not represented as if it enrolled those populations.

## SEA

- Source type: clinical practice guideline / Standards chapter
- Substantive coverage: S61–S81
- Figures reconciled: 3/3 (Figures 4.1–4.3)
- Tables reconciled: 4/4 (Tables 4.1–4.4)
- Algorithms/workflows reconciled: 3/3
- External methodology document: not supplied; limitation preserved
- Verdict: `Read first`
- SEA QA: PASS

## Reference queue

- Bibliography entries extracted: 307
- P0 direct-verification priorities: 95
- P1 current high-value supporting evidence: 133
- P2 contextual/background evidence: 79

## Extraction limitations / schema gaps

- The LiteratureAtom schema has no dedicated `guideline_recommendation` atom kind, so recommendations use `author_conclusion` with descriptive tags as permitted by the large-source workflow.
- The ADA evidence-grade definitions and full guideline-development method are delegated to the separate Introduction and Methodology and were not supplied in this input.
- Bibliography entries were not atomized; they were preserved as a reference task queue.
- Cited primary studies were not independently read; secondary quantitative reports are explicitly tagged and anchored to this guideline chapter.
- No external verification was performed.

## Protocol/version note

The project designates `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing SEA source. The supplied v4-named file's internal heading says “Integrated Compact v3.” The workflow followed the v4-named file as authoritative and recorded this version-label mismatch rather than silently changing it.

## Drive lifecycle

- ATOM/validation/coverage/crosswalk/SEA-QA JSON files saved to `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`.
- SEA HTML saved to `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`.
- Reference task queue and processing report saved to `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`.
- `dc26s004.pdf` moved from `10 - Active Literature / 1 - American Diabetes Association 2026` to `90 - Processed / Clinical Medicine & Pharmacy / 47 - American Diabetes Association 2026`.
- Live active ADA folder reconciled after the move: 10 section PDFs remain unprocessed.
- `TBR - Current Task Queue` updated from 12 to 10 remaining ADA section PDFs in both the active-state line and actionable-work line.
