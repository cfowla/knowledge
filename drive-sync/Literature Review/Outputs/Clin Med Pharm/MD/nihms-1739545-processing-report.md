# nihms-1739545 processing report

## Activated macros

- @ATOM
- @SEA

## Source

- Title: Teriparatide-associated calciphylaxis: a case series
- Citation: Osteoporos Int. 2022;33(2):499-504
- DOI: 10.1007/s00198-021-06139-3
- Raw Drive source: `nihms-1739545.pdf`
- PDF pages: 8
- SHA-256: `a714c06236c0bf925b5bac879d78fed0163fd1114c1f28d71dcead824b735ea4`
- Source path verified as `3 - TBR / 2 - 10 - Active Literature / 1 - Clinical Medicine & Pharmacy / 27 - nihms-1739545`

## ATOM status

- Publication ID: `50b59556-66d1-5331-b0e1-1f4d2e07dd46`
- Atoms: 44
- By kind: `{"adverse_event": 15, "author_conclusion": 6, "conflict_of_interest": 1, "eligibility_criterion": 1, "exposure_description": 3, "limitation": 4, "method": 2, "population_description": 6, "qualitative_result": 2, "quantitative_result": 3, "study_objective": 1}`
- Semantic batches: `{"nihms-1739545-aggregate-results-v1": 17, "nihms-1739545-case-table-v1": 12, "nihms-1739545-design-v1": 5, "nihms-1739545-interpretation-v1": 10}`
- Pydantic structural validation: PASS
- JSON Schema validation: PASS
- Sufficiency validation: PASS
- Structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Exact duplicate canonical statements: 0

All 12 Table 1 cases were captured as case-level adverse-event atoms. Background statements sourced to earlier literature were not converted into primary-study findings.

## SEA status

The supplied 8-page PDF was rendered and inspected. The article has one main-text table and no figures. Table 1 spans PDF pages 6-7 and all 12 rows were reconstructed in the SEA HTML. No supplement was present. Final scoring followed source extraction and table reconciliation.

Verdict: **Skim deeply.** The paper is useful for recognition of a possible rare teriparatide-associated calciphylaxis signal, but the spontaneous-report case series cannot estimate incidence or establish causality.

SEA QA: **PASS**.

## Reference task queue

- References extracted: 13
- Directly included published teriparatide cases: references 8-11
- External bibliographic correction: not performed because @VERIFY was not activated
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

Writing control: `unslop.skill.md`

Version note: the governing SEA filename is labeled v4, while its internal heading says Integrated Compact v3. The project macro names the v4 filename as authoritative, so that file governed this run and the mismatch is recorded here.

## Output files

### JSON

- `nihms-1739545-atoms.json`
- `nihms-1739545-validation.json`
- `nihms-1739545-coverage.json`
- `nihms-1739545-crosswalk.json`
- `nihms-1739545-sea-qa.json`

### HTML

- `nihms-1739545-sea.html`

### Markdown

- `nihms-1739545-reference-task-queue.md`
- `nihms-1739545-processing-report.md`

## Intended Google Drive destinations

- JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`
- HTML: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`
- Markdown: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`
