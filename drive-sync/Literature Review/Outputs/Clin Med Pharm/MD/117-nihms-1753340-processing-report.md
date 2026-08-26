# 117 - nihms-1753340 processing report

Status: `PASS - ATOM/SEA VERIFIED`

Audit scope: exactly one publication packet.

## Source audit

- Primary source: `nihms-1753340.pdf`, Drive ID `1yJpTlvUpE8iRdrJgm4irFk-2D98dQYmK`, 45 pages, SHA-256 `42893f6bdb6a86f25e9c5afa32d61fa682873435634b03dbffbe6304beb27198`. The PDF is usable and complete for the supplied author manuscript.
- Identity: *Topical gel-based biomaterials for the treatment of diabetic foot ulcers*. Acta Biomaterialia. 2022;138:73-91. DOI `10.1016/j.actbio.2021.10.045`.
- Source type: narrative review / secondary literature.
- Supplements: none present in the packet; no separate attachments were found.
- Prior identity-matched outputs: SEA HTML and reference queue were found. No matching ATOM JSON, ATOM validation JSON, coverage JSON, or processing report was found before regeneration. The existing reference queue was incomplete under the current processing convention and was repaired in place.

## ATOM validation

- Atoms: 82. Shared publication ID: `b5249d91-3fd4-55b8-8204-a9d32f94e94d`. Atom IDs unique: 82/82.
- Required order executed using the authoritative supplied files directly: `literature(1).py` Pydantic structural validation, `literature_atom.schema.json` JSON Schema validation, then `literature_atoms(1).py` atom-kind sufficiency validation. No reconstructed validator contract was used.
- Structural errors: 0.
- JSON Schema errors: 0.
- Sufficiency errors: 0.
- Sufficiency warnings: 0.
- Duplicate atom IDs: 0. Duplicate statement+anchor pairs: 0.
- Provenance and source anchors: PASS.
- Drive-readback ATOM JSON was rerun through all three authoritative validation layers: PASS, zero errors/warnings.
- Secondary-source integrity: table-derived study findings are tagged `secondary_reported_result` and anchored to this review rather than represented as primary-study evidence. Ranges or thresholds lacking a reported single point estimate were not converted into invented point estimates.

## SEA and source coverage

- Existing identity-matched SEA HTML parses cleanly, all internal navigation anchors resolve, and source title/DOI/hash/publication ID match the current PDF and regenerated ATOM set.
- All 45 PDF pages were rendered and visually scanned. Three of three main-text figures and seven of seven tables are reconciled in the SEA. No algorithms/workflows or material supplements were present.
- Mechanical QA: self-contained HTML; 3 embedded data images; all figure/table headings present; no TODOs, placeholders, internal file/chat citation syntax, or stale planning text.
- Direct semantic checks: review conclusion/translation gap PASS; Table 7 Regranex healing increase 40-50% and 4-6 week faster healing PASS; manufacturing/regulatory/cell/nanoparticle uncertainty PASS; Table 2 >98% day-12 healing versus 95%, 90%, and 70% comparators/control PASS.
- ATOM and SEA reconcile to the same source SHA-256 and publication ID. No consequential contradiction was found.

## Reference processing

- Bibliography entries reconciled: 245 of 245. Missing numbers: 0. Duplicate numbers: 0.
- Every entry now has a role, priority, and downstream action: 245/245 for each field.
- Open checkboxes represent downstream cited-publication work; they do not mean this packet's reference processing is incomplete.

## Artifact locations

- Source PDF: https://drive.google.com/file/d/1yJpTlvUpE8iRdrJgm4irFk-2D98dQYmK/view?usp=drivesdk
- ATOM JSON: https://drive.google.com/file/d/1_2xaCUjY9CYq9xdU8FKOxEnn6HHvfR9Z/view?usp=drivesdk
- ATOM validation JSON: https://drive.google.com/file/d/17XcfxNE5Yeh2RCblMe1qCMoj9G4SGlNU/view?usp=drivesdk
- Coverage JSON: https://drive.google.com/file/d/1y-VQ9y_W7Ne8N7MqWOh4ZM0uvCoOwsCF/view?usp=drivesdk
- SEA HTML: https://drive.google.com/file/d/1eIbMBQoIj9jYibZhNfC6ROWCRCbinKYz/view?usp=drivesdk
- Reference task queue: https://drive.google.com/file/d/12R5s0UwJevBhaGbJ206mrRzpkU2Wr4Vn/view?usp=drivesdk
- Processing report JSON: https://drive.google.com/file/d/1uncKbD9PwAwCPaiYth6A5nPP9hIf7Kmz/view?usp=drivesdk
- Processing report Markdown: https://drive.google.com/file/d/16H53MSBjl9Nqxs9HyW7GJxz2bi2xDVDR/view?usp=drivesdk

## Drive readback

- ATOM JSON SHA-256: `39fefabfd7c665b2fdbf25c8c657781e1b8343f5fb08be3fe9c5fee24af68be4`.
- Validation JSON SHA-256: `d89e256809e4f0994e162e4825952dde2e2b06ad2b49aada0bc14526bb13b9ac`.
- Coverage JSON SHA-256: `ff66f973b66124abfd8ad35ef7f59583e252c376fcb286c6ffa2d6b8564cc610`.
- Reference Markdown SHA-256: `726f6f20bc5a2a5faddb90b136e9d64bbb3c1ca9e2f7e99cd3777f1ea1d37028`.
- SEA HTML SHA-256: `0e7f2fc142ae6bf74fd66317f35f53a77f63d420ab9318fac3eee5d854e3bacd`.

## Governing sources

- ATOM structural validation: `literature(1).py`.
- ATOM serialization: `literature_atom.schema.json`.
- ATOM sufficiency: `literature_atoms(1).py`.
- Workflow intent: `README(2).md`.
- Example atom: illustrative only.
- SEA: `summary-evaluation-appraisal-protocol-v4-compact.md`.
- Large-source coverage: `large-source-ATOM-SEA.md`.
- Historical SEA v3: reference only.
- No external web verification was used.

## Lifecycle

- Eligibility: all required packet outputs pass.
- Action: `MOVED AND VERIFIED` in `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`.
- Folder name preserved: `117 - nihms-1753340`.
- Folder ID preserved: `1i5aqt_YXvTuh0zgETDRE1YIPnVw3JTyc`.
- Previous parent: `1wA_mmV9fJvfM7ILPwPuc-Uac1SJ1hpk0`.
- New parent: `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`.
- Verification: present under Processed and absent under Active.
- Exact remaining task: none.
