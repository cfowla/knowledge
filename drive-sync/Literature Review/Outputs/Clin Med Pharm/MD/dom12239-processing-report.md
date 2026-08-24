# dom12239 processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Primary article: `Diabetes Obesity Metabolism - 2013 - Goring - Dapagliflozin compared with other oral anti‐diabetes treatments when added to.pdf`, 10 pages, canonical processed SHA-256 `e9870640b238fc1bafdbb0f01d9099cc195c6915cc780b0b5464e617e3f9fb97`
- Appendix S1: `dom12239-sup-0001-appendixs1.doc`, SHA-256 `94547569207c4b9f13a41b8e635dc5b14c2c5f54e42034547f011453b0d72558`
- Appendix S2: `dom12239-sup-0002-appendixs2.doc`, SHA-256 `06cf5e570dfdf4f5c638625d841e9f3dab064db5a162573418943b684fd8337e`
- Title: *Dapagliflozin compared with other oral anti-diabetes treatments when added to metformin monotherapy: a systematic review and network meta-analysis*
- Citation: Diabetes Obes Metab. 2014;16(5):433-442.
- DOI: `10.1111/dom.12239`
- PMID: `24237939`
- Shared publication ID: `5c8bd6a7-6ee0-5391-8db1-27bad5331c85`
- Source type: systematic review and Bayesian network meta-analysis of randomized controlled trials

## ATOM result

- LiteratureAtoms: **55**
- Atom kinds: `{"author_conclusion": 1, "comparator_description": 1, "conflict_of_interest": 1, "eligibility_criterion": 2, "funding_disclosure": 1, "intervention_description": 1, "limitation": 5, "method": 12, "outcome_definition": 4, "population_description": 2, "qualitative_result": 3, "quantitative_result": 21, "study_objective": 1}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Duplicate statement-anchor pairs: **0**

The source is secondary literature. The review's network meta-analysis estimates remain review-level quantitative results. The atom set does not present underlying trial observations as if this review generated them.

The current project model, schema, and sufficiency validator were rerun against all 55 stored atoms on 2026-08-23. All checks passed again without changing the atom JSON.

## SEA result

Coverage reconciles both main-text figures, all four main-text tables, Appendix S1 search strategies, and Appendix S2 absolute estimates. The verdict remains **Skim deeply**. The paper is useful historical comparative evidence but is not sufficient by itself for a current inpatient SGLT2 interchangeability or formulary decision.

SEA semantic QA was rerun on 2026-08-23. The HTML title is present, all six internal navigation targets resolve, appraisal and provenance content are present, and no TODO, placeholder, or internal tool-citation markers remain. `dom12239-sea-qa.json` records the recheck.

## Reference task queue

The article contains **58** bibliography entries. The original `dom12239-references.md` remains as a source-order bibliography. `dom12239-reference-task-queue.md` adds checkbox work state and source-based priorities without changing the citations.

- P0 direct trials used in the primary network or sensitivity analysis: **8**
- P1 later full publications or closely related direct active-comparator trials: **4**
- P2 methods and comparative-evidence sources: **18**
- P3 background, clinical context, mechanism, or general guidance: **28**

Bibliography entries were not atomized. No external bibliographic correction was performed during the 2026-08-23 reconciliation.

## Active-folder reconciliation

A stale active packet for the same publication remained at `3/2/1/17` after the canonical processed packet and outputs had already been completed.

- The active S1 and S2 supplements are exact byte matches to the canonical processed copies.
- The active main PDF has SHA-256 `58b8a7651f5b1a1b2114e4b8394a55fd25a6db4b577e29d761afbc316fb705a6`, while the canonical processed PDF has SHA-256 `e9870640b238fc1bafdbb0f01d9099cc195c6915cc780b0b5464e617e3f9fb97`.
- Both PDFs produce the same extracted-text SHA-256, `68dc63d0ce22e65df063e652cf1a06fca1a92cba47d0e45f440bf9c8d4ac0148`.
- Because the PDFs are not byte-identical, the stale active packet was preserved rather than deleted. The whole folder was moved under the canonical processed packet and renamed `Reconciled active intake - 2026-08-23`.

After the move, `2 - 10 - Active Literature` contains **18** numbered source folders plus its three organizational folders.

## Governing sources

ATOM precedence applied:

1. `literature(1).py`
2. `literature_atoms(1).py`
3. `literature_atom.schema.json`
4. `README(2).md`
5. `example_atom(1).json`

SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing protocol. The v3 protocol was treated as historical reference only. `large-source-ATOM-SEA.md` supplied the source-mapping and secondary-source guardrails. `unslop.skill.md` was applied to prose written during this reconciliation.

## Output files

### JSON

- `dom12239-atoms.json`
- `dom12239-validation.json`
- `dom12239-coverage.json`
- `dom12239-sea-qa.json`

### HTML

- `dom12239-sea.html`

### Markdown

- `dom12239-references.md`
- `dom12239-reference-task-queue.md`
- `dom12239-processing-report.md`
