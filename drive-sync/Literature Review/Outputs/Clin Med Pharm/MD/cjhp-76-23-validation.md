# cjhp-76-23 — ATOM + SEA validation report

## Source metadata

- Title: Comparison of a Fully Weight-Based Protocol with a Non–Weight-Based Dosage Titration Protocol for IV Unfractionated Heparin: A Before-and-After Study
- Journal: Canadian Journal of Hospital Pharmacy 2023;76(1):23-28
- DOI: 10.4212/cjhp.3265
- Retrieved file: `cjhp-76-23.pdf`
- SHA-256: `3f2af2f8e6517e700547ca70fb384cab20e6485b7f13bdc46a2ee7066b828203`
- Shared publication ID: `de77532b-37a2-5788-afc2-d38b5b7b0d28`

## ATOM validation

- Extracted atoms: **57**
- Structural/Pydantic errors: **0**
- JSON-schema errors: **0** (included in structural validation pass)
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

### Atom counts by kind

- `author_conclusion`: 4
- `comparator_description`: 2
- `conflict_of_interest`: 2
- `eligibility_criterion`: 7
- `funding_disclosure`: 1
- `intervention_description`: 4
- `limitation`: 4
- `method`: 12
- `outcome_definition`: 3
- `population_description`: 4
- `quantitative_result`: 6
- `study_objective`: 2
- `subgroup_result`: 6

### Extraction limitations

- The article's complete UFH nomograms are referenced as Appendices 1-4 but are not embedded in the retrieved PDF; exact titration tables were not invented.
- Bibliographic references were not atomized as primary-study results.
- The low-target after-era protocol changed both titration method and initial dose, so atoms preserve those as distinct source facts rather than treating the secondary result as an isolated titration effect.
- All model-extracted atoms remain `needs_review` pending human verification.

## SEA coverage manifest

- Sections: Abstract; Introduction; Methods; Statistical Analysis; Results; Discussion; Conclusion; disclosures/references.
- Main-text figures: **2/2 reconciled**.
- Main-text tables: **3/3 reconciled**.
- Visual strategy: all five objects represented as structured blocks/tables in the HTML; no screenshots embedded.
- Appendices: 1-4 referenced externally, absent from retrieved PDF, omitted with reason.
- Bibliography: omitted from condensation as provenance infrastructure.
- Noted source inconsistency: Figure 2 x-axis categories are labelled 1-6 while the Results text reports an adjustment range of 0-5.

## SEA mechanical QA

- HTML bytes: **25341**
- TOC anchors unresolved: **0**
- Internal citation/tool markers found: **0**
- Visual reconciliation: **5/5**
- QA verdict: **PASS**

## External information

None used. The outputs are grounded in the retrieved PDF plus the governing ATOM/SEA project sources.
