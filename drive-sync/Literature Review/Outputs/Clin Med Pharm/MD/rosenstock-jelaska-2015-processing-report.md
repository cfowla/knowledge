# Processing report: Rosenstock Jelaska 2015

Activated macros: `@ATOM` + `@SEA`

## Source packet

- Primary: `DOM-17-936.pdf`
- Supplement: `DOM-17-936-s001.docx`
- Title: Impact of empagliflozin added on to basal insulin in type 2 diabetes inadequately controlled on basal insulin: a 78-week randomized, double-blind, placebo-controlled trial
- DOI: `10.1111/dom.12503`
- PMID: `26040302`
- Trial registration: `NCT01011868`
- Primary SHA-256: `67a914ced6084afd7ab2ccb7d82bb07f682bbfa4f73ba11a59e99b7483413683`
- Supplement SHA-256: `328b68a1c72803603b7a9b33910fa8ea2678e5730897d3ce7a7d83507217e604`

## ATOM result

- Publication ID: `f3a41186-8a96-578c-b212-1e543293242a`
- LiteratureAtoms: **101**
- Counts by kind: `{"adverse_event": 14, "author_conclusion": 2, "comparator_description": 1, "conflict_of_interest": 2, "eligibility_criterion": 8, "funding_disclosure": 1, "intervention_description": 2, "limitation": 4, "method": 9, "outcome_definition": 11, "population_description": 10, "qualitative_result": 1, "quantitative_result": 35, "study_objective": 1}`
- Semantic batches: `{"rosenstock-jelaska-2015-design-v1": 32, "rosenstock-jelaska-2015-efficacy-v1": 26, "rosenstock-jelaska-2015-interpretation-v1": 9, "rosenstock-jelaska-2015-population-v1": 10, "rosenstock-jelaska-2015-safety-v1": 24}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Unique atom IDs: **PASS**
- One shared publication ID: **PASS**

## SEA result

Coverage reconciled all source visuals used for interpretation:

- 2/2 main figures
- 2/2 main tables
- 1/1 supplementary figure
- 4/4 supplementary tables

The SEA appraisal was scored after whole-source extraction and visual reconciliation. It separates trial findings from appraisal and does not treat this study as a head-to-head empagliflozin versus dapagliflozin comparison or as cardiovascular or kidney outcome evidence.

SEA mechanical QA: **PASSED**

## References

The Markdown reference artifact contains **39/39** numbered references from the article bibliography. Printed numbering is preserved. Bibliographic entries were not atomized and no external bibliography correction was used.

## Governing-source execution

The supplied `literature.py` model, `literature_atoms.py` sufficiency validator, and `literature_atom.schema.json` serialization contract were executed directly. The supplied `summary-evaluation-appraisal-protocol-v4-compact.md` and `large-source-ATOM-SEA.md` were applied. `unslop.skill.md` was retrieved from the File Library and applied to prose artifacts.

`README(2).md` and `example_atom.json` were not available in the current project attachments or File Library search. They rank below the executed ATOM model, sufficiency validator, and serialization schema, so their absence did not block validation. No external web verification was performed.

## Output routing

JSON to `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/JSON/`:

- `rosenstock-jelaska-2015-atoms.json`
- `rosenstock-jelaska-2015-validation.json`
- `rosenstock-jelaska-2015-coverage.json`
- `rosenstock-jelaska-2015-sea-qa.json`

HTML to `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/HTML/`:

- `rosenstock-jelaska-2015-sea.html`

Markdown to `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/MD/`:

- `rosenstock-jelaska-2015-references.md`
- `rosenstock-jelaska-2015-processing-report.md`
