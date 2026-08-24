# Cuker et al. 2026 processing status: ATOM and SEA blocked

## Source identity

- Title: *American Society of Hematology 2026 Guidelines for Immune Thrombocytopenia (ITP): Initial and Second-Line Therapy in Adults with Primary ITP*
- Authors: Adam Cuker, Deirdra R. Terrell, Honieh Sowdagar, et al.
- Journal: Blood Advances
- Publication date: August 19, 2026
- DOI: `10.1182/bloodadvances.2026021269`
- PMID: `42617047`
- Source type: focused clinical guideline update

## Requested workflow

Activated macros: `@ATOM + @SEA`. A reference task queue was also requested.

## Source access and coverage decision

The selected Drive packet contains only `PMID_42617047_acquisition_log.json`. The acquisition log records failed lawful full-text acquisition and sets `atom_sea_ready=false`. A fresh check on August 23, 2026 confirmed current publication metadata and the abstract, but did not recover the final full guideline or its complete bibliography.

ASH also exposes a 2025 public-comment supplementary document. It is explicitly labeled as a draft and cannot replace the August 2026 final publication. It can be used to understand development lineage and to locate candidate evidence, but final recommendation wording, rationale, evidence profiles, exclusions, references, and any post-comment changes must be read from the final publication before ATOM or SEA completion.

Coverage decision: **blocked for full @ATOM and @SEA**. The governing ATOM workflow requires source-supported assertions with reliable anchors. The governing SEA workflow requires source-wide mapping and coverage before final appraisal. An abstract-only extraction or a draft-to-final reconstruction would violate those gates.

## ATOM status

- Atom extraction: **not run**
- Validated atoms: **0**
- Structural validation: **not applicable**
- JSON Schema validation: **not applicable**
- Sufficiency validation: **not applicable**
- Reason: the final source body is unavailable.

The accessible abstract was not converted into a substitute final-source atom set. The 2025 draft recommendations were not represented as final 2026 recommendations.

## SEA status

- Coverage manifest: **incomplete and blocked**
- Section condensation: **not run**
- Final figure, table, and workflow reconciliation: **not possible**
- Final scoring and verdict: **not assigned**
- SEA HTML: **not generated**

## Reference task queue

The final 2026 bibliography was not exposed by the sources checked. A blocked reference task queue was generated as `cuker-terrell-2026-itp-guideline-reference-task-queue.md`. It records the acquisition and reconciliation work still required and includes only clearly labeled non-final development leads from the official 2025 public-comment material.

## File disposition

The packet is **not eligible for 90 - Processed** because ATOM, validation, SEA, and final reference extraction are incomplete. The correct state is **Needs Resolution**. The parent PubMed-trending checkbox should remain unchecked.

## Completion condition

Resume when a lawful copy of the final guideline is available. Process that final source from the beginning, extract and validate LiteratureAtoms, reconcile all source visuals and recommendation blocks, generate the SEA HTML only after coverage is complete, extract the final bibliography, and then move the packet to Processed.

Generated: `2026-08-23T08:56:16Z`
