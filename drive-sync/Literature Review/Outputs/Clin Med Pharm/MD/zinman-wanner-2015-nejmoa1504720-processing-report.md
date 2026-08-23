# Processing report: Empagliflozin, Cardiovascular Outcomes, and Mortality in Type 2 Diabetes

Source packet: `2 - Zinman Wanner 2015`  
Inputs: `NEJMoa1504720.pdf`, `nejmoa1504720_appendix.pdf`, `nejmoa1504720_protocol.pdf`  
DOI: `10.1056/NEJMoa1504720`  
PMID: `26378978`  
Publication ID: `8537e224-7854-57b3-9f1c-4e183c175549`

## ATOM

- LiteratureAtoms: 91
- Atom counts by kind: `{"adverse_event": 13, "author_conclusion": 3, "comparator_description": 1, "conflict_of_interest": 1, "eligibility_criterion": 3, "funding_disclosure": 1, "intervention_description": 2, "limitation": 5, "method": 12, "outcome_definition": 5, "population_description": 8, "qualitative_result": 3, "quantitative_result": 31, "study_objective": 1, "subgroup_result": 2}`
- Semantic extraction runs: `{"zinman-wanner-2015-nejmoa1504720-cardiovascular-outcomes-v1": 24, "zinman-wanner-2015-nejmoa1504720-design-methods-v1": 24, "zinman-wanner-2015-nejmoa1504720-interpretation-disclosure-v1": 11, "zinman-wanner-2015-nejmoa1504720-metabolic-riskfactor-v1": 9, "zinman-wanner-2015-nejmoa1504720-population-baseline-v1": 9, "zinman-wanner-2015-nejmoa1504720-safety-v1": 14}`
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
- Supplementary result objects reconciled: Figures S1-S3; Tables S1-S14
- Protocol/SAP analysis workflows reconciled: final hierarchy + Amendment 3/interim-analysis provenance
- Verdict: `Read first`
- SEA QA: PASS

## Reference queue

- Bibliography entries extracted: 30
- High-priority direct-evidence/design/context candidates: 16
- Standard contextual/mechanistic references: 14

## Extraction limitations / appraisal boundaries

- EMPA-REG OUTCOME is direct evidence for empagliflozin, not proof of dapagliflozin equivalence or a universal SGLT2 class effect.
- The trial enrolled patients with type 2 diabetes and established cardiovascular disease/high cardiovascular risk; extrapolation to lower-risk or inpatient populations requires other evidence.
- Subgroup interaction tests were not adjusted for multiple testing; cardiovascular-death subgroup analyses were post hoc.
- The protocol/SAP documents a change from an earlier 1.8/1.3 noninferiority sequence to the final 1.3 margin and an interim-analysis Haybittle-Peto correction; this is preserved as analysis provenance.
- The bibliography was not atomized; it is preserved as a separate reference task queue.
- No external bibliographic correction or current-practice verification was performed because `@VERIFY` was not activated.

## Source hashes (SHA-256)

- `NEJMoa1504720.pdf`: `37430615c8a0ef802416eb0ce516bd882a0de8127623b311f1e959bc6e605961`
- `nejmoa1504720_appendix.pdf`: `a45ef1a095d41e429bb3c20b5f6d134f20f9cfdab461723ffb5fd1fe0c7755fc`
- `nejmoa1504720_protocol.pdf`: `35274668a72eb30cb4c204010710946f74f7302f7628721b0c021259b1a4cad1`

## Drive lifecycle

- ATOM/validation/coverage/crosswalk/SEA-QA JSON files: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`.
- SEA HTML: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`.
- Reference task queue and processing report: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`.
- Source packet moved intact from `10 - Active Literature / 2 - Zinman Wanner 2015` to `90 - Processed / Clinical Medicine & Pharmacy / 48 - Zinman Wanner 2015`; all three input files were verified in the destination folder.
- `2026-08-20 SGLT2i formulary change rationale - TBR Task List.md` updated: EMPA-REG OUTCOME checked complete; item-level status reconciled to 78 checked / 45 unchecked.
- `TBR - Current Task Queue` updated to 30 numbered Active Literature source folders and 48 numbered Processed clinical source folders, with this publication added to the completed/reconciled record.
