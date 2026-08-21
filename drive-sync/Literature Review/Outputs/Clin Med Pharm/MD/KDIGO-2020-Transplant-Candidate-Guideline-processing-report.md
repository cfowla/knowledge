# KDIGO 2020 kidney transplant candidate guideline processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Title: KDIGO Clinical Practice Guideline on the Evaluation and Management of Candidates for Kidney Transplantation
- Issuing body: Kidney Disease: Improving Global Outcomes (KDIGO) Kidney Transplant Candidate Work Group
- Citation: Transplantation. 2020;104:S1-S103
- DOI: 10.1097/TP.0000000000003136
- Main guideline: `KDIGO-2020-Transplant-Candidate-Guideline.pdf`, 106 pages, SHA-256 `58f64dcae76177dbc77544dd1ad84aae69e81861d55c5a5be037c963a1a595f3`
- Summary Tables and Evidence Profiles: `KDIGO-Txp-Candidate-STs-EPs-FINAL.pdf`, 152 pages, SHA-256 `2c887f766da41cd3528935598e0b2e28c19d3978fe244ddf6da0dd8ce52d0c03`
- Supplemental Appendix A: `KDIGO-Txp-Candidate-Appendix-A-FINAL.pdf`, 74 pages, SHA-256 `d754ef21272dab22b6e0c563a0d16123eda2eb3e20cdc2cd371f72cc88f5695f`
- Supplemental Appendix B: `KDIGO-Txp-Candidate-Appendix-B-FINAL.pdf`, 6 pages, SHA-256 `68dd71384d35032fe3ecffad51e9eb8d0a9d57e74106d7179534299dd00f6a43`
- Shared publication ID: `f2645951-ea3c-5fc1-b201-6659a50d90b1`
- Evidence search: systematic searches last conducted August 2017, with additional evidence review through May 2019

## ATOM extraction

- Total LiteratureAtoms: **267**
- Formal guidance atoms: **257**
- Global scope, method, and limitation atoms: **10**
- Atom kinds: `other` 257, `method` 6, `limitation` 3, `study_objective` 1
- Assertion origin: `normalized_from_source` for all extracted atoms
- Review status: `needs_review` for all extracted atoms
- Shared publication identity: PASS
- Unique atom IDs: PASS
- Exact duplicate canonical statements after merge: 0

### Formal guidance by grade

| Grade | Count |
| --- | ---: |
| Not Graded | 66 |
| 2D | 45 |
| 1C | 42 |
| 1B | 32 |
| 2C | 27 |
| 1D | 23 |
| 1A | 13 |
| 2B | 6 |
| 2A | 3 |

### Semantic batches

| Batch | Scope | Atoms |
| --- | --- | ---: |
| `kdigo-2020-txp-global-v1` | scope, methods, evidence framework, and source limitations | 10 |
| `kdigo-2020-txp-access-age-pediatric-v1` | access, age, pediatric issues | 17 |
| `kdigo-2020-txp-psychosocial-adherence-tobacco-v1` | psychosocial assessment, adherence, tobacco | 17 |
| `kdigo-2020-txp-surgical-diabetes-v1` | surgical issues, obesity, diabetes | 21 |
| `kdigo-2020-txp-esrd-cause-recurrence-v1` | cause of ESKD and disease-specific recurrence | 49 |
| `kdigo-2020-txp-infections-v1` | infection screening, treatment, vaccination, viral disease | 58 |
| `kdigo-2020-txp-malignancy-v1` | malignancy screening and candidacy | 18 |
| `kdigo-2020-txp-cardiopulmonary-vascular-neuro-v1` | pulmonary, cardiac, PAD, neurologic disease | 34 |
| `kdigo-2020-txp-gi-heme-bone-immunology-v1` | GI/liver, hematologic, bone/mineral, immunologic assessment | 43 |

### Granularity and duplicate handling

The summary contains repeated cross-references to earlier recommendations. Seventeen repeated statements were linked to their first occurrence and were not emitted twice. Recommendation 10.5.2.4.2 was split into two atoms because it contains two independently graded actions. Recommendation 10.7.5 was split into six atoms because the six vaccine items each carry their own grade.

## Validation

- Strict local Pydantic structural validation: **PASS**, 267/267 atoms
- Generated JSON Schema serialization validation: **PASS**, 267/267 atoms
- Sufficiency validation for extracted kinds: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

### Governing-source execution boundary

The uploaded `large-source-ATOM-SEA.md` and the project `unslop.skill.md` were retrieved and applied. The named governing ATOM files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom.json`, plus the exact `summary-evaluation-appraisal-protocol-v4-compact.md`, were searched in connected project sources but were not directly retrievable in this session.

Validation therefore used the strict local Pydantic contract and generated JSON Schema reconstructed from recent validated project guideline artifacts and the large-source guideline guardrail. This report does not claim execution of unavailable authoritative project code. The accessible historical SEA compact protocol was used only as supporting structure and was not treated as a replacement for the named v4 authority.

## SEA coverage and QA

- All 19 clinical sections represented
- Formal guidance represented: **257/257 unique independently reviewable guidance assertions**
- Main figures: **3/3** reconciled
- Main tables: **14/14** inventoried and reconciled
- Summary Tables and Evidence Profiles: **22 evidence-profile summary pages** mapped and inspected
- Appendix A search strategy: inspected as reproducibility evidence
- Appendix B IOM concurrence tables: all **6/6 pages** inspected
- Main bibliography: **634 references** extracted
- Source claims kept separate from appraisal: PASS
- Underlying study results were not promoted to primary-study LiteratureAtoms: PASS
- Self-contained HTML: PASS
- Internal chat/file citation syntax: absent
- External verification: not performed because `@VERIFY` was not activated

Targeted rendered-page inspection covered the main search-yield figure, the nonadherence reevaluation algorithm, the HCV candidate algorithm, the major transplant-candidate tables, all 22 evidence-profile summary pages, representative Appendix A search strategies, and all Appendix B pages.

## Source-level appraisal findings

The guideline is broad and highly usable for transplant-candidate evaluation, but the evidence base is uneven. Many operational recommendations are ungraded or rest on low-certainty observational evidence. The source itself reports several development-process departures from Institute of Medicine standards, including no formal analytic framework, no public final systematic-review protocol, no independent peer review of search strategies, one extractor plus one checker rather than independent dual extraction, incomplete intellectual conflict-of-interest safeguards, and limited patient or public participation procedures.

The evidence package also shows that kidney transplantation is generally superior to remaining waitlisted across age groups and obesity categories, while several candidate-screening and risk-stratification questions remain supported by low or very low certainty evidence.

## References

The Markdown artifact contains the complete 634-entry main-guideline bibliography. Evidence-profile local citations were used for reconciliation but were not duplicated as a second bibliography.

## Schema gaps

- The current project LiteratureAtom pattern has no dedicated `guideline_recommendation` or `practice_point` atom kind. Formal guidance is represented as `atom_kind="other"` with descriptive tags.
- Recommendation strength and GRADE certainty are preserved in canonical text and tags rather than dedicated typed fields.
- Study effects summarized by KDIGO are secondary evidence reports. Primary-study atoms require separate extraction of the cited primary publications.

## Output files

- `KDIGO-2020-Transplant-Candidate-Guideline-atoms.json`
- `KDIGO-2020-Transplant-Candidate-Guideline-validation.json`
- `KDIGO-2020-Transplant-Candidate-Guideline-coverage.json`
- `KDIGO-2020-Transplant-Candidate-Guideline-sea.html`
- `KDIGO-2020-Transplant-Candidate-Guideline-references.md`
- `KDIGO-2020-Transplant-Candidate-Guideline-processing-report.md`
