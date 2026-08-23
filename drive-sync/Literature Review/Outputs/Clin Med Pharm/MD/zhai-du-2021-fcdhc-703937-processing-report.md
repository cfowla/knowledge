# Processing report — Zhai Du 2021

## Source
- Title: The Effects of Dapagliflozin in Patients With Heart Failure Complicated With Type 2 Diabetes: A Meta-Analysis of Placebo-Controlled Randomized Trials
- Authors: Miaobo Zhai; Xin Du; Changmei Liu; Huipu Xu
- Journal: Frontiers in Clinical Diabetes and Healthcare
- Published: 30 June 2021
- DOI: 10.3389/fcdhc.2021.703937
- PMID: 36994345
- Source file: `fcdhc-02-703937.pdf`
- SHA-256: `a6db314a49edc0aa933935f72e222b4c712e2b2b1f6d3ac1b2517c08dfea30d3`

## ATOM
- LiteratureAtoms: 60
- Counts by kind: author_conclusion=2, comparator_description=1, conflict_of_interest=1, data_availability=1, eligibility_criterion=7, intervention_description=1, limitation=5, method=14, other=6, outcome_definition=3, population_description=4, qualitative_result=3, quantitative_result=4, study_objective=1, subgroup_result=7
- Pydantic structural validation: PASS
- JSON Schema validation: PASS
- Sufficiency validation: PASS
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate atom IDs: 0

### Source consistency flags preserved
1. McMurray 2019 diabetic-subgroup count is reported as 2,139 and then 2,319; Table 1 lists full trial arms 2,373 + 2,371.
2. Figure 3C gives ACM OR 0.79 (95% CI 0.66-0.94), while prose/abstract give OR 0.76 with the same CI.
3. Abstract HFrEF CVD/ACM heterogeneity and ACM effect values conflict with the main Results/Figure 4.
4. Figure 1's report-retrieval and eligibility boxes are n=0 despite five included studies.
5. Discussion says two trials were large and “the other four” were small although only five total trials were included.

## SEA
- Main-text figures reconciled: 5/5
- Main-text tables reconciled: 2/2
- Trial sequential analysis reconciled: yes
- Separate supplement in selected source packet: no
- SEA QA: PASS
- Verdict: Do not use for practice; retain as a historical synthesis and source map to primary trials.

## References
- Bibliography entries extracted: 50
- Output format: Markdown
- Reference numbering preserved: 1–50

## Extraction limitations
- The source is a secondary meta-analysis. Atoms represent the review's methods, pooled results, and reported interpretation; they do not convert underlying trial findings into primary-study atoms.
- No separate supplementary file was present in the selected materials folder.
- No external evidence update was performed.
