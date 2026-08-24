# Processing report — Lim Choi 2023

## Source
- **Title:** Comparative cardiovascular outcomes in type 2 diabetes patients taking dapagliflozin versus empagliflozin: a nationwide population-based cohort study
- **PMID:** 37496050
- **DOI:** 10.1186/s12933-023-01911-7
- **Primary file:** `document.pdf`
- **Supplement:** `12933_2023_1911_MOESM1_ESM.docx`

## ATOM
- Publication ID: `3f711927-3a8a-5915-bcc5-a1c9de11e2b5`
- Extracted atoms: **60**
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Sufficiency warnings: **0**
- Exact duplicate pairs: **0**

### Atom counts by kind
- `adverse_event`: 4
- `author_conclusion`: 2
- `comparator_description`: 1
- `conflict_of_interest`: 1
- `data_availability`: 1
- `eligibility_criterion`: 6
- `exposure_description`: 1
- `funding_disclosure`: 1
- `limitation`: 4
- `method`: 10
- `other`: 1
- `outcome_definition`: 9
- `population_description`: 6
- `quantitative_result`: 9
- `study_objective`: 1
- `subgroup_result`: 3

## SEA
- Main figures reconciled: **3/3**
- Main tables reconciled: **1/1**
- Supplied supplementary tables reconciled: **5/5**
- SEA QA: **PASS**
- Verdict: **Read first** for direct comparative-effectiveness context; do not use alone to claim causal superiority.

## References
- Extracted bibliography entries: **45**
- Bibliography entries were preserved as references and not converted into LiteratureAtoms.
- Checkbox reference task queue: **45 items**; **6 confirmed complete / 39 pending** under conservative current-state reconciliation.

## Source consistency / limitations
- Primary-outcome 95% CI lower bound differs by source location: prose/abstract **0.855** vs Figure 2 **0.858**; upper bound **1.006** is unchanged.
- The study is observational; residual confounding, absent dose information, uncertain adherence, and predominantly Korean population limit causal and cross-population interpretation.

## Files
### JSON
- `lim-choi-2023-s12933-023-01911-7-atoms.json`
- `lim-choi-2023-s12933-023-01911-7-validation.json`
- `lim-choi-2023-s12933-023-01911-7-coverage.json`
- `lim-choi-2023-s12933-023-01911-7-crosswalk.json`
- `lim-choi-2023-s12933-023-01911-7-sea-qa.json`

### HTML
- `lim-choi-2023-s12933-023-01911-7-sea.html`

### Markdown
- `lim-choi-2023-s12933-023-01911-7-references.md`
- `lim-choi-2023-s12933-023-01911-7-reference-task-queue.md`
- `lim-choi-2023-s12933-023-01911-7-processing-report.md`

## Active-queue duplicate reconciliation
- The stale active packet formerly at `3/2/1/24` was reconciled to the canonical `17 - Lim Choi 2023` processed publication.
- Its PMID payload PDF and canonical `document.pdf` have identical SHA-256: `21ea14b0fc0c1d95007312c4491a8f79e3a3acea8bae3fa255affed16f589910`.
- The acquisition log and duplicate PDF are preserved beneath the canonical publication as `Reconciled active intake - 2026-08-23`.
- The existing 60-atom set was revalidated against the current Pydantic model, JSON Schema, and sufficiency rules: **0 structural errors, 0 schema errors, 0 sufficiency errors, 0 warnings, 0 duplicate statement-anchor pairs**.
- No second publication identity or duplicate SEA artifact was created.
