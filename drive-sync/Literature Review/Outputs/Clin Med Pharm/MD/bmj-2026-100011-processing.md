# bmj-2026-100011 processing and QA note

## Source

- File: `bmj-2026-100011.full.pdf`
- Exact title: *Tirzepatide and the risk of atherosclerotic cardiovascular events: population based cohort study*
- Source type: population-based observational cohort study using a trial-benchmarked active-comparator/new-user design
- DOI: 10.1136/bmj-2026-100011
- Publication: BMJ 2026;394:e100011; first published 2026-08-05; accepted 2026-06-17
- Raw PDF retained in the source folder; it was not moved or deleted.
- SHA-256: `103cea92c5b232ff0cf6cbb04a557f0232a3bf5ea5c6e6ddf742da69f1d42820`

## Pre-processing duplicate check

No completed LiteratureAtom or SEA artifact matching `bmj-2026-100011` or an unmistakable title-equivalent was found in the target Clin Med Pharm HTML/JSON/MD output folders. Processing therefore proceeded as a new run.

## @ATOM status

- Atom count: **66**
- Structural validation: **PASS** (0 errors)
- JSON Schema validation: **PASS** (0 errors)
- Sufficiency validation: **PASS** (0 errors; 0 warnings)
- Review status on atoms: `needs_review` (validated extraction, not human-verified)
- Assertion origins: {"normalized_from_source": 66}
- Atom counts by kind: {"adverse_event": 4, "author_conclusion": 3, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 5, "exposure_description": 1, "funding_disclosure": 1, "limitation": 7, "method": 14, "other": 1, "outcome_definition": 5, "population_description": 3, "qualitative_result": 4, "quantitative_result": 14, "study_objective": 1}

## @SEA coverage manifest

- Sections: abstract; introduction; methods (data sources, study design/conduct, transparency, eligibility, study drug/follow-up, outcomes, covariates, statistical analysis, sensitivity/subgroups, patient/public involvement); results (population, MACE, components, safety, negative controls/sensitivity/subgroups); discussion (comparison with other studies, policy implications, limitations, conclusions); disclosures/data sharing.
- Figures: Figure 1 and Figure 2 both reconciled and embedded as self-contained crops with structured interpretation.
- Tables: Table 1 reconciled as a structured baseline-balance summary; Table 2 reconstructed with all main endpoint rows.
- Supplementary material: referenced by the article but **not supplied for this task**; not retrieved or substituted. This limits verification of detailed subgroup, negative-control, covariate-code, and sensitivity tables.
- References: bibliography not atomized or condensed.

## Source inconsistencies preserved

1. Figure 2 reports the myocardial-infarction HR 0.67 with 95% CI **0.52-0.86**, whereas Table 2 and the prose report **0.52-0.87**. LiteratureAtom extraction uses the Table 2/prose value and flags the figure discrepancy in the SEA artifact.
2. The Results narrative says “Of these 7444 patients” while Table 1 and surrounding text use **7442 per group**; the reported percentages align with 7442.
3. Infection-related mortality has an HR CI excluding 1.0 but an absolute risk-difference CI that includes 0; the paper still reports NNT 200. This was preserved without model reconciliation.

## @SEA QA

- Status: **PASS**
- HTML bytes: 394070
- Parsed title: Tirzepatide and the risk of atherosclerotic cardiovascular events — Summary, Evaluation, and Appraisal
- TOC anchors: 8; missing: []
- Embedded figure blocks: 2
- HTML table blocks: 3
- Embedded images are self-contained data URIs: True
- Placeholder/internal-citation marker scan: none

## Extraction limitations

- Only the supplied primary PDF was used. No supplementary file or correction was supplied.
- Administrative claims cannot directly measure all socioeconomic, behavioral, adherence, dose-escalation, or clinical-severity factors; this is a source limitation, not a missing extraction field.
- The infection-related mechanistic interpretation is an author hypothesis and was not converted into a reported causal mechanism.
- Appraisal judgments in the SEA are clearly separated from source-reported results and are not encoded as reported LiteratureAtoms.
