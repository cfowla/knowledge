# KDIGO 2017 living kidney donor guideline ATOM + SEA processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Main guideline: *KDIGO Clinical Practice Guideline on the Evaluation and Care of Living Kidney Donors*
- Citation: Kidney Disease: Improving Global Outcomes (KDIGO) Living Kidney Donor Work Group. KDIGO Clinical Practice Guideline on the Evaluation and Care of Living Kidney Donors. Transplantation. 2017;101(Suppl 8S):S1-S109.
- DOI: `10.1097/TP.0000000000001769`
- Main PDF: `KDIGO-2017-Living-Kidney-Donors-Guideline.pdf`, 115 pages, SHA-256 `8864064d6e902574eb2505402e1ff787c38ee1a82476117e22860757373b568a`
- Companion article: *Application of the 2017 KDIGO Guideline for the Evaluation and Care of Living Kidney Donors to Clinical Practice*
- Companion DOI: `10.2215/CJN.12141019`
- Companion PDF: `KDGO-CJASN-LD-GL-review-in-press.pdf`, 10 pages, SHA-256 `82ca6d17ae6be6ed92eed8a6965f99733a2342286b07f3e67e7999d2e3f7e08d`
- Shared LiteratureAtom publication ID for the guideline: `1b99217c-992f-5c65-856f-90f120444063`

The companion article is a separate 2020 publication. It was used as a secondary clinical-application source in SEA and in the reference artifact. It was not forced into the guideline publication ID.

## ATOM status

- Total LiteratureAtoms: **157**
- `other`: **146**
- `method`: **7**
- `limitation`: **3**
- `study_objective`: **1**
- Formal guideline statements captured: **146 of 146**
- Not graded: **140**
- Level 2C: **2**
- Level 2D: **4**
- Local Pydantic contract validation: **PASS**
- Local JSON Schema validation: **PASS**
- Sufficiency validation for the generic atom kinds used: **PASS**
- Structural errors: **0**
- Serialization errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Duplicate review: **PASS**
- Review status: `needs_review`

The current project guideline pattern has no dedicated `guideline_recommendation` atom kind. Formal guidance is serialized as `atom_kind="other"` with chapter, recommendation identifier, grade, strength, and certainty tags when the source provides a grade. Results from cited primary studies remain secondary evidence in this packet and were not promoted to primary-study atoms.

## SEA status

- Guideline chapters represented: **19 of 19**
- Formal guidance table: **146 of 146 statements**
- Main figures inventoried: **21 of 21**
- Main tables inventoried: **24 of 24**
- Companion figures represented: **4 of 4**
- Companion tables represented: **2 of 2**
- Self-contained HTML: **PASS**
- TOC missing anchors: **none**
- Internal chat or file citation syntax: **absent**
- Remote scripts, fonts, and stylesheets: **absent**
- Placeholder and TODO scan: **PASS**
- Final scoring performed after source mapping and reconciliation: **PASS**
- External verification: **not performed**, because `@VERIFY` was not activated

### Appraisal

- Relevance: **10/10**
- Novelty: **9/10**
- Method strength: **8/10**
- Evidence strength: **5/10**
- External validity: **7/10**
- Implementation value: **10/10**

**Verdict:** Read first for the donor-evaluation architecture. Verify current practice before using it as a 2026 policy source. The integrated absolute-risk framework, informed-consent structure, clinical thresholds, and long-term follow-up plan have high operational value. Evidence certainty is uneven, 140 of 146 formal statements are ungraded, and the systematic search ended in September 2014 with selective supplementation through January 2017.

## References

- Main guideline bibliography: **530 listed entries**
- Main source numbering: **1 through 531**
- Missing source number: **509**
- Companion bibliography: **34 references**
- Markdown output: `KDIGO-2017-Living-Kidney-Donors-Guideline-references.md`
- Bibliographic entries were not atomized.

## Source-integrity findings

1. The supplied main guideline bibliography jumps from reference 508 to reference 510. No reference 509 appears. The reference artifact preserves the gap instead of inventing an entry.
2. Companion article reference 25 prints the access-date phrase `Accessed November March 1, 2020`. The wording is preserved and flagged instead of being corrected from an external source.
3. The guideline calls its kidney-failure projection model a proof of concept. The SEA keeps that limitation attached to the risk estimates rather than treating the model as a validated final selection tool.

## Governing-source execution boundary

The retrieved `large-source-ATOM-SEA.md` workflow and `unslop.skill.md` were applied. The named authoritative ATOM files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom.json`, plus the exact `summary-evaluation-appraisal-protocol-v4-compact.md`, were searched in connected project sources but were not directly retrievable in this session.

Structural and serialization checks therefore use a strict local Pydantic contract and generated JSON Schema reconstructed from recent validated project guideline artifacts and the large-source guideline guardrail. This report does not claim execution of unavailable authoritative project code.

## Output files

- `KDIGO-2017-Living-Kidney-Donors-Guideline-atoms.json`
- `KDIGO-2017-Living-Kidney-Donors-Guideline-validation.json`
- `KDIGO-2017-Living-Kidney-Donors-Guideline-coverage.json`
- `KDIGO-2017-Living-Kidney-Donors-Guideline-sea.html`
- `KDIGO-2017-Living-Kidney-Donors-Guideline-references.md`
- `KDIGO-2017-Living-Kidney-Donors-Guideline-processing-report.md`
