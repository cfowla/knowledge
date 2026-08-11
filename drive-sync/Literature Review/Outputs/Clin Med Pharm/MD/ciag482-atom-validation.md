# ATOM extraction and validation report — ciag482.pdf

## Source metadata

- **Title:** A novel RNA nucleic acid amplification test more accurately distinguishes active Clostridioides difficile infection from colonization
- **Journal:** Clinical Infectious Diseases
- **DOI:** 10.1093/cid/ciag482
- **Source type:** Major Article; diagnostic assay development and single-center diagnostic-accuracy evaluation
- **Publication identity (shared `publication_id`):** `c7e789ce-33a4-5917-baf1-aa58d819e539`
- **Input SHA-256:** `ed840dedc3b677a43b254e72ade4254d11a8a60b3df32fdbc12f1e88c98af1db`
- **Extraction run:** `ciag482-20260811-v1`
- **Extractor:** GPT-5.6 Sol via `@ATOM`

## Atom counts

- **Total atoms:** 69

- `author_conclusion`: 3
- `conflict_of_interest`: 1
- `data_availability`: 1
- `eligibility_criterion`: 2
- `funding_disclosure`: 1
- `limitation`: 2
- `method`: 8
- `other`: 1
- `population_description`: 2
- `qualitative_result`: 5
- `quantitative_result`: 42
- `study_objective`: 1

## Validation status

- Pydantic structural errors: **0**
- Supplied JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

## Extraction limitations

- The retrieved PDF is an accepted manuscript and references **Supplemental File S1** (complete methods) and **Supplemental File S2** (discordant-case adjudication details), but those supplements were not present in the retrieved PDF and were not separately fetched. Atoms therefore do not invent supplement-only details.
- The study has no perfect gold standard for metabolically active toxigenic C. difficile; discordant cases were resolved by blinded chart review, exactly as reported by the authors.
- Diagnostic performance atoms preserve reported post-adjudication 2×2 counts and metrics. No unreported confidence intervals were calculated.
- Author interpretation and implementation proposals are represented as `author_conclusion` or `other`, not as reported patient outcomes.
- All atoms retain one shared publication identity and source-level SHA-256 provenance; each atom has an independent UUID and source anchor.

## Output

- Validated atom JSON: `ciag482-atoms.json`
