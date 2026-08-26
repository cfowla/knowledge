# 36 - S0140673621012551 Publication Packet Repair Report

**Lifecycle status:** `PASS`  

**OVERRIDEN BY CONNOR FOWLER ON 2026-08-26T07:37:31Z**

**HUMAN REVIEW HAS YIELDED SUFFICIENT EVIDENCE TO PASS THIS PACKET**

**Audit date:** 2026-08-25  
**Packet:** `2 - 10 - Active Literature / 1 - Clinical Medicine & Pharmacy / 36 - S0140673621012551`

## Source identity and integrity

- Primary source: `1-s2.0-S0140673621012551-main.pdf`
  - Drive file ID: `1g37vj4y0nOpT7jxd2vxOZxOXSlw1sRRU`
  - Exact title: *Tofacitinib in juvenile idiopathic arthritis: a double-blind, placebo-controlled, withdrawal phase 3 randomised trial*
  - Authors: Nicolino Ruperto; Hermine I Brunner; Olga Synoverska; Tracey Ting; Gevorg Mendoza Mallon; Tadashi Urata; Claudia Martini; Luann McGuire; Jaime Hsu; Iain B McInnes; Daniel J Lovell; PRINTO and PRCSG investigators
  - Journal: *The Lancet* 398:1984-1996 (2021)
  - DOI: `10.1016/S0140-6736(21)01255-1`
  - PMID: `34767764`
  - ClinicalTrials.gov: `NCT02592434`
  - SHA-256: `a9722c52eb933420a04baaeb7c6cb2191d359038510a0172d892c74ed7771fb8`
  - Usability: PASS. The 13-page PDF opens, is text-extractable, and all pages were visually inspected.
- Material supplement: `1-s2.0-S0140673621012551-mmc1.pdf`
  - Drive file ID: `1iVKvpfKyjNhaW05GPMwem0cBt5SwKfp5`
  - 240-page supplementary appendix containing supplemental efficacy/safety figures and tables plus the protocol and statistical analysis plan.
  - SHA-256: `b509f43d18f795e93427856ec97f1a0ff6b772ad83a89139ea64b09f764d1eea`
  - Usability: PASS. Text was extracted; all evidence-bearing supplemental figure/table pages were visually inspected and the protocol/SAP were inspected textually.
- Main-text visual inventory: Figure 1 (trial profile), Figure 2 (flare efficacy/time to flare), Figure 3 (JADAS), Tables 1-3.
- Material supplement inventory: Figures S1-S11, Tables S2-S3, protocol, and SAP. Table S1 is the CONSORT checklist and is recorded as non-load-bearing for evidence synthesis.

## Verification boundary

- Project/source-derived findings: publication identity from the supplied article, study design, participant flow, efficacy and safety findings, limitations, visual/table content, supplement content, ATOM extraction, SEA synthesis, and lifecycle status.
- External identity verification: PubMed metadata was used only to confirm PMID `34767764` against the same title/DOI.
- No external clinical facts were substituted for the supplied article or appendix.

## Prior artifact audit

Identity matching was performed using title, DOI, stable identifier, study metadata, and content rather than filename similarity.

Before repair, no identity-matched ATOM JSON, authoritative ATOM validation JSON, coverage JSON, SEA HTML, SEA QA JSON, reference-processing Markdown queue, or processing report for this publication was found in the Clinical Medicine & Pharmacy output folders under `GitHub Sync / Literature Review / Outputs / Clin Med Pharm`.

The packet itself contained only the primary article and its supplementary appendix.

## ATOM repair and validation

The ATOM set was regenerated from the current primary article and material appendix using one shared publication identity.

- ATOM JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON / S0140673621012551-atoms.json`
  - Drive file ID: `1ZRMdYejUBCKbRUUwUabWdh2FJidCiniB`
- ATOM validation JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON / S0140673621012551-validation.json`
  - Drive file ID: `1kxY_mkzahzFG5v2_WGkIZiTbFEBp58dA`
- Coverage JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON / S0140673621012551-coverage.json`
  - Drive file ID: `1F5JZpefKMZW4IdebD_SZoTRn_2qHnt5A`

Validation result:

- 53 independently reviewable LiteratureAtom objects.
- One shared publication UUID across the set; all atom IDs unique.
- `literature.py` Pydantic structural validation: **0 errors**.
- `literature_atom.schema.json` JSON Schema validation: **0 errors**.
- `literature_atoms.py` atom-kind sufficiency validation: **0 errors, 0 warnings**.
- Blocking ATOM errors: **0**.
- Every atom has a reliable source locator and source excerpt.
- Provenance preserves the current primary-source hash and extraction-run identity.
- Reported, normalized, calculated, and inferred assertions were not collapsed into one origin class.

Direct semantic spot-checks:

1. Primary efficacy result — PASS: 21/72 (29%) tofacitinib versus 37/70 (53%) placebo flared by week 44; hazard ratio 0.46 (95% CI 0.27-0.79), p=0.0031.
2. Supplemental Figure S5 — PASS: week-44 JIA/ACR response panel preserved, including ACR30 71% versus 47% and the higher-threshold response categories.
3. Safety — PASS: Part 2 any adverse event 68/88 (77%) versus 63/85 (74%), serious adverse events 1/88 (1%) versus 2/85 (2%); entire tofacitinib exposure infection/infestation 107/225 (48%).
4. Limitations — PASS: indirect withdrawal/flare design, placebo dropout after flare, relatively small predominantly White cohort, short follow-up for rare harms, and limited PsA/ERA sample sizes are represented without converting appraisal into reported evidence.

## SEA repair and QA

SEA was regenerated from the same article/appendix version after the coverage manifest was built and the visual inventory reconciled.

- SEA HTML: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML / S0140673621012551_sea.html`
  - Drive file ID: `1JR8xua0iP44Ammw1HnPSDYCqnF0OWT6Z`
- SEA QA JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON / S0140673621012551-sea-qa.json`
  - Drive file ID: `1tB96an66ZPMMaUj_Gp5sCIP4yEQry8y6`

SEA result:

- HTML parseability: PASS.
- Exact source title, DOI, PMID, NCT number, article hash, and appendix hash: PASS.
- Design/methods: PASS, including the open-label 18-week run-in, double-blind withdrawal period, randomization population, endpoints, flare definition, and statistical analysis.
- Primary result/conclusion spot-check: PASS.
- Numerical claim spot-check: PASS for primary flare HR and absolute event rates.
- Limitation/uncertainty spot-check: PASS.
- Main-text Figure 1, Figure 2, Figure 3 and Tables 1-3: all represented structurally.
- Material supplemental Figures S1-S11, Tables S2-S3, protocol, and SAP: represented or explicitly reconciled. CONSORT Table S1 is explicitly omitted from evidence synthesis as a reporting checklist rather than a load-bearing evidentiary object.
- Figure/table-derived claim spot-check: PASS for Figure S5 response rates and the safety table.
- No TODOs, placeholders, stale source names, internal chat/file citation syntax, external scripts/stylesheets, or remote images were found.

## ATOM-SEA reconciliation

ATOM and SEA use the same publication identity and the same article/supplement hashes. Consequential findings were reconciled across both outputs.

- Primary flare result: consistent.
- Secondary JIA/ACR responses: consistent.
- JADAS/CHAQ-DI trajectory: consistent.
- Safety findings: consistent.
- Limitations and uncertainty: consistent.
- Sponsor/funding role: consistently identified.
- No unresolved cross-artifact contradiction or source-integrity issue was found after regeneration.

## Reference-processing gate

A new identity-matched reference task queue was created from all 30 references in the primary article:

- `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD / S0140673621012551_reference_task_queue.md`
  - Drive file ID: `16S0jX14pMDgQ-g72Etuz_2n4Pg1tCKxO`

The queue is an inventory, not proof of completion. All 30 entries remain explicitly unresolved because this packet audit did not find a pre-existing per-reference lifecycle completion record proving routing/acquisition/resolution for the cited works. They therefore remain unchecked rather than being promoted on citation presence or filename similarity.

**Reference-processing gate: FAIL / incomplete.**

## Lifecycle action

- Assigned status: `PARTIAL - REPAIR REQUIRED`.
- The packet remains in `2 - 10 - Active Literature / 1 - Clinical Medicine & Pharmacy`.
- The packet was **not** moved to `90 - Processed` because reference processing is not demonstrably complete.
- A Needs Resolution move is not warranted: the primary source and material supplement are complete and usable, and the ATOM/SEA artifacts now pass their validation gates.

## Exact remaining task

Reconcile all 30 entries in `S0140673621012551_reference_task_queue.md` against the live TBR / Active / Processed / Citation Bank lifecycle. For each citation, record a definitive existing/completed/routed/acquired/resolved disposition and perform any required routing or acquisition work. When every entry has defensible completion evidence, rerun the packet completion gate. ATOM and SEA do not currently require further repair.
