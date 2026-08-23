# Processing report: Bu et al. 2025

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Title: Empagliflozin and Dapagliflozin Outcomes in Heart Failure
- Journal: JAMA Network Open. 2025;8(12):e2546865.
- DOI: `10.1001/jamanetworkopen.2025.46865`
- Main article: 12 pages, SHA-256 `088d779aa37cfdc3709f6c929ef96583e1a7bbefd101e2d7cc159310b8c122dd`
- Supplement 1: 22 pages, SHA-256 `cf812bfb5c1f808d9ec63935d279788d85d6787e6f439f9f0f6555c03b432238`
- Supplement 2: referenced by the article but not present in the input packet
- Shared publication ID: `1c8de0d1-7ee6-5ef0-8605-0602b9ab0966`

## ATOM status

The extraction produced **56** LiteratureAtom objects across semantic batches. Counts by kind: `{'author_conclusion': 1, 'conflict_of_interest': 1, 'data_availability': 1, 'eligibility_criterion': 2, 'exposure_description': 2, 'limitation': 4, 'method': 9, 'outcome_definition': 5, 'population_description': 5, 'qualitative_result': 11, 'quantitative_result': 10, 'study_objective': 1, 'subgroup_result': 4}`.

Authoritative Pydantic structural validation: **PASS**. JSON Schema validation: **PASS**. Atom-kind sufficiency validation: **PASS** with 0 errors and 0 warnings. Atom IDs are unique and all atoms share one publication ID. All model-extracted atoms remain `needs_review`.

The governing ATOM sources were `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom(1).json`; large-source execution followed `large-source-ATOM-SEA.md`.

## SEA and coverage

All 12 main-article pages and all 22 Supplement 1 pages were inspected. Coverage reconciled **4 main tables, 1 main 5-panel figure, 11 supplemental tables, and 4 supplemental figures**. SEA QA status: **PASS**.

Verdict: **Read first** for an empagliflozin-versus-dapagliflozin heart-failure formulary evidence review. The matched primary result was AHR **0.99 (95% CI 0.83-1.19; P=.95)**, with no significant heterogeneity across LVEF groups (interaction P=.32). The IPTW sensitivity result was HR **0.93 (0.79-1.10; P=.420)**. The paper supports absence of an observed large effectiveness difference in this cohort but does **not** prove therapeutic equivalence or interchangeability.

SEA v4 scores: relevance **9/10**, novelty **7/10**, method strength **7/10**, evidence strength **6/10**, external validity **6/10**, implementation value **8/10**.

## Source-integrity findings

1. The article reports CV-death AHR 0.94 (95% CI 0.67-1.32) with P=.94. The P value appears numerically discordant with the HR/CI relationship under usual Wald inference; the source value was preserved and not silently corrected.
2. Supplement eTable 11 labels its estimates `HR`, while a copied footnote describes adjusted HRs; the extraction preserves the table header as `HR` rather than assuming additional adjustment.
3. Supplement 2 was absent from the packet; only the article's statement `Data Sharing Statement: See Supplement 2` was extracted.

## Reference task queue

The article contains **19** numbered references. They were converted to `bu-jung-2025-jamanetworkopen-2025-46865-reference-task-queue.md` in source order. PDF line wrapping was normalized. No external bibliographic correction was performed.

## Output files

- `bu-jung-2025-jamanetworkopen-2025-46865-atoms.json`
- `bu-jung-2025-jamanetworkopen-2025-46865-validation.json`
- `bu-jung-2025-jamanetworkopen-2025-46865-coverage.json`
- `bu-jung-2025-jamanetworkopen-2025-46865-crosswalk.json`
- `bu-jung-2025-jamanetworkopen-2025-46865-sea.html`
- `bu-jung-2025-jamanetworkopen-2025-46865-sea-qa.json`
- `bu-jung-2025-jamanetworkopen-2025-46865-reference-task-queue.md`
- `bu-jung-2025-jamanetworkopen-2025-46865-processing-report.md`

JSON outputs belong in `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/JSON`. The SEA HTML belongs in `.../HTML`. Markdown files belong in `.../MD`.
