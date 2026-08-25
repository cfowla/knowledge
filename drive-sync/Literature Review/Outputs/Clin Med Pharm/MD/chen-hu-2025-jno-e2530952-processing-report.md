# GLP-1 RAs and Cardiovascular and Kidney Outcomes by Body Mass Index in Type 2 Diabetes: ATOM + SEA processing report

## Source packet

- Requested Drive folder: `3 - TBR / 2 - 10 - Active Literature / 1 - Clinical Medicine & Pharmacy / 144 - Chen Hu 2025 - Supplement Only - Needs Main`
- Raw Drive files found: **1**, `zoi250869supp1_prod_1756497055.58921.pdf`
- Main article file in Drive: **not found**
- Main article recovered from canonical JAMA Network Open HTML using DOI `10.1001/jamanetworkopen.2025.30952`
- Supplement 2 Data Sharing Statement: **not present in the Drive folder**

## ATOM

- Atoms: **51**
- Counts by kind: `{"adverse_event": 4, "author_conclusion": 2, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 1, "exposure_description": 1, "funding_disclosure": 1, "limitation": 4, "method": 5, "outcome_definition": 3, "population_description": 3, "qualitative_result": 9, "study_objective": 1, "subgroup_result": 14}`
- Counts by batch: `{"chen-hu-2025-jno-e2530952-design-v1": 15, "chen-hu-2025-jno-e2530952-interpretation-v1": 9, "chen-hu-2025-jno-e2530952-primary-results-v1": 18, "chen-hu-2025-jno-e2530952-sensitivity-v1": 9}`
- Structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Sufficiency warnings: **0**
- All atoms use one publication ID and remain `needs_review`.

## SEA and coverage

- Main article figures/tables reconciled: **5/5**
- Supplement 1 pages rendered and visually inspected: **40/40**
- Supplement tables/figures reconciled: **16/16**
- Final SEA scoring was assigned after extraction and visual reconciliation.
- Verdict: **Read soon. Do not use this study alone as a BMI-based prescribing rule.**

## References

- Primary bibliography entries exported: **49/49**
- Output: `chen-hu-2025-jno-e2530952-reference-task-queue.md`
- The supplement eReferences were not substituted for the primary article bibliography.

## Governing sources applied

ATOM precedence: `literature(1).py` -> `literature_atoms(1).py` -> `literature_atom.schema.json` -> `README(2).md` -> `example_atom(1).json`.

SEA: `summary-evaluation-appraisal-protocol-v4-compact.md`. Large-source guidance: `large-source-ATOM-SEA.md`. Writing control: `unslop.skill.md`.

## Limitations

- The target Drive folder contains Supplement 1 only. The primary article file is absent; exact citation and DOI were taken from the supplement and the canonical JAMA Network Open full-text HTML was used to recover the main article content needed for ATOM, SEA, and the primary bibliography.
- The raw main-article PDF was not available in the target Drive folder. Main-article visual content was reconciled from the journal HTML figure/table objects rather than a locally retrieved main PDF.
- Supplement 2, which contains the Data Sharing Statement, was not present in the Drive folder and was not inspected.
- The study is observational. Association estimates were not converted into causal treatment effects.
- Not every baseline characteristic or every sensitivity-table cell was atomized. The extraction prioritizes independently reviewable design assertions, central matched outcomes, key sensitivity findings, limitations, and disclosures.
- All model-extracted atoms remain needs_review because no independent human verification step is represented.

## Output files

- `chen-hu-2025-jno-e2530952-atoms.json`
- `chen-hu-2025-jno-e2530952-validation.json`
- `chen-hu-2025-jno-e2530952-coverage.json`
- `chen-hu-2025-jno-e2530952-crosswalk.json`
- `chen-hu-2025-jno-e2530952-sea-qa.json`
- `chen-hu-2025-jno-e2530952-sea.html`
- `chen-hu-2025-jno-e2530952-reference-task-queue.md`
- `chen-hu-2025-jno-e2530952-processing-report.md`

Generated 2026-08-25T02:23:27Z.
