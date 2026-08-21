# 2022 AHA/ACC/HFSA heart failure guideline processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Main source: *2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure*
- Citation: Heidenreich PA, Bozkurt B, Aguilar D, et al. *J Am Coll Cardiol.* 2022;79:e263-e421.
- DOI: `10.1016/j.jacc.2021.12.012`
- Main PDF: `159` pages, SHA-256 `c2f1c0124c4c80f556540377132d34e2b98cf11f04e4cd7fa91e34fd9b8281bc`
- Online Data Supplement: `807` PDF pages spanning printed source pagination 1-844, SHA-256 `3b6c15df77c88efcc1c4c7d193b15464dab869302345c547f5a6d79e211607f4`
- Comprehensive writing-committee RWI supplement: `12` pages, SHA-256 `5088b97b34064f0d67059d6a315b9022a05fd58dce473e45c3f3d0f169087a07`
- Shared publication ID: `5e3b1762-f87c-56d7-9b8f-44d543955ebd`

## ATOM status

- LiteratureAtoms: **201**
- Formal guidance atoms: **189**
- Source COR/LOE recommendations: **177**
- Source economic value statements: **12**
- Atom kinds: `{'study_objective': 1, 'method': 3, 'other': 194, 'limitation': 2, 'conflict_of_interest': 1}`
- Shared publication identity: PASS
- Unique atom IDs: PASS
- Local Pydantic contract validation: PASS
- Local JSON Schema validation: PASS
- Local sufficiency check for extracted generic kinds: PASS
- Structural errors: 0
- Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Review status: all atoms remain `needs_review`

The recovered LiteratureAtom pattern has no dedicated guideline recommendation or economic value statement kind. Formal guidance is represented as `atom_kind="other"` with tags preserving section, recommendation number, Class of Recommendation, Level of Evidence, or economic value grade.

Underlying trial effects summarized by the guideline remain secondary evidence. They were used in SEA evidence synthesis but were not represented as primary-study LiteratureAtoms.

## Formal guidance profile

- Class 1: **81**
- Class 2a: **50**
- Class 2b: **21**
- Class 3 Harm: **16**
- Class 3 No Benefit: **9**
- LOE A: **26**
- LOE B-R: **46**
- LOE B-NR: **59**
- LOE C-LD: **39**
- LOE C-EO: **7**

## SEA coverage and QA

- Main numbered figures: **15/15 inventoried**
- Main numbered tables: **33/33 inventoried**
- Online Data Supplement evidence-table blocks: **99**
- Key decision-path figures rendered and visually checked: HF stages, LVEF classification, diagnostic algorithm, HFrEF treatment, CRT, HFmrEF, HFpEF, transthyretin amyloidosis, selected comorbidities, and disease-course/palliative trajectory
- Claims and appraisal separated: PASS
- Scoring performed after extraction and reconciliation: PASS
- Self-contained HTML: PASS
- Internal chat or file citation syntax in HTML: absent
- Placeholder/TODO scan: PASS
- External verification: not performed because `@VERIFY` was not activated

### Source-level appraisal

The guideline is a high-value foundational HF reference. Its strongest evidence is concentrated in HFrEF pharmacotherapy and selected device questions. Evidence becomes less uniform in HFmrEF, HFpEF, diagnostics, implementation, advanced HF, and special populations. The document's breadth is a practical strength but means the COR/LOE attached to each recommendation matters more than an overall judgment of guideline quality.

Local project-pattern scores, not claimed as execution of the unavailable named SEA v4 rubric:

- Relevance: **10/10**
- Novelty at publication: **9/10**
- Method strength: **9/10**
- Evidence strength: **8/10**
- External validity: **8/10**
- Implementation value: **10/10**

**Verdict:** Read first as a foundational heart-failure guideline, with recommendation-specific confidence and an explicit currency check for decisions affected by evidence published after 2021.

## References

The Markdown reference artifact contains the main guideline reference section from printed pages e371-e410 in source order. The source uses section-local reference numbering, so that numbering is preserved. Evidence-table citations in the Online Data Supplement were used for reconciliation but were not duplicated as a second bibliography.

## Governing-source execution boundary

The large-source workflow `large-source-ATOM-SEA.md` was available and applied. `unslop.skill.md` was retrieved from the project Google Drive and applied to prose artifacts.

The named authoritative files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, `example_atom.json`, and `summary-evaluation-appraisal-protocol-v4-compact.md` were searched in connected project sources but were not directly retrievable in this session. The validation artifacts therefore use a strict local Pydantic contract and generated JSON Schema reconstructed from recent validated project LiteratureAtom outputs plus local sufficiency checks. This run does not claim execution of the unavailable authoritative project code or exact SEA v4 scoring rubric.

## Output files

- `AHA-ACC-HFSA-2022-Heart-Failure-Guideline-atoms.json`
- `AHA-ACC-HFSA-2022-Heart-Failure-Guideline-validation.json`
- `AHA-ACC-HFSA-2022-Heart-Failure-Guideline-coverage.json`
- `AHA-ACC-HFSA-2022-Heart-Failure-Guideline-sea.html`
- `AHA-ACC-HFSA-2022-Heart-Failure-Guideline-references.md`
- `AHA-ACC-HFSA-2022-Heart-Failure-Guideline-processing-report.md`
