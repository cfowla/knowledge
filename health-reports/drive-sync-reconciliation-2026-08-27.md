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
