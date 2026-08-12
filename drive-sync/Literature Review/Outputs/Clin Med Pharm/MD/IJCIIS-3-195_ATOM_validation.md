# @ATOM extraction report — IJCIIS-3-195.pdf

## Source metadata

- **Title:** Comparison of heparin dosing based on actual body weight in non-obese, obese and morbidly obese critically ill patients
- **Authors:** Anthony T. Gerlach; Jerilynn Folino; Benjamin N. Morris; Claire V. Murphy; Stansilaw P. Stawicki; Charles H. Cook
- **Journal:** International Journal of Critical Illness and Injury Science
- **Year / issue:** 2013; 3(3):195-199
- **DOI:** 10.4103/2229-5151.119200
- **Design:** Retrospective single-center review of continuous UFH infusions in critically ill patients
- **Publication ID:** `cf250087-756c-5e61-ba2b-ff057ff16a74`
- **Evaluated file:** `IJCIIS-3-195.pdf`
- **Raw PDF SHA-256:** `971e4beebe41fe8dbc0db359b00d14d2e76d6ddc115e9fd87400b1ccb7b1a0ac`

## Extraction summary

- **Atoms extracted:** 81
- **Structural validation errors:** 0
- **JSON Schema validation errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0
- **Review status:** `needs_review` for all atoms (language-model extraction; no human verification asserted)

### Atom counts by type

| Atom kind | Count |
|---|---:|
| `adverse_event` | 4 |
| `author_conclusion` | 2 |
| `conflict_of_interest` | 1 |
| `eligibility_criterion` | 2 |
| `funding_disclosure` | 1 |
| `intervention_description` | 2 |
| `limitation` | 4 |
| `method` | 2 |
| `outcome_definition` | 5 |
| `population_description` | 8 |
| `qualitative_result` | 4 |
| `study_objective` | 1 |
| `subgroup_result` | 45 |

## Validation report

### Structural validation
PASS — every atom round-tripped through the governing `LiteratureAtom` Pydantic model.

### Serialization contract
PASS — every serialized atom validated against `literature_atom.schema.json`.

### Sufficiency validation
PASS — no atom-kind sufficiency errors or warnings were returned.

## Extraction limitations

- The schema has no dedicated field for standard deviation; means are normalized into `quantitative_result.estimate`, while the source-reported ±SD is retained in the canonical statement and `original_result_text`.
- Between-group P values reported in Tables 3 and 4 are associated with each corresponding group-specific atom because the current schema lacks a multi-arm aggregate comparison object that cleanly separates row-level P values from individual arm estimates.
- Table 1 is preserved as a method/protocol atom and in the SEA structured table rather than atomizing every titration row into separate intervention atoms.
- No thrombosis/clinical efficacy endpoint was reported; the study primarily evaluates aPTT-based surrogate anticoagulation control and bleeding observations.
- Data availability was not reported in the article and no `data_availability` atom was invented.

## Source coverage

- Pages 1-5 inspected from the raw PDF.
- Main-text tables reconciled: Table 1 (heparin protocol), Table 2 (demographics), Table 3 (heparin dosage), Table 4 (outcomes).
- Main-text figures: none.
- Appendices/supplements: none in the retrieved PDF.
