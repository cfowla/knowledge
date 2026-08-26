# Processing report: Clostridioides difficile-induced diarrhoea following dasatinib therapy

## Activated macros

None. The publication-packet repair prompt directly required authoritative ATOM and SEA verification; project macros were not implicitly activated.

## Lifecycle result

**PASS - ATOM/SEA VERIFIED**

The packet is eligible for promotion because the primary source is usable, ATOM has zero blocking validation errors, SEA passes semantic/mechanical QA, all three figures are reconciled, the reference list is verified 17/17, and the required output set is complete.

## Source packet

- Folder: `10 - bcr-2020-239394`
- Main article: `bcr-2020-239394.pdf`
- Exact title: *Clostridioides difficile-induced diarrhoea following dasatinib therapy*
- Journal: *BMJ Case Reports* 2021;14:e239394
- DOI: `10.1136/bcr-2020-239394`
- Source type: single-patient case report
- Source pages reviewed: 3 of 3
- Source SHA256: `cc6a4c31ff3ede2159c0f5b0a81b20e815506d8668d41fa3669396b993b9d946`
- Publication ID: `f132c6e5-cee2-5faa-bce0-120806b037ef`
- Supplements: none present

## Source-integrity findings

1. Page 1 visibly prints the white blood cell count as `−6.85×10^9/L`. The prior SEA normalized this to positive `6.85×10^9/L` without noting the change. The repaired SEA and ATOM preserve the source-printed negative sign and flag it as an unresolved source-level anomaly.
2. The bibliography contains apparent source-printed anomalies. The prior reference queue silently corrected several entries. The repaired queue preserves the source text, including reference 4 `Ivan CH, R O’toole`, reference 8 `diarrhea of colitis`, and reference 14 `Kmira Zet al.`.
3. These source anomalies are not repaired into reported evidence. Any normalized interpretation must remain separate from the source-reported record.

## ATOM status

- Atoms: **28**
- By kind: `{"author_conclusion": 4, "conflict_of_interest": 1, "funding_disclosure": 1, "intervention_description": 4, "method": 3, "other": 2, "population_description": 1, "qualitative_result": 9, "quantitative_result": 2, "study_objective": 1}`
- Pydantic structural validation using `literature(1).py`: **PASS**
- JSON Schema validation using `literature_atom.schema.json`: **PASS**
- Sufficiency validation using `literature_atoms(1).py`: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Unique atom IDs: **PASS**
- Shared publication ID: **PASS**
- Input-document hash preserved on every atom: **PASS**
- Review status: `needs_review` for model-extracted atoms; no human verification was invented.

## SEA status

- Existing identity-matched SEA was reviewed against the current source and governing v4 protocol.
- HTML parseability: **PASS**
- Required metadata/methods-design/main claims/quantitative findings/limitations/provenance: **PASS**
- Figures: **3/3 represented with embedded crops and structured interpretation**
- Tables: none in source
- Algorithms/workflows: none in source
- Supplements: none in source
- Source-integrity repair for printed WBC value: **complete**
- Mechanical HTML QA: **PASS**
- Direct semantic spot-checks: primary conclusion **PASS**; numerical claim **PASS**; uncertainty/limitation **PASS**; figure-derived claim **PASS**; source-integrity preservation **PASS**.

The SEA's external current-practice note was rechecked against the official SHEA/IDSA 2021 focused update: fidaxomicin is suggested over a standard course of vancomycin for an initial adult CDI episode, vancomycin remains acceptable, and metronidazole is reserved as an alternative for nonsevere CDI when preferred agents are unavailable.

## ATOM/SEA reconciliation

- Both artifacts use the same title, DOI, source file and SHA256.
- CDI diagnosis, symptom timing, dasatinib exposure, metronidazole treatment, 14-day endoscopic resolution, 2-year non-recurrence after dasatinib restart, and the authors' causal hypothesis are represented consistently.
- The repaired artifacts distinguish source-reported association/hypothesis from appraisal. The lack of recurrent diarrhoea after dasatinib restart is preserved as causality context rather than rewritten as proof for or against causation.
- No consequential contradiction remains unresolved between ATOM and SEA.

## Reference processing

- References in source: **17**
- Reconciled against source: **17/17**
- Source order preserved: **PASS**
- Source-printed wording preserved: **PASS**
- Bibliography atomized as primary evidence: **No**
- Queue existence alone was not accepted as completion; each entry was checked against the source bibliography.
- Output: `bcr-2020-239394-reference-task-queue.md`

## Required outputs

### JSON

- `bcr-2020-239394-atoms.json`
- `bcr-2020-239394-validation.json`
- `bcr-2020-239394-coverage.json`
- `bcr-2020-239394-crosswalk.json`
- `bcr-2020-239394-sea-qa.json`

### HTML

- `bcr-2020-239394-sea.html`

### Markdown

- `bcr-2020-239394-reference-task-queue.md`
- `bcr-2020-239394-processing-report.md`

## Governing project sources

ATOM authority order:
1. `literature(1).py`
2. `literature_atoms(1).py`
3. `literature_atom.schema.json`
4. `README(2).md`
5. `example_atom(1).json` (illustrative only)

SEA authority: `summary-evaluation-appraisal-protocol-v4-compact.md`. The v3 HTML is historical/reference material only. The large-source skill was reviewed; this three-page case report is suitable for one complete pass rather than semantic batching.

## Lifecycle action

Move `10 - bcr-2020-239394` from `2 - 10 - Active Literature / 1 - Clinical Medicine & Pharmacy` to `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`, preserving the folder name, after all Drive uploads are verified.

## Exact remaining task

None after verified upload and folder move.
