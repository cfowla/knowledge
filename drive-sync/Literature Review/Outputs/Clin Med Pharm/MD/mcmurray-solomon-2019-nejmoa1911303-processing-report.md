# Processing report: Dapagliflozin in Patients with Heart Failure and Reduced Ejection Fraction

Source packet: `5 - McMurray Solomon 2019`  
Inputs: `NEJMoa1911303.pdf`, `nejmoa1911303_appendix.pdf`, `nejmoa1911303_protocol.pdf`, `NEJMc1917241.pdf`  
Main DOI: `10.1056/NEJMoa1911303`  
Correspondence DOI: `10.1056/NEJMc1917241`  
Trial: `NCT03036124`  
Main publication ID: `08048970-c024-590b-baa3-080fb2f657b7`  
Correspondence publication ID: `a5a8238d-ad19-50d7-a9e3-408a11522b59`

## ATOM

- Main DAPA-HF LiteratureAtoms: 108
- Main atom counts by kind: `{"adverse_event": 11, "author_conclusion": 2, "comparator_description": 1, "eligibility_criterion": 4, "funding_disclosure": 1, "intervention_description": 1, "limitation": 4, "method": 13, "outcome_definition": 6, "population_description": 11, "qualitative_result": 4, "quantitative_result": 16, "study_objective": 1, "subgroup_result": 33}`
- Main semantic extraction runs: `{"dapa-hf-design-methods-v1": 9, "dapa-hf-efficacy-v1": 18, "dapa-hf-interpretation-v1": 9, "dapa-hf-outcomes-v1": 6, "dapa-hf-population-eligibility-v1": 14, "dapa-hf-protocol-sap-v1": 4, "dapa-hf-safety-v1": 12, "dapa-hf-subgroups-v1": 33, "dapa-hf-supplement-v1": 3}`
- Correspondence LiteratureAtoms: 9
- Correspondence atom counts by kind: `{"author_conclusion": 5, "conflict_of_interest": 1, "other": 3}`
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate canonical statements: 0
- Duplicate statement-anchor pairs: 0

## SEA

- Main source type: phase 3 randomized, double-blind, placebo-controlled, event-driven HFrEF trial
- Main figures reconciled: 3/3
- Main tables reconciled: 2/2
- Supplementary objects reconciled: Figures S1-S2; Table S1
- Protocol/SAP: original protocol v1.0 (26-Oct-2016), final protocol v2.0 (26-Oct-2017), original SAP v1.0 (31-Jan-2017), final SAP v3.0 (23-Jul-2019) semantically reconciled
- Main verdict: `Read first`
- Correspondence verdict: `Skim deeply`
- SEA QA: `PASS` for both publication units

## Reference queue

- Main-article bibliography entries extracted: 20
- Correspondence citation entries itemized: 12
- Main references 1 (Zinman et al. 2015), 3 (Wiviott et al. 2019), and 10 (Wanner et al. 2016) are already processed in the current TBR stream.
- Remaining bibliography items remain independent reference tasks unless separately completed elsewhere.

## Extraction limitations / appraisal boundaries

- DAPA-HF directly evaluates dapagliflozin 10 mg once daily in symptomatic HFrEF with LVEF ≤40%; it does not alone establish effects across all HF phenotypes or all SGLT2 inhibitors.
- Enrollment excluded eGFR <30 mL/min/1.73 m² or rapidly declining renal function and SBP <95 mm Hg; direct transport beyond those boundaries requires other evidence.
- Black participants constituted <5%, few very elderly multimorbid patients were enrolled, and baseline sacubitril-valsartan use was low.
- The renal composite was uncommon and did not show a statistically persuasive difference.
- Individual subgroup estimates are less precise than the randomized overall effect; the NYHA class contrast should not be elevated above the totality of subgroup evidence.
- The 2020 correspondence is interpretive follow-up. It clarifies protocol and measurement boundaries but does not convert proposed mechanisms or rebuttals into randomized causal evidence.
- Bibliography entries were not atomized; they were routed to the reference task queue.

## Source hashes (SHA-256)

- `NEJMoa1911303.pdf`: `f722bcd53ae00633d3fd947fe2b968821cee355fcf2a8ca1d20c77b9336a1395`
- `nejmoa1911303_appendix.pdf`: `be3782e5cce018dba47c85f09b394cd847ff8c3adf5cf8ddb6280c72a4fe3568`
- `nejmoa1911303_protocol.pdf`: `2aaa0770fb33dd19335299ad3582779c3ff98125dd6b720b04092d69b01ad053`
- `NEJMc1917241.pdf`: `84dcdbcc48ec348f56dabb84cf26d247dd30ba21a8b2159bb2b07f0576568979`

## Drive lifecycle

- ATOM/validation/coverage/crosswalk/SEA-QA JSON files: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`.
- SEA HTML files: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`.
- Reference task queue and this processing report: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`.
- Source packet stored intact in `90 - Processed / Clinical Medicine & Pharmacy / 51 - McMurray Solomon 2019`.
- Stateful TBR documentation marks both NEJMoa1911303 and NEJMc1917241 complete; the SGLT2 queue is reconciled to 82 checked / 41 unchecked records, and `TBR - Current Task Queue` is reconciled to 27 numbered Active Literature source folders and 51 numbered processed clinical source folders.
