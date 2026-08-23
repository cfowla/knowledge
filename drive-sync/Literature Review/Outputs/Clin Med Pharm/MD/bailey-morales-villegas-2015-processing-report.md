# Bailey Morales Villegas 2015 — Processing Report

## Source packet
- Primary article: `Diabetic Medicine - 2014 - Bailey - Efficacy and safety of dapagliflozin monotherapy in people with Type 2 diabetes a.pdf` — DOI 10.1111/dme.12624; PMID 25381876.
- No supplementary file was present in the source folder.

## ATOM
- Publication ID: `32dce92d-77f7-4ba9-9f48-611607f2a5b5`
- Atoms: **109**
- Pydantic structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Status: **PASS**
- Counts by kind: `{'adverse_event': 26, 'author_conclusion': 1, 'comparator_description': 1, 'conflict_of_interest': 1, 'eligibility_criterion': 4, 'funding_disclosure': 1, 'intervention_description': 3, 'limitation': 4, 'method': 10, 'outcome_definition': 8, 'population_description': 6, 'qualitative_result': 5, 'quantitative_result': 38, 'study_objective': 1}`

## SEA coverage
- Main figures: 2/2 reconciled.
- Main tables: 4/4 reconciled.
- Supplements: none present in the source folder.
- SEA QA: **PASS**.

## References
- 34 numbered references extracted from the primary article into `bailey-morales-villegas-2015-references.md`.
- Citation line wrapping and minor punctuation were normalized from the source; no external bibliographic metadata was added.

## Project-source governance
- Applied: `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, and the supplied SEA protocol.
- Source gap: `README(2).md` and `example_atom.json`, named by the @ATOM macro as lower-precedence workflow/example sources, were not present in the available project-source set. No missing study facts were invented to compensate.
- SEA version note: the governing file supplied as `summary-evaluation-appraisal-protocol-v4-compact.md` internally identifies the protocol as Compact v3. Per project precedence, the v4-designated file was treated as governing and the separate v3 HTML as historical reference.

## Output routing
- JSON outputs → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`
- SEA HTML → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`
- References and processing report → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`
