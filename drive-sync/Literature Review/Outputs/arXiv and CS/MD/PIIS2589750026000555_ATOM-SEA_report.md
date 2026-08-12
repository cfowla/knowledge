# PIIS2589750026000555 — ATOM + SEA processing report

## Source metadata

- **Title:** Prediction of structural glaucoma progression from baseline fundus photographs using deep learning: a retrospective multicentre study
- **Source file:** `PIIS2589750026000555.pdf`
- **Journal/year:** The Lancet Digital Health, 2026
- **DOI:** `10.1016/j.landig.2026.101032`
- **Design:** retrospective multicentre deep-learning development/external-validation study
- **Pages:** 12
- **PDF bytes:** 5,891,899
- **SHA-256:** `aad84bc2471f0c3529fe6de472b67c3a125855e45812b1efa318e13765e517bc`
- **Publication ID:** `70e72d9a-22f0-54d3-8ea9-8238335590a6`

## ATOM extraction

- **Total validated atoms:** 68
- **Structural/Pydantic validation:** PASS
- **JSON Schema contract validation:** PASS
- **Sufficiency validation:** PASS
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0

### Atom counts by kind

| Atom kind | Count |
|---|---:|
| `author_conclusion` | 4 |
| `conflict_of_interest` | 1 |
| `data_availability` | 2 |
| `eligibility_criterion` | 2 |
| `funding_disclosure` | 2 |
| `limitation` | 6 |
| `method` | 15 |
| `population_description` | 7 |
| `qualitative_result` | 2 |
| `quantitative_result` | 26 |
| `study_objective` | 1 |

### Validation errors

Structural errors: None.

Sufficiency errors: None.

Sufficiency warnings: None.

## SEA coverage manifest

- **Main-text figures:** 5; all represented in the HTML as structured figure-appraisal blocks after direct visual inspection of the rendered PDF pages.
- **Main-text table:** 1; represented as a structured table-appraisal block after direct visual inspection of the rendered PDF page.
- **Algorithms/workflows:** study/model workflow in Figure 1 and clinical-integration illustration in Figure 3 are explicitly reconciled.
- **Sections covered:** Summary, Research in context, Introduction, Methods, Results, Discussion, Contributors/Disclosures, Data sharing.
- **References:** not condensed except as provenance infrastructure.
- **Appendix:** the article repeatedly cites an online appendix, but it is not included in the retrieved 12-page PDF. Appendix-only content was not inferred or reconstructed.

## SEA QA

- **HTML parse/title:** PASS
- **TOC anchors:** PASS (7 checked; missing: none)
- **Figure blocks:** 6 (expected 6 visual objects: 5 figures + 1 table)
- **Embedded images:** 0 (visuals reconstructed as structured blocks)
- **Internal citation/tool markers:** PASS (none)
- **HTML bytes:** 1,644,391

## Extraction and appraisal limitations

1. The online appendix was unavailable in the retrieved PDF, so appendix-only model configuration parameters, detailed software specifications, supplementary ROC analyses, and additional subgroup/sensitivity tables were not independently inspected.
2. The main-text study is retrospective; its progression target is a deep-learning-derived G-RISK slope observed in eyes under active management.
3. Source anchors use page plus section/figure/table location rather than paragraph numbering because the two-column PDF does not provide stable paragraph IDs.
4. No external sources were used to fill missing details, resolve appendix omissions, or upgrade claims beyond what the retrieved source supports.

## Generated artifacts

- `PIIS2589750026000555_atoms.json`
- `PIIS2589750026000555_SEA.html`
- `PIIS2589750026000555_ATOM-SEA_report.md`
