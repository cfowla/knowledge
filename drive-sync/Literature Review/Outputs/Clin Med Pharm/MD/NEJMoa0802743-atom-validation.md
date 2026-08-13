# NEJMoa0802743 ATOM Validation Report

## Source identity

- Primary article: **Effects of Intensive Glucose Lowering in Type 2 Diabetes** (The Action to Control Cardiovascular Risk in Diabetes Study Group), N Engl J Med 2008;358:2545-2559. DOI: 10.1056/NEJMoa0802743.
- Primary file: `NEJMoa0802743.pdf`
- Supporting material: `NEJMoa0802743-supplemental.pdf`
- Shared publication ID: `da63b382-771a-5ace-a1a9-01740f695477`

## Supporting-material handling

The primary article remains the publication object. Supplement-derived assertions use the same publication ID while retaining the supplement SHA-256 hash and a distinct extraction run ID. The supplement was used for participant-flow and mortality-category context and was not treated as an independent study.

## Atom counts

Total atoms: **35**

- `adverse_event`: 5
- `author_conclusion`: 1
- `comparator_description`: 1
- `conflict_of_interest`: 1
- `eligibility_criterion`: 1
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 2
- `method`: 5
- `other`: 1
- `outcome_definition`: 1
- `population_description`: 1
- `qualitative_result`: 4
- `quantitative_result`: 9
- `study_objective`: 1

## Validation

- Structural validation errors: **0**
- Serialization-schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

None.

## Extraction limitations

- Atoms prioritize independently reviewable design, exposure, efficacy, safety, subgroup, supporting-flow, funding, limitation, and interpretation assertions central to the primary report.
- The supplement was incorporated where it added participant-flow and mortality-category detail; it was not exhaustively atomized row-by-row.
- The trial could not identify which component of the multifactorial intensive glycemia strategy caused the mortality signal; no mechanism was invented.
- Appraisal judgments were not encoded as reported study data.
- The number-needed-to-harm statement was retained only because it was directly reported by the article authors; it was not newly calculated by the extractor.
