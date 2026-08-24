# Processing Report — Solomon McMurray 2022

## Source packet
- Main article: `NEJMoa2206286.pdf` — DOI 10.1056/NEJMoa2206286; PMID 36027570.
- Supplementary appendix: `nejmoa2206286_appendix.pdf`.
- Protocol/SAP bundle: `nejmoa2206286_protocol.pdf`.
- Related correspondence: `NEJMc2213974.pdf` — DOI 10.1056/NEJMc2213974.

## ATOM
- Main publication: **127 LiteratureAtoms**; one publication identity.
- Correspondence: **13 LiteratureAtoms**; separate publication identity.
- Main Pydantic structural errors: 0; JSON Schema errors: 0; sufficiency errors: 0; warnings: 0.
- Correspondence Pydantic structural errors: 0; JSON Schema errors: 0; sufficiency errors: 0; warnings: 0.
- Exact duplicate statement-anchor pairs: main 0; correspondence 0.

## SEA
- Main SEA verdict: **Read first**.
- Correspondence SEA verdict: **Skim deeply**.
- Main visual/table coverage: 2 main figures + 2 main tables; 2 supplement figures + Tables S1-S8 (including S7.1-S7.3); protocol/SAP version and analysis workflows selectively reconciled.
- Main SEA QA: **PASS**.
- Correspondence SEA QA: **PASS**.

## Reference task queue
- **29 unique tasks**: 15 main bibliography + 3 supplement-only + 11 correspondence-only citations after deduplication.
- The two unrelated carryover citations that precede the DELIVER correspondence heading on journal page 286 were excluded.

## Source-integrity / interpretation notes
- The primary Cox proportional-hazards assumption was reported as violated (P=0.006); robust analyses remained directionally consistent.
- The dual-primary analysis and primary KCCQ analysis were amended in November 2020 and are surfaced explicitly.
- Subgroup analyses were underpowered; subgroup atoms preserve reported estimates without treating them as independently powered conclusions.
- The correspondence prints a DAPA-HF+DELIVER cardiovascular-death HR 0.86 with 95% CI 0.76–0.86; the extracted atom preserves the printed value and flags it rather than silently correcting it.

Generated: 2026-08-23.
