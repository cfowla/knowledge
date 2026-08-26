# Publication packet repair report: 120 - nihms-1829921

## Lifecycle status

PASS - ATOM/SEA VERIFIED

## Source identity and packet condition

- Title: The ECHELON-2 Trial: 5-year results of a randomized, phase III study of brentuximab vedotin with chemotherapy for CD30-positive peripheral T-cell lymphoma
- Citation: Ann Oncol. 2022;33(3):288-298.
- DOI: 10.1016/j.annonc.2021.12.002
- PMID: 34921960
- PMCID: PMC9447792
- NIHMSID: NIHMS1829921
- Trial: NCT01777152
- Primary file: `nihms-1829921.pdf`
- Primary Drive file ID: `1hP3VcIdl18reEMykHe7rbe7xtO3Tlmfn`
- Primary PDF pages: 18
- Primary SHA-256: `16c24fcf949e427cb3c2cd87559f016a2c41af652b351556e7efe01c49719142`
- Primary-source usability: PASS. The PDF opens, extracts, renders through all 18 pages, and contains the complete article body, four main figures, Table 1, and 37 references.
- Supplements: five supplied DOCX files, all non-empty and usable. They contain Supplementary Figures S1-S2 and Supplementary Tables S1-S3.

## Identity-matched artifact audit

The audit matched artifacts by exact title, DOI, PMID, PMCID, NIHMSID, trial identifier, primary SHA-256, source metadata, and content. Filename similarity was not accepted as identity proof.

Existing identity-matched artifacts that passed review:

- SEA HTML: `nihms-1829921-sea.html`, Drive ID `1zLGa3YYth1T4nTw5ms-Rhpi-0CVi3MO4`
- Reference task queue: `nihms-1829921-reference-task-queue.md`, Drive ID `19XpxzEbQshTNamlmGknOgAVU_YtIVIpr`

Missing from the required Drive output folders before repair:

- ATOM JSON
- authoritative ATOM validation JSON
- coverage JSON
- processing report

A prior File Library extraction was not treated as proof of Drive completion. Its stable publication identity was preserved because it matched the current source by title, DOI, NIHMSID, source hash, and content.

## ATOM repair and authoritative validation

Generated `nihms-1829921-atoms.json` with 80 LiteratureAtom objects across seven semantic batches. Every atom uses publication ID `cacba548-9407-539c-9500-8862f1668549`. Atom IDs are unique and all batches use schema version 1.0.

Validation ran in the required order against the supplied project sources:

1. `literature(1).py` Pydantic structural validation: PASS, 0 errors
2. `literature_atom.schema.json` Draft 2020-12 JSON Schema validation: PASS, 0 errors
3. `literature_atoms(1).py` atom-kind sufficiency validation: PASS, 0 errors, 0 warnings

Merge checks passed. There are no duplicate atom IDs or duplicate canonical-statement plus source-anchor pairs. Provenance and source anchors are present on every atom.

Direct semantic spot-checks passed for the overall PFS result, overall OS result, peripheral-neuropathy follow-up, Table 1 post-progression brentuximab response, Supplementary Table S1 CD30-response strata, and the exploratory and multiplicity limits of the 5-year analysis.

Two source-reporting issues were preserved rather than silently repaired:

- The CHOP ongoing-neuropathy paragraph prints grade counts of 30/42, 11/42, and 1/42 alongside percentages of 64%, 23%, and 2%. The counts sum to 42, but the printed percentages are internally inconsistent. No recalculated percentages replaced the source values.
- The abstract reports median follow-up of 47.6 months for the 5-year efficacy estimates, while Results reports median follow-up to last contact of 66.8 months with a range of 0 to 90 months. These were retained as distinct reported follow-up summaries.

All model-extracted atoms retain `review_status=needs_review` because no independent human reviewer identity is represented in provenance. This does not replace the direct semantic audit performed for packet closure.

## SEA verification

The existing SEA was checked against the current primary PDF and all five supplied supplements. Regeneration was not required.

- HTML parseability: PASS
- Exact source identity and primary SHA-256: PASS
- Methods and design: PASS
- Main claims and quantitative findings: PASS
- Limitations and uncertainty: PASS
- Provenance: PASS
- Table-of-contents anchors: PASS
- Internal chat or file citation syntax: absent
- TODO or placeholder text: absent
- Main figures: 4 of 4 reconciled
- Main tables: 1 of 1 reconciled
- Algorithms or workflows: 0
- Material supplements: 5 of 5 reconciled

Semantic checks confirmed PFS HR 0.70 with 95% CI 0.53 to 0.91, OS HR 0.72 with 95% CI 0.53 to 0.99, 5-year PFS 51.4% versus 43.0%, 5-year OS 70.1% versus 61.0%, the exploratory and underpowered subgroup constraints, and Table 1 and Figure 2-derived findings. The SEA also preserves the printed neuropathy-percentage inconsistency.

## Reference processing

Reference processing was checked against the primary PDF rather than accepted from file presence alone.

- Source bibliography entries: 37
- Queue entries: 37
- Source numbering represented in queue: 1 through 37 with no gaps
- Status: PASS

The unchecked queue entries are downstream cited-publication tasks. They do not indicate missing bibliography extraction from this publication packet and do not block closure.

## ATOM and SEA reconciliation

ATOM and SEA use the same source identity and primary SHA-256. Consequential design, efficacy, subgroup, safety, subsequent-therapy, limitation, and source-integrity claims were cross-checked. No cross-artifact contradiction requiring repair remains.

## Output locations

JSON, `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`:

- `nihms-1829921-atoms.json`, Drive ID `1UxXljKpw8CWwmE3UodlSRb7hSWbfkseA`
- `nihms-1829921-validation.json`, Drive ID `1MHRqDoFqt5kF3kyqewIsJlwOAkQu6On3`
- `nihms-1829921-coverage.json`, Drive ID `1J9n2k3dqJoF547bERXlcBpSNVlr3dPp3`

HTML, `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`:

- `nihms-1829921-sea.html`, Drive ID `1zLGa3YYth1T4nTw5ms-Rhpi-0CVi3MO4`

Markdown, `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`:

- `nihms-1829921-reference-task-queue.md`, Drive ID `19XpxzEbQshTNamlmGknOgAVU_YtIVIpr`
- `nihms-1829921-processing-report.md`, Drive ID `1lRXU4eIToAp_trdRrRmAWx9FPzkJrcE8`

## Governing and supporting sources

ATOM validation used the supplied `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom(1).json`, with the example treated as illustrative only. SEA verification used `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing SEA protocol. `large-source-ATOM-SEA.md` guided coverage and reconciliation. `summary-evaluation-appraisal-protocol-v3-compact.html` was historical reference only. `unslop.skill.md` controlled prose style.

The governing filename is `summary-evaluation-appraisal-protocol-v4-compact.md`, while its internal heading identifies Integrated Compact v3. Project precedence makes the v4-named file authoritative.

External verification was used only to confirm stable bibliographic identity and a full-text visual-access fallback. The Drive primary PDF and supplied supplements remained the evidence basis for packet validation.

## Lifecycle action

The packet folder `120 - nihms-1829921` was moved from Active Clinical Medicine & Pharmacy to `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`. The folder name and Drive ID were preserved.

- Packet folder Drive ID: `1Afs2R7jJ_bLBgNsFk8ByvykSOR7tG31X`
- Previous parent: `1wA_mmV9fJvfM7ILPwPuc-Uac1SJ1hpk0`
- New parent: `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`
- Move result: PASS, verified by post-move folder metadata

Exact remaining task: none for this publication packet. The 37 unchecked reference-queue entries are downstream cited-publication tasks and remain outside this closed packet.
