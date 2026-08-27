# Processing report: 16. Diabetes Care in the Hospital: Standards of Care in Diabetes—2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s016.pdf`  
Drive file ID: `1InXfDAGTrWqzZULB6kgxL7XGZp2BFsF6`  
DOI: `10.2337/dc26-S016`  
SHA-256: `e03e780318c3b06f385961c69c1ef12255c57a151706ffde97188c2fa478950b`

## Prewalk

- Exact source identity matched the expected Drive ID and was verified as a direct child of the ADA 2026 folder under Active Literature.
- Repository searches for `dc26s016` and `dc26-s016` found no exact-section artifact family before generation.
- Current ATOM domain model, sufficiency validator, schema, example, and v4-named SEA protocol were checked against the current GitHub ORACLE state; local project copies matched the current GitHub blobs for the governing code/schema/protocol files.
- Historical ADA outputs were used only for output-path and reporting conventions and did not satisfy any gate for this source.

## Reference extraction

- Bibliography entries extracted and reconciled: **198/198** (references 1–198).
- References were preserved in the task queue and were not atomized.
- Queue priority counts: P0 **152**, P1 **25**, P2 **21**. These are workflow-triage labels, not evidence grades.

## ATOM

- LiteratureAtoms: **90**
- Shared publication ID: `1c7f4385-a61c-5cd4-8f26-a5aeae13eed0`
- Atom counts by kind: `{"author_conclusion": 22, "limitation": 6, "method": 22, "other": 32, "outcome_definition": 4, "quantitative_result": 4}`
- Pydantic structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Duplicate statement-anchor pairs: **0**

Formal recommendations are represented as ADA panel statements using `author_conclusion` plus `guideline_recommendation` tags. Quantitative findings attributed to cited studies remain anchored to this chapter as secondary reported evidence; any derived absolute differences are explicitly marked `calculated_from_reported_data`.

## SEA and reconciliation

- Source type: clinical practice guideline / Standards chapter
- Substantive coverage: **S339–S350** through `The Future`, before References
- Figures/workflows reconciled: **1/1** (Figure 16.1)
- Tables reconciled: **2/2** (Tables 16.1–16.2)
- Formal recommendation identifiers: **21/21**
- Bibliography entries: **198/198**
- Crosswalk: **PASS**; all recommendation and visual IDs resolve to this source’s atoms.
- SEA QA: **PASS**
- Verdict: `Read first`

## Extraction limitations and schema gaps

- The LiteratureAtom schema has no dedicated `guideline_recommendation` atom kind; formal recommendations use `author_conclusion` with descriptive tags.
- Recommendation evidence grades are preserved in tags rather than a dedicated typed field.
- The full ADA guideline-development methodology, evidence-grade definitions, and contributor disclosures are in separate ADA materials referenced by this chapter and were not part of this exact input.
- Secondary reports from cited studies are not substitutes for primary-study extraction.
- All atoms remain `needs_review` because this run is not an independent human verification step.
- No external current-practice or regulatory verification was performed because `@VERIFY` was not activated.

## Protocol version note

The project file is named `summary-evaluation-appraisal-protocol-v4-compact.md`, while its internal heading identifies Integrated Compact v3. The current v4-named project/GitHub source was treated as governing; the naming mismatch was recorded rather than silently reconciled.

## Output family

JSON folder:
- `ada-ppc-2026-dc26-s016-atoms.json`
- `ada-ppc-2026-dc26-s016-validation.json`
- `ada-ppc-2026-dc26-s016-coverage.json`
- `ada-ppc-2026-dc26-s016-crosswalk.json`
- `ada-ppc-2026-dc26-s016-sea-qa.json`

HTML folder:
- `ada-ppc-2026-dc26-s016-sea.html`

Markdown folder:
- `ada-ppc-2026-dc26-s016-reference-task-queue.md`
- `ada-ppc-2026-dc26-s016-processing-report.md`

## Publication verification

- Local generation/validation: **PASS**.
- GitHub publication/readback: **PENDING**.

## Lifecycle state

- Promotion gate: **PENDING GitHub readback**.
- Source remains in Active until the whole exact output family is independently verified.
