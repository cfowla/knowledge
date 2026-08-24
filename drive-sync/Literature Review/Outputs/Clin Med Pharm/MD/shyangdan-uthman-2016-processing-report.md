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
- Canonical primary PDF: `e009417.full.pdf`, 20 pages, SHA-256 `10d17e740a7ee6b8b893e51e5ad6dfd4c90ba73a0dd1d930d4be3f3c88d4b4b7`
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
- Shared publication identities: 1
- Duplicate statement-anchor pairs: 0

The 70-atom set was revalidated on August 23, 2026 against the supplied current `literature.py`, `literature_atoms.py`, and `literature_atom.schema.json`. The supplied `README(2).md` and `example_atom(1).json` were also inspected under the declared ATOM precedence. No repair was required. All atoms remain `needs_review` because the extraction was model-assisted and has not received independent human verification.

## SEA result

The source was appraised as a systematic review with Bayesian network meta-analysis of randomized trials. Coverage reconciles all 16 main-text figures, all 3 main-text tables, the study-selection workflow, the Bayesian NMA workflow, and the one-page Ovid MEDLINE search-strategy supplement. SEA QA remains **PASS** under the v4 protocol. The article's count inconsistency, 13 stated included trials versus 14 when its drug-specific counts are summed, remains a source-consistency flag.

Verdict: **Read soon** for historical comparative SGLT-2 glycaemic, weight, and systolic blood-pressure efficacy. Do not use this source alone for current inpatient formulary equivalence, safety, cardiorenal outcomes, or contemporary treatment recommendations.

## Reference task queue

The primary article contains 30 bibliography entries. The original source-order bibliography remains in `shyangdan-uthman-2016-references.md`. A separate checkbox queue, `shyangdan-uthman-2016-reference-task-queue.md`, preserves all 30 entries in source order and groups them for downstream work:

- P0: 14 primary randomized trial references used by the review evidence base or sensitivity analyses
- P1: 7 guidance, prior synthesis, or safety-context references
- P2: 7 systematic-review or network-meta-analysis methods references
- P3: 2 mechanistic background randomized studies

Bibliography entries were not converted into LiteratureAtoms.

## August 23 reconciliation

The live queue item at `3/2/1/23` was a stale duplicate intake for this already completed publication. Its `PMID_26911584_payload.pdf` has SHA-256 `1007c257ab9168edd775d41ea290b70499af1b78936793dad8db3d821158b13b`, so it is not byte-identical to the canonical primary PDF. Text comparison and DOI/title identity confirm the same article; the active copy carries Warwick repository wrapper and download metadata. It was preserved for provenance rather than replacing the canonical PDF.

The stale active folder and its acquisition log were moved beneath `90 - Processed / Clinical Medicine & Pharmacy / 36 - Shyangdan Uthman 2016` as `Reconciled active intake - 2026-08-23`. No second publication record or second ATOM/SEA output set was created. The parent SGLT2 task was already complete, so its checked/open totals did not change.

## Source and validation limitations

- `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom(1).json` were available and inspected under the declared ATOM precedence.
- `summary-evaluation-appraisal-protocol-v4-compact.md` was used as the governing SEA protocol; the v3 HTML remains historical reference only.
- The source states that 13 trials met inclusion criteria, while its drug-specific counts sum to 14. The discrepancy is preserved rather than silently repaired.
- The review did not compare safety outcomes, so no comparative safety atoms were created.
- Several outcomes were sensitive to inclusion of atypical trials, especially the dual-therapy SBP network.
- External current-practice verification was not performed because `@VERIFY` was not activated.

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
- `shyangdan-uthman-2016-reference-task-queue.md`
- `shyangdan-uthman-2016-processing-report.md`
