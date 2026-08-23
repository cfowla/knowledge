# Teo Ting 2022 — Processing Report

## Source packet
- Primary article: `Effects_of_SodiumGlucose_Cotr.pdf` — DOI `10.1007/s40256-022-00528-7`; *American Journal of Cardiovascular Drugs* 2022;22:299–323.
- Supplementary material: referenced by the article but **not present** in the source folder.

## ATOM
- Publication ID: `3fadc1cb-1c27-51dd-859f-de977ab10e8b`
- Atoms: **71**
- Pydantic structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Status: **PASS**
- Counts by kind: `{'adverse_event': 17, 'author_conclusion': 2, 'comparator_description': 1, 'conflict_of_interest': 1, 'data_availability': 1, 'eligibility_criterion': 1, 'funding_disclosure': 1, 'intervention_description': 1, 'limitation': 5, 'method': 8, 'outcome_definition': 4, 'population_description': 1, 'qualitative_result': 4, 'quantitative_result': 23, 'study_objective': 1}`
- Preserved source discrepancy: abstract HbA1c class difference **0.16% (95% CI 0.06–0.26)** versus Results/Table 2 **0.21% (95% CI 0.07–0.35)**.

## SEA coverage
- Main figures: **5/5 reconciled**.
- Main tables: **2/2 reconciled**.
- Supplementary Tables 1–4 and Supplementary Figures 1–4: referenced but unavailable in the provided folder.
- SEA QA: **PASS**.

## References
- **42** numbered references extracted into `teo-ting-2022-references.md`.
- Line wrapping normalized; no missing citation metadata was invented.

## Project-source governance
- Applied: `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, project large-source ATOM/SEA guidance, and the supplied SEA protocol.
- Source gap: `README(2).md` and `example_atom.json`, named by @ATOM as lower-precedence workflow/illustrative sources, were not available in the project attachments or exact Google Drive searches. No study facts were invented to compensate.
- SEA version note: the governing file is named `summary-evaluation-appraisal-protocol-v4-compact.md`; its internal heading says “Integrated Compact v3.” Project/file precedence was followed, with historical v3 HTML treated as reference-only.

## Output routing
- JSON outputs → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`
- SEA HTML → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`
- References and processing report → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`
