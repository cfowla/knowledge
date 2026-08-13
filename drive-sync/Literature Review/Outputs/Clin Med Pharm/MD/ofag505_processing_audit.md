# ofag505 ATOM + SEA processing audit

## Source identity

- File: `ofag505.pdf`
- Title: Epidemiology and risk factors for infection in multiple myeloma patients treated with bispecific antibodies
- Journal: Open Forum Infectious Diseases
- DOI: 10.1093/ofid/ofag505
- Source type: major article; single-center observational cohort
- Study setting: University Hospital 12 de Octubre, Madrid, Spain
- Study period: January 2020 to May 2025
- PDF pages: 20
- SHA-256: `0e098786ddd72c4aba318d6b88ff57add58b27a069539cd75e961bad3b708a6d`

## Preflight / existing-output check

No existing `ofag505` or unmistakably title-equivalent ATOM/SEA artifact was found in the target `Clin Med Pharm/HTML`, `JSON`, or `MD` folders before processing. Both ATOM and SEA were therefore generated.

## Source coverage manifest

- Sections inspected: title/abstract; Introduction; Materials and Methods (study population and setting, study design, study definitions, antimicrobial prophylaxis, statistical analysis); Results (study population and outcomes, incidence and clinical syndromes, CMV, CRS/ICANS, overall/viral/bacterial risk factors, severe-infection risk factors); Discussion; conclusion; acknowledgements/funding/data availability/conflict-of-interest/AI declaration; references.
- Main-text tables: Table 1 (demographic/clinical characteristics), Table 2 (course outcomes), Table 3 (infection incidence/syndromes/grades/etiology). All reconciled.
- Main-text figures: Figure 1 (infectious syndromes), Figure 2 (causative agents). Both visually inspected from rendered PDF and represented in SEA with embedded crops plus structured interpretation.
- Supplementary material referenced by the manuscript but not present in the specified source folder: Supplementary Methods; Figure S1; Tables S1-S9. These were not reconstructed or substituted.
- Main-text numeric statements that explicitly summarize supplementary analyses were retained because they are directly reported in the primary PDF.

## ATOM validation

- Publication ID: `e690e30c-feda-55cf-a558-0e381df1d922`
- Total atoms: **110**
- Structural/Pydantic validation: **passed**
- JSON Schema validation: **passed**
- Sufficiency validation: **passed**
- Structural errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate canonical statements: 0

### Atom counts by kind

- `adverse_event`: 2
- `author_conclusion`: 4
- `conflict_of_interest`: 1
- `data_availability`: 1
- `eligibility_criterion`: 1
- `funding_disclosure`: 1
- `intervention_description`: 3
- `limitation`: 9
- `method`: 6
- `other`: 1
- `outcome_definition`: 3
- `population_description`: 11
- `qualitative_result`: 1
- `quantitative_result`: 64
- `study_objective`: 2

## Claim -> atom crosswalk

| Claim | Atom ID |
|---|---|
| Overall infection incidence 3.20/course-year | `6788c83c-5100-5c91-a97d-76a7d264a0fc` |
| Any infection in 81.6% of courses | `198022a5-21f8-523e-a6c6-d295303db6b8` |
| Severe infection in 45.9% of courses | `be013d94-041f-5c5c-81dd-4db097db14fd` |
| Anti-BCMA vs anti-GPRC5D aHR 1.41 | `8e2222cd-326a-5d71-a389-1f870001e532` |
| Prior BsAb exposure aHR 1.75 | `dd4f8c50-3797-5098-ac31-1985a616ad3a` |
| Prior allogeneic HSCT aHR 1.59 | `51786fd8-3ac1-5d73-b36a-0c30a547e354` |
| ICANS aHR 3.23 for overall infection | `831dfdd1-6af7-5c50-b5d7-a2f4d51c72ad` |
| IVIg aHR 0.68 for overall infection | `2d791d18-bb37-5f0a-8687-75541649b9bc` |
| IVIg aHR 0.42 for severe infection | `51fd250a-87e8-5c25-90dc-e68e875583e2` |
| First-CRS concurrent documented infection 6.8% | `3c13d5f6-9bd6-5d88-a3d2-240533199a9a` |
| Infections caused 46.2% of deaths | `40abef71-a8db-5dd8-9f4a-23e78f336ecd` |

## SEA coverage and QA

- Coverage manifest completed before HTML drafting.
- Tables 1-3 reconciled as structured blocks.
- Figures 1-2 reconciled via rendered visual inspection and embedded self-contained image crops.
- Claims and independent appraisal are separated.
- Appraisal scores were assigned after source extraction and visual/table reconciliation.
- HTML contains no internal chat/file citation syntax, remote scripts, remote stylesheets, or remote images.
- Supplementary-only content was explicitly marked unavailable.

## Limitations / unresolved items

1. The source PDF explicitly depends on unavailable Supplementary Methods, Figure S1, and Tables S1-S9 for additional definitions, pathogen detail, antibiotic-use detail, and full regression tables. This constrains independent verification of some methods and covariate-selection/model details.
2. The table reports on-treatment HGG as 81 (85.3%) without an explicit denominator on that row. The ATOM output preserves the reported count and percentage and does not infer a denominator.
3. Individual-agent causal comparisons are not supported by this observational, heterogeneous, single-center cohort; the article itself acknowledges this limitation.
4. The Results text reports bacteremia as 14/358 episodes even though the study consistently reports 352 total infection episodes; this denominator inconsistency was not silently corrected.
5. Table 1 reports PJP prophylaxis as 100 (100.0%) despite 98 total courses, another source-level count/denominator inconsistency; the extraction relies on the methods statement that prophylaxis was prescribed to all patients rather than inventing a corrected count.
6. No outside source was used to fill missing study material.
