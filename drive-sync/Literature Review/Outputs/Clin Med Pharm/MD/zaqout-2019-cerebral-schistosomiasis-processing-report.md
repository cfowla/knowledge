# Zaqout 2019 cerebral schistosomiasis processing report

## Activated macros

- @ATOM
- @SEA

## Source

- Title: *Cerebral schistosomiasis: Case series from Qatar*
- Citation: *International Journal of Infectious Diseases*. 2019;86:167-170.
- DOI: 10.1016/j.ijid.2019.07.002
- Source type: case report article containing a three-patient case series and narrative literature review
- Raw Drive file: `1-s2.0-S1201971219302772.pdf`
- PDF pages: 4
- SHA-256: `09fa53db5a4928b76f1d758e48667910094301a24b5a91fed670717101f872a9`
- Shared publication ID: `b0dfe983-67e9-51d0-9481-31ff63fae4bc`

## ATOM status

- Atoms: 29
- By kind: `{"author_conclusion": 4, "conflict_of_interest": 1, "funding_disclosure": 1, "intervention_description": 3, "method": 2, "population_description": 4, "qualitative_result": 13, "study_objective": 1}`
- Semantic batches: general, Case 1, Case 2, Case 3, and interpretation
- Pydantic structural validation: PASS
- JSON Schema validation: PASS
- Sufficiency validation: PASS
- Structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate atom IDs: 0
- Duplicate statement-anchor pairs: 0

Primary case-series findings were atomized at source and case level. Background claims and cited-study results in the discussion were not converted into primary-study atoms. Treatment responses remain descriptive qualitative results because the report has no comparator or causal treatment-effect design.

The current LiteratureAtom model has no dedicated case-report treatment-outcome kind. The extraction uses `qualitative_result` for descriptive clinical outcomes rather than inventing a new schema kind.

## SEA status

All 4 pages were rendered and visually inspected. The article has one main composite figure with nine panels and no tables. Figure 1 was reconstructed as a structured figure block. No supplement was present in the target Drive folder.

Verdict: **Skim deeply.** The paper is useful for recognizing cerebral schistosomiasis as a tumor mimic in patients with relevant epidemiologic exposure. It is weak evidence for treatment selection or diagnostic test performance.

SEA QA: PASS. The HTML is self-contained, all navigation anchors resolve, no external fonts or scripts are used, and no internal tool citation syntax appears in the file.

## Reference task queue

- Bibliography entries: 21
- Source order preserved
- External bibliographic correction: not performed
- Bibliography atomized: no
- Output: `zaqout-2019-cerebral-schistosomiasis-references.md`

## Governing sources applied

ATOM precedence:

1. `literature(1).py`
2. `literature_atoms(1).py`
3. `literature_atom.schema.json`
4. `README(2).md`
5. `example_atom(1).json`, illustrative only

SEA governing file: `summary-evaluation-appraisal-protocol-v4-compact.md`.

Supporting workflow: `large-source-ATOM-SEA.md`.

Writing control: `unslop.skill.md`.

No `@VERIFY` macro was activated, so no external clinical or bibliographic source was used to revise the article's claims.
