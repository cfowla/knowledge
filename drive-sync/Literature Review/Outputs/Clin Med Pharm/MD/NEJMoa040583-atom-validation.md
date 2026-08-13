# ATOM Validation Report — NEJMoa040583

## Source metadata
- Primary source: `NEJMoa040583.pdf`
- Supporting correction: `NEJMoa040583-correction.pdf`
- Title: Intensive versus Moderate Lipid Lowering with Statins after Acute Coronary Syndromes
- Citation: N Engl J Med 2004;350:1495-1504
- Publication ID: `6bb4eba6-cc50-5234-9e8f-640d3af96559`
- Primary SHA-256: `5affe0a40099c38079e40f10e641a2593a2485b8c5d1f6590a5c2d30cb7a0e94`
- Correction SHA-256: `7024935fa65834facc3ff485babc72c35a2c4eaef9fc2a16a7a9031525b2c64b`
- Extraction timestamp: `2026-08-12T12:43:21.697103+00:00`

## Atom counts by type
- `adverse_event`: 5
- `author_conclusion`: 2
- `conflict_of_interest`: 3
- `eligibility_criterion`: 6
- `funding_disclosure`: 1
- `limitation`: 3
- `method`: 8
- `other`: 1
- `outcome_definition`: 4
- `population_description`: 3
- `qualitative_result`: 1
- `quantitative_result`: 17
- `study_objective`: 1
- `subgroup_result`: 4
- **Total atoms:** 59

## Validation status
- Pydantic structural validation: **PASS** for 59/59 atoms
- JSON Schema validation: **PASS** for 59/59 atoms
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

No sufficiency issues were returned by `validate_literature_atom_sufficiency`.

## Correction handling
- The correction was treated as supporting source material for the same study identity, not as a separate trial.
- It corrects only several Figure 2 numbers-at-risk values. The correction does not state that the plotted event curves, primary endpoint rates, or reported treatment-effect estimate changed.
- A dedicated `other` atom preserves the corrected numbers at risk with provenance anchored to the correction PDF.

## Extraction limitations
- The atom set prioritizes independently reviewable study design, eligibility, endpoint, efficacy, safety, subgroup, interpretation, funding, conflict-of-interest, and erratum assertions. It does not atomize every row of Table 1 or every subgroup row in Figure 5 when the paper itself summarizes the pattern at a higher level.
- Numeric values were recorded only when they were recoverable from the supplied primary PDF or correction. No missing study details were imputed.
- Canonical statements are normalized paraphrases unless otherwise indicated; they are therefore labeled `normalized_from_source` rather than represented as verbatim quotations.
- Human verification remains appropriate before downstream clinical or evidence-synthesis use; all atoms are marked `needs_review`.

