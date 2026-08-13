# dkag282 @ATOM validation report

- **Source:** Inter- and intraindividual variability of long-acting injectable cabotegravir/rilpivirine trough concentrations after 1 year of continuous use
- **DOI:** 10.1093/jac/dkag282
- **Primary PDF SHA-256:** `c3e7fdeec14759260230ec19394d9a37190b213b5784bf9315df89d2c1cf7c65`
- **Publication ID:** `d587c1c3-ae05-5769-9d40-cb56bdbc5cc5`
- **Atoms extracted:** **53**
- **Pydantic structural validation:** **PASS**
- **JSON Schema serialization validation:** **PASS**
- **Sufficiency validation:** **PASS**
- **Sufficiency warnings:** **0**

## Atom counts by kind

- `author_conclusion`: 5
- `conflict_of_interest`: 1
- `data_availability`: 1
- `eligibility_criterion`: 3
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 6
- `method`: 10
- `outcome_definition`: 3
- `population_description`: 1
- `qualitative_result`: 1
- `quantitative_result`: 19
- `study_objective`: 1

## Assertion origin counts

- `calculated_from_reported_data`: 1
- `directly_reported`: 31
- `normalized_from_source`: 21

## Validation issues

No structural, serialization-contract, sufficiency errors, or sufficiency warnings were detected.

## Extraction limitations

- Supplementary Table S1 was not supplied and was not fetched or substituted, per task instructions.
- The article reports 8 participants (17%) with at least one detectable HIV RNA value; this percentage was preserved as reported rather than recalculated.
- The transparency statement uses the initials J.M.D., which do not directly match a listed author name in the article header; the initials were preserved without identity inference.

## Source-material boundary

Only the primary `dkag282.pdf` was used. The article mentions Supplementary Table S1, but no corresponding correction or supplementary file was specified for this task, so it was not invented, substituted, or retrieved.
