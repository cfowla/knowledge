# ciag422 LiteratureAtom Validation Report

- **Structural validation:** PASS
- **Sufficiency validation:** PASS
- **Validated atoms:** 69
- **Structural/schema errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0

## Atom counts by kind

- `adverse_event`: 7
- `author_conclusion`: 3
- `conflict_of_interest`: 1
- `eligibility_criterion`: 1
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 4
- `method`: 4
- `outcome_definition`: 3
- `population_description`: 31
- `qualitative_result`: 2
- `quantitative_result`: 10
- `study_objective`: 1

## QA warning

- **Source internal denominator discrepancy:** Table 1 reports on-treatment ALT/AST/total bilirubin as n=9 with 9/9 normal, while the Results narrative reports liver function tests available in 8/10 with no elevations. Both source assertions are retained separately and neither was corrected or merged.

## Extraction limitations

- Retrospective source with incomplete follow-up denominators; atoms preserve reported denominators rather than imputing missing data.
- The source contains a liver-test denominator discrepancy (8 in narrative vs 9 in Table 1).
- No supplementary source material or correction was specified for this task.
- Bibliography entries were not atomized because they are not study-generated assertions.

## Validation note

Every atom was instantiated through the governing Pydantic `LiteratureAtom` model and then passed through `validate_literature_atom_sufficiency`. The serialized output was also checked against `literature_atom.schema.json`; the provided schema exactly matches the model-generated JSON schema.
