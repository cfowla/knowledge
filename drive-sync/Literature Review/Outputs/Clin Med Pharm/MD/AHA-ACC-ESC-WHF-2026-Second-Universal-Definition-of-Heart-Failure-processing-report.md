# 2026 Second Universal Definition of Heart Failure processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Main source: *AHA/ACC/ESC/WHF Expert Consensus Document: Second Universal Definition of Heart Failure (2026)*
- Source type: multisociety expert consensus document
- DOI: `10.1016/j.jacc.2026.05.036`
- Main PDF: 16 pages, SHA-256 `5572532a8ad32a0f1610aa57cae3e13a73f743fd40afdfca3d4f708345e69419`
- Substantive main text: pages 1-10
- References: pages 11-13
- Main writing-group and reviewer disclosures: pages 14-16
- Companion disclosure supplement: `mmc1(2).pdf`, 26 pages, SHA-256 `8bb9416bb0218a8d054392be25e40fb23cae2fe07e16dec2991764a5d400bcc4`
- Shared LiteratureAtom publication ID: `d422f8be-3689-511c-ba26-f2e5a5929faa`

The document explicitly states that it is not a clinical practice guideline and not a clinical decision support document. Treatment recommendations remain the responsibility of current and future professional society heart failure guidelines.

## ATOM status

- LiteratureAtoms: **58**
- Atom kinds: `{'author_conclusion': 4, 'conflict_of_interest': 2, 'limitation': 3, 'method': 4, 'other': 44, 'study_objective': 1}`
- Assertion origin: `normalized_from_source` for all atoms
- Review status: `needs_review` for all atoms
- Shared publication identity: PASS
- Unique atom IDs: PASS
- Local Pydantic structural validation: PASS
- Local generated JSON Schema validation: PASS
- Sufficiency validation for the extracted generic atom kinds: PASS
- Structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0

Semantic batches:

| Batch | Scope | Atoms |
| --- | --- | ---: |
| `hf2026-global-v1` | source type, purpose, multisociety framework, major changes | 5 |
| `hf2026-definition-stages-v1` | HF syndrome definition, stages A-D, risk reduction and screening | 15 |
| `hf2026-phenotypes-causes-v1` | LVEF grouping, cause taxonomy, geography and generalizability | 15 |
| `hf2026-trajectories-v1` | improvement, remission, recovery, worsening HF and decompensation | 11 |
| `hf2026-presentations-mimics-v1` | acute and chronic presentation, mimics, conclusions | 9 |
| `hf2026-disclosures-v1` | approvals and conflict disclosures | 3 |

The current recovered LiteratureAtom pattern has no dedicated expert-consensus definition, consensus classification, or consensus recommendation kind. Consensus definitions and classifications are represented as `atom_kind="other"`. Panel interpretations are represented as `author_conclusion`. Cited primary-study results remain secondary reports and are tagged `secondary_reported_result`; they are not represented as if this consensus document generated primary participant data.

## SEA status

- Main PDF pages rendered and visually scanned: **16/16**
- Companion disclosure pages rendered and visually scanned: **26/26**
- Main substantive pages represented: **10/10**
- Main figures reconciled: **1/1**
- Main tables reconciled: **3/3**
- Main disclosure pages inspected: **3/3**
- Claims and appraisal separated: PASS
- Appraisal performed after source extraction and reconciliation: PASS
- Self-contained HTML: PASS
- Internal chat or file citation syntax in HTML: absent
- Remote scripts, fonts, images, and stylesheets: absent
- Placeholder or TODO scan: PASS
- External verification: not performed because `@VERIFY` was not activated

The appraisal treats the document as a terminology and classification authority rather than a treatment guideline. Its main implementation value is the revised LVEF framework, cause taxonomy, trajectory language, distinction between worsening and decompensated HF, and explicit placement of geographic and social context inside the HF framework.

Local project-pattern scores, not claimed as execution of the unavailable exact SEA v4 rubric:

- Relevance: **10/10**
- Novelty: **9/10**
- Method strength: **7/10**
- Evidence strength: **7/10**
- External validity: **8/10**
- Implementation value: **9/10**

Verdict: Read first for 2026 HF terminology, literature normalization, registry structure, and CDS data modeling. Pair it with current HF practice guidelines for treatment decisions.

## References

- Main bibliography entries extracted: **71/71**
- Source numbering preserved
- Markdown output: `AHA-ACC-ESC-WHF-2026-Second-Universal-Definition-of-Heart-Failure-references.md`
- Text-layer line wrapping and obvious font-glyph artifacts were normalized
- No external bibliography lookup or correction was used
- Bibliographic entries were not atomized

## Disclosure handling

The main article includes writing-group and reviewer disclosure tables. The 26-page companion report adds 2024 and 2025 national society reviewer declarations. These materials were visually inspected and used for conflict-of-interest context. They were not reconstructed or atomized one relationship at a time.

## Governing-source execution boundary

The retrieved `large-source-ATOM-SEA.md` workflow and `unslop.skill.md` were applied.

The named authoritative files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, `example_atom.json`, and `summary-evaluation-appraisal-protocol-v4-compact.md` were searched in connected project sources but were not directly retrievable in this session.

Structural and serialization checks therefore use a strict local Pydantic contract and generated JSON Schema reconstructed from recent validated project LiteratureAtom outputs and the retrieved large-source guardrail. This report does not claim execution of unavailable authoritative project code or the unavailable exact SEA v4 scoring rubric.

## Output files and routing

JSON folder:
- `AHA-ACC-ESC-WHF-2026-Second-Universal-Definition-of-Heart-Failure-atoms.json`
- `AHA-ACC-ESC-WHF-2026-Second-Universal-Definition-of-Heart-Failure-validation.json`
- `AHA-ACC-ESC-WHF-2026-Second-Universal-Definition-of-Heart-Failure-coverage.json`

HTML folder:
- `AHA-ACC-ESC-WHF-2026-Second-Universal-Definition-of-Heart-Failure-sea.html`

Markdown folder:
- `AHA-ACC-ESC-WHF-2026-Second-Universal-Definition-of-Heart-Failure-references.md`
- `AHA-ACC-ESC-WHF-2026-Second-Universal-Definition-of-Heart-Failure-processing-report.md`
