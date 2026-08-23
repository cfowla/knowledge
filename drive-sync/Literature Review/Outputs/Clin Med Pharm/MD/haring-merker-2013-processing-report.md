# Häring Merker 2013 — Processing Report

## Source packet
- Primary article: `3396.pdf` — DOI `10.2337/dc12-2673`; *Diabetes Care* 2013;36:3396–3404.
- Supplement: `dc122673supplementarydata.pdf`.

## ATOM
- Publication ID: `23d03de2-6385-485f-b224-b4b1936add32`
- Atoms: **98**
- Pydantic structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Status: **PASS**
- Counts by kind: `{'adverse_event': 16, 'author_conclusion': 2, 'comparator_description': 1, 'conflict_of_interest': 1, 'eligibility_criterion': 4, 'funding_disclosure': 1, 'intervention_description': 2, 'limitation': 6, 'method': 8, 'outcome_definition': 4, 'population_description': 4, 'qualitative_result': 4, 'quantitative_result': 32, 'study_objective': 1, 'subgroup_result': 12}`

## SEA coverage
- Main figures: **2/2 reconciled**.
- Main tables: **2/2 reconciled**.
- Supplementary figures: **3/3 reconciled**.
- Supplementary tables: **5/5 reconciled**.
- SEA QA: **PASS**.
- Source discrepancy preserved: Supplementary Table 1 states meal-test subset n=125, while listed arm counts total 124 and the main article describes 124.

## References
- **32** numbered references extracted into `haring-merker-2013-references.md`.
- Bibliographic wrapping and typography normalized; no missing citation metadata was invented.

## Project-source governance
- Applied: `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, project large-source ATOM/SEA guidance, and the supplied SEA protocol.
- `example_atom.json` was consulted as illustrative only.
- Source gap: `README(2).md`, named by @ATOM as a lower-precedence workflow source, was not available after exact Google Drive search. No study facts were invented to compensate.
- SEA version note: the governing file is named `summary-evaluation-appraisal-protocol-v4-compact.md`; any internal version-heading inconsistency was resolved in favor of the filename/project precedence. Historical v3 HTML remained reference-only.

## Output routing
- JSON outputs → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`
- SEA HTML → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`
- References and processing report → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`
