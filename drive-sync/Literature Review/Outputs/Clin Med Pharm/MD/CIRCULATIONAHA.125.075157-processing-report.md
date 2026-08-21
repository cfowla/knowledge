# ATOM + SEA processing report: CIRCULATIONAHA.125.075157

## Activated macros

- `@ATOM`
- `@SEA`

## Source

- Title: *Risk of Heart Failure Hospitalization for GLP-1 Receptor Agonists Versus DPP-4 Inhibitors or SGLT-2 Inhibitors in Patients With Type 2 Diabetes: A Target Trial Emulation*
- Journal: Circulation. 2026;153:1086-1100
- DOI: `10.1161/CIRCULATIONAHA.125.075157`
- Shared publication ID: `de5bf759-f05e-5be9-abb3-7ad6a924f9a1`
- Primary article: `xu-et-al-2026-risk-of-heart-failure-hospitalization-for-glp-1-receptor-agonists-versus-dpp-4-inhibitors-or-sglt-2.pdf` (15 pages; SHA-256 `4dd7c6e0f95e670c312115cb3296a0ea22a71f09879d9bb367ce714149d3bdbb`)
- Published supplement: `circ-2025-075157-s01.pdf` (61 pages; SHA-256 `61c508de9396e95990294a5382eb9361be5971bd7d86bfe2a007835a75c86a83`)
- Updated supplement source: `updated_supplementary_material.docx` (SHA-256 `3f2f2b8a349b53e49bcda8ec002ac52057bf3e100efdc7fa1c2ddcfed95a3674`)
- STROBE checklist: `circ-2025-075157-s02.pdf` (6 pages; SHA-256 `15f47845e37347d8cd3b14e4f1bdbeed1469381d08d0b622602fde14792cac84`)
- Podcast transcript: `cotr153_15_transcript.pdf` (9 pages; SHA-256 `7f90db47349e8468831c92947fc2916b66db5d44c206b0ea852f5a36d86da095`)

## ATOM status

- Atoms: **83**
- By kind: `{"author_conclusion": 4, "comparator_description": 2, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 3, "funding_disclosure": 2, "intervention_description": 1, "limitation": 7, "method": 16, "other": 1, "outcome_definition": 2, "population_description": 9, "qualitative_result": 3, "quantitative_result": 28, "study_objective": 1, "subgroup_result": 2}`
- Semantic batches: `{"circ075157-agents-subgroups-v1": 9, "circ075157-design-methods-v1": 23, "circ075157-interpretation-disclosures-v1": 16, "circ075157-main-outcomes-v1": 10, "circ075157-population-balance-v1": 11, "circ075157-sensitivity-v1": 14}`
- Assertion origins: `{"normalized_from_source": 83}`
- Local reconstructed Pydantic validation: **PASS**
- Local generated JSON Schema validation: **PASS**
- Local reconstructed sufficiency validation: **PASS**
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

## SEA status

All 15 main-article pages and 61 published-supplement pages were rendered and visually scanned. Main Tables 1-4 and Figures 1-2 were reconciled. Supplementary Method Tables 1-4, Method Figures 1-2, Tables S1-S13, and Figures S1-S17 were reconciled. The STROBE checklist was used for reporting-completeness context. The podcast transcript was treated as secondary commentary only.

The strongest study result is the lower HHF rate for GLP-1RA vs DPP-4i: weighted HR 0.77 (95% CI 0.66-0.91) and 3-year RD -0.88 percentage points (95% CI -1.45 to -0.25). GLP-1RA vs SGLT-2i showed similar observed HHF rates: weighted HR 1.02 (95% CI 0.85-1.18), without a formal equivalence or noninferiority design.

## References

The Markdown reference artifact contains all **61** numbered bibliography entries from the primary article. Bibliography entries were not atomized.

## Version note

The published supplement PDF and the updated supplement DOCX differ in some expanded-methods citation numbers. The updated DOCX aligns several references with the main article bibliography, for example Schomaker et al. as reference 29 rather than 53. The published PDF governed visual/table reconciliation; the updated DOCX was used as a citation-number version-control check. No key numerical result-table conflict was identified in reviewed values.

## Governing-source runtime limitation

The required project files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, `example_atom.json`, and the exact `summary-evaluation-appraisal-protocol-v4-compact.md` were searched for in connected project sources but were not directly retrievable in this session. `large-source-ATOM-SEA.md` and `unslop.skill.md` were retrieved and applied. Structural/schema/sufficiency validation therefore used a strict local contract reconstructed from recent validated project LiteratureAtom outputs and the visible large-source guardrails. This report does not claim execution of unavailable authoritative project code. No protocol-specific numeric SEA score was invented.

## Output files

- `CIRCULATIONAHA.125.075157-atoms.json`
- `CIRCULATIONAHA.125.075157-validation.json`
- `CIRCULATIONAHA.125.075157-coverage.json`
- `CIRCULATIONAHA.125.075157-sea.html`
- `CIRCULATIONAHA.125.075157-references.md`
- `CIRCULATIONAHA.125.075157-processing-report.md`
