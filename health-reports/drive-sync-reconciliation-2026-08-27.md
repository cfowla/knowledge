# Drive sync reconciliation audit: 2026-08-27

## Scope

Repository: `cfowla/knowledge`  
Audited path: `drive-sync/`  
Sync identity: `google-drive-sync[bot]`  
Audit window: 2026-08-24 through 2026-08-27  
Known incident: `8cce889c3597a69006d0337269bcad419f931ca6`

This is an inventory and reconciliation record. No publication artifact was changed or restored as part of this audit.

The complete changed-file lists were inspected for all four Drive-sync commits in the window. Large commits were checked through all available changed-file pages so removals were not inferred from a truncated comparison. The first deletion in the window was also traced backward. Its deleted path first appeared in the 2026-08-23 Drive-sync commit `cd5976a1797261698c41e921ca2e900c2003c9c6`, not in a GitHub-authored publication commit, so the audit window did not need to extend earlier than 2026-08-24.

## Summary

| Result | Count |
| --- | ---: |
| Drive-sync commits audited | 4 |
| Removed paths | 19 |
| Expected Drive-owned deletions or supersessions | 3 |
| GitHub-only files deleted by sync | 16 |
| GitHub-only deletions later restored unchanged | 1 |
| GitHub-only deletions later replaced by a newer valid version | 6 |
| Unresolved losses | 9 |
| Current versions found to be older than the deleted version | 0 |

The nine unresolved paths are all from one repository-only application tree, `drive-sync/Acquisition Runtime/pmc-acquire-web/`, added by non-sync commit `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` and deleted by the next Drive sync. No unresolved publication-artifact loss remains from the 2026-08-27 incident.

## Sync commits audited

| Sync commit | Timestamp UTC | Removed paths | Finding |
| --- | --- | ---: | --- |
| `50e68fac10b71acedef64e4c8b2430dae805961d` | 2026-08-24 08:23:16Z | 1 | One Drive-owned reference artifact was superseded by the reconciled queue naming. |
| `55ec019884604dabe0efe8be15992c34257e6f35` | 2026-08-25 08:21:59Z | 9 | Deleted the GitHub-only `pmc-acquire-web` application tree. All nine remain absent. |
| `db9d93e1c8a24a3036d881c1e6dd1524385c2c61` | 2026-08-26 08:21:36Z | 2 | Two Drive-owned IJO artifact names were superseded by canonical replacements. |
| `8cce889c3597a69006d0337269bcad419f931ca6` | 2026-08-27 05:15:48Z | 7 | Deleted seven newly GitHub-authored ADA artifacts. All seven were later recovered; one unchanged and six as newer valid versions. |

## Deletion inventory

### 2026-08-24: `50e68fac10b71acedef64e4c8b2430dae805961d`

| Removed path | First appeared | Last pre-delete change | Last substantive source | Current status | Classification | Required action |
| --- | --- | --- | --- | --- | --- | --- |
| `drive-sync/Literature Review/Outputs/Clin Med Pharm/MD/haring-merker-2013-references.md` | `cd5976a1797261698c41e921ca2e900c2003c9c6`, 2026-08-23 07:59:37Z | `cd5976a1797261698c41e921ca2e900c2003c9c6` | Drive sync bot | Exact old path is absent. The same 2026-08-24 sync added `haring-merker-2013-reference-task-queue.md` and a queue reconciliation report. The canonical task queue remains present. | Expected Drive-owned deletion; superseded by a newer valid canonical artifact. | None. |

### 2026-08-25: `55ec019884604dabe0efe8be15992c34257e6f35`

All nine paths below first appeared in non-sync commit `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` at 2026-08-25 02:31:11Z. That commit, authored by Connor Fowler, added the standalone PMC acquisition web interface. It was the last substantive change before the 08:21:59Z Drive sync deleted the tree. The current directory returns no content, and current repository searches found no `pmc_acquire.py` or `PMC Acquire Web` replacement elsewhere.

| Removed path | First appeared | Pre-delete commit | Last substantive source | Current status | Classification | Required action |
| --- | --- | --- | --- | --- | --- | --- |
| `drive-sync/Acquisition Runtime/pmc-acquire-web/.gitignore` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | Human, non-sync | Absent | GitHub-only file deleted by sync; unresolved loss. | In a separate task, restore or rehome from `2be007f` if the application is retained, or explicitly retire it. |
| `drive-sync/Acquisition Runtime/pmc-acquire-web/README.md` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | Human, non-sync | Absent | GitHub-only file deleted by sync; unresolved loss. | Restore or rehome from `2be007f`, or explicitly retire the application. |
| `drive-sync/Acquisition Runtime/pmc-acquire-web/pmc_acquire.py` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | Human, non-sync | Absent | GitHub-only file deleted by sync; unresolved loss. | Restore or rehome from `2be007f`, or explicitly retire the application. |
| `drive-sync/Acquisition Runtime/pmc-acquire-web/runs/.gitkeep` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | Human, non-sync | Absent | GitHub-only file deleted by sync; unresolved loss. | Restore with the tree if the application is retained; otherwise retire with the tree. |
| `drive-sync/Acquisition Runtime/pmc-acquire-web/server.py` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | Human, non-sync | Absent | GitHub-only file deleted by sync; unresolved loss. | Restore or rehome from `2be007f`, or explicitly retire the application. |
| `drive-sync/Acquisition Runtime/pmc-acquire-web/static/app.js` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | Human, non-sync | Absent | GitHub-only file deleted by sync; unresolved loss. | Restore or rehome from `2be007f`, or explicitly retire the application. |
| `drive-sync/Acquisition Runtime/pmc-acquire-web/static/index.html` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | Human, non-sync | Absent | GitHub-only file deleted by sync; unresolved loss. | Restore or rehome from `2be007f`, or explicitly retire the application. |
| `drive-sync/Acquisition Runtime/pmc-acquire-web/static/style.css` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | Human, non-sync | Absent | GitHub-only file deleted by sync; unresolved loss. | Restore or rehome from `2be007f`, or explicitly retire the application. |
| `drive-sync/Acquisition Runtime/pmc-acquire-web/tests/test_smoke.py` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` | Human, non-sync | Absent | GitHub-only file deleted by sync; unresolved loss. | Restore or rehome from `2be007f`, or explicitly retire the application. |

### 2026-08-26: `db9d93e1c8a24a3036d881c1e6dd1524385c2c61`

Both deleted paths first appeared in the prior Drive-sync commit `55ec019884604dabe0efe8be15992c34257e6f35` at 2026-08-25 08:21:59Z. No human or non-sync substantive change intervened.

| Removed path | First appeared | Pre-delete commit | Last substantive source | Current status | Classification | Required action |
| --- | --- | --- | --- | --- | --- | --- |
| `drive-sync/Literature Review/Outputs/Clin Med Pharm/HTML/IJO-66-717-sea.html` | `55ec019884604dabe0efe8be15992c34257e6f35` | `55ec019884604dabe0efe8be15992c34257e6f35` | Drive sync bot | Exact lowercase old path is absent. Canonical `IJO-66-717-SEA.html` exists, and the sync also retained a superseded copy. | Expected Drive-owned deletion; replaced by newer canonical artifact. | None. |
| `drive-sync/Literature Review/Outputs/Clin Med Pharm/MD/IJO-66-717-references-task-queue.md` | `55ec019884604dabe0efe8be15992c34257e6f35` | `55ec019884604dabe0efe8be15992c34257e6f35` | Drive sync bot | Exact pluralized old path is absent. Canonical `IJO-66-717-reference-task-queue.md` exists, and the sync also retained a superseded copy. | Expected Drive-owned deletion; replaced by newer canonical artifact. | None. |

### 2026-08-27: `8cce889c3597a69006d0337269bcad419f931ca6`

These seven files were authored or added by non-sync commits minutes before the Drive sync. The sync therefore deleted repository-only work, not merely stale Drive-owned mirror content.

| Removed path | First appeared and pre-delete commit | Last substantive source | Current status | Classification | Required action |
| --- | --- | --- | --- | --- | --- |
| `drive-sync/Literature Review/Outputs/Clin Med Pharm/JSON/ada-ppc-2026-dc26-s011-coverage.json` | `9f00784db8915317dc9ba8eea8fc4713c86b819e`, 2026-08-27 04:59:05Z | Human, non-sync | Reintroduced by non-sync agent commit `29dc7f0109e71d37dba1b6c21fd0d99677a1d2b6` at 07:16:02Z with a different blob. Current Section 11 SEA-QA reports coverage reconciliation PASS. | GitHub-only file deleted by sync; later replaced by a newer valid version. | None. Do not restore the deleted older version. |
| `drive-sync/Literature Review/Outputs/Clin Med Pharm/JSON/ada-ppc-2026-dc26-s011-crosswalk.json` | `78b4af42ef39bcb084474f7b5c29416d66895dd1`, 2026-08-27 05:00:14Z | Human, non-sync | Reintroduced by non-sync agent commit `86f7f792235498c0ec1ad797899f4697f36b5c21` at 07:07:18Z with a different blob. Current SEA-QA reports all 19 recommendations mapped, atom IDs resolving, and no unresolved items. | GitHub-only file deleted by sync; later replaced by a newer valid version. | None. Do not restore the deleted older version. |
| `drive-sync/Literature Review/Outputs/Clin Med Pharm/JSON/ada-ppc-2026-dc26-s011-sea-qa.json` | `ce8c5069accd571b2e3a2a54bdfe72c57617e002`, 2026-08-27 04:59:29Z | Human, non-sync | Reintroduced and repaired by `86f7f792235498c0ec1ad797899f4697f36b5c21`. Current file reports `status: PASS`, `gate_pass: true`, and no failed checks. | GitHub-only file deleted by sync; later replaced by a newer valid version. | None. Do not restore the deleted older version. |
| `drive-sync/Literature Review/Outputs/Clin Med Pharm/JSON/ada-ppc-2026-dc26-s011-validation.json` | `6305fdeeb397528fb55954b9d93349a30d62f3b1`, 2026-08-27 04:59:20Z | Human, non-sync | Reintroduced and repaired by `86f7f792235498c0ec1ad797899f4697f36b5c21`. Current validation reports structural PASS, JSON Schema PASS, sufficiency PASS, source provenance PASS, and whole-source ATOM gate PASS. | GitHub-only file deleted by sync; later replaced by a newer valid version. | None. Do not restore the deleted older version. |
| `drive-sync/Literature Review/Outputs/Clin Med Pharm/JSON/ada-ppc-2026-dc26-s012-coverage.json` | `ba4c570e761616c018c8a8492a2f9e0e32dc16c0`, 2026-08-27 04:54:17Z | Human, non-sync | Restored by `2cdc8bd966705232a4d5a189d1c2be26cb9f58a0` at 05:17:54Z. The restored blob SHA is exactly `9e137b52566c49e91b5cb8e9898c07083c4e11f6`, the same blob deleted by `8cce889c`. | GitHub-only file deleted by sync; later restored unchanged. | None. |
| `drive-sync/Literature Review/Outputs/Clin Med Pharm/MD/ada-ppc-2026-dc26-s011-processing-report.md` | `e354d1d3a441e6d2e38e0bfbcee3b9d13fcada03`, 2026-08-27 05:01:09Z | Human, non-sync | Reintroduced and later finalized by `82478aa80dd1538198f183d35a3a81e8fa105e58` at 07:25:00Z. Current report records ATOM, coverage, crosswalk, SEA-QA, and lifecycle PASS, with final state `PROCESSED - COMPLETE`. | GitHub-only file deleted by sync; later replaced by a newer valid version. | None. Do not restore the deleted older version. |
| `drive-sync/Literature Review/Outputs/Clin Med Pharm/MD/ada-ppc-2026-dc26-s011-reference-task-queue.md` | `53c411c898b54d63bf82d322131efe065f6284ab`, 2026-08-27 05:03:54Z | Human, non-sync | Reintroduced by `29dc7f0109e71d37dba1b6c21fd0d99677a1d2b6` with a different blob. Current processing report reconciles 159/159 bibliography entries and confirms the complete Section 11 artifact family. | GitHub-only file deleted by sync; later replaced by a newer valid version. | None. Do not restore the deleted older version. |

## Unresolved loss

The unresolved loss is limited to the nine-file `pmc-acquire-web` tree deleted in `55ec019884604dabe0efe8be15992c34257e6f35`.

Source commit for recovery, if the application is still wanted:

`2be007fe944a2715b82b2d73e9b3ddfac2dcff3a`  
2026-08-25 02:31:11Z  
`Add standalone PMC acquisition web interface`

No files from this tree were restored in this audit.

## Containment status

Commit `b5f1a48eed6ea91510d628966e8a0870a08ae621` at 2026-08-27 10:46:19Z changed `.github/workflows/sync-google-drive.yml` from destructive `rclone sync` to non-deleting `rclone copy`. This prevents future Drive absence from deleting destination-only repository files under `drive-sync`.

The containment change does not prevent a Drive file from replacing a repository file at the same relative path. That remaining collision mode is separate from the deletion incidents audited here.

## Required follow-up

1. Decide whether `pmc-acquire-web` is still intended to exist. If yes, restore or rehome the nine-file tree from `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` in a separate task. If no, record an explicit retirement so the absence is no longer an unresolved loss.
2. Do not restore any of the seven ADA files deleted by `8cce889c3597a69006d0337269bcad419f931ca6`; their current versions are either byte-identical restorations or newer valid replacements.
3. Keep the non-deleting `rclone copy` containment in place. Consider a separate guard for same-path overwrite detection if repository-authored files will continue to coexist under `drive-sync`.

## Silent overwrite and reversion audit

### Scope and method

This second pass uses the same 2026-08-24 through 2026-08-27 window and examines only paths with Git status `modified`. Removed paths remain governed by the deletion inventory above. For each sync commit, the immediately preceding tree and intervening non-sync ancestry were compared against the sync's modified-path set. Analytical artifacts were then checked against available validation, QA, processing-report, provenance, source-identity, and source-reconciliation evidence. No ATOM, SEA, validation, coverage, crosswalk, queue, or processing report was regenerated.

Across the four sync commits there were 89 modified-file events: 19 on 2026-08-24, 3 on 2026-08-25, 62 on 2026-08-26, and 5 on 2026-08-27. No modified path had an intervening non-sync same-path edit immediately before the sync. No probable rollback or overwrite of GitHub-authored work was found, and no modified-path case remains uncertain for manual review.

This does not negate the deletion losses above. The `pmc-acquire-web` loss and the seven ADA losses were path-removal events, not silent same-path reversions.

| Sync commit | Modified paths | Intervening non-sync same-path changes | Result |
| --- | ---: | ---: | --- |
| `50e68fac10b71acedef64e4c8b2430dae805961d` | 19 | 0 | Drive-side lifecycle/reconciliation updates; no GitHub-authored same-path version was displaced. |
| `55ec019884604dabe0efe8be15992c34257e6f35` | 3 | 0 | Three recurring Drive-owned historical DOCX updates. The intervening `pmc-acquire-web` commit only added new paths. |
| `db9d93e1c8a24a3036d881c1e6dd1524385c2c61` | 62 | 0 | Broad Clinical packet reconciliation from the prior sync state; analytical changes are newer Drive content, not a rollback of an intervening repository edit. |
| `8cce889c3597a69006d0337269bcad419f931ca6` | 5 | 0 | Three Drive-owned historical DOCX updates plus two validated `nihms-1048629` reconciliation repairs. |

### 2026-08-24: `50e68fac10b71acedef64e4c8b2430dae805961d`

The parent is the prior Drive-sync commit `cd5976a1797261698c41e921ca2e900c2003c9c6`; no non-sync commit intervened. Therefore none of the 19 modified paths can represent a sync rollback of work committed between the two syncs.

Classification:

- **Normal Drive-owned update:** the three recurring historical/superseded acquisition-runtime DOCX files and `Clin Med Pharm/MD/dom12307-references.md`. No non-sync same-path edit was present in the relevant history.
- **Legitimate newer Drive content:** the Sinha/Gul and Sun/Zhou analytical families, plus the `dom12239`, `haring-merker-2013`, `lim-choi-2023`, and `shyangdan-uthman-2016` processing reports. The same sync added companion QA, validation, queue, or reconciliation evidence. Sinha/Gul validation was expanded substantially and explicitly records source reconciliation; Sun/Zhou validation changed to `status: PASS` with a newer generation timestamp. No quality evidence supports treating the prior blobs as superior.
- **Formatting/export-only change:** none classified solely on this basis.
- **Probable rollback or overwrite:** none.
- **Uncertain/manual review:** none.

Complete modified-path inventory, with paths shortened below `drive-sync/`:

- `Acquisition Runtime/scholar-acquire-chatgpt/90 - HISTORICAL DEVELOPMENT AND EVIDENCE/HISTORICAL - v0.4-development/v0.4.3 repair plan - HISTORICAL WORK LOG/Prompt 3 - HISTORICAL CORROBORATING REPORTS (non-authoritative)/CORROBORATING PROSE ONLY - V0.4.3 Prompt 3 Route Proof Report.docx`
- `Acquisition Runtime/scholar-acquire-chatgpt/90 - HISTORICAL DEVELOPMENT AND EVIDENCE/HISTORICAL - v0.4-development/v0.4.3 repair plan - HISTORICAL WORK LOG/SUPERSEDED - Prompt 4 clean ten-PMID regression and ATOM-SEA handoff/SUPERSEDED - V0.4.3 Prompt 4 Preflight Hard-Stop Report.docx`
- `Acquisition Runtime/scholar-acquire-chatgpt/90 - HISTORICAL DEVELOPMENT AND EVIDENCE/SUPERSEDED - V0.4.3 Prompt 3 Final Authority Reconciliation (pre direct Unpaywall proof).docx`
- `Literature Review/Outputs/Clin Med Pharm/JSON/sinha-gul-2024-cureus-69711-atoms.json`
- `Literature Review/Outputs/Clin Med Pharm/JSON/sinha-gul-2024-cureus-69711-coverage.json`
- `Literature Review/Outputs/Clin Med Pharm/JSON/sinha-gul-2024-cureus-69711-sea-qa.json`
- `Literature Review/Outputs/Clin Med Pharm/JSON/sinha-gul-2024-cureus-69711-validation.json`
- `Literature Review/Outputs/Clin Med Pharm/JSON/sun-zhou-2014-e004619-atoms.json`
- `Literature Review/Outputs/Clin Med Pharm/JSON/sun-zhou-2014-e004619-coverage.json`
- `Literature Review/Outputs/Clin Med Pharm/JSON/sun-zhou-2014-e004619-crosswalk.json`
- `Literature Review/Outputs/Clin Med Pharm/JSON/sun-zhou-2014-e004619-sea-qa.json`
- `Literature Review/Outputs/Clin Med Pharm/JSON/sun-zhou-2014-e004619-validation.json`
- `Literature Review/Outputs/Clin Med Pharm/MD/dom12239-processing-report.md`
- `Literature Review/Outputs/Clin Med Pharm/MD/dom12307-references.md`
- `Literature Review/Outputs/Clin Med Pharm/MD/haring-merker-2013-processing-report.md`
- `Literature Review/Outputs/Clin Med Pharm/MD/lim-choi-2023-s12933-023-01911-7-processing-report.md`
- `Literature Review/Outputs/Clin Med Pharm/MD/shyangdan-uthman-2016-processing-report.md`
- `Literature Review/Outputs/Clin Med Pharm/MD/sinha-gul-2024-cureus-69711-processing-report.md`
- `Literature Review/Outputs/Clin Med Pharm/MD/sun-zhou-2014-e004619-processing-report.md`

### 2026-08-25: `55ec019884604dabe0efe8be15992c34257e6f35`

The immediate parent `2be007fe944a2715b82b2d73e9b3ddfac2dcff3a` is a non-sync commit, but its complete diff only adds the nine-file `pmc-acquire-web` tree. It does not modify any pre-existing path. Those nine added paths were deleted by the sync and are already recorded above; they are not same-path overwrite cases.

The sync's only three modified paths are the recurring historical/superseded acquisition-runtime DOCX files listed in the 2026-08-24 inventory. All three are classified as **normal Drive-owned updates**. There is no evidence of an intervening GitHub-authored version, substantive loss, or rollback on those paths.

### 2026-08-26: `db9d93e1c8a24a3036d881c1e6dd1524385c2c61`

The immediate parent is the 2026-08-25 Drive-sync commit itself. No non-sync commit intervened. The commit contains a broad Clinical packet reconciliation: 3 recurring historical DOCX modifications and 59 Clinical artifact modifications.

Classification:

- **Normal Drive-owned update:** the three recurring historical/superseded acquisition-runtime DOCX files.
- **Legitimate newer Drive content:** all 59 modified Clinical artifacts. This classification is based on the direct-sync ancestry and the accompanying packet evidence, not on recency alone. The same commit adds missing coverage, validation, SEA-validation/QA, processing-report, and reference-reconciliation artifacts across the affected packets. Representative source-integrity patches include `33-S0735109721058460_SEA.html`, which corrects mislabeled supplemental Table 2/3/6/7 rows against the supplied supplement; `06-0725-atom-validation.json`, which adds explicit render QA; and the IJO family, where the canonical uppercase SEA is expanded while obsolete naming is moved to superseded status. These are reconciliation/repair signals, not evidence of a Drive rollback.
- **Formatting/export-only change:** formatting normalization occurs inside several SEA diffs, but those same files also contain provenance, source-integrity, or QA changes, so no file is classified solely as formatting/export-only.
- **Probable rollback or overwrite:** none.
- **Uncertain/manual review:** none.

Complete modified Clinical path inventory, grouped under `drive-sync/Literature Review/Outputs/Clin Med Pharm/`:

**HTML (8)**

- `HTML/18-041-sea.html`
- `HTML/30-RomJOphthalmol-59-188-sea.html`
- `HTML/33-S0735109721058460_SEA.html`
- `HTML/37-S1556086421032172-SEA.html`
- `HTML/45-S1470204520304447-SEA.html`
- `HTML/IJO-66-717-SEA.html`
- `HTML/S1201971213001100_sea.html`
- `HTML/bcr-2020-239394-sea.html`

**JSON (44)**

- `JSON/04-0893-atoms.json`
- `JSON/06-0725-atom-validation.json`
- `JSON/06-0725-atoms.json`
- `JSON/11-S1567134821004251-atoms.json`
- `JSON/117-nihms-1753340-atoms.json`
- `JSON/117-nihms-1753340-validation.json`
- `JSON/18-041-atoms.json`
- `JSON/18-041-coverage.json`
- `JSON/2029-07-atoms.json`
- `JSON/2029-07-sea-qa.json`
- `JSON/2029-07-validation.json`
- `JSON/2457-06-atoms.json`
- `JSON/25-main1-atoms.json`
- `JSON/26-recurrent-guillain-barre-syndrome-case-series-atoms.json`
- `JSON/26-recurrent-guillain-barre-syndrome-case-series-coverage.json`
- `JSON/30-RomJOphthalmol-59-188-atoms.json`
- `JSON/30-RomJOphthalmol-59-188-coverage.json`
- `JSON/30-RomJOphthalmol-59-188-validation.json`
- `JSON/37-S1556086421032172-atoms.json`
- `JSON/40-wharton-2021-semaglutide-gi-tolerability-atoms.json`
- `JSON/40-wharton-2021-semaglutide-gi-tolerability-validation.json`
- `JSON/44-S1936879820320124-EXTRACT-PE-atoms.json`
- `JSON/45-S1470204520304447-atoms.json`
- `JSON/794-neonatal-mrsa-conjunctivitis-atoms.json`
- `JSON/794-neonatal-mrsa-conjunctivitis-coverage.json`
- `JSON/794-neonatal-mrsa-conjunctivitis-validation.json`
- `JSON/IJO-66-717-atoms.json`
- `JSON/IJO-66-717-validation.json`
- `JSON/S1876034114000793-atoms.json`
- `JSON/S1876034114000793-coverage.json`
- `JSON/bcr-2020-239394-atoms.json`
- `JSON/bcr-2020-239394-coverage.json`
- `JSON/bcr-2020-239394-sea-qa.json`
- `JSON/biomolecules-11-01624-atoms.json`
- `JSON/biomolecules-11-01624-validation.json`
- `JSON/dkx358-atoms.json`
- `JSON/jco-39-3441-atoms.json`
- `JSON/jco-39-3441-validation.json`
- `JSON/nihms-1829921-atoms.json`
- `JSON/nihms-1829921-validation.json`
- `JSON/nihms-2063155-atoms.json`
- `JSON/usaa232-atoms.json`
- `JSON/usaa232-coverage.json`
- `JSON/usaa232-validation.json`

**MD (7)**

- `MD/117-nihms-1753340-references.md`
- `MD/18-041-reference-task-queue.md`
- `MD/2029-07-reference-task-queue.md`
- `MD/30-RomJOphthalmol-59-188-reference-task-queue.md`
- `MD/IJO-66-717-reference-task-queue.md`
- `MD/bcr-2020-239394-reference-task-queue.md`
- `MD/jco-39-3441-reference-task-queue.md`

### 2026-08-27: `8cce889c3597a69006d0337269bcad419f931ca6`

Thirteen non-sync commits occurred after the 2026-08-26 sync and before the 2026-08-27 sync parent `a5c77b461746f3e747e344c64066ff34a1b374e9`. A complete compare of that interval shows workflow/trigger changes and seven newly added ADA artifacts, but none of the five paths later marked `modified` by the sync. The seven ADA overlaps were deletions and remain documented in the deletion inventory.

The five modified paths are:

- the same three recurring historical/superseded acquisition-runtime DOCX files — **normal Drive-owned update**;
- `Literature Review/Outputs/Clin Med Pharm/HTML/21 - nihms-1048629 - SEA.html` — **legitimate newer Drive content**;
- `Literature Review/Outputs/Clin Med Pharm/JSON/21 - nihms-1048629 - ATOM.json` — **legitimate newer Drive content**.

The `nihms-1048629` changes are not merely newer timestamps. The companion `21 - nihms-1048629 - ATOM Validation.json` at the sync commit reports structural validation PASS, JSON Schema PASS, sufficiency PASS, source-anchor verification `PASS_AFTER_MINIMAL_REPAIR`, SEA reconciliation `PASS_AFTER_RECONCILIATION`, and lifecycle `PASS - ATOM/SEA VERIFIED`. The ATOM change narrows one source anchor from page `3` to `2-3` without changing the canonical statement, assertion origin, quantitative estimate, or atom kind. The SEA records the source's own 4.5-month versus Table 1 median inconsistency rather than silently normalizing it. This is a source-integrity repair, not a rollback.

### Overwrite-audit conclusion

No same-path sync overwrite/reversion loss was identified in the established audit window. Specifically:

- no sync-modified path had a non-sync same-path edit immediately before the sync;
- no analytical artifact reviewed showed validation, QA, provenance, or source-identity evidence that the post-sync version was a rollback to an inferior Drive version;
- no modified path is classified as probable rollback/overwrite;
- no modified path remains uncertain for manual review.

The reconciliation record therefore contains both loss modes: confirmed deletion losses are preserved in the deletion inventory, while the same-path overwrite audit is negative for this window. The non-deleting `rclone copy` containment fixes deletion-by-absence but still does not technically prevent a future same-path collision; a separate collision detector or ownership boundary remains advisable if GitHub-authored work continues under `drive-sync`.
