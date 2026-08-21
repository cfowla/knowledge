# Comparative Outcomes of Empagliflozin to Dapagliflozin in Patients With Heart Failure: ATOM + SEA Processing Report

## Source metadata

- **Authors:** Katherine L. Modzelewski; Alexandra Pipilas; Nicholas A. Bosch
- **Journal:** JAMA Network Open
- **Citation:** JAMA Network Open. 2024;7(5):e249305.
- **DOI:** 10.1001/jamanetworkopen.2024.9305
- **Published:** May 2, 2024
- **Correction:** July 24, 2024, numerical error in Results
- **Main PDF:** `modzelewski_2024_oi_240344_1721226492.47545.pdf`
- **Supplement:** `zoi240344supp1_prod_1721226492.49545.pdf`
- **Main SHA-256:** `db7a6c8a21741c66334a26bbf06d741efb8202230cca5fd75bd67a6bb679ab04`
- **Supplement SHA-256:** `36decfa76909850c1bffe8a9ea05ee90796215678f8def6d54031e332ee89f4a`
- **Packet SHA-256:** `c13d32aa3e33af049ea75266a81c570c879f41737c7ed5e62d5767bd300a02c1`

## Activated macros

- `@ATOM`
- `@SEA`

## Source processing

The main article and Supplement 1 were inspected as one publication packet. Extraction used four semantic batches: methods, overall results, subgroup results, and discussion/limitations. The bibliography was treated as provenance infrastructure and exported separately to Markdown.

## ATOM extraction

- **Publication ID:** `824965d6-7278-5958-8e82-929ce38325e0`
- **Total atoms:** 44
- **Local reconstructed Pydantic structural validation:** PASS
- **Local project-guidance sufficiency validation:** PASS
- **Structural errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0
- **Exact JSON Schema validation:** NOT RUN because `literature_atom.schema.json` was not retrievable

### Counts by atom kind

| Atom kind | Count |
|---|---:|
| `adverse_event` | 3 |
| `author_conclusion` | 2 |
| `comparator_description` | 1 |
| `conflict_of_interest` | 1 |
| `eligibility_criterion` | 3 |
| `funding_disclosure` | 1 |
| `intervention_description` | 1 |
| `limitation` | 6 |
| `method` | 10 |
| `outcome_definition` | 3 |
| `population_description` | 3 |
| `qualitative_result` | 3 |
| `quantitative_result` | 4 |
| `study_objective` | 1 |
| `subgroup_result` | 2 |


## SEA coverage

- Main text: Abstract, Introduction, Methods, Results, Discussion, Limitations, Conclusions, Article Information, References.
- Main figures: 2/2 reconciled.
- Main tables: baseline-characteristics table reconciled across pages 5-6.
- Supplement: eTable 1, eFigures 1-5, eTables 2-3 reconciled.
- Supplement 2 was referenced but not supplied and was not analyzed.
- References: 20 entries exported in source order.

## Source integrity findings

1. **Matched denominator conflict:** the abstract and Figure 1 report 11,077 patients per group. The Results text, baseline table, Supplement analyses, and reported primary event percentages are consistent with 11,007 per group. Quantitative atoms use 11,007 only where the Results/Table/Supplement support it, and the conflict remains explicit.
2. **Reference-number mismatch:** the Limitations paragraph cites reference 20 for immortal-time bias, but reference 19 is the Yadav and Lewis immortal-time-bias article. Reference 20 is the Juurlink et al. hyperkalemia article. The reference export preserves source numbering.

## SEA appraisal summary

- **Fallback project-pattern verdict:** Read soon
- **Relevance:** 9/10
- **Novelty:** 8/10
- **Method strength:** 6/10
- **Evidence strength:** 5/10
- **External validity:** 7/10
- **Implementation value:** 5/10
- **Core interpretation:** empagliflozin initiation was associated with a modestly lower 1-year composite of all-cause mortality or hospitalization than dapagliflozin in this matched TriNetX cohort. The signal was driven by hospitalization, not a demonstrated mortality difference. Residual confounding, broad all-cause hospitalization, limited safety ascertainment, clustering limitations, adherence uncertainty, and source-reporting inconsistencies prevent using this study alone to prefer one drug.

## Governing-source limitation

The project macro specifies `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, and `summary-evaluation-appraisal-protocol-v4-compact.md` as authoritative. Those exact files were not retrievable in this run despite project-source searches. The generated validation therefore uses a strict local Pydantic contract reconstructed from retrievable project outputs previously labeled valid and applies sufficiency rules from the retrievable large-source ATOM+SEA guidance. The SEA scorecard uses dimensions found in retrievable project SEA outputs. Neither exact authoritative ATOM validation nor exact SEA v4 scoring is claimed.

## Mechanical QA

- Atom JSON parse: PASS
- Local Pydantic parse: PASS
- Local sufficiency checks: PASS
- Duplicate atom IDs: PASS
- Exact statement+anchor duplicates: 0
- SEA HTML parse: PASS
- Reference count: 20
- Internal citation syntax in HTML: PASS
- Placeholder scan: PASS

## Output files

- `modzelewski-2024-empagliflozin-dapagliflozin-atoms.json`
- `modzelewski-2024-empagliflozin-dapagliflozin-validation.json`
- `modzelewski-2024-empagliflozin-dapagliflozin-coverage.json`
- `modzelewski-2024-empagliflozin-dapagliflozin-sea.html`
- `modzelewski-2024-empagliflozin-dapagliflozin-references.md`
- `modzelewski-2024-empagliflozin-dapagliflozin-processing-report.md`

## External-source use

No external web evidence was used. Scientific findings and appraisal were grounded in the supplied main article and Supplement 1, with retrievable project outputs used only to reconstruct output shape and fallback validation/scoring conventions where exact governing project files were unavailable.
