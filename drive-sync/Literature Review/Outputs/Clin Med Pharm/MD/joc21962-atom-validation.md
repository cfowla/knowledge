# ATOM Validation Report — joc21962.pdf

- **Source:** Major Outcomes in High-Risk Hypertensive Patients Randomized to Angiotensin-Converting Enzyme Inhibitor or Calcium Channel Blocker vs Diuretic: The Antihypertensive and Lipid-Lowering Treatment to Prevent Heart Attack Trial (ALLHAT)
- **Supporting correction:** `joc21962-correction.pdf` — corrected Table 6 replaces the original table; the correction states that results and conclusions are unaffected.
- **Publication ID:** `e5ea1e9b-7b9d-5484-bf67-f682cadffd36`
- **Atoms extracted:** 74

## Counts by atom kind
- `adverse_event`: 2
- `author_conclusion`: 2
- `conflict_of_interest`: 1
- `eligibility_criterion`: 2
- `funding_disclosure`: 3
- `intervention_description`: 3
- `limitation`: 4
- `method`: 5
- `other`: 2
- `outcome_definition`: 6
- `population_description`: 2
- `qualitative_result`: 1
- `quantitative_result`: 37
- `study_objective`: 1
- `subgroup_result`: 3

## Validation
- Pydantic structural validation: **PASS** (0 errors)
- JSON Schema validation: **PASS** (0 errors)
- Sufficiency validation: **PASS** (0 errors, 0 warnings)

## Correction handling
- Original Table 6 on journal page 2992 is superseded by the January 8, 2003 correction.
- Corrected total deaths: chlorthalidone 2203 (17.3 per 100 persons), amlodipine 1256 (16.8), lisinopril 1314 (17.2).
- Corrected noncardiovascular deaths: 1067 (8.9), 571 (8.0), and 616 (8.6), respectively; amlodipine vs chlorthalidone P=.04.
- Corrected unintentional injury/suicide/homicide deaths: 66 (0.6), 19 (0.4), and 28 (0.4), respectively; amlodipine vs chlorthalidone P=.005. The article notes this was not a prespecified hypothesis.
- The correction explicitly states that the revised data do not affect the original results or conclusions.

## Extraction limitations
- Atoms prioritize the study design, treatment exposure, endpoint definitions, major clinical outcomes, important intermediate/safety outcomes, prespecified subgroup findings, correction, conclusions, limitations, funding, and conflicts rather than atomizing every background citation or every individual cell in Tables 1-6.
- No external sources were used to add study details not present in the primary PDF or correction.
- The primary PDF itself contains the January 2003 Table 6 correction as appended material on PDF page 18; the separately supplied correction PDF was treated as the authoritative supporting correction and used to supersede original Table 6 values.
