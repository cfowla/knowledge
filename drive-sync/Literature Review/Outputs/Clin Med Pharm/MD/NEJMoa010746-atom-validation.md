# NEJMoa010746 — ATOM Validation Report

## Source metadata

- **Primary:** `NEJMoa010746.pdf`
- **Title:** Effects of Clopidogrel in Addition to Aspirin in Patients with Acute Coronary Syndromes without ST-Segment Elevation
- **Source:** N Engl J Med. 2001;345:494-502.
- **Study:** CURE (Clopidogrel in Unstable Angina to Prevent Recurrent Events)
- **Design:** Randomized, double-blind, placebo-controlled, multicenter trial
- **Randomized:** 12,562 patients
- **Publication ID:** `cdae3cfd-1b1b-5a90-85ea-a8851b496b6f`
- **Primary SHA-256:** `44e80cda7d455428b7f010c4136d466f4bc3608d1615088644d097805a6dce3c`
- **Correction 1 SHA-256:** `2b623385fc3e61ec8b5dbc858bab05c2a2beb9d907479561f81d9ce8b33f4859`
- **Correction 2 SHA-256:** `68c97ccdc6057e209178c756f0c0ce274379db8ff4df5e6d749c45a6498a818f`

## Supporting corrections incorporated

- `NEJMoa010746-correction1.pdf`: corrected abstract life-threatening bleeding to 2.2% vs 1.8%; corrected manuscript-writing-committee name to Keith A.A. Fox; corrected overall CABG bleeding rates to 8.3% vs 6.6% (not 1.3% vs 1.1%).
- `NEJMoa010746-correction2.pdf`: corrected investigator listing from B. Pontillo to D. Pontillo; this does not alter clinical outcome atoms.

## Atom counts by type

- `adverse_event`: 10
- `author_conclusion`: 1
- `comparator_description`: 1
- `conflict_of_interest`: 1
- `eligibility_criterion`: 2
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 3
- `method`: 6
- `outcome_definition`: 3
- `population_description`: 3
- `qualitative_result`: 1
- `quantitative_result`: 16
- `study_objective`: 1
- `subgroup_result`: 2

- **Total validated atoms:** 52

## Structural validation

- **Status:** PASS
- **Errors:** 0

## Sufficiency validation

- **Status:** PASS
- **Errors:** 0
- **Warnings:** 0

## Extraction limitations

- Atomization prioritizes independently reviewable design, efficacy, safety, adherence, limitation, funding, and conflict-of-interest assertions; the investigator roster and bibliography were not atomized.
- The current schema has no dedicated erratum/correction object. Corrected clinical values are represented using the same publication identity and correction-specific provenance/tags.
- `NEJMoa010746-correction2.pdf` changes an investigator name only; it is recorded in source handling but does not generate a clinical result atom.
- No external sources were used to update the trial to current practice; this extraction is grounded in the primary article plus the two supplied corrections.

## Output

- Validated atom JSON: `NEJMoa010746-atoms.json`