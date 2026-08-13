# NEJMoa065485 ATOM + SEA Validation Report

## Activated macros

- `@ATOM`
- `@SEA`

## Source metadata

- **Primary article:** `NEJMoa065485.pdf`
- **Exact title:** Correction of Anemia with Epoetin Alfa in Chronic Kidney Disease
- **Citation:** N Engl J Med 2006;355:2085-2098
- **Trial registration:** NCT00211120
- **Supporting material:** `NEJMoa065485-supplemental.pdf` - Supplementary Appendix: Epoetin Dosing
- **Publication ID used across atoms:** `476cfcc5-5580-51c0-aa9b-e8d4aee39533`
- **Primary SHA-256:** `f6908856ae8b9aa4e87b830e6b0c57ca73f5646a533fade5f19fc51352713e8f`
- **Supplement SHA-256:** `56f31f6071e8168ba722f1e83070fc64f24112ced83438faa43f11f7a9d66df3`

## @ATOM output

- **Total validated atoms:** 54
- **Structural errors:** 0
- **JSON-schema errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0

### Atom counts by kind

| Atom kind | Count |
|---|---:|
| `adverse_event` | 4 |
| `author_conclusion` | 2 |
| `comparator_description` | 1 |
| `conflict_of_interest` | 1 |
| `eligibility_criterion` | 2 |
| `funding_disclosure` | 1 |
| `intervention_description` | 2 |
| `limitation` | 4 |
| `method` | 7 |
| `outcome_definition` | 4 |
| `population_description` | 1 |
| `qualitative_result` | 3 |
| `quantitative_result` | 21 |
| `study_objective` | 1 |

### Validation status

Each serialized object in `NEJMoa065485-atoms.json` was validated with:

1. the `LiteratureAtom` Pydantic model from `literature.py`;
2. the generated JSON serialization contract in `literature_atom.schema.json`;
3. `validate_literature_atom_sufficiency()` from `literature_atoms.py`.

All 54 objects passed all three validation layers. No repairs were required after validation.

### Extraction limitations / schema notes

- The LiteratureAtom schema is atom-level and does not provide a study-level metadata container, so article-level source metadata are reported in this Markdown file rather than wrapped around the JSON array.
- The supplied supplemental appendix contains dosing details only; it was treated as supporting provenance for the same publication, not as a separate study.
- No subgroup-result atoms were created because the supplied source set did not report a primary subgroup analysis requiring atomization.
- Table 2 contains many quality-of-life scale/subscale cells. The atom set preserves the study-level quality-of-life assertion plus the load-bearing exception rather than creating a separate atom for every questionnaire cell; the SEA HTML reconciles the table-level evidence.
- `QuantitativeResult` provides one principal interval field. Where a source sentence contained arm-specific intervals (for example, time to target in both groups), the additional arm interval was preserved in the canonical statement / `original_result_text` rather than fabricated into an unsupported structure.
- No current guideline or regulatory information was added to the atoms.

## @SEA coverage manifest

| Source object | Status | Representation |
|---|---|---|
| Abstract | Included | Synthesis + section condensation |
| Introduction | Included | Section condensation |
| Methods | Included | PICO + section condensation |
| Results | Included | Section condensation + quantitative extraction |
| Discussion / limitations / conclusion | Included | Section condensation + appraisal |
| Figure 1 | Reconciled | Structured block |
| Figure 2 | Reconciled | Structured block |
| Figure 3 | Reconciled | Structured block |
| Table 1 | Reconciled | Structured summary |
| Table 2 | Reconciled | Reconstructed endpoint table + QoL summary |
| Table 3 | Reconciled | Reconstructed safety table |
| Supplementary Appendix | Included | Structured dosing block |
| Investigator appendix / references | Not condensed | Provenance/reference infrastructure |

### SEA QA

- Primary PDF visually rendered and inspected: **14/14 pages**.
- Supplemental PDF visually rendered and inspected: **2/2 pages**.
- Main-text figures reconciled: **3/3**.
- Main-text tables reconciled: **3/3**.
- Required HTML TOC anchors: **9/9 resolve**.
- Internal ChatGPT/file citation syntax in HTML: **none**.
- TODO/placeholder/planning-language scan: **passed**.
- HTML is single-file and self-contained: **passed**.
- Current-practice external verification: **not performed**; the HTML explicitly limits practice translation to the evaluated 2006 source and states that current guideline/label review is required for contemporary decisions.

## Generated files

- `NEJMoa065485-atoms.json`
- `NEJMoa065485-sea.html`
- `NEJMoa065485-validation.md`
