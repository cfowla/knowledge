# Processing report

## Source

- Folder: `Immanuel Yonatan 2025`
- File: `NarraJ-5-e1833.pdf`
- Title: Redefining treatment paradigms: Early use of dapagliflozin and empagliflozin in acute heart failure – a systematic review and meta-analysis of randomized controlled trials
- DOI: `10.52225/narra.v5i1.1833`
- PMID (from TBR task list): `40352167`
- SHA-256: `39a3ac3d8a415ba0c1b17a5a18538bb7da18a160109c6d603ee8c965284d99c8`

## ATOM

- Atoms: **47**
- Kinds: `{"adverse_event": 6, "author_conclusion": 2, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 2, "funding_disclosure": 1, "intervention_description": 2, "limitation": 4, "method": 10, "other": 1, "population_description": 4, "qualitative_result": 4, "quantitative_result": 7, "study_objective": 1}`
- Semantic batches: `{"immanuel-yonatan-2025-fulltext-v1-disclosures": 4, "immanuel-yonatan-2025-fulltext-v1-general": 1, "immanuel-yonatan-2025-fulltext-v1-interpretation": 7, "immanuel-yonatan-2025-fulltext-v1-methods": 12, "immanuel-yonatan-2025-fulltext-v1-outcomes": 14, "immanuel-yonatan-2025-fulltext-v1-population": 9}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

This article is a secondary source. Pooled and trial-summary findings remain tagged as secondary-source evidence; primary-study atoms require direct extraction from the cited RCT publications.

## SEA

All 16 pages were rendered and visually inspected. Fifteen main-text figures, two main-text tables, and the PRISMA workflow were reconciled as structured blocks. No supplementary file was present in the selected Drive packet.

## Source-integrity findings

1. Narrative says 473 database records plus 1 hand-search record = 474; the database-specific counts shown in Figure 1 sum to 474 before adding the hand-search record, so the component counts do not reconcile with the stated total.
2. Results narrative reports approximately 49.36% of patients had diabetes, whereas the Table 1 summary reports 51.1%.
3. The paper repeatedly describes the mortality endpoint as in-hospital all-cause mortality, while Table 2 labels follow-up as ranging from 5 to 90 days.
4. Table 2 reports 20/420 control vs 15/423 early SGLT2i but prints RR 1.20 (95% CI 0.27–5.25), a direction inconsistent with the displayed event rates; it also labels 3 RCTs while listing only references [15,16].
5. Methods state that only low-risk or some-concerns studies were included, yet sensitivity analysis is described as removing high-risk studies.
6. The Results sentence refers to symptomatic hypertension, while Figure 12 and Table 2 specify symptomatic hypotension.
7. Results prose attributes the significant serious-adverse-event reduction to empagliflozin, while Figure 15 and Table 2 label the pooled intervention as early dapagliflozin and empagliflozin.

No discrepancy was silently repaired.

## References

The article contains **31** numbered references. They were exported to `immanuel-yonatan-2025-narra-e1833-references.md` with PDF line wrapping normalized and without external bibliographic correction.

## Governing-source boundary

Applied: `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, `README(2).md`, `example_atom(1).json`, `large-source-ATOM-SEA.md`, and `summary-evaluation-appraisal-protocol-v4-compact.md`. No external/web verification was requested or used for the extraction/appraisal.

## Output files

- `immanuel-yonatan-2025-narra-e1833-atoms.json`
- `immanuel-yonatan-2025-narra-e1833-validation.json`
- `immanuel-yonatan-2025-narra-e1833-coverage.json`
- `immanuel-yonatan-2025-narra-e1833-crosswalk.json`
- `immanuel-yonatan-2025-narra-e1833-sea.html`
- `immanuel-yonatan-2025-narra-e1833-sea-qa.json`
- `immanuel-yonatan-2025-narra-e1833-references.md`
- `immanuel-yonatan-2025-narra-e1833-processing-report.md`
