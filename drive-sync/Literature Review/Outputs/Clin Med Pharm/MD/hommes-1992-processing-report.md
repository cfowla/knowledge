# Processing Report - Hommes et al. heparin meta-analysis

## Activated workflows

- `@ATOM`
- `@SEA`

## Source identity

- Drive filename: `hommes-et-al-2008-subcutaneous-heparin-compared-with-continuous-intravenous-heparin-administration-in-the-initial.pdf`
- PDF-internal title: **Subcutaneous Heparin Compared with Continuous Intravenous Heparin Administration in the Initial Treatment of Deep Vein Thrombosis: A Meta-analysis**
- Authors: Daan W. Hommes; Alessandra Bura; Lucia Mazzolai; Harry R. Buller; Jan W. ten Cate
- Publication: *Annals of Internal Medicine*. 1992;116:279-284.
- PDF pages: 6
- SHA-256: `13665783266d3436453d1f5abd34f8232dbf0c057eb31559be32b82e89a174e8`
- Note: the Drive filename contains “2008,” but the PDF itself identifies a 1992 publication. Source-internal metadata governs.

## @ATOM validation report

- Publication UUID: `d595c096-bdbf-5d45-8598-d6122b8917b3`
- Extraction run: `hommes-1992-meta-analysis-v1`
- Atoms: **53**
- Structural / JSON-schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

### Atom counts by kind

- `study_objective`: 1
- `population_description`: 1
- `quantitative_result`: 15
- `author_conclusion`: 3
- `method`: 6
- `eligibility_criterion`: 1
- `outcome_definition`: 2
- `qualitative_result`: 9
- `adverse_event`: 10
- `limitation`: 4
- `funding_disclosure`: 1

### Assertion origins

- `normalized_from_source`: 49
- `directly_reported`: 4

### Semantic limitation

The governing LiteratureAtom implementation is explicitly oriented to primary literature, whereas this source is a meta-analysis. Trial-level efficacy and safety rows from Table 2 were therefore encoded as **secondary-reported results**, tagged `secondary_reported_result`, and anchored to the meta-analysis rather than represented as if Hommes et al. directly enrolled those participants. No appraisal statements were converted into reported-data atoms.

## @SEA coverage manifest

- Source type: systematic overview + meta-analysis
- Substantive pages: PDF pages 1-5 (printed pages 279-283)
- Bibliography: PDF page 6 (printed page 284)
- Sections/headings: structured abstract; introduction; Methods - Identification of Clinical Studies; outcome definitions; Systematic Overview; six methodologic standards; Meta-analysis; Results - Systematic Overview; Meta-analysis results; Discussion; acknowledgments/funding; references
- Tables: Table 1, Table 2
- Figures: Figure 1 (efficacy forest plot), Figure 2 (safety forest plot)
- Algorithms/workflows: none
- Appendices/supplements: none in the retrieved PDF
- Representation: Tables 1-2 reconstructed as structured HTML tables; Figures 1-2 reconstructed as structured numerical/interpretive blocks because their load-bearing data are fully recoverable from Table 2
- Omission: individual bibliography entries were not condensed because they are provenance infrastructure rather than the article's empirical results

## SEA appraisal outcome

- Verdict: **Read soon for a heparin deep dive; do not use alone for current practice**
- Relevance: 9/10
- Novelty: 7/10
- Method strength: 6/10
- Evidence strength: 5/10
- External validity: 4/10
- Implementation value: 4/10

Primary caution: efficacy heterogeneity was significant (`P < 0.001`), trial effects were discordant, outcome definitions varied, and daily heparin dose was often higher in the subcutaneous arm. Safety remained imprecise (`RR 0.79`, 95% CI `0.42-1.48`).

## External current-practice verification

This material is **not part of the 1992 source extraction**. A current-context check used:

- Stevens SM, Woller SC, Baumann Kreuziger L, et al. *Antithrombotic Therapy for VTE Disease: Compendium and Review of CHEST Guidelines 2012-2021.* Chest. 2024;166(2):388-404. DOI: `10.1016/j.chest.2024.03.003`.

The contextual check was used only to prevent historical route-comparison evidence from being misread as current choice-of-agent guidance.

## QA

- Raw PDF retained locally through both ATOM and SEA: **yes**
- ATOM Pydantic construction: **pass**
- LiteratureAtom JSON schema validation: **pass**
- Sufficiency validation: **pass**
- SEA coverage manifest completed before HTML generation: **pass**
- Main-text tables/figures reconciled: **4/4**
- HTML self-contained CSS/scripts/resources: **pass**
- Internal chat/file citation syntax in HTML: **none**
- TODO/placeholder/planning language scan: **pass**
