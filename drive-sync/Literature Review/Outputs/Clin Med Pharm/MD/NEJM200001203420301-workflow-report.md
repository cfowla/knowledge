# NEJM200001203420301 — ATOM + SEA Workflow Report

## Source metadata

- **Primary file:** `NEJM200001203420301.pdf`
- **Exact title:** Effects of an Angiotensin-Converting–Enzyme Inhibitor, Ramipril, on Cardiovascular Events in High-Risk Patients
- **Group author:** The Heart Outcomes Prevention Evaluation Study Investigators
- **Writing group named in article:** Salim Yusuf, Peter Sleight, Janice Pogue, Jackie Bosch, Richard Davies, Gilles Dagenais
- **Source type:** Randomized, double-blind, placebo-controlled clinical trial within a 2×2 factorial design
- **Journal citation:** N Engl J Med. 2000;342:145–153.
- **DOI:** 10.1056/NEJM200001203420301
- **PMID:** 10639539
- **Supporting correction files:** `NEJM200001203420301-correction1.pdf`; `NEJM200001203420301-correction2.pdf`

## Corrections incorporated

1. The March 9, 2000 correction changes the Abstract cardiac-arrest result to **RR 0.62; P=0.02**; Table 4 of the primary article already contains these corrected values.
2. The same correction changes the Discussion wording to: reduction in heart failure among patients with **no evidence of impairment of left ventricular systolic function**.
3. Investigator-list corrections were reviewed. The first correction adds P. Talbot and changes L. di Gerogio to L. di Giorgio; the May 4, 2000 correction then specifies **L. De Giorgio** and changes **S. La Tour** to **F. La Tour**. These appendix-name changes do not alter the clinical results.

## SEA source coverage manifest

- **source_id:** NEJM200001203420301
- **source_type:** Original randomized clinical trial
- **date/version:** January 20, 2000 primary article; corrections March 9 and May 4, 2000
- **sections/headings:** Abstract; Introduction/background; Methods (Study Design, Patients, Organization of the Study, Outcomes, Statistical Analysis); Results (Characteristics of the Patients, Compliance, Blood Pressure, Primary Outcomes and Deaths from Any Cause, Secondary and Other Outcomes, Subgroup Analysis, Temporal Trends); Discussion; Appendix; References
- **figures:** 2
  - Figure 1 — Kaplan–Meier estimates for the primary composite
  - Figure 2 — forest plot of the primary composite across predefined subgroups
- **tables:** 4
  - Table 1 — baseline characteristics
  - Table 2 — reasons for discontinuation
  - Table 3 — primary outcome and mortality
  - Table 4 — secondary and other outcomes
- **algorithms/workflows:** none
- **appendices/supplements:** Investigator appendix in primary article; two separate correction notices supplied as supporting materials
- **visual strategy:**
  - Figure 1: structured reconstruction using reported time-to-event description and exact RR/CI
  - Figure 2: embedded crop because the forest-plot layout and subgroup confidence intervals are load-bearing and not fully recoverable from extracted text
  - Tables 1–4: structured HTML tables
  - Correction notices: structured text summary; no screenshot needed
- **coverage decision:** All main-text figures and tables included. Methods, quantitative results, subgroup findings, tolerability, discussion, funding, corrections, and current-practice context included.
- **omissions:** Full investigator roster and full reference list omitted from narrative condensation because they are provenance/bibliography rather than load-bearing study evidence. Their presence and correction history are documented.

## ATOM validation

- **Publication ID:** `34e993d6-87bd-5547-9bc1-f353b944ff7a`
- **Total atoms:** 59
- **Structural validation:** PASS — 0 Pydantic structural errors
- **JSON Schema validation:** PASS — 0 schema errors against `literature_atom.schema.json`
- **Sufficiency validation:** PASS — 0 errors; 0 warnings

### Atom counts by kind

| Kind | Count |
|---|---:|
| adverse_event | 3 |
| author_conclusion | 3 |
| comparator_description | 1 |
| eligibility_criterion | 7 |
| funding_disclosure | 1 |
| intervention_description | 2 |
| limitation | 1 |
| method | 7 |
| outcome_definition | 11 |
| population_description | 1 |
| qualitative_result | 3 |
| quantitative_result | 15 |
| study_objective | 1 |
| subgroup_result | 3 |

### Extraction limitations

- The article did not measure left ventricular function in every participant; this is preserved as a source-reported limitation/caveat rather than silently resolved.
- Figure 2 does not print exact numerical relative risks for every subgroup in text; those subgroup-specific point estimates were not invented. The forest plot is preserved visually in the SEA artifact, while exact numerical atoms are limited to subgroup results explicitly reported in prose.
- Adverse-event discontinuation atoms preserve reported arm percentages; no unreported confidence intervals or P values were inferred.
- Appendix investigator corrections were incorporated into provenance notes, not converted into clinical-result atoms.

## SEA QA status

- **Raw source availability check:** PASS — primary PDF and both correction PDFs remained present locally before/following SEA generation.
- **HTML output:** PASS — self-contained single-file HTML; nontrivial size; title parsed successfully.
- **TOC anchors:** PASS — all internal navigation targets resolve.
- **Figure/table reconciliation:** PASS — 2/2 main-text figures and 4/4 main-text tables accounted for.
- **Correction reconciliation:** PASS — both supplied correction notices incorporated.
- **Placeholder/planning-language scan:** PASS — no TODO/placeholder/planning markers or internal tool citation syntax found.
- **External current-practice verification:** 2023 AHA/ACC/ACCP/ASPC/NLA/PCNA Chronic Coronary Disease guideline (current ACC CCD guideline as of 2026-08-12) plus 2025 AHA/ACC CCD performance measures. External guidance is explicitly separated from source-derived findings in the HTML.

## Final generated artifacts

- `NEJM200001203420301-atoms.json`
- `NEJM200001203420301-sea.html`
- `NEJM200001203420301-workflow-report.md`
