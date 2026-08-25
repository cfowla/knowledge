# Processing report

## Source

- Title: New Delhi metallo-β-lactamase-1 in Enterobacteriaceae: emerging resistance
- Authors: Dylan R. Pillai, Allison McGeer, Donald E. Low
- Source type: narrative review with targeted literature search
- Publication: CMAJ 2011;183(1):59-64
- DOI: 10.1503/cmaj.101487
- Retrieved file: 1830059.pdf
- SHA-256: 88ca212b1108b9f622fdea52f35751adbfa112b4b5e172f2bc89d186d43dc168

## ATOM

- Atoms: 40
- Counts by kind: {"author_conclusion": 2, "conflict_of_interest": 1, "intervention_description": 1, "limitation": 2, "method": 3, "other": 5, "qualitative_result": 8, "quantitative_result": 18}
- Pydantic structural validation: PASS
- JSON Schema validation: PASS
- Sufficiency validation: PASS
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Shared publication_id: PASS
- Unique atom_id values: PASS

This is a secondary narrative review, not primary literature. Findings attributed to cited studies remain anchored to the review and carry `secondary_reported_result` tags. The bibliography was not atomized.

## SEA coverage

- Source pages inspected: 6/6
- Main-text tables: 1/1 reconciled
- Main-text figures: 2/2 reconciled with embedded crops and structured interpretation
- Boxed workflow/guidance content: Box 1 reconciled
- Supplement: none present
- Final verdict: Skim deeply for early NDM-1 history, mechanism, epidemiology, and detection logic. Do not use the 2011 treatment section as current therapeutic guidance.

## Current-practice verification

The SEA protocol requires currency checking for clinical practice. Current official sources were checked even though `@VERIFY` was not activated.

- IDSA 2026 AMR guidance now prefers aztreonam-avibactam or cefiderocol for invasive NDM-producing Enterobacterales; ceftazidime-avibactam plus aztreonam is an alternative if aztreonam-avibactam is unavailable.
- CDC 2026 surveillance reported blaNDM in 5.4% of sampled carbapenemase-producing CRE isolates in 2016 and 39.8% in 2023, showing that NDM is no longer adequately framed as mainly an imported South Asia-associated problem.

## Reference task queue

- Source bibliography entries: 33
- Output: `pillai-mcgeer-low-2011-cmaj101487-references-task-queue.md`
- Source order preserved
- No external bibliographic backfilling

## Governing sources

ATOM precedence applied: `literature(1).py` -> `literature_atoms(1).py` -> `literature_atom.schema.json` -> `README(2).md` -> `example_atom(1).json`.

SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing protocol. The file is named v4, while its internal heading says "Integrated Compact v3." The filename-level v4 source governed, and the version-label conflict is reported rather than repaired.

`large-source-ATOM-SEA.md` was inspected. Semantic batching was not needed for this six-page review. `unslop.skill.md` was retrieved from Google Drive and applied to prose artifacts.

## Output files

### JSON
- `pillai-mcgeer-low-2011-cmaj101487-atoms.json`
- `pillai-mcgeer-low-2011-cmaj101487-validation.json`
- `pillai-mcgeer-low-2011-cmaj101487-coverage.json`

### HTML
- `pillai-mcgeer-low-2011-cmaj101487-sea.html`

### Markdown
- `pillai-mcgeer-low-2011-cmaj101487-references-task-queue.md`
- `pillai-mcgeer-low-2011-cmaj101487-processing-report.md`

## Intended Google Drive destinations

- JSON files: `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/JSON/`
- SEA HTML: `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/HTML/`
- Markdown files: `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/MD/`
