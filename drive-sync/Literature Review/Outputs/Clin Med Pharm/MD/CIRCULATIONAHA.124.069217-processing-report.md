# CIRCULATIONAHA.124.069217 ATOM + SEA processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Title: *Effect of Empagliflozin on Heart Failure Outcomes After Acute Myocardial Infarction: Insights From the EMPACT-MI Trial*
- Citation: Circulation. 2024;149:1627-1638.
- DOI: `10.1161/CIRCULATIONAHA.124.069217`
- Trial registration: `NCT04509674`
- Main article: 12 pages, SHA-256 `a0943219681068c3b16c8ff7723d17a8d33e9f282fefe9bcf1ab96848d3ba249`
- Supplemental material: 19 pages, SHA-256 `170f9e3c924eaa0e81d48051f1b7cd6d7740ead97f03c0252af010c84241be16`
- Podcast transcript: 6 pages, SHA-256 `bce0ebcd642892e380c330247c42a673896c55a74a2dc08d64a106ccb257053a`
- Shared LiteratureAtom publication ID: `640dc59f-b65e-57d4-a5e0-50ca2ab12894`

The article and supplement were treated as one publication identity. The podcast transcript was reviewed as supporting author-interview context and was not atomized as primary evidence.

## ATOM result

- Total LiteratureAtoms: **70**
- Atom kinds: `{'adverse_event': 6, 'author_conclusion': 2, 'comparator_description': 1, 'conflict_of_interest': 2, 'data_availability': 1, 'eligibility_criterion': 4, 'funding_disclosure': 1, 'intervention_description': 1, 'limitation': 6, 'method': 11, 'outcome_definition': 4, 'population_description': 3, 'qualitative_result': 4, 'quantitative_result': 20, 'study_objective': 1, 'subgroup_result': 3}`
- Assertion origin: `{'normalized_from_source': 70}`
- Shared publication identity: **PASS**
- Unique atom IDs: **PASS**
- Local reconstructed Pydantic contract validation: **PASS**
- Local serialization-shape validation: **PASS**
- Local sufficiency validation for extracted kinds: **PASS**
- Structural errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

### Semantic batches

| Batch | Scope | Atoms |
| --- | --- | ---: |
| `empact-mi-hf-global-v1` | source identity, design, population, eligibility, intervention, follow-up | 13 |
| `empact-mi-hf-methods-v1` | endpoint definitions, ascertainment, statistical methods | 12 |
| `empact-mi-hf-results-v1` | primary hierarchy, first/recurrent HHF, timing and sensitivity analyses | 12 |
| `empact-mi-hf-ae-therapy-v1` | exploratory HF adverse events and post-discharge therapy initiation | 17 |
| `empact-mi-hf-interpretation-v1` | subgroups, limitations, conclusions, funding, conflicts and data availability | 16 |

## SEA result

The primary article, all six main figures, the complete supplement, Supplementary Tables 1-4, and Supplementary Figures 1-6 were reconciled before final appraisal. The SEA keeps the negative primary composite next to the positive HF hospitalization findings and separates prespecified HHF analyses from exploratory broad-HF adverse-event analyses.

No protocol-specific numeric SEA score was assigned because the exact `summary-evaluation-appraisal-protocol-v4-compact.md` file was not directly retrievable.

## Source-integrity findings

1. Figure 6A and the Results prose report different diuretic-initiation populations and estimates. The prose reports HR 0.80, 95% CI 0.64 to 1.00, P=0.046 with 138, 12.2%, versus 174, 15.3%. Figure 6A starts with 1,788 versus 1,873 patients at risk and reports HR 0.76, 95% CI 0.61 to 0.96, P=0.021. They were preserved as distinct source presentations.
2. The podcast uses conversational language that calls the HF analysis post hoc. The formal article and Supplementary Table 1 identify first and total HHF analyses as prespecified. The formal publication governs extraction.
3. The article itself states that failure of the primary endpoint means the HF endpoint analyses should be considered exploratory in a strict statistical sense.

## References

The main article contains **13 references**. They were exported in source order to `CIRCULATIONAHA.124.069217-references.md`. Bibliographic entries were not atomized.

## Governing-source execution boundary

The available `large-source-ATOM-SEA.md` workflow and `unslop.skill.md` were applied. The named authoritative files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, `example_atom.json`, and `summary-evaluation-appraisal-protocol-v4-compact.md` were searched in connected project sources but were not directly retrievable.

Validation therefore used a strict local Pydantic contract and serialization shape reconstructed from current project LiteratureAtom artifacts plus local sufficiency checks. This report does not claim execution of unavailable authoritative project code or the exact SEA v4 scoring rubric.

## Output files

- `CIRCULATIONAHA.124.069217-atoms.json`
- `CIRCULATIONAHA.124.069217-validation.json`
- `CIRCULATIONAHA.124.069217-coverage.json`
- `CIRCULATIONAHA.124.069217-sea.html`
- `CIRCULATIONAHA.124.069217-references.md`
- `CIRCULATIONAHA.124.069217-processing-report.md`
