# dkag282 @SEA source coverage manifest

## Source identity

- **Source ID:** `dkag282`
- **Exact title:** Inter- and intraindividual variability of long-acting injectable cabotegravir/rilpivirine trough concentrations after 1 year of continuous use
- **Source type:** Journal article; prospective observational pharmacokinetic cohort study
- **Journal / citation:** *Journal of Antimicrobial Chemotherapy* 2026; 81: dkag282
- **DOI:** 10.1093/jac/dkag282
- **Primary file:** `dkag282.pdf`
- **Primary file length:** 5 pages
- **Primary source boundary:** Primary article only. No correction or supplementary file was specified for this task.

## Sections / headings mapped

1. Title / authors / affiliations / publication metadata
2. Structured abstract: Objectives, Methods, Results, Conclusions
3. Introduction
4. Methods
5. Results
6. Discussion
7. Acknowledgements
8. Funding
9. Transparency declarations
10. Supplementary data notice
11. References

## Figures

- **Figure 1:** Individual participant trough concentrations at Visits 1–3 for (a) cabotegravir and (b) rilpivirine, with 4×PA-IC90 reference lines.
  - **Coverage decision:** Include as an embedded crop/screenshot because individual longitudinal trajectories and threshold crossings are layout-dependent and not faithfully reducible to prose alone.
  - **Source location:** PDF page 3.

## Tables

- **Table 1:** Characteristics associated with cabotegravir or rilpivirine trough concentrations less than 4× protein-adjusted 90% inhibitory concentrations.
  - **Coverage decision:** Reconstruct as a structured HTML table, preserving group denominators, values, units, and P-values.
  - **Source location:** PDF page 3.

## Algorithms / workflows

- None in the main text.

## Appendices / supplements

- The article states that **Table S1** is available as supplementary data at JAC Online.
- **Coverage decision:** Not retrieved or substituted. The task explicitly specifies no corresponding correction or supplementary source material. The missing supplement is disclosed as a coverage limitation.

## Visual strategy

- **Embedded crop/screenshot:** Figure 1.
- **Structured reconstruction:** Table 1.
- **Omitted with reason:** Supplementary Table S1 — not supplied/specified for the task.

## Coverage decision

Full main-text coverage: abstract, introduction, methods, results, discussion, acknowledgements, funding, transparency declarations, supplementary-data notice, Figure 1, and Table 1. Pure bibliography entries are not individually condensed because they are provenance infrastructure rather than findings of this primary study.

## Known source-level issues / cautions

- Main text reports **8 participants (17%)** with at least one detectable HIV-RNA value; the main text does not clarify the denominator implied by 17%. This is preserved as reported rather than silently recalculated.
- The transparency statement uses the initials **J.M.D.**, which do not directly correspond to a listed author name in the article header. The initials are preserved without identity inference.
