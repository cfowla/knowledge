# ATOM extraction and validation report — jgi_117.pdf

## Source metadata

- **Title:** Anticoagulation Therapy in Patients with Venous Thromboembolic Disease
- **Authors:** Jeff Whittle, MD, MPH; Patti Johnson, RN; A. Russell Localio, MPH, MS
- **Source:** Journal of General Internal Medicine. 1998;13:373-378.
- **Source type:** Cross-sectional retrospective chart review of a population-based random sample
- **Study setting:** 21 randomly selected Pennsylvania hospitals; Medicare beneficiaries treated in 1992
- **Drive file:** jgi_117.pdf (Google Drive file ID `104qD63tEtCJwR1qxnKqjJbiQM5rY8o6t`)
- **PDF SHA-256:** `61a04091ade26f09d7c9101d9456c58af75d287973383f922ca5318c7f6bf472`
- **Publication UUID:** `df66cebc-00f1-5be5-a4bd-5deffbe7afb5`

## Atom counts

- **Total atoms:** 35
- `author_conclusion`: 2
- `eligibility_criterion`: 2
- `funding_disclosure`: 1
- `limitation`: 2
- `method`: 4
- `outcome_definition`: 4
- `population_description`: 1
- `qualitative_result`: 3
- `quantitative_result`: 15
- `study_objective`: 1

## Validation

- **Pydantic structural errors:** 0
- **JSON Schema errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0
- **Status:** PASS

## Extraction limitations

- Table 1 reports male gender as `128 (36%)`; 128/270 is not 36%. The source value is internally inconsistent. No correction was invented, and this datum was not atomized as a quantitative population result.
- VTE diagnosis did not require independent laboratory confirmation; the study intentionally evaluated treatment given the attending physician's diagnosis.
- The therapeutic PTT definition used `>1.5 times control`; the authors explicitly note that this threshold can vary by reagent and laboratory.
- The reported 90-day VTE readmission comparison is described as “data not shown,” limiting independent verification from the article.
- Length-of-stay findings are observational associations, not randomized causal estimates of early warfarin initiation.
- The study evaluates 1992 practice against 1989 ACCP consensus recommendations and is a historical quality-of-care study, not a current anticoagulation protocol.

## Representation notes

- Reported, normalized, calculated, and inferred origins were kept distinct. No calculated or extractor-inference atoms were needed for the final set; canonical paraphrases are marked `normalized_from_source`.
- Appraisal judgments are not encoded as reported literature atoms.
- Every atom uses the same publication UUID and source-document hash; each atom has its own UUID and page/section provenance.
