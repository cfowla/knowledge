# Processing Report - VASCULAR COMPLICATIONS IN PEDIATRIC PANCREATITIS: A CASE SERIES

## Activated macros

`@ATOM + @SEA`

## Source

- Google Drive folder: `23 - nihms-1718801` under `3 / 2 / 1`
- Retrieved raw document: `nihms-1718801.pdf`
- Source type: retrospective multicenter registry case series
- Journal: J Pediatr Gastroenterol Nutr. 2021;73(4):e94-e97
- DOI: `10.1097/MPG.0000000000003218`
- SHA-256: `01e6fc3b29d770c386290f086bdb8114574fe93c4d7d71b7a3be5f14cbb046ec`
- PDF pages rendered and inspected: 10/10

## ATOM

- Atom count: **56**
- Counts by kind: `{"adverse_event": 1, "author_conclusion": 5, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 1, "funding_disclosure": 1, "intervention_description": 1, "limitation": 5, "method": 4, "other": 11, "outcome_definition": 2, "population_description": 7, "qualitative_result": 1, "quantitative_result": 14, "study_objective": 1}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Review status: all atoms `needs_review`

## SEA coverage

- Main-text figures: **0**
- Main-text tables: **2/2 reconciled**
- Supplementary material/Table S1: referenced in the manuscript but **not present in the retrieved Drive folder**; not reconstructed from external sources.
- Final verdict: **Skim deeply** for pediatric vascular-complication frequency/case patterns; **do not use as a stand-alone anticoagulation decision study**.

## Source-integrity findings

1. The manuscript reports 5/410 (1.2%) total vascular complications: 4 venous thromboses plus 1 left gastric artery pseudoaneurysm. The “What is New” box calls 1.2% the incidence of PSMVT, which does not strictly match the four venous events. The wording was preserved and flagged.
2. The abstract reports 1 recanalization among 2 venous-thrombosis patients without anticoagulation. The Results text says 1 of the other 3 non-anticoagulated patients recanalized, apparently counting the pseudoaneurysm case; Table 2 then labels that case “did not re-canalize.” No silent reconciliation was applied.

## Reference task queue

- Source bibliography entries: **20**
- Output: `dike-2021-vascular-complications-pediatric-pancreatitis-references-task-queue.md`
- PMIDs are included only when printed in the source. No missing bibliographic identifiers were backfilled.

## Governing-source notes

- ATOM precedence applied: `literature(1).py` → `literature_atoms(1).py` → `literature_atom.schema.json` → `README(2).md` → `example_atom(1).json`.
- SEA governing file applied: `summary-evaluation-appraisal-protocol-v4-compact.md`.
- The SEA governing filename says v4, while its internal heading says “Integrated Compact v3.” Per project precedence, the supplied v4-named file governed; the version-label conflict is reported rather than repaired.
- `large-source-ATOM-SEA.md` was inspected. Semantic batching was not required for this 10-page source; the entire main manuscript was inspected directly, with the two tables handled as discrete visual objects.
- `unslop.skill.md` was searched in the File Library and Google Drive `GitHub Sync/SKILLS`, but no source file was available. No undocumented writing rules were inferred from prior outputs that merely mention it.

## Output files

### JSON
- `dike-2021-vascular-complications-pediatric-pancreatitis-atoms.json`
- `dike-2021-vascular-complications-pediatric-pancreatitis-validation.json`
- `dike-2021-vascular-complications-pediatric-pancreatitis-coverage.json`

### HTML
- `dike-2021-vascular-complications-pediatric-pancreatitis-sea.html`

### Markdown
- `dike-2021-vascular-complications-pediatric-pancreatitis-references-task-queue.md`
- `dike-2021-vascular-complications-pediatric-pancreatitis-processing-report.md`
