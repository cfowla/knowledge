# Processing Report — raschke-et-al-2000-the-weight-based-heparin-dosing-nomogram-compared-with-a-standard-care-nomogram.pdf

## Activated macros

- `@ATOM`
- `@SEA`

## Source

- **Title:** The Weight-based Heparin Dosing Nomogram Compared with a "Standard Care" Nomogram: A Randomized Controlled Trial
- **Authors:** Robert A. Raschke, Brendan M. Reilly, James R. Guidry, Joseph R. Fontana, Sandhya Srinivas
- **Citation:** Ann Intern Med. 1993;119:874-881
- **Drive source file:** `raschke-et-al-2000-the-weight-based-heparin-dosing-nomogram-compared-with-a-standard-care-nomogram.pdf`
- **Drive file ID:** `1MQf6r5F_HlZ-FGS3EqrPdf-2Y6rv6sx5`
- **Verified source folder:** `TBR/Lit Cluster: Heparin Deep Dive` (matched within folder `Lit Cluster: Heparin Deep Dive`)
- **Raw PDF size:** 1,600,649 bytes
- **SHA-256:** `fde750e6c883f4e0142b41d6a7feb050abcab2194b1bc99f5be149f36b57dd42`
- **Publication ID:** `4cdea982-d8eb-587b-9d4c-9b213ea304c3`
- **PDF pages:** 8
- **Main-text visual inventory:** 5 tables, 3 figures
- **Source filename note:** the Drive filename contains `2000`, but the retrieved article is dated 1 November 1993 and cites Ann Intern Med. 1993;119:874-881.

## @ATOM result

**Validated atom count:** 82

### Counts by atom kind

- `adverse_event`: 3
- `author_conclusion`: 3
- `comparator_description`: 1
- `eligibility_criterion`: 9
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 5
- `method`: 14
- `other`: 1
- `outcome_definition`: 6
- `population_description`: 4
- `qualitative_result`: 6
- `quantitative_result`: 25
- `study_objective`: 1
- `subgroup_result`: 2

### Validation

- Pydantic structural validation using `literature.py`: **PASS** — 0 errors
- `literature_atom.schema.json` validation: **PASS** — 0 errors across all 82 serialized atoms
- Atom-kind sufficiency validation using `literature_atoms.py`: **PASS** — 0 errors, 0 warnings
- Review status of generated atoms: `extracted` (not human-verified)

### Schema gaps

- The current `QuantitativeResult` contract requires an effect estimate. The two prespecified subgroup time-to-event analyses and the Cox analysis of dose-per-kilogram reported significance values but not hazard ratios/effect estimates; these were preserved as `qualitative_result` atoms rather than inventing numerical estimates.
- The current schema has no dedicated full nomogram/decision-table object. The two titration algorithms are represented as intervention/comparator descriptions with source-table anchors.
- The proposed post-study order sheet is a compound workflow rather than a single exposure/result object; it is represented as `other` with an explicit Figure 3 anchor and `post_study`/`implementation_workflow` tags.

### Extraction limitations and consistency findings

- Source anchors use printed journal pages plus table/figure labels rather than sentence-level character offsets.
- Table 4 reports bleeding denominators of 52 standard-care and 63 weight-based patients despite randomized group sizes of 53 and 62. The atom set preserves the table values and does not silently reconcile the inconsistency.
- The clinical recurrence result is preserved as reported, including the sensitivity analysis excluding two recurrences after warfarin discontinuation; appraisal of causal attribution is not encoded as reported data.
- No conflict-of-interest or data-availability statement was identified in the retrieved article; no atom was fabricated for absent reporting.
- DOI was not reported in the retrieved PDF and was not externally inferred.

## @SEA result

### Coverage manifest

- **Source type:** Original investigation; randomized controlled trial
- **Coverage decision:** all substantive sections and all 8 main-text visual objects are represented. References are treated as provenance infrastructure and are not summarized citation-by-citation.
- **Figures reconciled:** 3/3
- **Tables reconciled:** 5/5
- **Algorithms/workflows:** Table 1 standard-care fixed-unit titration; Table 2 actual-body-weight titration; Figure 3 proposed operational order sheet
- **Appendices/supplements:** none present
- **Bibliography:** not condensed citation-by-citation

### Visual strategy

- Tables 1-5: structured reconstruction
- Figure 1: embedded source crop + structured interpretation
- Figure 2: embedded source crop + structured interpretation
- Figure 3: embedded source crop + structured interpretation

### SEA appraisal summary

- **Verdict:** Read first — foundational/historical UFH protocol evidence
- **Relevance:** 10/10
- **Novelty:** 9/10
- **Method strength:** 7/10
- **Evidence strength:** 7/10
- **External validity:** 5/10
- **Implementation value:** 9/10

The trial provides strong source-level evidence that the studied actual-body-weight nomogram achieved earlier APTT target attainment than the fixed-dose standard-care nomogram. Its strongest endpoints are laboratory surrogates. Major bleeding was too uncommon for robust comparative safety inference, and the recurrent-VTE result is limited by sparse events, incomplete follow-up, unmonitored outpatient anticoagulation, and warfarin discontinuation in two standard-care recurrences.

A key implementation boundary is assay dependence: the authors explicitly tied generalizability of the APTT ranges to reagent/system characteristics. Figure 3 is also a **proposed post-study order sheet**, not a pure trial-protocol reproduction; it includes warfarin starting on the second day, whereas warfarin was withheld during the trial's first 48 hours.

### SEA QA

- Raw PDF remained available for the SEA pass: **PASS**
- Exact source title/citation matched: **PASS**
- Coverage manifest created before HTML drafting: **PASS**
- All TOC anchors resolve: **PASS**
- All main-text figures/tables/workflows reconciled: **PASS**
- Embedded visual count: 3
- Structured table count in HTML: 6 (PICO table + source Tables 1-5)
- Internal chat/file citation syntax absent from HTML: **PASS**
- TODO/placeholder/planning language absent: **PASS**
- Self-contained HTML with embedded CSS/images: **PASS**
- External verification: **not used** (`@VERIFY` was not activated)

## Final deliverables

- `raschke-et-al-2000-the-weight-based-heparin-dosing-nomogram-compared-with-a-standard-care-nomogram_atoms.json`
- `raschke-et-al-2000-the-weight-based-heparin-dosing-nomogram-compared-with-a-standard-care-nomogram_sea.html`
- `raschke-et-al-2000-the-weight-based-heparin-dosing-nomogram-compared-with-a-standard-care-nomogram_processing-report.md`
