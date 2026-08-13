# Processing Report — heartjnl-2026-328038

## Activated workflow

- @ATOM
- @SEA
- Primary source only; no supplementary source material was supplied.

## Source coverage manifest

- **source_id:** heartjnl-2026-328038
- **exact_title:** Mineralocorticoid receptor antagonists in patients with transthyretin amyloid cardiomyopathy receiving disease-modifying therapy
- **source_type:** Original research; retrospective cohort study
- **date/version:** First published 7 August 2026
- **stable_identifier:** DOI 10.1136/heartjnl-2026-328038
- **evaluated_file:** heartjnl-2026-328038.full.pdf
- **page_count:** 7
- **sections/headings:** Abstract; Introduction; Methods; Results; Patient characteristics; Study endpoints; Sensitivity analysis; Discussion; Limitations; Conclusion; declarations/references
- **main-text tables:** Table 1 (baseline characteristics); Table 2 (clinical endpoints)
- **main-text figures:** Figure 1 (unmatched Kaplan-Meier); Figure 2 (matched Kaplan-Meier); Figure 3 (ATTR subtype forest plot)
- **algorithms/workflows:** Cohort construction and propensity-score matching workflow described in Methods; graphical abstract is supplemental and unavailable
- **appendices/supplements referenced but not supplied:** eMethods 1-3; graphical abstract; supplemental eFigure 1
- **visual strategy:** all 2 main-text tables and 3 main-text figures reconciled as structured blocks in SEA HTML; no screenshot embedding required because the load-bearing values could be reconstructed from the primary PDF
- **coverage decision:** full primary article covered; pure bibliography not condensed; unavailable supplement explicitly omitted

## @ATOM validation

- **Atom count:** 59
- **Structural validation:** pass (0 errors)
- **JSON-schema serialization validation:** pass (0 errors)
- **Sufficiency validation:** pass (0 errors; 0 warnings)
- **Review status:** atoms are marked `extracted`, not human-verified

### Counts by atom kind
- adverse_event: 2
- author_conclusion: 2
- comparator_description: 1
- conflict_of_interest: 1
- data_availability: 1
- eligibility_criterion: 2
- exposure_description: 1
- funding_disclosure: 1
- limitation: 9
- method: 6
- outcome_definition: 4
- population_description: 4
- qualitative_result: 2
- quantitative_result: 13
- study_objective: 1
- subgroup_result: 9

## Source reconciliation findings

- The narrative Results text on page 3 reports several pre-match baseline percentages that do not match the corresponding values in Table 1; atoms therefore encode the overall qualitative imbalance rather than normalising those conflicting percentages.
- For the tafamidis-only sensitivity composite, narrative Results reports HR 1.04 (95% CI 0.83-1.32), whereas Table 2 reports HR 1.05 (95% CI 0.83-1.32); the quantitative atom uses the table value and preserves this discrepancy in QA.
- For tafamidis-only all-cause mortality, narrative Results reports HR 1.05 (95% CI 0.74-1.50), whereas Table 2 reports HR 1.06 (95% CI 0.74-1.50); the quantitative atom uses the table value and preserves this discrepancy in QA.
- The article references online supplemental eMethods, a graphical abstract, and supplemental eFigure 1. These materials were not supplied for this task and were not substituted or inferred.
- Table 1 reports a post-match troponin-I SMD of 0.117, which exceeds the methods-defined balance threshold of <0.10, despite the narrative statement that baseline characteristics were well balanced.
- The primary-cohort portion of Table 2 appears to have the final two column headings reversed: hazard-ratio values are printed under the heading "P value (log-rank)" and p values under "HR (95% CI)"; the narrative Results and the sensitivity-analysis subtable clarify the intended interpretation.
- The Results section reports ATTRwt-CM n=2116, ATTRv-CM n=939 and unknown n=2847 within a 4598-patient cohort; these counts sum above the cohort total, suggesting overlap or a reporting/definition issue that cannot be resolved without the referenced supplemental query details.

## Extraction limitations

- Primary PDF only; no supplemental source material was provided.
- General ATTR-CM cohort query details referenced in supplemental eMethods 2/3 cannot be fully audited from the primary PDF alone.
- Table 1 is reconciled for balance and key baseline patterns but not atomized row-by-row because several narrative/table baseline values conflict and those rows are not independent study endpoints.

## SEA coverage and QA

- Source classified as observational clinical research and appraised with the clinical-practice module.
- Coverage manifest completed before final narrative/HTML generation.
- Table 1, Table 2, Figure 1, Figure 2 and Figure 3 are each represented as structured evidence blocks.
- Referenced supplemental materials are explicitly marked unavailable rather than reconstructed.
- Claims and model appraisal are separated in the HTML.
- Six appraisal dimensions scored only after source/visual extraction and reconciliation.
- HTML title/source ID verified.
- All table-of-contents anchors resolve.
- Required metadata, synthesis, PICO, section condensation, visuals, reconciliation, appraisal, takeaways and provenance sections are present.
- No TODO/placeholder/planning language detected.
- No internal chat/file citation syntax detected.
- Mechanical/semantic QA status: **PASS**.

## Broad claim-to-atom crosswalk

- Study question/design/eligibility/exposure definitions → objective, method, eligibility, exposure and comparator atoms.
- Primary/secondary/safety endpoint definitions → outcome-definition atoms.
- Cohort flow/baseline population → population-description and qualitative-result atoms.
- Unmatched and matched effectiveness/safety results → quantitative-result and adverse-event atoms.
- Tafamidis-only sensitivity → quantitative-result/adverse-event atoms tagged `sensitivity analysis`.
- ATTRwt/ATTRv analyses → subgroup-result atoms plus one qualitative result for sparse ATTRv mortality events.
- Interpretation and prospective-study need → author-conclusion atoms.
- Bias, exposure classification, phenotype/stage gaps and generalisability → limitation atoms.
- Funding, conflicts and data access → disclosure/data-availability atoms.

## Output files

- `heartjnl-2026-328038-atoms.json`
- `heartjnl-2026-328038-atom-validation.json`
- `heartjnl-2026-328038-sea.html`
- `heartjnl-2026-328038-processing-report.md`
