# jco-40-282 processing report

## Activated macros

- @ATOM
- @SEA

## Source

- Title: Adjuvant Palbociclib for Early Breast Cancer: The PALLAS Trial Results (ABCSG-42/AFT-05/BIG-14-03)
- DOI: 10.1200/JCO.21.02554
- Trial: NCT02513394
- Raw Drive source: `jco-40-282.pdf`
- PDF pages: 25
- SHA-256: `38002cfaace89009b6aaece6d789e3c1df1985b3904f273e28aea0f854b332f2`
- Substantive article: PDF pages 1-12, printed pages 282-293
- Disclosure appendix: PDF pages 13-14
- Investigator and site roster: PDF pages 15-25

## ATOM status

- Publication ID: `bb7ed778-af38-57ab-b3cd-837e87caccc7`
- Atoms: 76
- By kind: `{"adverse_event": 10, "author_conclusion": 3, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 3, "exposure_description": 1, "funding_disclosure": 1, "intervention_description": 1, "method": 10, "outcome_definition": 5, "population_description": 6, "qualitative_result": 1, "quantitative_result": 15, "study_objective": 1, "subgroup_result": 16}`
- Semantic batches: `{"jco-40-282-design-v1": 24, "jco-40-282-efficacy-v1": 28, "jco-40-282-interpretation-v1": 3, "jco-40-282-population-v1": 7, "jco-40-282-safety-exposure-v1": 14}`
- Pydantic structural validation: PASS
- JSON Schema validation: PASS
- Sufficiency validation: PASS
- Structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Exact duplicate canonical statements: 0

The extraction covers trial design, eligibility, intervention and comparator, endpoints, ITT population, primary and secondary efficacy, all Figure 3 subgroup hazard ratios, Table 2 event categories, treatment exposure, major safety results, disclosures, data sharing, and author conclusions. Secondary-study findings discussed by the authors were not represented as if PALLAS generated them.

## SEA status

- Main article pages inspected: 12/12
- Disclosure pages inspected: 2/2
- Main figures reconciled: 3/3
- Main tables reconciled: 3/3
- Appendix site roster: omitted from evidence condensation with reason
- Self-contained HTML: PASS
- Figure crops embedded: 3
- Internal chat citation syntax: absent
- Placeholder scan: PASS

Verdict: Read first for the palbociclib adjuvant question. The final PALLAS analysis is a strong negative randomized trial. It found no iDFS benefit and documented substantial treatment discontinuation and hematologic toxicity.

## Reference task queue

- Numbered references extracted: 46/46
- Source numbering preserved
- External bibliographic correction: not performed
- Bibliography atomized: no

## Source limitations

The supplied PDF does not contain the online Data Supplement, protocol, or statistical analysis plan referenced by the article. Those materials were not silently reconstructed.

## Governing sources applied

ATOM precedence: `literature(1).py` -> `literature_atoms(1).py` -> `literature_atom.schema.json` -> `README(2).md` -> `example_atom(1).json`. SEA used `summary-evaluation-appraisal-protocol-v4-compact.md`. Large-source workflow and `unslop.skill.md` were applied as supporting controls.

## Output files

- `jco-40-282-atoms.json`
- `jco-40-282-validation.json`
- `jco-40-282-sea.html`
- `jco-40-282-references.md`
- `jco-40-282-processing-report.md`
