# Processing report

## Source

- Folder: `Bodea Serban 2026`
- File: `jcm-15-00378.pdf`
- Title: Effects of SGLT2 Inhibitors on Clinical Outcomes, Symptoms, Functional Capacity, and Cardiac Remodeling in Heart Failure: A Comprehensive Systematic Review and Multidomain Meta-Analysis of Randomized Trials
- DOI: `10.3390/jcm15010378`
- SHA-256: `9272d2e37bfeecf94ebaa1b08cf37d6c993ba2b33e201261989bbcfe7471edd9`

## ATOM

- Atoms: **63**
- Kinds: `{"adverse_event": 1, "author_conclusion": 2, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 1, "funding_disclosure": 1, "limitation": 13, "method": 6, "outcome_definition": 2, "population_description": 2, "qualitative_result": 9, "quantitative_result": 23, "study_objective": 1}`
- Semantic batches: `{"bodea-serban-2026-clinical-v1": 8, "bodea-serban-2026-general-v1": 15, "bodea-serban-2026-interpretation-v1": 15, "bodea-serban-2026-remodeling-safety-v1": 15, "bodea-serban-2026-symptoms-function-v1": 10}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

The review is a secondary source. Individual-trial findings remain secondary reports and were tagged accordingly. Primary-study atoms require direct extraction of the cited trial publications.

## SEA

All 24 pages were rendered and inspected. Five main-text figures and two main-text tables were reconciled as structured blocks. The source-linked supplementary package was not present in the selected Drive folder, so supplement-only material was not independently inspected.

## Source-integrity findings

1. The paper reports 23,812 total participants, while Table 1 row sample sizes sum to 23,999.
2. Section 3.3 reports 22,927 participants across six cited cardiovascular-outcome trials, while their Table 1 sample sizes sum to 22,477.
3. Methods describe a DerSimonian-Laird random-effects model but also say tau-squared was estimated with Paule-Mandel.
4. Eligibility wording names dapagliflozin, empagliflozin, and canagliflozin, while SOLOIST-WHF with sotagliflozin is included and later discussed in sensitivity analysis.

No discrepancy was silently repaired.

## References

The paper contains **39** numbered references. They were exported to `Bodea-Serban-2026-SGLT2-HF-references.md` with PDF line wrapping normalized and without external bibliographic correction.

## Governing-source boundary

Applied: `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, `large-source-ATOM-SEA.md`, `summary-evaluation-appraisal-protocol-v4-compact.md`, `example_atom.json`, and `unslop.skill.md`. `README(2).md` was not available in supplied project sources or connected Drive searches and is recorded as a source gap.

## Output files

- `Bodea-Serban-2026-SGLT2-HF-atoms.json`
- `Bodea-Serban-2026-SGLT2-HF-validation.json`
- `Bodea-Serban-2026-SGLT2-HF-coverage.json`
- `Bodea-Serban-2026-SGLT2-HF-crosswalk.json`
- `Bodea-Serban-2026-SGLT2-HF-sea.html`
- `Bodea-Serban-2026-SGLT2-HF-sea-qa.json`
- `Bodea-Serban-2026-SGLT2-HF-references.md`
- `Bodea-Serban-2026-SGLT2-HF-processing-report.md`
