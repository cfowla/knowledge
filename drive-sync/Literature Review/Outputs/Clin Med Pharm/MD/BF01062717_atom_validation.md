# BF01062717 ATOM Extraction and Validation Report

## Source metadata

- **Title:** Improved Anticoagulation with a Weight-Adjusted Heparin Nomogram in Patients with Acute Coronary Syndromes: A Randomized Trial
- **Authors:** Walid M. Hassan; Greg C. Flaker; Cindy Feutz; Gregory F. Petroski; Dan Smith
- **Journal:** Journal of Thrombosis and Thrombolysis
- **Citation:** 1995;2:245-249
- **DOI:** 10.1007/BF01062717
- **Design:** Prospective randomized, single-center, two-nomogram comparison
- **Primary source file:** BF01062717.pdf
- **SHA-256:** `0ad2553ed4c416c9d3754baf70d71e3c125f748f60a0205f3f049aa28475db47`
- **Publication ID:** `3f8ff608-58b6-5ad1-abf9-374c21b768d4`
- **Extraction run:** `BF01062717-full-v1`

## Atom counts

- **Total atoms:** 56
- `adverse_event`: 2
- `author_conclusion`: 6
- `comparator_description`: 7
- `eligibility_criterion`: 1
- `intervention_description`: 7
- `method`: 9
- `outcome_definition`: 4
- `population_description`: 2
- `qualitative_result`: 1
- `quantitative_result`: 16
- `study_objective`: 1

## Validation status

- **Pydantic structural validation:** PASS (0 errors)
- **JSON Schema validation:** PASS (0 errors)
- **Sufficiency validation:** PASS (0 errors; 0 validator warnings)

## Source reconciliation warnings

- The Abstract reports 18-hour subtherapeutic APTT as 11% versus 26%, whereas the Results narrative reports 23% versus 48%; both source assertions were preserved rather than reconciled.
- Table 2 contains internally inconsistent numerator/denominator/percentage combinations, including 3/28 labeled 14%, 6/26 labeled 33%, and 4/23 labeled 61%. These values were not silently corrected.
- The Results narrative and Table 2 report different p values for some timepoints because the narrative discusses subtherapeutic proportions while Table 2 appears to test the three-category APTT distribution; the source does not explicitly explain every difference.
- The printed control-multiple notation for the weight-based 46-60-second Table 1 row is ambiguous; the atom preserves that ambiguity instead of normalizing to an assumed range.
- The source prints unusual safety-definition units (platelet count in U/L and hemoglobin change in g/L) and a minor-event hematocrit change expressed in g; these were preserved as printed and should not be treated as normalized clinical units.

## Extraction limitations

- Single-center sample of 64 patients with only 48 hours of follow-up.
- Primary efficacy evidence is laboratory anticoagulation (APTT), a surrogate rather than ischemic or mortality outcomes.
- No sample-size/power calculation is reported.
- Envelope randomization is described, but sequence generation, envelope opacity/sealing, and allocation-concealment safeguards are not reported.
- Treatment delivery was unblinded; complication review was blinded after study completion.
- Available APTT denominators vary by timepoint, but reasons for missing/terminated observations are not reported.
- No major bleeding events occurred, leaving the study underinformative for comparative bleeding safety.
- The trial predates contemporary ACS antithrombotic and invasive-management practice; its tested dose/target should not be transplanted directly into current protocols.

## Output

- Validated atom JSON: `BF01062717_atoms.json`
- All atoms are marked `needs_review`; no human verification was asserted.
