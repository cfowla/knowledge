# Processing report: Empagliflozin and Progression of Kidney Disease in Type 2 Diabetes

Source packet: `3 - Wanner Inzucchi 2016`  
Inputs: `NEJMoa1515920.pdf`, `nejmoa1515920_appendix.pdf`, `nejmoa1515920_protocol.pdf`  
DOI: `10.1056/NEJMoa1515920`  
Trial: `NCT01131676`  
Publication ID: `3371052e-0431-5780-b277-f326b5863f40`

## ATOM

- LiteratureAtoms: 86
- Atom counts by kind: `{"adverse_event": 20, "author_conclusion": 2, "comparator_description": 1, "eligibility_criterion": 2, "funding_disclosure": 1, "intervention_description": 2, "limitation": 4, "method": 18, "other": 1, "outcome_definition": 7, "population_description": 8, "qualitative_result": 4, "quantitative_result": 15, "study_objective": 1}`
- Semantic extraction runs: `{"wanner-inzucchi-2016-nejmoa1515920-design-methods-v1": 21, "wanner-inzucchi-2016-nejmoa1515920-interpretation-disclosure-v1": 9, "wanner-inzucchi-2016-nejmoa1515920-population-baseline-v1": 8, "wanner-inzucchi-2016-nejmoa1515920-protocol-sap-v1": 7, "wanner-inzucchi-2016-nejmoa1515920-renal-function-v1": 8, "wanner-inzucchi-2016-nejmoa1515920-renal-outcomes-v1": 7, "wanner-inzucchi-2016-nejmoa1515920-safety-v1": 20, "wanner-inzucchi-2016-nejmoa1515920-supplement-subgroups-v1": 6}`
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate canonical statements: 0
- Duplicate statement-anchor pairs: 0

## SEA

- Source type: prespecified renal/microvascular analysis within a randomized, double-blind, placebo-controlled cardiovascular outcomes trial
- Main figures reconciled: 3/3
- Main tables reconciled: 2/2
- Supplementary objects reconciled: Figures S1-S9; Tables S1-S8
- Protocol/SAP: renal endpoint definitions and Publication SAP renal-analysis workflow semantically batched
- Verdict: `Read first`
- SEA QA: `PASS`

## Reference queue

- Bibliography entries extracted: 39
- Reference 23 (Zinman et al. 2015 parent EMPA-REG cardiovascular outcomes paper) is already processed in the current TBR stream; other bibliography items remain independent reference tasks unless separately completed elsewhere.

## Extraction limitations / appraisal boundaries

- The evidence directly evaluates empagliflozin, not dapagliflozin equivalence or a universal SGLT2 class effect.
- The enrolled population had type 2 diabetes plus established cardiovascular disease/high cardiovascular risk and baseline eGFR ≥30 mL/min/1.73 m².
- No formal a priori power calculations were performed for microvascular outcomes; nominal alpha 0.05 was used without multiplicity correction.
- The harder renal composite of creatinine doubling, renal-replacement therapy, or renal death was post hoc.
- Hard renal-event counts were comparatively small; the broader nephropathy composite was substantially influenced by macroalbuminuria progression.
- Bibliography entries were not atomized; they were preserved as a separate reference task queue.
- No external current-practice evidence was imported into ATOM or SEA claims.

## Source hashes (SHA-256)

- `NEJMoa1515920.pdf`: `477fe88d47fefb30cce163ffde1f845e46ba02f2f33785fa00f4275eb0184293`
- `nejmoa1515920_appendix.pdf`: `fe90c4d62f6b0aeadc61f1412daf159f1e8ca3f644afd4231d22a22e3d5f9ca2`
- `nejmoa1515920_protocol.pdf`: `f83e22074d7863cdc9e34a1ca9750f0addb7f9f0a2b778cf20fc7a4f2ad13443`

## Drive lifecycle

- ATOM/validation/coverage/crosswalk/SEA-QA JSON files: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`.
- SEA HTML: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`.
- Reference task queue and processing report: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`.
- Source packet moved intact from `10 - Active Literature / 3 - Wanner Inzucchi 2016` to `90 - Processed / Clinical Medicine & Pharmacy / 49 - Wanner Inzucchi 2016`; all three input PDFs were verified in the destination folder.
- `2026-08-20 SGLT2i formulary change rationale - TBR Task List.md` updated: Wanner et al. 2016 checked complete; item-level status reconciled to 79 checked / 44 unchecked.
- `TBR - Current Task Queue` updated to 29 numbered Active Literature source folders and 49 numbered Processed clinical source folders, with Wanner et al. 2016 added to the completed/reconciled record.
