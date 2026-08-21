# KDIGO 2025 IgAN and IgAV guideline processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Title: KDIGO 2025 Clinical Practice Guideline for the Management of Immunoglobulin A Nephropathy (IgAN) and Immunoglobulin A Vasculitis (IgAV)
- Citation: Kidney Int. 2025;108(4S):S1-S71
- DOI: 10.1016/j.kint.2025.04.004
- Main PDF: `KDIGO-2025-IgAN-IgAV-Guideline.pdf`, 71 pages, SHA-256 `4fe42962842b3f7330ca7bec7551fdb98ae90e56f6a12978c16c5d3a6a1eeb44`
- Data supplement: `KDIGO-2025-IgAN-IgAV-Guideline_Data-Supplement.pdf`, 151 pages, SHA-256 `5437519f76f86056b54d5780be7a28d55a37d2d3cc04d72a6f4f9b378001e6a5`
- LiteratureAtom publication ID: `48da6a08-5140-555e-9ea2-1de3219b079b`

## ATOM status

- Atoms: 51
- By kind: {"author_conclusion": 10, "limitation": 1, "method": 6, "other": 33, "study_objective": 1}
- Formal recommendations: 6
- Practice Points: 27
- Research recommendations: 10
- Local Pydantic validation: passed
- Local generated JSON Schema validation: passed
- Sufficiency validation for extracted kinds: passed
- Structural errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0

The recovered project pattern has no dedicated guideline recommendation or Practice Point atom kind. Formal guidance is represented as `atom_kind="other"` with recommendation or Practice Point tags. Recommendation strength and GRADE certainty are preserved in tags.

## SEA status

All 71 main-guideline pages and all 151 supplement pages were rendered and visually reviewed. All 5 main figures, 9 main tables, and Supplement Tables S1-S65 were inventoried. Key evidence profiles for Nefecon, oral systemic glucocorticoids, RAS inhibition, SGLT2 inhibition, and sparsentan were reconciled with the data supplement before appraisal.

The SEA keeps source guidance separate from appraisal and treats trial results summarized by KDIGO as secondary evidence.

## References

- Main guideline bibliography: 133 entries, including the source's `100a` reference.
- Data supplement: 164 table-local citation occurrences captured, with 111 unique citation strings in the Markdown index.
- Bibliographic entries were not atomized.

## Source-integrity finding

Main guideline reference 86 prints the DAPA-CKD IgAN analysis by Wheeler et al. as `Kidney Int. 2021;388:117-127`. The data supplement prints the same publication as `Kidney International 2021;100:215-224`. The conflict is preserved and flagged rather than silently corrected.

## Governing-source execution boundary

The authoritative project files literature.py, literature_atoms.py, literature_atom.schema.json, README(2).md, example_atom.json, and summary-evaluation-appraisal-protocol-v4-compact.md were searched in connected project sources but were not directly retrievable in this session. Validation therefore used a strict local Pydantic contract and its generated JSON Schema reconstructed from current validated project guideline artifacts plus the retrieved large-source guideline guardrail. This report does not claim execution of unavailable authoritative project code.

## Output files

- `KDIGO-2025-IgAN-IgAV-Guideline-atoms.json`
- `KDIGO-2025-IgAN-IgAV-Guideline-validation.json`
- `KDIGO-2025-IgAN-IgAV-Guideline-coverage.json`
- `KDIGO-2025-IgAN-IgAV-Guideline-sea.html`
- `KDIGO-2025-IgAN-IgAV-Guideline-references.md`
- `KDIGO-2025-IgAN-IgAV-Guideline-processing-report.md`
