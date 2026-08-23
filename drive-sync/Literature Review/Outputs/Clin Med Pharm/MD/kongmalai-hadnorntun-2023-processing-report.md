# Processing Report - Kongmalai Hadnorntun 2023

Source: Comparative cardiovascular benefits of individual SGLT2 inhibitors in type 2 diabetes and heart failure: a systematic review and network meta-analysis of randomized controlled trials

- PMID: 38179304
- DOI: 10.3389/fendo.2023.1216160
- Primary article SHA-256: `bf20fe6789a003a23efc88216d1989503f5b4e25a307c8910779c2cf69946fb9`
- Supplement SHA-256: `6cabae1b71caab1517b7ce330ca925d634875d8d18cf0c742caf5eff1ca87ad8`
- LiteratureAtoms: 104
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Exact duplicate canonical statements: 0
- SEA QA: PASS
- References extracted: 48

## Coverage

Reconciled 4 main-text figures, 3 main-text tables, all 8 supplementary tables, and all supplementary figure families S1-S8 in the supplied 39-page data sheet.

## Source-consistency flags

- Narrative follow-up maximum 3.6 years versus Table 1 value 4.2 years for DECLARE-TIMI 58.
- Narrative female-percentage range begins at 2.3%, inconsistent with Table 1 values around 22.3%-44.36%.
- All-cause mortality text calls canagliflozin RR 0.76 (0.58-1.00) significant, while Table 3 does not mark it significant and the abstract/discussion say only dapagliflozin reached significance.
- Discussion safety wording conflicts with results that show statistically significant SAE reductions and a canagliflozin any-AE increase.
- HF-specific sensitivity text reports no significant head-to-head differences; Supplementary Table S7 should be interpreted with its row/column direction before reusing active-agent contrasts.

## Extraction boundary

This publication is a systematic review/network meta-analysis, not a primary trial. Trial-level numerical results extracted as atoms are tagged `secondary_reported_result` and remain anchored to this review. No underlying trial result is represented as if Kongmalai et al. generated the original patient-level data.
