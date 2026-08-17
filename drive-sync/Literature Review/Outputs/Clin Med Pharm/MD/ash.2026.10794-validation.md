# ash.2026.10794 ATOM + SEA Validation Report

## Activated macros

- `@ATOM`
- `@SEA`

## Source metadata

- **Primary article:** `retrospective-multicenter-evaluation-of-oral-step-down-versus-intravenous-carbapenem-treatment-of-extended-spectrum-beta-lactamase-producing-escherichia-coli-urinary-tract-infections.pdf`
- **Exact title:** Retrospective multicenter evaluation of oral step-down versus intravenous carbapenem treatment of extended-spectrum beta-lactamase-producing *Escherichia coli* urinary tract infections
- **Authors:** Margarita Bellon; Alice Margulis Landayan; Jorge Morales; Jorge Murillo; Stephen Breazeale; Timothy P. Gauthier
- **Journal/year:** *Antimicrobial Stewardship & Healthcare Epidemiology*, 2026;6:e225
- **DOI:** 10.1017/ash.2026.10794
- **Study type:** Multicenter retrospective observational comparative cohort
- **Source pages:** 4
- **Publication ID:** `78a32610-4193-5735-be50-55b0a2440f0e`
- **PDF SHA-256:** `ac4009f74cf99ca08e5c5a3398253dc9901298de6a4f737e3a947077fff11a11`

## ATOM governing sources

Authority order used:

1. `literature.py` — domain model and structural validation
2. `literature_atoms.py` — atom-kind sufficiency validation
3. `literature_atom.schema.json` — serialization contract
4. `README(2).md` — workflow intent
5. `example_atom.json` — illustrative only

## ATOM extraction summary

**Total atoms:** 46

| Atom kind | Count |
|---|---:|
| quantitative_result | 20 |
| limitation | 7 |
| method | 3 |
| outcome_definition | 3 |
| adverse_event | 3 |
| eligibility_criterion | 2 |
| study_objective | 1 |
| population_description | 1 |
| intervention_description | 1 |
| comparator_description | 1 |
| qualitative_result | 1 |
| author_conclusion | 1 |
| funding_disclosure | 1 |
| conflict_of_interest | 1 |

### Structural validation

- All 46 atoms instantiated successfully with the `LiteratureAtom` Pydantic model.
- All 46 serialized atoms round-trip validated successfully through `LiteratureAtom.model_validate()`.
- Each serialized object was checked against `literature_atom.schema.json`.
- **Schema/structural errors: 0**

### Sufficiency validation

Each atom was checked with `validate_literature_atom_sufficiency()` from `literature_atoms.py`.

- **Sufficiency errors: 0**
- **Sufficiency warnings: 0**

### Assertion origin / provenance

- Source-reported statements were preserved as `directly_reported` where used verbatim or as `normalized_from_source` where normalized into canonical statements.
- No appraisal statement was converted into a reported-data atom.
- No calculated effect sizes were inserted into the ATOM set.
- Each atom has a source page/section anchor; table-derived quantitative results additionally identify the table and row.
- One publication ID is shared across the complete atom set.

## ATOM extraction limitations

- The paper reports oral agents as a pooled step-down strategy; it does not provide agent-specific clinical outcomes.
- Oral agent use is not cross-tabulated by uncomplicated versus complicated UTI phenotype, so agent-by-syndrome effectiveness cannot be atomized from the source.
- Clinical failure estimates are reported without confidence intervals.
- Follow-up outside the health system is unavailable in the source.
- Table 1 reports catheter-associated UTI as 14/60 versus 5/60 with `p=.43`; the value was preserved as source-reported but not used to create a corrected/calculated atom.

## SEA governing source

- `summary-evaluation-appraisal-protocol-v4-compact.md` — authoritative
- v3 HTML — historical/reference only

## SEA coverage manifest

- **Sections mapped:** Abstract; Introduction; Methods; Results; Discussion; financial support; competing interests; references
- **Figures:** 0
- **Tables:** 2
- **Algorithms/workflows:** 0
- **Appendices/supplements:** none provided
- **Visual inspection:** all 4 PDF pages rendered and inspected
- **Table reconciliation:** Table 1 and Table 2 reconstructed as structured HTML
- **Omissions:** bibliography entries were not independently appraised; no main-text figure/table/workflow was omitted

## SEA external currency verification

Because the source makes practice-facing antimicrobial stewardship claims, current official guidance was checked under the SEA v4 currency rule:

- IDSA 2025 Guideline Update on Complicated Urinary Tract Infections
- IDSA 2026 Guidance on the Treatment of Antimicrobial Resistant Gram-Negative Infections

The SEA artifact labels this information as external verification and keeps it separate from source-reported findings.

## SEA QA status

- Self-contained HTML: **PASS**
- Required TOC anchors resolve: **PASS**
- Exact source identity/DOI included: **PASS**
- Main-text tables reconciled: **PASS (2/2)**
- Final appraisal performed after source/table extraction: **PASS**
- Claims separated from appraisal: **PASS**
- External verification clearly labeled: **PASS**
- No internal chat/file citation syntax in HTML: **PASS**
- No TODO/placeholders/planning language: **PASS**

## Generated files

- `ash.2026.10794-atoms.json`
- `ash.2026.10794-sea.html`
- `ash.2026.10794-validation.md`
