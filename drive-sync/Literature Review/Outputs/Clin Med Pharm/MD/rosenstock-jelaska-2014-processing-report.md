# Rosenstock Jelaska 2014 — Processing Report

## Source packet
- Primary article: `1815.pdf` — DOI 10.2337/dc13-3055; PMID 24929430.
- Supplement: `dc133055supplementarydata.pdf`.
- Ancillary presentation: `july_2014_dc13_3055.ppt` — inspected for reconciliation only; not treated as a separate evidentiary publication.

## ATOM
- Publication ID: `2bf9b9a4-1423-430a-932d-1ba7478da9a7`
- Atoms: **87**
- Pydantic structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Status: **PASS**
- Counts by kind: `{'adverse_event': 24, 'author_conclusion': 2, 'comparator_description': 1, 'conflict_of_interest': 1, 'eligibility_criterion': 6, 'funding_disclosure': 1, 'intervention_description': 2, 'limitation': 2, 'method': 14, 'outcome_definition': 6, 'population_description': 4, 'qualitative_result': 2, 'quantitative_result': 21, 'study_objective': 1}`

## SEA coverage
- Main figures: 2/2 reconciled.
- Main tables: 2/2 reconciled.
- Supplementary figures: 3/3 reconciled.
- Supplementary tables: 3/3 reconciled.
- SEA QA: **PASS**.

## References
- 23 numbered references extracted from the primary article into `rosenstock-jelaska-2014-references.md`.
- Citation punctuation/typography normalized from the source; no external metadata was added.

## Project-source governance
- Applied: `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, and the supplied SEA protocol.
- Source gap: `README(2).md` and `example_atom.json`, named by the @ATOM macro as lower-precedence workflow/example sources, were not present in the supplied project-source set. No missing study facts were invented to compensate.
- SEA version note: the governing file supplied as `summary-evaluation-appraisal-protocol-v4-compact.md` contains an internal heading that identifies itself as Compact v3. Per project precedence, the supplied v4-designated file was treated as governing; the separate v3 HTML was treated as historical reference.

## Output routing
- JSON outputs → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`
- SEA HTML → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`
- References and processing report → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`
