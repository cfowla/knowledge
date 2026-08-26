# Processing Report — 39 - NEJMoa2108269

## Lifecycle status

**PASS - ATOM/SEA VERIFIED**

Source identity: *Cardiovascular and Renal Outcomes with Efpeglenatide in Type 2 Diabetes*. New England Journal of Medicine. 2021;385:896-907. DOI `10.1056/NEJMoa2108269`. PMID `34215025`. Trial `NCT03496298`.

## Source audit

- Primary PDF: `NEJMoa2108269.pdf`, 12 pages, SHA-256 `29e306e2b7d40b6d690f9d2ceb6e5d53e349056e2554c88b154d15ae91fa08e9`.
- Protocol/SAP: `nejmoa2108269_protocol.pdf`, 335 pages, SHA-256 `91994df157f2559a3b8f02ff5efc669750479b5a3091883119f45413452445c4`.
- Supplementary appendix: `nejmoa2108269_appendix.pdf`, 38 pages, SHA-256 `1c9ce4d7f05b2c70e6aa53f8ba5f4cc1917cbdc593dca00260c6cf4ecb84f348`.
- Primary source is readable, unencrypted, internally complete from article page 896 through 907, and source identity matches both supplements.
- All 12 primary PDF pages were rendered and visually reviewed. Main-text Table 1, Table 2, Table 3, Figure 1, and Figure 2 were reconciled. The supplementary appendix inventory reconciled Figures S1-S5 and Tables S1-S8. The protocol/SAP was inspected for material prespecified design and analysis boundaries.

## Artifact audit and repair

No identity-matched packet artifacts were found in the packet folder or the appropriate `GitHub Sync / Literature Review / Outputs / Clin Med Pharm` type folders. Other documents that merely cited this DOI were rejected as source-mismatched artifacts. The following source-specific outputs were regenerated from the current packet and then read back from Drive:

| Artifact | Drive location | Result |
|---|---|---|
| ATOM JSON | `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON / 39-NEJMoa2108269-atoms.json` — https://drive.google.com/file/d/1pS_VkRA__hz_sfJjD0IC2Sd8cUQgY2JH/view | Regenerated; 43 atoms; one publication ID; unique atom IDs; current primary-source hash in provenance. |
| ATOM validation JSON | `... / JSON / 39-NEJMoa2108269-validation.json` — https://drive.google.com/file/d/1gtizVNSyByUUN2RK7Hl9jiRocj_l9XUN/view | PASS; zero blocking errors; zero warnings. |
| Coverage JSON | `... / JSON / 39-NEJMoa2108269-coverage.json` — https://drive.google.com/file/d/1ixiCrtFtt6dGq09nA5W-nOhzG8WQ3U0w/view | PASS; all main-text and material supplemental visual/table items reconciled. |
| SEA HTML | `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML / 39-NEJMoa2108269-SEA.html` — https://drive.google.com/file/d/1zMuOVkpnOkANFDoXeebFZXTZxSNQwGmA/view | Regenerated; parseable self-contained HTML; semantic/mechanical QA pass. |
| Reference task queue | `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD / 39-NEJMoa2108269-reference-task-queue.md` — https://drive.google.com/file/d/1YsJr_-TIqjONexZ6ErPSjKtxFcT7DTn7/view | PASS; 30 source references reconciled to 30 contiguous queue entries. |
| Processing report | `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD / 39-NEJMoa2108269-processing-report.md` | This report. |

## Authoritative ATOM validation

Validation was run against the governing project files supplied to this Evidence Analysis project, in the required order:

1. `literature.py` Pydantic structural validation: **43/43 PASS**.
2. `literature_atom.schema.json` JSON Schema validation: **43/43 PASS**.
3. `literature_atoms.py` atom-kind sufficiency validation: **43/43 PASS**.

Blocking errors: **0**. Sufficiency warnings: **0**.

Merge/source integrity: one deterministic publication UUID (`4e4563f4-5786-5636-aaae-768bef8bb583`); 43 unique atom IDs; all atoms use the same publication identity; current primary PDF SHA-256 is preserved in every atom provenance record; no duplicate canonical statements; all retained atoms are marked verified.

Direct ATOM semantic spot-checks passed for:

- Primary MACE: 189/2717 vs 125/1359; HR 0.73 (95% CI 0.58-0.92); superiority P=0.007.
- Composite renal outcome: HR 0.68 (95% CI 0.57-0.79); P<0.001.
- Prespecified SGLT2 subgroup claim: baseline users HR 0.70 (95% CI 0.37-1.30), nonusers HR 0.74 (0.58-0.94).
- Limitation: short follow-up and 314 primary events vs 330 planned.
- Table 3 safety claim: severe gastrointestinal adverse events 3.3% vs 1.8%, P=0.009.

The uploaded ATOM JSON was downloaded from Drive after upload and rerun through the same authoritative validator sequence; the readback result remained PASS with zero errors/warnings.

## SEA validation

- HTML parses successfully; IDs are unique and all table-of-contents anchors resolve.
- Required source metadata, randomized design/methods, main claims, quantitative findings, limitations/uncertainty, clinical PICO, appraisal dimensions, implementation boundary, and provenance are present.
- Every appraisal score includes rationale, evidence basis, principal limiting factor, and conditions that would raise or lower the score.
- Main text: Table 1, Table 2, Table 3, Figure 1, and Figure 2 are represented as structured evidence blocks.
- Supplement: Figures S1-S5 and Tables S1-S8 are represented as structured evidence blocks; the protocol/SAP has a separate material-supplement block.
- No internal chat/file citation syntax, TODOs, placeholders, or planning language remains.
- Direct semantic spot-checks passed for the primary conclusion, primary MACE result, renal numerical result, 314/330 uncertainty statement, Figure 2 subgroup result, and Table 3 gastrointestinal safety result.
- The uploaded HTML was downloaded from Drive after upload and the parse/anchor/coverage checks remained PASS.

## ATOM ↔ SEA reconciliation

ATOM and SEA identify the same article, DOI, PMID, trial, primary SHA-256, protocol SHA-256, and appendix SHA-256. The primary MACE result, renal composite, SGLT2 subgroup uncertainty, early-closeout limitation, gastrointestinal safety signal, randomized design, high-risk eligibility boundary, funding, and provenance are handled consistently. No consequential contradiction or source-integrity mismatch remains.

## Reference-processing verification

The primary article contains exactly 30 numbered references. The regenerated queue contains exactly 30 contiguous tasks numbered 1 through 30 under the correct article title, DOI, PMID, and current primary-source hash. References 1, 10, 15, 16, and 30 were spot-checked directly against the article. Queue presence was not accepted as completion evidence; count, numbering, identity, and representative citation fidelity were verified. Unchecked boxes are the intended downstream retrieval/review tasks and do not indicate missing extraction from this publication packet.

## Warnings

- Median follow-up was 1.81 years and the trial accrued 314 primary MACE events rather than the planned 330.
- Final visits began early because of a sponsor funding decision reported by the authors as unrelated to trial data.
- The study enrolled a selected high-risk population with cardiovascular and/or kidney disease, limiting generalizability to lower-risk type 2 diabetes.
- Baseline SGLT2-inhibitor use was 15.2%; the baseline-user subgroup confidence interval was wide.
- This packet audit validates the 2021 source and its artifacts. It does not independently establish current 2026 regulatory availability, guideline position, formulary status, or treatment sequencing.

## Lifecycle action

All packet-specific requirements passed. The folder `39 - NEJMoa2108269` was moved, preserving its name, from `2 - 10 - Active Literature / 1 - Clinical Medicine & Pharmacy` to `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`. Drive move response reported the Processed clinical folder (`1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`) as the folder's parent. A post-move parent-scoped search found the packet under Processed and found no matching packet remaining under the Active clinical parent.

**Exact remaining task:** None. Packet lifecycle is closed.
