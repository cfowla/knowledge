# fmed-12-1745447 — ATOM + SEA processing report

## Source metadata

- **File:** `fmed-12-1745447.pdf`
- **Exact title:** *In-house chromogenic anti-factor Xa assay: development, validation, and identification of factors predicting APTT discordance*
- **Authors:** Lin Sun; Jinxia Zhao; Guohong Jiang; Wenfei Lu; Hui Rong; Limin Lun; Yuehan Wang; Tianhui Zhou
- **Source type:** Original Research — single-center prospective sample collection with analytical assay development/validation, observational APTT/anti-factor Xa concordance analysis, and exploratory predictive modeling
- **Journal:** Frontiers in Medicine
- **Published:** 12 January 2026
- **DOI:** 10.3389/fmed.2025.1745447
- **PDF pages:** 15
- **SHA-256:** `105fbee6222c9b2eb2348fc5cbcc71a2164b0ffab3dc90bac185aa7c59b14eaf`
- **LiteratureAtom publication_id:** `18700ae2-6b77-529a-aa58-0f9f9c835b78`

## @ATOM result

**Total atoms:** 101

| Atom kind | Count |
|---|---:|
| quantitative_result | 52 |
| method | 15 |
| eligibility_criterion | 8 |
| limitation | 5 |
| subgroup_result | 5 |
| author_conclusion | 3 |
| study_objective | 3 |
| population_description | 2 |
| qualitative_result | 2 |
| conflict_of_interest | 1 |
| data_availability | 1 |
| exposure_description | 1 |
| funding_disclosure | 1 |
| other | 1 |
| outcome_definition | 1 |

### Validation

- **Pydantic structural validation:** PASS
- **`literature_atom.schema.json` validation:** PASS — 0 schema errors
- **`validate_literature_atom_sufficiency`:** PASS — 0 sufficiency errors, 0 warnings
- **Unique atom IDs:** 101 / 101
- **Publication identity:** one shared `publication_id` across all atoms
- **Review status:** all atoms are `needs_review`; none were marked human-verified

### Source consistency findings retained rather than repaired

1. **Patient/sample allocation:** the paper reports 190 specimens from 110 total patients, but §2.1.5 describes 80 derivation specimens from 80 different patients plus 110 concordance/modeling specimens from 110 different patients independent of the derivation set.
2. **Figure 1 unit:** the x-axis is labeled incubation time in minutes while the body/caption describe seconds.
3. **Figure 4 calibration equation:** the printed caption equation conflicts with the equation drawn in the plot and the main-text equation.
4. **Figure 8 denominator:** caption reports `n=120`, whereas §3.3.2 describes 80 method-comparison specimens.
5. **Figure 9 Bland–Altman bias:** caption reports mean bias 0.005 IU/mL; Discussion later reports −0.008 IU/mL.
6. **Figure 10 denominator:** caption reports `n=110`, while the text states §3.4.1 used the 80-sample derivation set.
7. **Figure 11 ROC values:** figure/caption reports cutoffs 71.34 s and 125.80 s with AUC 0.870 and 0.855; main text reports 78.9 s and 126.6 s with AUC 0.723 and 0.815.
8. **Figure 12 concordance matrix:** the displayed heatmap diagonal totals 57/110, while the prose reports 46/110 concordant and gives concordant category counts of 8/32/6.
9. **Figure 14 monitoring algorithm:** prose, caption, and flowchart are internally inconsistent on eGFR direction and AT-III branch logic.

These conflicts were **not** silently reconciled. Atoms retain source-backed statements and the SEA marks the conflicts as appraisal limitations.

### Extraction limitations

- No separate supplementary file was retrieved during this run; only the requested raw PDF was available.
- Bibliography entries were not atomized.
- The current LiteratureAtom model does not encode a dedicated “source inconsistency” object; discrepancies are therefore documented in this report/SEA rather than converted into reported evidence atoms.
- Some complex multi-metric analytical results are serialized using the primary quantitative estimate plus structured arm observations/original-result context, consistent with the current schema.

## @SEA coverage manifest

- **Substantive source:** pages 1–13; disclosures begin on page 13 and references occupy pages 14–15.
- **Mapped sections:** Abstract; Introduction; Materials and methods §§2.1–2.6; Results §§3.1–3.6; Discussion; Conclusion; Data availability; Ethics; Author contributions; Funding; Acknowledgments; Conflict of interest; Generative AI statement; Publisher note; References.
- **Figures:** 14 / 14 reconciled.
- **Tables:** 2 / 2 reconciled.
- **Workflow/algorithm:** Figure 14 reconciled.
- **Visual strategy:** Figures 11 and 14 embedded as crops because their layout and numeric/branch inconsistencies are load-bearing; the remaining figures/tables are represented with structured extraction blocks.
- **Omissions:** bibliography not condensed; no separate supplement was available.

## SEA appraisal summary

- **Verdict:** Read first for heparin monitoring/assay-development context; do not treat as a practice standard.
- **Relevance:** 10/10
- **Novelty:** 7/10
- **Method strength:** 5/10
- **Evidence strength:** 5/10
- **External validity:** 3/10
- **Implementation value:** 6/10

The analytical validation is the strongest component. Clinical threshold and predictive-model claims are substantially limited by single-center design, small modeling sample, internal validation only, absence of bleeding/thrombosis outcomes, and multiple unresolved source-level inconsistencies.

## SEA mechanical QA

- Self-contained HTML: PASS
- Exact title/source ID: PASS
- Required TOC anchors resolve: PASS
- Main-text visual reconciliation: PASS — 14 figures, 2 tables
- Embedded external fonts/scripts/remote images: NONE
- Internal tool/file citation syntax: NONE
- TODO/placeholders/planning language: NONE
- Provenance and caveats: PRESENT

## Output files

- `fmed-12-1745447-atoms.json` — validated LiteratureAtom array
- `fmed-12-1745447-atom-validation.json` — structured ATOM validation/source-consistency report
- `fmed-12-1745447-sea.html` — self-contained SEA appraisal
- `fmed-12-1745447-review.md` — this processing/validation/QA report
