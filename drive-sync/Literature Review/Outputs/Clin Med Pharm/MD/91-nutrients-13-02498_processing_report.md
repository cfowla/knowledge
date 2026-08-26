# Publication packet repair report: 91 - nutrients-13-02498

## Lifecycle status

PASS - ATOM/SEA VERIFIED

## Source audit

The packet contains one usable primary source, `nutrients-13-02498.pdf`, and no supplement. The source is Arribas-López et al., *The Effect of Amino Acids on Wound Healing: A Systematic Review and Meta-Analysis on Arginine and Glutamine*, Nutrients 2021;13:2498, DOI `10.3390/nu13082498`. The 26-page PDF SHA-256 is `634f8b1359ceb9a660f561bf42ae55a1dafba68f4af25d4974b8a8fb085c0a8e`.

No identity-matched ATOM, SEA, validation, coverage, reference, or processing artifact was found in the Clinical Medicine and Pharmacy GitHub Sync output folders before regeneration.

## ATOM validation

The regenerated ATOM file contains 25 LiteratureAtom objects under `atoms`. Every atom uses publication ID `a36bb0dc-395a-5348-8a0e-9e08121b52d8`, atom IDs are unique, and every provenance record carries the current primary-source hash.

Validation executed against the supplied governing files in the required order: `literature(1).py` structural validation, `literature_atom.schema.json` JSON Schema validation, then `literature_atoms(1).py` atom-kind sufficiency validation. Structural errors: 0. JSON Schema errors: 0. Sufficiency errors: 0. Sufficiency warnings: 0.

The atoms remain `needs_review`. Packet-level semantic verification is complete, but the extractor and packet auditor are not an independent human reviewer.

This publication is a secondary systematic review. Review-level pooled syntheses are preserved as review-level evidence. Cited primary-study findings are not represented as if this review generated them.

## SEA and coverage verification

The SEA HTML parses and passes its mechanical QA. All 15 main-text figures and all 3 main tables are reconciled, including the two panels of Figure 14. There is no material supplement in the packet.

Direct source checks passed for the conclusion, mortality result, limitations, and a figure-derived T-cell claim. The audit preserved several source-integrity discrepancies rather than silently correcting them:

- Abstract hydroxyproline CI upper bound `4.45` conflicts with Results and Figure 8 upper bound `5.45`.
- Methods and Figures 9 and 15 use standardized mean difference, while nearby prose or the abstract calls the effects MD.
- Figure 15 totals 315 plus 312 participants, while Results prose reports 540 participants.
- The abstract states ten electronic databases, while Methods names six search sources.
- The displayed study-selection counts in Figures 4 and 5 are not fully arithmetically reconcilable.

ATOM and SEA use the same source file and SHA-256. No consequential contradiction between the regenerated ATOM and SEA remains after preserving the source's own discrepancies.

## Reference processing

The source bibliography contains 115 numbered references. All 115 are represented exactly once in the reference task queue. Missing reference numbers: 0. Duplicate reference numbers: 0. Every queue entry has a source role, priority, and downstream action.

Reference processing for this publication packet is complete. Open checkboxes are downstream cited-publication work and do not indicate missing bibliography extraction from this packet.

## Governing sources

ATOM used `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom(1).json`, with the example treated as illustrative only. SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing file. Its internal heading identifies Integrated Compact v3, but the project precedence makes the v4-named file authoritative. `large-source-ATOM-SEA.md` guided coverage and reconciliation. `summary-evaluation-appraisal-protocol-v3-compact.html` was historical reference only. `unslop.skill.md` controlled prose style.

No external current-practice verification was performed. This audit evaluates the supplied 2021 source and its project artifacts, not current wound-care guidance.

## Lifecycle action

The packet was moved to `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`. The folder name and Drive ID were preserved.

Move evidence:

- Packet folder Drive ID: `1XTailwFluvu_hU2Y87xxe0QYvvHFMdUD`
- Previous parent: `1wA_mmV9fJvfM7ILPwPuc-Uac1SJ1hpk0`
- New parent: `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`
- Move write: PASS
- Move readback: PASS

## Output locations

JSON folder `11E9bOmVQfGBg5ImBnK4WzaJAnC7gPB9J`:

- `91-nutrients-13-02498_ATOM.json`, Drive ID `1JSgZy9zWGOootUo-oxPARrZa-1Mg2EJi`
- `91-nutrients-13-02498_ATOM_validation.json`, Drive ID `1QMb371d_TSeipLy55UDEYzPxHJFFZ2Wi`
- `91-nutrients-13-02498_coverage.json`, Drive ID `1Prkravp4O4Sdoc1AJbEF6yN5CORnAECR`
- `91-nutrients-13-02498_SEA_validation.json`, Drive ID `1GBTqDYg6Ju1Kmp3-mWSupa-uXapGJix7`
- `91-nutrients-13-02498_processing_report.json`, Drive ID `133I7vQ-VSY2SvRL4QFYQLCui5kJOi16a`

HTML folder `1t2Qgc7ljqbHaepJpxOqFi-M6-tL_CF3W`:

- `91-nutrients-13-02498_SEA.html`, Drive ID `1Q2ckNBi2Lo7bK0x8YQgEWlZ1NzckheWE`

Markdown folder `1lco726EB7CwmkbsW3eun3kZgILdZinZv`:

- `91-nutrients-13-02498_reference_task_queue.md`, Drive ID `1UiVZHAQ_PN1LqLErAVdkby6kO8HkeYqj`
- `91-nutrients-13-02498_processing_report.md`, Drive ID `1T9C1vt7-ivQc6M0GYEOce3LtmoP98W2F`

Exact remaining task for this publication packet: none. Open reference queue items are downstream cited-publication tasks outside this closed packet.
