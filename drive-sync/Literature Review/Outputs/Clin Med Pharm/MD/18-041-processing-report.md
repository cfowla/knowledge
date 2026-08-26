# 32 - 18-041 — Processing Report

**Status:** `PASS - ATOM/SEA VERIFIED`  
**Audit scope:** exactly one publication packet.

## Source audit

- Primary source: `18-041.pdf` (Drive ID `1Ou1YB2BCy3_0KrYjyg1w24QW2V3lMSK1`), usable, 5 pages, SHA-256 `e9cfebe538067e1264052790821f711233970be5d2b1bb637aba9fedea5d221a`.
- Identity: Cannabidiol in Anxiety and Sleep: A Large Case Series.
- DOI: `10.7812/TPP/18-041`; citation `Perm J. 2019;23:18-041`.
- Supplements/attachments: none.
- Packet root contained only the primary PDF.
- Prior identity-matched outputs: SEA HTML and reference queue found; ATOM JSON, ATOM validation JSON, coverage JSON, and processing reports were absent. The SEA provenance and reference-processing artifact were repaired from the current source.

## ATOM validation

- Atoms: **51**; one publication identity; atom IDs unique.
- Required validator order executed: `literature.py` structural validation -> `literature_atom.schema.json` JSON Schema -> `literature_atoms.py` atom-kind sufficiency validation.
- Exact supplied validator files were copied byte-for-byte into the runtime; no reconstructed/local substitute contracts were used.
- Structural errors: **0**; JSON Schema errors: **0**; sufficiency errors: **0**; warnings: **0**; blocking errors: **0**.
- Provenance/source-anchor support: **51/51 pass**; source SHA-256 preserved on every atom.
- Direct semantic spot checks passed for the month-1 anxiety result, Table 1 HAM-A value, no-comparator limitation, dechallenge/rechallenge safety event, and cautious RCT-needed conclusion.

## SEA and source coverage

- SEA HTML is parseable and contains source metadata, methods/design, main claims, quantitative findings, limitations/uncertainty, appraisal, and provenance.
- Main-text visual inventory reconciled: **1 figure + 1 table**; no algorithms/workflows; no supplements. Both load-bearing visuals are represented as structured content.
- Semantic spot checks pass: primary result/conclusion; numerical retention claim; limitation/uncertainty; Figure 1/Table 1 trajectory claim.
- Stale provenance naming an earlier folder path was repaired to the current packet/source hash.
- ATOM and SEA use the same current PDF/version; no consequential contradiction or inconsistent uncertainty handling was found.

## Reference processing

- **24/24** bibliography entries reconciled, no missing/duplicate entries, and every entry has an assigned downstream class/action.
- Open checkboxes are future acquisition/appraisal tasks and do not represent unfinished packet-level reference processing.

## Artifact locations

- ATOM JSON: https://drive.google.com/file/d/1uYUNMzb_Nj6uRWvarU1-6UB4tkKYMqUA/view?usp=drivesdk
- ATOM validation JSON: https://drive.google.com/file/d/1t-w8UV7M61ISPH8pJYtsMcFbB2-Hxa6J/view?usp=drivesdk
- Coverage JSON: https://drive.google.com/file/d/1AzfEP9W5k6eJ3auyqqhd__av1ijCN2dM/view?usp=drivesdk
- SEA HTML: https://drive.google.com/file/d/1c1P3tHuA_TvhFneYSpf0gRpbTx9XA7eT/view?usp=drivesdk
- Reference task queue: https://drive.google.com/file/d/10R4uVnidiAREDjv9gCYz1zdn_wWrWaH3/view?usp=drivesdk

## Warnings

- The project-governing SEA file is named `summary-evaluation-appraisal-protocol-v4-compact.md` but its internal heading self-identifies as Integrated Compact v3; project precedence makes the v4-named file authoritative.
- The article's legal-status discussion is historical source content; no external current-law verification was used.
- Table 1 does not report group-specific denominators for later follow-up means; this uncertainty is preserved in the SEA and ATOM artifacts.

## Lifecycle

- Eligibility: all required ATOM, SEA, coverage, and packet-level reference-processing gates pass.
- Action: **MOVED AND VERIFIED** in `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`.
- Folder name to preserve: `32 - 18-041`.
- Move verification: folder ID `1oPDc8kkuOK5TY_6-4MpfhYo64MXe9eI_` now has parent `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`; it is absent from the prior Active parent.
- Exact remaining task: **none**.

- Processing report JSON: https://drive.google.com/file/d/1psz8PrFVRmjESCUt5R6ThQmTtfYPp-2J/view?usp=drivesdk
- Processing report Markdown: https://drive.google.com/file/d/131GSPyIpHjUVBxg-ERwH41YyAailFyDE/view?usp=drivesdk
