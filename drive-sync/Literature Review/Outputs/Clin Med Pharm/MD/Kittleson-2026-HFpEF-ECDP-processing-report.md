# 2026 ACC HFpEF ECDP processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Title: *Management of Heart Failure With Preserved Ejection Fraction: 2026 ACC Expert Consensus Decision Pathway*
- DOI: `10.1016/j.jacc.2026.06.018`
- Source type: ACC Expert Consensus Decision Pathway, a secondary clinical policy document
- Main PDF: `kittleson-et-al-2026-management-of-heart-failure-with-preserved-ejection-fraction-2026-acc-expert-consensus-decision.pdf`, 30 pages, SHA-256 `5331dde1e41f786ad168b2a10bec65225b0687b9f7e85f161461339cba6ca68a`
- Supplemental Appendix: `mmc1(3).pdf`, 11 pages, SHA-256 `820d2fbfc152ccf38d8fa3c45ee30c0dd498b0110541855af293b5840472bcfd`
- Shared publication ID: `a93797b7-2fee-52ec-b3a6-421d0aa325cc`
- Supplied publication status: Article in Press / proof, approved July 2026

## ATOM status

- LiteratureAtoms: **92**
- Kinds: `{'study_objective': 1, 'method': 6, 'author_conclusion': 41, 'other': 32, 'limitation': 11, 'conflict_of_interest': 1}`
- Shared publication identity: **PASS**
- Unique atom IDs: **PASS**
- Local recovered-contract Pydantic validation: **PASS**
- Local generated JSON Schema validation: **PASS**
- Sufficiency validation for the generic atom kinds used: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Review status: all atoms remain `needs_review`

The source is an expert consensus pathway rather than primary empirical literature. The extraction therefore represents the committee's own guidance, definitions, methods, limitations, and selected secondary reports of trial evidence. Secondary trial effects are tagged `secondary_reported_result` and are not represented as if the ECDP enrolled the participants or generated those outcomes.

## SEA status

The full 30-page main proof and 11-page Supplemental Appendix were rendered and inspected. The SEA reconciles all **8/8 figures**, **6/6 main tables**, Supplemental **Table S1**, and the relevant/comprehensive RWI appendices. Final appraisal was performed after whole-source synthesis.

A protocol-specific numeric SEA score was not assigned. The exact governing file `summary-evaluation-appraisal-protocol-v4-compact.md` was searched in connected project sources but was not directly retrievable.

## References

- Main bibliography: **209** entries
- Supplemental Appendix bibliography: **9** entries
- All 9 supplemental references duplicate main bibliography entries and are cross-mapped rather than duplicated.
- Output: `Kittleson-2026-HFpEF-ECDP-references.md`

## Source-integrity findings

1. Supplemental Table S1 refers to a new Figure 9 for the CKM benefit matrix, while the supplied main proof contains Figures 1 through 8 and labels the CKM matrix as Figure 8.
2. The main proof still contains placeholder volume and page fields in the requested citation, so final pagination was not invented.
3. Some comorbidity passages use "GLP-1 receptor antagonists" while the treatment section describes GLP-1 receptor agonist or incretin-based therapy and Figure 7 uses GLP-1RA. The inconsistency was preserved and flagged.

## Governing-source execution boundary

The supplied `large-source-ATOM-SEA.md` workflow and retrieved `unslop.skill.md` were applied. The named authoritative ATOM files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom.json`, plus the exact SEA v4 protocol, were searched in connected project sources but were not directly retrievable. The historical v3 SEA HTML was retrieved only as supporting structure.

Validation therefore uses a strict local Pydantic contract and generated JSON Schema reconstructed from current validated project LiteratureAtom outputs plus the supplied large-source consensus/guideline guardrail. This report does not claim execution of unavailable authoritative project code or the unavailable v4 scoring rubric.

No external verification was performed because `@VERIFY` was not activated.

## Output files

- `Kittleson-2026-HFpEF-ECDP-atoms.json`
- `Kittleson-2026-HFpEF-ECDP-validation.json`
- `Kittleson-2026-HFpEF-ECDP-coverage.json`
- `Kittleson-2026-HFpEF-ECDP-sea.html`
- `Kittleson-2026-HFpEF-ECDP-references.md`
- `Kittleson-2026-HFpEF-ECDP-processing-report.md`
