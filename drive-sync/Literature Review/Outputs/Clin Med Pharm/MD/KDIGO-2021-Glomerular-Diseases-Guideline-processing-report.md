# KDIGO 2021 Glomerular Diseases — ATOM + SEA Processing Report

## Activated macros
- `@ATOM`
- `@SEA`

## Source identity
- **Title:** *KDIGO 2021 Clinical Practice Guideline for the Management of Glomerular Diseases*
- **Organization:** Kidney Disease: Improving Global Outcomes (KDIGO) Glomerular Diseases Work Group
- **Citation:** *Kidney Int. 2021;100(4S):S1–S276*
- **DOI:** `10.1016/j.kint.2021.05.021`
- **Main guideline:** 281 PDF pages; SHA-256 `8ed871ec098c7eba1cfb0ff6bf2355a6c422166b2691aac138f0273307b2acff`
- **Data supplement:** 478 PDF pages; SHA-256 `2c694e198964bc790f07489ec2f6bc3cbb0c4968f71902c4e4e06953a8931d76`
- **Version boundary:** the supplied main PDF is the 2021 guideline with May-2024 warning stamps. It explicitly marks Chapter 9 (AAV) and Chapter 10 (lupus nephritis) as outdated and directs readers to external 2024 updates. Those replacement chapters are **not present** in the supplied files.

## Large-source execution
Semantic batches:
- Global scope/methods/version control: **7 atoms**
- Chapter 1 — General principles: **24**
- Chapter 2 — IgAN/IgAV: **25**
- Chapter 3 — Membranous nephropathy: **13**
- Chapter 4 — Nephrotic syndrome in children: **14**
- Chapter 5 — Adult MCD: **11**
- Chapter 6 — Adult FSGS: **13**
- Chapter 7 — Infection-related GN: **21**
- Chapter 8 — Immunoglobulin/complement-mediated MPGN-pattern disease: **15**
- Chapter 11 — Anti-GBM GN: **9**
- Chapters 9–10: coverage/version-control only; legacy formal statements intentionally not atomized as active guidance.

Total LiteratureAtoms: **152**
- `study_objective`: 1
- `method`: 4
- `other`: 147
- Active formal recommendations: **16**
- Active Practice Points: **129**
- Global/method/version atoms: **7**

Recommendation grades among active chapters:
- Level 1: 15
- Level 2: 1
- Evidence certainty B: 7
- Evidence certainty C: 8
- Evidence certainty D: 1

Deprecated source content not emitted as active formal-guidance atoms:
- Chapter 9: 26 labeled statements
- Chapter 10: 28 labeled statements

## Validation
- Strict local Pydantic contract validation: **PASS**
- Generated JSON-Schema validation: **PASS**
- Sufficiency validation for extracted atom kinds: **PASS**
- Structural errors: 0
- JSON-Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Review status: `needs_review`

### Governing-source execution boundary
The uploaded `large-source-ATOM-SEA.md` source was retrieved and applied. The named governing ATOM code/schema files (`literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, `example_atom.json`) and the exact SEA v4 protocol file were searched for in connected project sources but were not directly retrievable in this session. Validation therefore used a strict local contract reconstructed from recent validated project LiteratureAtom artifacts and the large-source guideline guardrail. This report does **not** claim execution of unavailable authoritative project code.

## SEA coverage and QA
- 145/145 active formal guidance statements represented
- Source-deprecated Chapters 9/10 explicitly segregated
- 100/100 main figures inventoried
- 6/6 main tables inventoried
- Supplement Tables S1–S218 inventoried with no missing numbers
- 153 active-chapter evidence tables + 3 methods tables represented; 62 deprecated-chapter tables tagged as legacy
- Selected load-bearing quantitative evidence profiles preserved in the HTML
- HTML self-contained; no external scripts/fonts/images
- Internal chat/file citation syntax: absent
- TODO/placeholder scan: PASS
- External verification: not performed (`@VERIFY` was not activated)

## References
- Main guideline bibliography: **976** entries
- Data supplement: **648** reference entries (2 IOM standards references + 646 table-local bracket citations; repetitions preserved)
- Bibliographic entries were extracted to Markdown and were not atomized.

## Schema gaps
1. No dedicated `guideline_recommendation` or `practice_point` atom kind in the project serialization pattern used for recent guideline outputs; formal guidance is serialized as `atom_kind="other"` with descriptive tags.
2. No native external-supersession field for outdated guideline chapters; the AAV/LN deprecation boundary is preserved with source-level atoms, tags, coverage status, and omission of legacy formal statements from active atomization.

## Output files
- `KDIGO-2021-Glomerular-Diseases-Guideline-atoms.json`
- `KDIGO-2021-Glomerular-Diseases-Guideline-validation.json`
- `KDIGO-2021-Glomerular-Diseases-Guideline-coverage.json`
- `KDIGO-2021-Glomerular-Diseases-Guideline-sea.html`
- `KDIGO-2021-Glomerular-Diseases-Guideline-references.md`
- `KDIGO-2021-Glomerular-Diseases-Guideline-processing-report.md`
