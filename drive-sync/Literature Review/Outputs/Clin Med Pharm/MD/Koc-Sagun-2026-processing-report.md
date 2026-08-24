# Koç & Sağun 2026 — Processing Report

## Requested workflow

`@ATOM + @SEA + reference task queue`

## Source identity

- **Title:** Large language model accuracy in inhaler technique counselling for asthma and COPD: A comparison of free and paid models across ten devices
- **Authors:** Abdurrahman Koç; Ferhat Sağun; Necmettin Öğe; Sami Avcil; Ali Tolga Çelik; Muhammet Ali Takeş; Bekir Sunay
- **Journal:** Digital Health
- **Publication date:** 2026-08-14
- **PMID:** 42605352
- **DOI:** 10.1177/20552076261478506

## Source-access result

The packet contains only `PMID_42605352_acquisition_log.json`. The acquisition log records a failed lawful acquisition and `atom_sea_ready: false`. No full-text PDF/JATS, supplement, or bibliography is present.

A current external verification on 2026-08-23 confirmed the article identity and abstract, but did not provide a defensible complete primary-source payload or bibliography. The search was therefore used only for source-identity/retrieval confirmation.

## ATOM status

**NOT RUN — source gate failed.**

LiteratureAtom extraction requires independently reviewable assertions anchored to the primary source. Creating a complete atom set from the abstract would omit methods/results/limitations and source visuals and would not satisfy the requested workflow.

- Atom count: 0
- Pydantic structural validation: not applicable
- JSON Schema validation: not applicable
- Sufficiency validation: not applicable

## SEA status

**NOT RUN — coverage gate failed.**

SEA v4 requires source mapping plus reconciliation of sections, figures, tables, workflows, appendices, and omissions before appraisal. Those source objects are unavailable, so no SEA scores or practice verdict were assigned. A blocked-status HTML was generated to document the failure boundary.

## Reference task queue

**BLOCKED.** The complete bibliography is unavailable. A blocked reference-queue artifact was created with acquisition/unblock tasks and zero fabricated bibliography entries.

## Disposition

This packet is **not eligible for `90 - Processed`** because the requested ATOM, SEA, and reference extraction are not complete. It should be moved from the numbered Active Literature queue to `10 - Active Literature / 3 - Needs Resolution`, matching the existing project convention for source-access blockers. The parent PubMed-trending checkbox for PMID 42605352 should remain unchecked.

## Unblock condition

Acquire the lawful primary full text and bibliography, then rerun the full `@ATOM + @SEA + reference task queue` workflow and move the packet to Processed only after validation and SEA QA pass.
