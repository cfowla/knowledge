# Zelniker et al. 2021 publication packet processing report

## Lifecycle result

**PASS — promoted to Processed**

Packet: `151 - Zelniker Raz 2021`

## Exact publication identity

Thomas A. Zelniker, Itamar Raz, Ofri Mosenzon, et al. **Effect of Dapagliflozin on Cardiovascular Outcomes According to Baseline Kidney Function and Albuminuria Status in Patients With Type 2 Diabetes: A Prespecified Secondary Analysis of a Randomized Clinical Trial.** *JAMA Cardiology*. 2021;6(7):801–810. Published online April 14, 2021. DOI `10.1001/jamacardio.2021.0660`. ClinicalTrials.gov `NCT01730534`.

Publication UUID used across all atoms: `a29823fb-ac5f-5f60-8b1b-7c0d6b18f0b2`.

## Source inventory

- Primary: `jamacardiology_zelniker_2021_oi_210015_1625699332.29883.pdf` — readable, 10 pages.
- Supplement 1: `hoi210015supp1_prod_1625699332.30383.pdf` — 189 pages; includes Revised Clinical Study Protocol D1693C00001 Edition 5.0 (25 Sep 2016), appendices, and Statistical Analysis Plan Edition 8 (31 May 2018).
- Supplement 2: `hoi210015supp2_prod_1625699332.31383.pdf` — 9 pages; 2 eTables and 5 eFigures.
- Additional acquisition artifacts: none identified in the bounded prewalk.
- Source/identity blocker: none.

## Bounded discovery disposition

The single identity-based discovery pass across the Clinical output root and repository found no identity-matched ATOM, validation, SEA, SEA-QA, crosswalk, reference, coverage, or processing-report artifacts. Discovery was then closed. No prior analytical artifact was available to preserve or repair; all required analytical outputs were produced forward from the original source packet.

## Artifacts generated

JSON:
- `zelniker-2021-atoms.json`
- `zelniker-2021-atom-validation.json`
- `zelniker-2021-coverage.json`
- `zelniker-2021-claim-atom-crosswalk.json`
- `zelniker-2021-reference-reconciliation.json`
- `zelniker-2021-sea-qa.json`
- `zelniker-2021-parent-publication-gate.json`

MD:
- `zelniker-2021-references.md`
- `zelniker-2021-sea-qa.md`
- `zelniker-2021-processing-report.md`

HTML:
- `zelniker-2021-sea.html`

## ATOM validation

- Atom count: **83**
- Shared publication_id: **one** (`a29823fb-ac5f-5f60-8b1b-7c0d6b18f0b2`)
- Pydantic structural errors: **0**
- JSON-Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Duplicate/publication-ID consistency findings: **0**
- ATOM result: **PASS**

## SEA / coverage / SEA-QA

- Main-text tables reconciled: **2/2**
- Main-text figures reconciled: **2/2**
- Main-text workflows: **0**
- Supplement 2 eTables reconciled: **2/2**
- Supplement 2 eFigures reconciled: **5/5**
- Supplement 1 protocol/SAP: analysis-relevant design, population, endpoint, randomization, analysis-set, subgroup, and change-log material reconciled.
- SEA is self-contained HTML with claims separated from appraisal and final scoring performed after extraction/reconciliation.
- SEA-QA result: **PASS**

## Reference reconciliation

- Main article bibliography: **34** references
- Supplement 1 protocol bibliography: **16** references
- Supplement 1 Appendix I bibliography: **24** references
- Supplement 1 SAP bibliography: **12** references
- Raw bibliography entries: **86**
- Unique references after reconciliation: **85**
- Duplicates reconciled: **1** (Levey et al. 2009 appears in both protocol and SAP)
- Reference reconciliation: **PASS**

Cited-publication acquisition or independent processing is downstream work and is not a prerequisite for this parent publication gate.

## Parent publication gate

1. Source integrity — **PASS**
2. Exact publication identity/provenance — **PASS**
3. ATOM Pydantic/JSON-Schema/sufficiency validation — **PASS**
4. Merged ATOM reconciliation — **PASS**
5. SEA / visual / supplement reconciliation — **PASS**
6. Claim↔atom crosswalk — **PASS**
7. SEA-QA — **PASS**
8. Complete bibliography extraction/reconciliation — **PASS**
9. Parent output completeness — **PASS** after this report is staged with the output family

**Parent publication-gate verdict: PASS.**

No genuine unresolved source, evidence, or packet-level blocker remains. The packet does not belong in Needs Resolution.

## Lifecycle action

Canonical output staging succeeded. The packet was moved from `2 - 10 - Active Literature / 1 - Clinical Medicine & Pharmacy` to `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`.

Final Drive folder: `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy / 151 - Zelniker Raz 2021`

Folder ID: `10I0t7zm7mNFh9d7KsRWisex3r8EU7vwF`.

Generated: 2026-08-28
