# NEJM200101043440101 ATOM Validation Report

## Source identity

- Primary article: **Effects on Blood Pressure of Reduced Dietary Sodium and the Dietary Approaches to Stop Hypertension (DASH) Diet** (Sacks et al.; DASH-Sodium Collaborative Research Group), N Engl J Med 2001;344:3-10.
- Primary file: `NEJM200101043440101.pdf`
- Supporting material: none specified.
- Shared publication ID: `c3ff34cf-b331-5c34-abbf-4f5b0865e902`
- Primary PDF SHA-256: `5ce2b1c18c7232c74e45c72d954c7b7042c222efff16719dffbcb99ba6b12519`

## Atom counts

Total atoms: **51**

- `adverse_event`: 2
- `author_conclusion`: 1
- `comparator_description`: 1
- `eligibility_criterion`: 1
- `funding_disclosure`: 1
- `intervention_description`: 2
- `limitation`: 2
- `method`: 8
- `outcome_definition`: 1
- `population_description`: 1
- `qualitative_result`: 9
- `quantitative_result`: 17
- `study_objective`: 1
- `subgroup_result`: 4

## Validation

- Structural validation errors: **0**
- Serialization-schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

None.

## Extraction limitations

- Atoms prioritize independently reviewable design, population, dietary exposure, adherence, blood-pressure efficacy, subgroup, tolerability, funding, limitation, and conclusion assertions central to the primary report.
- No corresponding materials were specified, so only the primary article was used.
- The article reports blood pressure over 30-day feeding periods; long-term cardiovascular outcomes were not measured in this report and were not inferred.
- Numeric confidence intervals were normalized into ascending lower/upper bounds where the source prose presented negative reductions in reverse textual order.
- Appraisal judgments were not encoded as reported study data.
- The DOI was not printed in the evaluated PDF and was therefore left unset rather than inferred from the filename.
