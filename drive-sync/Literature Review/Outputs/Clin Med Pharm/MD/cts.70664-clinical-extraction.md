# cts.70664 — Clinical / pharmacometrics extraction

## Verified citation and publication metadata

Kang M, Choi S, Park S-S, Han S, Han S. **A Simulation-Based Assessment of Dosage Regimen Appropriateness for Multiple Myeloma Medicines Reflecting Demographic and Ethnic Differences.** *Clinical and Translational Science*. 2026;19(8):e70664. doi:10.1111/cts.70664. PMID:42515832. PMCID:PMC13408018. **First published:** 2026-07-27. **Issue:** August 2026, volume 19, issue 8.

## Source basis and access boundary

The primary basis for this extraction is the author abstract plus four primary figure captions exposed through the PubMed record. The publisher/PMC full-text route was not retrievable during this run. Detailed model equations, complete tables, exact trial/Korean real-world sample sizes, exact regimen doses, supplements, and full discussion text are therefore not asserted below unless supported by the accessible primary material.

## Study objective

The study asks whether demographic and regional differences between multinational multiple-myeloma clinical-trial populations (TP) and Korean patients (KP), represented with Korean real-world demographic data, could produce clinically relevant differences in modeled drug exposure and downstream predicted response. The work is positioned as a model-informed way to identify where formal pharmacokinetic or focused bridging evaluation may be worth prioritizing when conventional bridging studies are difficult in an orphan disease.

## Simulation framework

- Representative drugs from major multiple-myeloma treatment classes were selected when usable population-PK models were available.
- Covariate distributions from the source clinical-trial populations were compared with Korean real-world patient covariates.
- Population-model simulations compared key exposure metrics between TP and KP.
- A **≥10% exposure difference** was the trigger for additional efficacy or safety evaluation.
- Figure 2 shows simulated concentration-time profiles and Cmax distributions with mean curves and 5th–95th percentile prediction intervals.
- Figure 3 applies a sigmoid Emax exposure-response relationship between carfilzomib AUC and predicted overall response rate (ORR) for two approved regimens.
- Figure 4 relates ln(AUC) distributions to hematologic adverse-event severity and marks TP/KP median ln(AUC).

## Drugs and regimens evaluated

The accessible primary material identifies five therapies: **daratumumab, carfilzomib, lenalidomide, melphalan, and panobinostat**. Two approved carfilzomib dosing regimens were simulated in the efficacy analysis. Exact dose values for those regimens were not recoverable from the accessible primary route and are intentionally not reconstructed.

## Demographic / physiologic covariates

Figure 1 identifies drug-specific covariate distributions showing greater than 10% differences between TP and KP. The exposed caption includes **weight, body-surface area (BSA), fat-free mass (FFM), and creatinine clearance (CrCl)** across the daratumumab, carfilzomib, panobinostat, lenalidomide, and melphalan comparisons. This matters because the population-PK models translate different covariate distributions into different simulated exposure distributions rather than treating ethnicity itself as a direct causal dosing variable.

## Exposure targets and downstream evaluation

The source reports concentration-time profiles, Cmax, and AUC-based analyses. The core operational threshold is not a therapeutic target concentration but a **between-population exposure difference of at least 10%**, after which published exposure-response or exposure-safety information is used to estimate possible clinical consequences.

## Results

- **Carfilzomib:** simulated exposure was approximately **12%–15% lower** in KP than TP across two dosing regimens. Applying published exposure-response information yielded an estimated **4%–9% lower predicted ORR** in KP.
- **Lenalidomide:** simulated exposure was approximately **25% higher** in KP. The corresponding modeled probability of grade ≥3 hematologic adverse events was approximately **1.27-fold higher**.
- **Daratumumab, melphalan, panobinostat:** no meaningful simulated exposure differences were observed between the compared populations.
- **Figure 4:** the caption reports a mean ln(AUC) difference of **0.89, p<0.001** across hematologic adverse-event severity groups; the full underlying dataset and model specification were not accessible in this run.

## Implications for fixed dosing and model-informed population evaluation

The study does **not** establish a direct dose-adjustment rule for Korean patients. Its practical implication is prioritization: fixed regimens may reproduce trial-like exposure reasonably for some agents while selected drugs can show modeled exposure shifts when the trial and target-population covariate distributions differ. That makes carfilzomib and lenalidomide candidates for closer PK/bridging scrutiny rather than automatic population-based dose changes.

For model-informed development, the reusable concept is the workflow itself: combine an established population-PK model with target-population real-world covariate distributions, simulate exposure under the approved regimen, apply a prespecified materiality threshold, and only then connect material exposure shifts to published exposure-response or safety functions. This is a screening/prioritization framework, not proof that a different fixed dose improves outcomes.

## Key limitations

### Study-level interpretive limits supported by the design

- Clinical consequences are **predicted from exposure-response/safety relationships**, not prospectively observed treatment outcomes in a Korean comparative trial.
- The analysis evaluates a Korean target population; the authors suggest possible relevance to broader East Asian evaluation, but broader regional generalization requires separate validation.
- A modeled exposure difference can identify a reason for further study but does not by itself prove that dosing should change.

### Extraction-access limits for this run

- Full model equations, parameter tables, sample sizes, and exact carfilzomib regimen doses were not available through the accessible primary route.
- Main-text tables and supplements could not be inventoried.
- The complete 21-reference bibliography could not be retrieved; the references file preserves only the subset exposed by the primary PubMed route.

## Bottom line

This is a useful pharmacometrics paper for **model-informed bridging triage**: it demonstrates that target-population covariate distributions can materially shift modeled exposure for some fixed-dose multiple-myeloma therapies while leaving others essentially unchanged. The strongest use is to decide **which drug/population pairs deserve additional PK or focused bridging work**, not to make a clinical dose change from simulation alone.
