# Roden Weng 2013 processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source

- Title: Empagliflozin monotherapy with sitagliptin as an active comparator in patients with type 2 diabetes: a randomised, double-blind, placebo-controlled, phase 3 trial
- Journal: Lancet Diabetes Endocrinol. 2013;1:208-219.
- DOI: 10.1016/S2213-8587(13)70084-6
- PMID: 24622369
- Trial registration: NCT01177813
- Primary PDF: `1-s2.0-S2213858713700846.pdf`, 12 pages, SHA-256 `fa79db96324313f00dc8b3df551ccd17fddf5d6a53aeac2c1b532c9b2e179b15`
- Supplement: `mmc1.pdf`, 7 pages, SHA-256 `c91780b0ea11959b53517501659ade31785681ecf20a8c14bdae7af27ddfb68d`
- Shared publication ID: `77feaf03-1061-5be5-bef6-1f07fa312e8d`

## ATOM result

- Total LiteratureAtoms: 80
- Counts by kind: `{"adverse_event": 10, "author_conclusion": 2, "comparator_description": 1, "conflict_of_interest": 3, "eligibility_criterion": 3, "funding_disclosure": 2, "intervention_description": 2, "limitation": 5, "method": 9, "outcome_definition": 4, "population_description": 2, "qualitative_result": 3, "quantitative_result": 30, "study_objective": 1, "subgroup_result": 3}`
- Assertion origins: `{"directly_reported": 24, "extractor_inference": 1, "normalized_from_source": 55}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0

All atoms use `needs_review` because the extraction was model-assisted and has not received independent human verification.

## SEA result

The source was appraised as a multicentre randomized phase 3 clinical trial. Coverage reconciled all four main-text figures, all five main-text tables, the participant-flow workflow, the hierarchical testing workflow, and the five substantive supplement table groups. The HTML keeps confirmatory placebo comparisons separate from exploratory comparisons with sitagliptin.

Verdict: **Read soon** for historical empagliflozin monotherapy efficacy and safety. Do not use this 2013 trial alone for current inpatient formulary equivalence or current clinical recommendations.

## References

The primary article contains **19** bibliography entries. They were exported to `roden-weng-2013-references.md`. Bibliography entries were not converted into LiteratureAtoms.

## Source and validation limitations

- `literature.py`, `literature_atoms.py`, and `literature_atom.schema.json` were available and executed.
- `summary-evaluation-appraisal-protocol-v4-compact.md` was available and used as the governing SEA protocol. The v3 HTML was historical reference only.
- `README(2).md` and `example_atom.json` were not present in the supplied project files and were not found by exact Drive search. Their workflow/example guidance therefore could not be inspected.
- The source reports placebo `n=229` in the treated-set safety table despite `n=228` randomized to placebo. That source denominator was preserved rather than silently changed.
- One supplement row was unreliable in the extracted text layer and was excluded from atoms rather than repaired by inference.
- No external current-practice verification was performed.

## Output files

JSON folder:
- `roden-weng-2013-atoms.json`
- `roden-weng-2013-validation.json`
- `roden-weng-2013-coverage.json`
- `roden-weng-2013-sea-qa.json`

HTML folder:
- `roden-weng-2013-sea.html`

Markdown folder:
- `roden-weng-2013-references.md`
- `roden-weng-2013-processing-report.md`
