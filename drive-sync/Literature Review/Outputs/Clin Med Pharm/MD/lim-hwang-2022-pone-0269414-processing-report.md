# Lim et al. 2022 processing report

## Source

- Title: Comparison of cardiovascular and renal outcomes between dapagliflozin and empagliflozin in patients with type 2 diabetes without prior cardiovascular or renal disease
- DOI: 10.1371/journal.pone.0269414
- PMID: 36251654
- Main PDF SHA-256: `4eac4ddedc3b4d59a3bf3c29bccbd13d69fb9af51de02b29a5d7a5fce58b60d6`
- S1 Appendix SHA-256: `14d810bffa5bf8ee2f612b563af275869fe2acd2f6c8775d9215f176ead80531`

## ATOM

- LiteratureAtoms: 87
- Pydantic structural validation: PASS
- JSON Schema validation: PASS
- Sufficiency validation: PASS
- Sufficiency warnings: 0
- Exact duplicate canonical statements: 0
- Publication identity: one shared publication ID across all atoms

Atom counts by kind: `{"author_conclusion": 3, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 7, "funding_disclosure": 1, "intervention_description": 2, "limitation": 3, "method": 9, "outcome_definition": 5, "population_description": 10, "qualitative_result": 5, "quantitative_result": 38, "study_objective": 1}`

## Coverage

- Main figures reconciled: 4 of 4
- Main tables reconciled: 4 of 4
- S1 Appendix: 3,684 patient rows and 50 columns; aggregate arm sizes and Table 2 event counts reconciled
- Bibliography pages: excluded from atomization and extracted as a 38-item reference task queue

## SEA

- Self-contained HTML: PASS
- TOC anchor check: PASS
- Internal citation marker scan: PASS
- Placeholder and planning-language scan: PASS
- Verdict: Read soon
- Main appraisal limit: direct dapagliflozin versus empagliflozin estimates are too imprecise to establish equivalence or noninferiority

## Governing sources

ATOM used `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, and `README(2).md`, with `example_atom(1).json` as an illustration only. Large-source handling followed `large-source-ATOM-SEA.md`. SEA used `summary-evaluation-appraisal-protocol-v4-compact.md`; the v3 HTML was historical reference only. `unslop.skill.md` was applied to prose artifacts.

No external verification was performed because `@VERIFY` was not activated.

## Output files

- `lim-hwang-2022-pone-0269414-atoms.json`
- `lim-hwang-2022-pone-0269414-validation.json`
- `lim-hwang-2022-pone-0269414-coverage.json`
- `lim-hwang-2022-pone-0269414-crosswalk.json`
- `lim-hwang-2022-pone-0269414-sea.html`
- `lim-hwang-2022-pone-0269414-sea-qa.json`
- `lim-hwang-2022-pone-0269414-references.md`
- `lim-hwang-2022-pone-0269414-processing-report.md`
