# NEJMoa1501035 — ATOM validation report

## Source metadata

- **Title:** Perioperative Bridging Anticoagulation in Patients with Atrial Fibrillation
- **Study:** BRIDGE trial
- **DOI:** 10.1056/NEJMoa1501035
- **Registry:** NCT00786474
- **Primary:** `NEJMoa1501035.pdf`
- **Supporting:** `nejmoa1501035_appendix.pdf`, `nejmoa1501035_protocol.pdf`
- **Publication ID:** `1538b880-4a92-5dee-ac56-ce1ea24c94c4`
- **Primary SHA-256:** `9bd3af1edc7628532c691787b8bd6fd45c204c40d6976afea6568e764a44c6f6`

## Atom counts

- **Total atoms:** 27
- `adverse_event`: 2
- `author_conclusion`: 1
- `comparator_description`: 1
- `eligibility_criterion`: 2
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 4
- `method`: 5
- `outcome_definition`: 2
- `population_description`: 1
- `quantitative_result`: 6
- `study_objective`: 1

## Validation

- Pydantic structural validation: **PASS**
- `literature_atom.schema.json` validation: **PASS**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

No atom-kind sufficiency issues were detected.

## Extraction limitations

- The primary article remains the evidence-generating source. Eligibility and detailed endpoint definitions from the Supplementary Appendix are anchored as supplement-derived context.
- The long protocol was used to confirm prespecified design, dosing, endpoints, and analysis context; administrative and operational protocol material was not atomized.
- Secondary outcome risk differences computed from reported arm percentages are explicitly marked `calculated_from_reported_data`.
- Discussion references were not converted into BRIDGE primary-study atoms.
