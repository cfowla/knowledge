# AHA-ACC-2024-Heart-Failure-Performance-Measures processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Title: *2024 Update to the 2020 ACC/AHA Clinical Performance and Quality Measures for Adults With Heart Failure: A Report of the American Heart Association/American College of Cardiology Joint Committee on Performance Measures*
- Authors: Kittleson MM, Breathett K, Ziaeian B, Aguilar D, Blumer V, Bozkurt B, Diekemper RL, Dorsch MP, Heidenreich PA, Jurgens CY, Khazanie P, Koromia GA, Van Spall HGC
- Journal: Circulation: Cardiovascular Quality and Outcomes
- Citation: Circ Cardiovasc Qual Outcomes. 2024;17:e000132.
- DOI: `10.1161/HCQ.0000000000000132`
- Source type: clinical performance and quality measure update
- PDF pages: 20
- SHA-256: `a2842d037a85f3cb86a789f20ff8001c2bdc011eea832eabb3bf3be7844e0a62`
- Shared publication ID: `5e1af632-a08b-57cf-86cb-0b443f3c6233`

## ATOM status

- LiteratureAtoms: **20**
- Formal measure atoms: **9/9**
- New performance measures: **3/3**
- New quality measures: **6/6**
- Atom kinds: `{'conflict_of_interest': 1, 'funding_disclosure': 1, 'limitation': 1, 'method': 4, 'other': 12, 'study_objective': 1}`
- Shared publication identity: **PASS**
- Unique atom IDs: **PASS**
- Local Pydantic contract validation: **PASS**
- Local generated JSON Schema validation: **PASS**
- Local sufficiency checks for extracted generic kinds: **PASS**
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Review status: all atoms remain `needs_review`

The recovered LiteratureAtom pattern has no dedicated `performance_measure` or `quality_measure` kind. The nine formal specifications are represented as `atom_kind="other"` with tags for measure type, identifier, phenotype, setting, and clinical topic. Trial results summarized in measure rationales remain secondary evidence and were not promoted to primary-study atoms.

## Semantic batches

| Batch | Scope | Atoms |
| --- | --- | ---: |
| `aha-acc-hfpm-2024-global-v1` | purpose, measure taxonomy, update decisions, measure status | 7 |
| `aha-acc-hfpm-2024-performance-v1` | PM-1 through PM-3 | 3 |
| `aha-acc-hfpm-2024-quality-v1` | QM-1 through QM-6 | 6 |
| `aha-acc-hfpm-2024-governance-v1` | limitations, peer review, funding, RWI | 4 |

## SEA status

The final HTML covers the update method, all nine Appendix A measure specifications, evidence maturity, implementation value, limitations, governance, and source-integrity conflicts. Final appraisal occurred after measure extraction and table reconciliation.

No protocol-specific numeric SEA score was assigned because the exact `summary-evaluation-appraisal-protocol-v4-compact.md` scoring rubric was not directly retrievable.

### Source-integrity findings

1. The abstract and Appendix A classify the monoclonal-protein-screen measure as **QM-6**, while Top 10 Take-Home Message 10 calls it a performance measure. The operational table classification is preserved in the atom and SEA artifact, with the conflict flagged.
2. Top 10 Take-Home Message 5 says heart transplant and LVAD patients are excluded from all measures, but Appendix A does not list those exclusions for QM-2, QM-3, or QM-6. The individual Appendix A specifications are preserved without rewriting the source.

## Reference extraction

- Printed reference pages: **888-890**
- Numbered references extracted: **117**
- Sequence 1 through 117 complete: **PASS**
- Bibliography atomized: **No**
- Output format: Markdown

## Governing-source execution boundary

The supplied `large-source-ATOM-SEA.md` workflow was retrieved and applied. `unslop.skill.md` was retrieved and applied to prose artifacts.

The named authoritative ATOM files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom.json`, plus the exact `summary-evaluation-appraisal-protocol-v4-compact.md`, were searched in connected project sources but were not directly retrievable. Validation therefore uses a strict local Pydantic contract and generated JSON Schema reconstructed from current validated project output patterns, plus local sufficiency checks for the generic atom kinds used here. This run does not claim execution of unavailable authoritative project code or the exact SEA v4 scoring rubric.

No external verification was performed because `@VERIFY` was not activated.

## Output files

- `AHA-ACC-2024-Heart-Failure-Performance-Measures-atoms.json`
- `AHA-ACC-2024-Heart-Failure-Performance-Measures-validation.json`
- `AHA-ACC-2024-Heart-Failure-Performance-Measures-coverage.json`
- `AHA-ACC-2024-Heart-Failure-Performance-Measures-sea.html`
- `AHA-ACC-2024-Heart-Failure-Performance-Measures-references.md`
- `AHA-ACC-2024-Heart-Failure-Performance-Measures-processing-report.md`

## Intended Google Drive GitHub Sync destinations

- JSON files: `Literature Review/Outputs/Clin Med Pharm/JSON/`
- SEA HTML: `Literature Review/Outputs/Clin Med Pharm/HTML/`
- Markdown references and processing report: `Literature Review/Outputs/Clin Med Pharm/MD/`
