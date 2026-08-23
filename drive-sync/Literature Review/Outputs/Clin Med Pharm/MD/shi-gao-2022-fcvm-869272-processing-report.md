# ATOM + SEA processing report: Shi et al. 2022

## Activated macros

- `@ATOM`
- `@SEA`

## Source

- Title: Comparative Efficacy of Dapagliflozin and Empagliflozin of a Fixed Dose in Heart Failure: A Network Meta-Analysis
- Authors: Zepeng Shi, Feng Gao, Wei Liu, Xuezhi He
- Journal: Frontiers in Cardiovascular Medicine
- Published: 2022-04-04
- DOI: `10.3389/fcvm.2022.869272`
- PMID: `35445086`
- Source type: systematic review and frequentist network meta-analysis of randomized controlled trials
- Source file: `fcvm-09-869272.pdf`
- Pages: 10
- SHA-256: `39119b9eea9bd72952b7ec5004e4e23a0dced3f8dcd84174eb5db14c59aaa04b`
- Shared publication ID: `86bc12bc-e0e4-5ee9-96d9-924e3538c3e0`

## Governing sources

ATOM precedence applied:

1. `literature.py`, retrieved as the project file `literature(1).py`, executed for structural Pydantic validation.
2. `literature_atoms.py`, retrieved as the project file `literature_atoms(1).py`, executed for sufficiency validation.
3. `literature_atom.schema.json`, executed for serialization validation.
4. `README(2).md`, searched but the exact file was not retrieved in the available project, File Library, or Drive sources.
5. `example_atom.json`, searched but the exact file was not retrieved in the available project, File Library, or Drive sources.

SEA precedence applied:

1. `summary-evaluation-appraisal-protocol-v4-compact.md`, treated as authoritative.
2. `summary-evaluation-appraisal-protocol-v3-compact.html`, historical/reference only.
3. Supplied primary review article.

The named v4 protocol file has an internal heading that still says "Integrated Compact v3." The project precedence names the v4 file as authoritative, so that file governed this run. `large-source-ATOM-SEA.md` was used as a supplementary coverage guardrail. `unslop.skill.md` was applied to prose artifacts.

## ATOM result

- Total atoms: **52**
- Counts by kind: `{"adverse_event": 3, "author_conclusion": 3, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 2, "intervention_description": 2, "limitation": 4, "method": 10, "outcome_definition": 6, "population_description": 2, "qualitative_result": 1, "quantitative_result": 15, "study_objective": 1}`
- Counts by assertion origin: `{"directly_reported": 2, "normalized_from_source": 50}`
- Semantic batches: `{"shi-gao-2022-interpretation-v1": 9, "shi-gao-2022-results-v1": 21, "shi-gao-2022-scope-methods-v1": 22}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Shared publication identity: **PASS**
- Duplicate atom IDs: **0**

The source is secondary evidence. Pooled and network quantitative atoms are tagged `secondary_reported_result`; they describe what this review reports about the underlying trials and do not imply that Shi et al. enrolled those participants. Active-agent network comparisons are tagged as indirect comparisons.

## Source integrity finding

Table 2 has a directionality conflict. Its footnote says each row is compared with each column, but placebo-row estimates are described in the Results text as active treatment versus placebo. The HF-exacerbation result has an additional conflict: OR 0.70, 95% CI 0.59-0.84 appears for dapagliflozin versus placebo and is also reported in narrative text as empagliflozin versus dapagliflozin. The corresponding atom keeps the narrative direction but carries `source_directionality_conflict` and `needs_source_adjudication` tags. The value should not be reused as a definitive active-agent estimate without source adjudication.

## SEA coverage and appraisal

- Main figures reconciled: **3/3**
- Main tables reconciled: **2/2**
- Study-selection workflow reconciled: **yes**
- Supplementary material supplied: **no**
- Cited but unavailable: Supplementary Tables S1-S2 and Supplementary Figures S1-S2
- References exported: **37/37**
- Final SEA verdict: **Do not use for practice as a stand-alone comparative-choice source.**

Protocol scores assigned after extraction and visual reconciliation:

- Relevance: **8/10**
- Novelty: **7/10**
- Method strength: **4/10**
- Evidence strength: **3/10**
- External validity: **4/10**
- Implementation value: **3/10**

The main reason for the low comparative-evidence score is that the dapagliflozin versus empagliflozin ranking is indirect. Trial populations differ in HF phenotype, comorbidity, functional class, background treatment, and follow-up. The supplied supplement is absent, no certainty framework is reported in the main article, and the matrix direction has an internal reporting conflict.

## References

The article bibliography contains 37 numbered references. Source numbering is preserved in `shi-gao-2022-fcvm-869272-references.md`. Line wrapping and split DOI strings were normalized from the PDF text layer. No external bibliography lookup or correction was used.

## Output files

JSON:
- `shi-gao-2022-fcvm-869272-atoms.json`
- `shi-gao-2022-fcvm-869272-validation.json`
- `shi-gao-2022-fcvm-869272-coverage.json`

HTML:
- `shi-gao-2022-fcvm-869272-sea.html`

Markdown:
- `shi-gao-2022-fcvm-869272-references.md`
- `shi-gao-2022-fcvm-869272-processing-report.md`

Additional QA file:
- `shi-gao-2022-fcvm-869272-sea-qa.json`
