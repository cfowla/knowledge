# Processing report: Engström et al. 2024

## Source

- Title: Comparative cardiovascular and renal effectiveness of empagliflozin and dapagliflozin: Scandinavian cohort study
- Journal: European Heart Journal - Cardiovascular Pharmacotherapy. 2024;10:432–443
- DOI: 10.1093/ehjcvp/pvae045
- PMID: 38918063
- Main article: 12 pages, SHA-256 `229c65380fef58c49ff18d835ac26c23d60d1bfccd28d723656f836dc975a0c5`
- Supplement: 22-page DOCX appendix, SHA-256 `c4c5c72f99f5fbbe20c176212a8350332a85df43fff92a6852c140c24dc24ee1`
- Publication ID: `ab1e0f29-d16b-5052-9107-95fba7d645e4`

## ATOM

The extraction produced **94 LiteratureAtom objects** across 11 semantic extraction runs. Counts by kind: `{"author_conclusion": 3, "comparator_description": 1, "conflict_of_interest": 3, "data_availability": 1, "eligibility_criterion": 5, "exposure_description": 1, "funding_disclosure": 2, "limitation": 5, "method": 14, "outcome_definition": 8, "population_description": 3, "qualitative_result": 5, "quantitative_result": 25, "study_objective": 1, "subgroup_result": 17}`.

Pydantic structural validation passed with **0 errors**. JSON Schema validation passed with **0 errors**. Atom-kind sufficiency validation passed with **0 errors and 0 warnings**. Atom IDs are unique and all atoms share one publication ID. All model-assisted atoms remain `needs_review`.

The governing ATOM sources were `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, `README(2).md`, and the illustrative `example_atom(1).json`, with the project-defined authority order preserved.

## SEA and coverage

All 12 main-article PDF pages were rendered/inspected during source mapping. Coverage reconciled **3 main figures, 2 main tables, and Supplementary Tables S1–S12** from the supplied DOCX appendix. The final HTML was generated only after source mapping and quantitative/table reconciliation. SEA QA **passed**.

Verdict: **Read first** for a formulary evidence review focused on empirical empagliflozin-versus-dapagliflozin cardiorenal effectiveness. The main adjusted HRs were 1.02 (95% CI 0.97–1.08) for MACE, 1.05 (0.97–1.14) for heart failure, and 0.97 (0.87–1.07) for serious renal events; DKA HR was 1.12 (0.94–1.33). The study strongly supports a lack of large comparative cardiorenal differences in routine-practice type 2 diabetes, but it does not by itself establish full therapeutic interchangeability across current indications, inpatient use, cost, dosing, or all safety outcomes.

Scores under the SEA rubric: relevance 10/10, novelty 9/10, method strength 8/10, evidence strength 8/10, external validity 8/10, implementation value 9/10.

## Source-integrity findings

- Serious renal events for dapagliflozin are reported as **4.1/1000 person-years** in the abstract and Table 2 but **4.0/1000** in the Results narrative. The Table 2 value is retained in the normalized main-result atom.
- Supplementary Tables S8 and S11 show small differences in some Denmark adjusted incidence rates despite identical event counts and arm sizes; the source does not explain whether rates were recomputed.

## References

The main article contains **23 numbered references**, transcribed from printed page 443 to `engstrom-soderling-2024-pvae045-references.md`. PDF line wrapping and typographic punctuation were normalized. No external bibliographic correction was used.

## Output files

- `engstrom-soderling-2024-pvae045-atoms.json`
- `engstrom-soderling-2024-pvae045-validation.json`
- `engstrom-soderling-2024-pvae045-coverage.json`
- `engstrom-soderling-2024-pvae045-sea.html`
- `engstrom-soderling-2024-pvae045-sea-qa.json`
- `engstrom-soderling-2024-pvae045-references.md`
- `engstrom-soderling-2024-pvae045-processing-report.md`

Intended Google Drive GitHub Sync locations follow the existing project convention: JSON files under `Literature Review/Outputs/Clin Med Pharm/JSON`, the SEA HTML under `.../HTML`, and Markdown files under `.../MD`.

No external verification was performed because `@VERIFY` was not activated.
