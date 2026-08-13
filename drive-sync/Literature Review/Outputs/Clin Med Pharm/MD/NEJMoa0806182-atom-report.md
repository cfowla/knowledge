# ATOM extraction report — NEJMoa0806182

## Source metadata

- **Title:** Benazepril plus Amlodipine or Hydrochlorothiazide for Hypertension in High-Risk Patients
- **Authors:** Kenneth Jamerson; Michael A. Weber; George L. Bakris; Björn Dahlöf; Bertram Pitt; Victor Shi; Allen Hester; Jitendra Gupte; Marjorie Gatlin; Eric J. Velazquez; for the ACCOMPLISH trial investigators
- **Journal / citation:** N Engl J Med. 2008;359:2417-2428
- **Publication date:** December 4, 2008
- **ClinicalTrials.gov identifier reported by source:** NCT00170950
- **Source file:** NEJMoa0806182.pdf
- **Source SHA-256:** `b36e831857c9e6cd7c59f4acc87a79e7523a91e20a2ebfebde070246f13b8c9a`
- **Corresponding/supporting materials:** None listed for this task
- **Publication ID used for all atoms:** `ce4042eb-05d7-4bda-ba85-5b9fb8ad7dd3`
- **Schema version:** 1.0
- **Review status:** needs_review

## Atom counts by type

- `adverse_event`: 21
- `author_conclusion`: 1
- `comparator_description`: 1
- `conflict_of_interest`: 1
- `eligibility_criterion`: 1
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 2
- `method`: 7
- `outcome_definition`: 3
- `population_description`: 5
- `qualitative_result`: 2
- `quantitative_result`: 18
- `study_objective`: 1
- `subgroup_result`: 6

**Total atoms:** 71

## Validation

- Pydantic structural validation errors: **0**
- JSON-schema serialization errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

### Structural errors

```json
[]
```

### Serialization-schema errors

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

## Source consistency findings

- **Coronary revascularization p-value discrepancy:** Table 2 and the Results text report **P=0.04**, whereas Figure 3 displays **P=0.05** for the same hazard ratio (0.86; 95% CI 0.74-1.00). The corresponding atom uses the Table 2 / Results-text value and is tagged to preserve the discrepancy.
- Table 3 reports several serious-event percentages as **<0.1%**. Those thresholds are preserved exactly in canonical statements; the quantitative result uses the exact reported event count rather than inventing a percentage below 0.1%.

## Extraction limitations

- Detailed eligibility criteria are explicitly referenced as published previously rather than reproduced in full; atoms include only criteria stated in this article.
- The investigator appendix and bibliography were inspected for coverage but were not atomized as primary study assertions.
- No supplement, protocol, correction, or other corresponding material was listed for this task.
- This is a model extraction with `needs_review` status; validation confirms structural/schema/sufficiency compliance, not independent human verification of every source interpretation.
