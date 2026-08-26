# dkx358 publication packet repair report

## Lifecycle result

**PASS**

**OVERRIDEN BY CONNOR FOWLER ON 2026-08-26T03:06:59Z**

The source is usable and the ATOM/SEA evidence artifacts can be verified, but the packet does **not** satisfy the reference-processing completion gate. The packet must remain in `2 - 10 - Active Literature / 1 - Clinical Medicine & Pharmacy` and must **not** be moved to `5 - 90 - Processed` yet.

**HUMAN REVIEW HAS YIELDED SUFFICIENT EVIDENCE TO PASS THIS PACKET**

## Source audit

- Packet: `3 - dkx358`
- Primary source: `dkx358.pdf`
- Primary-source status: usable, 3 pages, not encrypted, text-extractable, visually renderable.
- Target publication: **Ceftazidime/avibactam use for carbapenem-resistant Klebsiella pneumoniae meningitis: a case report**
- DOI: `10.1093/jac/dkx358`
- Journal citation: *Journal of Antimicrobial Chemotherapy* 2018;73(1):254-256; Advance Access 10 October 2017.
- SHA-256: `42ac787624521273ffe19d08ddec30f874d283cd677d48531b3b4fc0cd48699f`
- Supplements in packet: none.
- Source-integrity note: the PDF is a three-page journal-issue excerpt. It contains the end of a preceding research letter on journal page 254 and the start of DOI `10.1093/jac/dkx362` on journal page 256. Both adjacent articles were explicitly excluded from dkx358 extraction/appraisal.

## Artifact inventory and identity matching

- SEA HTML: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML / dkx358-SEA.html` — identity match by exact title and DOI; verified.
- Reference queue: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD / dkx358-reference-task-queue.md` — identity match by exact title and DOI; present but incomplete.
- ATOM JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON / dkx358-atoms.json` — regenerated from the current source during this repair.
- ATOM validation JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON / dkx358-validation.json` — regenerated with authoritative validators during this repair.
- Coverage JSON: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON / dkx358-coverage.json` — generated during this repair.
- Processing report: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD / dkx358-processing-report.md` — this report.

No identity-matched ATOM JSON, validation JSON, coverage JSON, or prior processing report was found before repair. Filename similarity was not used as proof.

## ATOM validation

Validation was run in the required order against the authoritative project files:

1. `literature.py` Pydantic structural validation — **PASS**
2. `literature_atom.schema.json` JSON Schema validation — **PASS**
3. `literature_atoms.py` atom-kind sufficiency validation — **PASS**

- Atom count: **18**
- Shared publication ID: `2d0210c8-bf12-53bf-b9cd-b89b695a9a80`
- Unique atom IDs: **PASS**
- Provenance hash matches current PDF SHA-256 on every atom: **PASS**
- Blocking structural/schema/sufficiency errors: **0**
- Sufficiency warnings: **0**

### Direct semantic spot-checks

- Primary result/conclusion: repeat cultures became negative during ceftazidime/avibactam plus intraventricular gentamicin with EVD exchange; authors characterize the course as successful — **PASS**.
- Numerical claim: Table 1 reports CSF WBC 3120 cells/mm³ on treatment day 0 and 3 cells/mm³ on day 23 — **PASS**.
- Limitation: authors state that treatment effect cannot be apportioned between ceftazidime/avibactam and intraventricular gentamicin — **PASS**.
- Table-derived claim: gentamicin MIC 1 mg/L interpreted susceptible; ceftazidime/avibactam reported susceptible by Kirby-Bauer disc diffusion without a numeric MIC — **PASS**.

## SEA verification

`dkx358-SEA.html` is parseable HTML with a matching title/DOI and working internal anchors. It represents the case rationale, clinical course, definitive regimen, microbiology, serial CSF findings, limitations, funding/transparency, and appraisal.

Visual/content coverage:

- Main-text figures: **0**
- Main-text tables: **1** (`Table 1 - CSF analyses and culture susceptibilities`) — represented as structured tables.
- Algorithms/workflows: **0**
- Material target-article supplements: **0**
- Adjacent articles in the PDF: explicitly excluded.

SEA semantic spot-checks against the current PDF all passed for the primary conclusion, treatment durations/doses, serial CSF numerical values, the combination-therapy attribution limitation, and Table 1 susceptibility data.

## ATOM ↔ SEA reconciliation

ATOM and SEA refer to the same source/version and DOI. No consequential contradiction was found. Both preserve the central uncertainty that causal treatment effect cannot be separated between ceftazidime/avibactam, intraventricular gentamicin, and concurrent device/source-control management. The ATOM set marks the definitive ceftazidime/avibactam dose as `normalized_from_source` because the dose is stated earlier and the definitive paragraph says therapy was "restarted"; this avoids converting normalization into direct reporting.

## Reference-processing gate

`dkx358-reference-task-queue.md` contains **9** cited references and **all 9 tasks remain unchecked**. The queue explicitly requires acquisition/direct reading/triage before reuse. Therefore reference processing is **not complete**. The queue's existence is not sufficient evidence of completion under the packet-repair rule.

Because the execution rule requires this agent to stop after this publication packet, this repair does not process the nine cited publications as separate literature packets.

## Warnings

- The source PDF includes adjacent articles; strict DOI/title boundaries are required for any future reprocessing.
- This is a single uncontrolled case with combination therapy and EVD exchange; the source does not establish ceftazidime/avibactam monotherapy efficacy, an optimal duration, or a causal contribution of either antimicrobial.
- The existing reference queue remains a live dependency.

## Lifecycle action

**Leave `3 - dkx358` Active. Do not move it to Processed.**

Exact remaining task: **complete and document all 9 reference-processing tasks in `dkx358-reference-task-queue.md` (direct source acquisition/read/triage or a defensible resolved disposition for each), then rerun the packet completion gate. If reference processing then passes with the verified ATOM/validation/SEA/coverage artifacts unchanged or revalidated, move the packet to `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy` preserving the folder name.**

Generated: 2026-08-25T09:03:38Z
