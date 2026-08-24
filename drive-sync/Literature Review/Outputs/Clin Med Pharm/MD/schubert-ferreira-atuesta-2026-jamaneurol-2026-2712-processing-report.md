# Safety of Antiseizure Medications During Direct Oral Anticoagulant Therapy in Epilepsy - processing report

## Activated macros

`@ATOM + @SEA`

## Result

Status: **BLOCKED FOR WHOLE-SOURCE COMPLETION**. An abstract-only partial package was generated and validated. The source packet cannot meet the project's `90 - Processed` gate because the article body and bibliography are unavailable in this run. The packet should remain active as a resolution item rather than being represented as fully processed.

## Project-source requirements applied

ATOM validation used `literature(1).py` as the structural authority, `literature_atoms(1).py` for atom-kind sufficiency, and `literature_atom.schema.json` for serialization validation. `README(2).md` supplied workflow intent and `example_atom(1).json` remained illustrative only. SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing protocol. `large-source-ATOM-SEA.md` supplied the whole-source coverage and access-gap guardrails. The v3 SEA file was historical reference only. `unslop.skill.md` controlled prose style.

## Source-derived findings

The accessible JAMA Neurology abstract reports a retrospective target-trial emulation in 9,529 ASM initiators receiving DOACs. It reports higher thromboembolic risk with levetiracetam and strong enzyme-inducing ASMs, higher mortality with levetiracetam and valproate, lower major bleeding with strong enzyme-inducing ASMs, and higher intracranial major bleeding with valproate. The exact abstract-level effect estimates are preserved in the ATOM JSON and SEA.

## External verification

On 2026-08-23 the JAMA Neurology public article page was rechecked. It confirms the source identity, publication date, structured abstract, and DOI. It also exposes a `Get Access` flow for the article body and PDF in this session. No paywall bypass, account login, purchase, or secondary-source reconstruction was used.

## Model inference and appraisal boundary

The SEA scoring is an appraisal of the accessible abstract, not a full article appraisal. The main limitation is unresolved residual confounding plus the inability to inspect detailed methods, absolute event rates, balance diagnostics, figures, tables, supplements, and sensitivity analyses. The `Read first` verdict means the full article deserves priority review. It does not authorize a medication change from the abstract alone.

## Validation

- Extracted abstract-level atoms: 26
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Shared publication identity: PASS
- Duplicate statement-anchor pairs: 0
- Whole-source ATOM gate: BLOCKED
- Full SEA coverage gate: BLOCKED
- SEA mechanical QA: PASS WITH ACCESS LIMITATION

## Reference task queue

The bibliography is not accessible. A blocker queue was generated with five P0 completion tasks and an explicit unknown reference count. No bibliography entries were fabricated.

## Output files

### JSON

- `schubert-ferreira-atuesta-2026-jamaneurol-2026-2712-atoms.json`
- `schubert-ferreira-atuesta-2026-jamaneurol-2026-2712-validation.json`
- `schubert-ferreira-atuesta-2026-jamaneurol-2026-2712-coverage.json`
- `schubert-ferreira-atuesta-2026-jamaneurol-2026-2712-crosswalk.json`
- `schubert-ferreira-atuesta-2026-jamaneurol-2026-2712-sea-qa.json`

### HTML

- `schubert-ferreira-atuesta-2026-jamaneurol-2026-2712-sea.html`

### Markdown

- `schubert-ferreira-atuesta-2026-jamaneurol-2026-2712-reference-task-queue.md`
- `schubert-ferreira-atuesta-2026-jamaneurol-2026-2712-processing-report.md`

## Placement decision

The current TBR placement rule reserves `90 - Processed` for packets whose references, ATOM, validation, and SEA outputs are complete and verified. This packet does not satisfy that rule. Route `27 - Schubert Ferreira-Atuesta 2026` to `3 - Needs Resolution`, keep the parent PubMed-trending item unfinished, and update the current TBR state to reflect the new blocked packet.
