# DAPA-CKD processing report

## Source package

- Main article: `NEJMoa2024816.pdf`
- Supplementary appendix: `nejmoa2024816_appendix.pdf`
- Related correspondence: `NEJMc2032809.pdf`
- Main publication: Heerspink HJL, Stefánsson BV, Correa-Rotter R, et al. *Dapagliflozin in Patients with Chronic Kidney Disease.* N Engl J Med. 2020;383:1436-1446. DOI `10.1056/NEJMoa2024816`.
- Correspondence DOI: `10.1056/NEJMc2032809`.
- Trial: `NCT03036150`.

## ATOM status

- Main DAPA-CKD LiteratureAtoms: **103**
- Main atom counts by kind: `{"adverse_event": 12, "author_conclusion": 2, "comparator_description": 1, "data_availability": 1, "eligibility_criterion": 22, "funding_disclosure": 1, "intervention_description": 1, "limitation": 3, "method": 15, "outcome_definition": 8, "population_description": 12, "quantitative_result": 14, "study_objective": 1, "subgroup_result": 10}`
- Main semantic extraction runs: `{"dapa-ckd-design-v1": 2, "dapa-ckd-disclosures-v1": 2, "dapa-ckd-efficacy-v1": 11, "dapa-ckd-egfr-v1": 3, "dapa-ckd-eligibility-v1": 22, "dapa-ckd-general-v1": 1, "dapa-ckd-interpretation-v1": 5, "dapa-ckd-methods-v1": 15, "dapa-ckd-outcomes-v1": 8, "dapa-ckd-population-v1": 12, "dapa-ckd-safety-v1": 12, "dapa-ckd-subgroups-v1": 10}`
- Correspondence LiteratureAtoms: **9**
- Correspondence atom counts by kind: `{"author_conclusion": 1, "conflict_of_interest": 1, "limitation": 1, "other": 6}`
- Pydantic structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Duplicate statement-anchor pairs: **0**
- Review status: model-extracted atoms remain `needs_review`; no human verification was fabricated.

## SEA status

- Main source type: randomized, double-blind, placebo-controlled, multicenter CKD outcomes trial.
- Main figures reconciled: **3/3**.
- Main tables reconciled: **2/2**.
- Supplement: Supplemental Methods §5.1–5.4, Figure S1, Figure S2, and Table S1 reconciled.
- Main verdict: **Read first**.
- Correspondence verdict: **Skim deeply**.
- SEA mechanical/semantic QA: **PASS** for both publication units.

## Interpretation boundary

The confirmatory DAPA-CKD evidence supports the primary cardiorenal/kidney composite and the prespecified hierarchical secondary renal, cardiovascular-death/HF-hospitalization, and all-cause mortality outcomes. Cardiovascular death alone had HR 0.81 (95% CI 0.58–1.12) and is not elevated to a confirmatory finding. Prespecified subgroups are retained with the explicit boundary that they were not multiplicity-adjusted. The source directly supports albuminuric CKD with eGFR 25–75 mL/min/1.73 m² under its protocol exclusions; broader transport is inference, not reported trial evidence.

The correspondence is a distinct interpretive publication unit. It adds baseline-diuretic subgroup information and a dietary-sodium measurement limitation but does not convert proposed natriuretic or tubuloglomerular mechanisms into randomized causal findings.

## Reference queue

- Main-article bibliography entries: **20**.
- DAPA-CKD correspondence citation entries itemized: **8 unique**.
- Already processed main references are marked complete: Wanner et al. 2016, Wiviott et al. 2019, McMurray et al. 2019, and Zinman et al. 2015.
- Other citations remain independent tasks unless separately completed elsewhere.

## Output files

- `heerspink-stefansson-2020-nejmoa2024816-atoms.json`
- `heerspink-stefansson-2020-nejmoa2024816-validation.json`
- `heerspink-stefansson-2020-nejmoa2024816-coverage.json`
- `heerspink-stefansson-2020-nejmoa2024816-crosswalk.json`
- `heerspink-stefansson-2020-nejmoa2024816-sea.html`
- `heerspink-stefansson-2020-nejmoa2024816-sea-qa.json`
- `nejmc2032809-correspondence-2021-atoms.json`
- `nejmc2032809-correspondence-2021-validation.json`
- `nejmc2032809-correspondence-2021-coverage.json`
- `nejmc2032809-correspondence-2021-crosswalk.json`
- `nejmc2032809-correspondence-2021-sea.html`
- `nejmc2032809-correspondence-2021-sea-qa.json`
- `heerspink-stefansson-2020-nejmoa2024816-reference-task-queue.md`
- `heerspink-stefansson-2020-nejmoa2024816-processing-report.md`

## Drive lifecycle and state update

- Main ATOM/validation/coverage/crosswalk/SEA-QA JSON files are saved in `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`.
- Correspondence ATOM/validation/coverage/crosswalk/SEA-QA JSON files are saved in the same JSON output folder.
- Main and correspondence SEA HTML files are saved in `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`.
- The reference task queue and this processing report are saved in `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`.
- The complete three-file source packet was moved intact from Active Literature to `90 - Processed / Clinical Medicine & Pharmacy / 53 - Heerspink Stefansson 2020`.
- `2026-08-20 SGLT2i formulary change rationale - TBR Task List.md` now marks both `NEJMoa2024816` and `NEJMc2032809` complete; item-level status is **85 checked / 38 unchecked**.
- `TBR - Current Task Queue` was updated to **25** numbered Active Literature source folders and **53** numbered processed clinical source folders, with the DAPA-CKD completion recorded.
