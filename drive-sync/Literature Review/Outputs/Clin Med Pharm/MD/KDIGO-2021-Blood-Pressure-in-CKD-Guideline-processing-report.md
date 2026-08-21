# KDIGO 2021 Blood Pressure in CKD — ATOM + SEA Processing Report

## Activated macros
- `@ATOM`
- `@SEA`

## Source identity
- Title: *KDIGO 2021 Clinical Practice Guideline for the Management of Blood Pressure in Chronic Kidney Disease*
- Organization: Kidney Disease: Improving Global Outcomes (KDIGO) Blood Pressure Work Group
- Citation: *Kidney International*. 2021;99(3S):S1–S87
- DOI: `10.1016/j.kint.2020.11.003`
- Main guideline: 92 PDF pages; SHA-256 `3717244e8a539e710f32180720b442cf0d1dda12810cecbe61e4e8cfb54f7b23`
- Data supplement: 329 PDF pages; SHA-256 `87cd1f93e6121356fed36f6e4fe55ecd438d588a077771e51e440d6001b04d11`

## Large-source execution
Semantic batches:
- Global scope/methods: 5 atoms
- Chapter 1 — BP measurement: 5 formal guidance atoms
- Chapter 2 — lifestyle: 6
- Chapter 3 — adult BP management: 14
- Chapter 4 — transplant: 2
- Chapter 5 — children: 4

Total LiteratureAtoms: **36**
- `other`: 32
- `method`: 3
- `study_objective`: 1
- Formal recommendations: 11
- Practice Points: 20

Recommendation grades:
- Level 1: 5
- Level 2: 6
- Evidence certainty B: 6
- Evidence certainty C: 5

## Validation
- Strict local Pydantic contract validation: PASS
- Local JSON-schema validation: PASS
- Sufficiency validation for the extracted atom kinds: PASS
- Structural errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Review status: `needs_review`

### Governing-source execution boundary
The uploaded `large-source-ATOM-SEA.md` skill was retrieved and applied. The named governing ATOM code/schema files (`literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, `example_atom.json`) and the SEA v4 protocol file were searched for in the connected project sources but were not directly retrievable in this session. Validation therefore used a strict local contract reconstructed from recent validated project LiteratureAtom artifacts and the large-source guideline guardrail; this report does **not** claim execution of unavailable authoritative project code.

## SEA coverage and QA
- 31/31 formal guidance statements represented
- 8/8 main figures mapped
- 6/6 main tables mapped
- Supplement Tables S1–S107 inventoried with no missing table numbers
- Key load-bearing evidence profiles summarized, including low-salt diet (Table S5), intensive BP targets (Table S11), SPRINT CKD evidence, transplant evidence, and ESCAPE pediatric evidence
- HTML is self-contained
- Internal chat/file citation syntax: absent
- Draft/placeholder scan: PASS
- External verification: not performed (`@VERIFY` was not activated)

## References
- Main guideline bibliography: **389** entries
- Data supplement: **624** table-local citation entries, with repetitions preserved
- Bibliographic entries were extracted to Markdown and were not atomized.

## Schema gap
The current project guideline pattern has no dedicated `guideline_recommendation` or `practice_point` atom kind. Formal guideline statements are serialized as `atom_kind="other"` with tags for recommendation/practice-point identity, chapter, strength, and certainty.

## Output files
- `KDIGO-2021-Blood-Pressure-in-CKD-Guideline-atoms.json`
- `KDIGO-2021-Blood-Pressure-in-CKD-Guideline-validation.json`
- `KDIGO-2021-Blood-Pressure-in-CKD-Guideline-coverage.json`
- `KDIGO-2021-Blood-Pressure-in-CKD-Guideline-sea.html`
- `KDIGO-2021-Blood-Pressure-in-CKD-Guideline-references.md`
