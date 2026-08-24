# Häring Merker 2013 — Processing Report

## Source packet
- Primary article: `3396.pdf` — DOI `10.2337/dc12-2673`; *Diabetes Care* 2013;36:3396–3404.
- Supplement: `dc122673supplementarydata.pdf`.

## ATOM
- Publication ID: `23d03de2-6385-485f-b224-b4b1936add32`
- Atoms: **98**
- Pydantic structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Status: **PASS**
- Counts by kind: `{'adverse_event': 16, 'author_conclusion': 2, 'comparator_description': 1, 'conflict_of_interest': 1, 'eligibility_criterion': 4, 'funding_disclosure': 1, 'intervention_description': 2, 'limitation': 6, 'method': 8, 'outcome_definition': 4, 'population_description': 4, 'qualitative_result': 4, 'quantitative_result': 32, 'study_objective': 1, 'subgroup_result': 12}`

## SEA coverage
- Main figures: **2/2 reconciled**.
- Main tables: **2/2 reconciled**.
- Supplementary figures: **3/3 reconciled**.
- Supplementary tables: **5/5 reconciled**.
- SEA QA: **PASS**.
- Source discrepancy preserved: Supplementary Table 1 states meal-test subset n=125, while listed arm counts total 124 and the main article describes 124.

## Reference task queue
- **32** numbered references were preserved in source order and normalized to `haring-merker-2013-reference-task-queue.md`.
- Every reference is an unchecked downstream task; **12** are tagged high priority for direct study context, SGLT2 mechanism, empagliflozin development, or interpretation.
- External bibliographic correction was not performed because `@VERIFY` was not activated.

## Queue reconciliation — 2026-08-23
- Task path `3/2/1/21` resolved to a stale active wrapper for this already processed publication.
- The wrapper contained only `PMID_23963895_acquisition_log.json`; the primary article and supplement were already in the canonical processed packet.
- The stale wrapper was moved under `90 - Processed / Clinical Medicine & Pharmacy / 40 - Häring Merker 2013` and renamed `Reconciled active intake - 2026-08-23`.
- The parent SGLT2 task-list item was already checked complete, so SGLT2 item totals are unchanged.

## Project-source governance
- Scientific outputs were previously generated using `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, project large-source ATOM/SEA guidance, and the supplied SEA protocol, with `example_atom.json` illustrative only.
- Current queue reconciliation inspected the available ATOM/SEA governing sources and did not alter scientific assertions or validation results.
- SEA v4 remains governing; historical v3 remains reference-only.

## Output routing
- JSON outputs → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`
- SEA HTML → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`
- Reference task queue, processing report, and reconciliation report → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`
