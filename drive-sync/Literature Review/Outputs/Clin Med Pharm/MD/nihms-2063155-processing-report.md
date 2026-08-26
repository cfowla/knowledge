# Publication packet repair report: 1 - nihms-2063155

## Lifecycle status

PASS - ATOM/SEA VERIFIED

## Source identity and packet condition

- Title: Trends in Invasive Methicillin-Resistant Staphylococcus aureus Infections
- Citation: Pediatrics. 2013;132(4):e817-e824
- DOI: 10.1542/peds.2013-1112
- PMID: 24062373
- PMCID: PMC11931424
- NIHMSID: NIHMS2063155
- Primary file: `nihms-2063155.pdf`
- Primary Drive file ID: `1RxwDWSsHC3iQ8JDjfptJ6RIjGDNQHxb9`
- PDF pages: 17
- SHA-256: `1db8b7f47977e2040169e5ff219b962c35f96b11771274ba4fd7bcc1aaae735d`
- Supplements: none present in the packet
- Primary-source usability: PASS. The PDF opens normally and contains the article body, bibliography, two figures, and three tables.

## Identity-matched artifact audit

The audit searched by exact title, DOI, PMID, PMCID, NIHMSID, source metadata, and source content. Filename similarity was not accepted as identity proof.

Existing identity-matched artifacts that passed review:

- SEA HTML: `nihms-2063155-sea.html`, Drive ID `1wKP5MbDsuaK7UCPMrhJbW07zoCnUO9OW`
- Reference task queue: `nihms-2063155-reference-task-queue.md`, Drive ID `1FYvWmHhIqrUDYp_LZSocC-d1N0J84DCn`

Missing before repair:

- ATOM JSON
- authoritative ATOM validation JSON
- coverage JSON
- processing report

No prior identity-matched ATOM validation report was found, so no reconstructed or local validator result was accepted as proof.

## ATOM repair and validation

Generated `nihms-2063155-atoms.json` with 56 LiteratureAtom objects across semantic extraction batches. All atoms share publication ID `5a0646e8-d518-5f64-acdc-9c707b7bb7d7` and have unique atom IDs and source anchors.

Validation ran in the required order against the supplied project sources:

1. `literature(1).py` Pydantic structural validation: PASS, 0 errors
2. `literature_atom.schema.json` JSON Schema validation: PASS, 0 errors
3. `literature_atoms(1).py` atom-kind sufficiency validation: PASS, 0 errors, 0 warnings

Merge checks passed. There are no duplicate statement and anchor pairs. Direct semantic spot checks passed for the Figure 2 community-associated trend, Table 3 national burden, the main national-representativeness limitation, and Table 1 case fatality values.

One source discrepancy is preserved rather than silently repaired. The abstract prints the upper confidence limit for the community-associated annual trend as 18.2%, while the main Results text and Figure 2 use 18.3%. The ATOM result uses the main Results and Figure 2 value of 18.3% and records the discrepancy in validation notes.

The current schema requires an `exposures` context for quantitative results. For descriptive epidemiology, age, race, epidemiologic category, calendar year, or national-estimate strata are encoded with role `exposure` only to satisfy that context contract. This encoding does not assert causality.

## SEA verification

The existing SEA was checked against the current PDF and does not require regeneration.

- HTML parseability: PASS
- Source title, DOI, PMID, PMCID, and SHA-256: PASS
- Methods and design: PASS
- Main claims and quantitative findings: PASS
- Limitations and uncertainty: PASS
- Provenance: PASS
- Table of contents anchors: PASS
- Internal chat or file citation syntax: absent
- TODO or placeholder text: absent
- Main figures: 2 of 2 reconciled
- Main tables: 3 of 3 reconciled
- Workflows or algorithms: 0
- Supplements: 0

Semantic spot checks passed for the primary conclusion, the 10.2% annual increase in community-associated incidence among children older than 3 months, the 2010 overall national incidence of 2.6 per 100,000 and estimated 1,895 infections, the 43.9 per 100,000 estimate in infants aged 3 through 89 days, the racial incidence difference, the national-representativeness limitation, and a Table 1 fatality claim.

The SEA also keeps the study's causal boundary intact. The authors suggest that NICU infection-prevention progress may partly explain the decline in late-onset hospital-onset disease among infants, but the surveillance study did not test that mechanism.

## Reference processing

Reference processing was verified against the primary PDF rather than accepted from file presence alone.

- Source bibliography entries: 37
- Queue entries: 37
- Source numbering represented in queue: 1 through 37, complete with no gaps
- Queue entries with PMID: 33
- Non-PMID source or report entries: 4
- Status: PASS

The unchecked queue items are downstream cited-publication work. They do not indicate missing bibliography extraction from this packet and do not block closure of the primary publication packet.

## ATOM and SEA reconciliation

ATOM and SEA use the same primary source and source hash. Consequential methods, trend estimates, national burden values, limitations, and the NICU causal-boundary issue were checked across both artifacts. No cross-artifact contradiction requiring repair was found.

## Output locations

JSON, GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON:

- `nihms-2063155-atoms.json`, Drive ID `171takakNbv7y0n3ppkHF7svwpSFlzS_p`
- `nihms-2063155-validation.json`, Drive ID `1wazPACuuA-8iserVEPKTllFVM1ckgZvl`
- `nihms-2063155-coverage.json`, Drive ID `12guJP-K9IShoYSeS6_Q8xlYY5ZSbZZ1M`

HTML, GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML:

- `nihms-2063155-sea.html`, Drive ID `1wKP5MbDsuaK7UCPMrhJbW07zoCnUO9OW`

Markdown, GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD:

- `nihms-2063155-reference-task-queue.md`, Drive ID `1FYvWmHhIqrUDYp_LZSocC-d1N0J84DCn`
- `nihms-2063155-processing-report.md`, Drive ID `1w36cLEt8XXyKTQM_C9IbchGLLCCZCxwx`

## Governing and supporting sources

ATOM validation used the supplied `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom(1).json`, with the example treated as illustrative only. SEA verification used `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing SEA protocol. `large-source-ATOM-SEA.md` guided coverage and reconciliation. `summary-evaluation-appraisal-protocol-v3-compact.html` was historical reference only. `unslop.skill.md` controlled prose style.

No external web verification was used for this packet audit.

## Lifecycle action

Status is PASS - ATOM/SEA VERIFIED. The folder `1 - nihms-2063155` was moved from Active Clinical Medicine & Pharmacy to `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`. The folder name and Drive ID were preserved.

Move evidence:

- Packet folder Drive ID: `1fx9xdGxPvG48-A7vapHcnv11c4-UEMvh`
- Previous parent: `1wA_mmV9fJvfM7ILPwPuc-Uac1SJ1hpk0`
- New parent: `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`
- Move result: PASS

Exact remaining task: none for this publication packet. The 37 unchecked reference-queue entries are downstream cited-publication tasks and remain outside this closed packet.
