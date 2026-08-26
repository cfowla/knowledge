# 53 - toxins-13-00215 — Processing Report

**Status:** PASS - ATOM/SEA VERIFIED

## Source audit
- Primary source: `toxins-13-00215.pdf`
- DOI: `10.3390/toxins13030215`
- Pages: 9
- SHA-256: `4eabeb0d46a15e70a741c822f878f2d5b9729f69a0da8c4ab19c6cb91704c0c0`
- Supplements/attachments: none
- Usability: PASS; all 9 pages rendered and all 5 main-text figures inspected.

## ATOM validation
- Atoms: 38
- Structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Authoritative validator order: literature.py → literature_atom.schema.json → literature_atoms.py
- Result: PASS

## SEA validation
- Parseable/self-contained HTML: PASS
- Figures reconciled: 5/5
- Tables: 0
- Supplements: 0
- Source metadata, methods/design, quantitative findings, limitations/uncertainty, provenance: PASS
- Direct semantic spot checks: PASS

## Reference processing
- Source bibliography entries: 17
- Queue entries reconciled: 17/17
- Duplicate/missing numbers: 0/0
- Every entry has an assigned downstream action.
- Packet-level reference reconciliation: COMPLETE. Unchecked queue boxes are downstream tasks, not an incomplete packet reconciliation.

## Reconciliation
ATOM and SEA use the same source/version and agree on the design, population, regimen, main longitudinal QoL signal, CES-D result, and the distinction between observed clinical resistance and the untested neutralizing-antibody hypothesis. The source's likely 45-month HFS-30/AIMS label inconsistency is explicitly preserved in both workflows rather than silently corrected.

## Warnings
- The PDF text layer contains duplicated/overlaid peer-review text on several middle pages; rendered final pages are visually coherent.
- No comparator arm, visit-specific denominator/attrition series, dedicated adverse-event incidence, or neutralizing-antibody testing is reported.

## Lifecycle
Moved to `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy` and verified. The folder name was preserved and the packet no longer appears under the Active Clinical Medicine & Pharmacy parent. Exact remaining task: none.
