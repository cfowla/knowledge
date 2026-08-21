# ehad195 processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Main source: `ehad195.pdf`
- Supporting evidence tables: `ehad195_evidence_tables.docx`
- Declaration-of-interest supplement: `doi_summary_2023_fu_2021_hf_10-07-23.pdf`
- Title: *2023 Focused Update of the 2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure*
- Citation: European Heart Journal. 2023;44:3627-3639.
- DOI: `10.1093/eurheartj/ehad195`
- Shared publication ID: `2f91337d-a06f-55ab-80ee-c7db81988a88`

## ATOM result

- Total LiteratureAtoms: **47**
- Atom kinds: `{'author_conclusion': 4, 'conflict_of_interest': 1, 'data_availability': 1, 'funding_disclosure': 1, 'limitation': 4, 'method': 5, 'other': 30, 'study_objective': 1}`
- Formal recommendation rows captured: **7/7**
- Secondary trial summaries remain explicitly tagged `secondary_reported_result` and are not represented as primary-study quantitative atoms.
- Pydantic structural validation: **PASS** under the reconstructed local contract.
- Generated JSON Schema validation: **PASS**.
- Sufficiency validation for extracted kinds: **PASS**.
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

## SEA result

The focused update, both management figures, Tables 1 to 3, all five Recommendation Tables, the 15-row evidence table, and declaration-of-interest governance material were reconciled. The final HTML keeps source claims separate from appraisal and preserves neutral mortality components and trial-specific limitations near the affected recommendations.

A numeric SEA score was not assigned. The exact `summary-evaluation-appraisal-protocol-v4-compact.md` file and its scoring rubric were searched in connected project sources but were not directly retrievable.

## References

The supplied evidence-table DOCX contains **51** bibliography entries. They were exported to `ehad195-references.md` with whitespace normalization only.

## Governing-source execution boundary

The named governing ATOM files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom.json`, plus the exact SEA v4 protocol, were not directly retrievable in this session. `large-source-ATOM-SEA.md` and `unslop.skill.md` were retrieved and applied. ATOM validation therefore uses a strict local Pydantic contract and generated JSON Schema reconstructed from a current validated project guideline artifact. This report does not claim execution of unavailable authoritative source code.

## Output files

- `ehad195-atoms.json`
- `ehad195-validation.json`
- `ehad195-coverage.json`
- `ehad195-sea.html`
- `ehad195-references.md`
- `ehad195-processing-report.md`
