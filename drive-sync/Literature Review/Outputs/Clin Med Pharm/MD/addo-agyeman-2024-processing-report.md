# Addo Agyeman 2024 processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source

- Title: Dapagliflozin in Heart Failure: A Comprehensive Meta-analysis on Functional Capacity, Symptoms, and Safety Outcomes
- Authors: Basilio Addo, Walter Agyeman, Sammudeen Ibrahim, Patrick Berchie
- Journal: American Journal of Cardiovascular Drugs. 2024;24:753–773.
- DOI: 10.1007/s40256-024-00669-x
- PMID: 39261443
- Source file: `Dapagliflozin_in_Heart_Failure.pdf`, 22 PDF pages, SHA-256 `239a5e406394a7745e08e691ae18acb0b9f5ad0dfbc88a5d43520693bc1b0e76`
- Shared publication ID: `92e12ad5-4c14-578f-9ff2-9233bd3a0e77`
- Source type: systematic review and conventional meta-analysis of randomized clinical trials

## ATOM result

- Total LiteratureAtoms: 52
- Counts by kind: `{"adverse_event": 2, "author_conclusion": 4, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 1, "funding_disclosure": 1, "intervention_description": 1, "limitation": 3, "method": 11, "outcome_definition": 5, "population_description": 2, "qualitative_result": 6, "quantitative_result": 4, "study_objective": 1, "subgroup_result": 8}`
- Assertion origins: `{"directly_reported": 21, "normalized_from_source": 31}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0

All atoms use `needs_review` because extraction was model-assisted and has not received independent human verification.

## SEA result

The source was appraised as a systematic review/meta-analysis of randomized heart-failure trials of dapagliflozin. Coverage reconciled all **7 main-text figures** and **2 main-text tables**, including the PRISMA study-selection workflow and the risk-of-bias figure. No supplement was present in the source packet.

Key pooled results preserved in the appraisal include: 6-minute walk distance MD 3.59 m (95% CI −1.44 to 8.63); KCCQ MD 2.75 points (95% CI 1.95 to 3.56); heart-failure hospitalization RR 0.76 (95% CI 0.68 to 0.84); all-cause mortality RR 0.90 (95% CI 0.83 to 0.99); and any adverse event RR 0.98 (95% CI 0.93 to 1.03).

Verdict: **Skim deeply**. The review is useful as secondary orientation to dapagliflozin heart-failure evidence, but should not be used as a cornerstone source for dapagliflozin-versus-empagliflozin equivalence or formulary interchangeability because it does not directly compare the drugs and contains material reporting/methodological inconsistencies.

## References

The primary article contains **40** bibliography entries. They were exported to `addo-agyeman-2024-references.md`. Bibliography entries were not converted into LiteratureAtoms solely because they were cited.

## Source and validation limitations

- `literature.py`, `literature_atoms.py`, and `literature_atom.schema.json` were available and executed as the governing ATOM model, sufficiency validator, and serialization contract.
- `summary-evaluation-appraisal-protocol-v4-compact.md` was available and used as the governing SEA protocol; the v3 HTML was treated as historical reference only.
- `README(2).md` and `example_atom.json` were not present in the supplied project files and were not found by exact Drive search; their supporting workflow/example guidance could not be inspected.
- The source reports 10 included studies, but Table 2 additionally contains Wiviott 2019/DECLARE baseline rows that are absent from Table 1, Figure 2, and the outcome forest plots and are incompatible with the reported pooled N=12,695 if treated as included HF trial data.
- Section 3.3 states nine trials had overall “some concerns” risk of bias and two had low risk, while Figure 2 visually shows eight “some concerns” and two low-risk trials.
- Continuous outcomes are correctly analyzed/labeled as mean differences in the Methods and forest plots, but the Abstract/Results prose repeatedly calls the 6MWD and KCCQ pooled estimates risk ratios.
- The Abstract adverse-event result is internally inconsistent (RR 0.96 with 95% CI 0.98–1.03); Section 3.5.3 and Figure 7 report RR 0.98 (95% CI 0.93–1.03).
- The Discussion describes a significant reduction in overall adverse events even though the pooled adverse-event result is nonsignificant.
- The conclusion overstates mortality benefit across heart-failure phenotypes; the HFrEF mortality subgroup is significant, while the HFpEF subgroup is not.
- No protocol/registration, GRADE certainty assessment, or publication-bias/small-study-effect analysis was reported in the source.

## Output files

Stored under `GitHub Sync / Literature Review / Outputs / Clin Med Pharm`.

### JSON

- `addo-agyeman-2024-atoms.json`
- `addo-agyeman-2024-validation.json`
- `addo-agyeman-2024-coverage.json`
- `addo-agyeman-2024-sea-qa.json`

### HTML

- `addo-agyeman-2024-sea.html`

### Markdown

- `addo-agyeman-2024-references.md`
- `addo-agyeman-2024-processing-report.md`
