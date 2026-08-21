# Metoprolol Population Pharmacokinetics in Older Chinese Patients With CKM Syndrome — Clinical / PK Extraction

**Verified citation:** Chai H, Sia JEV, Hu D, Jia Y, Hu S, Wu X, Liu D, Lai X, Cui C. *Metoprolol Population Pharmacokinetics in Older Chinese Patients With CKM Syndrome: Joint Effects of rs1065852 and CKM₂S₂-BAG Score on Clearance.* Clinical and Translational Science. 2026;19(8):e70677. doi:10.1111/cts.70677. PMID:42496093. PMCID:PMC13398154.

**Publication timing:** August 2026 issue. An independent article index reports July 24, 2026 as the online publication date; the publisher full-text landing page was not retrievable through the current route, so that online date is retained with moderate rather than primary-source verification confidence.

## Source-access boundary

The authoritative PubMed record supplied the citation, author abstract, conflict statement, and captions for Figures 1–3. The publisher/PMC full text and parameter tables were not retrievable through the current web route. Full-text-specific details below are therefore separated as **externally corroborated detailed extraction** from a contemporaneous technical summary of the article; they were not promoted into primary-source ATOM fields unless independently exposed by PubMed.

## Population and data

- 42 older Chinese adults, age 60–93 years, with cardiovascular-kidney-metabolic (CKM) syndrome receiving immediate-release metoprolol tartrate.
- Detailed indexed summary: 83 sparse plasma trough samples; metoprolol doses 6.25–50 mg twice daily, with most patients receiving 12.5–25 mg twice daily.
- Detailed indexed summary: 21 participants were age 60–74 and 21 were age 75 or older; 28.6% had rs1065852 T/T; the T-allele frequency was 0.49; median CKM₂S₂-BAG score was 11 and 42.9% had a score >11.
- The observational source cohort was linked in the detailed summary to Peking University Third Hospital and ClinicalTrials.gov NCT05893849.

## Population-PK model

### Primary-source supported

- One-compartment disposition with first-order absorption and elimination.
- Candidate covariates: demographics, genetic polymorphism, laboratory variables, comorbidities, frailty phenotype, SARC-F, age-adjusted Charlson Comorbidity Index, CKM stage, and CKM₂S₂-BAG score.
- rs1065852 T/T and CKM₂S₂-BAG >11 were the reported clearance covariates.
- CL/F interindividual variability decreased from 46.9% in the model without these final covariates to 39.9% after their inclusion.

### Externally corroborated full-text detail

- NONMEM 7.4.4 using FOCEI.
- Absorption rate constant (Ka) fixed at 0.235 h⁻¹ from prior elderly metoprolol data.
- Interindividual variability modeled exponentially; residual unexplained variability modeled proportionally.
- Stepwise covariate modeling used likelihood-ratio testing with forward inclusion P<0.05 and backward elimination P<0.01.
- Model evaluation included GOF plots, nonparametric bootstrap (1000 replicates), and VPC (1000 simulated datasets).
- A two-compartment model did not materially improve fit over the final one-compartment structure according to the detailed indexed summary.

## Covariate effects and parameter estimates

- **rs1065852 T/T:** approximately 32% lower apparent clearance (detailed summary: 31.8% reduction; covariate estimate −0.318; RSE 50%).
- **CKM₂S₂-BAG >11:** approximately 30% lower apparent clearance (detailed summary: 30.2% reduction; covariate estimate −0.302; RSE 34%).
- **Joint high-risk stratum:** detailed summary reports CL/F 60.0 L/h for T/T + score >11 versus 126 L/h for the reference stratum lacking both features, corresponding to a 52.4% lower model-predicted CL/F.
- **IIV in CL/F:** 46.9% → 39.9% after inclusion of the two final covariates (7.0 percentage-point absolute decrease; about 14.9% relative decrease in the CV value). This is **not** an R² or a direct estimate of “percent variance explained.”
- Typical V/F, residual-error estimate, shrinkage, objective-function changes for each retained covariate, and bootstrap confidence intervals for all model parameters were not recoverable from the accessible primary record and should not be invented.

## Diagnostics

- **Figure 1:** GOF panels compare observed concentrations with individual and population predictions and CWRES with predictions and time; LOESS trend lines are shown.
- **Figure 2:** VPC based on 1000 simulated datasets; observed and model-simulated medians and 5th/95th percentiles are compared on linear/log scales, including a magnified 14–16 h region.
- Detailed summary reports 99.4% bootstrap convergence and generally concordant VPC/GOF behavior. Because the full parameter table and bootstrap distribution were not directly available, model stability should be considered supported but incompletely independently audited.

## Dose simulations

Figure 3 directly documents four twice-daily doses (50, 25, 12.5, 6.25 mg) across four strata formed by rs1065852 (C/C or C/T vs T/T) and CKM₂S₂-BAG (≤11 vs >11). The simulations reference 8.0 ng/mL as a lower pharmacodynamic threshold and 16.95 ng/mL as a concentration associated in prior literature with increased fall risk.

The detailed indexed summary identifies five subgroup–dose combinations with median simulated troughs within the literature-derived range:

- C/C or C/T + score ≤11: 25 mg BID → 9.1 ng/mL.
- C/C or C/T + score >11: 25 mg BID → 15.7 ng/mL.
- T/T + score ≤11: 25 mg BID → 16.1 ng/mL.
- T/T + score ≤11: 12.5 mg BID → 8.0 ng/mL.
- T/T + score >11: 12.5 mg BID → 13.2 ng/mL.
- 50 mg BID exceeded the 16.95 ng/mL threshold in all simulated strata in the detailed summary.

These are model simulations against literature-derived concentration thresholds, not prospectively validated dose recommendations.

## Incremental value of rs1065852 and CKM₂S₂-BAG

The two covariates appear to provide complementary stratification: each is associated with an approximately 30% reduction in CL/F, while the joint T/T + high-score stratum was modeled at roughly half the reference-stratum clearance. Inclusion of the covariates reduced the CL/F IIV CV from 46.9% to 39.9%, indicating a meaningful but incomplete reduction in unexplained heterogeneity.

The evidence does **not** establish the independent incremental predictive value with the rigor expected for a clinical prediction model. The accessible sources do not provide cross-validated prediction error, external validation, covariate-specific ΔOFV in the final report, calibration, decision-curve analysis, or prospective dosing outcomes. Precision is also limited: the detailed indexed summary reports RSE 50% for the genotype effect and 34% for the score effect. CKM₂S₂-BAG was originally created as a cardiovascular-risk score rather than a PK construct, so its clearance association is best viewed as an exploratory proxy for multi-organ disease burden until replicated.

## Practice interpretation

This study is useful for hypothesis generation and for designing a prospective model-informed precision-dosing study. It is not sufficient to implement rs1065852/CKM₂S₂-BAG-guided metoprolol dosing in routine practice. The cohort is small, single-country, restricted to older CKM patients, based on sparse trough data, and uses only one CYP2D6 variant rather than comprehensive genotype-to-phenotype assignment. The simulated thresholds are literature-derived and clinical outcomes such as falls were not prospectively measured in this cohort.

## Conflicts and limitations

- Authors declared no conflicts of interest in the PubMed record.
- Detailed summary: small cohort; predominantly CKM stages 3–4; CYP2D6 inhibitor users excluded; genetic analysis limited to rs1065852; no non-Chinese validation; simulations based on PK thresholds rather than clinical outcomes.
- Authors explicitly call for prospective clinical-outcome validation and comprehensive CYP2D6 genotyping.

## Sources / provenance

Primary bibliographic record and primary abstract/figure captions: https://pubmed.ncbi.nlm.nih.gov/42496093/

Independent publication-date index: https://visualize.jove.com/42496093-Metoprolol-Population-Pharmacokinetics-in-Older-Chinese-Patients-With-CKM-Syndrome-Joint-Effects-of-rs-and-CKMsubsubSsubsubBAG-Score-on-Clearance

Detailed secondary technical summary used only where explicitly labeled: https://www.ebiotrade.com/newsf/2026-7/20260727000320196.htm

Study registry context: https://clinicaltrials.gov/study/NCT05893849
