# 14 - S1201971213001100 Publication Packet Repair Report

**Lifecycle status:** `PASS`  

**OVERRIDEN BY CONNOR FOWLER ON 2026-08-26T07:37:31Z**

**HUMAN REVIEW HAS YIELDED SUFFICIENT EVIDENCE TO PASS THIS PACKET**

**Audit date:** 2026-08-25  
**Packet:** `2 - 10 - Active Literature / 1 - Clinical Medicine & Pharmacy / 14 - S1201971213001100`

## Source identity and integrity

- Primary source: `1-s2.0-S1201971213001100.pdf`
- Exact title: *In vivo acquired daptomycin resistance during treatment of methicillin-resistant Staphylococcus aureus endocarditis*
- Authors: Laurent Dortet; Nadia Anguel; Nicolas Fortineau; Christian Richard; Patrice Nordmann
- Journal: *International Journal of Infectious Diseases* 17(11):e1076-e1077 (2013)
- DOI: `10.1016/j.ijid.2013.02.019`
- PMID: `23578850` — external identity verification from PubMed metadata.
- Primary-source SHA-256: `e3a96ee7d3b65196812728ea82f14b21f594832850b034c33b9c74dfc65c5cfa`
- Source usability: PASS. The two-page PDF opens, is text-extractable, and both pages were visually inspected.
- Supplements: none present in the packet.
- Main-text figures: 1. Tables: 0. Algorithms/workflows: 0.
- Source-integrity warning: the case-report narrative states the initial daptomycin MIC was `0.25 mg/L`, while Figure 1 displays `0.125 mg/L` for isolate S1. The supplied source does not reconcile the discrepancy. The repair preserves both values by locator rather than normalizing them.

## Verification boundary

- Project/source-derived findings: primary PDF identity, case details, Figure 1 values, ATOM extraction, SEA content, and lifecycle state.
- External verification used only for publication identity: PubMed confirmed PMID `23578850` and the same title/DOI. No external clinical facts were used to repair the case findings.

## Artifact audit and repairs

### ATOM

No identity-matched ATOM JSON, authoritative validation JSON, or coverage JSON was found in the Clinical Medicine & Pharmacy JSON output folder before repair. These were regenerated from the current source.

- ATOM JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON / S1201971213001100-atoms.json`
  - Drive file ID: `1B9Oq-HSDvQ813CQaPX75A_xEt5UirbOz`
- ATOM validation JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON / S1201971213001100-validation.json`
  - Drive file ID: `1DhYg1dsy1sLBj-hKf_q7ZAXluE7eZEom`
- Coverage JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON / S1201971213001100-coverage.json`
  - Drive file ID: `13_Ut9lp6Ln7bCbXFI2uUqaO-pd_bG8Nv`

ATOM result:

- 35 independently reviewable atoms under one publication identity.
- Pydantic structural validation using authoritative `literature.py`: 0 errors.
- JSON Schema validation using authoritative `literature_atom.schema.json`: 0 errors.
- Atom-kind sufficiency validation using authoritative `literature_atoms.py`: 0 errors, 0 sufficiency warnings.
- Atom IDs are unique; publication identity is shared across all atoms.
- Every atom has a source locator and source excerpt; provenance carries the current primary-source SHA-256.
- The narrative `0.25 mg/L` and Figure 1 `0.125 mg/L` initial daptomycin MIC values are represented as separate directly reported atoms and flagged as an unresolved source-internal discrepancy.
- Direct semantic spot-checks passed for the primary conclusion, serial daptomycin MICs, day-68 treatment switch and subsequent negative cultures, candidate-gene result, and Figure 1 values.
- Background claims from cited literature were not promoted into primary-case atoms.

### SEA

An identity-matched SEA HTML already existed, but its Figure 1 reconstruction incorrectly used the narrative baseline daptomycin MIC (`0.25 mg/L`) as the Figure 1 S1 value. The HTML was repaired in place so the structured Figure 1 reconstruction now shows `0.125 mg/L` and explicitly records the narrative-versus-figure discrepancy.

- SEA HTML: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML / S1201971213001100_sea.html`
  - Drive file ID: `1KELko5ESyQYqBp-swteqm7no7DlZ8Ana`
- SEA QA JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON / S1201971213001100-sea-qa.json`
  - Drive file ID: `1_ED58L-0C4b83S334C5pJex1ZT8MQ5Pi`

SEA result:

- HTML parseability: PASS.
- Source title/DOI/source hash: PASS.
- Methods/design coverage: PASS for a case report, including E-test/broth-dilution susceptibility methods and candidate-gene comparison.
- Main claims and quantitative findings: PASS, including persistent bacteremia, daptomycin MIC evolution, rifampin MIC `>32 mg/L`, TEE vegetation measurements, and reported vancomycin concentrations `25-35 mg/L`.
- Limitations/uncertainty: PASS; n=1 design, no comparative causal inference, inability to attribute clearance to a single component of the three-drug switch, and unresolved molecular resistance mechanism are explicit.
- Figure/table/workflow reconciliation: PASS; Figure 1 is represented structurally after direct visual inspection; no tables or algorithms/workflows are present.
- Source-integrity warning: PASS as documented warning, not silently repaired in the source. The SEA distinguishes narrative baseline daptomycin MIC `0.25 mg/L` from Figure 1 S1 `0.125 mg/L`.
- Internal chat/file citation syntax, TODOs, placeholders, broken TOC anchors, external scripts/stylesheets, and remote images: none found.

## ATOM-SEA reconciliation

ATOM and SEA are grounded to the same PDF version and SHA-256. The primary clinical sequence, serial susceptibility findings, treatment timeline, negative cultures after the day-68 regimen change, candidate-gene result, and unresolved mechanism are consistent across both artifacts. The only consequential source-level inconsistency identified is the baseline daptomycin MIC discrepancy; both ATOM and SEA now preserve the same locator-specific distinction. No cross-artifact contradiction remains after repair.

## Reference-processing gate

The packet has an identity-matched five-reference Markdown queue:

- `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD / S1201971213001100_reference_task_queue.md`
  - Drive file ID: `1UvClHm5LhrqO0R-jPlPugVEeKusjsY8w`

All five reference tasks remain unchecked. Targeted Drive searches for the five cited works did not identify a packet-level completion record proving that each reference has been routed/acquired/resolved in the live literature lifecycle. Some titles occur only inside the queue itself or as citations in unrelated guideline material; those occurrences are not proof of completed reference processing.

**Reference-processing gate: FAIL / incomplete.**

## Lifecycle action

- Assigned status: `PARTIAL - REPAIR REQUIRED`.
- Packet remains in `2 - 10 - Active Literature / 1 - Clinical Medicine & Pharmacy`.
- The packet was **not** moved to `90 - Processed` because the reference-processing completion gate is not satisfied.
- No Needs Resolution move is warranted because the primary source is complete and usable.

## Exact remaining task

Reconcile all five entries in `S1201971213001100_reference_task_queue.md` against the live TBR/Active/Processed/Citation Bank lifecycle, complete the required routing/acquisition actions, and record a definitive disposition for every entry. Once all five references are demonstrably complete or defensibly resolved, rerun the packet completion gate. ATOM and SEA do not currently require further repair.
