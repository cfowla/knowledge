# ATOM + SEA processing report: Chen et al. 2023

## Activated macros

- `@ATOM`
- `@SEA`

## Source

- Title: Indirect comparison of SGLT2 inhibitors in patients with established heart failure: evidence based on Bayesian methods
- Authors: Hai-Bin Chen, Yao-Lin Yang, Rong-Sen Meng, Xue-Wei Liu
- Journal: ESC Heart Failure
- Published online: 2023-01-26
- DOI: `10.1002/ehf2.14297`
- PMID: `36702979`
- Source type: systematic review and Bayesian network meta-analysis of randomized controlled trials
- Main source: supplied PDF, 11 pages, journal pages 1231-1241
- Supplement: supplied 12-page DOCX
- PDF SHA-256: `ede2e54a8b827b4f26775ca70b734bffad20fa2d3fdf0cf3334ba646628b15f9`
- Supplement SHA-256: `36412d7e8c81162b7609890d25b5c8ec9bb6565d722d3d545dc105836149b8a2`
- Shared publication ID: `af351849-06e1-56bd-a3be-fcc37b27e1c5`

## Governing sources

ATOM precedence applied:

1. `literature.py`, available as `literature(1).py`, used for Pydantic structural validation.
2. `literature_atoms.py`, available as `literature_atoms(1).py`, used for sufficiency validation.
3. `literature_atom.schema.json`, used for JSON Schema validation.
4. `README(2).md` was not available in the supplied project-source set.
5. `example_atom.json` was not available in the supplied project-source set.

SEA precedence applied:

1. `summary-evaluation-appraisal-protocol-v4-compact.md`, treated as authoritative.
2. v3 protocol material, historical reference only.
3. The supplied main article and supplement.

The v4-named protocol file retains an internal v3 heading. Project precedence names the v4 file as authoritative, so the v4-named file governed this run. `large-source-ATOM-SEA.md` supplied the coverage and secondary-source guardrails. `unslop.skill.md` governed prose cleanup.

## ATOM result

- Total atoms: **68**
- Counts by kind: `{"author_conclusion": 2, "comparator_description": 1, "conflict_of_interest": 1, "eligibility_criterion": 3, "funding_disclosure": 1, "intervention_description": 1, "limitation": 6, "method": 11, "outcome_definition": 4, "population_description": 4, "qualitative_result": 5, "quantitative_result": 20, "study_objective": 1, "subgroup_result": 8}`
- Counts by assertion origin: `{"calculated_from_reported_data": 1, "directly_reported": 2, "extractor_inference": 1, "normalized_from_source": 64}`
- Semantic batches: `{"chen-yang-2023-ehf2-14297-interpretation-v1": 10, "chen-yang-2023-ehf2-14297-results-v1": 32, "chen-yang-2023-ehf2-14297-scope-methods-v1": 21, "chen-yang-2023-ehf2-14297-supplement-v1": 5}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Duplicate atom IDs: **0**

This is secondary evidence. Result atoms are tagged to show that the network analysis summarizes underlying randomized trials. The atoms do not imply that Chen et al. enrolled those trial participants.

## Source integrity findings

The main endpoint sections repeatedly state that five trials and 21,927 patients were included. The arm denominators in Supplementary Table S3 sum to 21,947. The difference is 20 participants. The extraction preserves 21,927 as the source-reported analysis population and 21,947 as a calculated value from the reported table.

The Methods say publication bias was not assessed because the review included few studies. The Results and supplement still show funnel plots and describe mild asymmetry. This was retained as a reporting tension, not converted into a formal publication-bias result.

## SEA coverage and appraisal

- Main figures reconciled: **5/5**
- Main tables reconciled: **1/1**
- Supplementary figures reconciled: **7/7**
- Supplementary tables reconciled: **3/3**
- Trial-selection workflow reconciled: **yes**
- References exported: **30/30**
- Final verdict: **Read soon for formulary context, but do not use as the stand-alone comparative-choice source.**

Scores assigned after extraction and figure/table reconciliation:

- Relevance: **9/10**
- Novelty: **6/10**
- Method strength: **5/10**
- Evidence strength: **4/10**
- External validity: **5/10**
- Implementation value: **4/10**

All active-agent 95% intervals cross the null. The ranking probabilities are descriptive and do not establish superiority. The paper can support an argument that no efficacy difference was detected in this network. It cannot prove dapagliflozin and empagliflozin are therapeutically equivalent.

## Output files

JSON:
- `chen-yang-2023-ehf2-14297-atoms.json`
- `chen-yang-2023-ehf2-14297-validation.json`
- `chen-yang-2023-ehf2-14297-coverage.json`
- `chen-yang-2023-ehf2-14297-sea-qa.json`

HTML:
- `chen-yang-2023-ehf2-14297-sea.html`

Markdown:
- `chen-yang-2023-ehf2-14297-references.md`
- `chen-yang-2023-ehf2-14297-processing-report.md`
