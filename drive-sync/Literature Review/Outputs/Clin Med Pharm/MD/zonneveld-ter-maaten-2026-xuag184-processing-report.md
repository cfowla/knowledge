# Processing report: Early effects of SGLT2 inhibitors in acute heart failure: an individual patient-level meta-analysis

## Activated macros

@ATOM + @SEA

## Source packet

- Main article: `xuag184.pdf`, 14 pages, SHA256 `dec0c0be7a1d9772b20f49969dd49ef03d6cd216394140ba0d52ab0e0e795563`
- Supplement: `xuag184_supplementary_data.docx`, rendered to 20 pages for visual reconciliation, SHA256 `05e29c0bc5b50aef223009ceab2b12b4f635c5b872191af5870f4828f9f9e681`
- DOI: `10.1093/ejhf/xuag184`
- PMID: `42334253`
- Publication ID: `e1e97b86-f167-526e-a471-706978fbe0d7`

## ATOM status

- Atoms: **77**
- By kind: `{"adverse_event": 6, "author_conclusion": 2, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 1, "funding_disclosure": 1, "intervention_description": 2, "limitation": 7, "method": 10, "other": 6, "outcome_definition": 3, "population_description": 7, "qualitative_result": 3, "quantitative_result": 23, "study_objective": 1, "subgroup_result": 2}`
- Semantic batches: `{"xuag184-clinical-safety-v1": 21, "xuag184-decongestion-v1": 12, "xuag184-design-v1": 25, "xuag184-interpretation-v1": 19}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Unique atom IDs: **PASS**
- Shared publication ID: **PASS**
- Exact duplicate statement-anchor pairs: **0**

All model-extracted atoms remain `needs_review`. No human verification status was invented.

## SEA status

All 14 main pages and 20 supplementary pages were reviewed. The graphical abstract, Figures 1-5, Tables 1-5, Supplementary Figures S1-S5, and Supplementary Tables S1-S7 were reconciled. The final appraisal was completed after extraction and visual/table reconciliation. Mechanical HTML QA status: **PASS**.

## Source-integrity findings

1. Main Table 3 reports Day-2 weight-change P=.053, while Supplementary Table S7 reports fixed-effect P=.008 for the same raw group medians.
2. Supplementary Table S5 prints NT-proBNP >=3340 ng/L subgroup HR 0.32 with 95% CI 0.38-1.35, placing the point estimate outside the interval.
3. Table 1 prints an EMPAG-HF placebo urine-output IQR as 6450-3550 mL, with reversed bounds.
4. The Methods prose gives the eGFR subgroup unit as mg/ml/1.73 m2, while tables use mL/min/1.73 m2.
5. Supplementary Table S6 reports placebo-only 24-hour raw medians of 2250 mL with SGLT2i and 3050 mL with placebo, P=.005, without a comparative effect estimate. No adjusted direction was inferred.

No discrepancy was silently repaired.

## References

The main article contains **33** numbered references. They were exported in source order as an unchecked Markdown reference task queue. Bibliography entries were not atomized.

## Governing sources applied

ATOM precedence: `literature(1).py` -> `literature_atoms(1).py` -> `literature_atom.schema.json` -> `README(2).md` -> `example_atom(1).json`. Large-source execution used `large-source-ATOM-SEA.md`. SEA used `summary-evaluation-appraisal-protocol-v4-compact.md`; the v3 HTML was historical reference only. `unslop.skill.md` was retrieved and applied to prose.

The SEA governing filename says v4, while the file's internal heading says "Integrated Compact v3." The supplied file governed this run; the label conflict remains documented.

## Output files

- `zonneveld-ter-maaten-2026-xuag184-atoms.json`
- `zonneveld-ter-maaten-2026-xuag184-validation.json`
- `zonneveld-ter-maaten-2026-xuag184-coverage.json`
- `zonneveld-ter-maaten-2026-xuag184-crosswalk.json`
- `zonneveld-ter-maaten-2026-xuag184-sea.html`
- `zonneveld-ter-maaten-2026-xuag184-sea-qa.json`
- `zonneveld-ter-maaten-2026-xuag184-references.md`
- `zonneveld-ter-maaten-2026-xuag184-processing-report.md`

## Intended Google Drive destinations

- JSON: `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/JSON/`
- HTML: `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/HTML/`
- Markdown: `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/MD/`
