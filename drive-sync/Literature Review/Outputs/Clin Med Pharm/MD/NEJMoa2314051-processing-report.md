# NEJMoa2314051 processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Primary article: `NEJMoa2314051.pdf`, 12 pages, SHA-256 `69df44d3e49445d5533f18c9e509703c9859367a4f2e6f4ab59a8febb60e411f`
- Supplementary appendix: `nejmoa2314051_appendix.pdf`, 31 pages, SHA-256 `41077e432dd6a2b2cb2037c361f0e2a884bb723fc3e16828c9b7ff74a37a7836`
- Protocol and TSAP packet: `nejmoa2314051_protocol.pdf`, 239 pages, SHA-256 `ec5e67b6c6a7ccf6ac9d79102501acb79b400a96e28a586e21d065977dbdd229`
- Title: *Empagliflozin after Acute Myocardial Infarction*
- Trial: EMPACT-MI
- Citation: N Engl J Med. 2024;390:1455-1466.
- DOI: `10.1056/NEJMoa2314051`
- ClinicalTrials.gov: `NCT04509674`
- Shared publication ID: `53659615-5b7d-5d7f-b1be-239e15a0d433`

## ATOM result

- Total LiteratureAtoms: **64**
- Atom kinds: `{"adverse_event": 11, "author_conclusion": 3, "comparator_description": 1, "data_availability": 1, "eligibility_criterion": 2, "funding_disclosure": 1, "intervention_description": 1, "limitation": 5, "method": 11, "outcome_definition": 3, "population_description": 8, "qualitative_result": 2, "quantitative_result": 14, "study_objective": 1}`
- Semantic batches: `{"nejmoa2314051-design-v1": 19, "nejmoa2314051-efficacy-v1": 16, "nejmoa2314051-interpretation-v1": 10, "nejmoa2314051-population-v1": 8, "nejmoa2314051-safety-v1": 11}`
- Local reconstructed Pydantic validation: **PASS**
- Local generated JSON Schema validation: **PASS**
- Local sufficiency check: **PASS**
- Structural errors: **0**
- Serialization errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

The primary confirmatory result is preserved as negative: first HHF or all-cause death HR 0.90, 95% CI 0.76-1.06, P=0.21. The first-HHF and total-HHF findings are tagged as exploratory and are not promoted to a positive trial conclusion.

## SEA result

The primary article, all five main figures and tables, six supplementary figures, seven supplementary tables, protocol amendment history, and final TSAP were reconciled. The HTML separates reported trial findings from appraisal. No protocol-specific numeric SEA score was assigned because the exact v4 scoring protocol was not directly retrievable.

A source-integrity issue was retained in Supplementary Table S7. The ICD/CRT row reports HR 0.80 with 95% CI 1.58-1.10. The interval is internally impossible. It was not silently repaired and was not converted into a quantitative LiteratureAtom.

## References

The primary article contains **28** bibliography entries. They were exported to `NEJMoa2314051-references.md`. The protocol and TSAP bibliographies were treated as supporting provenance and were not merged into the requested article reference list.

## Governing-source execution boundary

The named governing ATOM files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom.json`, plus `summary-evaluation-appraisal-protocol-v4-compact.md`, were searched but were not directly retrievable in this session. `large-source-ATOM-SEA.md` and `unslop.skill.md` were available and applied. Validation therefore uses a strict local Pydantic contract and generated JSON Schema reconstructed from recent validated project outputs. This report does not claim execution of unavailable authoritative project code.

## QA

- Shared publication identity: **PASS**
- Unique atom IDs: **PASS**
- Duplicate statement plus anchor pairs: **0**
- HTML parse: **PASS**
- Internal HTML anchor targets: **PASS**
- Internal ChatGPT or file citation syntax in HTML: **absent**
- TODO or placeholder text: **absent**
- External web verification: **not performed**

## Output files

- `NEJMoa2314051-atoms.json`
- `NEJMoa2314051-validation.json`
- `NEJMoa2314051-coverage.json`
- `NEJMoa2314051-sea.html`
- `NEJMoa2314051-references.md`
- `NEJMoa2314051-processing-report.md`
