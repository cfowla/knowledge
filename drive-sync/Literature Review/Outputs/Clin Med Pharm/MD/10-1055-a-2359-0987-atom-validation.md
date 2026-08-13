# ATOM Validation Report — 10-1055-a-2359-0987.pdf

## Source metadata

- Title: *Management of Therapeutic-intensity Unfractionated Heparin: A Narrative Review on Critical Points*
- Source type: Narrative review (secondary source; not primary literature)
- Journal: TH Open 2024;8:e297-e307
- DOI: 10.1055/a-2359-0987
- SHA-256: `ccc3bfa5611226370f959450c316ef183a9f6a481416770ffbc52c4908802ac6`
- Shared publication_id: `d5703d73-955a-536d-b0f3-ccf37b24c889`

## Atom counts by type

- `adverse_event`: 2
- `author_conclusion`: 11
- `conflict_of_interest`: 1
- `limitation`: 2
- `method`: 2
- `other`: 4
- `population_description`: 1
- `qualitative_result`: 17
- `quantitative_result`: 7
- `study_objective`: 1
- **Total:** 48

## Validation

- Pydantic structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

## Extraction limitations

- The governing LiteratureAtom MVP is designed for primary literature, but this source is a narrative review. Quantitative results attributed to cited studies are therefore encoded as statements *reported by the review* and tagged `secondary_reported_result`; they must not be interpreted as primary-study extraction.
- The schema has no dedicated secondary-source or narrative-review result type. This is a schema-fit limitation rather than a source-content gap.
- The review does not report a systematic search strategy, study-selection flow, or formal risk-of-bias assessment, so no such details were invented.
- Atoms retain source-page anchors to the review PDF; primary-study provenance requires separate extraction from each cited publication.
- `review_status` is `needs_review` because extraction was performed by a language model and was not independently human-verified.

## QA status

- Structural model validation: PASS
- Serialization schema validation: PASS
- Atom-kind sufficiency validation: PASS
