# ATOM validation and SEA coverage report — `cjhp-62-448.pdf`

## Source metadata

- **Title:** Evaluation of 2 Weight-Based Protocols for Administration of Heparin
- **Authors:** Diana Tsang; Karen F Shalansky; Elaine Lum
- **Source:** Canadian Journal of Hospital Pharmacy. 2009;62(6):448–456.
- **Source type:** Primary literature; retrospective, open-label observational study with a historical comparator.
- **Study period:** September 2006–January 2007.
- **Evaluable sample:** 100 patients (50 standard protocol; 50 lower-target protocol).
- **Publication ID:** `eaa044cc-2904-5c4f-8a20-4e789d687008`
- **Source SHA-256:** `90396a78ef9d224d3b26ceb14b5f568be80b50f34b590c61e6adce5259c79ddf`

## ATOM extraction summary

- **Atoms extracted:** 49
- **Pydantic structural validation:** PASS — 0 errors.
- **JSON Schema validation:** PASS — all 49 atoms validated against `literature_atom.schema.json`.
- **Sufficiency validation:** PASS — 0 errors/warnings from `validate_literature_atom_sufficiency`.
- **Assertion origin:** atoms are serialized as `normalized_from_source`; no calculated or extractor-inference atoms were introduced.

### Atom counts by kind

| Atom kind | Count |
|---|---:|
| `adverse_event` | 4 |
| `author_conclusion` | 1 |
| `eligibility_criterion` | 1 |
| `intervention_description` | 6 |
| `limitation` | 5 |
| `method` | 5 |
| `other` | 1 |
| `outcome_definition` | 2 |
| `population_description` | 2 |
| `qualitative_result` | 3 |
| `quantitative_result` | 10 |
| `study_objective` | 1 |
| `subgroup_result` | 8 |

## SEA coverage manifest

- **Sections mapped:** Abstract; Introduction; Methods; Results; Discussion; Conclusion; References; Appendix 1; Appendix 2.
- **Figures:** 0.
- **Main-text tables:** 4 — all represented as structured tables/blocks in the SEA artifact.
- **Algorithms/workflows:** 2 — Appendix 1 standard heparin/warfarin protocol and Appendix 2 lower-target heparin protocol; both reconstructed as structured workflow tables.
- **Appendices:** 2 — both included because dosing/titration details are central to interpretation and implementation history.
- **References:** bibliography inspected for context but not atomized or condensed as evidence.
- **Visual strategy:** structured reconstruction; no embedded screenshots required because the tables and protocol workflows were legible and recoverable from the PDF text/render.

## Source consistency finding

The source contains an internal target-range inconsistency: **Table 1 lists the lower-target protocol as 60–120 s**, whereas the Introduction and Appendix 2 specify **60–100 s**. This was preserved as an explicit `other` atom and flagged in the SEA appraisal rather than silently reconciled.

## Extraction limitations

- The atom set prioritizes independently reviewable study design, protocol, primary/secondary outcome, safety, compliance, conclusion, and limitation assertions; not every descriptive baseline cell was atomized.
- Results attributed to the 1996 protocol are secondary reports/historical comparator data within this 2009 article; the cited 1996 primary paper was not separately extracted here.
- No funding, conflict-of-interest, or data-availability statement was located in the retrieved PDF text; no such atom was invented.
- The source itself states that PTT assay methodology and both institutional protocols changed shortly after the study; the historical dosing tables should not be treated as current practice authority without independent verification.

## Output files

- `cjhp-62-448-atoms.json` — validated LiteratureAtom array.
- `cjhp-62-448-sea.html` — self-contained SEA appraisal.
- `cjhp-62-448-validation.md` — this validation/coverage report.
