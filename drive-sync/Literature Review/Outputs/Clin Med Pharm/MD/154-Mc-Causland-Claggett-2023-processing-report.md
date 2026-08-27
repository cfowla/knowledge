# Processing report: Dapagliflozin and Kidney Outcomes in Patients With Heart Failure With Mildly Reduced or Preserved Ejection Fraction: A Prespecified Analysis of the DELIVER Randomized Clinical Trial

## Packet identity

- Packet: `154 - Mc Causland Claggett 2023`
- Drive folder ID: `1888CHHo6P7s8i6sopr6k3_Ed4hGzulRE`
- Primary source: `jamacardiology_mc_causland_2022_oi_220070_1672335570.90403.pdf`
- DOI: `10.1001/jamacardio.2022.4210`
- PMID: `36326604`; PMCID: `PMC9634592`; trial: `NCT03619213`
- Primary SHA-256: `2aa4f1a1279871176a765b1c5de6bbc57884d5d4b6bb74d1dc38aa7649952c9b`
- Supplement 1 SHA-256: `8c02977125db15fab381864a710bf3fe22e37f2ea708a105e614aaacfc026e01`
- Supplement 2 SHA-256: `fb6bea94f71facc664cd80c59757442051bb09d7690b2002239ea4274999b3b9`

## Prewalk and first unsatisfied gate

Fresh Drive inventory found one primary article plus two source supplements. Repository searches by packet name, source filename, DOI, title/article number, and normalized author form found no identity-matched completion family. Source integrity passed for the evidence-bearing publication package. The first unsatisfied parent-publication requirement was therefore **ATOM: required identity-matched ATOM evidence was absent**. No neighboring packet artifact was used as completion evidence.

The article cites a separate `Supplement 3` Data Sharing Statement that is not present in the packet. This discrepancy is preserved. Because it is a data-sharing/provenance attachment and not needed to interpret the trial methods, reported efficacy/safety results, figures, tables, or statistical analyses, it is nonblocking for this parent-publication gate.

## ATOM and validation

- LiteratureAtoms: **57**
- Shared publication ID: `8621d8d7-1bcf-5e3d-b859-db4738bfee65`
- Counts by kind: `{"adverse_event": 6, "author_conclusion": 2, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 2, "funding_disclosure": 1, "intervention_description": 1, "limitation": 4, "method": 8, "outcome_definition": 3, "population_description": 3, "qualitative_result": 2, "quantitative_result": 13, "study_objective": 1, "subgroup_result": 8}`
- Pydantic structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**; warnings: **0**
- Duplicate statement-anchor pairs: **0**
- Model-extracted atoms remain `extracted`; no human verification was fabricated.

## SEA, coverage, reconciliation, and crosswalk

- Main article pages inspected: **10/10** by render/text reconciliation.
- Main figures: **2/2 reconciled**.
- Main tables: **3/3 reconciled**.
- Supplement 1: final protocol v4.0, final sponsor SAP v5.0, academic SAP v1.3, and analysis-relevant methods reconciled; superseded/non-load-bearing administrative content was not atomized.
- Supplement 2: **5/5 eTables** and **3/3 eFigures** reconciled.
- SEA-QA: **PASS**.
- Crosswalk referential integrity: **PASS**; every referenced atom ID resolves to the shared publication ID.

## Bibliography

- Primary-article bibliography entries: **34/34 extracted and reconciled**.
- Reference 16 and reference 18 are duplicate source citations to the same DELIVER primary trial publication; both source positions are preserved.
- Unchecked cited references remain downstream work and do **not** block parent publication lifecycle under the current Clinical packet failure-gate rule.

## Output family

The exact identity-matched family is present under `drive-sync/Literature Review/Outputs/Clin Med Pharm/`:

- `JSON/154-Mc-Causland-Claggett-2023-atoms.json`
- `JSON/154-Mc-Causland-Claggett-2023-validation.json`
- `JSON/154-Mc-Causland-Claggett-2023-coverage.json`
- `JSON/154-Mc-Causland-Claggett-2023-crosswalk.json`
- `JSON/154-Mc-Causland-Claggett-2023-sea-qa.json`
- `HTML/154-Mc-Causland-Claggett-2023-sea.html`
- `MD/154-Mc-Causland-Claggett-2023-reference-task-queue.md`
- `MD/154-Mc-Causland-Claggett-2023-processing-report.md`

Canonical publication commit: `8772943a17b01f25d833a9c256eb80ba72576fa7` (`Publish Mc Causland Claggett 2023 packet artifacts`). The publication workflow verified the bundle before write, then the canonical validation, coverage, crosswalk, and SEA-QA artifacts were read back from the repository.

## Publication-gate verification

- Source integrity and identity: **PASS**.
- ATOM structural/schema/sufficiency validation: **PASS**.
- SEA/SEA-QA: **PASS**.
- Coverage/reconciliation: **PASS**.
- Crosswalk referential integrity: **PASS**.
- Bibliography extraction/reconciliation: **PASS (34/34)**.
- Output completeness/provenance: **PASS** — exact eight-file identity-matched output family verified in `cfowla/knowledge`; source hashes, DOI, publication ID, and artifact relationships are consistent.
- Unresolved packet-level requirements: **NONE**.

## Lifecycle state

- Classification before repair: `NO COMPLETION EVIDENCE`.
- Evidence audit classification: `FAIL, repair required` — first unsatisfied requirement was the absent ATOM gate.
- Smallest repair: because no identity-matched upstream artifact family existed, the missing ATOM -> validation -> SEA -> coverage/reconciliation -> crosswalk -> SEA-QA -> reference queue -> processing report family was created from the exact source packet.
- Promotion gate: **PASS**.
- Source packet moved intact from Active Clinical parent `1wA_mmV9fJvfM7ILPwPuc-Uac1SJ1hpk0` to the current Processed Clinical parent `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`.
- Exact packet absent as a direct child of Active after move: **PASS**.
- Exact packet present as a direct child of Processed Clinical Medicine & Pharmacy after move: **PASS**.
- Downstream cited-publication follow-up remains separately trackable and nonblocking.
- Final lifecycle state: **PROCESSED**.
