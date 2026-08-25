# Rein and Westervelt 1973 processing report

Activated macros: @ATOM and @SEA.

## Source

- Primary file: `aac00351-0166.pdf`
- Title: Pharmacodynamics of Cefazolin in the Presence of Normal and Impaired Renal Function
- Citation: Antimicrob Agents Chemother. 1973;4(3):366-371.
- Google Drive folder: `3 / 2 / 1 / 147 - Rein Westervelt 1973`
- PDF pages inspected: 6
- PDF SHA-256: `7ad6e23881017a01b4f665ba2a191e2d61d8f25b86729e8b84a1602f6d2f552f`

## ATOM status

- Literature atoms: 45
- Counts by kind: `{"author_conclusion": 4, "eligibility_criterion": 2, "exposure_description": 1, "funding_disclosure": 1, "intervention_description": 1, "limitation": 3, "method": 4, "outcome_definition": 2, "population_description": 2, "qualitative_result": 4, "quantitative_result": 20, "study_objective": 1}`
- Counts by semantic batch: `{"rein-westervelt-1973-design-v1": 13, "rein-westervelt-1973-interpretation-v1": 8, "rein-westervelt-1973-renal-urinary-v1": 5, "rein-westervelt-1973-serum-elimination-v1": 19}`
- Pydantic structural validation: PASS
- JSON Schema validation: PASS
- Sufficiency validation: PASS
- Structural errors: 0
- Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- All atom IDs are unique and all atoms share one publication ID.

The full Table 1 and Table 3 concentration matrices are preserved in the SEA HTML. They were not expanded into one atom per numeric cell because the atom set targets independently reviewable study assertions rather than a duplicate tabular dump.

## SEA status

All six PDF pages were rendered and visually inspected. Three figures and three tables were reconciled. Final scoring followed extraction and visual review.

Verdict: **Skim deeply.** The source is useful historical renal pharmacokinetic evidence, especially for the creatinine-clearance relation and probenecid experiment. It should not be used alone as current cefazolin dosing guidance.

SEA QA: **PASS**.

## Source-integrity findings

1. The abstract states 12 subjects, but the methods describe five healthy volunteers plus nine renal-failure patients. Table 1 has 14 non-probenecid rows and lists C.L. twice at different creatinine clearances.
2. The discussion cites reference 18 for biliary concentrations, but the printed bibliography contains references 1 through 17 only.
3. No source-level explanation reconciles either issue. They were not silently repaired.

## Reference task queue

- Printed bibliography entries: 17
- External bibliographic correction: not performed because @VERIFY was not activated
- Bibliography atomized: no

## Governing sources applied

ATOM precedence:
1. `literature(1).py`
2. `literature_atoms(1).py`
3. `literature_atom.schema.json`
4. `README(2).md`
5. `example_atom(1).json`, illustrative only

SEA governing file: `summary-evaluation-appraisal-protocol-v4-compact.md`.

Supporting workflow: `large-source-ATOM-SEA.md`.

Writing control: `unslop.skill.md`.

The governing SEA filename is labeled v4 while its internal heading says Integrated Compact v3. The v4-named file governed this run because the project macro declares it authoritative.

## Output files

### JSON

- `rein-westervelt-1973-atoms.json`
- `rein-westervelt-1973-validation.json`
- `rein-westervelt-1973-coverage.json`
- `rein-westervelt-1973-crosswalk.json`
- `rein-westervelt-1973-sea-qa.json`

### HTML

- `rein-westervelt-1973-sea.html`

### Markdown

- `rein-westervelt-1973-reference-task-queue.md`
- `rein-westervelt-1973-processing-report.md`

## Intended Google Drive destinations

- JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`
- HTML: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`
- Markdown: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`
