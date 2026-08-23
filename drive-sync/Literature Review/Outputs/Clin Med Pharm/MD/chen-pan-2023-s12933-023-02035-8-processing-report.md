# Chen Pan 2023 processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source

- Title: Impact of SGLT2 inhibitors on patient outcomes: a network meta-analysis
- Authors: Jui-Yi Chen, Heng-Chih Pan, Chih-Chung Shiao, Min-Hsiang Chuang, Chun Yin See, Tzu-Hsuan Yeh, Yafei Yang, Wen-Kai Chu, Vin-Cent Wu
- Journal: Cardiovascular Diabetology. 2023;22:290.
- DOI: 10.1186/s12933-023-02035-8
- PMID: 37891550
- PROSPERO: CRD42022361906
- Main source: `Chen Pan 2023.pdf`, 15 PDF pages, SHA-256 `d7d65370c832c3ace7fd5919e9c327e51cbc051a9807ac278419bbd974331d74`
- Supplement: `12933_2023_2035_MOESM1_ESM.docx`, 33 rendered pages, SHA-256 `c7d8b1cbf378e7e29dc8bf4c841fd4395336502ea041d5d6e325e0cd3f024243`
- Shared publication ID: `7b85aff3-a2dd-5653-b47a-892d4e7b71bf`
- Source type: systematic review and frequentist random-effects network meta-analysis of double-blind randomized controlled trials

## ATOM result

- Total LiteratureAtoms: 82
- Counts by kind: `{"adverse_event": 1, "author_conclusion": 2, "comparator_description": 1, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 1, "funding_disclosure": 1, "intervention_description": 1, "limitation": 9, "method": 7, "other": 4, "outcome_definition": 3, "population_description": 1, "qualitative_result": 9, "quantitative_result": 1, "study_objective": 1, "subgroup_result": 38}`
- Assertion origins: `{"directly_reported": 17, "normalized_from_source": 65}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0

All atoms use `needs_review` because extraction was model-assisted and has not received independent human verification.

## SEA result

Coverage reconciled all **4 main-text figures** and **2 main-text tables**, plus **8 supplementary figures** and **32 Word table objects**. Of the supplement tables, Tables 6-30 are 25 CINeMA confidence tables, Table 31 documents PROSPERO status, and Table 32 is the PRISMA checklist; the first five Word table objects function as layout/figure containers rather than independent data tables.

Key indirect active-drug estimates preserved include empagliflozin vs dapagliflozin for all-cause death in diabetes (RR 0.81, 95% CI 0.69-0.96), canagliflozin vs dapagliflozin for CV death/HHF in non-HF patients (RR 0.75, 95% CI 0.58-0.98), and sotagliflozin vs dapagliflozin for MACE in HF (RR 0.73, main article CI 0.58-0.92; supplement CI 0.57-0.92). These are **indirect comparisons with zero direct active-comparator trials**; relevant CINeMA tables rate several as **low or very low confidence**.

Verdict: **Read soon**. The paper is highly relevant for mapping individual SGLT2 inhibitor hypotheses but is not sufficient by itself to establish dapagliflozin-versus-empagliflozin clinical non-equivalence or formulary interchangeability.

## References

The primary article contains **59** bibliography entries. They were exported to `chen-pan-2023-s12933-023-02035-8-references.md`. Bibliography entries were not converted into LiteratureAtoms solely because they were cited.

## Source and validation limitations

- `literature.py`, `literature_atoms.py`, and `literature_atom.schema.json` were available and executed as the governing ATOM structural, sufficiency, and serialization contracts.
- `summary-evaluation-appraisal-protocol-v4-compact.md` governed SEA; v3 was historical reference only.
- `README(2).md` and `example_atom.json` were not available in the supplied project sources or exact Drive search, so their supporting guidance could not be inspected.
- The PRISMA Results prose says 503 records were removed after 721 duplicates from 1,224 records, whereas Figure 1 shows 503 records remained after duplicate removal.
- The Results text says included trials were published 2017-2022, while Table 1 includes EMPA-REG OUTCOME (2015) and labels DECLARE-TIMI 58 as 2009.
- The main article reports sotagliflozin-vs-dapagliflozin HF MACE RR 0.73 (95% CI 0.58-0.92); the supplement reports RR 0.73 (95% CI 0.57-0.92).
- The supplement says CANVAS randomized 17,160 patients, while Table 1 arm counts total 10,142.
- The supplement prints CANVAS amputation HR 1.97 with 95% CI 1.41-1.75, which does not contain the point estimate.
- The abstract describes sotagliflozin-vs-dapagliflozin CV death/HHF as “borderline significantly lower” despite RR 0.90 (95% CI 0.80-1.01), whose interval includes 1.
- The network includes no direct comparisons between any two active SGLT2 inhibitors; key agent-vs-agent findings depend on indirect evidence and transitivity assumptions.

## Output files

Stored under `GitHub Sync / Literature Review / Outputs / Clin Med Pharm`.

### JSON
- `chen-pan-2023-s12933-023-02035-8-atoms.json`
- `chen-pan-2023-s12933-023-02035-8-validation.json`
- `chen-pan-2023-s12933-023-02035-8-coverage.json`
- `chen-pan-2023-s12933-023-02035-8-crosswalk.json`
- `chen-pan-2023-s12933-023-02035-8-sea-qa.json`

### HTML
- `chen-pan-2023-s12933-023-02035-8-sea.html`

### Markdown
- `chen-pan-2023-s12933-023-02035-8-references.md`
- `chen-pan-2023-s12933-023-02035-8-processing-report.md`
