# Dhana Aqel 2025 processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source

- Title: Comparative Cardiovascular Outcomes of Dapagliflozin Versus Empagliflozin in Patients With Type 2 Diabetes: A Meta-Analysis
- Authors: Rhuna Dhana, Yousef Aqel, Anurag Rawat, Aakash Mahato, Abdelaziz Maali Abusal, Nazish Munawar, Calvin R. Wei, Adil Amin
- Journal: Cureus. 2025;17(5):e83449.
- DOI: 10.7759/cureus.83449
- PMID: 40322609 (from the active TBR queue metadata)
- Source file: `cureus-0017-00000083449.pdf`, 8 PDF pages, SHA-256 `9eca67196f4fce67e7776fa6cd54f60b7b1a104324c8b5f2b3cde9c019b2aa18`
- Shared publication ID: `994a6328-a3ac-5043-a398-6d1c7344cade`
- Source type: systematic review and random-effects meta-analysis of retrospective comparative studies

## ATOM result

- Total LiteratureAtoms: 47
- Counts by kind: `{"author_conclusion": 3, "comparator_description": 1, "conflict_of_interest": 1, "eligibility_criterion": 2, "funding_disclosure": 1, "intervention_description": 1, "limitation": 7, "method": 7, "other": 3, "outcome_definition": 4, "population_description": 1, "qualitative_result": 2, "quantitative_result": 5, "study_objective": 1, "subgroup_result": 8}`
- Assertion origins: `{"calculated_from_reported_data": 1, "directly_reported": 16, "extractor_inference": 2, "normalized_from_source": 28}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0

All atoms use `needs_review` because extraction was model-assisted and has not received independent human verification.

## SEA result

Coverage reconciled all **5 main-text figures** and **3 main-text tables**. No supplement was present in the source packet. The source was appraised as a systematic review/meta-analysis based entirely on retrospective direct-comparison cohorts.

Key pooled results: MACE RR 1.04 (95% CI 0.96-1.13; I² 64%); all-cause mortality RR 1.05 (0.96-1.15; I² 0%); myocardial infarction RR 1.04 (0.94-1.16; I² 0%); stroke RR 1.00 (0.91-1.09; I² 0%). The heart-failure subgroup was RR 0.90 (0.82-1.00) with interaction p=0.04, but subgroup evidence was limited.

Verdict: **Skim deeply**. The review is directly relevant to dapagliflozin-versus-empagliflozin formulary questions but should not be treated as proof of equivalence or noninferiority.

## References

The article contains **27** bibliography entries. They were exported to `dhana-aqel-2025-references.md`. Bibliography entries were not converted into LiteratureAtoms solely because they were cited.

## Source and validation limitations

- `literature.py`, `literature_atoms.py`, and `literature_atom.schema.json` were available and executed as the governing ATOM model, sufficiency validator, and serialization contract.
- `summary-evaluation-appraisal-protocol-v4-compact.md` was available and used as the governing SEA protocol; the v3 HTML was treated as historical reference only.
- `README(2).md` and `example_atom.json` were not present in the supplied project files and were not found by exact Drive search; their supporting workflow/example guidance could not be inspected.
- Reported overall N is 280,617 (158,352 empagliflozin + 122,265 dapagliflozin), but Table 1 sums to 290,600 (163,654 + 126,946). The 9,983-person difference exactly equals the Suzuki et al. row, indicating the narrative totals omit one of the eight listed study rows.
- Results prose states mean age ranged 52-62.4 years, while Table 1 includes 62.6 years for Alhakak et al.
- NOS domain maxima are internally inconsistent: Methodology specifies selection/comparability/outcome = 4/2/3, whereas Table 2 note states 4/3/2.
- The review does not report a prospective protocol/registration, GRADE certainty assessment, sensitivity analysis, or publication-bias assessment.
- Eligibility allows extractable RR or HR, while the pooling method only states that RRs were calculated; effect-measure harmonization is not explained.
- Several studies come from the same countries/time periods, but the article does not report assessment of overlapping source populations. This remains a model-identified risk, not a confirmed duplication.

## Output files

Stored under `GitHub Sync / Literature Review / Outputs / Clin Med Pharm`.

### JSON

- `dhana-aqel-2025-atoms.json`
- `dhana-aqel-2025-validation.json`
- `dhana-aqel-2025-coverage.json`
- `dhana-aqel-2025-sea-qa.json`

### HTML

- `dhana-aqel-2025-sea.html`

### Markdown

- `dhana-aqel-2025-references.md`
- `dhana-aqel-2025-processing-report.md`
