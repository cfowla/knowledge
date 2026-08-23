# Shyangdan Uthman 2016 processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source

- Title: SGLT-2 receptor inhibitors for treating patients with type 2 diabetes mellitus: a systematic review and network meta-analysis
- Authors: Deepson S Shyangdan, Olalekan A Uthman, Norman Waugh
- Journal: BMJ Open. 2016;6:e009417.
- DOI: 10.1136/bmjopen-2015-009417
- PMID: 26911584
- Primary PDF: `e009417.full.pdf`, 20 pages, SHA-256 `10d17e740a7ee6b8b893e51e5ad6dfd4c90ba73a0dd1d930d4be3f3c88d4b4b7`
- Supplement: `bmjopen-2016-February-6-2--inline-supplementary-material-1.pdf`, 1 page, SHA-256 `ba1e5bdb3b77511ad3f27e3d08dafbf80c3d5ae5d1e47c1705e4cc84921673e8`
- Shared publication ID: `8669dded-573b-5382-a3e6-2ae822098f10`

## ATOM result

- Total LiteratureAtoms: 70
- Counts by kind: `{"author_conclusion": 2, "conflict_of_interest": 2, "data_availability": 1, "eligibility_criterion": 2, "funding_disclosure": 2, "limitation": 9, "method": 10, "outcome_definition": 4, "population_description": 2, "qualitative_result": 10, "quantitative_result": 25, "study_objective": 1}`
- Assertion origins: `{"directly_reported": 42, "extractor_inference": 1, "normalized_from_source": 27}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0

All atoms use `needs_review` because extraction was model-assisted and has not received independent human verification.

## SEA result

The source was appraised as a systematic review with Bayesian network meta-analysis of randomized trials. Coverage reconciled all 16 main-text figures, all 3 main-text tables, the study-selection workflow, the Bayesian NMA workflow, and the one-page Ovid MEDLINE search-strategy supplement. The article's own count inconsistency (13 stated included trials versus 14 when drug-specific counts are summed) is preserved as a source-consistency flag.

Verdict: **Read soon** for historical comparative SGLT-2 glycaemic, weight, and systolic blood-pressure efficacy. Do not use this source alone for current inpatient formulary equivalence, safety, cardiorenal outcomes, or contemporary treatment recommendations.

## References

The primary article contains **30** bibliography entries. They were exported to `shyangdan-uthman-2016-references.md`. Bibliography entries were not converted into LiteratureAtoms.

## Source and validation limitations

- `literature.py`, `literature_atoms.py`, and `literature_atom.schema.json` were available and executed.
- `summary-evaluation-appraisal-protocol-v4-compact.md` was available and used as the governing SEA protocol; the v3 HTML was historical reference only.
- `README(2).md` and `example_atom.json` were not present in the supplied project files and were not found by exact Drive search; their workflow/example guidance could not be inspected.
- The source states that 13 trials met inclusion criteria, while its drug-specific counts sum to 14. The discrepancy was retained rather than silently repaired.
- The review did not compare safety outcomes, and no comparative safety atoms were fabricated.
- Several outcomes were sensitive to inclusion of atypical trials, especially the dual-therapy SBP network.
- No external current-practice verification was performed because this task was source processing rather than a current-practice update.

## Output files

JSON folder:
- `shyangdan-uthman-2016-atoms.json`
- `shyangdan-uthman-2016-validation.json`
- `shyangdan-uthman-2016-coverage.json`
- `shyangdan-uthman-2016-sea-qa.json`

HTML folder:
- `shyangdan-uthman-2016-sea.html`

Markdown folder:
- `shyangdan-uthman-2016-references.md`
- `shyangdan-uthman-2016-processing-report.md`
