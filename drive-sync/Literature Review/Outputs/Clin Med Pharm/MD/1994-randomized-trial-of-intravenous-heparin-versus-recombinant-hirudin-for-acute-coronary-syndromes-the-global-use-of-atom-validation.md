# ATOM Extraction and Validation Report

**Source:** Randomized Trial of Intravenous Heparin Versus Recombinant Hirudin for Acute Coronary Syndromes  
**Group author:** The Global Use of Strategies to Open Occluded Coronary Arteries (GUSTO) IIa Investigators  
**Citation:** Circulation. 1994;90:1631-1637.  
**Publication ID:** `9269f7a1-3f24-424f-9c72-992b038bad06`  
**Input SHA-256:** `37401609cd183e4ccb1f8945c65a700ebeaa1b4e8836148432e2d8024133f774`

## Atom counts

Total atoms: **39**

- `adverse_event`: 1
- `author_conclusion`: 8
- `comparator_description`: 1
- `conflict_of_interest`: 1
- `eligibility_criterion`: 2
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 2
- `method`: 7
- `outcome_definition`: 2
- `population_description`: 1
- `qualitative_result`: 3
- `quantitative_result`: 1
- `study_objective`: 1
- `subgroup_result`: 7

## Validation

- Pydantic structural validation: **PASS**
- LiteratureAtom sufficiency validation: **PASS**
- Structural errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0


## Extraction limitations

- The publication is an early safety report; final efficacy and detailed secondary outcomes were explicitly deferred.
- The trial was stopped early after 2,564 of 12,000 planned participants, limiting efficacy inference and precision.
- No study details were invented; unreported efficacy outcomes were not atomized.
- Discussion statements based on prior/pilot literature were not converted into current-trial quantitative results.

## Coverage note

The full 7-page PDF was inspected. Main substantive sections were abstract/background, methods, results, discussion, three main-text tables, and acknowledgments. The investigator appendix and bibliography were treated as provenance/context rather than evidence-atom targets, except the funding disclosure. All three main-text tables were reconciled during extraction and SEA.
