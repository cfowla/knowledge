# Processing report

## Source

- Folder: `Henry Strange 2018`
- Title: Effects of Dapagliflozin on 24-Hour Glycemic Control in Patients with Type 2 Diabetes: A Randomized Controlled Trial
- Journal: Diabetes Technology & Therapeutics. 2018;20(11):715–724
- DOI: `10.1089/dia.2018.0052`
- PMID: `30222367`
- PMCID: `PMC6208164`
- Source-package note: the Drive folder contained nine publisher supplementary PDFs but not the main article PDF; the exact open-access primary article was resolved by DOI/PMID/PMCID and used for whole-source extraction.

## ATOM

- Atoms: **53**
- Kinds: `{"adverse_event": 5, "author_conclusion": 2, "comparator_description": 1, "conflict_of_interest": 1, "eligibility_criterion": 3, "funding_disclosure": 1, "intervention_description": 1, "limitation": 6, "method": 7, "outcome_definition": 4, "population_description": 3, "quantitative_result": 14, "study_objective": 1, "subgroup_result": 4}`
- Semantic batches: `{"henry-strange-2018-design-population-v1": 16, "henry-strange-2018-primary-glycemia-v1": 11, "henry-strange-2018-safety-interpretation-v1": 15, "henry-strange-2018-secondary-variability-v1": 11}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

The study-level publication identity is shared across every atom. Subgroup and secondary P values were preserved as nominal where the source says confirmatory treatment-difference inference should not be made. Two appraisal-derived limitations (short duration and surrogate-outcome scope) are explicitly marked `assertion_origin=extractor_inference`.

## SEA

Coverage reconciled all **3 main figures, 3 main tables, 5 supplementary figures, and 4 supplementary tables (15 total)**. Every visual/table was represented as a structured block. Main-article PDF screenshots were attempted but the web screenshot endpoint returned cache-miss errors; parsed primary-PDF text/captions and the supplied supplementary PDFs supported the structured reconstruction. SEA mechanical QA: **PASS**.

## Key appraisal constraints

1. The trial was powered only for the overall primary treatment comparison; secondary/exploratory and stratum P values were nominal.
2. The insulin stratum allowed rapid-acting mealtime insulin, dose changes were at investigator discretion, and detailed insulin-dose information was not collected.
3. Metformin and insulin strata differed in baseline disease severity, limiting causal interpretation of between-stratum differences.
4. Four weeks and N=100 are inadequate for uncommon or long-term safety outcomes.
5. Outcomes are glycemic/CGM surrogates, not cardiovascular, renal, hospitalization, or mortality endpoints.
6. AstraZeneca supported the study and funded medical-writing/editorial assistance; several authors reported AstraZeneca employment, stock, consulting, or other relationships.

## References

The article contains **24** numbered references. They were exported to `Henry-Strange-2018-Dapagliflozin-24h-Glycemic-Control-references.md` with PDF line wrapping normalized and without independent bibliographic correction.

## Governing-source boundary

Applied: `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, `README(2).md`, `example_atom(1).json`, `large-source-ATOM-SEA.md`, `summary-evaluation-appraisal-protocol-v4-compact.md`, and `unslop.skill.md`. The style skill was retrieved from File Library and applied to prose artifacts.

## Output files

- `Henry-Strange-2018-Dapagliflozin-24h-Glycemic-Control-atoms.json`
- `Henry-Strange-2018-Dapagliflozin-24h-Glycemic-Control-validation.json`
- `Henry-Strange-2018-Dapagliflozin-24h-Glycemic-Control-coverage.json`
- `Henry-Strange-2018-Dapagliflozin-24h-Glycemic-Control-crosswalk.json`
- `Henry-Strange-2018-Dapagliflozin-24h-Glycemic-Control-sea.html`
- `Henry-Strange-2018-Dapagliflozin-24h-Glycemic-Control-sea-qa.json`
- `Henry-Strange-2018-Dapagliflozin-24h-Glycemic-Control-references.md`
- `Henry-Strange-2018-Dapagliflozin-24h-Glycemic-Control-processing-report.md`
