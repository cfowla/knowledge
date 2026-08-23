# ATOM + SEA processing report: Kani et al. 2024

## Activated macros

- `@ATOM`
- `@SEA`

## Source

- Title: Comparison of Effectiveness Among Different Sodium-Glucose Cotransoporter-2 Inhibitors According to Underlying Conditions: A Network Meta-Analysis of Randomized Controlled Trials
- Authors: Ryoma Kani; Atsuyuki Watanabe; Yoshihisa Miyamoto; Kentaro Ejiri; Masao Iwagami; Hisato Takagi; Leandro Slipczuk; Yusuke Tsugawa; Tadao Aikawa; Toshiki Kuno
- Journal: Journal of the American Heart Association
- Citation: J Am Heart Assoc. 2024;13:e031805
- DOI: `10.1161/JAHA.123.031805`
- Source type: systematic review and frequentist network meta-analysis of placebo-controlled randomized trials
- Main source: supplied 10-page PDF
- Supplement: supplied 50-page PDF
- Main PDF SHA-256: `da1f15a92799300cab0a13a69c99e7dd5b61d6e36daf761c365bea660234f4f1`
- Supplement SHA-256: `5089c1636ef6a4f1120ba0a376272fe487439e74c79ec154c3b16a85779e4798`
- Shared publication ID: `03acb063-1ad9-5875-a8dd-eb1542fcb467`

The exact published title spells `Cotransoporter-2`; this source wording is preserved rather than silently corrected.

## Governing sources

ATOM precedence applied as specified by the project: `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, then `example_atom.json`. The Pydantic model, JSON Schema, and sufficiency validator were executed directly from the supplied project sources. SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as authoritative and the v3 HTML only as historical reference. `large-source-ATOM-SEA.md` supplied the combined-workflow coverage rules. `unslop.skill.md` was applied to prose artifacts.

The v4-named protocol retains an internal v3 heading. Project source precedence names the v4 file as authoritative, so the v4-named file governed this run.

## ATOM result

- Total atoms: **90**
- Counts by kind: `{"author_conclusion": 3, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 6, "funding_disclosure": 1, "intervention_description": 1, "limitation": 8, "method": 10, "outcome_definition": 6, "population_description": 4, "qualitative_result": 24, "quantitative_result": 10, "study_objective": 1, "subgroup_result": 13}`
- Counts by assertion origin: `{"normalized_from_source": 90}`
- Semantic batches: `{"kani-watanabe-2024-jaha-e031805-interpretation-v1": 17, "kani-watanabe-2024-jaha-e031805-overall-results-v1": 8, "kani-watanabe-2024-jaha-e031805-scope-methods-v1": 31, "kani-watanabe-2024-jaha-e031805-sensitivity-safety-v1": 22, "kani-watanabe-2024-jaha-e031805-subgroup-results-v1": 12}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Duplicate atom IDs: **0**

This source is secondary evidence. Network-result atoms are tagged as secondary and indirect where applicable. They do not imply that Kani et al. enrolled the underlying trial participants.

## Source and evidence integrity

The network contains only placebo-controlled trial edges. Active-agent comparisons are indirect, and there are no closed loops for a direct-versus-indirect inconsistency check. The main-text screening sentence is compressed, so precise study-flow counts were taken from Supplementary Figure S1 rather than reconstructed from ambiguous wording. Exact orthostatic-hypotension pairwise estimates were not recoverable from the graph text layer and were retained qualitatively rather than invented.

## SEA coverage and appraisal

- Main figures reconciled: **4/4**
- Main tables: **0**
- Supplementary tables reconciled: **32/32**
- Supplementary figures reconciled: **11/11**
- PRISMA study-selection workflow reconciled: **yes**
- References exported: **67/67**
- Final verdict: **Read soon for comparative class and formulary context; do not use as a stand-alone agent-selection hierarchy.**

Protocol scores assigned after extraction and visual reconciliation:

- Relevance: **8/10**
- Novelty: **7/10**
- Method strength: **6/10**
- Evidence strength: **5/10**
- External validity: **6/10**
- Implementation value: **5/10**

No external current-practice verification was performed because `@VERIFY` was not activated.

## References

The Markdown reference artifact contains all **67** numbered references from the main article in source order. Obvious PDF text-layer line breaks and split DOI spacing were normalized. The bibliography was not atomized.

## Output files

JSON:
- `kani-watanabe-2024-jaha-e031805-atoms.json`
- `kani-watanabe-2024-jaha-e031805-validation.json`
- `kani-watanabe-2024-jaha-e031805-coverage.json`
- `kani-watanabe-2024-jaha-e031805-sea-qa.json`

HTML:
- `kani-watanabe-2024-jaha-e031805-sea.html`

Markdown:
- `kani-watanabe-2024-jaha-e031805-references.md`
- `kani-watanabe-2024-jaha-e031805-processing-report.md`
