# Publication Packet Processing Report — 40 - Wharton 2021 - Semaglutide GI tolerability

## Lifecycle status

**PASS**

**OVERRIDEN BY CONNOR FOWLER ON 2026-08-26T07:36:18Z**

**HUMAN REVIEW HAS YIELDED SUFFICIENT EVIDENCE TO PASS THIS PACKET**


The primary article and material supplement are usable and identity-consistent. The missing ATOM, authoritative validation, and coverage artifacts were regenerated from the current source packet. The existing SEA HTML passes source-identity, content, visual-coverage, and mechanical QA. The packet cannot be promoted because required reference processing is not demonstrated as complete.

## Source inventory

- Primary: `Diabetes Obesity Metabolism - 2021 - Wharton - Gastrointestinal tolerability of once‐weekly semaglutide 2 4 mg in adults.pdf` — Drive ID `1er5T7rdxIc3xYXJvZxUnjt6_pDMnQGz_`; DOI `10.1111/dom.14551`; 12 PDF pages; SHA-256 `a97adb9d84aaccfc5f106264e5332029ac622ef09b13c3746db801439ce030f6`.
- Supplement: `dom14551-sup-0001-supinfo.docx` — Drive ID `1WUqzEcQsldELOM3wnpbqphoj8gcfEKR-`; 13 rendered pages; SHA-256 `723afc59f168b26ece87422c77e936ade573fca8c896427a391da59f4dd2cdbe`.
- Combined source hash: `12a749330215b64648ae99617ad1d80e38a78820dfb8339f303935865a8ce015`.
- Shared publication ID: `fa91a8b3-3bbe-5f55-b8cd-184c1d0bf4e0`.

The primary article is complete and readable. It contains the pooled STEP 1-3 post-hoc GI tolerability/weight-loss analyses and the separate STEP 4 randomized-withdrawal analysis. The supplement contains Appendix S1, Tables S1-S4, and Figures S1-S2.

## Artifact audit and repair

Identity matching used the exact title, DOI `10.1111/dom.14551`, source metadata, and content. Filename similarity alone was not accepted.

- ATOM JSON: missing before this audit; regenerated as `40-wharton-2021-semaglutide-gi-tolerability-atoms.json`.
- ATOM validation JSON: missing before this audit; regenerated as `40-wharton-2021-semaglutide-gi-tolerability-validation.json` using the supplied authoritative validators.
- Coverage JSON: missing before this audit; regenerated as `40-wharton-2021-semaglutide-gi-tolerability-coverage.json`.
- SEA HTML: existing identity-matched `40-wharton-2021-semaglutide-gi-tolerability-sea.html`; retained after QA.
- Reference task queue: existing identity-matched `40-wharton-2021-semaglutide-gi-tolerability-reference-task-queue.md`; contains all 46 printed references.
- Processing report: missing before this audit; created by this audit.

## ATOM validation

Validation executed in the required order against the supplied governing files:

1. `literature(1).py` Pydantic structural validation: **PASS** — 0 errors.
2. `literature_atom.schema.json` JSON Schema validation: **PASS** — 0 errors.
3. `literature_atoms(1).py` atom-kind sufficiency validation: **PASS** — 0 errors, 0 warnings.

Additional integrity checks: 54 atoms; one shared publication ID; atom IDs unique; 0 exact statement/anchor duplicate pairs. Model-extracted atoms remain `needs_review`; this is a review-state warning, not a structural/sufficiency failure.

Direct source spot-checks passed for the primary safety result, event-specific percentages, mediation estimates, Table 1 adherence values, author conclusion, and stated limitations.

## SEA verification

Existing SEA QA: **PASS**. HTML is parseable; internal navigation resolves; source title and DOI match; methods/design, main claims, quantitative findings, limitations, and provenance are present; no internal chat/file citation syntax or placeholder markers were found.

Coverage was reconciled against the raw sources: 12/12 primary PDF pages and 13/13 supplement pages were rendered and visually reviewed. Main-text Figures 1-4 and Table 1 are represented. Supplement Appendix S1, Tables S1-S4, and Figures S1-S2 are represented. No load-bearing visual is unaccounted for.

Semantic checks include: any GI AE 72.9% versus 47.1%; nausea 43.9% versus 16.1%; permanent GI-AE discontinuation 4.3% versus 0.7%; Figure 4 mediation effects below 1 percentage point; and the post-hoc/on-treatment/confounding/STEP 4 reporting-bias limitations.

## ATOM ↔ SEA reconciliation

ATOM and SEA use the same DOI, primary PDF, supplement, and study/version boundaries. No consequential contradiction was found. Both keep pooled STEP 1-3 results separate from the selected STEP 4 post-run-in randomized population, preserve the post-hoc nature of the weight/mediation analyses, and represent the same tolerability conclusion.

## Reference-processing gate

The reference queue contains **46** references, with **0** marked complete and **46** unresolved. A queue file by itself is not evidence that downstream reference work is complete. The audit therefore cannot certify the reference-processing requirement. Drive identity searches for reference 1 by DOI `10.1016/S2213-8587(17)30236-X` returned the Wharton source/queue context but no identity-matched completed downstream artifact for that reference, which is enough to establish that the full 46-reference gate is not demonstrated as complete.

## Lifecycle action

No move to `90 - Processed` was performed. The packet remains Active. It was not moved to Needs Resolution because the primary source is usable and the publication identity is unambiguous.

## Exact remaining task

Complete or defensibly disposition all unresolved entries in `40-wharton-2021-semaglutide-gi-tolerability-reference-task-queue.md` according to the project reference-processing convention, record completion evidence, then rerun the lifecycle gate. Promote this packet only if the reference gate passes and the repaired ATOM/SEA outputs remain valid.

## Governing sources

ATOM structural validation used the supplied `literature(1).py`; serialization validation used `literature_atom.schema.json`; atom-kind sufficiency used `literature_atoms(1).py`. `README(2).md` supplied workflow intent and `example_atom(1).json` was illustrative only. SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing protocol by project precedence; its internal heading says Integrated Compact v3. `large-source-ATOM-SEA.md` supplied supporting coverage/reconciliation guidance. The supplied v3 HTML was historical reference only.
