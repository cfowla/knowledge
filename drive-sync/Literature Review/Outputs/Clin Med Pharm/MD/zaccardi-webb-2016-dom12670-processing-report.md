# Processing report

## Source

- Folder: `Zaccardi Webb 2016`
- Main file: `Diabetes Obesity Metabolism - 2016 - Zaccardi - Efficacy and safety of sodium‐glucose co‐transporter‐2 inhibitors in type 2.pdf`
- Supplement packet: 17 DOCX files (`Appendix S1`, Supplementary Tables S1–S8, Supplementary Figures S1–S8)
- Title: Efficacy and safety of sodium-glucose co-transporter-2 inhibitors in type 2 diabetes mellitus: systematic review and network meta-analysis
- DOI: `10.1111/dom.12670`
- PMID: `27059700`
- Main SHA-256: `e160cc285badf753f9c68b8372498bc734d454929cd9e589a85505503c05fbc9`

## ATOM

- Atoms: **123**
- Kinds: `{"adverse_event": 6, "author_conclusion": 3, "comparator_description": 2, "conflict_of_interest": 4, "data_availability": 1, "eligibility_criterion": 2, "funding_disclosure": 2, "intervention_description": 3, "limitation": 6, "method": 10, "other": 3, "outcome_definition": 14, "population_description": 15, "qualitative_result": 7, "quantitative_result": 44, "study_objective": 1}`
- Semantic batches: `{"zaccardi-webb-2016-consistency-v1": 15, "zaccardi-webb-2016-general-v1": 23, "zaccardi-webb-2016-interpretation-v1": 15, "zaccardi-webb-2016-outcomes-methods-v1": 23, "zaccardi-webb-2016-primary-efficacy-v1": 26, "zaccardi-webb-2016-safety-v1": 13, "zaccardi-webb-2016-secondary-efficacy-v1": 5, "zaccardi-webb-2016-source-integrity-v1": 3}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Exact duplicate canonical statements: **0**

The review is secondary literature. Trial results summarized by the review are represented as the review's network/meta-analytic findings and are not re-labeled as primary-study observations.

## SEA and coverage

All 12 article PDF pages and all 17 supplied supplementary DOCX files were inspected. Two main figures, three main tables, eight supplementary tables, eight supplementary figures, the PRISMA/search appendix, and the 74-reference bibliography were reconciled.

## Source-integrity findings

1. **UTI wording error:** main text calls the 1,959 UTI events “hypoglycaemic” events; Supplementary Table S3 identifies 1,959 UTI events.
2. **Genital-infection count conflict:** main text reports 1,285 events; Supplementary Table S3 reports 1,312.
3. **UTI denominator conflict:** Supplementary Table S3 reports 24,037 participants in the UTI network, exceeding the full review population of 23,997 by 40.
4. **Body-weight network inconsistency:** full network p=0.0229; the 24–30-week sensitivity network p=0.386.

No discrepancy was silently repaired.

## References

The article contains **74** numbered references. They were exported to `zaccardi-webb-2016-dom12670-references.md` with line wrapping normalized and without external bibliographic correction.

## Governing sources applied

ATOM: `literature(1).py` → `literature_atoms(1).py` → `literature_atom.schema.json`; large-source execution used `large-source-ATOM-SEA.md`. SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as governing protocol; v3 was historical reference only.

Source gaps: `README(2).md`, `example_atom.json`, and `unslop.skill.md` were not available in the current supplied project sources. Their absence was not filled from prior examples.

## Output files

- `zaccardi-webb-2016-dom12670-atoms.json`
- `zaccardi-webb-2016-dom12670-validation.json`
- `zaccardi-webb-2016-dom12670-coverage.json`
- `zaccardi-webb-2016-dom12670-crosswalk.json`
- `zaccardi-webb-2016-dom12670-sea.html`
- `zaccardi-webb-2016-dom12670-sea-qa.json`
- `zaccardi-webb-2016-dom12670-references.md`
- `zaccardi-webb-2016-dom12670-processing-report.md`
