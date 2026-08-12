# CLC-20-1006 - ATOM validation and SEA coverage report

## Source metadata

- **Title:** Heparin Dosing for Percutaneous Coronary Angioplasty: Use of Body Surface Area to Improve Initial Activated Clotting Time Values
- **Authors:** Gene R. Pesola, MD; David A. Pesola, MD, FACC
- **Citation:** Clinical Cardiology. 1997;20:1006-1009.
- **Source type:** Primary clinical literature; small matched comparative study of initial UFH dosing during PTCA.
- **Evaluable sample:** 54 patients (27 BSA-guided; 27 age-/gender-matched fixed-dose controls).
- **Raw PDF:** `CLC-20-1006.pdf`, 4 pages, SHA-256 `694d069a0576ad9084b5ff701abe7ebf1e6276652dffa9ae193a488b4964699b`.
- **Publication ID:** `9c7e73fd-3abc-51e3-94b1-2e57a051fd03`.

## ATOM execution

Governing precedence used: `literature.py` -> `literature_atoms.py` -> `literature_atom.schema.json` -> workflow intent/examples, as specified by the accessible project ATOM/SEA control document.

### Atom counts

- **Total:** 31
- `author_conclusion`: 3
- `comparator_description`: 1
- `eligibility_criterion`: 1
- `intervention_description`: 2
- `limitation`: 4
- `method`: 5
- `other`: 2
- `outcome_definition`: 2
- `population_description`: 2
- `qualitative_result`: 1
- `quantitative_result`: 7
- `study_objective`: 1


### Validation

- JSON syntax: **PASS**.
- Required LiteratureAtom v1 field-shape checks: **PASS**.
- Accessible ATOM sufficiency rules: **PASS** with 0 errors / 0 warnings.
- Unique atom UUIDs and one shared publication ID: **PASS**.
- All atoms: `review_status = needs_review`.

**Validator caveat:** the standalone executable copies of `literature.py`, `literature_atoms.py`, and `literature_atom.schema.json` were not retrievable in the active file/connector context. Therefore this run does not claim a fresh executable Pydantic or official JSON-Schema validation. The output was checked against the accessible validated LiteratureAtom v1 artifact contract and the sufficiency rules exposed by the project control document.

### Extraction boundaries / limitations

1. The paper is primary literature, so the ATOM set represents its own population, methods, pharmacodynamic results, interpretation, and limitations. Secondary claims about earlier studies in the Discussion were not recast as primary-study efficacy atoms.
2. The main study outcome is a 10-minute ACT surrogate; the paper does not report bleeding, thrombosis, ischemic events, transfusion, or other patient-centered outcomes.
3. The source does not describe random allocation. It compares a previously used fixed-dose approach with a recently adopted BSA-adjusted method and matched controls; the SEA therefore treats the study as nonrandomized.
4. The BSA formula was explicitly described as empirical.
5. ACT thresholds are device- and specimen-source-dependent in the source; this constraint is preserved rather than generalized away.
6. No funding, conflict-of-interest, or data-availability disclosure was located in the retrieved four-page source; none was invented.
7. Table-row values affected by OCR ambiguity were not used as load-bearing results. Aggregate values and Table III were checked against rendered pages.

## Raw-PDF continuity check before SEA

- Local raw PDF present immediately after ATOM: **PASS**.
- Size: 379,188 bytes.
- SHA-256 unchanged: **PASS** (`694d069a0576ad9084b5ff701abe7ebf1e6276652dffa9ae193a488b4964699b`).
- Refetch before SEA: **not required**.

## SEA coverage manifest

- **Sections:** Summary/abstract; Introduction; Methods (Study Population; PTCA Dosing Procedure; Statistical Analysis); Results; Discussion; Conclusion; References.
- **Main-text tables:** 3 - all accounted for.
  - Table I: structured summary of patient-level fixed-dose data and printed aggregates.
  - Table II: structured summary of patient-level BSA-guided data and printed aggregates.
  - Table III: full target-attainment comparison reproduced as a structured table.
- **Figures:** 0.
- **Algorithms/workflows:** 0 graphical workflows; the BSA equation is represented as a structured dosing rule.
- **Appendices/supplements:** none in the retrieved source.
- **References:** inspected for context/provenance but not atomized or condensed item-by-item.
- **External current-practice verification:** not performed; source-derived content and appraisal are kept separate.

## SEA appraisal summary

- **Verdict:** Skim deeply.
- **Relevance:** 8/10.
- **Novelty:** 4/10.
- **Method strength:** 4/10.
- **Evidence strength:** 5/10.
- **External validity:** 2/10.
- **Implementation value:** 2/10.
- **Best use:** historical/mechanistic evidence for individualized UFH dosing and ACT-device specificity.
- **Do not use for:** a stand-alone contemporary PCI dosing protocol or inference of clinical bleeding/thrombotic benefit.

## SEA mechanical QA

- HTML exists and has nontrivial size: **PASS** (18,637 bytes).
- HTML title parsed/present: **PASS**.
- TOC anchors resolve: **PASS**.
- Main table/visual coverage reconciled: **PASS**.
- Internal chat/file citation markers absent: **PASS**.
- Placeholder/planning-language scan: **PASS**.
- Overall SEA mechanical QA: **PASS**.

## Output files

- `CLC-20-1006-atoms.json` - ATOM extraction.
- `CLC-20-1006-sea.html` - self-contained SEA reference artifact.
- `CLC-20-1006-validation.md` - this ATOM validation / SEA coverage report.
