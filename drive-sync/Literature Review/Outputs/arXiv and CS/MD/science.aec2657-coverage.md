# science.aec2657 - Coverage and Validation Notes

## Source coverage manifest

```text
SOURCE COVERAGE MANIFEST
source_id: science.aec2657 / DOI 10.1126/science.aec2657
exact_title: Generative design of bacteriophages with genome language models
source_type: Primary research article; computational generative genomics + experimental synthetic biology
journal_date_version: Science 393 (6811), eaec2657; 6 August 2026; submitted 12 September 2025; accepted 2 June 2026
primary_file: science.aec2657.pdf
source_hash_sha256: 376b29048d3fed2d7f9df0538c86d967231f56b3bdd7fbe214e70c2362be5246
pdf_pages: 14 total (summary page + 12-page article + article landing/copyright page)
substantive_article_pages: PDF pages 2-13 (article pages 1-12); PDF page 1 is Research Article Summary; PDF page 14 is landing/copyright page
sections_or_headings:
  - Research Article Summary: Introduction / Rationale / Results / Conclusion (PDF p1)
  - Introduction / background and study framing (article p1; PDF p2)
  - Evo generates realistic bacteriophage genomic sequences (article pp1-2; PDF pp2-3)
  - Generative design of bacteriophages with target host tropism (article pp2-4; PDF pp3-5)
  - Creating viable generated bacteriophage genomes (article pp4-5; PDF pp5-6)
  - Generated bacteriophages reveal sequence and structural insights (article pp4-7; PDF pp5-8)
  - Generated bacteriophages exhibit a broad range of fitness profiles (article pp7-8; PDF pp8-9)
  - Generated bacteriophages rapidly overcome bacterial resistance (article pp7-9; PDF pp8-10)
  - Discussion (article pp8-10; PDF pp9-11)
  - References and notes (article pp10-12; PDF pp11-13)
  - Acknowledgements / funding / competing interests / data, code, materials availability (article p12; PDF p13)
figures:
  - Figure 1: Evo generates realistic bacteriophage genomic sequences (article p2; PDF p3)
  - Figure 2: Generative design of bacteriophages with target host tropism (article p3; PDF p4)
  - Figure 3: Creating viable generated bacteriophage genomes (article p5; PDF p6)
  - Figure 4: Generated bacteriophages reveal sequence and structural insights (article p6; PDF p7)
  - Figure 5: Generated bacteriophages exhibit a broad range of fitness profiles (article p8; PDF p9)
  - Figure 6: Generated bacteriophages rapidly overcome bacterial resistance (article p9; PDF p10)
tables: none in main text
algorithms_or_workflows:
  - Figure 2A six-step design pipeline
  - Figure 2H filtering/evaluation cascade
  - Figure 3D experimental validation/rebooting workflow
  - Figure 5D pooled coinfection fitness assay workflow
  - Figure 6C serial-passage resistance/counter-resistance workflow
appendices_or_supplements:
  - Primary PDF states supplementary materials contain Materials and Methods, Supplementary Text, Figs. S1-S30, Table S1, References 93-140, MDAR checklist, Data S1.
  - Per task instruction, no supplementary source material is specified; these are not fetched or used as evidence.
visual_strategy:
  structured_blocks: Figures 1-6 and all embedded workflows listed above
  embedded_crops_or_screenshots: none required; captions and rendered figures are sufficiently interpretable for structured extraction
  omitted_with_reason: supplementary figures/tables are out of scope by user instruction; bibliography is provenance rather than a synthesis target
coverage_decision: Full main-article coverage with all six main-text figures reconciled; no main-text tables; supplementary methods/results explicitly excluded.
omissions:
  - Detailed Materials and Methods are only in supplementary materials and therefore not evaluated.
  - Supplementary Text, Figs. S1-S30, Table S1, MDAR checklist, and Data S1 are not used.
  - Bibliographic entries are not individually summarized.
```

## @ATOM validation summary

- Structural validation (Pydantic `LiteratureAtom`): **PASS** (68 atoms; 0 errors)
- Serialization contract validation (`literature_atom.schema.json`): **PASS** (68 atoms; 0 errors)
- Sufficiency validation (`validate_literature_atom_sufficiency`): **PASS** (0 errors; 0 warnings)
- Review status: atoms remain `needs_review`; validation is not equivalent to human source verification.

### Atom counts by kind

- `author_conclusion`: 6
- `conflict_of_interest`: 1
- `data_availability`: 1
- `funding_disclosure`: 1
- `limitation`: 3
- `method`: 16
- `population_description`: 1
- `qualitative_result`: 20
- `quantitative_result`: 18
- `study_objective`: 1

### Assertion origins

- `calculated_from_reported_data`: 1
- `directly_reported`: 27
- `normalized_from_source`: 40


## Extraction limitations

1. Only `science.aec2657.pdf` was used as the primary article. The Drive folder also contains supplementary files, but the task explicitly specified no corresponding supplementary source material, so those files were not fetched or used as evidence.
2. The primary article states that detailed Materials and Methods, Supplementary Text, Figs. S1-S30, Table S1, MDAR checklist, and Data S1 are in supplementary materials. Claims that depend on those materials could not be independently reconciled beyond what the primary article itself reports.
3. Range-only numeric statements that do not map cleanly to the current single-estimate `QuantitativeResult` model are retained as reviewable qualitative-result atoms rather than forcing an invented midpoint or central estimate.
4. Appraisal judgments (for example, narrow external validity, lack of in vivo therapeutic validation, and possible training-set/memorization concerns) are kept in the SEA artifact and are not converted into reported-data atoms.

## @SEA coverage decision

- Main-text figures reconciled: **6/6** (Figures 1-6), all represented as structured blocks.
- Main-text tables: **0**.
- Main-text workflows represented: Figure 2A design pipeline; Figure 2H filtering cascade; Figure 3D experimental validation; Figure 5D pooled-competition workflow; Figure 6C serial-passage resistance workflow.
- Supplementary figures/tables: explicitly out of scope for this task.
- Final SEA scoring occurs only after the full main article and all six main figures were reviewed.
