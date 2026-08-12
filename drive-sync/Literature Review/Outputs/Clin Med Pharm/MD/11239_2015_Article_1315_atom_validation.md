# ATOM validation report — 11239_2015_Article_1315.pdf

## Source metadata

- Title: Guidance for the practical management of the heparin anticoagulants in the treatment of venous thromboembolism
- Authors: Maureen A. Smythe; Jennifer Priziola; Paul P. Dobesh; Diane Wirth; Adam Cuker; Ann K. Wittkowsky
- Journal: Journal of Thrombosis and Thrombolysis 41:165–186 (2016)
- DOI: 10.1007/s11239-015-1315-2
- Source file: 11239_2015_Article_1315.pdf
- SHA-256: `352ed4497254dabee9294559cd80c398ef675500bb14b6eac6f2281bd06e5f65`
- Publication ID: `86789a1e-ea94-5d7a-a04a-cc9d2ff80a6e`
- Source type: clinical guidance / focused literature review with multidisciplinary consensus recommendations

## Extraction summary

- Extracted atoms: **73**
- Structural validation errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Serialization-schema errors (`literature_atom.schema.json`): **0**

### Atom counts by kind

- `author_conclusion`: 63
- `conflict_of_interest`: 1
- `funding_disclosure`: 1
- `limitation`: 4
- `method`: 3
- `study_objective`: 1

## Validation status

All 73 emitted atoms were instantiated through the governing Pydantic `LiteratureAtom` model. Sufficiency validation was then run with `validate_literature_atom_sufficiency` for every atom.

- Structural errors: None.
- Sufficiency errors: None.
- Sufficiency warnings: None.

## Source-type/schema boundary

This source is a **guidance document/secondary synthesis**, not a primary study. The current LiteratureAtom schema has no dedicated `guideline_recommendation` atom kind. To avoid implying that the guidance document generated the underlying trial data, recommendation statements are represented as `author_conclusion` atoms with descriptive tags including `guideline_recommendation` and `secondary_source_guidance`. Embedded trial results cited by the authors were not converted into primary-study `quantitative_result` atoms; those should be extracted from the cited primary publications when primary-study atoms are required.

## Extraction limitations

- The focused review was not reported as a systematic review with reproducible full search strings, screening flow, risk-of-bias assessment, or formal evidence-certainty grading.
- Table 5 was used as the principal recommendation anchor because it consolidates the guidance statements and preserves question-level context.
- Recommendations were split into independently reviewable assertions where defensible, so one Table 5 row may yield several atoms.
- All emitted atoms remain `needs_review`; no human verification step was performed in this run.
