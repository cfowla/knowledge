# archinte_154_13_011 - ATOM Validation and SEA Coverage Report

## Source metadata

- **File:** `archinte_154_13_011.pdf`
- **Title:** Use of a Standardized Heparin Nomogram to Achieve Therapeutic Anticoagulation After Thrombolytic Therapy in Myocardial Infarction
- **Authors:** Greg C. Flaker; John Bartolozzi; Vicki Davis; Carolyn McCabe; Christopher P. Cannon; for the TIMI 4 Investigators
- **Citation:** *Arch Intern Med.* 1994;154:1492-1496
- **Source type:** Journal article; interim analysis of the first 217 TIMI 4 participants, with a nonrandomized center-level comparison of heparin-nomogram implementation
- **Google Drive source ID:** `18v8ofCy3usPE78bRwO0KzzxUVy0vQYvb`
- **SHA-256:** `8b51c5c44021f6d738fce65257f151ba780ebfd55a4ab5549b273bef125901f5`
- **Publication UUID:** `a892dcc3-806a-5c03-812d-4d85a890fff0`
- **Extraction run:** `archinte_154_13_011-atom-v1`

## ATOM extraction summary

- **Total atoms:** 64
- **Structural validation:** PASS (64/64 Pydantic-valid)
- **JSON Schema validation:** PASS (0 errors against `literature_atom.schema.json`)
- **Sufficiency validation:** PASS (0 errors; 0 warnings)
- **Review status:** all atoms marked `needs_review` because extraction was language-model generated and has not been human-verified.

### Atom counts by kind

- `adverse_event`: 7
- `author_conclusion`: 5
- `eligibility_criterion`: 3
- `funding_disclosure`: 2
- `intervention_description`: 9
- `limitation`: 3
- `method`: 6
- `outcome_definition`: 3
- `population_description`: 1
- `qualitative_result`: 1
- `quantitative_result`: 23
- `study_objective`: 1

## Assertion-origin handling

- Source-supported paraphrases are labeled `normalized_from_source`.
- Explicit calculations from reported values are labeled `calculated_from_reported_data` (for example, mean differences and risk differences).
- No appraisal judgments were encoded as reported study data.

## SEA coverage manifest

- **Sections covered:** structured abstract; introduction/background; Methods; Results; Comment/discussion; funding/support notes.
- **Figures:** Figure 1, Figure 2, Figure 3 - all reconciled.
- **Study tables:** Table 1 and Table 2 - both reconciled.
- **Operational workflow:** Table 1 treated as the heparin dose-adjustment algorithm.
- **Other table:** publisher SI-to-conventional hemoglobin conversion table omitted from study-evidence extraction because it is not study data.
- **Page 1496 investigator/center listing:** treated as administrative provenance rather than an empirical section; not atomized except for study support/sponsor information reported on page 1495.
- **Figure 3:** embedded as a source crop in the SEA HTML because exact bar values are not printed in the prose/table; only the source-reported significance at 48 and 96 hours was atomized.

## Extraction limitations

1. The TIMI 4 thrombolytic regimens were randomized, but **use of the heparin nomogram was not randomly assigned to centers**; the article itself identifies this as a confounding limitation.
2. Figure 3 shows bar heights for nomogram vs non-nomogram centers, but exact percentages are not numerically printed. Approximate visual readings were not promoted into quantitative atoms.
3. Some time-point aPTT denominators are shown only in Figure 1; the Figure 2 percentage series does not print a denominator for each bar. No unsupported denominator transfer was made.
4. Reinfarction and reocclusion group comparisons were not statistically interpretable because of small event numbers; this is retained as a limitation atom rather than over-interpreted.
5. The source reports limited uncertainty information (mostly P values; no confidence intervals for the center comparison).
6. This is a 1994 article. The SEA treats its heparin regimen and nomogram as **historical evidence**, not a current dosing standard. Contemporary ACS guidance was checked only for currency context, not used to rewrite the study results.

## QA

- Raw PDF retained locally during both ATOM and SEA passes: **yes**.
- PDF visually rendered and inspected: **yes, 5/5 pages**.
- ATOM structural validation: **PASS**.
- ATOM sufficiency validation: **PASS**.
- SEA coverage gate completed before HTML generation: **PASS**.
- SEA HTML internal citation/tool markers: **none**.
- SEA HTML TODO/placeholder/planning-language scan: **PASS**.

Generated 2026-08-12 09:59 UTC.
