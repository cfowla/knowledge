# ATOM + SEA processing report: archinte_154_9_008.pdf

## Source metadata

- **Title:** Physician-Guided Treatment Compared With a Heparin Protocol for Deep Vein Thrombosis
- **Authors:** C. Gregory Elliott; Scott J. Hiltunen; Mary Suchyta; Russell D. Hull; Gary E. Raskob; Graham F. Pineo; Robert L. Jensen; Sandra Yeates; Natalie Kitterman
- **Journal:** Archives of Internal Medicine
- **Citation:** 1994;154:999-1004 (May 9, 1994)
- **Source file:** `archinte_154_9_008.pdf`
- **SHA-256:** `c1efb8c36c176b01d30698dfb2364defdf0cf8c0cd379bb10e24ac7aa6e29a61`
- **Study design:** Prospective concurrent-cohort comparison; protocol-directed IV unfractionated heparin (n=20) versus nonprotocol physician management (n=48); nonrandomized.
- **Publication ID:** `b792bd01-2a52-5dee-89d9-db7e4460e175`
- **DOI:** Not identified in the source PDF; not externally inferred.

## ATOM validation

- **Atoms extracted:** 68
- **Structurally validated atoms:** 68
- **JSON Schema validation errors:** 0
- **Structural errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0
- **Review status:** `needs_review` (machine-extracted; not human-verified)

### Atom counts by kind
- `adverse_event`: 3
- `author_conclusion`: 1
- `comparator_description`: 1
- `eligibility_criterion`: 3
- `intervention_description`: 10
- `limitation`: 4
- `method`: 4
- `outcome_definition`: 3
- `population_description`: 3
- `qualitative_result`: 7
- `quantitative_result`: 22
- `study_objective`: 1
- `subgroup_result`: 6

### Assertion origins

- `directly_reported`: 53
- `extractor_inference`: 1
- `normalized_from_source`: 14


## Source coverage / SEA manifest

- **Sections mapped:** Abstract; introduction/background; Patients and Methods (Study Population, Heparin Protocol, Data Collection, Statistical Methods); Results (Patient Population, Heparin Doses, APTT Response, Physician Response to Subtherapeutic APTT, Clinically Overt Bleeding, Recurrent Venous Thrombosis or Pulmonary Embolism, Deaths); Comment; references.
- **Main-text tables:** 4/4 reconciled.
- **Main-text figures:** 1/1 reconciled.
- **Algorithms/workflows:** Table 1 dose-titration protocol reconciled as structured content.
- **Appendices/supplements:** None present in the six-page PDF.
- **Reference section:** Read for context but not atomized as primary evidence.
- **Visual strategy:** All tables and the Kaplan-Meier figure were inspected in rendered page images and represented as structured HTML because the load-bearing values/rules were recoverable without embedding screenshots.

## Extraction limitations and appraisal-relevant source issues

- The comparison was nonrandomized and used concurrent cohorts assembled through different pathways: the protocol group came from the UFH arm of a concurrent LMWH trial, whereas the nonprotocol group consisted of patients excluded from that trial for specified reasons.
- The authors explicitly acknowledged possible patient-selection bias and transfer/contamination of protocol methods into nonprotocol care.
- Warfarin timing differed markedly: all protocol patients started warfarin between 24 and 48 hours, versus 9/48 nonprotocol patients within 48 hours. This is relevant to later clinical outcomes even though the primary early APTT endpoint precedes much of that difference.
- The study was small (20 vs 48 patients) and underpowered for major bleeding and recurrent VTE; the authors explicitly warned about type II error for bleeding.
- The primary endpoint was a surrogate, institution-specific therapeutic APTT threshold (>55 s; >1.5× upper limit of normal), not a patient-centered outcome.
- Table 4 reports one-tailed P values. The Kaplan-Meier/Cox F test showed a significant time-to-therapeutic difference (P=.025), while the simple mean time-to-first-therapeutic-APTT comparison in Table 4 was P=.08; these are different analyses rather than a direct numerical conflict.
- The protocol mandated four APTTs in the first 24 hours; the authors noted this intensity may be impractical or unnecessary for many patients.
- No conflict-of-interest, funding, or data-availability statement was identified in the PDF text.
- The paper is historical evidence about protocolization of UFH management and should not be treated as a current dosing standard without contemporary validation.

## SEA QA

- Coverage manifest built before appraisal: **PASS**
- All 4 tables reconciled: **PASS**
- Main figure reconciled: **PASS**
- Claims separated from appraisal: **PASS**
- Final scoring performed after extraction: **PASS**
- HTML self-contained, no external scripts/fonts/images: **PASS**
- Internal chat/file citation syntax absent from HTML: **PASS**
- Source PDF remained available locally through ATOM and SEA execution: **PASS**
