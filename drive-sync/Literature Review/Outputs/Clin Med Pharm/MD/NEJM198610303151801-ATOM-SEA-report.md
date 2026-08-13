# NEJM198610303151801 — ATOM + SEA Processing Report

## Source metadata

- **Title:** Continuous Intravenous Heparin Compared with Intermittent Subcutaneous Heparin in the Initial Treatment of Proximal-Vein Thrombosis
- **Authors:** Russell D. Hull; Gary E. Raskob; Jack Hirsh; Richard M. Jay; Jacques R. Leclerc; William H. Geerts; David Rosenbloom; David L. Sackett; Christine Anderson; Linda Harrison; Michael Gent
- **Journal:** The New England Journal of Medicine
- **Citation:** N Engl J Med. 1986;315:1109-1114.
- **Source file:** `NEJM198610303151801.pdf`
- **Drive source folder:** `TBR/Lit Cluster: Heparin Deep Dive`
- **PDF pages:** 6
- **Source format:** image-based PDF; reviewed from rendered pages
- **Input SHA-256:** `8fbed954c965068e1530e893a8bf47e05bd4c0c57cadbf7b222551ad5616e475`

## Activated macros

- `@ATOM`
- `@SEA`

## Governing project sources

### ATOM precedence
1. `literature.py` — domain model and structural validation
2. `literature_atoms.py` — atom-kind sufficiency validation
3. `literature_atom.schema.json` — serialization contract
4. `README(2).md` — workflow intent
5. `example_atom.json` — illustrative only

### SEA precedence
1. `summary-evaluation-appraisal-protocol-v4-compact.md` — authoritative
2. v3 HTML — historical/reference only
3. Primary source PDF

## ATOM extraction

- **Total atoms:** 36
- **Structural validation:** PASS
- **Sufficiency validation:** PASS
- **Structural errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0

### Counts by atom kind

| Atom kind | Count |
|---|---:|
| `adverse_event` | 1 |
| `author_conclusion` | 3 |
| `comparator_description` | 1 |
| `eligibility_criterion` | 4 |
| `exposure_description` | 1 |
| `funding_disclosure` | 1 |
| `intervention_description` | 1 |
| `method` | 5 |
| `outcome_definition` | 3 |
| `population_description` | 2 |
| `qualitative_result` | 2 |
| `quantitative_result` | 8 |
| `study_objective` | 1 |
| `subgroup_result` | 3 |

### Extraction limitations

- The supplied PDF is image-based; extraction was performed from rendered page images rather than a usable embedded text layer.
- Atoms are language-model extracted and have review_status=needs_review; they have not been independently human-verified.
- The atom schema supports one QuantitativeResult object per atom, so selected multi-timepoint series are preserved in the SEA artifact rather than forced into a lossy atom representation.
- No dedicated field exists for trial-registration information; none was reported in this 1986 article.

## SEA coverage manifest

- **Sections reviewed:** Abstract; Introduction; Methods (Patients, Regimens, Surveillance and Follow-up, Outcome Events, Blood Processing and Measurements, Statistical Analysis); Results (Patients, Recurrent VTE, Relation between recurrent VTE and anticoagulation, Bleeding, Deaths, Mean Doses, APTT); Discussion; acknowledgments/references.
- **Main-text tables:** 4/4 reconciled as structured reconstructions.
- **Main-text figures:** 1/1 reconciled as a structured extraction.
- **Algorithms/workflows:** none.
- **Appendices/supplements:** none in supplied PDF.
- **Bibliography:** not condensed individually; treated as provenance infrastructure.

## SEA appraisal summary

- **Verdict:** Read first.
- **Relevance:** 10/10
- **Novelty:** 9/10
- **Method strength:** 8/10
- **Evidence strength:** 7/10
- **External validity:** 5/10
- **Implementation value:** 7/10
- **Core interpretation:** the trial is foundational evidence that prolonged inadequate early UFH anticoagulation is strongly associated with recurrent VTE. It should not be interpreted as proving that every subcutaneous UFH strategy is intrinsically inferior to IV UFH, because the tested SC regimen produced substantially weaker early anticoagulant responses and was judged inadequate by the authors.

## SEA mechanical QA

- **HTML file:** PASS
- **HTML bytes:** 26452
- **TOC anchors:** PASS
- **Table reconciliation:** 4/4
- **Figure reconciliation:** 1/1
- **Placeholder/planning/internal citation syntax scan:** PASS
- **Overall SEA QA:** PASS

## Output files

- `NEJM198610303151801-atoms.json`
- `NEJM198610303151801-SEA.html`
- `NEJM198610303151801-ATOM-SEA-report.md`

## External-source use

- No external/web sources were used. Findings and appraisal were grounded in the retrieved primary PDF and governing project sources.
