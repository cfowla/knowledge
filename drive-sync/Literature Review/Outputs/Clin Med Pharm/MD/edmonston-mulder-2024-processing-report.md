# Edmonston Mulder 2024 processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source

- Title: Kidney and Cardiovascular Effectiveness of Empagliflozin Compared With Dipeptidyl Peptidase-4 Inhibitors in Patients With Type 2 Diabetes
- Authors: Daniel Edmonston, Hillary Mulder, Elizabeth Lydon, Karen Chiswell, Zachary Lampron, Christina Shay, Keith Marsolo, William Schuyler Jones, Javed Butler, Raj C. Shah, Alanna M. Chamberlain, Daniel E. Ford, Howard S. Gordon, Wenke Hwang, Alexander Chang, Ajaykumar Rao, Hayden B. Bosworth, Neha Pagidipati
- Journal: American Journal of Cardiology. 2024;221:52–63.
- DOI: 10.1016/j.amjcard.2024.04.011
- PMID: 38641191
- Main source: `1-s2.0-S0002914924002686-main.pdf`, 12 PDF pages, SHA-256 `218e4388c44f94e83232e753dfe3d981345df42728f20a1b31d69010b5d3e222`
- Supplement: `1-s2.0-S0002914924002686-mmc1.pdf`, 60 PDF pages, SHA-256 `4a6871f366ec8de886d0b0003d97a4d77e7124560d1927d9a23b88c357d72aa1`
- Shared publication ID: `320523f7-d3fe-5366-ba03-537bcd25cb2c`
- Source type: retrospective EHR-based active-comparator new-user comparative-effectiveness cohort study

## ATOM result

- Total LiteratureAtoms: 103
- Counts by kind: `{"adverse_event": 10, "author_conclusion": 3, "comparator_description": 2, "conflict_of_interest": 2, "eligibility_criterion": 3, "funding_disclosure": 1, "intervention_description": 1, "limitation": 7, "method": 13, "outcome_definition": 7, "population_description": 5, "qualitative_result": 1, "quantitative_result": 29, "study_objective": 1, "subgroup_result": 18}`
- Assertion origins: `{"directly_reported": 64, "normalized_from_source": 39}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0

All atoms use `needs_review` because extraction was model-assisted and has not received independent human verification.

## SEA result

The source was appraised as a large, multisystem real-world comparative-effectiveness study of empagliflozin versus DPP-4 inhibitors. Coverage reconciled **3 main-text figures**, **3 main-text tables**, and **all 7 supplied supplementary tables**. Supplementary Table 1 spans 46 pages of coding definitions and was treated as reproducibility infrastructure rather than reproduced cell-by-cell.

The detailed main-table estimate for the primary kidney composite was HR 0.75 (95% CI 0.65–0.86), with weighted incidence rates 26.65 versus 36.65 per 1,000 person-years. The association was consistent in propensity-matched (HR 0.75, 95% CI 0.67–0.84) and COVID-era sensitivity analyses (HR 0.70, 95% CI 0.57–0.87), and was present in both CKD and non-CKD strata. Heart-failure hospitalization alone was not significantly different (HR 0.96, 95% CI 0.84–1.11). Genital mycotic infection was more frequent with empagliflozin (HR 1.72, 95% CI 1.58–1.88).

Verdict: **Read soon**. The study is useful active-comparator real-world evidence for empagliflozin cardiorenal effectiveness, but it should not be used alone to infer dapagliflozin–empagliflozin equivalence or formulary interchangeability.

## References

The main article contains **34** bibliography entries. They were exported to `edmonston-mulder-2024-references.md`. Bibliography entries were not converted into LiteratureAtoms solely because they were cited.

## Source and validation limitations

- The study is observational; residual and unmeasured confounding remain possible despite post-LASSO overlap weighting and sensitivity analyses.
- Prescriptions were used as treatment exposure; fills and adherence were not confirmed.
- Some outcomes were code-based and not prospectively adjudicated; eGFR measurement timing was not standardized.
- CKD was defined by eGFR without albuminuria, and patients with baseline eGFR <30 mL/min/1.73 m² were excluded.
- Abstract and detailed tables contain minor numerical discrepancies that were preserved rather than silently reconciled:
  - primary composite 95% CI: abstract 0.65–0.87 vs Table 2 0.65–0.86;
  - all-cause mortality HR: abstract 0.76 vs Table 2 0.75;
  - MI/stroke/death 95% CI: abstract 0.70–0.95 vs Table 2 0.70–0.94;
  - CKD primary composite: abstract 0.68 (0.53–0.88) vs Table 3 0.67 (0.52–0.86).
- Boehringer Ingelheim & Lilly Diabetes Alliance funded the study; sponsor review opportunity and reported author relationships are documented in the source.

## Output files

Stored under `GitHub Sync / Literature Review / Outputs / Clin Med Pharm`.

### JSON
- `edmonston-mulder-2024-atoms.json`
- `edmonston-mulder-2024-validation.json`
- `edmonston-mulder-2024-coverage.json`
- `edmonston-mulder-2024-sea-qa.json`

### HTML
- `edmonston-mulder-2024-sea.html`

### Markdown
- `edmonston-mulder-2024-references.md`
- `edmonston-mulder-2024-processing-report.md`
