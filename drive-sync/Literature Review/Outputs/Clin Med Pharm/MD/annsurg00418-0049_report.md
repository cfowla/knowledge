# Literature Processing Report — annsurg00418-0049.pdf

## Source metadata

- **Title:** Assessment of Anticoagulant Treatment of Venous Thromboembolism
- **Authors:** William W. Coon, M.D.; Park W. Willis, III, M.D.; Michael J. Symons, Ph.D.
- **Journal:** Annals of Surgery, October 1969; 170(4):559-567
- **Source type:** Historical clinical treatment series with an embedded prospective randomized anticoagulation-intensity comparison
- **Raw PDF:** 9 pages; 1,291,270 bytes
- **SHA-256:** `095257ad8de1779ddd75f31d601589780a7a93860605733a34aea9b64aa1d11c`
- **Drive file ID:** `1qEHAFOyikuydwMG185Xh7P3FISRbq4XA`

## @ATOM result

- **Validated atoms:** 44
- **Structural validation:** PASS — 0 errors
- **Sufficiency validation:** PASS — 0 errors; 0 warnings

### Atom counts by kind

- `adverse_event`: 2
- `author_conclusion`: 5
- `eligibility_criterion`: 1
- `funding_disclosure`: 1
- `intervention_description`: 2
- `limitation`: 3
- `method`: 5
- `population_description`: 1
- `qualitative_result`: 2
- `quantitative_result`: 21
- `study_objective`: 1

### Assertion origin counts

- `directly_reported`: 15
- `normalized_from_source`: 29

### Extraction limitations

- This is a historical single-center institutional series with an embedded randomized intensity substudy; the atom set preserves source claims but does not update them to contemporary practice.
- The article reports treatment courses/episodes as well as patients; denominators therefore vary by analysis and should not be treated as a single patient-level cohort.
- The source acknowledges differential follow-up and diagnostic misclassification of pulmonary embolism.
- The outpatient-duration comparison in Table 5 was not randomized; the source-reported treatment-selection mechanism is preserved in the atoms, while confounding appraisal is kept separate in the SEA artifact.
- The article does not provide modern effect measures or confidence intervals for most comparisons; none were invented.

## @SEA coverage manifest

- **Sections mapped:** Background/introduction; Methods of Analysis; Results; Discussion; Summary; Acknowledgment; References; appended post-presentation Discussion
- **Figures:** 0
- **Tables:** 6; all reconciled as structured HTML tables
- **Algorithms/workflows:** 0
- **Appendices/supplements:** none
- **Bibliography:** not condensed into evidence findings
- **Post-presentation discussion:** summarized separately as commentary, not study evidence

## @SEA QA

- **HTML QA:** PASS
- **HTML bytes:** 27340
- **TOC anchor failures:** 0
- **Structured tables:** 6/6
- **Forbidden placeholders/internal citation markers found:** 0

## Key appraisal boundary

The paper is historically important for VTE anticoagulation, recurrence timing, and bleeding, but its randomized “intensity” comparison used Quick prothrombin activity targets rather than a heparin-specific assay. It should not be treated as direct evidence for a heparin therapeutic range, aPTT target, anti-Xa target, or weight-based heparin dosing algorithm.

## Output files

- `annsurg00418-0049_atoms.json` — validated LiteratureAtom array
- `annsurg00418-0049_sea.html` — self-contained SEA appraisal
- `annsurg00418-0049_report.md` — this validation, coverage, and QA report
