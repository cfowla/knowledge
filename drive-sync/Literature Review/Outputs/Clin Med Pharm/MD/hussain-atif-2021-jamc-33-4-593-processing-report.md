# Processing report: Comparison of efficacy and safety profile of empagliflozin versus dapagliflozin as add on therapy in type 2 diabetic patients

## Activated macros

@ATOM + @SEA

## Source packet

- Main article: `jmanager,+10-Mazhar+Hussain.pdf`
- Journal: J Ayub Med Coll Abbottabad 2021;33(4):593-597
- PMID: `35124914`
- DOI: not listed in the supplied article
- Source pages reviewed: 5 of 5
- Source SHA256: `ab78e51b14f60002b117c1d3e3059470948a671a80773bc694d732a0d0606304`
- Publication ID: `b00f7ddb-0922-5df5-ace1-240931153ee8`
- Supplement: none present in the source packet

## ATOM status

- Atoms: **67**
- By kind: `{"adverse_event": 8, "author_conclusion": 4, "comparator_description": 2, "conflict_of_interest": 1, "eligibility_criterion": 2, "funding_disclosure": 1, "intervention_description": 2, "limitation": 3, "method": 14, "outcome_definition": 2, "population_description": 8, "qualitative_result": 2, "quantitative_result": 17, "study_objective": 1}`
- Pydantic structural validation using `literature(1).py`: **PASS**
- JSON Schema validation using `literature_atom.schema.json`: **PASS**
- Sufficiency validation using `literature_atoms(1).py`: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Unique atom IDs: **PASS**
- Shared publication ID: **PASS**
- Exact duplicate statement and anchor pairs: **0**

All model-extracted atoms remain `needs_review`. No human verification status was invented.

## SEA status

The full article was reviewed. Figure 1 and Tables 1 through 3 were reconciled before appraisal. No supplement was present. Final SEA scoring occurred after extraction and visual reconciliation. Mechanical HTML QA status: **PASS**.

SEA verdict: **Do not use for practice**. The paper is directly relevant to empagliflozin versus dapagliflozin comparison, but its internal reporting conflicts prevent a reliable treatment preference or formulary conclusion.

## Source-integrity findings

The source contains multiple consequential internal conflicts. No discrepancy was silently repaired.

1. Methods reports 410 recruited and 280 enrolled, while Results and Figure 1 report 410 screened or recruited, 356 enrolled, and 280 randomized.
2. Results states 76 exclusions, but the five Figure 1 exclusion categories sum to 81.
3. The abstract gives fixed doses of empagliflozin 25 mg and dapagliflozin 10 mg, while Methods gives dose ranges of 10 to 25 mg and 5 to 10 mg daily.
4. The article defines p<0.05 as significant but calls the between-group body-weight result non-significant at p=0.032.
5. Narrative changes in body weight, fasting blood glucose, and HbA1c do not match changes calculated from Table 2 baseline and week-12 means.
6. Table 2 prints empagliflozin week-12 fasting glucose as `125.4±655 mg/dL`.
7. Table 2 final p-values are interpreted in the Results as between-group comparisons, but the table footnote describes the final column as a within-group baseline-to-week-12 comparison.
8. Table 3 reports 15 genital infections among 127 dapagliflozin patients as 7.08%; 15 divided by 127 is 11.81%.
9. The infection percentages are ordered differently in the Results narrative than in Table 3.
10. Independent appraisal calculations from the displayed baseline means, SDs, and arm sizes do not reproduce several Table 1 p-values. For example, a two-sided Welch test gives approximate p values of 0.00020 for age, 0.00021 for fasting glucose, and 0.000026 for HbA1c, compared with printed p values of 0.82, 0.44, and 0.62.
11. Table 3 states that chi-square tests were used. Pearson chi-square from the printed urinary-infection counts gives p about 0.060, compared with the printed p=0.005.

The recalculations are appraisal checks. They are not replacements for source-reported values and were not serialized as reported LiteratureAtoms.

## Reference task queue

- References extracted: **27**
- Bibliography order and source spelling preserved
- Bibliography atomized: **No**
- Source-printed reference 14 year `2105` preserved rather than silently corrected
- Output: `hussain-atif-2021-jamc-33-4-593-reference-task-queue.md`

## Governing sources applied

ATOM precedence:
1. `literature(1).py`
2. `literature_atoms(1).py`
3. `literature_atom.schema.json`
4. `README(2).md`
5. `example_atom(1).json`

SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing protocol. The v3 HTML was historical reference only. The large-source workflow was consulted and the five-page article was judged suitable for one complete pass rather than semantic batching. `unslop.skill.md` was applied to generated prose.

The governing SEA filename says v4 while its internal heading says `Integrated Compact v3`. The supplied v4-named file governed this run, and the label conflict was not rewritten.

## Output files

### JSON

- `hussain-atif-2021-jamc-33-4-593-atoms.json`
- `hussain-atif-2021-jamc-33-4-593-validation.json`
- `hussain-atif-2021-jamc-33-4-593-coverage.json`
- `hussain-atif-2021-jamc-33-4-593-crosswalk.json`
- `hussain-atif-2021-jamc-33-4-593-sea-qa.json`

### HTML

- `hussain-atif-2021-jamc-33-4-593-sea.html`

### Markdown

- `hussain-atif-2021-jamc-33-4-593-reference-task-queue.md`
- `hussain-atif-2021-jamc-33-4-593-processing-report.md`

## Google Drive destinations

- JSON: `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/JSON/`
- HTML: `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/HTML/`
- Markdown: `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/MD/`

Drive verification is complete. The parent SGLT2 task-list item is checked, the source packet is stored in `90 - Processed / Clinical Medicine & Pharmacy / 14 - Hussain Atif 2021`, and `TBR - Current Task Queue` was reconciled to 19 active numbered source folders, 58 processed clinical source folders, and 89 checked / 34 unchecked SGLT2 records.
