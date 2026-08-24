# Häring Merker 2013 — Queue Reconciliation Report

## Trigger
Task queue path: `3/2/1/21`.

## Publication identity
- Häring HU, Merker L, Seewaldt-Becker E, et al.
- *Empagliflozin as Add-on to Metformin Plus Sulfonylurea in Patients With Type 2 Diabetes: A 24-week, randomized, double-blind, placebo-controlled trial.*
- Diabetes Care. 2013;36:3396–3404.
- DOI: `10.2337/dc12-2673`
- PMID: `23963895`

## Existing validated work
The queue entry resolves to the already processed publication packet at `90 - Processed / Clinical Medicine & Pharmacy / 40 - Häring Merker 2013`.

- 98 LiteratureAtoms; Pydantic structural errors: 0; JSON Schema errors: 0; sufficiency errors: 0; sufficiency warnings: 0.
- SEA QA: PASS.
- Coverage reconciled 2/2 main figures, 2/2 main tables, 3/3 supplementary figures, and 5/5 supplementary tables.
- The source discrepancy remains preserved: Supplementary Table 1 states meal-test subset n=125, while listed arm counts total 124 and the main article describes 124.

## Reference-queue normalization
The previously stored 32-entry bibliography was converted to the current checkbox-based reference task-queue format without external bibliographic correction because `@VERIFY` was not activated. Twelve entries are tagged high priority because they directly inform study context, SGLT2 mechanism, empagliflozin development, or trial interpretation.

## Active-wrapper reconciliation
The stale active wrapper `21 - Haring Merker 2013` contained only `PMID_23963895_acquisition_log.json`; the primary article and supplement were already in the canonical processed packet. The active wrapper was therefore moved under the canonical processed packet as `Reconciled active intake - 2026-08-23`, preserving the acquisition log and removing the stale publication entry from Active Literature.

## Queue state
The parent SGLT2 task-list record for PMID `23963895` was already checked complete, so item-level SGLT2 completion totals are unchanged. The Active Literature numbered-folder count decreases by one after this reconciliation.
