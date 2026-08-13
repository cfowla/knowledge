# NEJMoa010713 ATOM validation report

## Source metadata

- Title: A Randomized Trial of the Angiotensin-Receptor Blocker Valsartan in Chronic Heart Failure
- Citation: N Engl J Med. 2001;345(23):1667-1675
- DOI: 10.1056/NEJMoa010713
- Publication ID: `cf58caef-8eeb-5a5a-a43f-f27347d0bac0`
- SHA-256: `14fb89f077b0dd1747b48b684bc39713a965499edd374d381e86d0e5ffbcadbd`
- PDF pages: 9

## Atom counts

- Total validated atoms: **51**

- `adverse_event`: 6
- `author_conclusion`: 3
- `comparator_description`: 1
- `conflict_of_interest`: 1
- `eligibility_criterion`: 2
- `funding_disclosure`: 1
- `intervention_description`: 1
- `limitation`: 4
- `method`: 8
- `outcome_definition`: 3
- `population_description`: 2
- `qualitative_result`: 5
- `quantitative_result`: 10
- `study_objective`: 1
- `subgroup_result`: 3

## Validation status

- Structural/Pydantic errors: **0**
- JSON Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

## Extraction limitations

- No corresponding correction or supplement was listed by the user for this source.
- Eligibility exclusion criteria were referenced by the article as published previously and were not reproduced in this PDF; they were not invented.
- Figure 4 exact subgroup relative-risk point estimates were not numerically tabulated in the PDF; atoms retain only values explicitly stated in text or tables.
- Atoms are structurally/sufficiency validated but remain review_status=needs_review because no independent human verification was performed.

## Output

- `NEJMoa010713-atoms.json` contains the validated LiteratureAtom objects as a JSON array.
- Every atom has the same publication identity and source-document hash; every atom has a source page/section/table/figure anchor.

## SEA coverage and QA

- Source type: Peer-reviewed randomized controlled clinical trial
- Main-text figures reconciled: **4/4** (all embedded source crops)
- Main-text tables reconciled: **2/2** (all structured blocks)
- Algorithms/workflows: none reported in the article.
- Appendix: investigator list condensed/omitted from narrative because it does not alter trial interpretation.
- References: not condensed; used as provenance infrastructure only.
- SEA semantic/mechanical QA: **PASS**
- HTML size: 411,430 bytes; TOC anchors missing: 0; embedded figure crops: 4.
- Current-practice statements in the SEA are explicitly separated from source-derived findings and were externally verified against AHA/ACC/HFSA sources.
