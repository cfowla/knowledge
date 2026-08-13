# ofag510 ATOM Coverage and Extraction Notes

## Source identity
- **Title:** Absence of Mycoplasma genitalium Strains Simultaneously Harboring Wild-Type gyrA, parC, and 23S rRNA Genes in Japan: Next-Generation Sequencing-Based Surveillance
- **Journal:** Open Forum Infectious Diseases
- **Type:** Brief report; observational molecular antimicrobial-resistance surveillance
- **DOI:** 10.1093/ofid/ofag510
- **Evaluated file:** `ofag510.pdf`
- **Publication identity:** `887bb891-63f8-52b8-a0a0-9a71b7edc0b9`
- **SHA-256:** `3d38b76e1a856dc4b76617c8410ff4768750331d0c0c633ccda89e170decf44e`

## Source map
- Page 1: title/authors, lead summary, beginning of background
- Pages 2-3: background and Methods; start of Results
- Pages 3-4: Results
- Pages 4-6: Discussion, limitations, conclusion, notes/data availability
- Pages 7-8: references
- Pages 9-10: Table 1, individual gyrA/parC/23S rRNA variants
- Page 11: Table 2, three-gene resistance-pattern combinations
- Main-text figures: none
- Main-text tables: 2 (Table 1 spans pp. 9-10; Table 2 p. 11)
- Main-text workflows/algorithms: none

## Supplementary-material status
The article explicitly references a Supplementary Figure, Supplementary Tables 1 and 2, and Supplementary Methods. These items are **not embedded** in the evaluated 11-page PDF and no separate companion file was present in the requested source folder. The extraction therefore does not invent primer sequences, detailed NGS protocols, or the supplementary clinic-location figure.

## ATOM coverage
- Extracted atoms: **66**
- Atom kinds: {"author_conclusion": 4, "conflict_of_interest": 1, "data_availability": 1, "funding_disclosure": 1, "limitation": 4, "method": 6, "population_description": 3, "qualitative_result": 1, "quantitative_result": 35, "study_objective": 1, "subgroup_result": 9}
- Covered: objective, population, sampling/anonymization, sequencing/statistics methods, study-specific mutation definitions, NGS success, Table 1 variant prevalence, statistically significant sex/city comparisons, Table 2 resistance patterns, dual-class prevalence, no-triple-wild-type result, limitations, author conclusions, data availability, funding, and conflicts.
- Not atomized as primary-study evidence: prevalence estimates from cited external studies and literature-derived treatment-response statements in the Discussion.

## Validation
- Pydantic structural validation: **PASS**
- JSON schema serialization validation: **PASS**
- Atom-kind sufficiency validation: **PASS**
- Sufficiency warnings: **0**
- Review status: `needs_review` (machine extraction; no human source verification claimed)

## Important interpretation boundary
The study is molecular surveillance. It did not report phenotypic antimicrobial susceptibility testing or treatment outcomes. The paper's resistance-associated categories, including its broad fluoroquinolone mutation definition, are retained as source-defined classifications rather than converted into phenotypic resistance claims.
