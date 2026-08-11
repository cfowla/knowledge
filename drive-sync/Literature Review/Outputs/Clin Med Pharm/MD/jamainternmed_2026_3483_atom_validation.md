# ATOM Extraction and Validation Report

## Source metadata

- **Title:** Intensification and Deintensification of Diabetes Medications Among Older Adults With Type 2 Diabetes
- **Authors:** Phuc Le, PhD, MPH, Ning Guo, MS, Anita D. Misra-Hebert, MD, MPH, Nicholas J. Casacchia, PharmD, MS, Yihua Yue, PhD, MPH, Hamlet Gasoyan, PhD, Glen B. Taksler, PhD, Michael B. Rothberg, MD, MPH
- **Journal:** JAMA Internal Medicine
- **Source type:** Research Letter; retrospective EHR cohort study
- **Published online:** August 10, 2026
- **DOI:** 10.1001/jamainternmed.2026.3483
- **Source file:** jamainternal_le_2026_ld_260017_1785358236.39199.pdf
- **SHA-256:** `9ad0aa0b0a15297f2eaf7376d561dc56db3725b4130dc2cdd273b8db389a5f93`
- **Publication ID:** `c8584430-150e-5738-ba12-dad6913ad731`
- **Extraction run:** `jamainternmed-2026-3483-full-v1`

## Extraction scope

The retrieved PDF was read as a 4-page primary source. It contains the main research letter, one patient-characteristics table, one multi-panel figure, author/disclosure material, and references. The article links to eMethods/eTables in Supplement 1 and a data-sharing statement in Supplement 2, but those supplements are not embedded in the retrieved PDF and were not reconstructed.

## Atom counts

- **Total validated atoms:** 63
- `author_conclusion`: 5
- `conflict_of_interest`: 4
- `data_availability`: 1
- `eligibility_criterion`: 4
- `exposure_description`: 2
- `limitation`: 6
- `method`: 8
- `outcome_definition`: 2
- `population_description`: 3
- `qualitative_result`: 3
- `quantitative_result`: 24
- `study_objective`: 1

## Validation status

- **Structural validation:** PASS
- **Structural errors:** 0
- **Sufficiency validation:** PASS
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0

## Extraction limitations

- Supplement 1 (eMethods/eTables) was referenced but not embedded in the retrieved PDF; detailed health-status coding logic beyond the main-text summary could not be atomized.
- Supplement 2 (data-sharing statement) was referenced but not embedded; only the main-text statement directing readers to Supplement 2 was extracted.
- Figure values not explicitly reported in the article text were not converted into precise numeric atoms by visual estimation.
- Medication-class table values were extracted as reported prevalence; the article notes that medication percentages can exceed 100% in aggregate because patients may use more than one medication.
- No external sources were used to fill missing study details.

## Governing validation

Each atom was validated against the `LiteratureAtom` Pydantic model in `literature.py` and then passed through `validate_literature_atom_sufficiency()` from `literature_atoms.py`. No appraisal judgments were inserted as reported evidence.
