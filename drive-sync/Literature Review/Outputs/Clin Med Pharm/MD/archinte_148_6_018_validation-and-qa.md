# ATOM + SEA Validation and QA — `archinte_148_6_018.pdf`

## Source metadata

- **Title:** Physician Practices in the Treatment of Pulmonary Embolism and Deep Venous Thrombosis
- **Authors:** Arthur P. Wheeler, MD; Robert D. B. Jaquiss, MD; John H. Newman, MD
- **Citation:** *Arch Intern Med.* 1988;148:1321-1325.
- **Source type:** Retrospective observational chart review / physician-practice audit
- **Drive source ID:** `1qCHP8fTHvPl2qZ6IN74Nh4iU3wbasAGF`
- **Raw PDF size:** 844,607 bytes
- **PDF pages:** 5
- **SHA-256:** `4e9ca4a49d0880f6ac2fd051a004049dead40e9455358e1fce180a03a254a3e2`
- **LiteratureAtom publication_id:** `b1648cdb-8311-42b3-b215-e4d44dc758fe`

## ATOM extraction

- **Validated atoms:** 44
- **Structural validation:** PASS — every atom round-tripped through the governing Pydantic `LiteratureAtom` model and validates individually against `literature_atom.schema.json`.
- **Sufficiency validation:** PASS — 0 errors, 0 warnings under `validate_literature_atom_sufficiency`.
- **Atom ID uniqueness:** PASS
- **Shared publication identity:** PASS

### Counts by atom kind

| Atom kind | Count |
|---|---:|
| `adverse_event` | 3 |
| `author_conclusion` | 2 |
| `eligibility_criterion` | 1 |
| `funding_disclosure` | 1 |
| `limitation` | 4 |
| `method` | 2 |
| `outcome_definition` | 5 |
| `population_description` | 1 |
| `qualitative_result` | 2 |
| `quantitative_result` | 22 |
| `study_objective` | 1 |

## Source-derived extraction limitations / issues

- The article reports the first PTT therapeutic-rate as **40% in Results** and **41% in the Figure 1 caption**. The atom set preserves this as an internal one-percentage-point source discrepancy rather than silently reconciling it.
- The study's “heparin-induced thrombocytopenia” definition was clinical/laboratory and **not confirmed** with the platelet-aggregating-substance testing discussed by the authors.
- Nine of eleven recurrent events were **suspected**, not proved; six suspected recurrences had no repeat diagnostic test and three had negative repeat radiologic studies.
- The study explicitly states it was **not designed to establish** whether promptly achieving/maintaining PTT >1.5 times control was necessary or desirable, and it did not measure the clinical risk attributable to study-defined “subtherapeutic” PTT.
- No DOI or PMID is printed in the evaluated PDF; none was added from outside sources.
- No external/current-practice verification was performed; SEA appraisal treats the paper as a historical primary source.

## SEA coverage manifest

- **Sections/headings:** title/abstract; introduction; Patients and Methods; Results; Efficacy of Initial Heparin Therapy; Physician Responses to Low PTT; Physician Response to Elevated PTT; Bleeding Complications; Recurrences; Warfarin Sodium Therapy; Comment; Complications; References.
- **Main-text table:** 1 — “Timing of Events in Patients Treated for Deep Venous Thrombosis or Pulmonary Embolism.”
- **Figures:** 6 — Figures 1-6 all reconciled in the SEA artifact as structured evidence blocks.
- **Algorithms/workflows:** none.
- **Appendices/supplements:** none in the PDF.
- **Visual strategy:** structured reconstruction for the table and all six figures; no image embedding was necessary for interpretation.
- **Omissions:** bibliography condensed to provenance only; individual references were not appraised because @SEA was executed against the primary paper itself.

## SEA QA

- Coverage manifest created before final narrative synthesis: PASS
- Every main-text figure/table accounted for: PASS
- Claims and appraisal separated: PASS
- Final scoring performed after full-source extraction/reconciliation: PASS
- Self-contained single-file HTML with embedded CSS: PASS
- Internal tool/file citation syntax absent from HTML: PASS
- No TODO/placeholder/planning language: PASS
- Scope warning included: PASS

## Output files

- `archinte_148_6_018_atoms.json`
- `archinte_148_6_018_sea.html`
- `archinte_148_6_018_validation-and-qa.md`
