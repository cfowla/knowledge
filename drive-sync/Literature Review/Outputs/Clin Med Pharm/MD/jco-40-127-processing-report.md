# jco-40-127 processing report

## Activated macros

- @ATOM
- @SEA

## Source

- Title: Long-Term Outcomes With Nivolumab Plus Ipilimumab or Nivolumab Alone Versus Ipilimumab in Patients With Advanced Melanoma
- Citation: J Clin Oncol. 2022;40(2):127-137.
- DOI: 10.1200/JCO.21.02229
- Clinical trial: NCT01844505
- Raw Drive source: `jco-40-127.pdf`
- Source path: `3 - TBR / 2 - 10 - Active Literature / 1 - Clinical Medicine & Pharmacy / 127 - jco-40-127`
- PDF pages: 13
- SHA-256: `4dadc8ebfd1f1268e873388894545de8f349c4c7540b294cae45b3ac66d127e8`
- Retrieved Drive documents: 1 main PDF
- Linked but unavailable in the retrieved folder: Data Supplement, Protocol

## ATOM status

- Publication ID: `78e1dc50-6683-5527-a36d-c5ea27f45a03`
- Atoms: 82
- By kind: `{"adverse_event": 3, "author_conclusion": 1, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 1, "funding_disclosure": 1, "intervention_description": 2, "limitation": 1, "method": 3, "other": 1, "outcome_definition": 5, "population_description": 1, "qualitative_result": 4, "quantitative_result": 37, "study_objective": 1, "subgroup_result": 18}`
- Semantic batches: `{"jco-40-127-design-v1": 15, "jco-40-127-disclosures-v1": 4, "jco-40-127-efficacy-v1": 27, "jco-40-127-subgroups-v1": 19, "jco-40-127-treatment-free-safety-v1": 17}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Exact duplicate statement plus anchor pairs: **0**

The extraction preserves the randomized comparisons against ipilimumab and keeps combination versus nivolumab findings tagged as descriptive and unpowered. Results that are not reached remain qualitative rather than receiving invented numeric values. Background cross-trial comparisons and bibliography entries were not converted into primary-study atoms.

## SEA status

All 13 PDF pages were rendered and visually inspected. The 10 substantive article pages and all seven main-text figures were reconciled. There are no main-text tables. The Data Supplement and Protocol were not present in the source folder, so the HTML does not claim detailed safety tables or protocol-level checks that require those files.

Verdict: **Read soon.** The report provides strong long-term randomized evidence for nivolumab-containing therapy versus ipilimumab. It does not provide a powered head-to-head answer for nivolumab plus ipilimumab versus nivolumab alone.

SEA QA: **PASS**, subject to the companion validation JSON remaining error-free.

## Reference task queue

- References extracted: 14
- Numbering preserved: 1-14
- External bibliographic correction: not performed
- Bibliography atomized: no

## Governing sources applied

ATOM precedence:
1. `literature(1).py`
2. `literature_atoms(1).py`
3. `literature_atom.schema.json`
4. `README(2).md`
5. `example_atom(1).json`, illustrative only

SEA governing file: `summary-evaluation-appraisal-protocol-v4-compact.md`

Supporting workflow: `large-source-ATOM-SEA.md`

Historical reference only: `summary-evaluation-appraisal-protocol-v3-compact.html`

Writing control: `unslop.skill.md`

## Output files

- `jco-40-127-atoms.json`
- `jco-40-127-validation.json`
- `jco-40-127-coverage.json`
- `jco-40-127-sea.html`
- `jco-40-127-references.md`
- `jco-40-127-processing-report.md`
