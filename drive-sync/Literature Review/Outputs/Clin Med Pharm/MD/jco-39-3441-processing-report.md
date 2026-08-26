# 122 - jco-39-3441 processing report

Status: `PASS - ATOM/SEA VERIFIED`

Audit scope: exactly one publication packet.

## Source audit

- Primary source: `jco-39-3441.pdf`, Drive ID `17fkUDHuhMsdY99kVPl1x1GppZ1dvEccn`, 14 PDF pages, SHA-256 `a46e9cedc7c3f2643acf99e5b3f8d2017f1426c92bf2f4f54d14fb9655d44c7d`. The PDF is usable and contains the complete published main article.
- Identity: Acalabrutinib Versus Ibrutinib in Previously Treated Chronic Lymphocytic Leukemia: Results of the First Randomized Phase III Trial
- DOI: `10.1200/JCO.21.01210`
- PMID: `34310172`
- Trial registration: `NCT02477696`
- Packet gap: the article references a Data Supplement and Study Protocol, but neither is present in the packet or identity-matched Drive outputs. This prevents independent review of supplement-only material. It does not prevent verification of the reported main-text methods, efficacy, safety, limitations, four figures, or two tables.
- Prior output audit: an identity-matched SEA and a 37-item reference queue existed. No identity-matched ATOM JSON, validation JSON, coverage JSON, or processing report existed before this repair.

## ATOM validation

- Atoms: 61. One publication identity. Atom IDs are unique.
- Required validator order executed: `literature(1).py`, then `literature_atom.schema.json`, then `literature_atoms(1).py`.
- The supplied authoritative validator files were executed directly. No reconstructed local contract was substituted.
- Structural errors: 0.
- JSON Schema errors: 0.
- Sufficiency errors: 0.
- Sufficiency warnings: 0.
- Duplicate statement and anchor pairs: 0.
- Source anchors and provenance: pass.
- Assertion origin is explicit. Fifty-one atoms are normalized from the source and ten calculated absolute differences are labeled `calculated_from_reported_data`.
- Figure 3 coverage: all 23 displayed prespecified subgroup estimates were atomized directly from the figure.

## SEA and source coverage

- The existing identity-matched SEA HTML parses cleanly and matches the source title, DOI, PMID, trial registration, and PDF hash.
- Methods and design: pass.
- Main claims and quantitative findings: pass.
- Limitations and uncertainty: pass.
- Provenance: pass.
- Main-text visuals: four of four figures and two of two tables reconciled. No main-text algorithm or workflow is present.
- Semantic checks passed for PFS noninferiority, AF/flutter incidence, the open-label limitation, and the Figure 4 cumulative atrial fibrillation hazard ratio.
- ATOM and SEA use the same source and version. No consequential contradiction was found.

## Reference processing

- Bibliography entries reconciled: 37 of 37.
- Missing reference numbers: 0.
- Duplicate reference numbers: 0.
- Every entry now has a role, priority, and downstream action.
- Open checkboxes are separate cited-publication tasks. They do not indicate incomplete bibliography processing for this packet.

## Artifact locations

- ATOM JSON: https://drive.google.com/file/d/123Ew1KhJbHWLyd4pbvdcUdmKW6R6K6CG/view?usp=drivesdk
- ATOM validation JSON: https://drive.google.com/file/d/1kNwky60WWNeluevfastiv3RIXkV3O6yl/view?usp=drivesdk
- Coverage JSON: https://drive.google.com/file/d/1L1nl6EPiHasajE7oJU9BsrUuyvhQH9bH/view?usp=drivesdk
- SEA HTML: https://drive.google.com/file/d/1zoELgCdOupBg-gmCk7O236Cd3fDrYHmI/view?usp=drivesdk
- Reference task queue: https://drive.google.com/file/d/1HkspmgvvsSDqQGLNvqy7qN-duoh6jfUn/view?usp=drivesdk
- Drive readback matched the validated local ATOM, validation, coverage, and reference files byte for byte.

## Governing sources

- ATOM structural validation: `literature(1).py`.
- ATOM serialization: `literature_atom.schema.json`.
- ATOM sufficiency: `literature_atoms(1).py`.
- ATOM workflow: `README(2).md`.
- Example atom: illustrative only.
- SEA: `summary-evaluation-appraisal-protocol-v4-compact.md`.
- Large-source coverage: `large-source-ATOM-SEA.md`.
- Historical SEA v3 HTML: reference only.
- Prose control: `unslop.skill.md`.
- External checks were limited to ASCO and PMC identity metadata. Source extraction and semantic validation used the Drive PDF.

## Lifecycle

- Eligibility: all required packet outputs pass.
- Action: `MOVED AND VERIFIED` in `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`.
- Folder name preserved: `122 - jco-39-3441`.
- Folder ID preserved: `1ZHmmOzghUOC1HPwcwfTYJpgjtYhMA3ld`.
- Previous parent: `1wA_mmV9fJvfM7ILPwPuc-Uac1SJ1hpk0`.
- New parent: `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`.
- Verification: present under Processed and absent under Active.
- Processing report JSON: https://drive.google.com/file/d/1ygUQryzMVkOKgxNiznaPoQsfhCTqrcwL/view?usp=drivesdk
- Processing report Markdown: https://drive.google.com/file/d/1vIzj513ZF5NLpNur0U-pwvcG35VvTvhI/view?usp=drivesdk
- Exact remaining task: none.
