# ATOM Validation Report — NEJM199902113400601


## Source metadata


- **Title:** A Multicenter, Randomized, Controlled Clinical Trial of Transfusion Requirements in Critical Care
- **Citation:** N Engl J Med 1999;340:409-417
- **Primary file:** `NEJM199902113400601.pdf`
- **Supporting correction:** `NEJM199902113400601-correction.pdf` (N Engl J Med 1999;340:1056)
- **Publication ID:** `091dc575-22c0-54f1-9ce3-730f654f0f18`
- **Primary SHA-256:** `86165cef0c14e6f3a0c6a1a4d1796e7d7641b3f807eeed76f0efa24e68ca45f0`
- **Correction SHA-256:** `fe7a80665d6fddda9ee683f597e174588d91b4bb4a1517cdd47043c40e28501b`


## Correction incorporation


- Page 412 enrollment comparison corrected to 20% cardiac disease among enrolled patients versus 26% among those not enrolled (P<0.01).
- Page 413 wording corrected from P=0.15 and P=0.58 to P>0.15 and P>0.58 for similarity of cointerventions.


## Atom counts by type


| Atom kind | Count |
|---|---:|
| `adverse_event` | 4 |
| `author_conclusion` | 2 |
| `comparator_description` | 1 |
| `eligibility_criterion` | 2 |
| `funding_disclosure` | 1 |
| `intervention_description` | 1 |
| `limitation` | 4 |
| `method` | 3 |
| `outcome_definition` | 2 |
| `population_description` | 3 |
| `qualitative_result` | 1 |
| `quantitative_result` | 14 |
| `study_objective` | 1 |
| `subgroup_result` | 7 |
| **Total** | **46** |


## Validation status


- Pydantic structural validation errors: **0**
- JSON Schema validation errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Schema validation executed: **yes**


## Extraction limitations


- Atoms were extracted from the primary 9-page article and the 1-page published correction; no external sources were used.
- The article reports several means with standard deviations, but the current LiteratureAtom schema has no dedicated SD field; SDs are preserved in canonical/original-result text where central.
- For subgroup comparisons where the article reported arm rates plus a confidence interval for an absolute difference but did not print the point difference, the difference was calculated from the reported rates and marked `calculated_from_reported_data`.
- The original article was designed as an equivalence trial but was stopped early; appraisal of whether formal equivalence was demonstrated is kept in the SEA artifact rather than encoded as reported trial data.
- Review status remains `needs_review`; validation confirms structural/schema/sufficiency conformance, not independent human verification of every extraction choice.
- No DOI, PMID, or current-practice guideline alignment was added because those items were not present in the supplied source bundle and external verification was not requested.