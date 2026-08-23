# Processing report: Bonnesen et al. 2025

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Title: Effectiveness of Empagliflozin vs Dapagliflozin for Kidney Outcomes in Type 2 Diabetes
- Journal: JAMA Intern Med. 2025;185(3):314-323.
- DOI: `10.1001/jamainternmed.2024.7381`
- Main article: 10 pages, SHA-256 `341eef224e08361425390a76cd69b98a3dec124345419915819ae50fcc65ebec`
- Supplement 1: 18 pages, SHA-256 `b54ccb2f052808f5f99016d38b5939a599e3ae34ca12e7f1e863bd61f139c045`
- Shared publication ID: `efa324e5-ef77-5d76-b69d-6ab018906dca`

## ATOM status

The extraction produced **128** LiteratureAtom objects across **8** semantic batches. Counts by kind: `{'author_conclusion': 3, 'comparator_description': 1, 'conflict_of_interest': 1, 'data_availability': 1, 'eligibility_criterion': 4, 'funding_disclosure': 2, 'intervention_description': 1, 'limitation': 5, 'method': 13, 'outcome_definition': 4, 'population_description': 4, 'qualitative_result': 2, 'quantitative_result': 17, 'study_objective': 1, 'subgroup_result': 69}`.

Authoritative Pydantic structural validation: **PASS**. JSON Schema validation: **PASS**. Atom-kind sufficiency validation: **PASS** with 0 errors and 0 warnings. Atom IDs are unique and all atoms share one publication ID. All model-extracted atoms remain `needs_review`.

The governing ATOM sources were `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom(1).json`, with the first three carrying the governing validation and serialization requirements. Large-source execution used `large-source-ATOM-SEA.md`.

## SEA and coverage

All 10 main-article pages and all 18 Supplement 1 pages were inspected. Coverage reconciled the main baseline table, 4 main figures, 8 supplemental tables, and 5 supplemental figures. SEA QA status: **PASSED**.

Verdict: **Read first** for a formulary evidence review focused on empagliflozin versus dapagliflozin kidney effectiveness. The main intention-to-treat risk ratios were 0.98 for AKI, 0.97 for incident CKD G3-G5, 1.04 for CKD A2/A3, and 0.94 for CKD progression. The progression estimate was imprecise. The study does not establish full therapeutic interchangeability because safety, heart-failure effectiveness, current indication differences, inpatient use, operational policy, and cost were outside the comparative kidney-outcome design.

SEA v4 scores: relevance **9/10**, novelty **8/10**, method strength **8/10**, evidence strength **7/10**, external validity **7/10**, implementation value **8/10**.

## Source-integrity findings

1. Supplement eTable 1 labels the research question as cardiovascular effectiveness, although its aim and outcomes are kidney-related.
2. The Supplement contents swap the eTable 6 and eTable 7 titles relative to the actual table pages, and the main Results text contains inconsistent table-number references.
3. Main Methods and eTable 1 require CKD confirmation at least 90 days apart, while Figure 1 footnotes say 30 to 180 days after first indication for incident CKD outcomes.

No discrepancy was silently repaired.

## Reference task queue

The article contains **41** numbered references. They were converted to `bonnesen-heide-jorgensen-2025-jamainternmed-2024-7381-reference-task-queue.md` in source order. PDF line wrapping was normalized. No external bibliographic correction was performed.

## Output files

- `bonnesen-heide-jorgensen-2025-jamainternmed-2024-7381-atoms.json`
- `bonnesen-heide-jorgensen-2025-jamainternmed-2024-7381-validation.json`
- `bonnesen-heide-jorgensen-2025-jamainternmed-2024-7381-coverage.json`
- `bonnesen-heide-jorgensen-2025-jamainternmed-2024-7381-crosswalk.json`
- `bonnesen-heide-jorgensen-2025-jamainternmed-2024-7381-sea.html`
- `bonnesen-heide-jorgensen-2025-jamainternmed-2024-7381-sea-qa.json`
- `bonnesen-heide-jorgensen-2025-jamainternmed-2024-7381-reference-task-queue.md`
- `bonnesen-heide-jorgensen-2025-jamainternmed-2024-7381-processing-report.md`

JSON outputs belong in `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/JSON`. The SEA HTML belongs in `.../HTML`. Markdown files belong in `.../MD`.

No external verification was performed because `@VERIFY` was not activated.
