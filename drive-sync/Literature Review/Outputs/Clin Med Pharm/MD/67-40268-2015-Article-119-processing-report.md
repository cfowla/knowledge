# Processing report: 67 - 40268_2015_Article_119

Activated macros: @ATOM, @SEA.

## Source

- File: `40268_2015_Article_119.pdf`
- Title: Safety of Epidural Corticosteroid Injections
- DOI: 10.1007/s40268-015-0119-3
- Design: systematic review
- PDF pages: 16
- SHA-256: `8db8e2d220c5347d83470c062d51ad76350185181e5944a77cbfebded997d953`
- Google Drive source ID: `17YL8oTTCMiRiD8zqM5Y75SXPGAJmtJso`

## ATOM

- Atom count: 65
- Kinds: `{"author_conclusion": 10, "conflict_of_interest": 1, "eligibility_criterion": 1, "funding_disclosure": 1, "limitation": 6, "method": 4, "other": 26, "qualitative_result": 1, "quantitative_result": 11, "study_objective": 1, "subgroup_result": 3}`
- Semantic batches: `{"40268-2015-adverse-events-v1": 17, "40268-2015-approach-results-v1": 19, "40268-2015-interpretation-v1": 19, "40268-2015-review-design-v1": 10}`
- Pydantic structural validation: PASS
- JSON Schema validation: PASS
- Sufficiency validation: PASS
- Structural errors: 0
- Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0

This source is secondary literature. Selected numerical findings from cited studies are tagged `secondary_reported_result` and remain anchored to this review. They do not become primary-study evidence atoms.

## SEA

All 16 PDF pages were rendered and visually scanned. The two main figures and three main tables were reconciled. Final appraisal occurred after section and visual extraction. The article is best used as a historical safety map and citation source, not as a current incidence estimate or current practice standard.

## Source integrity findings

1. Results prose says 162 papers met inclusion criteria, while Figure 1 says 159. The reported 58 studies plus 101 case reports also totals 159.
2. Table 1, Manchikanti et al. 2014, prints percentages that do not match the listed counts if 688 injections is the denominator.
3. Table 3, Manchikanti et al. 2012, prints some percentages that do not match the listed counts if 1,310 injections is the denominator.
4. Infection-frequency statements differ between section 4.5 and the Discussion and were not reconciled by the source.

No discrepancy was silently repaired.

## References

The article contains 210 numbered references. They were exported to `67-40268-2015-Article-119-references-task-queue.md`. Bibliography entries were not atomized.

## Governing sources

ATOM precedence was followed: `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, `README(2).md`, then `example_atom(1).json` as illustrative only. SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing file. Its internal heading says Integrated Compact v3, but project precedence designates the v4-named file as authoritative. `large-source-ATOM-SEA.md` guided coverage and secondary-source handling. `unslop.skill.md` controlled prose style.

No external verification was performed because @VERIFY was not activated.
