# 35 - Leary 2021 - JAMA Oncology 210036 processing report

Status: `PASS - ATOM/SEA VERIFIED`

Audit scope: exactly one publication packet.

## Source audit

- Primary source: `jamaoncology_leary_2021_oi_210036_1631288533.71835.pdf`, Drive ID `19U0fd3ji1Cf3w0w9KhsjS7S4V_IU__9I`, 9 pages, SHA-256 `8798e8f048f4eba09ceb53ea420340c996e412af6975fac96491c0169cd5a57d`. The PDF is usable and complete for the published article.
- Identity: Efficacy of Carboplatin and Isotretinoin in Children With High-risk Medulloblastoma: A Randomized Clinical Trial From the Children's Oncology Group
- DOI: `10.1001/jamaoncol.2021.2224`
- Trial registration: `NCT00392327`
- Supplement 1: `coi210036supp1_prod_1631288533.72336.pdf`, 1107-page protocol archive, SHA-256 `366041b1f91889f0e89d112604d10158e766d7d38e3bb9ab90c7384c5644e4c9`.
- Supplement 2: `coi210036supp2_prod_1631288533.72835.pdf`, 11 pages of eMethods, eTables 1 through 5, and eFigures 1 through 3, SHA-256 `ff1a7e4e3ecf6ce0d09046f7b213fafa0cbb7dbea6d529ed4476690874f17d3a`.
- Packet warning: The article points to a separate Supplement 3 data sharing statement; it was not present in the packet or elsewhere in Drive search. This does not affect the trial methods, efficacy, safety, or subgroup result verification.
- Prior identity-matched ATOM, SEA, coverage, reference, or processing outputs: none found before regeneration after title, DOI, content, and identifier searches in the expected GitHub Sync folders.

## ATOM validation

- Atoms: 51. One publication identity. Atom IDs unique.
- Required order executed: `literature(1).py` Pydantic structural validation, then `literature_atom.schema.json` JSON Schema validation, then `literature_atoms(1).py` sufficiency validation.
- Authoritative supplied validator files were executed directly. No reconstructed validator contract was used.
- Structural errors: 0.
- JSON Schema errors: 0.
- Sufficiency errors: 0.
- Sufficiency warnings: 0.
- Duplicate statement and anchor pairs: 0.
- Provenance and source anchors: pass.

## SEA and source coverage

- SEA HTML parses cleanly and contains source metadata, design and methods, main claims, quantitative findings, limitations, appraisal, and provenance.
- Main article: all 9 pages rendered and visually scanned. Four of four main figures and one of one main table reconciled.
- Supplement 2: all 11 pages rendered and visually scanned. Five of five eTables and three of three eFigures reconciled.
- Supplement 1: all 1107 pages text-mapped. The final protocol version dated April 11, 2018 was identified. Key design, scientific aims, eligibility, treatment, and statistical pages were rendered and inspected. Historical duplicate protocol versions and administrative forms were not reproduced because they do not change interpretation of the reported trial results.
- Semantic checks: overall carboplatin EFS 66.4% versus 59.2%, P=.11; group 3 EFS 73.2% versus 53.7%, P=.047; induction grade 3 or higher neutrophil decrease 57.9% versus 30.0%; subgroup-randomization and neurocognitive limitations. All pass against the source.
- ATOM and SEA use the same source packet, hashes, and publication identity. No consequential contradiction was found. Both preserve the main uncertainty that molecular subgroup was not a randomization stratum.

## Reference processing

- Bibliography entries reconciled: 32 of 32.
- Missing reference numbers: 0.
- Duplicate reference numbers: 0.
- Every entry has a role, priority, and downstream action in the task queue.
- Open checkboxes represent downstream cited-publication work. They do not mean this packet's bibliography processing is incomplete.

## Artifact locations

- ATOM JSON: https://drive.google.com/file/d/1jERBbC50Po9tGE5ad2nZ40KefBB_ZTf3/view?usp=drivesdk
- ATOM validation JSON: https://drive.google.com/file/d/1KMK_mzgFvNeMtBNJ7HnqeVBkTvKaoQhY/view?usp=drivesdk
- Coverage JSON: https://drive.google.com/file/d/1uiep3NErDJC7-GcIIcXXiv04jJkIIVdd/view?usp=drivesdk
- SEA HTML: https://drive.google.com/file/d/1hmI2PXBKK2NXnvW-rE36UjkNhGu9_OKZ/view?usp=drivesdk
- Reference task queue: https://drive.google.com/file/d/11K3ZCo9Cn9Sbzxg_5y6q9Mz5f3webRT9/view?usp=drivesdk
- Drive readback: core artifacts were fetched after upload and matched the validated local files byte for byte.

## Governing sources

- ATOM structural validation: `literature(1).py`.
- ATOM serialization: `literature_atom.schema.json`.
- ATOM sufficiency: `literature_atoms(1).py`.
- Workflow intent: `README(2).md`.
- Example atom: illustrative only.
- SEA: `summary-evaluation-appraisal-protocol-v4-compact.md`.
- Large-source coverage: `large-source-ATOM-SEA.md`.
- Historical SEA v3 HTML: reference only.
- Prose control: `unslop.skill.md`.
- No external web verification was used.

## Lifecycle

- Eligibility: all required packet outputs pass.
- Action: `MOVED AND VERIFIED` in `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`.
- Folder name preserved: `35 - Leary 2021 - JAMA Oncology 210036`.
- Folder ID preserved: `1WNQV8PCA43GIM-CYxDuNPpJZYXD_nLcd`.
- Previous parent: `1wA_mmV9fJvfM7ILPwPuc-Uac1SJ1hpk0`.
- New parent: `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`.
- Verification: present under Processed and absent under Active.
- Processing report JSON: https://drive.google.com/file/d/1J5Xii-iXAD9QB4adXFwI1sQN0DVc0Oau/view?usp=drivesdk
- Processing report Markdown: https://drive.google.com/file/d/1Xlezn632vG8GTTBcQ0V3fofeUxa4mqGW/view?usp=drivesdk
- Exact remaining task: none.
