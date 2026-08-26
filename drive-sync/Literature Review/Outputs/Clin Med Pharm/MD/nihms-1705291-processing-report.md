# 101 - nihms-1705291 — Processing Report

**Status:** `PASS - ATOM/SEA VERIFIED`  
**Audit scope:** exactly one publication packet.

## Source audit

- Primary source: `nihms-1705291.pdf` (Drive ID `1SeMx0R3P9li7qKjZDTSj6Gwilz3e6zNJ`), usable, 33 pages, SHA-256 `87a7b06886a98b46fdf1f5ca300a8bcd9053c3026117a19a12eaffb75292a99f`.
- Identity: Pathophysiology and Management of Persistent Pulmonary Hypertension of the Newborn.
- DOI: `10.1016/j.clp.2021.05.009`; citation: Clin Perinatol. 2021;48(3):595–618.
- Source type/version: narrative clinical review; NIH/HHS accepted author manuscript.
- Supplements/attachments: none; packet root contained only the primary PDF.
- Prior identity-matched outputs: none found after packet + GitHub Sync searches by NIHMS ID, DOI, title/identity and content.

## ATOM validation

- Atoms: **80**; one publication identity; atom IDs unique.
- Required order executed: `literature.py` structural validation → `literature_atom.schema.json` JSON Schema validation → `literature_atoms.py` atom-kind sufficiency validation.
- Exact supplied validator files were copied byte-for-byte into the runtime; reconstructed/local substitute contracts were not used.
- Structural errors: **0**; JSON Schema errors: **0**; sufficiency errors: **0**; warnings: **0**; anchor-support failures: **0**; blocking errors: **0**.
- Source SHA-256 is preserved on every atom.
- Semantic spot checks pass for the primary conclusion/practice shift, numerical epidemiology, oxygen-target uncertainty, Figure 7 numerical claim, and Figure 11/Table 3 source-integrity variation.

## SEA and source coverage

- SEA HTML is parseable and contains source metadata, source scope, clinical methods/evidence framing, main claims, quantitative findings, limitations/uncertainty, appraisal, practice translation, and provenance.
- Main-text inventory reconciled: **11 figures + 3 tables + 1 management workflow**; no packet supplements.
- Load-bearing visual crops are embedded for Figures 4, 5, 6, 7, and 11; all other figures/tables are represented structurally.
- Direct semantic spot checks pass for primary conclusion, numerical claim, explicit limitation, and figure-derived quantitative claim.
- ATOM and SEA use the same PDF/version/SHA. No consequential ATOM↔SEA contradiction was found.

## Reference processing

- **80/80** numbered bibliography entries reconciled and assigned downstream class/action.
- Source duplicates are explicitly reconciled: Ref 66→62, Ref 65→63, Ref 71→26.
- Open checkboxes denote future acquisition/appraisal work and do not represent incomplete packet-level reference processing.

## Artifact locations

- ATOM JSON: https://drive.google.com/file/d/15_Brtdu9vXQ7dslv9PqN8Hg3yWpCvpzm/view?usp=drivesdk
- ATOM validation JSON: https://drive.google.com/file/d/1_ZKCx_DVHAXoIaId_ltDbf9IaLJ19TCR/view?usp=drivesdk
- Coverage JSON: https://drive.google.com/file/d/1ZqucGVXQZkaDtPzDnLdt8OSMrNx6PoRS/view?usp=drivesdk
- SEA HTML: https://drive.google.com/file/d/1uCGEK9_jynxFPo5e4PS9WhbAvYSvLSAZ/view?usp=drivesdk
- SEA validation JSON: https://drive.google.com/file/d/1qhsQ5c5joVS0-nNSBfV7LPsbitZMhkN8/view?usp=drivesdk
- Reference task queue: https://drive.google.com/file/d/1RZF_hQHrBL7FEEU1X0UJKrvUVxeQEocc/view?usp=drivesdk
- Processing report JSON: https://drive.google.com/file/d/1Gw_vX7O65iTf-8pqS5U51w-49ePygnyY/view?usp=drivesdk
- Processing report Markdown: https://drive.google.com/file/d/1cHqrbCLApp2OpKMVgq-QRM4ZeH5VCJZe/view?usp=drivesdk

## Warnings

- Evaluated file is an unedited accepted manuscript; production errors may exist.
- Manuscript contains at least one imperfect figure cross-reference.
- Figure 11 and Table 3 give different epinephrine, norepinephrine, and vasopressin dose ranges; they are preserved as separate source contexts and must not be silently harmonized.
- Table 3 aerosolized iloprost is transcribed as `1–2.5 mg/kg every 2–4 h`; dose/unit-sensitive statements require independent current clinical verification before use.
- Source-era FDA/regulatory statements are historical source content and were not externally re-verified in this packet repair.

## Lifecycle

- Eligibility for `90 - Processed`: **YES**.
- Action: **MOVED AND VERIFIED**.
- Folder: `101 - nihms-1705291` (ID `1unogVbc0oE4YtfwinfBjA53s6yh_NM-z`).
- Current/verified parent: `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT` (`5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`).
- Exact remaining task: **none**.

- Move verification: folder ID `1unogVbc0oE4YtfwinfBjA53s6yh_NM-z` has only processed parent `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`; Active-parent search returned no match.
