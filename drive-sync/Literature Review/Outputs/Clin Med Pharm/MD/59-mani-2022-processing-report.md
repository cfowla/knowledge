# MANI processing report

Activated macros: `@ATOM`, `@SEA`

## Source

- Folder: `59 - MANI - Mild Moderate Asthma Network in Italy`
- Raw source: `Mild Moderate Asthma Network in Italy MANI a long-term observational study.pdf`
- DOI: `10.1080/02770903.2021.1968895`
- ClinicalTrials.gov: `NCT04796844`
- PDF pages: 7
- SHA-256: `9ec653f8d65d7821b99b97f2409adbcc9587b057e205da852bab0217682c58e2`
- Source type: prospective observational cohort study design/network description

## ATOM result

- Atoms: **54**
- Counts by kind: `{"author_conclusion": 4, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 5, "funding_disclosure": 1, "limitation": 2, "method": 20, "outcome_definition": 18, "population_description": 1, "study_objective": 1}`
- Semantic batches: `{"mani-2022-data-analysis-v1": 13, "mani-2022-design-v1": 14, "mani-2022-interpretation-v1": 9, "mani-2022-outcomes-v1": 18}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

The source is a design article, not a completed cohort-results report. Planned outcomes, follow-up, statistical methods, and sample-size assumptions remain method or outcome-definition atoms. No observed MANI result was invented.

## SEA result

All seven PDF pages were rendered and inspected. The article contains no main-text figures, tables, algorithms, or supplements. The appraisal therefore focuses on the study design, planned outcomes, data collection, statistical plan, limitations, and disclosure sections. Final verdict: **Skim deeply**. Best use is registry design and provenance, not treatment efficacy or practice change.

## Reference task queue

- References extracted: **26**
- Output: `59-mani-2022-reference-task-queue.md`
- External bibliographic correction: not performed
- Bibliography entries were not atomized

## Governing sources applied

ATOM precedence:
1. `literature(1).py`
2. `literature_atoms(1).py`
3. `literature_atom.schema.json`
4. `README(2).md`
5. `example_atom(1).json`

SEA governing protocol: `summary-evaluation-appraisal-protocol-v4-compact.md`

Supporting workflow: `large-source-ATOM-SEA.md`

Writing control: `unslop.skill.md`

## Output files

### JSON
- `59-mani-2022-atoms.json`
- `59-mani-2022-validation.json`
- `59-mani-2022-coverage.json`

### HTML
- `59-mani-2022-sea.html`

### Markdown
- `59-mani-2022-reference-task-queue.md`
- `59-mani-2022-processing-report.md`

Generated: 2026-08-25T02:44:35Z
