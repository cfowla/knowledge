# NEJMoa0802987 processing report

## Activated workflows

- @ATOM
- @SEA

## Source metadata

- Primary article: **Intensive Blood Glucose Control and Vascular Outcomes in Patients with Type 2 Diabetes**
- Group author: The ADVANCE Collaborative Group
- Journal: *New England Journal of Medicine*
- Citation: 2008;358:2560-2572
- DOI: 10.1056/NEJMoa0802987
- Trial registration: NCT00145925
- Primary file: `NEJMoa0802987.pdf` (13 pages; SHA-256 `cd9b345f0db7a63a0b52f6f36fbaf42f827d86db89fe24467249b5cdeeee97e8`)
- Supporting file: `NEJMoa0802987-supplemental.pdf` (15 pages; SHA-256 `201c8c4c9e11330070f833466ea99b3d49ecdde3631ba4fc97fa0196ab2a276a`)

## ATOM extraction

- Publication identity: `c15798d3-d7b2-5ce8-84c7-3d8f4257ce8b`
- Total independently reviewable atoms: **36**
- Structural validation: **PASS** — 0 Pydantic errors
- Serialization-schema validation: **PASS** — 0 JSON Schema errors
- Sufficiency validation: **PASS** — 0 errors, 0 warnings
- Review status in serialized atoms: `extracted`

### Atom counts by type

- `adverse_event`: 2
- `author_conclusion`: 1
- `comparator_description`: 1
- `eligibility_criterion`: 1
- `funding_disclosure`: 1
- `intervention_description`: 2
- `limitation`: 2
- `method`: 5
- `outcome_definition`: 4
- `population_description`: 1
- `qualitative_result`: 1
- `quantitative_result`: 14
- `study_objective`: 1

## Source coverage used for extraction

Primary article assertions were extracted from the objective, eligibility/design, treatment strategies, endpoint definitions, statistical methods, baseline population, achieved glycemic separation, primary and secondary vascular outcomes, renal components, safety outcomes, subgroup analysis, limitations, conclusion, and funding disclosure. The supplement was used where it materially clarified the intervention algorithm, HbA1c standardization, blood-pressure separation, and end-of-follow-up insulin use.

Pure collaborator rosters in the supplement were treated as provenance/administrative material rather than evidence atoms. No study detail absent from the article or supplement was invented. Appraisal judgments were not serialized as reported evidence.

## SEA coverage manifest

- Main-text sections: Abstract; Introduction; Methods; Results; Discussion; funding/conflict disclosures; references.
- Main-text table: Table 1 (baseline and end-of-follow-up characteristics/treatments) — structured extraction.
- Main-text figures: Figure 1 enrollment; Figure 2 glucose-control trajectories; Figure 3 cumulative incidence curves; Figure 4 prespecified outcomes forest plot; Figure 5 subgroup forest plot — all reconciled as structured text blocks in HTML.
- Supplementary material used: intensive glucose-control algorithm; HbA1c standardization; Supplementary Figure 1 (blood pressure); Supplementary Table 1 (diabetes management); Supplementary Table 2 (hospitalizations).
- Supplement collaborator-center roster: omitted from narrative condensation because it does not change methods, outcomes, safety, or interpretation; multicenter scope is retained in the Methods summary.
- Representation strategy: structured reconstruction only; screenshots were not embedded because the quantitative/semantic content of the included visuals was recoverable from the rendered PDF and extracted text.

## Extraction limitations

The atom schema does not contain a publication-metadata wrapper, so source-level bibliographic metadata are reported here rather than inserted into each atom. Some source statements (for example, retinopathy) are represented with normalized structured estimates to preserve independently reviewable outcome context. The supplement reports end-of-follow-up denominators that differ from the randomized denominators because they reflect participants with available final-visit data; those denominators were preserved rather than imputed.

## QA status

- Raw primary PDF still present before SEA: **yes**
- Raw supplemental PDF still present before SEA: **yes**
- SEA generated only after source mapping and visual/table reconciliation: **yes**
- Final HTML is self-contained with embedded CSS and no external scripts/fonts/images: **yes**
- Internal chat/file citation syntax inside HTML: **none**
- TODO/placeholders/planning language: **none detected**
