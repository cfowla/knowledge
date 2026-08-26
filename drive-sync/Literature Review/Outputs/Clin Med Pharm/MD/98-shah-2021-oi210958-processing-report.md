# Publication packet repair report: 98 - Shah 2021 - oi210958

## Lifecycle status

PASS - ATOM/SEA VERIFIED

## Source identity and packet condition

- Title: Risk of Infection Associated With Administration of Intravenous Iron: A Systematic Review and Meta-analysis
- Citation: JAMA Network Open. 2021;4(11):e2133935
- DOI: 10.1001/jamanetworkopen.2021.33935
- Stable packet identifier: oi210958
- Primary file: `shah_2021_oi_210958_1737557817.362.pdf`
- Primary Drive file ID: `1UELaO6W3gUV45wAqqvicCLrpk4kNKrYu`
- Primary PDF pages: 23
- Primary SHA-256: `ffa884c10754aa053839947707a7e2de1bd22aaea320f8f88e838f8ffb8be9b4`
- Supplement: `zoi210958supp1_prod_1737557817.75976.pdf`
- Supplement Drive file ID: `1Z2KD6ZnU6DgI9IOtzcxJNOWDk9ZcyWsO`
- Supplement PDF pages: 74
- Supplement SHA-256: `2b648f7872159ecc88a275f13ab10b17c93f2d2c6474d77ff063edc1b283c676`
- Main-text figures: 3
- Main-text tables: 2
- Material supplement items: 18
- Primary-source usability: PASS. The current PDF opens normally and contains the article, figures, tables, references, article information, and correction history. The separate supplement also opens normally.

The current main PDF reports corrections in 2022 and 2024 and a January 27, 2025 notice concerning reanalysis after retraction of one included study. The 2021 supplement was retained as the source supplement but is not silently treated as harmonized with the corrected main article.

## Identity-matched artifact audit

The packet itself and the Clin Med Pharm GitHub Sync output folders were searched using title, DOI, stable identifier, source metadata, and content. Filename similarity alone was not accepted as identity proof.

No identity-matched ATOM JSON, authoritative ATOM validation JSON, coverage JSON, SEA HTML, reference task queue, or processing report existed before repair. The packet therefore required regeneration from the current source rather than promotion based on prior artifact claims.

## ATOM regeneration and validation

Generated `98-shah-2021-oi210958-atoms.json` with 42 LiteratureAtom objects. All atoms share publication ID `60e93aef-15eb-5305-a260-8135e25f25b6`. Atom IDs are unique. Every atom has a source anchor and extraction provenance. Model-extracted atoms remain `needs_review` because no independent human reviewer is represented in atom provenance. Packet-level verification is recorded by this audit rather than by changing atom review status.

Validation ran in the required order against the authoritative project sources:

1. `literature(1).py` Pydantic structural validation: PASS, 0 errors
2. `literature_atom.schema.json` JSON Schema validation: PASS, 0 errors
3. `literature_atoms(1).py` atom-kind sufficiency validation: PASS, 0 errors, 0 warnings

Merge integrity passed. There are no duplicate atom IDs or duplicate statement and anchor pairs. The shared publication identity and schema version are consistent across the merged set.

Direct semantic spot checks passed for the corrected primary infection result, the oral-iron and no-iron forest-plot estimates, RBC transfusion requirement, the main limitation about heterogeneity and infection ascertainment, the article correction history, the stale supplement GRADE value, and the eTable 7 arithmetic issue.

## Source-integrity findings preserved

These are source warnings, not validator failures. They were carried into the validation, coverage, and SEA artifacts instead of being silently repaired.

- The Results narrative states 311 full-text articles assessed. The abstract and Figure 1 state 312.
- The main text reports 31 RCTs at low risk of bias, 106 at high risk, and 22 with some concerns. Those counts total 159 despite 154 RCTs in the review, so they cannot be treated as a clean mutually exclusive partition without source clarification.
- The corrected main article reports infection RR 1.16 with 19,322 participants and 16 more infections per 1,000. The original 2021 supplement GRADE table reports RR 1.17 with 19,480 participants and 17 more per 1,000.
- The prose reports 54 RCTs and 12,116 participants for RBC transfusion requirement. Table 2 arm denominators sum to 12,296.
- The prose reports 15 RCTs and 3,445 participants for short-term mortality. Table 2 arm denominators sum to 2,590.
- Supplement eTable 7 contains row totals that do not equal the two comparator columns for several infection-site rows. One printed example is genitourinary 6 plus 7 with a displayed total of 35. These values were preserved as source-integrity problems rather than recalculated by inference.

## SEA regeneration and verification

Generated one self-contained HTML appraisal from the same current primary source and supplement.

- HTML parseability: PASS
- Source title, citation, DOI, evaluated filenames, and version note: PASS
- Design characterization: PASS. The artifact identifies a systematic review and random-effects meta-analysis of RCTs with descriptive nonrandomized-study synthesis.
- Methods and design: PASS
- Main claims: PASS
- Quantitative findings: PASS
- Limitations and uncertainty: PASS
- Provenance: PASS
- Table-of-contents anchors: PASS, 0 missing targets
- Internal chat or file citation syntax: absent
- TODO and stale planning text: absent
- Main figures: 3 of 3 reconciled
- Main tables: 2 of 2 reconciled
- Material supplement items: 18 of 18 reconciled

Semantic checks included the primary result, a numerical efficacy claim, a limitation claim, Figure 2 and Figure 3 estimates, Table 2 transfusion findings, the correction history, and supplement-derived source-integrity warnings.

The corrected main paper is the operative source version for conflicting corrected estimates. The older supplement values remain visible where necessary to document the version mismatch.

## Reference processing

Reference processing was checked against the primary PDF rather than accepted from file presence alone.

- Numbered bibliography entries in source: 208
- Queue entries: 208
- Numbering represented: 1 through 208, contiguous
- Status: PASS

The unchecked queue items are downstream cited-publication tasks. They do not indicate missing bibliography extraction from this packet and do not block closure of the primary publication packet under the current processed-packet convention.

## ATOM and SEA reconciliation

ATOM and SEA use the same primary PDF, supplement, source hashes, and publication identity. Consequential methods, primary infection findings, secondary hematologic and transfusion outcomes, uncertainty, correction history, and figure/table-derived claims were checked across both artifacts. No cross-artifact contradiction requiring repair remains.

Where the main article and supplement disagree after correction, both artifacts give precedence to the corrected main article while recording the supplement as stale rather than harmonizing it by inference.

## Output locations

JSON, `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`:

- `98-shah-2021-oi210958-atoms.json`, Drive ID `1qhO1kUf0765eWS0K_j2U-A-IVFYCqnaz`
- `98-shah-2021-oi210958-validation.json`, Drive ID `1GhsJtMIJcemm169aSHUjINHAQ9t_-Dj3`
- `98-shah-2021-oi210958-coverage.json`, Drive ID `1oi_GQ56Y9YiZLGcIoe5gxpWEaq9oRk_C`

HTML, `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`:

- `98-shah-2021-oi210958-sea.html`, Drive ID `1Y30KDu_ADnDEjEtt5eQ1KiiD0uERY6JX`

Markdown, `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`:

- `98-shah-2021-oi210958-reference-task-queue.md`, Drive ID `1TFEiqe_QY9lSmzBsUlV_6CAf-ObQeDzm`
- `98-shah-2021-oi210958-processing-report.md`, Drive ID `1z0wY9KBrb7cqCaDw4T2ZaWZBvGLI-S7h`

## Governing and supporting sources

ATOM validation used `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom(1).json`. The example was treated as illustrative only.

SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing protocol. `large-source-ATOM-SEA.md` guided coverage and reconciliation. `summary-evaluation-appraisal-protocol-v3-compact.html` was historical reference only. `unslop.skill.md` controlled prose style.

No external web verification was used. Extraction, validation, SEA appraisal, reference processing, and packet status were grounded in the Drive source files and the supplied project contracts.

## Lifecycle action

Status is PASS - ATOM/SEA VERIFIED.

The folder `98 - Shah 2021 - oi210958`, Drive ID `1wV2_beyNPzO_fEdXslKhFyzvb0PQhskL`, was moved from Active Clinical Medicine & Pharmacy to `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`. The folder name and Drive ID were preserved.

Move evidence:

- Previous parent: `1wA_mmV9fJvfM7ILPwPuc-Uac1SJ1hpk0`
- New parent: `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`
- Move result: PASS
- Post-move verification: present under the processed clinical parent and absent under the active clinical parent

Exact remaining task: none for this publication packet. The 208 unchecked reference-queue entries are downstream cited-publication tasks outside this closed packet.
