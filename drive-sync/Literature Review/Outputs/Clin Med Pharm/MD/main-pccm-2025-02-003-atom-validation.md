# ATOM validation report - main.pdf

## Source metadata

- **Title:** Pulmonary embolism prophylaxis and treatment: What’s right, what’s wrong, and the future
- **Authors:** Bruce L Davidson; Nicolas De Schryver
- **Source type:** Narrative review article
- **Journal:** Chinese Medical Journal Pulmonary and Critical Care Medicine
- **Volume/pages:** 3 (2025), 1-5
- **DOI:** 10.1016/j.pccm.2025.02.003
- **Available online:** 10 March 2025
- **Source file:** main.pdf
- **SHA-256:** `ee258ca1ac4bbf1fe3399d12d04b913d1cc329325fcd22059fc416e1a4be3ab4`
- **Publication ID:** `0e8f95b9-e36c-5408-afc5-79d330025f21`
- **Extraction run:** `main-pccm-2025-02-003-v1`

## Extraction scope

The LiteratureAtom model is explicitly designed for primary literature, while this source is a narrative review. Atoms therefore represent assertions made by this review. Numerical findings attributed to cited studies are tagged `secondary_reported_result`; their provenance remains the review page, not the underlying primary paper. No atom is presented as if the review enrolled participants or generated those results.

## Atom counts

- **Total atoms:** 47
- `author_conclusion`: 10
- `conflict_of_interest`: 1
- `limitation`: 2
- `other`: 4
- `qualitative_result`: 8
- `quantitative_result`: 21
- `study_objective`: 1

## Assertion origin counts

- `directly_reported`: 1
- `normalized_from_source`: 46

## Validation

- **Pydantic structural errors:** 0
- **JSON Schema contract errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0

## Extraction limitations

- The source does not report a systematic search strategy, study-selection process, risk-of-bias method, or evidence-grading framework; those details were not invented.
- Review-level numerical summaries may omit denominators, exact population definitions, comparators, or uncertainty reported in the underlying primary papers. Those missing details remain missing in the atoms.
- The source contains no scientific figures, tables, algorithms, or supplements.
- Bibliographic reference entries were not atomized as evidence.
- Strong practice recommendations and criticisms were preserved as author conclusions or limitations, not converted into primary-study results.
