# Processing report: 12. Retinopathy, Neuropathy, and Foot Care: Standards of Care in Diabetes—2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s012.pdf`  
Drive file ID: `1LaVs5MQ5VFrLP1Ja6K_BgdNLvvWx6Qre`  
DOI: `10.2337/dc26-S012`  
SHA-256: `8f9779e8dfacc691bd78d15d65f5d70fa9fb92e1db204cad5f0174497b475bad`

## Prewalk

- Exact source identity matched the expected Drive ID and was verified as a direct child of the Active ADA folder.
- Repository searches for `dc26s012` and `dc26-s012` found no exact-section artifact family before generation.
- Historical ADA outputs were used only for file-layout and reporting conventions.

## ATOM

- LiteratureAtoms: 105
- Shared publication ID: `e89be5b9-45f6-5394-b9da-eea5ab6a00e9`
- Atom counts by kind: `{"author_conclusion": 40, "limitation": 14, "other": 38, "quantitative_result": 13}`
- Semantic batches: `{"ada-ppc-2026-dc26-s012-evidence-v1": 13, "ada-ppc-2026-dc26-s012-foot-care-v1": 27, "ada-ppc-2026-dc26-s012-neuropathy-v1": 24, "ada-ppc-2026-dc26-s012-retinopathy-v1": 37, "ada-ppc-2026-dc26-s012-table-12-1-v1": 4}`
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate statement-anchor pairs: 0

Recommendations are represented as ADA panel statements using `author_conclusion` plus `guideline_recommendation` tags. Quantitative findings attributed to underlying studies are tagged `secondary_reported_result` and remain anchored to this chapter; the Standards chapter is not represented as if it enrolled those study populations.

## SEA and reconciliation

- Source type: clinical practice guideline / Standards chapter
- Substantive coverage: S261–S272 before References
- Figures reconciled: 0/0
- Tables reconciled: 1/1 (Table 12.1)
- Formal recommendations: 12.1–12.32 (32/32)
- Bibliography entries: 169/169
- SEA QA: PASS
- Verdict: `Read first`

## Reference task queue

- Bibliography entries extracted: 169
- P0: 129
- P1: 22
- P2: 18
- Bibliography entries were not atomized.

## Extraction limitations and schema gaps

- The LiteratureAtom schema has no dedicated `guideline_recommendation` atom kind; formal recommendations use `author_conclusion` with descriptive tags.
- Recommendation evidence grades are preserved in tags rather than a dedicated typed field.
- The full ADA guideline-development method and evidence-grade definitions are in the separate Introduction and Methodology and were not part of this exact input.
- All atoms remain `needs_review` because this run is not an independent human verification step.
- No external current-practice or regulatory verification was performed because `@VERIFY` was not activated.

## Protocol version note

The project file is named `summary-evaluation-appraisal-protocol-v4-compact.md`, while its internal heading identifies Integrated Compact v3. The v4-named project source was treated as governing; the naming mismatch was recorded rather than silently reconciled.

## Output family

JSON folder:
- `ada-ppc-2026-dc26-s012-atoms.json`
- `ada-ppc-2026-dc26-s012-validation.json`
- `ada-ppc-2026-dc26-s012-coverage.json`
- `ada-ppc-2026-dc26-s012-crosswalk.json`
- `ada-ppc-2026-dc26-s012-sea-qa.json`

HTML folder:
- `ada-ppc-2026-dc26-s012-sea.html`

Markdown folder:
- `ada-ppc-2026-dc26-s012-reference-task-queue.md`
- `ada-ppc-2026-dc26-s012-processing-report.md`

## Lifecycle state

- Pre-promotion state: **NOT YET PROMOTED**.
- Promotion is gated on successful GitHub write + independent readback of the complete exact output family, source-identity check, passing ATOM validation, complete coverage/reconciliation, passing SEA-QA, and bibliography verification.
