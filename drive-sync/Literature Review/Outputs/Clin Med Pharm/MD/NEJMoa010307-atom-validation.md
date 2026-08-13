# ATOM Extraction and Validation Report - NEJMoa010307

## Source metadata

- **Title:** Early Goal-Directed Therapy in the Treatment of Severe Sepsis and Septic Shock
- **Authors:** Emanuel Rivers; Bryant Nguyen; Suzanne Havstad; Julie Ressler; Alexandria Muzzin; Bernhard Knoblich; Edward Peterson; Michael Tomlanovich; Early Goal-Directed Therapy Collaborative Group
- **Journal:** New England Journal of Medicine 2001;345:1368-1377
- **DOI:** 10.1056/NEJMoa010307
- **Primary file:** `NEJMoa010307.pdf`
- **Corresponding materials:** None
- **Primary PDF SHA-256:** `c8b32c982836960102c9a1aa3ab288443be57034cffa23d33b1d4898260ed150`
- **Publication ID:** `b018bd98-8372-5451-b4c0-dd644b428a5b`

## Extraction summary

- **Total atoms:** 54
- **Assertion origin policy:** Source-supported assertions were normalized into independently reviewable canonical statements. No appraisal statements were converted into reported evidence. No unreported study details were invented.
- **Review status:** `needs_review` for all atoms; extraction is structurally/sufficiency validated but not human-verified.

### Atom counts by kind

| Atom kind | Count |
|---|---:|
| `author_conclusion` | 1 |
| `comparator_description` | 1 |
| `eligibility_criterion` | 2 |
| `funding_disclosure` | 1 |
| `intervention_description` | 6 |
| `limitation` | 3 |
| `method` | 7 |
| `outcome_definition` | 2 |
| `population_description` | 1 |
| `qualitative_result` | 1 |
| `quantitative_result` | 25 |
| `study_objective` | 1 |
| `subgroup_result` | 3 |

## Validation

- **Pydantic structural errors:** 0
- **JSON Schema errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0

**Status: PASS.** Every atom round-tripped through the `LiteratureAtom` Pydantic model, validated against `literature_atom.schema.json`, and passed `validate_literature_atom_sufficiency()` without errors or warnings.

## Extraction limitations

- The article is a 10-page journal PDF with no corresponding correction or supplement supplied in the requested Drive folder.
- The extraction targets independently reviewable claims and does not attempt cell-by-cell atomization of every baseline covariate or every coagulation variable in Table 2.
- The paper does not present a dedicated adverse-event section; treatment administration and causes of death were captured as quantitative-result atoms rather than reclassified as adverse events.
- The funding statement was extracted. No separate conflict-of-interest statement was identified in the supplied PDF, so none was invented.
- Source anchors use journal page numbers plus section/table/figure locators. All atoms remain linked to the same publication identity.
- The article uses 2001 sepsis definitions and an intervention bundle that requires historical/current-practice contextualization; this is handled in the SEA artifact rather than in reported-data atoms.

## Output

- Validated atom JSON: `NEJMoa010307-atoms.json`
- This validation report: `NEJMoa010307-atom-validation.md`