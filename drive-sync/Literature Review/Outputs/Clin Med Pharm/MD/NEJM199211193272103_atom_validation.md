# ATOM Validation Report — NEJM199211193272103

- Source: **Acenocoumarol and Heparin Compared with Acenocoumarol Alone in the Initial Treatment of Proximal-Vein Thrombosis**
- Citation: N Engl J Med. 1992;327:1485-1489.
- Publication ID: `d0771144-cf33-52f8-95db-ec8b97cefd36`
- Input SHA-256: `a4fc31d06812e71ebb7a451ec515590a57583d8c200df91a1f54543608bb9c84`
- Extraction run: `NEJM199211193272103-atom-v1`
- Atoms extracted: **46**
- Structural errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

## Atom counts by kind

- `adverse_event`: 3
- `author_conclusion`: 2
- `comparator_description`: 1
- `eligibility_criterion`: 10
- `funding_disclosure`: 2
- `intervention_description`: 1
- `method`: 9
- `outcome_definition`: 3
- `population_description`: 2
- `qualitative_result`: 4
- `quantitative_result`: 8
- `study_objective`: 1

## Assertion origins

- `calculated_from_reported_data`: 4
- `normalized_from_source`: 42

## Structural validation

PASS — every serialized atom round-tripped through the governing `LiteratureAtom` Pydantic model.

## Sufficiency validation

PASS — no atom-kind sufficiency errors were returned by `validate_literature_atom_sufficiency`.

## Extraction limitations

- The PDF text layer contained only the NEJM download footer; rendered page images were used as the authoritative source.
- The original article did not report confidence intervals for its main event-rate comparisons.
- Calculated risk summaries are clearly labeled `calculated_from_reported_data`; author-reported and calculated assertions were not merged.
- No conflict-of-interest or data-availability statement was identified in the source.

## Coverage

- Pages inspected: 5/5
- Main-text tables reconciled: Table 1 and Table 2
- Main-text figures reconciled: Figure 1
- Supplement/appendix: none identified
- References were treated as provenance infrastructure and were not atomized.
