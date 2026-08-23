# Herrington & Staplin 2023 — Processing Report

## Source package

- Primary publication: **Empagliflozin in Patients with Chronic Kidney Disease** (EMPA-KIDNEY Collaborative Group), *N Engl J Med* 2023;388:117–127; DOI `10.1056/NEJMoa2204233`.
- Supporting source: `nejmoa2204233_protocol.pdf`, a 122-page package containing superseded and final protocol/DAP versions.
- Operative methods source used for extraction: **Final Trial Protocol v2.0 (2020-01-13)** and **Final Data Analysis Plan v1.2**.
- The separate Supplementary Appendix cited by the article was not present in the target folder. Its result tables/figures were not reconstructed.

## ATOM status

- Publication identity: `0782000a-f2dc-5926-b70b-36458b61327e` shared across article and protocol-derived atoms.
- LiteratureAtoms: **97**.
- Semantic batches: **5** (`general`, `methods-protocol`, `results`, `subgroups-safety`, `conclusions-protocol`).
- Pydantic structural errors: **0**.
- JSON Schema errors: **0**.
- Sufficiency errors: **0**.
- Sufficiency warnings: **0**.
- Duplicate statement-anchor pairs: **0**.
- Review status: `needs_review` for language-model extracted atoms; validation does not imply human verification.

## SEA status

- Verdict: **Read first**.
- Main visual reconciliation: **3/3 figures and 2/2 tables** represented as structured blocks.
- Protocol workflows: randomization/follow-up and DAP local-creatinine substitution algorithm represented.
- SEA QA: **PASS**.
- Important interpretive boundary: low-albuminuria event-based subgroup estimates are less precise; favorable eGFR-slope evidence is not converted into a claim of statistically significant event reduction for every low-UACR stratum.

## Governing-protocol version note

The governing SEA project file is named `summary-evaluation-appraisal-protocol-v4-compact.md`, although its internal heading still identifies the integrated compact protocol as v3. Per project macro precedence, the v4-named file governs and the internal heading mismatch is retained as a version-label discrepancy rather than silently corrected.

## Reference queue

- **24** references from the main article were transcribed into a Markdown task queue.
- DAPA-CKD (Heerspink et al. 2020) is marked already processed because a verified TBR source packet/output set exists.
- Protocol bibliography entries were not automatically promoted to separate primary-study tasks.

## Output files

- `herrington-staplin-2023-nejmoa2204233-atoms.json`
- `herrington-staplin-2023-nejmoa2204233-validation.json`
- `herrington-staplin-2023-nejmoa2204233-coverage.json`
- `herrington-staplin-2023-nejmoa2204233-crosswalk.json`
- `herrington-staplin-2023-nejmoa2204233-sea-qa.json`
- `herrington-staplin-2023-nejmoa2204233-sea.html`
- `herrington-staplin-2023-nejmoa2204233-reference-task-queue.md`
- `herrington-staplin-2023-nejmoa2204233-processing-report.md`

## Stateful workflow update

After output upload verification, the SGLT2 formulary-change task entry for EMPA-KIDNEY should be marked complete; the source packet should move from Active Literature to the next numbered Clinical Medicine & Pharmacy Processed folder; and `TBR - Current Task Queue` should be reconciled to the resulting active/processed and SGLT2 counts.
