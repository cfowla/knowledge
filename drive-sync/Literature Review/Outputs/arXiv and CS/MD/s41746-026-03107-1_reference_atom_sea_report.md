# ATOM + SEA processing report — s41746-026-03107-1_reference.pdf

## Activated macros
- `@ATOM`
- `@SEA`

## Governing project sources
### ATOM precedence
1. `literature.py` — structural domain validation
2. `literature_atoms.py` — atom-kind sufficiency validation
3. `literature_atom.schema.json` — serialization contract
4. `README(2).md` — workflow intent
5. `example_atom.json` — illustrative only

### SEA precedence
1. `summary-evaluation-appraisal-protocol-v4-compact.md`
2. v3 material — historical/reference only
3. Retrieved primary PDF

## Source
- **Title:** Sequential question answering AI for hierarchical gastric pathology diagnosis
- **Journal:** npj Digital Medicine
- **Status:** Article in Press; unedited manuscript
- **DOI:** 10.1038/s41746-026-03107-1
- **Received:** 2026-01-31
- **Accepted:** 2026-07-30
- **Retrieved file:** `s41746-026-03107-1_reference.pdf`
- **Size:** 9,353,179 bytes
- **Pages:** 43
- **SHA-256:** `85ae83de07fc81dc2799474005216271c56da104726ac961ccae0c19557c333a`
- **Shared publication_id:** `8a28b707-605f-549c-bced-f37a516dfb2f`

## Large-source / semantic batch plan
| Batch | Scope | Atoms |
|---|---|---:|
| 00-objective | Objective, hierarchy, Auto-QA/HITL-QA framing | 6 |
| 01-datasets | Cohorts, taxonomy, labeling rules | 11 |
| 02-architecture | Preprocessing, model architecture, prompts, training, baselines | 15 |
| 03-autoqa | Structured-report and Auto-QA task results | 13 |
| 04-hitl | HITL gains and intervention burden | 13 |
| 05-error-ablation | Difficult tasks, FNR, interpretability, ablations | 18 |
| 06-discussion | Conclusions, deployment statements, limitations, provenance | 16 |

## Atom counts
- **Total:** 92

- `author_conclusion`: 2
- `conflict_of_interest`: 1
- `data_availability`: 2
- `eligibility_criterion`: 1
- `funding_disclosure`: 1
- `limitation`: 8
- `method`: 24
- `other`: 2
- `population_description`: 6
- `qualitative_result`: 3
- `quantitative_result`: 41
- `study_objective`: 1

## Validation
- Pydantic structural validation: **PASS** (92/92 atoms)
- JSON Schema validation against `literature_atom.schema.json`: **PASS** (92/92 atoms)
- Atom-kind sufficiency validation: **PASS**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Review status: all atoms are `needs_review` because extraction was performed by a language model rather than human-verified.

## SEA coverage
- Main substantive text: PDF pp. 2–31
- References: PDF pp. 31–35; not atomized as evidence
- Main figures: Figures 1–8 on PDF pp. 36–43; all reconciled as structured blocks in the HTML
- Main-text tables: none
- Supplementary material: Figures S1–S21 and Tables S1–S20 are cited but not present in the retrieved PDF

## Source-derived limitations affecting extraction/appraisal
1. The file is an unedited Article in Press manuscript and warns that errors may remain.
2. Supplementary tables/figures are unavailable in the retrieved PDF, preventing independent inspection of several referenced ablations, confusion matrices, AUC analyses, hyperparameters, and computational-efficiency details.
3. The study is retrospective; clinical utility is not established by the benchmark results.
4. The source itself reports substantial remaining HITL intervention burden and explicitly states that human oversight is still necessary.

## SEA QA
- Coverage manifest created before narrative synthesis: **PASS**
- All eight main figures reconciled: **PASS**
- Appraisal performed after extraction: **PASS**
- Self-contained HTML with embedded CSS and no external scripts/fonts/images: **PASS**
- Internal chat/file citation syntax in HTML: **none**
- Placeholder/TODO scan: **PASS**
- Source/title match: **PASS**

## Output files
- `s41746-026-03107-1_reference_atoms.json`
- `s41746-026-03107-1_reference_sea.html`
- `s41746-026-03107-1_reference_atom_sea_report.md`
