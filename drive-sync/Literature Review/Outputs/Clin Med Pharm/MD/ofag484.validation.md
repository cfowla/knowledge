# ATOM validation report — ofag484.pdf

## Source metadata

- **Title:** Impact of changes in chlamydia treatment guidelines on recurrent/persistent rectal Chlamydia trachomatis infections
- **Journal:** Open Forum Infectious Diseases
- **DOI:** 10.1093/ofid/ofag484
- **Source file:** ofag484.pdf
- **Source type:** Major Article; controlled interrupted time-series observational/quasi-experimental study
- **Source span:** 16-page accepted/advance article PDF
- **Publication year in source:** 2026
- **Publication ID:** 260a0671-78fe-53c6-9151-a7ad515b844e
- **SHA-256:** `bc9e5baeb4f6454907e5aa2f2ca78858f6578a22760205adaa13b3dc00c5e227`
- **Extraction run:** `ofag484-atom-v1`

## Atom counts

- **Total atoms:** 117

- `author_conclusion`: 1
- `comparator_description`: 1
- `conflict_of_interest`: 2
- `data_availability`: 1
- `eligibility_criterion`: 2
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 5
- `method`: 8
- `other`: 1
- `outcome_definition`: 2
- `population_description`: 2
- `qualitative_result`: 10
- `quantitative_result`: 78
- `study_objective`: 2

### Assertion origin counts

- `directly_reported`: 25
- `extractor_inference`: 1
- `normalized_from_source`: 91

## Validation status

- **Pydantic structural errors:** 0
- **JSON Schema serialization errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0
- **Overall:** PASS

## Extraction limitations

- The PDF is an accepted/advance article containing one main-text figure and four main-text tables; no supplement was included in the retrieved PDF, although the manuscript references Supplemental Tables 1-4.
- The study uses an EHR-defined recurrent/persistent outcome that combines reinfection and persistence; atoms preserve that source terminology rather than resolving the distinction.
- Table 1 contains extensive descriptive cells; atoms capture the study-defining populations and the baseline differences that the authors identify as analytically important rather than atomizing every descriptive cell.
- Table 2, all displayed Table 3 sensitivity estimates, and all displayed Table 4 odds-ratio estimates were atomized individually.
- One internal manuscript inconsistency is preserved as an extractor-inference limitation atom: the Discussion assigns the 16.9% relative trend reduction to a different period contrast than Table 2 and the Results.
- Exact online publication date was not stated in the retrieved PDF; the file identifies the article as © 2026 and the download watermark is dated 11 August 2026.

## SEA coverage manifest

- **Sections/headings:** structured abstract; Introduction; Methods (design/setting/population, cITS definitions/analyses, azithromycin-correlate analysis); Results (primary impact, sensitivity analyses, azithromycin correlates); Discussion; declarations; references.
- **Main-text figures:** 1 (Figure 1) — embedded source crop in HTML.
- **Main-text tables:** 4 (Tables 1-4) — all represented as structured blocks/tables in HTML.
- **Algorithms/workflows:** none.
- **Supplements:** Supplemental Tables 1-4 referenced but absent from retrieved PDF.
- **Omissions:** bibliography not condensed citation-by-citation; unavailable supplements not reconstructed.

## SEA QA

- `file_nontrivial`: PASS
- `title_matches`: PASS
- `all_toc_anchors_resolve`: PASS
- `figure_count`: PASS
- `main_table_sections`: PASS
- `ratings_present`: PASS
- `provenance_present`: PASS
- `no_internal_citations`: PASS
- `no_placeholders`: PASS
- `self_contained_figure`: PASS
- **Overall SEA QA:** PASS
