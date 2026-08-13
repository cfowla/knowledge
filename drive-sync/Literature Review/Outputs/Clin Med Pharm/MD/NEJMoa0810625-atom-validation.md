# NEJMoa0810625 LiteratureAtom Validation Report
## Source metadata
- Primary: `NEJMoa0810625.pdf`
- Supporting: `NEJMoa0810625-appendix.pdf`
- Title: *Intensive versus Conventional Glucose Control in Critically Ill Patients*
- DOI: `10.1056/NEJMoa0810625`
- Trial: NICE-SUGAR; ClinicalTrials.gov `NCT00220987`
## Atom counts

- Total validated atoms: **47**
- `adverse_event`: 1
- `author_conclusion`: 1
- `comparator_description`: 1
- `conflict_of_interest`: 1
- `eligibility_criterion`: 11
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 4
- `method`: 1
- `outcome_definition`: 1
- `population_description`: 2
- `qualitative_result`: 7
- `quantitative_result`: 14
- `study_objective`: 1

## Structural validation
- Errors: **0**

## Sufficiency validation
- Errors: **0**
- Warnings: **0**

## Extraction limitations

- The atom schema does not provide dedicated fields for publication-level bibliographic metadata, randomization concealment, blinding, or trial registration; these are represented through source metadata, method/limitation atoms, and tags where applicable.
- Qualitative subgroup-interaction atoms preserve the reported interaction P values in canonical statements because the current quantitative-result object requires a single numerical effect estimate and is not designed for an interaction-only result without a corresponding estimate.
- The supporting appendix was used for eligibility criteria and treatment-limitation context. Appendix nutrition tables and detailed cause-of-death coding instructions were reviewed for SEA but were not atomized exhaustively because they did not add independently practice-changing assertions beyond the primary article results.
- No missing study detail was inferred or fabricated.
