# ATOM Validation Report — `mayoclinproc_84_12_005.pdf`

## Source metadata

- **Title:** Effect of Body Mass Index on Bleeding Frequency and Activated Partial Thromboplastin Time in Weight-Based Dosing of Unfractionated Heparin: A Retrospective Cohort Study
- **Authors:** Seth R. Bauer, PharmD; Narith N. Ou, PharmD; Benjamin J. Dreesman, PharmD; Jeffrey J. Armon, PharmD; Jan A. Anderson, PharmD; Stephen S. Cha, MS; Lance J. Oyen, PharmD
- **Journal:** Mayo Clinic Proceedings. 2009;84(12):1073-1078.
- **DOI:** `10.4065/mcp.2009.0220`
- **Source file:** `mayoclinproc_84_12_005.pdf`
- **Drive source ID:** `1UVQ-8QJmb--qoee2_HHYRUF6yiYOuQ2G`
- **PDF SHA-256:** `c0fb55228790e40b30f013f853dc2dab3f6ae8bdc6b826b4f800a130f2774677`
- **Publication UUID:** `f0993987-c99c-51c4-8af6-1b0fb4b07b31`
- **Extraction run:** `mayoclinproc_84_12_005-atom-v1`
- **Extraction time:** 2026-08-12T08:57:39.799318+00:00

## Atom counts

**Total atoms:** 76

### By atom kind
- `adverse_event`: 8
- `author_conclusion`: 3
- `eligibility_criterion`: 4
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 5
- `method`: 12
- `outcome_definition`: 4
- `population_description`: 1
- `qualitative_result`: 3
- `quantitative_result`: 30
- `study_objective`: 1
- `subgroup_result`: 3

### By assertion origin
- `calculated_from_reported_data`: 3
- `directly_reported`: 29
- `normalized_from_source`: 44

## Validation

- **Pydantic structural validation:** PASS — 76/76 atoms round-trip validated.
- **JSON Schema serialization validation:** PASS — each atom conforms to `literature_atom.schema.json`.
- **Sufficiency validation:** PASS — 0 errors, 0 warnings.
- **Review status:** `extracted` (not independently human-verified).

## Coverage manifest

- **Sections:** structured abstract; Introduction; Patients and Methods (Definitions, Heparin Dosing and Monitoring, Outcomes, Statistical Analyses); Results (Primary and Exploratory analyses); Discussion; Conclusion; References.
- **Tables:** 4/4 represented.
- **Figures:** 2/2 represented.
- **Workflow/algorithm:** Table 1 UFH dosing nomogram represented.
- **Supplements/appendices:** none identified.
- **References:** bibliography not atomized.

## Extraction limitations and source issues

1. The source reports the cohort period as February 1, 2002 through **November 31, 2003**, an invalid calendar date. This was preserved as source-reported and tagged `source_date_inconsistency`; no silent correction was made.
2. The paper is a retrospective single-center cohort with BMI-stratified comparisons, not a randomized or direct capped-vs-uncapped dosing comparison. Atoms preserve the authors' conclusions as `author_conclusion` rather than converting them into stronger causal claims.
3. The study did not measure thromboembolic efficacy outcomes and states that it was underpowered for infrequent efficacy events.
4. Prior UFH exposure before nomogram initiation could not be fully determined, and concomitant antithrombotic exposure could not be established as balanced across BMI quartiles.
5. Multi-group tables/figures sometimes lack a single source-reported effect estimate. Structured atoms therefore retain group values and source P values; calculated contrasts are explicitly marked `calculated_from_reported_data`.
6. Figure-derived bleeding counts and APTT percentages were visually reconciled against rendered PDF pages before extraction.

## Protocol source note

The governing project file is named `summary-evaluation-appraisal-protocol-v4-compact.md`, but its internal heading identifies itself as “Integrated Compact v3.” Per project precedence, the v4-named file was treated as authoritative.
