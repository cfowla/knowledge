# Processing report: Dapagliflozin and Cardiovascular Outcomes in Type 2 Diabetes

Source packet: `4 - Wiviott Raz 2019`  
Inputs: `NEJMoa1812389.pdf`, `nejmoa1812389_appendix.pdf`, `nejmoa1812389_protocol.pdf`  
DOI: `10.1056/NEJMoa1812389`  
Trial: `NCT01730534`  
Publication ID: `f12745dc-e7b9-59d0-885e-b86b3200d31a`

## ATOM

- LiteratureAtoms: 111
- Atom counts by kind: `{"adverse_event": 15, "author_conclusion": 4, "comparator_description": 1, "data_availability": 1, "eligibility_criterion": 5, "funding_disclosure": 1, "intervention_description": 1, "limitation": 7, "method": 21, "outcome_definition": 6, "population_description": 12, "qualitative_result": 4, "quantitative_result": 19, "study_objective": 1, "subgroup_result": 13}`
- Semantic extraction runs: `{"declare-clinical-outcomes-v1": 11, "declare-design-methods-v1": 25, "declare-interpretation-v1": 11, "declare-population-baseline-v1": 12, "declare-protocol-sap-v1": 11, "declare-risk-factor-effects-v1": 4, "declare-safety-v1": 17, "declare-sensitivity-v1": 5, "declare-subgroups-v1": 15}`
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate canonical statements: 0
- Duplicate statement-anchor pairs: 0

## SEA

- Source type: randomized, double-blind, placebo-controlled cardiovascular outcomes trial
- Main figures reconciled: 3/3
- Main tables reconciled: 2/2
- Supplementary objects reconciled: Figures S1-S6; Tables S1-S3
- Protocol/SAP: final Statistical Analysis Plan Edition 8 (31 May 2018), analysis sets, primary testing hierarchy, sensitivity methods, closed testing, safety framework, and amendment chronology semantically reconciled
- Verdict: `Read first`
- SEA QA: `PASS`

## Reference queue

- Bibliography entries extracted: 36
- References 14 (Zinman et al. 2015) and 19 (Wanner et al. 2016) are already processed in the current TBR stream; other bibliography items remain independent reference tasks unless separately completed elsewhere.

## Extraction limitations / appraisal boundaries

- The evidence directly evaluates dapagliflozin in adults with type 2 diabetes and established ASCVD or multiple risk factors; it is not a universal SGLT2 class-effect proof.
- Screening creatinine clearance <60 mL/min was excluded, so advanced CKD representation was limited.
- A placebo adherence run-in creates selection that can reduce routine-practice generalizability.
- The co-primary cardiovascular-death-or-heart-failure efficacy endpoint was added during the trial in response to external evidence, before DMC review of comparative MACE efficacy data; alpha was split without increasing sample size.
- MACE superiority and cardiovascular/all-cause mortality benefit were not demonstrated.
- Many secondary, subgroup, and safety comparisons were not multiplicity-protected and should not be elevated to confirmatory claims.
- Bibliography entries were not atomized; they were preserved as a separate reference task queue.
- No external current-practice evidence was imported into ATOM or SEA claims.

## Source hashes (SHA-256)

- `NEJMoa1812389.pdf`: `2c022acf5c3082daad6f5ce81b12df825d171ef27fe7932935a54f20a14c564d`
- `nejmoa1812389_appendix.pdf`: `cb08b90799f837d21bfb8f91d8b61f2cecf65e5e1c05f2bd550b59a74d055031`
- `nejmoa1812389_protocol.pdf`: `e1dfa7c6073a06b8480e094f405af7c5b1c8e9dca8dc9352d446ec5f9c852d4a`

## Drive lifecycle

- ATOM/validation/coverage/crosswalk/SEA-QA JSON files: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`.
- SEA HTML: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`.
- Reference task queue and processing report: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`.
- Source packet moved intact from `10 - Active Literature / 4 - Wiviott Raz 2019` to `90 - Processed / Clinical Medicine & Pharmacy / 50 - Wiviott Raz 2019`; all three input PDFs were verified in the destination folder.
- `2026-08-20 SGLT2i formulary change rationale - TBR Task List.md` updated: Wiviott et al. 2019 checked complete; item-level status reconciled to 80 checked / 43 unchecked.
- `TBR - Current Task Queue` reconciled to 28 numbered Active Literature source folders and 50 numbered Processed clinical source folders, with Wiviott et al. 2019 added to the completed/reconciled record.
