# Processing report — Abuhashem Aramin 2026

## Source package

- **Title:** A network meta-analysis of safety and efficacy of sodium-glucose cotransporter 2 inhibitors in heart failure patients
- **Journal:** Annals of Medicine & Surgery. 2026;88:2288–2297.
- **DOI:** `10.1097/MS9.0000000000004669`
- **PMID:** `41789221`
- **Source type:** systematic review and frequentist network meta-analysis of randomized controlled trials
- **Files processed:** `Abuhashem 2026.pdf`, `ms9_2025_12_17_ibraheim_2_sdc2.docx`, `js9_2025_12_17_xiao_1_sdc1.docx`

## ATOM

- Shared publication UUID: `b968f625-1143-5fe9-ad8a-5b9dbe3794b8`
- LiteratureAtoms: **151**
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Sufficiency errors / warnings: **0 / 0**
- Secondary-review results are tagged as `secondary_synthesis_result`; they are not represented as if the review itself enrolled trial participants.

## SEA

- SEA QA: **PASS_WITH_SOURCE_WARNINGS**
- Main-text coverage: **3 figures + 1 multi-page table**, all reconciled.
- Supplied supplement coverage: **15 tables**, all reconciled.
- Cited Supplementary Figures S1–S18: **not present in supplied packet**; explicitly omitted rather than reconstructed.
- Final verdict: **Read soon**; useful comparative context, not sufficient alone for head-to-head agent superiority.

## References

- Printed numbered references exported: **50**.
- Reference 22 is malformed/concatenated in the source PDF and was preserved rather than silently repaired.

## Source-consistency findings preserved

1. Abstract search cutoff (March 2023) conflicts with Methods cutoff (8 April 2024).
2. Abstract/Results describe 16 RCTs and 80,666 participants; Discussion describes 12 trials and 69,024 participants.
3. Methods labels the risk-of-bias tool ROB-1 but cites/describes RoB 2.
4. Main-text CINeMA confidence language conflicts with supplied Tables S2–S8.
5. Reference 22 appears to contain two citations under one number and ends incompletely.

## Protocol-source gaps

The @ATOM macro names `README(2).md` and `example_atom.json` as required supporting sources, but neither was available in the supplied project sources/Drive search. Extraction therefore followed the higher-authority executable `literature.py`, `literature_atoms.py`, and `literature_atom.schema.json` sources. This gap is recorded in validation and was not filled from general knowledge.

## External information

None. `@VERIFY` was not activated.

## Google Drive output locations

Root: `GitHub Sync / Literature Review / Outputs / Clin Med Pharm`

### JSON

- `abuhashem-aramin-2026-atoms.json` — https://drive.google.com/file/d/1O0hGYvIsKL3PlW14-1msJ7e6H72UOLrg/view
- `abuhashem-aramin-2026-validation.json` — https://drive.google.com/file/d/1U4S_yBZtloEiwcHIm7ipx-XojUhO0qY0/view
- `abuhashem-aramin-2026-coverage.json` — https://drive.google.com/file/d/1N8DZnHKsMEHP8zFqWYvoF3JtIQDCbDiX/view
- `abuhashem-aramin-2026-sea-qa.json` — https://drive.google.com/file/d/1k6wzamu1Oc3cYSvRj228xfeBqugrWu2g/view

### HTML

- `abuhashem-aramin-2026-sea.html` — https://drive.google.com/file/d/1oZrz3rNTDj_wQ7RjT815DVWcs86V6s6x/view

### Markdown

- `abuhashem-aramin-2026-references.md` — https://drive.google.com/file/d/1E-QfGrTpQIWQ4m_RE3DqQCGZNWsQyxH0/view
