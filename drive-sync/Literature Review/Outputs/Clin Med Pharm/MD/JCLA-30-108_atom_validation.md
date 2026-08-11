# LiteratureAtom Extraction and Validation Report — JCLA-30-108.pdf

## Source metadata

- **Title:** Influence of Body Mass Index on the Activated Clotting Time Under Weight-Based Heparin Dose
- **Authors:** Xia Hong; Pei-Ren Shan; Wei-Jian Huang; Qian-Li Zhu; Fang-Yi Xiao; Sheng Li; Hao Zhou
- **Journal:** Journal of Clinical Laboratory Analysis 30:108-113 (2016)
- **DOI:** 10.1002/jcla.21823
- **Primary source file:** JCLA-30-108.pdf
- **SHA-256:** `a4d86d317112d75a647b7a7174733b834d32f976b3a91ac7cdfa9fbb216ce6e2`
- **Publication ID:** `a9d49f76-f014-5bf9-b7a7-e9f90112d5bb`
- **Source type:** Primary journal article; single-center nonrandomized pharmacodynamic study of a fixed 100 U/kg UFH loading dose stratified by BMI quartile.

## Atom counts

- **Total atoms:** 36
- `author_conclusion`: 2
- `conflict_of_interest`: 1
- `eligibility_criterion`: 1
- `intervention_description`: 1
- `limitation`: 1
- `method`: 5
- `other`: 3
- `outcome_definition`: 2
- `population_description`: 2
- `qualitative_result`: 4
- `quantitative_result`: 13
- `study_objective`: 1

### Assertion origin
- `calculated_from_reported_data`: 3
- `directly_reported`: 6
- `extractor_inference`: 3
- `normalized_from_source`: 24

## Validation

- Pydantic structural validation: **PASS** (36/36 instantiated)
- Supplied `literature_atom.schema.json` validation: **PASS**
- Sufficiency validation: **PASS**
- Sufficiency warnings: **0**

## Extraction limitations and source consistency findings

- The article contains no main-text figures; all four main-text tables were inspected from rendered PDF pages.
- Table 1 contains an apparent internal inconsistency: Group A BMI is printed as `57.70 ± 5.72 kg/m²`, duplicating the weight value and contradicting the stated Group A BMI range. This was preserved as an extractor-inference atom rather than silently corrected.
- The prose percentages for ACT peak time do not match the reported counts for 5 and 10 minutes. Separate calculated-from-reported-data atoms preserve the count-derived percentages.
- Several Table 2 ΔACT means are not arithmetically consistent with the displayed group mean ACT minus ACT0, especially ΔACT10. Values were preserved as printed and separately flagged.
- Only male patients were enrolled; the paper does not establish generalizability to women.
- Clinical bleeding or thrombotic outcomes were not the study endpoints; ACT and ΔACT were pharmacodynamic surrogate measures.
- The paper does not report a funding statement or a data-availability statement in the inspected text. No such details were invented.
- The route of the 100 U/kg heparin loading dose is not explicitly stated in the extracted article text; the atom therefore does not normalize it to IV.

## Output contract

- JSON file contains an array of 36 serialized `LiteratureAtom` objects. Each object independently validates against the supplied schema and Pydantic model.
