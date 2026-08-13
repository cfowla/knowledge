# NEJMoa1409077 — LiteratureAtom Validation Report

## Source metadata

- **Primary article:** McMurray JJV, Packer M, Desai AS, et al. *Angiotensin–Neprilysin Inhibition versus Enalapril in Heart Failure.* N Engl J Med. 2014;371:993–1004. DOI: 10.1056/NEJMoa1409077.
- **Trial:** PARADIGM-HF; ClinicalTrials.gov NCT01035255.
- **Supporting material:** `NEJMoa1409077-supplemental.pdf`; `NEJMoa1409077-protocol.pdf` (original protocol, amended protocol v04, and statistical analysis plan contained in the protocol PDF).
- **Publication ID shared by all atoms:** `e5dc276a-3617-5f97-9a0f-bc548a8b7ed7`
- **Extraction timestamp:** `2026-08-12T12:09:08+00:00`
- **Primary SHA-256:** `6342b629cdede0578cd1adcba1b67ba023f3a97869b4b70e1e1ae38e87cd973a`
- **Supplement SHA-256:** `33bb0e9cbaa8f29dba1ea3cca3b75ae718ed8a554946e20140bbd72c3ee12d69`
- **Protocol SHA-256:** `bd0a7ea3d45df4a64ba7d0175dd62cfc2f6f18dd57d6d675ffbdb4b24cbc2ccc`

## Atom counts

- **Total atoms:** 39
- `adverse_event`: 6
- `author_conclusion`: 1
- `comparator_description`: 1
- `eligibility_criterion`: 5
- `funding_disclosure`: 1
- `intervention_description`: 1
- `method`: 6
- `outcome_definition`: 2
- `population_description`: 2
- `quantitative_result`: 12
- `study_objective`: 1
- `subgroup_result`: 1

### Assertion origin
- `calculated_from_reported_data`: 5
- `directly_reported`: 5
- `normalized_from_source`: 29

## Validation

- **Pydantic structural validation:** PASS for all 39 atoms (objects were instantiated with `LiteratureAtom`).
- **Atom-kind sufficiency validation:** PASS; 0 error(s), 0 warning(s).
- No sufficiency errors or warnings.

## Extraction limitations

- The ATOM set records independently reviewable assertions from the primary article and uses protocol/supplement material only when it clarifies the same trial’s design or reported ancillary results.
- The open-label/single-blind run-in before randomization enriches the randomized population for patients able to tolerate target-dose enalapril and LCZ696. This is an appraisal/generalizability issue and was not converted into a reported efficacy result.
- The protocol PDF contains the original 2009 protocol, amended protocol v04 (2013, incorporating amendments 1–3), and statistical-analysis-plan material. Eligibility atoms use the amended criteria when the article documents the amendment.
- The supplementary appendix uses a safety-set denominator (N=8432) that differs from the main intention-to-treat efficacy population (N=8399). The supplementary serious-adverse-event atom preserves the supplement’s own denominators rather than reconciling them by inference.
- Adverse-event atoms whose effect measure is an absolute risk difference are explicitly labeled `calculated_from_reported_data`; the underlying event counts/rates and reported P values remain in the quantitative result context.
- No unreported study details were imputed, and appraisal judgments were not encoded as directly reported data.

## Output

- Validated atom JSON: `NEJMoa1409077-atoms.json`
