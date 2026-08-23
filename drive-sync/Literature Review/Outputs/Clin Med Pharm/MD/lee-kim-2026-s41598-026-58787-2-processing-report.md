# Processing report

## Source

- Folder: `Lee Kim 2026`
- Main file: `s41598-026-58787-2_reference.pdf`
- Supplement: `41598_2026_58787_MOESM1_ESM.docx`
- Title: Head-to-head comparative effectiveness of empagliflozin versus dapagliflozin and DPP-4 inhibitors on clinical and metabolic outcomes: a nationwide propensity-matched study
- DOI: `10.1038/s41598-026-58787-2`
- PMID: `42342812`
- Main SHA-256: `74bc6fcf8fd9ab626a61377111a130a8f3bf5d178d59696da050d890fb5abae5`
- Supplement SHA-256: `21b56ddc1a50cf0b3b0d4af46ca6030231146426faafbbef105d26465736c0da`
- Source version: accepted, unedited article-in-press manuscript.

## ATOM

- Atoms: **87**
- Kinds: `{"adverse_event": 6, "author_conclusion": 5, "comparator_description": 2, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 8, "funding_disclosure": 1, "intervention_description": 1, "limitation": 7, "method": 13, "other": 2, "outcome_definition": 13, "population_description": 7, "qualitative_result": 1, "quantitative_result": 18, "study_objective": 1}`
- Semantic batches: `{"lee-kim-2026-clinical-results-v1": 18, "lee-kim-2026-disclosures-v1": 3, "lee-kim-2026-general-v1": 20, "lee-kim-2026-interpretation-v1": 13, "lee-kim-2026-metabolic-results-v1": 6, "lee-kim-2026-outcomes-methods-v1": 22, "lee-kim-2026-population-results-v1": 5}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Exact duplicate canonical statements: **0**

The article is primary observational literature. Associations are preserved as reported; no observational association was converted into a causal claim.

## SEA and coverage

All 30 manuscript pages and all 8 rendered supplement pages were inspected. Two main-text figures, three main-text tables, four supplementary tables, and two supplementary figures were reconciled. The bibliography was extracted separately and was not atomized.

## Source-integrity findings

1. **Hospitalization definition conflict:** the main text defines all-cause hospitalization, while Supplementary Table S1 labels HOS as diabetes-related hospitalization with primary diagnosis E11.x–E14.x.
2. **Figure 2 direction-label conflict:** Table 2/prose interpret the printed HRs as EMPA versus comparator, but Figure 2 labels the series “DAPA vs EMPA” and “DPP4i vs EMPA.”
3. **Cohort-start date conflict:** Methods use January 1, 2016; Figure 1 prints drug exposure “since 2016.05.”
4. **Kidney-event definition mismatch:** main text includes new acute/chronic kidney disease, advanced CKD progression, or dialysis; Supplementary Table S1 describes incident AKI or advanced CKD using N17.x/N18.x/N19 without a dialysis procedure code.

No discrepancy was silently repaired.

## References

The article contains **34** numbered references. They were exported to `lee-kim-2026-s41598-026-58787-2-references.md` with PDF line wrapping normalized and without external bibliographic correction.

## Governing sources applied

ATOM: `literature(1).py` → `literature_atoms(1).py` → `literature_atom.schema.json` → `README(2).md` → `example_atom(1).json` (illustrative only). Large-source execution used `large-source-ATOM-SEA.md`. SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as governing protocol; v3 was historical reference only.

`unslop.skill.md` was requested as a writing control, but no actual `unslop.skill.md` source file was available in the supplied project sources; Drive search located only prior reports mentioning it. No unsourced requirements were inferred from those mentions.

## Output files

- `lee-kim-2026-s41598-026-58787-2-atoms.json`
- `lee-kim-2026-s41598-026-58787-2-validation.json`
- `lee-kim-2026-s41598-026-58787-2-coverage.json`
- `lee-kim-2026-s41598-026-58787-2-crosswalk.json`
- `lee-kim-2026-s41598-026-58787-2-sea.html`
- `lee-kim-2026-s41598-026-58787-2-sea-qa.json`
- `lee-kim-2026-s41598-026-58787-2-references.md`
- `lee-kim-2026-s41598-026-58787-2-processing-report.md`
