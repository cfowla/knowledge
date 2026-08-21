# cts.70667 — Clinical / pharmacometrics extraction

## Verified citation and publication metadata

Svyatova EA, Liu Z, Becker RE, Sung JM, Fayomi AP, Florian JA, Weaver JL, Rouse R, Howard KE. **Anti-PEG Antibodies From mRNA COVID-19 Vaccines Affect In Vitro Measurements of Pegylated Drug Levels.** *Clinical and Translational Science*. 2026;19(8):e70667. doi:10.1111/cts.70667. PMID: 42477513. PMCID: PMC13385214. **First published:** 2026-07-20. **Issue:** August 2026.

Primary full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC13385214/

## Study question

The investigators asked whether anti-PEG antibodies are increased after SARS-CoV-2 vaccination and whether anti-PEG-positive human serum interferes with in-vitro measurement of pegfilgrastim. The source is a laboratory/bioanalytical study using commercial de-identified serum, not an in-vivo PK or clinical-outcomes study.

## Assay methods

- **Anti-poly-PEG IgG:** commercial ELISA using poly-methoxy PEG-40K-BSA capture antigen.
- **Anti-mono-PEG IgG:** commercial ELISA using mono-methoxy PEG-20K-BSA capture antigen.
- **G-CSF ligand-binding assay:** anti-G-CSF capture/detection ELISA; calibration 200–6000 pg/mL; pegfilgrastim spike 2000 pg/mL.
- **G-CSF-receptor cell-based assay:** AML-193 cells; calibration 1000–60,000 pg/mL; serum diluted 1:5; anti-PEG monoclonal detection plus Alexa Fluor 488 anti-IgG; flow-cytometric readout; principal spike 7000 pg/mL.
- **Mechanistic depletion:** PEG-2000-linked polystyrene beads removed anti-PEG IgG before repeat drug-detection assays.
- **Competitive saturation:** three donor sera tested over increasing pegfilgrastim spikes to assess whether higher drug concentration overcame interference.
- **Statistics:** 4-parameter logistic curves; standards within ±20% expected and R² ≥0.990; one-way ANOVA with Tukey multiple comparisons; simple linear regression for correlation analyses.

## Main findings

### Anti-PEG response

At the single-time-point assessment, median anti-poly-PEG IgG titers were 5,911 ng/mL in controls, 12,373 ng/mL after mRNA-1273, 6,158 ng/mL after BNT162b2, and 6,473 ng/mL after Ad26.COV2.S. The Results narrative reports the mRNA-1273 group as significantly higher than all other groups at p<0.01, whereas the Figure 1 caption denotes ***p<0.0001 versus all other groups; this internal source discrepancy should not be silently reconciled.

In the 15-person longitudinal mRNA-1273 set, 8/15 had >100% anti-poly-PEG increases two weeks after the second dose, 7/15 had >600% increases six weeks after the second vaccination, and approximately one-third reached at least a 10-fold increase from baseline. At 32 weeks, 3/15 remained >1500% above baseline and 3/15 remained >100% above baseline. BNT162b2 cohorts did not show a group-level increase; three participants with pre-existing antibodies increased after vaccination. One of 14 Ad26.COV2.S recipients developed a measurable anti-PEG response despite that vaccine lacking PEG.

### Pegfilgrastim assay interference

With a **7000 pg/mL** pegfilgrastim spike in the cell-based assay, median measured concentrations were 7,696 pg/mL in controls, 6,246 after mRNA-1273, 7,566 after BNT162b2, and 7,377 after Ad26.COV2.S. About **15%** of the mRNA-1273 group had >50% loss of drug detection; no other group exceeded 2% at that degree of loss.

With a **2000 pg/mL** spike in the G-CSF ELISA, median measured concentrations were 2,078 pg/mL in controls, 1,952 after mRNA-1273, 2,157 after BNT162b2, and 2,264 after Ad26.COV2.S. Higher anti-poly-PEG titers generally tracked with lower recovery, but titer was not a perfect functional predictor.

### Mechanism and concentration dependence

Anti-PEG depletion restored pegfilgrastim recovery in low-detection sera and did not materially alter anti-PEG-negative serum, supporting antibody-mediated interference rather than a generic serum-matrix effect. In the three-donor saturation experiment, the cell-based assay remained vulnerable at concentrations relevant to lower-dose studies: donor 1 was near 100% recovery at 160 ng/mL but <50% at 40 ng/mL; donor 2 was 70% at 160 ng/mL and <25% at 40 ng/mL; donor 3 reached full recovery at 80 ng/mL. The ligand-binding ELISA recovered to 80%–120% for all three at about ≥8 ng/mL.

## Mechanistic interpretation

The ligand-binding ELISA does not rely on PEG-specific detection, so reduced recovery is consistent with anti-PEG antibodies sterically interfering with access to pegfilgrastim. The cell-based assay also uses an anti-PEG detection antibody and therefore has an additional plausible vulnerability: endogenous anti-PEG antibodies can both alter receptor-accessible drug and hinder the assay's PEG-directed detection step. Restoration after anti-PEG depletion is the strongest causal experiment in the paper.

## PK / drug-development implications

These results identify a **bioanalytical matrix-interference risk**, not proof of altered systemic exposure. For PK, biosimilarity, or comparability work with PEGylated products, especially at lower/subclinical doses, anti-PEG-positive samples could bias measured concentrations downward and increase apparent PK variability. That could jeopardize equivalence conclusions even when true exposure is unchanged.

Reasonable development responses include pre-screening or characterizing anti-PEG status, using orthogonal anti-PEG assays, performing spike/recovery and depletion experiments in method validation, avoiding assay architectures that are unnecessarily PEG-dependent, and prespecifying sensitivity analyses when anti-PEG interference is plausible. These are appraisal/implementation implications, not outcomes directly tested by this study.

## Limitations

- Only pegfilgrastim was tested; generalization to other PEGylated products is uncertain.
- No in-vivo PK, clearance, efficacy, or clinical dosing outcome was measured.
- Commercial serum availability determined sample sizes and collection schedules; vaccine status was vendor-provided/self-reported.
- Longitudinal cohorts were small, especially for Ad26.COV2.S.
- Anti-PEG titer alone did not reliably classify functional interference.
- The cell-based assay may amplify apparent interference because it uses an anti-PEG detection antibody.
- Supporting DOCX files were inventoried but not independently parsed in this run; the main article reports their roles and key linked findings.

## Practice boundary

Do **not** interpret this paper as evidence that a patient needs a pegfilgrastim dose change after mRNA vaccination. It supports assay-awareness during drug development and may justify investigating anti-PEG antibodies when unexplained analytical recovery problems occur. Clinical loss of efficacy and altered clearance remain untested.
