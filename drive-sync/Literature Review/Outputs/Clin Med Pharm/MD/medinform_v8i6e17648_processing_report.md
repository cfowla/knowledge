# medinform_v8i6e17648 — ATOM + SEA processing report

## Source metadata

- File: `medinform_v8i6e17648.pdf`
- Title: *Toward Optimal Heparin Dosing by Comparing Multiple Machine Learning Methods: Retrospective Study*
- DOI: `10.2196/17648`
- Source type: retrospective machine-learning modeling study
- Raw PDF size: 673,316 bytes
- Pages: 14
- SHA-256: `a600424a6c3a18dad85e770100bc08101dd2a4e9c4a959ef1dcd1db8ade2dde3`
- Publication ID: `113cd9e4-9991-51f3-8c25-ac9d7bea4337`
- Substantive pages: 1–12
- References: pages 13–14

## @ATOM result

- Total atoms: **77**
- Structural/Pydantic errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

### Counts by atom kind

- `author_conclusion`: 3
- `conflict_of_interest`: 1
- `data_availability`: 1
- `eligibility_criterion`: 1
- `funding_disclosure`: 1
- `limitation`: 4
- `method`: 9
- `other`: 4
- `outcome_definition`: 3
- `population_description`: 2
- `quantitative_result`: 47
- `study_objective`: 1

### Counts by assertion origin

- `calculated_from_reported_data`: 1
- `directly_reported`: 3
- `extractor_inference`: 3
- `normalized_from_source`: 70

### Extraction limitations / review-needed items

- The PDF contains an internal sample-size conflict: Results reports data set 1 as n=1,758, while Table 1 reports N=1,756; subgroup counts in Table 1 sum to 1,758.
- The abstract/Results narrative labels several shallow-neural-network class-specific precision values as F1 scores; Tables 3–5 report different F1 values.
- The Results narrative includes multiple F1 values for Table 2 models that do not match the table itself.
- Table 4 contains eICU normal-therapeutic rows where reported F1 values are not arithmetically consistent with the same row's reported precision and recall.
- These conflicts were preserved as `other` atoms with `extractor_inference` or `calculated_from_reported_data` origin rather than silently corrected.
- The extraction prioritizes independently reviewable methods, cohort definitions, key descriptive results, model-performance results, author conclusions, limitations, funding, and conflicts. It does not atomize every bibliographic citation or every descriptive cell in Table 1.

## @SEA coverage manifest

- Figure 1: covered as a structured block.
- Table 1: covered as a structured block with key values and pattern appraisal.
- Tables 2–5: covered with full main performance rows.
- Methods/results/discussion/conclusion: covered section by section.
- Multimedia Appendices 1–4: listed in the PDF but stored as separate DOCX files; their contents were not embedded in the retrieved PDF and were not retrieved for this execution.
- Reference list: not condensed; used only as provenance context.

## SEA appraisal summary

- Verdict: **Skim deeply**
- Relevance: **9/10**
- Novelty: **6/10**
- Method strength: **4/10**
- Evidence strength: **4/10**
- External validity: **4/10**
- Implementation value: **3/10**
- Clinical use now: **No** — the paper predicts an aPTT class and does not prospectively validate a dose-selection policy or clinical safety/efficacy outcomes.

## QA

- HTML exists and is nontrivial: **yes** (32199 bytes)
- HTML title parsed: **yes**
- Missing TOC anchors: **0**
- Internal chat/file citation markers: **none**
- Main-text figures reconciled: **1/1**
- Main-text tables reconciled: **5/5**
- Raw PDF retained locally through both ATOM and SEA execution: **yes**
