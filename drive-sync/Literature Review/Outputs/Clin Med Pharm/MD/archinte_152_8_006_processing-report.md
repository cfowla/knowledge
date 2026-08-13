# Processing Report — archinte_152_8_006.pdf

## Activated macros

- `@ATOM`
- `@SEA`

## Source

- **Title:** Optimal Therapeutic Level of Heparin Therapy in Patients With Venous Thrombosis
- **Authors:** Russell D. Hull, Gary E. Raskob, David Rosenbloom, Jane Lemaire, Graham F. Pineo, Barry Baylis, Jeffrey S. Ginsberg, Akbar A. Panju, Patrick Brill-Edwards, Rollin Brant
- **Citation:** Arch Intern Med. 1992;152:1589-1595
- **Drive source file:** `archinte_152_8_006.pdf`
- **Raw PDF size:** 1,194,398 bytes
- **SHA-256:** `871fb585e62aab57e69d4414cd3e95a9803cd53d87f1a02f1579df14d0cb00bd`
- **Publication ID:** `ff3f5792-2df6-58de-aa52-3af5f94a97bf`
- **PDF pages:** 7
- **Main-text visual inventory:** 2 tables, 3 figures

## @ATOM result

**Validated atom count:** 49

### Counts by atom kind

- `adverse_event`: 3
- `author_conclusion`: 3
- `eligibility_criterion`: 2
- `funding_disclosure`: 1
- `intervention_description`: 3
- `limitation`: 2
- `method`: 13
- `other`: 3
- `outcome_definition`: 4
- `population_description`: 1
- `qualitative_result`: 3
- `quantitative_result`: 9
- `study_objective`: 2

### Validation

- Pydantic structural validation: **PASS** — 0 errors
- `literature_atom.schema.json` validation: **PASS** — 0 errors across all 49 serialized atoms
- Atom-kind sufficiency validation: **PASS** — 0 errors, 0 warnings
- Review status of generated atoms: `extracted` (not human-verified)

### Schema gaps

- The current QuantitativeResult shape does not represent repeated multi-timepoint mean±SD series cleanly; two directly reported time-series assertions are serialized as atom_kind=other with schema_gap_multitimepoint tags.
- The current schema has no dedicated randomized-regimen object; regimen details are represented through exposure descriptors and method atoms.

### Extraction limitations

- The PDF is a 1992 journal scan/text reconstruction; source anchors use printed journal pages and table/figure labels rather than sentence-level character offsets.
- Detailed baseline characteristics were referenced by the article as comparable but were not tabulated in the retrieved paper; they were not invented.
- Bleeding criteria were referenced to prior publications rather than fully reproduced in this paper, so the atom preserves the reported classification approach without reconstructing missing definitions.
- No conflict-of-interest or data-availability statement was identified in the source; no atom was fabricated for absent reporting.

## @SEA result

### Coverage manifest

- **Source type:** Original investigation; randomized double-blind clinical trial / prescriptive heparin quality-assurance study
- **Coverage decision:** All substantive sections and all five main-text visual objects are represented. References are retained only as source context and are not summarized citation-by-citation.
- **Figures reconciled:** 3/3
- **Tables reconciled:** 2/2
- **Algorithms/workflows:** Table 1 titration nomogram plus monitoring/restart logic
- **Appendices/supplements:** none present
- **Bibliography:** not condensed citation-by-citation; treated as provenance infrastructure

### Visual strategy

- Table 1: structured reconstruction
- Table 2: structured reconstruction
- Figure 1: embedded source crop + structured interpretation
- Figure 2: embedded source crop + structured interpretation
- Figure 3: embedded source crop + structured interpretation

### SEA appraisal summary

- **Verdict:** Read first — historical/foundational heparin protocol evidence
- **Relevance:** 10/10
- **Novelty:** 7/10
- **Method strength:** 7/10
- **Evidence strength:** 6/10
- **External validity:** 4/10
- **Implementation value:** 8/10

The principal appraisal boundary is that the paper supports the feasibility and effectiveness of a prescriptive, assay-calibrated UFH protocol, but the comparison of patients with versus without persistent supratherapeutic APTT was not randomized. High APTT also reflected warfarin effects and clock-time variation. Therefore, the paper does **not** establish that deliberately higher heparin exposure is safe.

### SEA QA

- Raw PDF remained available for the SEA pass: **PASS**
- Exact source title/citation matched: **PASS**
- All TOC anchors resolve: **PASS**
- All main-text figures/tables reconciled: **PASS**
- Embedded visual count: 3
- Internal chat/file citation syntax absent from HTML: **PASS**
- TODO/placeholder/planning language absent: **PASS**
- Self-contained HTML with embedded CSS/images: **PASS**
- External verification: **not used** (`@VERIFY` was not activated)

## Final deliverables

- `archinte_152_8_006_atoms.json`
- `archinte_152_8_006_sea.html`
- `archinte_152_8_006_processing-report.md`
