# @ATOM extraction and validation report — jcm-11-01338.pdf

## Source metadata

- **Title:** Monitoring of Unfractionated Heparin Therapy in the Intensive Care Unit Using a Point-of-Care aPTT: A Comparative, Longitudinal Observational Study with Laboratory-Based aPTT and Anti-Xa Activity Measurement
- **Authors:** Benjamin Lardinois; Michaël Hardy; Isabelle Michaux; Geoffrey Horlait; Thomas Rotens; Hugues Jacqmin; Sarah Lessire; Pierre Bulpa; Alain Dive; François Mullier
- **Journal:** Journal of Clinical Medicine
- **Publication:** 2022;11(5):1338
- **DOI:** 10.3390/jcm11051338
- **Source file:** jcm-11-01338.pdf
- **Source SHA-256:** `f5b57edc048f17db4c258b9fcf8c925f167e00ca23bf752d771c2949ed28b452`
- **Publication UUID:** `b8adf46f-1deb-54b8-a34f-a6d6d2143696`
- **Extraction run:** `jcm-11-01338-fulltext-v1`
- **Review status:** `needs_review`

## Atom counts

- **Total validated atoms:** 87
- `adverse_event`: 3
- `author_conclusion`: 5
- `conflict_of_interest`: 1
- `data_availability`: 1
- `eligibility_criterion`: 5
- `funding_disclosure`: 1
- `intervention_description`: 6
- `limitation`: 7
- `method`: 15
- `other`: 1
- `population_description`: 4
- `qualitative_result`: 4
- `quantitative_result`: 31
- `study_objective`: 1
- `subgroup_result`: 2


## Validation

- **Pydantic structural errors:** 0
- **JSON-schema serialization errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0

All emitted atoms share one `publication_id`, have unique `atom_id` values, retain page/table/figure anchors, and include the source document hash in extraction provenance.

## Extraction limitations

- The retrieved PDF contains the main article and cites supplementary Tables S1-S3, but the supplementary files are not embedded in the retrieved PDF. The main-text statements that depend on those supplements are retained only at the level explicitly reported in the main article.
- Figure 3 contains 35 patient-level longitudinal panels; the atom set preserves source-reported aggregate interpretations and clinical-event counts rather than attempting unsupported numeric digitization of each plotted trace.
- Table 1 is represented through separate regimen/nomogram atoms for the main initiation strata plus a higher-level adjustment-method atom. The JSON does not duplicate every threshold cell as a separate atom when the information is already traceable to Table 1.
- Clinical bleedings and deaths are recorded as study-period outcomes without inferring that they were caused by UFH or by a monitoring method.
- No current-practice verification was added to the atoms; these objects represent what this 2022 source reports.


# @SEA appraisal and QA report — jcm-11-01338.pdf

## Coverage manifest

- **Source type:** Peer-reviewed clinical journal article; single-center prospective longitudinal observational comparative study
- **Main-text figures reconciled:** 6/6
- **Main-text tables reconciled:** 3/3
- **Workflows reconciled:** 2/2 (Table 1 UFH nomogram; Table 2 agreement classification)
- **Embedded crop:** Figure 3 patient-level longitudinal traces
- **Structured visual blocks:** Tables 1–3 and Figures 1, 2, 4, 5, 6
- **Supplementary limitation:** Tables S1–S3 are cited by the paper but are not embedded in the retrieved PDF; they were not reconstructed.
- **References:** treated as provenance infrastructure rather than evidence-extraction targets.

## Final appraisal

- **Verdict:** Read first for the heparin deep-dive; do not use as stand-alone practice guidance.
- **Relevance:** 9/10
- **Novelty:** 6/10
- **Method strength:** 6/10
- **Evidence strength:** 6/10
- **External validity:** 4/10
- **Implementation value:** 8/10
- **Appraisal confidence:** high for main-text analytical/workflow results; moderate for detailed confounder model coefficients because the cited supplementary tables were unavailable in the retrieved PDF.

## Output artifacts

- `jcm-11-01338-atoms.json` — validated LiteratureAtom collection
- `jcm-11-01338-sea.html` — self-contained SEA artifact
- `jcm-11-01338-processing-report.md` — combined extraction/validation/SEA report

## SEA extraction limitations

- The study does not compare clinical outcomes between alternative monitoring strategies because patient management was based on laboratory aPTT.
- Bleeding, mortality, and thrombosis are represented as observed cohort outcomes; no causal attribution to UFH or a monitoring assay is made.
- Figure 3 is embedded to preserve its multi-panel longitudinal layout; individual traces were not digitized into unsupported numerical estimates.
- This run did not add current-practice verification; practice translation is explicitly bounded to what the 2022 source supports.

## Final mechanical QA

- **ATOM revalidation:** PASS — 87 atoms; 0 Pydantic structural errors; 0 JSON-schema errors; 0 sufficiency errors; 0 sufficiency warnings.
- **Raw-source integrity:** PASS — SHA-256 remained `f5b57edc048f17db4c258b9fcf8c925f167e00ca23bf752d771c2949ed28b452` after ATOM and before SEA.
- **SEA semantic coverage:** PASS — 6/6 main-text figures and 3/3 main-text tables reconciled; 2/2 workflows represented.
- **SEA HTML checks:** PASS — title/source match, 8/8 TOC anchors resolve, no external scripts/styles/images, no placeholders/planning language/internal citation syntax.
