# Processing report: 15. Management of Diabetes in Pregnancy: Standards of Care in Diabetes—2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s015.pdf`  
Google Drive file ID: `12rhKQ-o9gYbqcu3peTLlTO9zqfkFXS86`  
DOI: `10.2337/dc26-S015`  
Source SHA-256: `55e99a4eb0e03da81294d7171a1f3e53b7ab6ad5b7c8af34dd4ff21f75c7bfcd`  
Publication ID: `0ef0a5b1-0219-52f4-b5cc-0d63ef57b942`

## Exact-section prewalk

- `dc26s015.pdf` was confirmed as a direct child of the Active ADA folder before processing.
- Exact repository searches for `dc26s015` and `dc26-s015` found no preexisting exact-section artifact family before processing.
- No output from `dc26s007` or another ADA section was used as completion evidence.
- Current ORACLE `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, and `summary-evaluation-appraisal-protocol-v4-compact.md` were read and matched the supplied project copies at the Git blob level.
- `large-source-ATOM-SEA.md`, `README(2).md`, and the example atom were used only in their declared supporting/illustrative roles.

## Reference extraction

- Bibliography entries extracted: **205/205**.
- Continuous numbering: **1–205 PASS**.
- Priority counts: **P0 24; P1 154; P2 27**.
- Bibliography items were preserved in the reference task queue and were not atomized as though they were primary evidence from this chapter.

## ATOM

- LiteratureAtoms: **114**.
- Shared publication ID: `0ef0a5b1-0219-52f4-b5cc-0d63ef57b942`.
- Atom counts by kind: `author_conclusion 47`, `limitation 8`, `other 29`, `qualitative_result 5`, `quantitative_result 25`.
- Semantic extraction batches: **6**.
- Guideline recommendation atoms: **47**.
- Secondary-reported-result atoms: **39**.
- Review status remains `needs_review`; no independent human review is represented.

Guideline boundary: numbered ADA recommendations are represented as guideline/panel statements using `author_conclusion` plus `guideline_recommendation` tags. Quantitative findings cited by the chapter are retained as secondary reports and are not represented as independently validated primary-study evidence.

## Validation

- Pydantic structural validation: **PASS**; errors **0**.
- JSON Schema validation: **PASS**; errors **0**.
- Sufficiency validation: **PASS**; errors **0**, warnings **0**.
- Unique atom IDs: **PASS**.
- Shared publication ID: **PASS**.
- Duplicate canonical statements: **0**.
- Duplicate statement-anchor pairs: **0**.

## SEA and coverage/reconciliation

- Source type: clinical practice guideline / standards chapter.
- PDF pages rendered and visually inspected: **18/18**.
- Substantive pages: **S321–S333**.
- Bibliography pages: **S333–S338**.
- Recommendation blocks reconciled: **33**, covering `15.1` through `15.32`, including `15.25a` and `15.25b`.
- Figures: **0/0**.
- Tables: **2/2** (`Table 15.1`, `Table 15.2`).
- Algorithms/workflows: **0/0**.
- Appendices/supplements: **0/0**.
- Bibliography: **205/205**.
- Cross-batch duplicate and inconsistency review: **completed**.
- SEA QA: **PASS**.

Key reconciliation decisions preserved:
- Preconception A1C `<6.5%` is distinct from the pregnancy A1C goal `<6%` when safely achievable.
- Table 15.2 lower target bounds are not conflated with recommendation 15.8 upper glucose goals.
- Aspirin `100–150 mg/day` is the recommendation; `162 mg/day` is retained as an acceptable option, with diabetes-specific efficacy uncertainty preserved.
- Recommendation 15.25b retains both the usual lipid-lowering stop/avoid rule and the selected very-high-risk exception.

## Crosswalk

- ATOMs mapped: **114/114**.
- All referenced atom IDs exist: **PASS**.
- Unmapped atom IDs: **0**.
- All atoms use the same publication ID: **PASS**.
- Recommendation numbers mapped: **33**.

## Required repository artifact family

Pre-promotion publication/readback status at 2026-08-27T06:41:16Z:

- `JSON/ada-ppc-2026-dc26-s015-atoms.json` — published; readback required before promotion.
- `JSON/ada-ppc-2026-dc26-s015-validation.json` — published; readback PASS.
- `JSON/ada-ppc-2026-dc26-s015-coverage.json` — published; readback PASS.
- `JSON/ada-ppc-2026-dc26-s015-crosswalk.json` — published; readback required before promotion.
- `JSON/ada-ppc-2026-dc26-s015-sea-qa.json` — published; readback required before promotion.
- `HTML/ada-ppc-2026-dc26-s015-sea.html` — published; readback required before promotion.
- `MD/ada-ppc-2026-dc26-s015-reference-task-queue.md` — published; readback required before promotion.
- `MD/ada-ppc-2026-dc26-s015-processing-report.md` — this report; lifecycle status below.

## Extraction limitations / schema gaps

- The current LiteratureAtom schema has no dedicated `guideline_recommendation` atom kind; project guidance permits `author_conclusion` with descriptive recommendation tags.
- The chapter delegates full ADA evidence-grading definitions and guideline-development methods to the separate Introduction and Methodology, which is outside this source PDF.
- Cited trial and observational results require direct reading of the cited publications before reuse as primary-study evidence.
- Model-extracted atoms remain `needs_review` because no independent human reviewer step is represented.

## Drive lifecycle

**PRE-PROMOTION STATE:** The source remains in the Active ADA folder while the complete exact-section repository family is being opened and verified. No move has yet been performed at this report revision.

Intended destination after the complete publication gate passes: `90 - Processed / Clinical Medicine & Pharmacy / 47 - American Diabetes Association 2026`.

## Gate status

**PRE-PROMOTION GATE: PASS, subject only to repository readback of the newly published crosswalk, SEA-QA, SEA, reference queue, and this report.** No source move is permitted until those readbacks confirm the exact section and expected content.
