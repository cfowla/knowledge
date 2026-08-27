# Processing report: 14. Children and Adolescents: Standards of Care in Diabetes—2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s014.pdf`  
Drive file ID: `1-rETa9X2cRcKb84a-I1CBQqPpR10caar`  
DOI: `10.2337/dc26-S014`  
SHA-256: `0aacb5775e36de0b11817af940a9b4a6d392efc4c61ba6187db6d9e0c2e9b756`

## Prewalk

- Exact source identity matched the expected Drive ID and was verified as a direct child of the Active ADA folder.
- Repository searches for `dc26s014` and `dc26-s014` found no exact-section artifact family before generation.
- Historical ADA outputs were used only for file-layout and reporting conventions; no neighboring section supplied substantive evidence.

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
- SEA QA: PASS
- Verdict: `Read first`

## Reference task queue

- Bibliography entries extracted: 251
- P0: 107
- P1: 47
- P2: 97
- Bibliography entries were not atomized.

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

- Pending repository publication and independent readback of all 8 artifacts.

## Lifecycle state

- Promotion gate: **PENDING repository readback**.
- Source remains Active until the complete GitHub output family is independently verified.
