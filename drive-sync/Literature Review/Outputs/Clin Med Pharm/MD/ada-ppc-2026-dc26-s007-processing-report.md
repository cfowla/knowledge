# Processing report: 7. Diabetes Technology: Standards of Care in Diabetes—2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s007.pdf`  
DOI: `10.2337/dc26-S007`  
SHA-256: `ce75fb8fbd82ae5e97839758548315da07add4b599274def7ab7d3ad246bb32a`

## ATOM

- LiteratureAtoms: 97
- Shared publication ID: `6429a224-328f-5817-90b7-4502196a3eca`
- Atom counts by kind: `{"author_conclusion": 52, "other": 36, "limitation": 5, "quantitative_result": 4}`
- Semantic batches: general principles 21; BGM 9; CGM 13; insulin delivery 5; AID 11; digital/inpatient 8; evidence 4; tables 26.
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate statement-anchor pairs: 0

Recommendations are represented as ADA panel statements using `author_conclusion` plus `guideline_recommendation` tags. Quantitative findings attributed to underlying trials, cohorts, reviews, and meter analyses are tagged `secondary_reported_result`. The chapter is not represented as if it enrolled those study populations.

## SEA

- Source type: clinical practice guideline / Standards chapter
- Substantive coverage: S150-S161 through The Future
- Figures reconciled: 0/0
- Tables reconciled: 4/4, Tables 7.1-7.4
- Formal recommendations: 7.1-7.30, including lettered subrecommendations
- External ADA methodology document: not supplied; limitation preserved
- Verdict: `Read first`
- SEA QA: PASS

## Reference task queue

- Bibliography entries extracted: 193
- P0 direct evidence for central technology efficacy, safety, accuracy, access, or implementation claims: 115
- P1 current high-value supporting evidence: 60
- P2 contextual, historical, or supporting evidence: 18
- Bibliography entries were not atomized.

## Extraction limitations and schema gaps

- The LiteratureAtom schema has no dedicated `guideline_recommendation` atom kind. Formal recommendations use `author_conclusion` with descriptive tags.
- Recommendation evidence grades are preserved in tags rather than a dedicated typed field.
- The full ADA guideline-development method and evidence-grade definitions are in the separate Introduction and Methodology, which was not supplied with this section.
- All atoms remain `needs_review` because this run does not represent an independent human verification step.
- No external current-practice or regulatory verification was performed because `@VERIFY` was not activated.

## Protocol note

The project designates `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing SEA source. Its internal heading identifies Integrated Compact v3. The v4-named project source was followed as authoritative, and the naming mismatch was recorded rather than silently reconciled.

## Output files

JSON folder:
- `ada-ppc-2026-dc26-s007-atoms.json` - https://drive.google.com/file/d/10aLZa5_YFUhY__R5BryTHa1LkgxcsZ3t/view
- `ada-ppc-2026-dc26-s007-validation.json` - https://drive.google.com/file/d/1zC07RHMW8NS_rPcGu-ukfS6RON7jfAlO/view
- `ada-ppc-2026-dc26-s007-coverage.json` - https://drive.google.com/file/d/1IHFLhPuG5OLSQzJXxfHYAUvM9GWQM8iJ/view
- `ada-ppc-2026-dc26-s007-crosswalk.json` - https://drive.google.com/file/d/1qsLVsruOmKlEYQRcZ2YNHgTdnxMFNlCa/view
- `ada-ppc-2026-dc26-s007-sea-qa.json` - https://drive.google.com/file/d/1Pxj10HpRTSizvTJdO4HCJl7y0iNAljlg/view

HTML folder:
- `ada-ppc-2026-dc26-s007-sea.html` - https://drive.google.com/file/d/119kIuEOZT-2pkg_NCtI-omIsDTyRBQlQ/view

Markdown folder:
- `ada-ppc-2026-dc26-s007-reference-task-queue.md` - https://drive.google.com/file/d/1g_qZHSZrNCqAAsdujnEEFQSrPb3uonRF/view
- `ada-ppc-2026-dc26-s007-processing-report.md`

## Drive lifecycle and state

- `dc26s007.pdf` moved from `10 - Active Literature / 1 - American Diabetes Association 2026` to `90 - Processed / Clinical Medicine & Pharmacy / 47 - American Diabetes Association 2026`.
- Destination parent was verified after the move.
- A live post-move folder read showed 12 ADA section PDFs remaining because another ADA section was processed concurrently during this run.
- `TBR - Current Task Queue` was reconciled to the live folder state and now records 12 remaining ADA section PDFs in both the Active Literature snapshot and Actionable work list.
