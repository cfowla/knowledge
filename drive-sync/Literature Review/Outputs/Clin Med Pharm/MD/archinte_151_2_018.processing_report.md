# ATOM + SEA processing report: archinte_151_2_018.pdf

## Source metadata

- **Title:** A Standard Heparin Nomogram for the Management of Heparin Therapy
- **Authors:** Moirra K. Cruickshank; Mark N. Levine; Jack Hirsh; Robin Roberts; Margaret Siguenza
- **Journal:** Archives of Internal Medicine
- **Citation:** 1991;151(2):333-337
- **DOI:** 10.1001/archinte.1991.00400020085018
- **Source file:** `archinte_151_2_018.pdf`
- **SHA-256:** `f273ba143d116debc078a5f1ce272b95b8273c688386365dd96a64b14e291c52`
- **Study design:** Prospective consecutive nomogram cohort compared with historical controls; single-center, nonrandomized validation/application study.
- **Publication ID:** `61237785-c306-5226-823b-5ce3d8e48b4c`

## ATOM validation

- **Atoms extracted:** 58
- **Structurally validated atoms:** 58
- **Structural errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0
- **Review status:** `needs_review` (machine-extracted; not human-verified)

### Atom counts by kind

- `author_conclusion`: 1
- `comparator_description`: 1
- `eligibility_criterion`: 2
- `funding_disclosure`: 1
- `intervention_description`: 9
- `limitation`: 3
- `method`: 3
- `other`: 4
- `outcome_definition`: 2
- `population_description`: 2
- `qualitative_result`: 3
- `quantitative_result`: 26
- `study_objective`: 1

### Assertion origins

- `calculated_from_reported_data`: 3
- `directly_reported`: 42
- `extractor_inference`: 4
- `normalized_from_source`: 9

### Structural errors

None.

### Sufficiency errors

None.

### Sufficiency warnings

None.

## Source coverage / SEA manifest

- **Sections mapped:** Abstract; introduction/background; Patients and Methods; Results (Initial Stages of Development, Patient Population, Time-to-Event Analysis, Success-Rate Analysis); Comment; references.
- **Main-text tables:** 6/6 reconciled.
- **Main-text figures:** 1/1 reconciled.
- **Algorithms/workflows:** Final nomogram (Table 1) and initial nomogram (Table 2) reconciled as structured content.
- **Appendices/supplements:** None present in the PDF.
- **Reference section:** Read for source context but not atomized as primary evidence.
- **Visual strategy:** Tables and the Kaplan-Meier figure are represented as structured HTML summaries rather than embedded screenshots because the load-bearing values and rules can be reconstructed from the source.

## Extraction limitations and source-internal issues

- Historical controls were not randomized or contemporaneous.
- The study and historical-control groups used different APTT therapeutic ranges (60-85 s vs 55-75 s), which limits direct comparability of therapeutic-success metrics.
- Clinical outcomes (recurrent VTE and bleeding) were underpowered and were not validly compared.
- The nomogram was explicitly reagent-specific (Actin FS) and the authors cautioned against direct generalization to other APTT reagents without local calibration.
- Table 4 and adjacent prose disagree on group assignment for heparin duration and on the study-group mean number of APTTs (8.6 in the table vs 8.4 in prose).
- Table 5 confidence intervals differ from the adjacent prose for all three reported APTT strata; the atom JSON preserves Table 5 values and separately flags the discrepancy.
- The Results section reports control therapeutic subsequent APTTs as 33.9%, while the Comment later states 34.2%.
- Initial APTT categories in historical controls account for 50 of 53 patients without an explanation for the remaining 3.
- No conflict-of-interest statement or data-availability statement was identified in the five-page source.

## SEA QA

- Coverage manifest built before appraisal: **PASS**
- All 6 tables reconciled: **PASS**
- Main figure reconciled: **PASS**
- Claims separated from appraisal: **PASS**
- Final scoring performed after extraction: **PASS**
- HTML self-contained, no external scripts/fonts/images: **PASS**
- Internal chat/file citation syntax absent from HTML: **PASS**
