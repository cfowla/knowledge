# cureus-8339 — ATOM validation and SEA QA

## Source metadata

- File: `cureus-0012-00000008339.pdf`
- Title: *Bleeding and Thrombotic Risk in Low Dose Heparin Infusion as Compared to Standard Dose Heparin Infusion*
- Authors: Forat Lutfi, Rohit Bishnoi, Vikas Patel, Aisha Elfasi, Michael Setteducato, Shuyao Zhang, Chintan P. Shah, Saji Kurian, Chethana Kamath, Dae Jun Kim, Marc S. Zumberg, Martina Murphy
- Journal: Cureus 12(5): e8339
- Published: 2020-05-28
- DOI: `10.7759/cureus.8339`
- Design: single-center retrospective comparative cohort
- Sample: 377 adults (LI 158; SI 219)
- PDF SHA-256: `1ec8556ee7c1e6babd33cb5a46c803ba63b70a18c0043c123819657d51c17e89`
- Shared publication_id: `08e567d2-c050-5783-9164-6f0b3867faa7`

## ATOM extraction

Total atoms: **47**

| Atom kind | Count |
|---|---:|
| adverse_event | 7 |
| author_conclusion | 4 |
| comparator_description | 3 |
| conflict_of_interest | 1 |
| eligibility_criterion | 1 |
| funding_disclosure | 1 |
| intervention_description | 3 |
| limitation | 2 |
| method | 6 |
| outcome_definition | 3 |
| population_description | 1 |
| qualitative_result | 1 |
| quantitative_result | 13 |
| study_objective | 1 |

### Validation

- Pydantic structural errors: **0**
- JSON Schema serialization errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Atom IDs: deterministic and unique
- Publication identity: one shared `publication_id` across all atoms
- Provenance: every atom includes PDF hash and extraction run ID `cureus-8339-20260811-v1`
- Review status: `extracted` (machine-extracted; not represented as human-verified)

### Assertion origin handling

- Study statements were encoded primarily as `normalized_from_source` because the canonical statements are normalized/paraphrased from the PDF.
- No calculated-from-reported-data atoms were added.
- No extractor-inference atoms were converted into reported study findings.

### Extraction limitations / source anomalies

1. Protocol assignment was based on clinician judgment, so the LI and SI groups are not exchangeable and comparative effects are heavily vulnerable to confounding by indication.
2. Table 1 visibly duplicates the LI anti-Xa `0.11-0.24` titration row. No missing interval was inferred or invented.
3. Page 7 prose reports the 3-month mortality OR confidence interval as `9.50-1.80`, while Table 5 reports `0.50-1.80`. The atom uses the Table 5 value and is tagged `table-preferred-over-prose-typo`.
4. Table 2 reports platelet count with the unit `g/cm3`, which appears internally implausible; the extraction preserves this as a source-reported unit in the SEA table rather than silently correcting it.
5. The main-text multivariable table does not enumerate the final adjustment covariates selected by the stepwise model; atoms mark the ORs as adjusted but do not invent adjustment variables.
6. No supplement/appendix or data-availability statement was identified in the retrieved PDF.

## SEA coverage manifest

- Pages inspected: **11/11**
- Main-text figures: **0**
- Main-text tables: **5/5 reconciled**
- Workflow/algorithm: Table 1 dose/titration/monitoring nomogram
- Appendices/supplements: none identified
- Visual strategy: all five tables reconstructed as structured HTML blocks; page renders were visually checked; screenshots were not embedded because the table content was recoverable without losing load-bearing information.
- References: not condensed; treated as provenance infrastructure.

## SEA appraisal status

- Source classified before appraisal: **retrospective comparative clinical pharmacotherapy study**
- Appraisal completed after section and table extraction: **yes**
- Claim vs appraisal separation: **yes**
- Clinical module / PICO included: **yes**
- Final verdict: **Read first** for a therapeutic-UFH/heparin-protocol deep dive; **do not use alone for practice change**.

## Mechanical HTML QA

- Single self-contained HTML file: **PASS**
- External fonts/scripts/images: **PASS — none present**
- Required anchors: `metadata`, `synthesis`, `sections`, `tables`, `appraisal`, `takeaways`, `provenance`
- Internal chat/file citation syntax: **PASS — none present**
- Placeholders/TODOs/planning language: **PASS — none present**


- Required anchor resolution: **PASS**
- HTML table count: **5** structured source tables (plus no unrelated data tables)
- HTML parse/title check: **PASS**
- Raw PDF retained locally at completion of ATOM and before/after SEA: **PASS (132,112 bytes)**
