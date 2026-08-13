# dkag280 — ATOM/SEA processing, validation, and coverage note

## Source identity
- Source ID: `dkag280`
- Exact title: Differential salivary disposition of linezolid and its two major metabolites (PNU-142300 and PNU-142586) after a single dose in healthy adults
- Source type: journal article; exploratory single-dose pharmacokinetic study using stored samples from a prior study
- DOI: 10.1093/jac/dkag280
- Primary source file: `dkag280.pdf`
- SHA-256: `9760f024d8a20af658e2fcee6f8296aab2f179e7f230060d8c02a94ac6533912`
- Corresponding correction/supplement: none specified; none substituted

## Existing-artifact check
Before processing, the target Google Drive output folders (`HTML`, `JSON`, `MD`) were searched for `dkag280` and for the unmistakable title phrase “Differential salivary disposition”. No matching completed ATOM or SEA artifact was found, so this was processed as a new article.

## @ATOM validation
- Atom count: **64**
- Structural validation (Pydantic): **PASS**
- Serialization validation (`literature_atom.schema.json`): **PASS**
- Sufficiency validation (`literature_atoms.py`): **PASS**
- Structural errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

### Atom counts by kind
- `author_conclusion`: 3
- `conflict_of_interest`: 1
- `data_availability`: 1
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 6
- `method`: 10
- `population_description`: 1
- `qualitative_result`: 4
- `quantitative_result`: 35
- `study_objective`: 1

### Assertion-origin handling
The extraction preserves the project distinction between directly reported and normalized assertions. No extractor-inference or calculated-from-reported-data atoms were created for this article because the key ratios used in the extraction were explicitly reported by the authors.

### Schema gaps / representation limits
- `QuantitativeResult` has no dedicated standard-deviation field. SD values are preserved in each atom's `canonical_statement` and `original_result_text`.
- The current schema has no explicit censored/BLQ quantitative-result representation. All-sample BLQ findings are represented as `qualitative_result` atoms, while the applicable LLOQ thresholds are preserved in a separate method atom.

## SEA source coverage manifest
- Sections/headings: Abstract; Introduction; Methods and experiments — Ethics, Data and subjects, Measurements, Pharmacokinetic analysis; Results — serum profiles and salivary comparison; Discussion; Conclusions; Funding; Transparency declarations; Author contributions; Data availability; References.
- Main-text figures: 1 (`Figure 1`, page 3).
- Main-text tables: 1 (`Table 1`, page 4).
- Calculation workflows/equations: AUC0–∞ extrapolation formula; protein-binding calculation.
- Appendices/supplements: none specified/provided.
- Figure strategy: Figure 1 embedded as a crop in the HTML because individual trajectories and the BLQ saliva panels are visually load-bearing.
- Table strategy: Table 1 reconstructed as structured HTML with all reported PK rows.
- Workflow strategy: PK equations represented as structured text.
- Omitted from narrative condensation: bibliography/reference list as evidence; author-contribution role details beyond source identification.

## SEA QA
- Raw primary PDF availability immediately before SEA: **CONFIRMED** (`497663` bytes; SHA-256 unchanged).
- Exact source title/source ID: **PASS**.
- Coverage manifest created before HTML generation: **PASS**.
- Main-text figure/table reconciliation: **PASS** (1/1 figure, 1/1 table).
- Claims separated from appraisal: **PASS**.
- Final ratings assigned after section/visual extraction: **PASS**.
- Self-contained HTML: **PASS** (embedded CSS + embedded Figure 1 crop; no external fonts/scripts/images).
- Internal chat/file citation syntax absent from HTML: **PASS**.
- Placeholder/TODO/planning-language scan: **PASS**.

## Extraction / appraisal limitations
- No correction or supplementary material was specified for this task.
- The article reuses stored samples from a previous study; this workflow treats `dkag280.pdf` as the primary publication as instructed.
- Reference-derived background claims were not reclassified as primary-study results in the atom set.
- Appraisal is constrained by the source itself: n=6, all male, healthy volunteers, single dose, 0–10 h sampling, metabolite saliva BLQ, and imprecise metabolite protein-binding estimates.

## Generated outputs
- `dkag280-atoms.json`
- `dkag280-atom-validation.json`
- `dkag280-sea.html`
- `dkag280-processing-notes.md`
