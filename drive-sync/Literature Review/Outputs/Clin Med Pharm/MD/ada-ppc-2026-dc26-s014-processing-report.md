# Processing report: 14. Children and Adolescents: Standards of Care in Diabetes—2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s014.pdf`  
Drive file ID: `1-rETa9X2cRcKb84a-I1CBQqPpR10caar`  
DOI: `10.2337/dc26-S014`  
SHA-256: `0aacb5775e36de0b11817af940a9b4a6d392efc4c61ba6187db6d9e0c2e9b756`

## Prewalk

- Exact source identity matched the expected Drive ID and was verified as a direct child of the Active ADA folder before processing.
- Repository searches for `dc26s014` and `dc26-s014` found no exact-section artifact family before generation.
- Historical ADA outputs were used only for file-layout and reporting conventions; no neighboring section supplied substantive evidence or completion evidence.

## Governing processing sources

- ATOM structural authority: `literature.py`; sufficiency authority: `literature_atoms.py`; serialization: `literature_atom.schema.json`; workflow context: `README(2).md`; example atom treated as illustrative only.
- SEA authority: project file `summary-evaluation-appraisal-protocol-v4-compact.md`; the internally labeled v3 material is historical/reference only.
- Large-source processing used semantic batching, shared publication identity, source-anchored extraction, batch/whole-source validation, and whole-source reconciliation before final appraisal.

## ATOM

- LiteratureAtoms: 125
- Shared publication ID: `c46b293c-9412-5e6f-8c73-faf9fd095b23`
- Atom counts by kind: `{"author_conclusion": 84, "limitation": 7, "other": 24, "quantitative_result": 10}`
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate statement-anchor pairs: 0

Formal recommendations are represented as ADA panel statements using `author_conclusion` plus `guideline_recommendation` tags. Quantitative findings attributed to underlying studies are tagged `secondary_reported_result` and remain anchored to this chapter; the Standards chapter is not represented as if it enrolled those study populations.

## SEA and reconciliation

- Source type: clinical practice guideline / Standards chapter
- Substantive coverage: S297–S314 before References
- Figures reconciled: 1/1 (Figure 14.1)
- Tables reconciled: 1/1 (Table 14.1, S308–S311)
- Algorithms/workflows reconciled: 1/1 (Figure 14.1)
- Formal recommendations: 14.1–14.84 (84/84)
- Bibliography entries: 251/251
- Crosswalk unmapped atom IDs: 0
- SEA QA: PASS
- Verdict: `Read first`

## Reference task queue

- Bibliography entries extracted and reconciled: 251/251
- P0: 107
- P1: 42
- P2: 102
- Bibliography entries were not atomized.
- Independent repository readback found page-order/download-footer contamination in the initially published queue near the S319–S320 transitions. The queue was therefore regenerated from the exact Drive source by file ID using PDF column-reading order, excluding page headers, page labels, and library download stamps.
- The repair workflow verified the exact source SHA-256 before extraction and required a deterministic repaired-output SHA-256 before replacement.
- Post-repair readback confirmed clean transition entries, including reference 233 (Kinney et al., T1D Exchange cannabis/DKA), reference 238 (ADA transition position statement), and reference 251 (Carreon et al., social-support review).
- Reference repair commit: `296aa08c9e877d4be724b558173ca3bdd080849a`.

## Extraction limitations and schema gaps

- The LiteratureAtom schema has no dedicated `guideline_recommendation` atom kind; formal recommendations use `author_conclusion` with descriptive tags.
- Recommendation evidence grades are preserved in tags rather than a dedicated typed field.
- The full ADA guideline-development method and evidence-grade definitions are in the separate Introduction and Methodology and were not part of this exact input.
- All atoms remain `needs_review` because this run is not an independent human verification step.
- No external current-practice or regulatory verification was used as evidence because `@VERIFY` was not activated.

## Protocol version note

The project file is named `summary-evaluation-appraisal-protocol-v4-compact.md`, while its internal heading identifies Integrated Compact v3. The v4-named project source was treated as governing; the naming mismatch was recorded rather than silently reconciled.

## Output family

JSON folder:
- `ada-ppc-2026-dc26-s014-atoms.json`
- `ada-ppc-2026-dc26-s014-validation.json`
- `ada-ppc-2026-dc26-s014-coverage.json`
- `ada-ppc-2026-dc26-s014-crosswalk.json`
- `ada-ppc-2026-dc26-s014-sea-qa.json`

HTML folder:
- `ada-ppc-2026-dc26-s014-sea.html`

Markdown folder:
- `ada-ppc-2026-dc26-s014-reference-task-queue.md`
- `ada-ppc-2026-dc26-s014-processing-report.md`

## Publication verification

- Complete expected artifact family present in `cfowla/knowledge`: 8/8.
- Large-artifact publication commit: `2fd616872c01046f51045cd9b7a68cdf283b8cf0`; the publication assembler verified exact local SHA-256 values for ATOM, SEA, and the then-current reference queue before committing and removed its staging files/workflow.
- ATOM readback: present and exact-section scoped.
- Validation readback: Pydantic PASS; JSON Schema PASS; sufficiency PASS; no warnings.
- Coverage readback: 84/84 recommendations; 1/1 figure; 1/1 table; 1/1 workflow; 251/251 bibliography.
- Crosswalk readback: all formal recommendations and supporting claims mapped; `unmapped_atom_ids: []`.
- SEA readback: exact title/source and expected substantive sections present.
- SEA-QA readback: `PASS`; HTML parse passed; no missing TOC anchors; no forbidden/placeholder tokens; provenance present.
- Reference queue readback after repair: 251/251; P0/P1/P2 = 107/42/102; previously contaminated page-transition entries corrected.
- Processing report readback is the final publication/lifecycle gate for this packet.

## Lifecycle state

- Promotion gate: **PASS**.
- Active ADA parent: `1j50uC_mGfCpLj6jvR9en2sUilsnTGKLV`.
- Processed ADA destination: `47 - American Diabetes Association 2026`, folder ID `1YSKH6Oqj52tYPN402sa9mxs_RFzGhNlG`.
- `dc26s014.pdf` was moved using the original Drive file ID; no copy/re-upload was created.
- Fresh Active-parent search after the move returned no `dc26s014.pdf`.
- Fresh Processed-parent search returned `dc26s014.pdf` with exact Drive file ID `1-rETa9X2cRcKb84a-I1CBQqPpR10caar`.
- Final lifecycle disposition: **PROCESSED**.
