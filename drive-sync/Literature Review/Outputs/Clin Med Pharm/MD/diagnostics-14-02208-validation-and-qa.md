# diagnostics-14-02208 — ATOM + SEA Validation and QA

## Activated macros

- `@ATOM`
- `@SEA`

## Source identity

- **File:** `diagnostics-14-02208.pdf`
- **Title:** *Pulmonary Embolism in Critically Ill Patients—Prevention, Diagnosis, and Management*
- **Authors:** Charikleia S. Vrettou; Effrosyni Dima; Ioanna Sigala
- **Journal:** *Diagnostics* (2024), 14(19), article 2208
- **DOI:** `10.3390/diagnostics14192208`
- **Source type:** Narrative review
- **Pages:** 17 total; substantive article pages 1–11; references pages 12–17
- **Raw PDF SHA-256:** `34726fa16102a2d214e006fe5d1e948020aab4028ca76ce64933bc1784f1350c`
- **Raw PDF local presence before SEA:** confirmed, 785,385 bytes
- **Shared LiteratureAtom publication_id:** `e55727b8-386d-4556-9f9f-c0ddd581e6a6`

## ATOM results

**Total atoms: 75**

| Atom kind | Count |
|---|---:|
| author_conclusion | 39 |
| conflict_of_interest | 1 |
| funding_disclosure | 1 |
| intervention_description | 22 |
| limitation | 1 |
| other | 4 |
| outcome_definition | 1 |
| qualitative_result | 1 |
| quantitative_result | 4 |
| study_objective | 1 |

### Validation

- Pydantic structural validation errors: **0**
- JSON Schema validation errors: **0**
- LiteratureAtom sufficiency errors: **0**
- LiteratureAtom sufficiency warnings: **0**
- Atom review status: `needs_review`

### Extraction boundary / schema limitation

This source is a narrative review, while the current LiteratureAtom schema is oriented primarily toward primary literature and does not define a dedicated narrative-review synthesis or guideline/recommendation atom kind. Review-level assertions were therefore encoded only in defensible existing kinds such as `author_conclusion`, `intervention_description`, or `other`. Numerical findings originating from cited studies remain anchored to this review and are tagged as secondary reported results rather than being represented as if this review enrolled participants or generated those primary data. Primary-study atoms require separate extraction from the cited original publications.

No SEA appraisal judgments were converted into reported LiteratureAtom evidence.

## SEA source map and coverage

### Source sections inspected

1. Abstract
2. Introduction
3. Thromboembolic Prophylaxis
4. Clinical Suspicion, Diagnosis, and Risk Stratification
   - Continuous Hemodynamic Monitoring
   - Imaging and Other Diagnostic Tests
   - Risk Stratification
5. Management of Acute Pulmonary Embolism in ICU
   - Therapeutic Anticoagulation
   - Inferior Vena Cava Filters
   - Reperfusion Therapies
6. Conclusions
7. References

### Visual / table reconciliation

- Main-text tables found: **7**
- Main-text tables represented in SEA: **7/7**
- Main-text figures found: **1**
- Main-text figures represented in SEA: **1/1**
- Main-text algorithms/workflows requiring separate reconciliation: **0**
- Supplements identified: **none**
- Bibliography pages were inspected for source structure but not condensed as independent evidence because they function as provenance infrastructure.

Figure 1 was inspected from the rendered PDF and embedded as a self-contained crop. All seven tables were reconstructed from source content and cross-checked against rendered pages.

## SEA appraisal summary

**Verdict:** Read first — as an ICU-specific orientation and citation map, not as a sole protocol authority.

| Dimension | Score |
|---|---:|
| Relevance | 9/10 |
| Novelty | 6/10 |
| Method strength | 4/10 |
| Evidence strength | 5/10 |
| External validity | 6/10 |
| Implementation value | 8/10 |

The final appraisal was assigned only after section extraction and figure/table reconciliation.

## External currency verification

External verification was kept separate from source-derived findings. The SEA notes that the ESC's currently published acute pulmonary embolism guideline remains the 2019 guideline and that ESC lists a new pulmonary embolism guideline in its planned 2027 publication schedule. This currency check does not alter what the 2024 review itself reported.

## Mechanical QA

- HTML source title/identifier reconciled: **pass**
- HTML is self-contained: **pass**
- Table-of-contents anchors resolve: **pass**
- Main-text visual/table coverage reconciled: **pass**
- Internal chat/file citation syntax absent from HTML: **pass**
- Draft markers absent: **pass**
- Claims and appraisal separated: **pass**
- Provenance and caveats included: **pass**

## Final outputs

- `diagnostics-14-02208-atoms.json`
- `diagnostics-14-02208-sea.html`
- `diagnostics-14-02208-validation-and-qa.md`
