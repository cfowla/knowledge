# Large-Source Manifest - 112 - dddt-15-4503

## Source identity

- **Exact title:** Anti-Inflammatory Effects of Curcumin in the Inflammatory Diseases: Status, Limitations and Countermeasures
- **Source type:** narrative review
- **Published:** 2021-11-02
- **Journal:** Drug Design, Development and Therapy 2021;15:4503-4525
- **DOI:** 10.2147/DDDT.S327378
- **Google Drive file ID:** 1jPud4caUn42VYfpiRmPmtC6j5s1EsUs_
- **SHA-256:** `b1033c0684caa96583446fbd65ee526995ce46fdd7f841742402cb83f868b5b3`
- **Page count:** 23
- **Substantive range:** journal pages 4503-4519
- **Reference range:** journal pages 4519-4524
- **Non-substantive:** journal page 4525 publisher advertisement

## Source map

**Headings:** Introduction, Anti-Inflammatory Mechanism of Curcumin, Anti-Inflammatory Effects of Curcumin in Several Inflammatory Diseases, Effect of Curcumin on Inflammatory Bowel Disease, Effect of Curcumin on Arthritis, Effect of Curcumin on Psoriasis, Effect of Curcumin on Depression, Effect of Curcumin on Atherosclerosis, Effect of Curcumin on COVID-19, Limitations and Countermeasures of Curcumin in the Treatment of Diseases, Limitations, Countermeasures, Derivatives and Prodrugs of Curcumin, Pharmaceutical Strategies, Combination Drug Therapy, Conclusion, Abbreviations, Acknowledgments, Disclosure, References

**Figures:** 4 main-text figures, all represented in SEA as structured descriptions.

**Tables:** 2 main-text tables, all 49 rows represented in SEA; row-level reports are also encoded as secondary-reported LiteratureAtoms.

**Algorithms/workflows:** none identified.

**Appendices/supplements:** none present in the evaluated PDF.

## Semantic batch plan

- **batch-00-general-mechanism** - pages 4503-4505: Front matter, introduction, curcumin anti-inflammatory mechanisms, Figures 1-2
- **batch-01-ibd-tables** - pages 4506-4510: Cross-disease overview, IBD, Table 1, Table 2, Figure 3
- **batch-02-arthritis-psoriasis** - pages 4510-4512: Arthritis and psoriasis evidence
- **batch-03-depression-atherosclerosis-covid** - pages 4512-4514: Depression, atherosclerosis, COVID-19
- **batch-04-limitations-countermeasures** - pages 4514-4516: Pharmacokinetic limitations, Figure 4, derivatives and prodrugs
- **batch-05-formulations-combination-conclusion** - pages 4517-4519: Pharmaceutical strategies, combination therapy, conclusion, acknowledgments/disclosure

## Coverage decision

All substantive narrative sections, all four figures and both tables were inspected. References were treated as provenance infrastructure rather than ATOM targets and were converted to a separate **184-item Markdown task queue**. The page-4525 journal advertisement was omitted.

## ATOM guardrail for this source

The governing LiteratureAtom model is primary-literature oriented, whereas this source is a narrative review. Study-level rows from Tables 1 and 2 are therefore represented as the **review's secondary report** of cited studies, tagged `secondary_reported_result` and `ref_N`. They are not presented as if this review enrolled participants or generated those findings.

## Protocol source version note

The project file designated `summary-evaluation-appraisal-protocol-v4-compact.md` identifies itself internally as **Integrated Compact v3**. The designated file was followed as governing, and the naming/version mismatch is recorded rather than silently resolved.

## Extraction limitations

- The source is a narrative review, not a primary study. ATOM therefore captures the review authors’ synthesis and table-reported secondary evidence with explicit secondary-source tags.
- The review rarely provides effect estimates, confidence intervals, denominators, or complete trial design details in its summary tables; directional outcomes were not converted into quantitative_result atoms.
- Pure bibliography entries were excluded from atomization and were instead converted into the separate 184-item reference task queue.
- The publisher advertisement on page 4525 was excluded as non-substantive content.
- No external evidence was used to upgrade or correct the review’s clinical claims; COVID-19 claims are preserved as historical 2021 source content.
