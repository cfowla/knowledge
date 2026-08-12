# ATOM + SEA Run Report — Audit of control of heparin treatment

## Source metadata

- **Source File:** bmjcred00428-0029b.pdf
- **Title:** Audit of control of heparin treatment
- **Journal:** British Medical Journal
- **Volume:** 290
- **Date:** 5 January 1985
- **Pages:** 27-28
- **Accepted:** 8 October 1984
- **Source Type:** prospective clinical audit / observational study
- **Publication Id:** eaf33f5c-c481-5bb0-babd-fb4510346132
- **Pdf Sha256:** cf7471362843b559bac7e11a0536326811b16013587a757faf772ba856df0515
- **Authors:** A G Fennerty, P Thomas, G Backhouse, P Bentley, I A Campbell, P A Routledge
- **Google Drive source:** https://drive.google.com/file/d/11t_TUesNUs2UrJi3BzE0I_izMhBgpMDt/view?usp=drivesdk

## Coverage manifest

- **Sections/headings:** Opening/background paragraph, Patients, methods, and results, Comment, References, Author affiliations/correspondence
- **Figures:** none
- **Tables:** Day by day analysis of anticoagulant state of patients receiving heparin infusion
- **Algorithms/workflows:** none
- **Appendices/supplements:** none
- **Coverage decision:** Full coverage of the heparin audit article on pages 27-28. Neighboring BMJ short communications contained in the same PDF were excluded as unrelated to the requested heparin literature cluster.
- **Omissions:** Bibliographic reference entries were not atomized because they are provenance/context rather than study-generated assertions.

## ATOM extraction

- **Total atoms:** 32
- `author_conclusion`: 5
- `intervention_description`: 1
- `method`: 2
- `outcome_definition`: 1
- `population_description`: 1
- `qualitative_result`: 2
- `quantitative_result`: 18
- `study_objective`: 1
- `subgroup_result`: 1

### Validation

- **Pydantic structural errors:** 0
- **JSON Schema serialization errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0

All 32 atoms passed Pydantic structural validation, the provided JSON Schema contract, and atom-kind sufficiency validation without warnings.

## Extraction limitations

- The PDF is a two-page BMJ journal-page extract containing multiple short communications; only **Audit of control of heparin treatment** was treated as the target publication unit.
- The source reports a historical kaolin cephalin clotting time (KCT) monitoring approach and does not provide a modern anti-Xa/aPTT protocol, clinical outcome comparison, randomized dosing algorithm, or explicit heparin indications.
- The exact denominator of actionable KCT measurements underlying the 26%, 12%, and 85% clinician-response percentages is not reported in the article text and was not inferred.
- Sex-specific sample sizes for the 28-patient dose-response subset are not reported and were not inferred.
- No funding, conflict-of-interest, or data-availability statements are present in the article; no atoms were created for absent disclosures.
- Governing SEA source file is `summary-evaluation-appraisal-protocol-v4-compact.md`; its internal heading identifies itself as “Integrated Compact v3.” The file itself was treated as authoritative per project precedence.

## SEA QA status

- Coverage manifest created before narrative synthesis: **pass**
- Main-text table reconciled: **pass**
- Figures/workflows reconciled: **pass** (none present)
- Scores assigned after extraction: **pass**
- Source claims separated from appraisal: **pass**
- HTML self-contained, no external fonts/scripts/images: **pass**
- Internal chat/file citation syntax absent from HTML: **pass**
- Practice warning included: **pass**

## Mechanical QA details
```json
{
  "html_bytes": 18352,
  "title": "Audit of control of heparin treatment \u2014 Summary, Evaluation, and Appraisal",
  "missing_toc_anchors": [],
  "forbidden_tokens_found": [],
  "table_count": 1,
  "rating_card_count": 6
}
```
