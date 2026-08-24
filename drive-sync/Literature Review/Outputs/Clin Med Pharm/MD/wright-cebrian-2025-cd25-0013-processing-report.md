# Processing report: A Primary Care Guide to the Screening and Pharmacologic Management of Chronic Kidney Disease in People Living With Type 2 Diabetes

## Activated macros

@ATOM + @SEA

## Source packet

- Main article: `diaclincd250013.pdf`
- Journal: Clinical Diabetes 2025;43(4):531-544
- PMID: `41140732`
- PMCID: `PMC12549410`
- DOI: `10.2337/cd25-0013`
- Source pages reviewed: 15 of 15 PDF pages, including the front infographic, 14 article pages, five numbered figures, Table 1, funding/conflict disclosures, and bibliography
- Source SHA256: `5b93fb9f6b57c30cc0efb01092ba355b21435f0f6667d0e62c4844111636d103`
- Publication ID: `f1473c86-ee35-5489-81d7-6b465d3ecf8d`
- Online supplement: cited at `10.2337/figshare.29260568` but not present in the supplied Drive packet

## ATOM status

- Atoms: **112**
- By kind: `{"author_conclusion": 35, "conflict_of_interest": 3, "data_availability": 1, "funding_disclosure": 2, "intervention_description": 4, "limitation": 4, "method": 4, "other": 32, "outcome_definition": 2, "population_description": 1, "qualitative_result": 1, "quantitative_result": 22, "study_objective": 1}`
- Pydantic structural validation using `literature(1).py`: **PASS**
- JSON Schema validation using `literature_atom.schema.json`: **PASS**
- Sufficiency validation using `literature_atoms(1).py`: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Unique atom IDs: **PASS**
- Shared publication ID: **PASS**
- Exact duplicate statement and anchor pairs: **0**

All model-extracted atoms remain `needs_review`. No human verification status was invented. Because this source is a clinical review and expert synthesis, trial results are serialized as this review's secondary reports and tagged `secondary_reported_result`; they are not represented as if Wright et al. enrolled those trial populations.

## SEA status

The full article and all five numbered figures plus Table 1 were reconciled before appraisal. The front-page infographic was treated as supporting front matter. The absent online supplement was recorded rather than reconstructed. Final SEA scoring occurred after source extraction and visual reconciliation. Mechanical HTML QA status: **PASS**.

SEA verdict: **Read first** as an implementation guide. Do not use the article as a stand-alone guideline, current drug-label authority, or direct empagliflozin-versus-dapagliflozin comparative-effectiveness source.

## Source-integrity and currency findings

1. Figure 1 uses `mg/mmol` around a sentence that prints the UACR threshold as `20 mg/mol`; this unit difference was preserved and flagged.
2. The finerenone prose gives 10 mg once daily at eGFR `>25 to <=60` and 20 mg at `>=60`, creating overlap at exactly 60. Figure 5 instead gives 10 mg for `>25 to <60` and 20 mg for `>=60`. No boundary was silently repaired.
3. Figure 5 displays eGFR `>=20` together with albuminuria `>=200 mg/g` for the SGLT2 inhibitor branch, while surrounding prose recommends an SGLT2 inhibitor for CKD and T2D at eGFR `>=20` without requiring that albuminuria threshold. This implementation ambiguity was retained.
4. The source's Figure 4 GLP-1 receptor agonist suicidality caution is no longer current. FDA's 13 January 2026 review found no increased suicidal-ideation or behavior risk and requested removal of the warning from affected labels. This was treated as external currency verification, not as a correction to the source atom.
5. The 2026 ADA CKD Standards continue the eGFR `>=20` SGLT2 recommendation and now provide a specific option to consider simultaneous SGLT2 inhibitor plus finerenone initiation in selected adults on RAS inhibition.

## Reference task queue

- References extracted: **80**
- Bibliography order and source spelling preserved
- Bibliography atomized: **No**
- Output: `wright-cebrian-2025-cd25-0013-reference-task-queue.md`

## Governing sources applied

ATOM precedence:
1. `literature(1).py`
2. `literature_atoms(1).py`
3. `literature_atom.schema.json`
4. `README(2).md`
5. `example_atom(1).json`

SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing protocol. The v3 HTML was historical reference only. The large-source workflow was consulted; the source was judged suitable for one complete pass with separate bibliography extraction. `unslop.skill.md` was applied to generated prose.

The governing SEA filename says v4 while its internal heading says `Integrated Compact v3`. The v4-named file governed this run, and the label conflict was not rewritten.

## Output files

### JSON

- `wright-cebrian-2025-cd25-0013-atoms.json`
- `wright-cebrian-2025-cd25-0013-validation.json`
- `wright-cebrian-2025-cd25-0013-coverage.json`
- `wright-cebrian-2025-cd25-0013-crosswalk.json`
- `wright-cebrian-2025-cd25-0013-sea-qa.json`

### HTML

- `wright-cebrian-2025-cd25-0013-sea.html`

### Markdown

- `wright-cebrian-2025-cd25-0013-reference-task-queue.md`
- `wright-cebrian-2025-cd25-0013-processing-report.md`

## Google Drive destinations

- JSON: `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/JSON/`
- HTML: `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/HTML/`
- Markdown: `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/MD/`

## Drive/state completion

- Source packet `20 - Wright Cebrian 2025` was moved from `10 - Active Literature` to `90 - Processed / Clinical Medicine & Pharmacy` only after the ATOM, validation, coverage, crosswalk, SEA, SEA-QA, and reference-task artifacts were saved.
- The SGLT2 parent task-list item for the Wright/Cebrian guide was changed from unchecked to checked. The maintained item-level state after this completion is **92 complete / 31 open**.
- `TBR - Current Task Queue` was updated from its immediately prior live snapshot of 16 active numbered source folders and 59 processed numbered source folders to 15 active and 60 processed, preserving concurrent task updates rather than restoring the older snapshot seen at the start of this run.
- The source PDF remains unchanged in the processed packet; SHA-256: `5b93fb9f6b57c30cc0efb01092ba355b21435f0f6667d0e62c4844111636d103`.

