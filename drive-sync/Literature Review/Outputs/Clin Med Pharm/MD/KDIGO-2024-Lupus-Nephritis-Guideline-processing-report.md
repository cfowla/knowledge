# KDIGO 2024 lupus nephritis guideline processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source identity

- Title: KDIGO 2024 Clinical Practice Guideline for the Management of Lupus Nephritis
- Organization: KDIGO Lupus Nephritis Work Group
- Citation: Kidney Int. 2024;105(1S):S1-S69
- Main guideline: 70 PDF pages; SHA-256 `b65b0c624ed315f45189edac2496cb6d5ffe9fb8f64e0b9670ce42ff0d8bab46`
- Data supplement: 101 PDF pages; SHA-256 `525d0ea8fdcf824082ff20acc59ea82cac147dcca7fc7f4255d3b89b96fea96c`
- Shared publication_id: `937fc35f-52dd-5682-b450-7021fb6241fe`

## ATOM

- 34 LiteratureAtoms
- Kinds: `study_objective` 1; `method` 4; `other` 29
- Formal guidance represented: 29/29
- Graded recommendations: 3
- Practice Points: 26
- Local stable-shape validation: PASS
- Local sufficiency check for extracted kinds: PASS
- Duplicate atoms found: 0

The current LiteratureAtom model has no dedicated `guideline_recommendation` atom kind. Formal guidance is represented as `other` with recommendation or Practice Point tags. Trial results summarized by the guideline were not represented as if the guideline generated those results.

## Governing-source execution boundary

The supplied `large-source-ATOM-SEA.md` workflow and `unslop.skill.md` were applied. The named governing ATOM files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom.json` were searched in connected project sources but were not directly retrievable. The named `summary-evaluation-appraisal-protocol-v4-compact.md` file was also searched but was not directly retrievable.

The validation artifact therefore reports local checks against the stable LiteratureAtom shape used by recent project artifacts. It marks authoritative Pydantic validation and authoritative JSON Schema validation as not executed. The SEA artifact follows the available large-source workflow but does not assign a protocol-specific numeric score because the v4 scoring rubric was unavailable.

## SEA coverage and QA

- 29/29 formal guidance statements represented
- 14/14 main figures mapped and reconciled
- 6/6 main methods tables mapped
- Supplement Tables S1-S49 inventoried without missing table numbers
- Key evidence profiles reconciled for hydroxychloroquine, cyclophosphamide dosing, mycophenolate, tacrolimus multitarget therapy, voclosporin, CNI triple therapy, belimumab, reduced-dose glucocorticoids, maintenance therapy, and selected newer biologics
- Self-contained HTML: PASS
- Internal chat or file citation syntax in HTML: absent
- Placeholder and TODO scan: PASS
- External verification: not performed

## Source-integrity findings

- Recommendation 10.2.3.1.1 says a CNI can be used when kidney function is "not severely impaired" but prints eGFR `<=45 mL/min/1.73 m2`. Figure 5 instead specifies voclosporin in patients with eGFR `>45 mL/min/1.73 m2` and warns about CNI nephrotoxicity in impaired kidney function. The conflict was preserved rather than repaired.
- The main methods section says the search was updated April 25, 2023. Supplement Table S1 says April 23, 2023.
- Several supplement plain-text summary cells contain apparent copied outcome labels, including Table S10's infection row and Table S11's infection and malignancy rows. Numerical results and certainty ratings were preserved.

## References

- Main guideline bibliography: 370 entries
- Data supplement Appendix B: 2 methodology references
- Data supplement table-local reference entries: 106, with repeated citations preserved
- Bibliographic entries were extracted to Markdown and were not atomized

## Output files

- `KDIGO-2024-Lupus-Nephritis-Guideline-atoms.json`
- `KDIGO-2024-Lupus-Nephritis-Guideline-validation.json`
- `KDIGO-2024-Lupus-Nephritis-Guideline-coverage.json`
- `KDIGO-2024-Lupus-Nephritis-Guideline-sea.html`
- `KDIGO-2024-Lupus-Nephritis-Guideline-references.md`
- `KDIGO-2024-Lupus-Nephritis-Guideline-processing-report.md`
