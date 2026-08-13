# Processing report — Bovill et al. TIMI II hemorrhage analysis

## Source identity

- Requested file: `bovill-et-al-2008-hemorrhagic-events-during-therapy-with-recombinant-tissue-type-plasminogen-activator-heparin-and.pdf`
- Exact paper title: **Hemorrhagic Events during Therapy with Recombinant Tissue-Type Plasminogen Activator, Heparin, and Aspirin for Acute Myocardial Infarction: Results of the Thrombolysis in Myocardial Infarction (TIMI), Phase II Trial**
- Journal: *Annals of Internal Medicine* 1991;115(4):256-265
- DOI: 10.7326/0003-4819-115-4-256
- PMID: 1906692
- PDF pages: 10
- SHA-256: `5c8c59b031956f632d91cdd7ee5aa9b3ffdbb9220de3f4726d1b9e31accbc92a`
- **Filename discrepancy:** the Drive filename contains `2008`, while the PDF itself is a 1991 publication.

## @ATOM result

- Publication ID: `4969bfb5-0693-4185-8fb6-9727f5dc92b1`
- Extraction run: `bovill-timi2-1991-atom-v1`
- Total atoms: **76**
- Structural validation: **PASS**
- Sufficiency validation: **PASS**
- Sufficiency warnings: **0**

### Atom counts by type

- `adverse_event`: 9
- `author_conclusion`: 3
- `comparator_description`: 1
- `eligibility_criterion`: 2
- `funding_disclosure`: 1
- `intervention_description`: 5
- `limitation`: 3
- `method`: 8
- `outcome_definition`: 3
- `population_description`: 1
- `quantitative_result`: 13
- `study_objective`: 1
- `subgroup_result`: 26

### Validation errors

- Structural errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0

## Coverage manifest

- Sections/headings: 16 mapped
- Tables: 6/6 reconciled (Tables 1-6)
- Figures: 2/2 reconciled (Figures 1-2)
- Algorithms/workflows: none
- Supplements/appendices: none in the retrieved PDF
- References: omitted from atomization as bibliography/provenance infrastructure

## Extraction limitations

1. Language-model extraction has not received human verification; atoms are marked `needs_review`.
2. rt-PA dose was changed sequentially from 150 mg to 100 mg, not randomized; dose comparisons are therefore vulnerable to era/protocol confounding, including concurrent eligibility and aspirin-timing changes described by the authors.
3. The paper contains many descriptive site-level bleeding cells; extraction prioritized independently reviewable results relevant to hemorrhage mechanisms, heparin/APTT, patient risk factors, invasive procedures, and rt-PA dose rather than generating a separate atom for every table cell.
4. Key numeric table values were checked against rendered PDF pages because the text layer occasionally substituted glyphs.

## @SEA QA

- Coverage manifest built before final synthesis: PASS
- Main-text tables reconciled: PASS (6/6)
- Main-text figures reconciled: PASS (2/2)
- Source claims separated from appraisal: PASS
- Final scores assigned after extraction/reconciliation: PASS
- Single-file HTML with embedded CSS and no remote assets: PASS
- Internal chat/file citation syntax in HTML: none
- TODO/placeholders/planning language: none expected; mechanical check performed after generation

## External metadata verification

DOI and PMID were verified against PubMed metadata. The scientific extraction and appraisal are grounded in the retrieved PDF.
