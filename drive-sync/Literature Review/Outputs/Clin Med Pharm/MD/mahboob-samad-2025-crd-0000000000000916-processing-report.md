# Processing report: Mahboob et al. 2025

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Title: Meta-Analysis of Cardiovascular Efficacy of Empagliflozin Versus Dapagliflozin in Type 2 Diabetes: Unveiling Key Insights
- Journal: Cardiology in Review. 2025;XXX:00–00.
- DOI: `10.1097/CRD.0000000000000916`
- Main article: 8 pages, SHA-256 `9d08286b5926718301cb0cf1a6d5d4c7789ade1649d810786928fa8ddb70d25f`
- Supplement: 11 pages, SHA-256 `cb881f885b3da7156cfc93456d30767817073534ba1f8501a73d8d319fea7bba`
- Shared publication ID: `af6066c2-4b0e-58ca-a589-12fdf1cb27f8`

## ATOM status

The extraction produced **82** LiteratureAtom objects. Counts by kind: `{'author_conclusion': 4, 'conflict_of_interest': 1, 'data_availability': 1, 'eligibility_criterion': 4, 'limitation': 5, 'method': 13, 'other': 3, 'outcome_definition': 10, 'population_description': 13, 'qualitative_result': 15, 'quantitative_result': 12, 'study_objective': 1}`.

Pydantic structural validation: **PASS**. JSON Schema validation: **PASS**. Atom-kind sufficiency validation: **PASS** with 0 errors and 0 warnings. Atom IDs are unique and all atoms share one publication ID. All model-extracted atoms remain `needs_review`.

The governing ATOM sources were `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom(1).json`; large-source execution used `large-source-ATOM-SEA.md`.

## SEA and coverage

All 8 main-article pages and all 11 supplied supplement pages were inspected. Coverage reconciled 4 main figures, 1 main table, 3 supplementary tables, and 6 supplementary sensitivity figures. SEA QA status: **PASS**.

Verdict: **Read first** for a formulary evidence review focused on empagliflozin versus dapagliflozin cardiovascular effectiveness. Primary pooled RRs were 0.91 for all-cause death, 1.12 for cardiovascular death, 1.01 for myocardial infarction, 0.90 for stroke, 1.03 for MACE, and 1.07 for heart failure-related events. None of the main pooled 95% CIs excluded 1, but heterogeneity was substantial and leave-one-out analysis made all-cause mortality and cardiovascular mortality statistically significant after excluding one influential study.

SEA v4 scores: relevance **9/10**, novelty **7/10**, method strength **5/10**, evidence strength **5/10**, external validity **7/10**, implementation value **6/10**.

## Source-integrity findings

1. The Abstract, Results, and Table 1-derived totals report 428,940 participants, while the Discussion strengths paragraph states 371,664.
2. PRISMA Figure 1 lists “observational studies” among excluded full-text reports although the Methods permit observational studies and all eight included studies are observational.
3. The conclusion discusses similar safety profiles and cost-effectiveness implications, but comparative safety and economic endpoints were not analyzed in the extracted outcome set.

No discrepancy was silently repaired.

## Reference task queue

The article contains **48** numbered references. They were converted to `mahboob-samad-2025-crd-0000000000000916-reference-task-queue.md` in source order. PDF line wrapping and soft-hyphen artifacts were normalized. No external bibliographic correction was performed.

## Output files

- `mahboob-samad-2025-crd-0000000000000916-atoms.json`
- `mahboob-samad-2025-crd-0000000000000916-validation.json`
- `mahboob-samad-2025-crd-0000000000000916-coverage.json`
- `mahboob-samad-2025-crd-0000000000000916-crosswalk.json`
- `mahboob-samad-2025-crd-0000000000000916-sea.html`
- `mahboob-samad-2025-crd-0000000000000916-sea-qa.json`
- `mahboob-samad-2025-crd-0000000000000916-reference-task-queue.md`
- `mahboob-samad-2025-crd-0000000000000916-processing-report.md`

JSON outputs belong in `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/JSON`. The SEA HTML belongs in `.../HTML`. Markdown files belong in `.../MD`.

No external verification was performed because `@VERIFY` was not activated.
