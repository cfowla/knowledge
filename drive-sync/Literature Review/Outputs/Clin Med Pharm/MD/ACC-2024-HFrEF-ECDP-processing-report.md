# ACC-2024-HFrEF-ECDP processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Main source: *2024 ACC Expert Consensus Decision Pathway for Treatment of Heart Failure With Reduced Ejection Fraction*
- Citation: Maddox TM, Januzzi JL Jr, Allen LA, et al. *J Am Coll Cardiol.* 2024;83(15):1444-1488.
- DOI: `10.1016/j.jacc.2023.12.024`
- Main PDF: 45 pages, SHA-256 `ea88d6b231e10159f33d7c36c8a1b10f5afc55e156aa013bd0e8f2d42640e645`
- Supplemental appendix: 15 pages, SHA-256 `a038778a38d15743a827e237455b7944fa8de56b7adcf2c14e4b137147763111`
- Shared publication ID: `6327d6a7-e707-565b-ad78-828ce1aca3a5`

## ATOM result

- LiteratureAtoms: **142**
- Atom kinds: `{'study_objective': 1, 'other': 129, 'limitation': 4, 'method': 4, 'author_conclusion': 2, 'conflict_of_interest': 2}`
- Semantic batches: `{'acc-hfref-2024-global-v1': 15, 'acc-hfref-2024-gdmt-initiation-v1': 33, 'acc-hfref-2024-optimization-monitoring-v1': 28, 'acc-hfref-2024-coordination-adherence-v1': 14, 'acc-hfref-2024-special-populations-access-v1': 15, 'acc-hfref-2024-complexity-comorbidity-v1': 26, 'acc-hfref-2024-palliative-conclusion-v1': 9, 'acc-hfref-2024-governance-disclosure-v1': 2}`
- Assertion origin: `{'normalized_from_source': 142}`
- Shared publication identity: **PASS**
- Unique atom IDs: **PASS**
- Local Pydantic contract validation: **PASS**
- Local generated JSON Schema validation: **PASS**
- Local sufficiency check for extracted generic kinds: **PASS**
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Review status: all atoms remain `needs_review`

The source is an expert consensus decision pathway. Practical guidance is represented as `atom_kind="other"` with descriptive tags because the recovered project pattern has no dedicated expert-consensus recommendation kind. Trial effects summarized in the ECDP remain secondary evidence and were not promoted to primary-study quantitative-result atoms.

## SEA result

All 45 main-source pages and all 15 supplemental pages were rendered and inspected. Four of four main figures, 15 of 15 main tables, and both supplemental tables were reconciled. The appraisal was performed after source mapping and ATOM extraction.

The ECDP is strongest as an implementation companion for rapid four-pillar HFrEF therapy, titration, monitoring, referral, adherence, medication access, team-based care, and palliative integration. Its core pharmacotherapy draws on strong randomized evidence. Many implementation questions and special-population decisions remain partly consensus-based.

Local project-pattern scores, not claimed as execution of the unavailable named SEA v4 rubric:

- Relevance: **10/10**
- Novelty at publication: **9/10**
- Method strength: **7/10**
- Evidence strength: **8/10**
- External validity: **8/10**
- Implementation value: **10/10**

## Source-integrity findings

1. Figure 1 describes Issue 8 as having ten pathophysiologic targets and ten management principles. Section 4.8 states that Table 14 contains 12 targets and enumerates Principles 1 through 11. The discrepancy was preserved.
2. Section 4.1.4 and Section 4.2.2 give different SGLT inhibitor eGFR initiation thresholds. The mismatch was flagged rather than reconciled.
3. The ECDP says its algorithms may be superseded by new data and should not override clinical judgment.

## References

- Main article bibliography: **273** numbered references
- Supplemental Preface and Methods references: **5**
- Supplemental Table 2 references: **4**
- Bibliographic entries were not atomized.

## Governing-source execution boundary

The supplied `large-source-ATOM-SEA.md` workflow and retrieved `unslop.skill.md` were applied. The named authoritative ATOM files `literature.py`, `literature_atoms.py`, `literature_atom.schema.json`, `README(2).md`, and `example_atom.json`, plus `summary-evaluation-appraisal-protocol-v4-compact.md`, were searched in connected project sources but were not directly retrievable in this session.

Structural and serialization checks therefore use a strict local Pydantic contract and generated JSON Schema reconstructed from current validated project artifacts plus the large-source guardrail. This run does not claim execution of unavailable authoritative project code or the exact SEA v4 scoring rubric.

No external current-practice verification was performed because `@VERIFY` was not activated.

## Output files

- `ACC-2024-HFrEF-ECDP-atoms.json`
- `ACC-2024-HFrEF-ECDP-validation.json`
- `ACC-2024-HFrEF-ECDP-coverage.json`
- `ACC-2024-HFrEF-ECDP-sea.html`
- `ACC-2024-HFrEF-ECDP-references.md`
- `ACC-2024-HFrEF-ECDP-processing-report.md`
