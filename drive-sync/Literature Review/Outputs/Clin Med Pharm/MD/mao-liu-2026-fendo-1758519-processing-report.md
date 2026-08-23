# Processing report - Mao et al. 2026

## Source

- Title: Glucose cotransporter-2 inhibitors on mortality and hospitalization in heart failure patients: a comprehensive meta-analysis
- Authors: Xiang Mao, Wenhua Liu, Bingqian Hu, Enguo Xu
- Journal: Frontiers in Endocrinology
- Published: 2026-05-13
- DOI: `10.3389/fendo.2026.1758519`
- PMID: `42211456`
- Publication ID: `284839e7-2c73-51f9-9c5f-a457d3973037`
- Main file: `fendo-17-1758519.pdf`
- Main file SHA-256: `7bf1035856789780ef7bbdc79ae00fa1e7b6de09d719d970da5e3b03d2884643`
- Supplement: `table 1.docx`
- Supplement SHA-256: `3bbbc25c6decfa7ab205419ce1bdad3e7b3c54e72d7fbb9b1616a6dca7e9e9da`
- Source type: systematic review and meta-analysis
- Printed pages: 14

## ATOM

- LiteratureAtoms: **110**
- By kind: `{"author_conclusion": 2, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 7, "funding_disclosure": 1, "limitation": 4, "method": 10, "other": 20, "outcome_definition": 3, "population_description": 19, "qualitative_result": 3, "quantitative_result": 27, "study_objective": 1, "subgroup_result": 11}`
- Assertion origins: `{"calculated_from_reported_data": 2, "directly_reported": 25, "normalized_from_source": 83}`
- Semantic batches: **5**
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Duplicate canonical statements: **0**
- Review status: all atoms remain `needs_review`

Two arithmetic source checks are represented as `calculated_from_reported_data`. Other cross-file contradictions remain in the validation and SEA artifacts so appraisal is not converted into reported evidence.

## SEA

- Main figures reconciled: **9/9**
- Main tables reconciled: **2/2**
- Supplied supplementary tables reconciled: **1/1**
- HTML QA: **PASS**
- Verdict: **Do not use for practice**
- Appraisal confidence: **high**, based on contradictions visible inside the supplied source packet.

## Source-integrity findings

1. CRITICAL: The article says the 15 included RCTs contain 28,484 participants, but the 15 sample sizes printed in Table 1 sum to 21,808, a difference of 6,676.
2. CRITICAL: Figures 2 and 3 use each Table 1 study sample size as the denominator in both the treatment and control columns. Across the 15 rows, the printed per-arm denominators sum to 43,616, exactly twice the 21,808 Table 1 total.
3. CRITICAL: The abstract and Results report pooled all-cause mortality HR 0.86 with 95% CI 0.79 to 0.92. Figure 2 prints HR 0.86 with 95% CI 0.83 to 0.89.
4. CRITICAL: Supplementary Table S1 says only seven listed studies contributed all-cause mortality and eight contributed HF hospitalization, while Figures 2 and 3 include all 15 studies for both outcomes.
5. MAJOR: Supplementary Table S1 uses Ganguly 2024 for the DELIVER-like row and Dougherty 2023 for the post-MI row. Main Table 1 uses Verma 2020 and Kotit 2023 in those positions.
6. CRITICAL: The included-study list cites Mordi 2017 as a trial protocol and Ferreira 2025 as a design paper, yet Table 1 and the primary forest plots assign them completed-trial characteristics and mortality or hospitalization event data.
7. MAJOR: The NT-proBNP Results text says 11 RCTs contributed data, Figure 4 plots 10 study rows, and Supplementary Table S1 maps nine rows to NT-proBNP.
8. MAJOR: The LVEF Results text and Figure 5 use 10 studies, while Supplementary Table S1 maps only five rows to LVEF, LV systolic function, reverse remodeling, or an LV-function surrogate.
9. MAJOR: The Results text describes follow-up as 6 to 36 months. Table 1 contains a 3-month minimum and a 28-month maximum.
10. MAJOR: The risk-of-bias prose reports 10 low-risk trials and five trials described as moderate-risk categories. Table 2 prints 13 overall Low ratings and two Some concerns ratings.
11. MODERATE: The study-selection prose says 30 articles were included from 45 potentially relevant records and then says 30 were excluded. Figure 1 instead shows 30 full-text exclusions and 15 included studies.
12. MODERATE: The Results discuss SOGALDI-PEF and DAPA-ICG, but neither name appears in Table 1 or Supplementary Table S1.
13. MODERATE: The trim-and-fill paragraph says the method altered a pooled HR of 0.86 without major changes and then gives 0.79 to 0.92, which is formatted like the original confidence interval rather than a clearly reported adjusted estimate.

No discrepancy was silently repaired. These findings compare the supplied PDF with the supplied Supplementary Table S1.

## Reference task queue

- References extracted: **31**
- High-priority included-study or direct-evidence candidates: **15**
- Output: `mao-liu-2026-fendo-1758519-reference-task-queue.md`
- External bibliographic correction: **not performed** because `@VERIFY` was not activated.
- Bibliography entries were not atomized.

## Governing sources applied

ATOM precedence:
1. `literature(1).py`
2. `literature_atoms(1).py`
3. `literature_atom.schema.json`
4. `README(2).md`
5. `example_atom(1).json`

SEA governing protocol: `summary-evaluation-appraisal-protocol-v4-compact.md`

Large-source workflow: `large-source-ATOM-SEA.md`

Writing control: `unslop.skill.md`

The named ATOM Pydantic model, sufficiency validator, and JSON Schema were executed directly. SEA scoring followed the supplied v4 protocol. The v3 HTML was treated as historical reference only.

## Output files

### JSON

- `mao-liu-2026-fendo-1758519-atoms.json`
- `mao-liu-2026-fendo-1758519-validation.json`
- `mao-liu-2026-fendo-1758519-coverage.json`
- `mao-liu-2026-fendo-1758519-crosswalk.json`
- `mao-liu-2026-fendo-1758519-sea-qa.json`

### HTML

- `mao-liu-2026-fendo-1758519-sea.html`

### Markdown

- `mao-liu-2026-fendo-1758519-reference-task-queue.md`
- `mao-liu-2026-fendo-1758519-processing-report.md`
