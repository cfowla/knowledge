# KDIGO 2024 ANCA-associated vasculitis - ATOM + SEA processing report

## Activated macros
- `@ATOM`
- `@SEA`

## Source identity
- Title: KDIGO 2024 Clinical Practice Guideline for the Management of Antineutrophil Cytoplasmic Antibody (ANCA)-Associated Vasculitis
- Organization: KDIGO ANCA Vasculitis Work Group
- Citation: Kidney International. 2024;105(3S):S71-S116
- DOI: `10.1016/j.kint.2023.10.008`
- Main guideline: 47 PDF pages; SHA-256 `f1b71336d847a2aab8e44129c099a09d1c383580ea38f31187c45be8f9bfdec8`
- Data supplement: 64 PDF pages; SHA-256 `55f5c766071ea66662212f789188e04beef60b22fc5a81be2fc5c9377bc862e3`
- Shared publication_id: `c6885399-fdd5-59b5-a3db-99e30a70cb92`

## ATOM
- 30 LiteratureAtoms
- Kinds: study_objective 1; method 4; other 25
- Formal guidance represented: 25/25
- 2 graded recommendations: 1B and 1C
- 23 ungraded Practice Points
- Local structural and serialization-shape validation: PASS
- Sufficiency check for extracted kinds: PASS
- Structural errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0

## Governing-source execution boundary
The uploaded `large-source-ATOM-SEA.md` skill and `unslop.skill.md` were retrieved and applied. The named governing ATOM code/schema files (`literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, `example_atom.json`) and the SEA v4 protocol file were searched in connected project sources but were not directly retrievable in this session. Validation therefore uses the stable LiteratureAtom object shape and guideline extraction pattern from recent project artifacts plus the large-source guideline guardrail. This report does not claim execution of unavailable authoritative project code.

## SEA coverage and QA
- 25/25 formal guidance statements represented
- 15/15 main figures mapped
- 6/6 main tables mapped
- Supplement Tables S1-S32 inventoried without missing table numbers
- Key evidence profiles reconciled for rituximab vs cyclophosphamide, reduced-dose glucocorticoids, avacopan, plasma exchange, and maintenance therapy
- Self-contained HTML: PASS
- Internal chat/file citation syntax: absent
- Placeholder/TODO scan: PASS
- External verification: not performed because `@VERIFY` was not activated

## Source-integrity findings
- Appendix B Tables S2-S3 contain apparent template residue naming other KDIGO guidelines.
- Supplement page 21 retains an editorial note that references need updating.
- Table S31's reference block contains citations not used by its table footnotes, including a lupus nephritis laquinimod abstract. The source content was preserved and flagged rather than silently corrected.

## References
- Main guideline bibliography: 86 entries
- Data supplement: 79 table-local reference entries, with repetitions preserved
- Bibliographic entries were extracted to Markdown and were not atomized.

## Output files
- `KDIGO-2024-ANCA-Vasculitis-Guideline-atoms.json`
- `KDIGO-2024-ANCA-Vasculitis-Guideline-validation.json`
- `KDIGO-2024-ANCA-Vasculitis-Guideline-coverage.json`
- `KDIGO-2024-ANCA-Vasculitis-Guideline-sea.html`
- `KDIGO-2024-ANCA-Vasculitis-Guideline-references.md`
- `KDIGO-2024-ANCA-Vasculitis-Guideline-processing-report.md`
