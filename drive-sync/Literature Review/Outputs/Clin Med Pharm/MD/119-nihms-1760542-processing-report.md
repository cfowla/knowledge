# Processing report: Combined PD-1 and HER2 blockade for HER2-positive gastric cancer

Activated macros: @ATOM, @SEA.

## Source packet

- Primary: `nihms-1760542.pdf`, 19 pages, SHA-256 `3afc52a122e180b6c0c04c918e29aaff5cdf0f34f2f52053a7a24fa30e745f5a`.
- Supplement: `NIHMS1760542-supplement-1760542_Sup_Info.pdf`, 201 pages, SHA-256 `b629f6d6cc8ee65e98284cb45ca52beb323baae9787d87fc0f519337e8f7d280`.
- Supplement guide: `NIHMS1760542-supplement-1760542_SI_guide.docx`, SHA-256 `86084a8360ccfcf84fb3037c841c550125167a767f1e07da86d934c23620c2a5`.
- DOI: `10.1038/s41586-021-04161-3`.
- Trial: `NCT03615326`.

## ATOM

- Atoms: **85**.
- Counts by kind: `{"adverse_event": 16, "author_conclusion": 3, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 14, "funding_disclosure": 1, "intervention_description": 4, "limitation": 3, "method": 15, "outcome_definition": 2, "population_description": 10, "qualitative_result": 1, "quantitative_result": 10, "study_objective": 1, "subgroup_result": 2}`
- Semantic batches: `{"nihms-1760542-design-v1": 22, "nihms-1760542-efficacy-v1": 13, "nihms-1760542-interpretation-v1": 9, "nihms-1760542-population-v1": 10, "nihms-1760542-protocol-context-v1": 15, "nihms-1760542-safety-v1": 16}`
- Pydantic structural validation: **PASS**.
- JSON Schema validation: **PASS**.
- Sufficiency validation: **PASS**.
- Structural errors: **0**.
- Schema errors: **0**.
- Sufficiency errors: **0**.
- Sufficiency warnings: **0**.

The primary interim efficacy signal is retained as an objective-response finding. It is not converted into a PFS or OS benefit. Protocol-only statements are tagged `protocol_planned` and anchored to the supplement.

## SEA and coverage

All 19 manuscript pages were rendered and visually checked. One main figure, two main tables, one extended-data figure, and six extended-data tables were reconciled. The complete 201-page supplement was text-mapped. Protocol pages covering design, eligibility, treatment, and statistical analysis were rendered and checked separately. Sponsor-redacted sections were not reconstructed.

The appraisal was performed after extraction and visual reconciliation. Current regulatory status and current guideline placement were not externally verified because @VERIFY was not activated.

## References

The primary article contains **32** numbered references. They were exported as a Markdown task queue. The protocol bibliography was not merged into the article reference queue.

## Governing sources

ATOM precedence was applied as `literature(1).py` -> `literature_atoms(1).py` -> `literature_atom.schema.json` -> `README(2).md` -> `example_atom(1).json`, with the example treated as illustrative only. SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as authoritative by project precedence. Its internal heading says Integrated Compact v3. The supplied v3 HTML was historical reference only. `large-source-ATOM-SEA.md` guided semantic batching. `unslop.skill.md` controlled prose style.

## Output files

- `119-nihms-1760542-atoms.json`
- `119-nihms-1760542-validation.json`
- `119-nihms-1760542-coverage.json`
- `119-nihms-1760542-sea.html`
- `119-nihms-1760542-references.md`
- `119-nihms-1760542-processing-report.md`
