# NEJMoa1511939 ATOM Validation Report

## Source identity

- Primary article: **A Randomized Trial of Intensive versus Standard Blood-Pressure Control** (SPRINT Research Group), N Engl J Med 2015;373:2103-2116. DOI: 10.1056/NEJMoa1511939.
- Primary file: `NEJMoa1511939.pdf`
- Supporting material: protocol, supplementary appendix, and 2017 correction supplied alongside the article.
- Shared publication ID: `2e130261-aa2d-5f02-8074-f3a20e3e22e5`

## Supporting-material handling

The primary article remains the publication object. Protocol/supplement-derived atoms use the same publication ID but retain support-file SHA-256 hashes and distinct extraction run IDs. The 2017 correction is authoritative for the two affected Framingham-risk rows in Table 1 and is not treated as a treatment-effect result.

## Atom counts

Total atoms: **33**

- `adverse_event`: 6
- `author_conclusion`: 1
- `comparator_description`: 1
- `eligibility_criterion`: 1
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 2
- `method`: 4
- `outcome_definition`: 1
- `qualitative_result`: 1
- `quantitative_result`: 10
- `study_objective`: 1
- `subgroup_result`: 3

## Validation

- Structural validation errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

None.

## Extraction limitations

- Atoms prioritize independently reviewable design, efficacy, renal, safety, correction, and interpretation assertions central to the primary report; the 261-page protocol was used as supporting context rather than exhaustively atomized.
- Cognitive, dementia, and MRI outcomes planned in the protocol were not reported in this 2015 primary article and were not converted into outcome-result atoms.
- No appraisal statements were encoded as reported study data.
- Reported NNT values were retained as directly reported; no new NNT/NNH calculations were inserted.
