# ehad192 processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Main guideline: `ehad192.pdf`
- Supplementary data: `ehad192_supplementary_data.pdf`
- Evidence tables: `for_ehj_2023_esc_guidelines_on_cvd_and_diabetes_evidence_tables_130423.pdf`
- Declaration-of-interest packet: `doi_summary_2023_diabetes_24042023.pdf`
- Title: *2023 ESC Guidelines for the management of cardiovascular disease in patients with diabetes*
- Journal: *European Heart Journal*. 2023;44:4043-4140.
- DOI: `10.1093/eurheartj/ehad192`
- Shared publication ID: `bc42c3d9-cbf1-535c-bb33-8b814a803c6f`

## Large-source execution

The packet was processed as a large guideline source. Semantic batches covered global methods and governance, diagnosis and risk assessment, lifestyle and glycaemia, blood pressure and lipids, antithrombotic therapy, CAD and ACS, heart failure, arrhythmia, CKD, aortic and peripheral arterial disease, type 1 diabetes, person-centred care, and evidence gaps.

Formal recommendations were extracted from all 27 Recommendation Tables. Supporting tables, figures, algorithms, the 37-page supplement, and the 228-page evidence packet were used for SEA reconciliation. Underlying trial findings were kept as secondary evidence and were not represented as if the ESC guideline generated the trial data.

## ATOM result

- Total LiteratureAtoms: **175**
- Formal guideline recommendation atoms: **144**
- Recommendation Tables represented: **27/27**
- Atom kinds: `{'author_conclusion': 7, 'conflict_of_interest': 1, 'data_availability': 1, 'funding_disclosure': 1, 'limitation': 15, 'method': 5, 'other': 144, 'study_objective': 1}`
- Recommendation class/level distribution: `{'IA': 50, 'IB': 20, 'IC': 25, 'IIIA': 1, 'IIIB': 4, 'IIaA': 4, 'IIaB': 20, 'IIaC': 8, 'IIbA': 1, 'IIbB': 7, 'IIbC': 4}`
- Pydantic structural validation: **PASS under reconstructed local contract**
- Generated JSON Schema validation: **PASS**
- Sufficiency validation: **PASS for extracted kinds**
- Structural errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Exact duplicate statement groups: **1**, retained because the same recommendation is formally repeated in separate recommendation tables.
- Review status: all atoms are `needs_review`.

## SEA result

The SEA artifact reconciles:

- 21/21 main figures
- 12/12 main general tables
- 27/27 recommendation tables
- 17/17 supplementary tables
- 8/8 supplementary figures
- 15/15 evidence-selection tables
- the declaration-of-interest packet for governance context

The appraisal separates guideline claims from model appraisal and preserves key treatment thresholds, risk-model boundaries, major cardiovascular and cardiorenal evidence signals, safety limitations, and the guideline's own evidence gaps.

No numeric SEA score was assigned because the exact governing SEA v4 scoring protocol was not directly retrievable in this session.

## References result

The Markdown bibliography contains:

- **845** main-guideline references
- **130** supplementary-data references
- **256** evidence-table references

Source-specific numbering is preserved. Overlapping references across the three source bibliographies were not silently merged.

## Governing-source execution boundary

The required authoritative project files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, `example_atom.json`, and `summary-evaluation-appraisal-protocol-v4-compact.md` were searched in connected project sources but were not directly retrievable.

`large-source-ATOM-SEA.md` was retrieved and applied. `unslop.skill.md` was retrieved from Google Drive and applied to generated prose.

The ATOM validation report therefore does **not** claim execution of the unavailable authoritative Pydantic model, sufficiency validator, or serialization schema. It uses a strict local Pydantic contract reconstructed from current validated project guideline artifacts, its generated JSON Schema, and a local sufficiency check for the extracted kinds.

## Output files

### JSON

- `ehad192-atoms.json`
- `ehad192-validation.json`
- `ehad192-coverage.json`

### HTML

- `ehad192-sea.html`

### Markdown

- `ehad192-references.md`
- `ehad192-processing-report.md`
