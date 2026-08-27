# 21 - nihms-1048629 - Processing Report

**Lifecycle status:** `PASS - ATOM/SEA VERIFIED`  
**Validated:** 2026-08-26T09:43:45Z  
**Primary source:** `nihms-1048629.pdf`  
**Source SHA-256:** `353de89de63571fe8e02b481ccd95d139ebaf41bb8e04edef9978e32be812c6a`

## Gate results

| Gate | Result | Evidence |
|---|---|---|
| Primary source identity/integrity | **PASS** | Title/DOI match the ATOM/SEA artifacts; source SHA-256 matches extraction provenance. |
| ATOM structural validation | **PASS** | 37/37 atoms validate against the current `LiteratureAtom` Pydantic model; 0 structural errors. |
| ATOM JSON Schema validation | **PASS** | 37/37 atoms validate against `literature_atom.schema.json`; 0 schema errors. |
| ATOM sufficiency validation | **PASS** | 37/37 atoms pass atom-kind sufficiency rules; 0 errors and 0 warnings. |
| Atom identity/duplicate checks | **PASS** | 37 unique atom IDs, one publication ID, no exact normalized duplicate statements. |
| Source anchors | **PASS AFTER MINIMAL REPAIR** | Case 1 anchor page changed from `3` to `2-3` because the case begins on PDF page 2 and continues on page 3. No claim meaning changed. |
| SEA coverage/reconciliation | **PASS AFTER RECONCILIATION** | All substantive sections represented; figures 0/0; tables 2/2; workflows 0/0. SEA updated to flag the source's abstract/Table 1 median discrepancy. |
| Reference processing | **NON-BLOCKING** | Existing reference task queue remains, but reference processing is not a blocking gate under the 2026-08-26 human-review override. |

## Source-level warning

The abstract reports a median time to resolution of **4.5 months** (range 2-5 months). Table 1 lists time-to-euthyroidism values of **3, 5, 4, 3, 2, 5, 5, 5, and 5 months**, whose median is **5 months**. This is an internal source inconsistency. The directly reported 4.5-month value was preserved in the ATOM artifact; it was not silently replaced. The reconciled SEA now flags the discrepancy explicitly.

## Repairs performed

- Updated the Case 1 atom's `source_anchor.page` from `3` to `2-3`.
- Added current validation/reconciliation metadata to the ATOM wrapper validation report.
- Reconciled the SEA by adding the source-level numerical inconsistency warning and updating its QA provenance block.
- Created a standalone ATOM validation record for future gate audits.

## Final disposition

`PASS - ATOM/SEA VERIFIED`

No unresolved structural, schema, sufficiency, source-identity, or SEA-coverage blocker remains. The source-level median discrepancy is documented as a non-blocking warning. Reference processing remains separate follow-up work and does not prevent lifecycle promotion under the current override.
