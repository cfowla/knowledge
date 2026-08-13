# NEJMoa1214103 ATOM Validation Report

## Source metadata

- Primary: `NEJMoa1214103.pdf` — Guérin C, et al. **Prone Positioning in Severe Acute Respiratory Distress Syndrome.** N Engl J Med. 2013;368:2159-2168. DOI: 10.1056/NEJMoa1214103.
- Supporting protocol: `NEJMoa1214103-protocol.pdf`
- Supporting appendix: `NEJMoa1214103-supplemental.pdf`
- Publication ID: `0e00c70b-fca9-5255-ae14-b1feb1a766be`
- Primary SHA-256: `4ff7d3b0be54fe3aee650c0b292e1b2cda661905c9b31bac4221721246e2c687`
- Extraction run: `NEJMoa1214103-primary-plus-support-v1`

## Atom counts

Total validated atoms: **32**

- `adverse_event`: 2
- `author_conclusion`: 1
- `comparator_description`: 1
- `conflict_of_interest`: 1
- `eligibility_criterion`: 2
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 3
- `method`: 5
- `outcome_definition`: 2
- `population_description`: 1
- `qualitative_result`: 1
- `quantitative_result`: 9
- `study_objective`: 1
- `subgroup_result`: 1

## Structural validation

- Errors: **0**


## Sufficiency validation

- Errors: **0**
- Warnings: **0**


## Extraction limitations

- The ATOM schema is assertion-centered and does not provide a publication-level metadata object; publication metadata are therefore reported here rather than embedded outside the validated atom objects.
- Supporting protocol content is largely French; only protocol details directly relevant to prespecification and intervention implementation were incorporated.
- The article reports an unusual hazard-ratio presentation for successful extubation; the extubation atom therefore preserves the directly reported arm proportions rather than inferring the direction/meaning of that hazard ratio.
- Mechanistic explanations in the Discussion were not converted into reported mechanistic findings when they were not directly measured.

## Validation status

**PASS** if structural errors = 0 and sufficiency errors = 0.

Final status: **PASS**
