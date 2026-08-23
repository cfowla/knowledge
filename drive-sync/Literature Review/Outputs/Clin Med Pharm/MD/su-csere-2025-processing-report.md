# Su Csere 2025 processing report

## Source packet
- Primary article: `1-s2.0-S0168822725002335-main.pdf`, *Comparative efficacy and safety of SGLT2 inhibitor class members in patients with heart failure and type 2 diabetes: A systematic review and network meta-analysis of randomized controlled trials*; DOI `10.1016/j.diabres.2025.112219`; PMID `40324721`.
- Supplement: `1-s2.0-S0168822725002335-mmc1.docx`, 93 rendered pages in the supplied DOCX, containing Secondary Results S1, Methods S1 search strategies, 11 supplementary tables, 74 supplementary figures, and secondary RCT references.
- Main SHA-256: `d50081d6d95067f15a59f8624854a16c0388a4874fe9aac481825fe71148b9b3`
- Supplement SHA-256: `db632dead8f91c3105785288467efd4debf392d979a6cd21811762ba9c285adc`

## ATOM
- Publication ID: `19ab7f87-e1a6-4977-8e1c-3973f90327ac`
- Atoms: **120**
- Counts by kind: `{'adverse_event': 15, 'author_conclusion': 2, 'comparator_description': 1, 'conflict_of_interest': 1, 'data_availability': 1, 'eligibility_criterion': 2, 'funding_disclosure': 1, 'intervention_description': 1, 'limitation': 13, 'method': 8, 'outcome_definition': 22, 'population_description': 4, 'qualitative_result': 7, 'quantitative_result': 31, 'study_objective': 1, 'subgroup_result': 10}`
- Pydantic structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Exact duplicate canonical statements: **0**
- Status: **PASS**

### Schema fit
The current LiteratureAtom model is primary-literature oriented and has no dedicated systematic-review/meta-analysis/NMA result kind. Review-level pooled and network estimates were therefore represented with existing `quantitative_result`, `adverse_event`, and `subgroup_result` kinds and tagged `secondary_reported_result`, `systematic_review`, and/or `network_meta_analysis`. No atom implies that Su et al. directly enrolled the participants summarized by the review.

## SEA coverage
- Main figures: **3/3 reconciled** (PRISMA, primary forest plots, primary rank heat).
- Main tables: **2/2 reconciled** (Table 1 multi-page characteristics; Table 2 GRADE Summary of Findings).
- Supplementary tables: **11/11 reconciled**.
- Supplementary figures: **74/74 reconciled**, grouped by semantic family in the coverage manifest and SEA.
- SEA QA: **PASS**.

## Source-consistency flags preserved
- HHF quality-of-evidence label differs across abstract/Table 2 versus Results prose.
- Supplementary Results S1/Figure S5 support hypotension HR **1.17 (95% CI 1.01–1.34)**; parsed main-text wording contains an inconsistent 1.71 value despite describing a 17% increase.
- Supplementary Results S1/Figure S33 report eGFR MD **+3.00 mL/min/1.73 m² (95% CI 1.71–4.30)**, conflicting with the direction/value shown in Table 2.
- Authors explicitly note that CANVAS Program incidence-only reporting prevented RR calculation for several outcomes, causing some Summary-of-Findings versus HR-forest differences.

## Reference task queue
- **50** numbered article references preserved in `su-csere-2025-reference-task-queue.md`.
- References **21–37** are the 17 included RCTs and are Priority A independent ATOM/SEA targets.
- References 1–20 and 38–50 are retained as guidelines, prior syntheses, methods, background, or comparative/real-world context and assigned lower queue priority.

## Project-source governance
- ATOM authority: `literature(1).py` → `literature_atoms(1).py` → `literature_atom.schema.json` → `README(2).md` → `example_atom(1).json`.
- SEA authority: supplied `summary-evaluation-appraisal-protocol-v4-compact.md`; separate v3 HTML treated as historical/reference only.
- Large-source rules from `large-source-ATOM-SEA.md` were applied to semantic batching, shared publication identity, supplement reconciliation, validation, and whole-source synthesis.
- No external web verification was used.

## Output routing
- JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`
- SEA HTML: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`
- Reference task queue and processing report: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`
