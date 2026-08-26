# 26 - Recurrent Guillain-Barre syndrome case series processing report

## Lifecycle result

**PASS - ATOM/SEA VERIFIED**

The publication packet is closed. The packet folder was moved from Active Clinical Medicine & Pharmacy to `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`. The folder name and Drive ID were preserved.

Packet folder Drive ID: `1SWuzNtD-F1G_h8P5FzdSCIsJOwu5mbp-`

Previous parent: `1wA_mmV9fJvfM7ILPwPuc-Uac1SJ1hpk0`

New parent: `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`

Move result: PASS

Exact remaining task for this publication packet: none.

## Primary source audit

The packet contains one primary source and no supplements.

Primary source: `recurrent-guillain-barr-syndrome-case-series.pdf`

Drive ID: `1tuTWjbtUbqriLTkoTFYqwnmZllFZHwFJ`

File size: 629,593 bytes

PDF pages: 3

SHA-256: `b97593fc081f47c6533ae35847c0c209f8dc06dfeaa4a006f9d918252c750204`

The PDF opens, renders, and contains the complete 2019 Neurology India case series. Source identity is `Recurrent Guillain-Barré Syndrome – Case Series`, Neurol India. 2019;67:1536-1538, DOI `10.4103/0028-3886.273649`.

The supplied PDF prints PMID as `xxxx`. No external PMID was substituted.

## Artifact inventory and repair

The preexisting SEA HTML and reference Markdown match the primary publication by title, DOI, citation, source metadata, and content. Before repair, no identity-matched ATOM JSON, ATOM validation JSON, or coverage JSON was present in the Clin Med Pharm JSON output folder. Those missing outputs were regenerated from the current primary PDF and uploaded.

JSON outputs in `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`:

- `26-recurrent-guillain-barre-syndrome-case-series-atoms.json`, Drive ID `1cd4M3cI-X-SFIkRceIvqav9PUbaVl6Mf`
- `26-recurrent-guillain-barre-syndrome-case-series-ATOM-validation.json`, Drive ID `1DQmU6Jpp8yLf1cgN3gZne2fQiROwtc0B`
- `26-recurrent-guillain-barre-syndrome-case-series-coverage.json`, Drive ID `1f555z-hR-xlTBk0YHDCJoyowhBqnygOO`
- `26-recurrent-guillain-barre-syndrome-case-series-SEA-validation.json`, Drive ID `1s_RIB8C91_MqkPAXwHgU_hUbSbB6HDPf`

HTML output in `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`:

- `26-recurrent-guillain-barre-syndrome-case-series-sea.html`, Drive ID `1U5lPrxWImSMPac5u0ue96SECBomTWapx`

Markdown output in `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`:

- `26-recurrent-guillain-barre-syndrome-case-series-reference-task-queue.md`, Drive ID `1SzksN9-XsCHy3NMgfwXBGz9e3n_urQOv`
- this processing report

## ATOM validation

A new 34-atom set was generated from the current PDF. All atoms share publication ID `504c19ef-f260-5d78-bd4e-2f43cb30f061`, which is the same publication ID recorded in the SEA artifact. Atom IDs are unique. Source anchors and extraction provenance are present. The PDF hash is carried in extraction provenance.

Validation was run in the required order against the supplied governing project files.

1. `literature(1).py` Pydantic structural validation: PASS, 0 errors.
2. `literature_atom.schema.json` JSON Schema validation: PASS, 0 errors.
3. `literature_atoms(1).py` atom-kind sufficiency validation: PASS, 0 errors, 0 warnings.

Exact duplicate canonical-statement and source-anchor pairs: 0.

Direct source spot checks passed for the primary result, AIDP proportions, disability uncertainty, and Table 1 content. The source reports 13 recurrent cases among 404 GBS patients, 3.2 percent. AIDP accounted for 76.9 percent of first attacks and 84.6 percent of recurrent attacks. Several paired comparisons are reported only as `P > 0.05`, without confidence intervals or exact p-values. No equivalence claim was introduced.

All model-extracted atoms remain `needs_review` because no independent human reviewer identity is represented. That atom review field is preserved rather than falsely marked verified. The packet-level verification reported here reflects direct source audit, authoritative validation, and semantic spot checking.

## SEA validation and coverage

The existing SEA HTML is identity matched to the same DOI, source file, source hash, and publication ID used by the repaired ATOM set.

Mechanical HTML QA: PASS. The document parses, its table-of-contents targets resolve, and no internal chat citation syntax, TODO markers, or placeholders were found.

Semantic QA: PASS. The artifact includes source metadata, methods and design, main claims, quantitative findings, limitations and uncertainty, provenance, appraisal, and clinical-use boundaries.

Coverage reconciliation:

- Primary PDF pages inspected: 3 of 3
- Main tables: 1 of 1 reconciled
- Main figures: 0 of 0
- Algorithms or workflows: 0
- Supplements or appendices: 0
- References: 10 of 10 reconciled

Table 1 is preserved as a structured paired-patient reconstruction. The between-attacks interval for Patient 12 is printed as `6` without a unit in the source cell. The SEA leaves that unit unresolved rather than inferring it.

The SEA correctly treats the study as descriptive evidence. It warns that failure to detect a significant difference does not establish equivalent episode severity, and it does not infer treatment efficacy from the large change in treatment use between first and recurrent attacks.

## ATOM and SEA reconciliation

ATOM and SEA use the same primary PDF, SHA-256, DOI, and publication ID. The repaired ATOM count of 34 matches the SEA provenance statement. Consequential methods, cohort selection, recurrence frequency, variant switching, disability results, treatment use, uncertainty, Table 1, and source-integrity issues were checked across both artifacts. No contradiction requiring repair remains.

## Reference processing

The source bibliography contains 10 numbered references. The reference task queue contains all 10 entries in the same order, with citation content preserved from the supplied article. I checked the queue against the primary PDF rather than treating file existence as completion.

Reference extraction and queue reconciliation: PASS, 10 of 10.

The unchecked boxes are downstream cited-publication tasks. They do not represent missing bibliography extraction from this primary packet. Processing those cited publications would require leaving the named packet and is outside this single-packet closure task.

## Source-integrity warnings preserved

- The supplied PDF prints PMID as `xxxx`.
- Patient 12 has a between-attacks interval of `6` with no unit printed in the Table 1 cell.
- Two patients were excluded for `comorbidities` without further explanation in the article.
- Several comparisons are reported only as `P > 0.05`, with no confidence intervals or exact p-values.
- Treatment patterns differ substantially between first and recurrent attacks, so treatment efficacy and episode equivalence cannot be inferred.

## Governing sources

ATOM structural validation used `literature(1).py`. Serialization validation used `literature_atom.schema.json`. Atom-kind sufficiency validation used `literature_atoms(1).py`. `README(2).md` supplied workflow intent, and `example_atom(1).json` was treated as illustrative only.

SEA QA used `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing protocol. `summary-evaluation-appraisal-protocol-v3-compact.html` was historical reference only. `large-source-ATOM-SEA.md` supplied supporting coverage and reconciliation guidance. `unslop.skill.md` was retrieved from File Library and applied to prose reporting.

No external web verification was used.
