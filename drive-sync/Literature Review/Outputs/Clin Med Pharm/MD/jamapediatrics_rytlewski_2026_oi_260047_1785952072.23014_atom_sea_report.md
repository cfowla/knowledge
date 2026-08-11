# ATOM + SEA Processing Report

## Activated macros

- `@ATOM`
- `@SEA`

## Source

- **Title:** Effectiveness of Oseltamivir in Hospitalized Children With Laboratory-Confirmed Influenza, 2014-2023
- **Journal:** JAMA Pediatrics
- **Published:** 2026-08-10
- **DOI:** 10.1001/jamapediatrics.2026.3376
- **Drive file:** `jamapediatrics_rytlewski_2026_oi_260047_1785952072.23014.pdf`
- **Drive file ID:** `1JLB1xYlgMn1SZiQdiOf-4ALTHu464Vrs`
- **Folder:** `TBR/Lit Cluster: 8-10 Clinical Pubs`
- **Raw PDF:** 402,910 bytes, 10 pages
- **SHA-256:** `67ed87bf843e77fffc25d878c17c028d9fdb788139d5782c0c82787b3de92f3c`

## ATOM governing sources

Precedence applied:

1. `literature.py` — domain model and structural validation
2. `literature_atoms.py` — atom-kind sufficiency validation
3. `literature_atom.schema.json` — serialization contract
4. `README(2).md` — workflow intent
5. `example_atom.json` — illustrative only

## ATOM extraction summary

- **Atoms:** 68
- **Pydantic structural validation:** PASS
- **JSON Schema serialization validation:** PASS
- **Sufficiency validation:** PASS
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0

### Atom counts by kind

- `author_conclusion`: 1
- `comparator_description`: 1
- `conflict_of_interest`: 1
- `data_availability`: 1
- `eligibility_criterion`: 2
- `exposure_description`: 3
- `funding_disclosure`: 2
- `limitation`: 7
- `method`: 8
- `outcome_definition`: 2
- `population_description`: 6
- `qualitative_result`: 7
- `quantitative_result`: 16
- `study_objective`: 1
- `subgroup_result`: 10

### Assertion origin

- `directly_reported`: 41
- `normalized_from_source`: 27
- `calculated_from_reported_data`: 0
- `extractor_inference`: 0

No appraisal statements were converted into reported-data atoms.

## SEA governing source

`summary-evaluation-appraisal-protocol-v4-compact.md` was treated as authoritative. The v3 HTML was historical/reference only and did not override v4.

## Source coverage manifest

- **Sections:** Abstract/Key Points, Introduction, Methods: Data Source and Patient Population, Methods: Exposures, Outcomes and Variables, Methods: Statistical Analyses, Methods: Subgroup and Sensitivity Analyses, Results, Primary Outcome of ICU Admission, Secondary Outcome of Hospital LOS, Discussion, Limitations, Conclusions, Article Information/Disclosures/References
- **Figures:** Figure 1: cohort flow diagram, Figure 2: adjusted hazard ratios for ICU admission, Figure 3: adjusted hazard ratios for hospital discharge
- **Tables:** Table 1: demographic and clinical characteristics, Table 2: time-varying treatment-category Cox models
- **Workflow:** Figure 1 cohort inclusion/exclusion flow
- **Main-text visual strategy:** structured reconstruction after direct visual inspection
- **Embedded screenshots in final HTML:** none; main visuals were reconstructable faithfully as structured blocks
- **Supplement status:** Supplement 1 and Supplement 2 are referenced but not embedded in the retrieved PDF
- **Bibliography:** inspected as source context but not atomized

## Key source-derived findings

- ICU analysis: **n=6,044**, oseltamivir before ICU **n=4,240 (70.2%)**.
- LOS analysis: **n=7,103**, oseltamivir **n=5,746 (80.9%)**.
- ICU admission: **aHR 0.69 (95% CI 0.60-0.80)**.
- Hospital discharge: **aHR 1.13 (95% CI 1.06-1.21)**.
- Model-estimated LOS reduction: **9.4 hours (95% bootstrap CI 4.3-14.6)**.
- Early vs no treatment for ICU: **aHR 0.74 (0.63-0.86)**.
- Late vs no treatment for ICU: **aHR 0.55 (0.41-0.73)**.
- Early vs no treatment for LOS: **aHR 1.15 (1.08-1.23)**.
- Late vs no treatment for LOS: **aHR 1.08 (0.98-1.20)**, not statistically significant.

## Appraisal summary

- **Verdict:** Read soon
- **Relevance:** 8.5/10
- **Novelty:** 7.5/10
- **Method strength:** 7.0/10
- **Evidence strength:** 6.5/10
- **External validity:** 7.0/10
- **Implementation value:** 7.5/10

The most important strength is the use of symptom-onset anchoring and time-dependent oseltamivir exposure to reduce immortal time bias. The most important limitation is residual confounding from nonrandom treatment selection; the treated group differed materially in baseline timing, comorbidity, ICU admission, and mechanical ventilation.

## Source/QA issues and limitations

1. The retrieved PDF does not contain Supplement 1 or Supplement 2. Values from supplements were included only when repeated verbatim in the main article; supplemental tables/figures were not independently inspected.
2. The abstract contains internally inconsistent sex counts/percentages relative to the stated ICU cohort and Table 1. Baseline sex extraction therefore uses Table 1 (3,982 male; 3,121 female in n=7,103).
3. The paper is observational; adjusted hazard ratios should not be converted into causal risk reductions or NNTs.
4. The timing analysis must not be interpreted as showing that delayed oseltamivir is preferable to early treatment.
5. No external guideline verification was performed. Statements about CDC/AAP/IDSA recommendations in the SEA artifact are explicitly identified as source-stated context.
6. ATOM records are marked `needs_review`: machine-extracted and validated, but not independently human-verified.

## Generated artifacts

- JSON: `jamapediatrics_rytlewski_2026_oi_260047_1785952072.23014_atoms.json`
- HTML: `jamapediatrics_rytlewski_2026_oi_260047_1785952072.23014_sea.html`
- Markdown: `jamapediatrics_rytlewski_2026_oi_260047_1785952072.23014_atom_sea_report.md`
