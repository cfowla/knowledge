# Processing report - Sun et al. 2014

## Source

- Title: The efficacy of dapagliflozin combined with hypoglycaemic drugs in treating type 2 diabetes mellitus: meta-analysis of randomised controlled trials
- Journal: BMJ Open. 2014;4:e004619
- DOI: 10.1136/bmjopen-2013-004619
- PMID: 24710132
- PROSPERO: CRD42013005034
- Main article: 11 pages, SHA-256 `901a1854f13676407f59ece892c09e2053436e7ffb95c8d6cf641dbb18e13b20`
- Supplement: 5 pages, SHA-256 `f773f4caa574c11c3312f41ed84f36dd214dc7cefbda0d8453282a7454f62e2b`
- Publication ID: `e1f5f0ae-5d97-5593-a9ad-e5611b8e48c5`

## ATOM

The extraction produced **79 LiteratureAtom objects** across six semantic runs. Counts by kind: `{"author_conclusion": 3, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 6, "funding_disclosure": 1, "intervention_description": 1, "limitation": 6, "method": 12, "other": 5, "outcome_definition": 3, "population_description": 2, "qualitative_result": 9, "quantitative_result": 18, "study_objective": 1, "subgroup_result": 9}`.

Pydantic structural validation passed with **0 errors**. JSON Schema validation passed with **0 errors**. Atom-kind sufficiency validation passed with **0 errors and 0 warnings**. Atom IDs are unique and all atoms share one publication ID. All model-assisted atoms remain `needs_review`.

The source is a systematic review/meta-analysis. Review-generated pooled estimates use the existing `quantitative_result` and `subgroup_result` kinds with secondary-source tags. Individual RCT rows reproduced in the review were not represented as if Sun et al. generated those primary-study observations.

## SEA and coverage

The 11-page main article and five-page supplement were mapped and visually reconciled. Coverage includes **6 main figures, 3 main tables, the Figure 1 study-selection workflow, and all 5 supplementary forest-plot appendices**. SEA QA passed.

Verdict: **Skim deeply**. The review is useful for early quantitative estimates of dapagliflozin add-on effects on HbA1c, fasting plasma glucose, and body weight. It should not stand alone for questions outside those endpoints.

SEA scores: relevance 7/10, novelty 7/10, method strength 6/10, evidence strength 6/10, external validity 5/10, implementation value 4/10.

## Source-integrity findings

- The abstract reverses the ordering of the two sensitivity-analysis result sets relative to the Results section: the abstract assigns -0.56/-1.11/-2.23 to exclusion of low-quality trials and -0.50/-1.08/-2.08 to exclusion of interim trials, whereas the Results section assigns them in the opposite way.
- GRADE Table 2 labels the HbA1c evidence as 3,986 participants from 14 studies, while the narrative Results section states that the HbA1c analysis included 12 randomized trials.
- GRADE Table 2 labels the body-weight evidence as 4,008 participants from 14 studies, while the narrative Results section states that the body-weight analysis included 12 randomized trials.
- Table 3 prints a fasting-plasma-glucose week coefficient of -0.01 with a 95% confidence interval of 0.004 to 0.012, an interval that is incompatible in sign with the printed point estimate; the Results prose also describes -1.52 as the follow-up-duration coefficient although Table 3 presents -1.52 as the intercept.
- The body-weight meta-regression is described as significant with R-squared 1 and p<0.01, while Table 3 prints a week estimate of -0.01 with 95% CI -0.02 to 0.01, which crosses zero; the source does not reconcile the difference.

No discrepancy was silently repaired.

## References and task queue

The main article contains **34 numbered references**. They were preserved in `sun-zhou-2014-e004619-references.md` with source numbering and printed bibliographic content retained. Line wrapping was normalized. Current processed-state reconciliation found **2/34 already complete** (refs 10 and 14) and **32/34 pending**. The Markdown file groups references into a model-inferred processing queue: included RCTs first, then related syntheses/protocol, methods/regulatory/bias context, and background sources. The priority grouping is not a source-reported evidence grade.

## Governing sources applied

ATOM precedence: `literature(1).py` -> `literature_atoms(1).py` -> `literature_atom.schema.json` -> `README(2).md` -> `example_atom(1).json` (illustrative only). Large-source execution used `large-source-ATOM-SEA.md` as a supplement. SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as governing protocol; the file's internal heading still says "Integrated Compact v3," which was treated as a version-label conflict rather than a reason to substitute the historical v3 HTML. `unslop.skill.md` was applied to prose artifacts.

No external verification was performed because `@VERIFY` was not activated.

## Output files

- `sun-zhou-2014-e004619-atoms.json`
- `sun-zhou-2014-e004619-validation.json`
- `sun-zhou-2014-e004619-coverage.json`
- `sun-zhou-2014-e004619-crosswalk.json`
- `sun-zhou-2014-e004619-sea.html`
- `sun-zhou-2014-e004619-sea-qa.json`
- `sun-zhou-2014-e004619-references.md`
- `sun-zhou-2014-e004619-processing-report.md`

Google Drive routing follows the established convention: JSON files under `GitHub Sync/Literature Review/Outputs/Clin Med Pharm/JSON`, SEA HTML under `.../HTML`, and Markdown reference queue plus processing report under `.../MD`.
