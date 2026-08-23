# Ross Thamer 2015 — Processing Report

## Source packet
- Primary article: `Diabetes Obesity Metabolism - 2015 - Ross - Efficacy and safety of empagliflozin twice daily versus once daily in patients.pdf` — DOI 10.1111/dom.12469; PMID 25827441; EudraCT 2012-000905-53.
- Supplements: Figure S1, Figure S2, Tables S1–S4, and Appendix S1 (7 DOCX files).

## ATOM
- Publication ID: `daed02b0-d119-4094-80ae-55def32ebadb`
- Atoms: **136**
- Pydantic structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Status: **PASS**
- Counts by kind: `{'adverse_event': 36, 'author_conclusion': 2, 'comparator_description': 1, 'conflict_of_interest': 1, 'eligibility_criterion': 10, 'funding_disclosure': 1, 'intervention_description': 1, 'method': 10, 'outcome_definition': 6, 'population_description': 21, 'qualitative_result': 1, 'quantitative_result': 45, 'study_objective': 1}`

## SEA coverage
- Main figures: 1/1 reconciled.
- Main tables: 1/1 reconciled.
- Supplementary figures: 2/2 reconciled.
- Supplementary tables: 4/4 reconciled.
- Appendix S1: included and reconciled.
- SEA QA: **PASS**.

## References
- 9 numbered references extracted from the primary article into `ross-thamer-2015-references.md`.
- Source citation text was preserved apart from line-break/punctuation normalization; no external bibliographic corrections were added.

## Project-source governance
- Applied governing ATOM sources: `literature.py` (supplied as `literature(1).py`), `literature_atoms.py` (supplied as `literature_atoms(1).py`), and `literature_atom.schema.json`.
- Source gap: `README(2).md` and `example_atom.json`, named by the @ATOM macro as lower-precedence workflow/example sources, were not present in the supplied project-source set or Drive search. No missing study facts were invented to compensate.
- SEA version note: the governing file supplied as `summary-evaluation-appraisal-protocol-v4-compact.md` contains an internal heading that identifies itself as Compact v3. Per project precedence, the supplied v4-designated file was treated as governing; the separate v3 HTML was treated as historical reference.

## Output routing
- JSON outputs → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`
- SEA HTML → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`
- References and processing report → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`
