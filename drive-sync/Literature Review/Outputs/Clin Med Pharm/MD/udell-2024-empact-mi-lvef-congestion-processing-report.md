# Udell 2024 EMPACT-MI LVEF and congestion processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Main article: `udell-et-al-2024-left-ventricular-function-congestion-and-effect-of-empagliflozin-on-heart-failure-risk-after.pdf`
- Supplemental material: `mmc1.docx`
- Title: *Left Ventricular Function, Congestion, and Effect of Empagliflozin on Heart Failure Risk After Myocardial Infarction*
- Citation: J Am Coll Cardiol. 2024;83(23):2233-2246.
- DOI: `10.1016/j.jacc.2024.03.405`
- Trial: EMPACT-MI, `NCT04509674`
- Source type: prespecified secondary analysis of an international randomized, double-blind, placebo-controlled trial
- Main PDF SHA-256: `b8f4599e8803071ae459ec90f8506feb44e7336a9dbcebacb6d967276f050159`
- Supplement SHA-256: `136bf28c622ec286cf844aaaaf712665cd4452df42c1b47dae62420cb91950a5`
- Shared publication ID: `c7c94ae1-11c9-5e17-8fd4-f8340ffcbc89`

## ATOM result

- LiteratureAtoms: **77**
- Atom kinds: `{"adverse_event": 5, "author_conclusion": 4, "comparator_description": 1, "conflict_of_interest": 1, "eligibility_criterion": 3, "funding_disclosure": 1, "intervention_description": 1, "limitation": 4, "method": 9, "outcome_definition": 4, "population_description": 8, "qualitative_result": 4, "quantitative_result": 13, "study_objective": 1, "subgroup_result": 18}`
- Semantic batches: `{"udell-2024-empact-mi-global-v1": 20, "udell-2024-empact-mi-baseline-v1": 7, "udell-2024-empact-mi-placebo-risk-v1": 10, "udell-2024-empact-mi-treatment-v1": 20, "udell-2024-empact-mi-exploratory-safety-v1": 10, "udell-2024-empact-mi-discussion-v1": 10}`
- Assertion origin: `{"normalized_from_source": 77}`
- Review status: `needs_review` for all atoms
- Local strict Pydantic contract validation: **PASS**
- Local generated JSON Schema validation: **PASS**
- Sufficiency validation for extracted kinds: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Duplicate atom IDs: **0**
- Exact duplicate canonical statements: **0**

The extraction keeps randomized treatment effects separate from prognostic placebo-arm associations. Baseline LVEF and congestion are exposures in the prognostic analyses, not randomized interventions. The dense five-way treatment forest plot is reconciled in SEA rather than converted into 15 additional near-duplicate atoms.

## SEA result

The main article and supplement were reconciled before appraisal. Coverage includes the main Table 1, Figures 1-4, the Central Illustration, Supplemental Figure 1, Supplemental Tables 1-4, and all four panels of Supplemental Figure 2.

Verdict: **Read soon.** Read the parent EMPACT-MI primary report first for the primary trial result. Use this analysis for the LVEF-congestion risk gradient, recurrent HF hospitalization effects, and evidence that the randomized empagliflozin HF hospitalization effect did not materially vary across the enrolled LVEF and congestion phenotypes.

The source supports fewer first and recurrent HF hospitalizations. It does not support an all-cause mortality benefit, a claim that one small subgroup benefits more than another, or extrapolation to post-MI patients with preserved LVEF and no congestion who were not meaningfully represented.

## Source-integrity finding

Supplemental Table 3 prints diastolic blood pressure in the congestion group as `19.8 ±14.6 mmHg`, compared with `73.5 ±9.9 mmHg` without congestion, with `P=0.5082`. The value is internally implausible and inconsistent with the surrounding blood-pressure data. It was not silently corrected and was not used as an atomized quantitative result.

## References

The article's **28** printed references were exported in source order to `udell-2024-empact-mi-lvef-congestion-references.md`. Bibliography entries were not atomized.

## Governing-source execution boundary

The uploaded `large-source-ATOM-SEA.md` workflow and retrieved `unslop.skill.md` were applied. The named authoritative files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, `example_atom.json`, and the exact `summary-evaluation-appraisal-protocol-v4-compact.md` were searched in connected project sources but were not directly retrievable in this session.

ATOM validation therefore uses a strict local Pydantic contract and generated JSON Schema reconstructed from current validated project LiteratureAtom outputs, plus the sufficiency rules in the retrieved large-source workflow. The SEA follows the retrieved large-source workflow and available project appraisal pattern. This run does not claim execution of the unavailable authoritative code or exact v4 scoring rubric.

No external verification was performed because `@VERIFY` was not activated.

## Output files

- `udell-2024-empact-mi-lvef-congestion-atoms.json`
- `udell-2024-empact-mi-lvef-congestion-validation.json`
- `udell-2024-empact-mi-lvef-congestion-coverage.json`
- `udell-2024-empact-mi-lvef-congestion-sea.html`
- `udell-2024-empact-mi-lvef-congestion-references.md`
- `udell-2024-empact-mi-lvef-congestion-processing-report.md`
