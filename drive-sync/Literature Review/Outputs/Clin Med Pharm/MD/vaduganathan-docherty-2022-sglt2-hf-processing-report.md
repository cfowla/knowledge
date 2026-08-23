# Processing report — Vaduganathan Docherty 2022

## Source

- **Title:** SGLT2 inhibitors in patients with heart failure: a comprehensive meta-analysis of five randomised controlled trials
- **Journal:** The Lancet. 2022;400:757–767.
- **DOI:** `10.1016/S0140-6736(22)01429-5`
- **PMID:** `36041474`
- **Version note:** evaluated PDF states corrected online version first appeared January 12, 2023.
- **Main PDF SHA-256:** `4bed77850718cfcf7995ab49ba1b19834274158265a697e3e0f3faab0429d98a`
- **Supplement PDF SHA-256:** `185499695a3d4d034831a20e4b8924426d5f0913172a48189896ca3d923df017`

## ATOM

- Shared publication ID: `3fea5931-bcbb-47d6-99e3-9d9597f1a767`
- LiteratureAtoms: **108**
- Counts by kind: `{"adverse_event": 10, "author_conclusion": 1, "conflict_of_interest": 1, "data_availability": 1, "funding_disclosure": 1, "intervention_description": 3, "limitation": 9, "method": 12, "other": 1, "outcome_definition": 2, "population_description": 1, "qualitative_result": 16, "quantitative_result": 14, "study_objective": 1, "subgroup_result": 35}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS** (0 errors)
- Sufficiency validation: **PASS** (0 errors, 0 warnings)
- Exact duplicate review: **0 duplicates**

## SEA

- Hierarchical source map and full supplied supplement reconciled.
- Main coverage: **2 figures + 2 tables**.
- Supplement coverage: **4 figures + 2 tables**.
- SEA QA: **PASS**.
- Verdict: **Read first**.

## Reference list

- Printed reference entries captured: **25**.
- Source numbering is preserved. The evaluated PDF skips reference number **18**.

## Source consistency / interpretation flags

1. The PDF contains a correction notice: corrected online version first appeared January 12, 2023.
2. The supportive five-trial extension was post hoc and had no assigned alpha; it is not the same inferential tier as the prespecified DELIVER + EMPEROR-Preserved meta-analysis.
3. DELIVER and EMPEROR-Preserved safety-event definitions and capture windows differed; safety events were deliberately not directly compared or meta-analysed.
4. The printed bibliography skips reference 18.
5. Subgroup interaction analyses were not multiplicity-corrected and can be underpowered.

## Schema gap

The current LiteratureAtom model has no dedicated systematic-review/meta-analysis result kind. Pooled meta-analytic findings were represented with `quantitative_result` / `subgroup_result` and descriptive tags without changing the schema.

## Output files

### JSON
- `vaduganathan-docherty-2022-sglt2-hf-atoms.json`
- `vaduganathan-docherty-2022-sglt2-hf-validation.json`
- `vaduganathan-docherty-2022-sglt2-hf-coverage.json`
- `vaduganathan-docherty-2022-sglt2-hf-crosswalk.json`
- `vaduganathan-docherty-2022-sglt2-hf-sea-qa.json`

### HTML
- `vaduganathan-docherty-2022-sglt2-hf-sea.html`

### Markdown
- `vaduganathan-docherty-2022-sglt2-hf-references.md`
- `vaduganathan-docherty-2022-sglt2-hf-processing-report.md`
