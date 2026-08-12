# cdr0027-0077 - ATOM / SEA Validation and QA Report

## Source metadata

- **File:** `cdr0027-0077.pdf`
- **Title:** Heparin Anticoagulation Responsiveness in a Coronary Care Unit: A Prospective Observational Study
- **Authors:** Faisal Alsayegh; Mona Al-Rasheed; Ali Al-Muhaini; Ekhlas Al-Humoud; Mona Al-Ostaz; Shaker A Mousa
- **Journal:** Cardiovascular Therapeutics
- **Year / volume / pages:** 2009; 27:77-82
- **DOI:** 10.1111/j.1755-5922.2009.00076.x
- **Raw PDF size:** 519,843 bytes
- **Raw PDF SHA-256:** `78e0a40a34022e5670ebbe6e9c0a5fcb7618c6f7be79798461e1317aecefd92e`
- **Publication UUID:** `8709ff48-2121-50c2-9fec-debe7d62d4a0`
- **PDF availability before SEA:** confirmed; the same locally materialized raw PDF was retained and used for SEA.

## ATOM extraction summary

**Total atoms: 58**

| Atom kind | Count |
|---|---:|
| adverse_event | 6 |
| author_conclusion | 4 |
| conflict_of_interest | 1 |
| eligibility_criterion | 2 |
| intervention_description | 1 |
| limitation | 2 |
| method | 7 |
| other | 2 |
| outcome_definition | 5 |
| population_description | 5 |
| qualitative_result | 1 |
| quantitative_result | 12 |
| study_objective | 1 |
| subgroup_result | 9 |

### Assertion-origin handling

- Directly reported statements were retained as `directly_reported` when no substantive normalization was needed.
- Source wording reorganized into a concise reviewable assertion was marked `normalized_from_source`.
- Two cross-document consistency observations were marked `extractor_inference`; they were not converted into reported study findings.
- No calculated-from-reported-data atoms were required for the final set.

## Structural validation

Governing model: `literature.py` (`LiteratureAtom` and nested Pydantic models).

- Pydantic construction: **PASS**
- Pydantic re-validation of serialized atoms: **PASS**
- Structural errors: **0**

## Serialization validation

Serialization contract: `literature_atom.schema.json`.

- JSON Schema validation: **PASS**
- Schema errors: **0**
- Output JSON: a JSON array containing 58 individually schema-valid `LiteratureAtom` objects.

## Sufficiency validation

Governing validator: `literature_atoms.py` (`validate_literature_atom_sufficiency`).

- Sufficiency errors: **0**
- Sufficiency warnings: **0**

All `quantitative_result`, `adverse_event`, and `subgroup_result` atoms contain the required population/exposure/outcome/result context. All subgroup atoms have `population.subgroup=true`.

## Source-level inconsistencies preserved

1. **48-hour over-anticoagulation count:** Table 2 reports **21 of 105 (20%)**; the adjacent Results prose reports **20 patients (20%)**. The atom set uses the Table 2 quantitative value and separately records the discrepancy as an `other` atom with `assertion_origin=extractor_inference`.
2. **Recurrence of ischemia:** Results prose states that recurrence of ischemia is shown in Table 4, but the displayed Table 4 contains no recurrence-of-ischemia row. This is preserved as an extractor-inference QA atom.
3. **Table 3 header ambiguity:** the printed second admission-APTT category appears as `APTT = 1`, whereas adjacent prose describes the group as an APTT ratio of **one or more**. The structured atom normalizes the comparator to `>=1.0` and tags the normalization for review rather than treating the printed glyph as unambiguous.

## Extraction limitations

- The article operationally discusses subtherapeutic APTT as “heparin resistance,” but it does not provide enough dose-intensity information to distinguish biological resistance from inadequate initial dosing, titration behavior, or assay variability. This distinction is handled in SEA appraisal, not rewritten as reported data.
- Patient body weight is not reported in Table 1 or the presented analyses, despite the fixed starting UFH regimen.
- Later APTT denominators decrease from 146 to 137 to 105; the source does not provide a complete patient-level accounting for treatment discontinuation before each timepoint.
- Platelet surveillance for HIT was not routine, limiting safety assessment.
- The paper reports selected chi-square P values but no multivariable adjustment or confidence intervals for the proposed predictors.
- No dedicated funding statement was identified in the retrieved PDF; funding status was not inferred.
- Bibliographic references were not atomized as primary-study findings.

## SEA coverage manifest

- **PDF pages inspected:** 6/6
- **Substantive sections:** abstract; introduction; methods and subsections; results and subsections; discussion; conclusion; conflict of interest
- **Main-text figures:** 0
- **Main-text tables:** 4
- **Formal algorithms/workflows:** 0
- **Appendices/supplements:** none in retrieved PDF
- **Representation:** Tables 1-4 reconstructed as structured HTML tables; no screenshot embedding required because their contents were recoverable and visually verified.
- **References:** acknowledged for provenance; individual reference entries not condensed.

## SEA appraisal status

Final scoring was assigned only after full section extraction and table reconciliation.

| Dimension | Score |
|---|---:|
| Relevance | 9/10 |
| Novelty | 5/10 |
| Method strength | 4/10 |
| Evidence strength | 4/10 |
| External validity | 3/10 |
| Implementation value | 6/10 |

**Verdict:** Read soon.

Best use: historical real-world evidence of frequent early off-target APTT under a local fixed-regimen UFH protocol and a case study in protocol/monitoring implementation.

Do not use as: a definitive prevalence estimate of biological heparin resistance, causal evidence for race/sex/diagnosis predictors, a current UFH dosing recommendation, or strong evidence of clinical-event safety.

## HTML mechanical QA

- Self-contained single-file HTML: **PASS**
- Nontrivial file size: **PASS**
- HTML title present: **PASS**
- TOC anchors resolve: **PASS**
- Required content sections present: **PASS**
- All 4 main-text tables reconciled: **PASS**
- Internal chat/file citation syntax absent: **PASS**
- TODO / placeholder / planning language absent: **PASS**
- External fonts/scripts/images absent: **PASS**

## External information

No external web information was used for the extraction or appraisal. The SEA artifact evaluates the 2009 source as published and explicitly does not claim current guideline concordance.

## Generated artifacts

- `cdr0027-0077-atoms.json`
- `cdr0027-0077-sea.html`
- `cdr0027-0077-validation-and-qa.md`
