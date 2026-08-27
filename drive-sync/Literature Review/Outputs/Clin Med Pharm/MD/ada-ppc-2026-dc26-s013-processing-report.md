# Processing report: 13. Older Adults: Standards of Care in Diabetes—2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s013.pdf`  
Drive file ID: `1txft89Vd_bV5-52AG8LpWhPOuATgGZbb`  
DOI: `10.2337/dc26-S013`  
SHA-256: `64a60eae7c82ee650400730247f323f4b4ec36362eacb88889539426cc77eeef`

## Prewalk

- The exact Drive file ID resolves to `dc26s013.pdf`.
- The source remained a direct child of the ADA Active folder during extraction.
- Exact GitHub searches for `dc26s013` and `dc26-s013` returned no section-specific output before this run.
- Historical ADA outputs were consulted only for file-family and reporting conventions. They were not used as completion evidence for Section 13.

## Source map

- Exact title: `13. Older Adults: Standards of Care in Diabetes—2026`.
- Source type: clinical practice guideline / ADA Standards chapter.
- Citation: `Diabetes Care 2026;49(Suppl. 1):S277-S296`.
- PDF pages: 20.
- Substantive content: S277-S292.
- References begin on S292 and continue through S296.
- Recommendations: 25.
- Main figures: 3.
- Main tables: 3.
- Algorithmic workflows: 2, Figures 13.2 and 13.3.
- Numbered references: 194, continuous sequence 1 through 194.

## Reference extraction

- Bibliography entries extracted: 194.
- P0 direct core-topic follow-up: 136.
- P1 high-value supporting evidence: 38.
- P2 contextual or background evidence: 20.
- Bibliography entries were not converted into LiteratureAtoms.
- No external bibliographic correction was performed.

## ATOM

- LiteratureAtoms: 112.
- Shared publication ID: `fde0a237-e86c-5bed-aac7-14b1d1ebcc51`.
- Atom counts by kind: `{"author_conclusion": 38, "limitation": 1, "method": 1, "other": 72}`.
- Semantic extraction runs: `{"ada-ppc-2026-dc26-s013-assessment-v1": 5, "ada-ppc-2026-dc26-s013-cardiovascular-v1": 1, "ada-ppc-2026-dc26-s013-end-of-life-v1": 7, "ada-ppc-2026-dc26-s013-general-v1": 6, "ada-ppc-2026-dc26-s013-hypoglycemia-v1": 2, "ada-ppc-2026-dc26-s013-insulin-simplification-v1": 11, "ada-ppc-2026-dc26-s013-lifestyle-v1": 4, "ada-ppc-2026-dc26-s013-neurocognitive-v1": 4, "ada-ppc-2026-dc26-s013-paltc-v1": 6, "ada-ppc-2026-dc26-s013-pharmacologic-v1": 17, "ada-ppc-2026-dc26-s013-recommendations-v1": 25, "ada-ppc-2026-dc26-s013-screening-v1": 6, "ada-ppc-2026-dc26-s013-simplification-v1": 4, "ada-ppc-2026-dc26-s013-technology-v1": 7, "ada-ppc-2026-dc26-s013-treatment-goals-v1": 6, "ada-ppc-2026-dc26-s013-type1-v1": 1}`.
- Pydantic structural errors: 0.
- JSON Schema errors: 0.
- Sufficiency errors: 0.
- Sufficiency warnings: 0.
- Duplicate atom IDs: 0.
- Duplicate statement-anchor pairs: 0.
- Current ATOM gate: `PASS`.

Guideline boundary: recommendation statements use `author_conclusion` plus `guideline_recommendation` and source-grade tags because the schema has no dedicated guideline recommendation kind. Study findings summarized by the chapter remain secondary reports anchored to this chapter. They are not represented as if the ADA chapter enrolled those populations.

## SEA and reconciliation

- Source type: clinical practice guideline / Standards chapter.
- All 20 PDF pages rendered and visually inspected.
- Recommendations reconciled: 25/25.
- Figures reconciled: 3/3.
- Tables reconciled: 3/3.
- Algorithms/workflows reconciled: 2/2.
- Figure 13.1: 4Ms assessment framework.
- Table 13.1: geriatric syndrome and functional-impairment screening approaches.
- Table 13.2: health-status treatment goals for glycemia, blood pressure, and lipids.
- Figure 13.2: four-step treatment-difficulty, goal-reassessment, simplification, and reassessment workflow.
- Figure 13.3: insulin-simplification algorithm.
- Table 13.3: simplification and deintensification triggers by health status.
- SEA verdict: `Read first`.
- SEA-QA: `PASS`.

## Crosswalk

- All 25 recommendation records link to exact Section 13 atom IDs.
- All six main visual objects link to source-anchored atoms.
- Every atom ID referenced by the crosswalk exists in the validated atom file.
- Recommendation atom IDs are unique.
- Crosswalk integrity gate: `PASS`.

## Extraction limitations and schema gaps

- The LiteratureAtom schema has no dedicated `guideline_recommendation` kind.
- The quantitative-result model is oriented toward primary-study effect structures. Secondary narrative results and thresholds that do not cleanly map to one modeled effect remain `other` atoms with descriptive tags.
- The chapter delegates the full evidence-grading system and guideline-development method to the separate ADA Introduction and Methodology. That document was not part of this exact source packet.
- Cited primary publications were not independently read as part of this exact-section run.
- All model-extracted atoms remain `needs_review` because no independent human reviewer step is represented.
- No external web verification was performed.

## Governing sources

- Structural validation: `literature(1).py`, checked against the current repository `ORACLE/literature.py`.
- Sufficiency validation: `literature_atoms(1).py`, checked against the current repository `ORACLE/literature_atoms.py`.
- Serialization: `literature_atom.schema.json`, checked against the current repository schema.
- Workflow intent: `README(2).md`.
- Example atom: illustrative only.
- SEA: `summary-evaluation-appraisal-protocol-v4-compact.md`.
- Large-source execution: current repository `large-source-ATOM-SEA.md`.
- Historical SEA v3 HTML: reference only.
- Prose control: `unslop.skill.md` from File Library.

Protocol/version note: the project names `summary-evaluation-appraisal-protocol-v4-compact.md` as authoritative, while its internal heading identifies Integrated Compact v3. Project precedence controls and the mismatch is recorded.

## Output family

- `drive-sync/Literature Review/Outputs/Clin Med Pharm/JSON/ada-ppc-2026-dc26-s013-atoms.json`
- `drive-sync/Literature Review/Outputs/Clin Med Pharm/JSON/ada-ppc-2026-dc26-s013-validation.json`
- `drive-sync/Literature Review/Outputs/Clin Med Pharm/JSON/ada-ppc-2026-dc26-s013-coverage.json`
- `drive-sync/Literature Review/Outputs/Clin Med Pharm/JSON/ada-ppc-2026-dc26-s013-crosswalk.json`
- `drive-sync/Literature Review/Outputs/Clin Med Pharm/JSON/ada-ppc-2026-dc26-s013-sea-qa.json`
- `drive-sync/Literature Review/Outputs/Clin Med Pharm/HTML/ada-ppc-2026-dc26-s013-sea.html`
- `drive-sync/Literature Review/Outputs/Clin Med Pharm/MD/ada-ppc-2026-dc26-s013-reference-task-queue.md`
- `drive-sync/Literature Review/Outputs/Clin Med Pharm/MD/ada-ppc-2026-dc26-s013-processing-report.md`

## Publication gate before lifecycle

- Exact source identity: `PASS`.
- Complete exact-section eight-file output family in `cfowla/knowledge`: `PASS`.
- Repository content readback for ATOM, validation, coverage, crosswalk, SEA-QA, SEA, reference queue, and processing report: `PASS`.
- ATOM structural, JSON Schema, and sufficiency validation: `PASS`.
- Recommendation coverage: `PASS` (25/25).
- Figure, table, and workflow reconciliation: `PASS` (3/3 figures, 3/3 tables, 2/2 workflows).
- Reference extraction and exact-section queue: `PASS` (194/194; continuous 1-194).
- Crosswalk consistency: `PASS`.
- SEA-QA: `PASS`.
- Processing-report consistency: `PASS`.
- Lifecycle eligibility before move: `PASS`.

## Lifecycle

- Source Active parent immediately before move: `1j50uC_mGfCpLj6jvR9en2sUilsnTGKLV` (`1 - American Diabetes Association 2026`): `VERIFIED`.
- Destination folder: `1YSKH6Oqj52tYPN402sa9mxs_RFzGhNlG` (`47 - American Diabetes Association 2026`): `VERIFIED`.
- Destination parent: `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT` (`1 - Clinical Medicine & Pharmacy`): `VERIFIED`.
- Processed parent: `1--1k5DCRqVcyFOHEIQynRQJEHIJM8ReQ` (`5 - 90 - Processed`): `VERIFIED`.
- Drive move operation: `PASS`.
- Source parent after move: `1YSKH6Oqj52tYPN402sa9mxs_RFzGhNlG`: `VERIFIED`.
- Destination presence of `dc26s013.pdf`: `PASS`.
- Absence of `dc26s013.pdf` from the Active ADA folder on fresh direct-child inventory: `PASS`.
- Final lifecycle status: `MOVED AND VERIFIED`.

Generated: 2026-08-27T05:31:02.134916Z
