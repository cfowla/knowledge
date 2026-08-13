# NEJMoa021328 — LiteratureAtom extraction and validation report

## Source metadata

- **Primary article:** *A Comparison of Rate Control and Rhythm Control in Patients with Atrial Fibrillation*
- **Group author:** The Atrial Fibrillation Follow-up Investigation of Rhythm Management (AFFIRM) Investigators
- **Journal:** New England Journal of Medicine
- **Citation in source:** N Engl J Med. 2002;347:1825-1833.
- **Source file:** `NEJMoa021328.pdf`
- **Source SHA-256:** `4dd5f648d587f918ff84c45a02c6bdb9943e921f7b27ba02c9d3da0810276653`
- **Supporting materials:** None supplied/listed for this paper.
- **Publication ID:** `3fd46778-2680-5eab-b26c-01bc659a51e6`
- **Extraction run:** `NEJMoa021328-primary-v1`

## Atom counts

- **Total validated atoms:** 42
- `adverse_event`: 6
- `author_conclusion`: 2
- `comparator_description`: 1
- `conflict_of_interest`: 1
- `eligibility_criterion`: 1
- `funding_disclosure`: 2
- `intervention_description`: 1
- `limitation`: 4
- `method`: 4
- `outcome_definition`: 2
- `population_description`: 2
- `qualitative_result`: 2
- `quantitative_result`: 12
- `study_objective`: 1
- `subgroup_result`: 1

## Validation

- **Structural/Pydantic errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0

### Structural errors

```json
[]
```

### Sufficiency errors

```json
[]
```

### Sufficiency warnings

```json
[]
```

## Extraction limitations

- The extraction is based on the primary nine-page journal article only; no corresponding supplement or protocol was listed for this task.
- Figure 2 presents subgroup hazard ratios graphically without printing numeric point estimates and confidence intervals for each subgroup. The atom preserves the authors' reported subgroup interpretation and the overall hazard ratio rather than reverse-engineering numeric values from plot geometry.
- Several treatment details refer to protocol publications cited by the article. Those external protocol papers were not treated as source evidence for this extraction.
- One crossover-related limitation is explicitly marked `extractor_inference`; it is appraisal derived from reported crossover data, not a statement labeled by the authors as a limitation.
- Current-practice implications are not encoded as reported LiteratureAtoms; they belong in SEA appraisal/context.
