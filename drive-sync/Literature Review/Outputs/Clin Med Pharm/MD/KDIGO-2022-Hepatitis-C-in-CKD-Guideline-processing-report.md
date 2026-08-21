# KDIGO 2022 hepatitis C in CKD guideline processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Title: KDIGO 2022 Clinical Practice Guideline for the Prevention, Diagnosis, Evaluation, and Treatment of Hepatitis C in Chronic Kidney Disease
- Issuing body: Kidney Disease: Improving Global Outcomes (KDIGO) Hepatitis C Work Group
- Citation: Kidney Int. 2022;102(6S):S129-S205
- DOI: 10.1016/j.kint.2022.07.013
- Main guideline: `KDIGO-2022-Hepatitis-C-in-CKD-Guideline.pdf`, 78 pages, SHA-256 `7a59501d9f9b60ceca7e15ce5ab0bfda33dc31270abed5b91b46288302d50ecf`
- Search-method appendix: `KDIGO-2022-Hepatitis-C-in-CKD-Guideline-Appendix.pdf`, 10 pages, SHA-256 `52b56baada8a91951770ee006fa8776d00a72b3420f5902b501dc1032528788d`
- Supplementary evidence tables: `KDIGO-2022-Hepatitis-C-in-CKD-Guideline-Supplementary-Tables.pdf`, 103 pages, SHA-256 `95e6d0cd9be29d3c8a931eee68892884413fa13bc7ef765ed21a491e763f7e08`
- Shared publication ID: `f2fb715d-0fc6-5c2f-b816-ced719914280`

## ATOM extraction

- Total LiteratureAtoms: **69**
- Formal guidance atoms: **62**
- Global scope/method/limitation atoms: **7**
- Atom kinds: `limitation` 1, `method` 5, `other` 62, `study_objective` 1
- Formal guidance by grade: `1C` 7, `1A` 19, `2D` 5, `1B` 8, `Not Graded` 17, `2B` 3, `1D` 2, `2C` 1
- Assertion origin: `normalized_from_source` 69
- Review status: `needs_review` 69
- Shared publication identity: PASS
- Unique atom IDs: PASS

### Semantic batches

| Batch | Scope | Atoms |
| --- | --- | ---: |
| `kdigo-2022-hcv-global-v1` | scope, version control, evidence methods, grading, review and search limitations | 7 |
| `kdigo-2022-hcv-detection-evaluation-v1` | Chapter 1 screening, follow-up, liver evaluation and associated testing | 21 |
| `kdigo-2022-hcv-treatment-v1` | Chapter 2 DAA treatment, interactions and HBV assessment | 8 |
| `kdigo-2022-hcv-infection-control-v1` | Chapter 3 hemodialysis infection control and outbreak response | 8 |
| `kdigo-2022-hcv-transplant-v1` | Chapter 4 transplant candidacy, donors, immunosuppression and complications | 18 |
| `kdigo-2022-hcv-glomerulonephritis-v1` | Chapter 5 HCV-associated glomerulonephritis | 7 |

## Validation

- Local Pydantic contract validation: **PASS**
- Local generated JSON Schema validation: **PASS**
- Sufficiency validation for extracted kinds: **PASS**
- Structural errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

### Governing-source execution boundary

The uploaded `large-source-ATOM-SEA.md` and retrieved `unslop.skill.md` were applied. The named governing ATOM files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom.json`, plus the exact `summary-evaluation-appraisal-protocol-v4-compact.md`, were searched in connected project sources but were not directly retrievable in this session. Validation therefore uses a strict local Pydantic contract and generated JSON Schema reconstructed from recent validated project guideline artifacts plus the large-source guideline guardrail. This report does not claim execution of unavailable authoritative project code.

## SEA coverage and QA

- Formal guidance: **62/62**
- Main figures: **5/5**
- Main tables: **19/19**
- Supplementary evidence tables: **S1-S26 inventoried and inspected**
- Appendix: **2/2 appendices inspected**
- Main bibliography: **346 references extracted**
- Source claims kept separate from appraisal: **PASS**
- Self-contained HTML: **PASS**
- Internal chat/file citation syntax: **absent**
- External verification: **not performed** because `@VERIFY` was not activated

Key evidence profiles reconciled include liver-fibrosis testing, HCV as a predictor of CKD progression, DAA therapy in CKD G4-G5 non-dialysis, dialysis and kidney-transplant recipients, hemodialysis isolation, transplantation versus waitlist, HCV-associated death/graft loss after transplant, HCV-infected donor to HCV-uninfected recipient transplantation, and HCV-associated glomerulonephritis.

## Source-integrity finding

Main Figure 1 reports high-quality evidence with total N=405 for sofosbuvir/velpatasvir in CKD G5D. Supplementary Table S6 reports 8 studies and N=629 for SVR12. Table S6 also prints an SVR12 estimate of 93.0% with a 95% CI of 93.0%-97.3%. The discrepancy was preserved and flagged rather than silently corrected.

## Schema gaps

- The current project guideline pattern has no dedicated `guideline_recommendation` atom kind. Formal guidance is represented as `atom_kind="other"` with descriptive tags.
- Recommendation strength and GRADE certainty are preserved in tags rather than dedicated typed fields.
- Trial effects summarized by KDIGO are secondary evidence. Primary-study atoms require separate extraction of the cited publications.

## References

- Main guideline bibliography: **346 entries**
- Supplement table-local citations were used for evidence provenance and were not duplicated as a second bibliography.
- Bibliographic entries were not treated as LiteratureAtoms.

## Output files

- `KDIGO-2022-Hepatitis-C-in-CKD-Guideline-atoms.json`
- `KDIGO-2022-Hepatitis-C-in-CKD-Guideline-validation.json`
- `KDIGO-2022-Hepatitis-C-in-CKD-Guideline-coverage.json`
- `KDIGO-2022-Hepatitis-C-in-CKD-Guideline-sea.html`
- `KDIGO-2022-Hepatitis-C-in-CKD-Guideline-references.md`
- `KDIGO-2022-Hepatitis-C-in-CKD-Guideline-processing-report.md`
