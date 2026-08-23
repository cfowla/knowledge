# Processing report: Bonnesen et al. 2024

## Source

- Title: Comparative Cardiovascular Effectiveness of Empagliflozin Versus Dapagliflozin in Adults With Treated Type 2 Diabetes: A Target Trial Emulation
- Journal: Circulation. 2024;150:1401-1411
- DOI: 10.1161/CIRCULATIONAHA.124.068613
- PMID: 39206550
- Main article: 11 pages, SHA-256 `345ea8ba011c2b98bdb93f74dd5a3d35c4f8314a45737a3f4ed33d4f4d88780b`
- Supplement: 10 pages, SHA-256 `e60d81d07895206a2900634af181b4b578439e0cd570c4f9c487d8c528c5790a`
- Publication ID: `db050afd-0952-57d4-a378-225935a82f0c`

## ATOM

The extraction produced 65 LiteratureAtom objects across 6 semantic batches. Counts by kind: `{"author_conclusion": 3, "comparator_description": 1, "conflict_of_interest": 2, "data_availability": 1, "eligibility_criterion": 3, "funding_disclosure": 3, "intervention_description": 1, "limitation": 4, "method": 12, "outcome_definition": 2, "population_description": 6, "qualitative_result": 1, "quantitative_result": 14, "study_objective": 1, "subgroup_result": 11}`.

Pydantic structural validation passed with 0 errors. JSON Schema validation passed with 0 errors. Atom-kind sufficiency validation passed with 0 errors and 0 warnings. Atom IDs are unique and all atoms share one publication ID. All model-assisted atoms remain `needs_review`.

The governing ATOM sources were `literature(1).py`, `literature_atoms(1).py`, and `literature_atom.schema.json`. `example_atom.json` was used only as an illustrative scaffold. The lower-precedence `README(2).md` was not available in the supplied project sources or Drive search, so no requirements were inferred from it.

## SEA and coverage

All 11 main-article pages and all 10 supplement pages were rendered and visually inspected. Coverage reconciled 4 main figures, the main baseline table, 5 supplementary tables, and 3 supplementary figures. The final HTML was generated after extraction and visual reconciliation. SEA QA passed.

Verdict: Read first for a formulary evidence review focused on empagliflozin versus dapagliflozin cardiovascular effectiveness. The primary six-year MACE estimate was RR 1.00, 95% CI 0.91 to 1.11, with risk difference 0.0 percentage points, 95% CI -0.9 to 1.0. The study does not establish full therapeutic interchangeability because comparative safety, current indication differences, renal outcomes, inpatient use, and cost were outside its comparative design.

Scores under the SEA v4 rubric: relevance 9/10, novelty 8/10, method strength 8/10, evidence strength 7/10, external validity 7/10, implementation value 8/10.

## Source-integrity findings

- Main Methods and Supplement Table S3 use prior-year laboratory summaries, while the Figure S2 note says prior-month summaries for hemoglobin A1c and eGFR.
- Supplement Table S3 labels an index-year subgroup as 2019-2022, while enrollment ended in 2020 and the main subgroup specification uses 2019-2021.
- The article states that no new data were created or analyzed even though it reports analyses of Danish registry data. The exact source wording was preserved.

## References

The main article contains 30 numbered references. They were transcribed from pages 1410-1411 to `bonnesen-heide-jorgensen-2024-circulationaha-124-068613-references.md`. PDF line wrapping and typographic dashes were normalized. No external bibliographic correction was used.

## Output files

- `bonnesen-heide-jorgensen-2024-circulationaha-124-068613-atoms.json`
- `bonnesen-heide-jorgensen-2024-circulationaha-124-068613-validation.json`
- `bonnesen-heide-jorgensen-2024-circulationaha-124-068613-coverage.json`
- `bonnesen-heide-jorgensen-2024-circulationaha-124-068613-sea.html`
- `bonnesen-heide-jorgensen-2024-circulationaha-124-068613-sea-qa.json`
- `bonnesen-heide-jorgensen-2024-circulationaha-124-068613-references.md`
- `bonnesen-heide-jorgensen-2024-circulationaha-124-068613-processing-report.md`

Intended Google Drive GitHub Sync locations follow the existing project convention: JSON files under `Literature Review/Outputs/Clin Med Pharm/JSON`, the SEA HTML under `.../HTML`, and Markdown files under `.../MD`.

No external verification was performed because `@VERIFY` was not activated.
