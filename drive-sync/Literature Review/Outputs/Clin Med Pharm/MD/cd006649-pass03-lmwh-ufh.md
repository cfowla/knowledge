# CD006649 — SEA Pass 3: LMWH versus UFH

**Working file:** `cd006649-pass03-lmwh-ufh.md`  
**Source:** Kahale LA, et al. *Anticoagulation for the initial treatment of venous thromboembolism in people with cancer.* Cochrane Database of Systematic Reviews. 2021; Issue 12. Art. No. CD006649. DOI: 10.1002/14651858.CD006649.pub8.  
**Pass:** 3 — comparison-specific deep pass: low molecular weight heparin (LMWH) versus unfractionated heparin (UFH)  
**Scaffold:** `cd006649-pass00-global.md`  
**Methods context:** `cd006649-pass01-methods.md`  
**Evidence-base context:** `cd006649-pass02-evidence-base.md`  
**Primary source objects:** Summary of Findings 1, physical PDF pp. 5–6; Results/Discussion, pp. 17–18; Analyses 1.1–1.2, pp. 51–52; relevant included-study characteristics as needed  
**Final whole-source SEA scoring:** **DEFERRED**  
**External verification:** **Not performed**

> This pass reconciles the LMWH-versus-UFH evidence within the 2021 Cochrane review. It separates the review's reported findings from pass-level appraisal. It does not update the evidence beyond the source's August 2021 search and does not assign final whole-review SEA scores or a current-practice verdict.

---

# 1. Pass purpose

Pass 0 designated LMWH versus UFH as the largest comparison family and identified five questions for this pass:

1. Reconcile the **3-month mortality** relative effect, absolute effect, event counts, contributing studies, heterogeneity, and GRADE rating.
2. Reconcile the **3-month recurrent VTE** relative effect, absolute effect, event counts, contributing studies, heterogeneity, and GRADE rating.
3. Determine what the absence of **bleeding and other patient-important outcomes** does to comparative interpretation.
4. Reconcile the main mortality analysis with the broader **sensitivity analysis**.
5. Test whether the authors' conclusion that LMWH is "probably superior" to UFH is proportionate to the source's own quantitative evidence and certainty assessment.

Passes 1–2 established several constraints that remain active here:

- the source uses random-effects pooling and a complete-case primary analysis;
- all cancer evidence comes from cancer subgroups of broader VTE trials;
- cancer types were not specified;
- seven LMWH-versus-UFH trials relied on cancer-subgroup data recovered from prior systematic reviews and were therefore restricted to sensitivity analyses;
- most trials were open label;
- LMWH products, UFH regimens, treatment setting, and subsequent anticoagulation were heterogeneous;
- most initial randomized parenteral treatment lasted only about 5–10 days, whereas outcomes were assessed at about 3 months.

---

# 2. Pass 3 coverage manifest

## Source objects inspected

### Summary table
- **Summary of Findings 1 — Low molecular weight heparin compared with unfractionated heparin**
  - physical PDF pp. 5–6
  - printed review pp. 3–4

### Main-text results and interpretation
- **Effects of interventions — LMWH versus UFH**
  - physical PDF p. 17
  - printed review p. 15
- **Discussion / overall completeness / quality of evidence / previous reviews**
  - physical PDF p. 18
  - printed review p. 16
- **Authors' conclusions**
  - physical PDF pp. 18–19
  - printed review pp. 16–17

### Quantitative figures
- **Analysis 1.1 — Mortality at 3 months**
  - physical PDF p. 51
  - printed review p. 49
- **Analysis 1.2 — Any recurrent VTE at 3 months**
  - physical PDF p. 52
  - printed review p. 50

### Cross-referenced study-characteristics context
Relevant characteristics from Pass 2 were consulted for:
- Breddin 2001
- Hull 1992
- Merli 2001
- Prandoni 1992
- Prandoni 2004 (GALILEI)
- Simonneau 1993
- sensitivity-only LMWH-versus-UFH trials where needed for provenance/context

## Visual representation decision

Both forest plots are numerically recoverable from the source and are reconstructed below as structured tables rather than embedded screenshots. Their load-bearing content is:

- per-study event counts and denominators;
- per-study RRs and 95% CIs;
- study weights;
- pooled effect;
- heterogeneity statistics;
- overall-effect test.

No visual is omitted from this semantic pass.

---

# 3. Comparison architecture

The review includes **13 trials comparing an LMWH regimen with UFH**, but that number should not be confused with the number contributing to each primary pooled estimate.

For the principal analyses:

- **Mortality:** 5 RCTs, 418 cancer-subgroup participants.
- **Recurrent VTE:** 3 RCTs, 422 cancer-subgroup participants.

The main-analysis cancer-subgroup data used here had stronger provenance than the seven sensitivity-only trials:

| Study | Cancer-subgroup data provenance | Main outcome contribution |
|---|---|---|
| Breddin 2001 | follow-up publication | mortality; recurrent VTE |
| Hull 1992 | follow-up publication | mortality |
| Merli 2001 | follow-up publication | recurrent VTE |
| Prandoni 1992 | directly reported | mortality |
| Prandoni 2004 (GALILEI) | obtained from study authors | mortality; recurrent VTE |
| Simonneau 1993 | directly reported | mortality |

The seven LMWH-versus-UFH trials whose cancer-subgroup data were obtained from earlier systematic reviews were excluded from the main analysis and retained for sensitivity analysis. Two of these, Lindmarker 1994 and Lopaciuk 1992, were also abstract publications.

### Pass 3 appraisal

The phrase **"13 LMWH-versus-UFH trials"** overstates the direct evidentiary density of the principal outcome estimates if reported without qualification. The mortality result rests on five cancer-subgroup datasets; recurrent VTE rests on only three.

The evidence is therefore broader at the review-identification level than at the outcome-estimation level.

---

# 4. Mortality at 3 months

## 4.1 Source-reported pooled effect

Summary of Findings 1 and Analysis 1.1 agree on the principal mortality estimate:

- **5 RCTs**
- **418 participants**
- **RR 0.66**
- **95% CI 0.40 to 1.10**
- UFH baseline risk in the Summary of Findings table: **168 per 1,000**
- absolute effect with LMWH: **57 fewer deaths per 1,000**
- **95% CI: 101 fewer to 17 more per 1,000**
- **GRADE: low certainty**
- downgrade: **two levels for very serious imprecision**
- **59 total mortality events**

The Results section describes the finding as LMWH **"may reduce mortality"** at three months.

### Statistical reconciliation

Analysis 1.1 reports:

- LMWH: **27/228 deaths**
- UFH: **32/190 deaths**
- pooled RR: **0.66 (95% CI 0.40–1.10)**
- Tau² = **0.00**
- Chi² = **3.15**, df = 4, P = **0.53**
- I² = **0%**
- overall-effect test: Z = **1.59**, P = **0.11**

The total forest-plot event count is 59, matching the Summary of Findings footnote.

## 4.2 Analysis 1.1 — study-level reconstruction

| Study | LMWH events / total | UFH events / total | Weight | RR (95% CI) |
|---|---:|---:|---:|---:|
| Breddin 2001 | 14 / 84 | 6 / 41 | 33.4% | 1.14 (0.47–2.75) |
| Hull 1992 | 7 / 46 | 14 / 49 | 39.1% | 0.53 (0.24–1.20) |
| Prandoni 1992 | 1 / 15 | 6 / 18 | 6.4% | 0.20 (0.03–1.48) |
| Prandoni 2004 (GALILEI) | 3 / 76 | 5 / 80 | 13.3% | 0.63 (0.16–2.55) |
| Simonneau 1993 | 2 / 7 | 1 / 2 | 7.9% | 0.57 (0.09–3.51) |
| **Pooled** | **27 / 228** | **32 / 190** | **100%** | **0.66 (0.40–1.10)** |

### Forest-plot interpretation

The pooled point estimate favors LMWH, but the 95% CI includes:

- potentially important mortality reduction;
- no difference;
- some potential mortality increase.

The absence of statistical heterogeneity (**I² = 0%**) does not mean that all study estimates are equivalent. Breddin 2001 has a point estimate above 1.0, while the other four point estimates favor LMWH. The two largest weights are Hull 1992 and Breddin 2001, which together contribute roughly 72.5% of the random-effects weight and point in different directions.

The small number of studies and events also limits the ability of I² to establish true homogeneity.

### Pass 3 appraisal

The pooled estimate is **compatible with a clinically important mortality benefit**, but it is not precise enough to establish that benefit. The Summary of Findings judgment of **low certainty due to very serious imprecision** is well aligned with the width of the CI and the 59-event evidence base.

The source's Results wording, **"may reduce mortality,"** is therefore better calibrated to the numerical evidence than a definitive superiority statement.

---

# 5. Mortality sensitivity analysis

The Results section reports a broader mortality meta-analysis that added:

- Büller 1997 (COLOMBUS)
- Duroux 1991
- Koopman 1996
- Levine 1996
- Simonneau 1997 (THESEE)
- Lindmarker 1994
- Lopaciuk 1992

These studies were not used in the principal analysis because their cancer-subgroup data were not directly reported in the trial report/follow-up source or obtained directly from investigators; the latter two studies were also abstract publications.

The sensitivity result was:

- **RR 0.75**
- **95% CI 0.56 to 1.02**

The source states that the mortality result **did not change** when these studies were included.

### What "did not change" means here

The sensitivity analysis preserves the same qualitative interpretation:

- point estimate remains in the direction of lower mortality with LMWH;
- CI still crosses 1.0;
- the estimate remains statistically non-significant.

The point estimate moves from **0.66** to **0.75**, and the interval becomes narrower, but the source does not provide the participant denominator or event count for this sensitivity analysis in the inspected Results passage. Those values should not be invented.

### Pass 3 appraisal

This sensitivity analysis strengthens confidence that the **direction** of the pooled mortality estimate is not wholly dependent on the five-study main-analysis set. It does **not** convert the evidence into a demonstrated mortality benefit because the 95% CI remains compatible with no effect.

It also relies on a less direct evidence-provenance layer for seven studies:

**primary RCT → earlier systematic review → current Cochrane review**

Thus, the narrower interval should not be interpreted without the provenance tradeoff that motivated the main/sensitivity separation.

---

# 6. Recurrent VTE at 3 months

## 6.1 Source-reported pooled effect

Summary of Findings 1 and Analysis 1.2 agree on the recurrent-VTE estimate:

- **3 RCTs**
- **422 participants**
- **RR 0.69**
- **95% CI 0.27 to 1.76**
- UFH baseline risk: **96 per 1,000**
- absolute effect with LMWH: **30 fewer recurrent VTE events per 1,000**
- **95% CI: 70 fewer to 73 more per 1,000**
- **GRADE: low certainty**
- downgrade: **two levels for very serious imprecision**
- **34 total recurrent-VTE events**

The source states that LMWH **"may reduce VTE recurrence slightly."**

The review could not analyze recurrent DVT and recurrent PE separately because those event data were not available separately.

## 6.2 Analysis 1.2 — study-level reconstruction

| Study | LMWH events / total | UFH events / total | Weight | RR (95% CI) |
|---|---:|---:|---:|---:|
| Breddin 2001 | 4 / 84 | 7 / 41 | 33.9% | 0.28 (0.09–0.90) |
| Merli 2001 | 9 / 96 | 3 / 45 | 31.3% | 1.41 (0.40–4.95) |
| Prandoni 2004 (GALILEI) | 5 / 76 | 6 / 80 | 34.7% | 0.88 (0.28–2.76) |
| **Pooled** | **18 / 256** | **16 / 166** | **100%** | **0.69 (0.27–1.76)** |

Analysis 1.2 reports:

- Tau² = **0.31**
- Chi² = **3.70**, df = 2, P = **0.16**
- I² = **46%**
- overall-effect test: Z = **0.78**, P = **0.44**

## 6.3 Heterogeneity and study-level pattern

The recurrent-VTE estimate is less internally consistent than the mortality estimate:

- Breddin 2001 favors LMWH and its individual CI excludes 1.0.
- Merli 2001 has a point estimate favoring UFH.
- Prandoni 2004 is close to the null with a wide CI.
- the three studies have similar meta-analytic weights, so no single study completely dominates the pooled estimate.
- I² = 46% is consistent with **moderate statistical heterogeneity** in this sparse evidence set.

The pooled CI from 0.27 to 1.76 is very wide and spans substantial benefit through substantial harm.

### Pass 3 appraisal

The recurrent-VTE result is **not a stable demonstration of benefit**. The point estimate favors LMWH, but the evidence is sparse, the event count is only 34, individual trial directions differ, and moderate heterogeneity is present.

The GRADE downgrade for very serious imprecision is strongly supported by the width of the interval. The source's phrasing that LMWH **"may reduce VTE recurrence slightly"** should be read as a low-certainty directional interpretation rather than evidence of a reliably established reduction.

No comparison-specific recurrent-VTE sensitivity estimate analogous to the mortality sensitivity analysis is reported in the inspected Results section.

---

# 7. Missing safety and patient-important outcomes

For LMWH versus UFH, Summary of Findings 1 explicitly lists the following as **not reported** for the cancer subgroup:

- major bleeding;
- minor bleeding;
- quality of life;
- postphlebitic syndrome;
- thrombocytopenia.

The Results section likewise states that no data were available for bleeding outcomes, postphlebitic syndrome, quality of life, or thrombocytopenia.

### Why this is load-bearing

The absence of these outcomes means this comparison does **not** provide a complete direct benefit–harm assessment in the cancer subgroup.

This is particularly important because the review's own clinical question is framed around both **efficacy and safety**. Mortality and recurrent VTE can be summarized, but the principal LMWH-versus-UFH evidence cannot directly establish whether any efficacy signal is accompanied by:

- more or less major bleeding;
- more or less minor bleeding;
- differences in thrombocytopenia;
- downstream postphlebitic syndrome;
- quality-of-life effects.

### Pass 3 appraisal

The missing bleeding evidence materially limits any broad claim that LMWH is simply "superior" to UFH. A mortality-oriented superiority claim and an overall efficacy-and-safety superiority claim are not equivalent.

The source itself partially acknowledges this by recommending that treatment decisions balance benefits and harms and patient values, but the necessary cancer-subgroup harm data are absent from this comparison.

---

# 8. Risk-of-bias context for the contributing studies

Pass 2 showed that most included studies were judged low risk in most domains but were usually open label.

For the principal mortality studies:

- **Hull 1992** was one of the three studies in the entire review judged blinded for participants/personnel.
- **Breddin 2001, Prandoni 1992, Prandoni 2004, and Simonneau 1993** were judged not blinded for participants/personnel.
- outcome assessors were judged blinded for these studies.
- allocation concealment was judged adequate except in **Breddin 2001**, where it was not reported.
- Breddin reported approximately **91% cancer-subgroup follow-up**; the other principal mortality studies were reported as having complete follow-up.

For recurrent VTE:

- Breddin 2001 and Prandoni 2004 had the above characteristics.
- **Merli 2001** did not report cancer-subgroup follow-up information; the review analyzed available data assuming potentially missing data were missing at random.

### Missing-outcome sensitivity testing

The review's Methods planned missing-participant-data sensitivity analyses when a primary pooled result was statistically significant. Because none of the outcome estimates in this review were significant, the review states that it **did not perform sensitivity analyses for missing outcome data**.

### Pass 3 appraisal

Objective mortality and objectively confirmed recurrent VTE reduce some of the concern created by open-label treatment, especially with blinded outcome assessment. However:

- open-label care can still affect co-interventions, treatment setting, monitoring, and threshold for diagnostic evaluation;
- Breddin's incomplete follow-up and Merli's unreported cancer-subgroup follow-up matter because the outcome-specific evidence sets are small;
- the review's significance-triggered missing-data sensitivity framework means non-significant results did not receive the same formal missingness stress test.

These are limitations rather than proof of biased effect estimates.

---

# 9. Breddin 2001 denominator inconsistency

Pass 2 identified an unresolved source-internal denominator issue for Breddin 2001:

- included-studies narrative: **83** people with cancer;
- Characteristics table: **137** people with cancer in the broader subgroup;
- Analyses 1.1 and 1.2: **84 LMWH + 41 UFH = 125** participants represented in each forest-plot row.

The forest-plot values are internally sufficient for reproducing the pooled analyses and are therefore preserved exactly in this pass.

### Required handling

This pass does **not** infer which Breddin denominator is the "correct" global cancer-subgroup count. The discrepancy likely relates to the study's three-arm structure, but the Cochrane source sections inspected do not explicitly resolve the mapping.

For the LMWH-versus-UFH pooled effects, the relevant reported values are the forest-plot denominators and events.

---

# 10. Clinical heterogeneity beneath the class labels

Pass 2 established that "LMWH versus UFH" combines multiple regimens rather than one uniform drug comparison.

## LMWH heterogeneity

The 13 LMWH-versus-UFH trials include:

- reviparin;
- nadroparin;
- tinzaparin;
- enoxaparin;
- dalteparin.

Dose frequency varies from once daily to twice daily.

## UFH heterogeneity

UFH regimens vary by:

- intravenous versus partly subcutaneous administration;
- approximately 5–10 days of treatment;
- different aPTT targets or absolute aPTT ranges.

## Treatment-setting heterogeneity

Several trials contrasted:

- subcutaneous LMWH managed at home or as an outpatient;
- intravenous UFH administered in hospital.

Thus, some comparisons are partly **drug-plus-delivery-strategy comparisons**, not pharmacologically isolated drug comparisons.

## Subsequent anticoagulation

In 14 of 15 included studies, initial parenteral therapy was followed by oral anticoagulation for at least three months, usually a vitamin K antagonist.

### Pass 3 appraisal

This treatment architecture matters especially for the mortality result. The randomized LMWH/UFH exposure generally lasted only the initial days of therapy, while mortality was measured at three months after substantial exposure to subsequent anticoagulation.

A 3-month mortality difference can still be causally related to early treatment, but the source cannot be interpreted as a three-month randomized comparison of LMWH versus UFH monotherapy.

The class-level pooled estimate also averages across multiple LMWH products, UFH protocols, VTE phenotypes, and care settings.

---

# 11. Applicability to "people with cancer"

The review's cancer population is not clinically well resolved.

The source states that:

- all cancer participants were **subgroups** of broader VTE trials;
- none of the studies specified the cancer types of the participants;
- planned subgroup analyses by participant characteristics could not be performed;
- 11 additional potentially eligible studies had cancer subgroups but lacked usable cancer-specific outcome data;
- those 11 studies could have contributed approximately **340 additional participants** to the review.

The source also acknowledges that restricting electronic retrieval to cancer terminology may be problematic when the needed data arise from broader VTE trials not restricted to cancer populations.

### Pass 3 appraisal

The LMWH-versus-UFH result supports an inference about a historically assembled, heterogeneous collection of cancer subgroups, not a clearly characterized contemporary cancer-associated-thrombosis population.

The review cannot establish whether the effect differs by:

- solid versus hematologic malignancy;
- cancer site or histology;
- stage;
- prognosis;
- thrombocytopenia;
- active cancer therapy;
- renal/hepatic function;
- other clinically important effect modifiers.

The inability to characterize these factors limits external validity even before considering how anticoagulant practice has evolved since the included trials.

No external currency verification is performed in this pass.

---

# 12. GRADE reconciliation

## Structured outcome-level evidence

Summary of Findings 1 reports:

### Mortality
- **Low certainty**
- downgraded **two levels**
- reason: **very serious imprecision**
- CI spans important benefit and potential harm
- 59 total events

### Recurrent VTE
- **Low certainty**
- downgraded **two levels**
- reason: **very serious imprecision**
- CI spans important benefit and potential harm
- 34 total events

The Abstract and Plain Language Summary also describe the LMWH-versus-UFH evidence as **low certainty**.

## Source-internal conflict

The Discussion's "Quality of the evidence" paragraph instead says that the review judged the LMWH-versus-UFH evidence to be **moderate** while simultaneously saying it was downgraded for **very serious imprecision**.

This is internally inconsistent with the structured Summary of Findings material.

### Pass 3 handling

The discrepancy is preserved rather than silently corrected.

For hierarchical synthesis:

- use **low certainty** when reproducing the structured Summary of Findings rating;
- flag the Discussion's "moderate" wording as an unresolved internal inconsistency;
- do not reinterpret the Discussion wording as a separate validated GRADE analysis unless the source explicitly provides one.

---

# 13. Comparison with prior systematic reviews inside the source

The Discussion reports that earlier systematic reviews had found a statistically significant mortality reduction with LMWH.

### Erkens 2010
- 6 studies
- 446 cancer-subgroup participants
- OR 0.53
- 95% CI 0.33 to 0.85

The current review attributes part of the discrepancy to Erkens 2010 not including Breddin 2001 mortality data.

### Robertson 2017
- Peto OR 0.53
- 95% CI 0.33 to 0.85
- P = 0.009

The current review notes that Robertson 2017 did not include Breddin 2001 or Prandoni 2004 (GALILEI) and used a Peto odds ratio rather than the current review's random-effects risk-ratio approach.

### Pass 3 appraisal

These prior-review findings show that the apparent mortality advantage is sensitive to:

- study inclusion;
- available cancer-subgroup data;
- analytic choices;
- effect measure.

The current Cochrane review's less conclusive estimate should not be treated as a simple replication of the earlier statistically significant result.

---

# 14. Calibration of the authors' conclusion

The review uses three different levels of certainty in its own wording.

## Results / Summary of Findings
- mortality: LMWH **may reduce** mortality;
- recurrent VTE: LMWH **may reduce** recurrence slightly;
- certainty: **low** in the structured Summary of Findings tables.

## Authors' conclusions
The review states that LMWH is **"probably superior"** to UFH for initial treatment and, in the practice implications, specifically states that LMWH is probably superior in reducing mortality.

## Numerical evidence
Mortality:
- RR 0.66
- 95% CI 0.40–1.10
- P = 0.11
- low certainty in SOF 1
- 59 events

Recurrent VTE:
- RR 0.69
- 95% CI 0.27–1.76
- P = 0.44
- low certainty
- 34 events
- I² = 46%

Safety:
- cancer-subgroup bleeding data unavailable for this comparison.

### Pass 3 appraisal

The phrase **"probably superior"** is stronger than the structured evidence supports.

A more evidence-proportionate synthesis of this review alone is:

> The pooled estimates favor LMWH for 3-month mortality and recurrent VTE, but both estimates are low certainty and imprecise, both confidence intervals cross the null, recurrent-VTE results show moderate heterogeneity, and cancer-subgroup bleeding data are unavailable.

This is a **Pass 3 appraisal**, not a replacement for the source's conclusion.

The source's Results phrasing ("may reduce") is more consistent with its structured GRADE rating than the later superiority wording.

---

# 15. What can and cannot be concluded from this comparison

## Source-supported findings

The source supports the statements that:

- the principal pooled mortality estimate favors LMWH numerically;
- the principal pooled recurrent-VTE estimate favors LMWH numerically;
- neither principal CI excludes no effect;
- mortality shows I² = 0%;
- recurrent VTE shows I² = 46%;
- the structured GRADE rating is low certainty for both outcomes;
- sensitivity inclusion of additional mortality data retains a point estimate favoring LMWH but still crosses the null;
- cancer-subgroup bleeding and several other patient-important outcomes are unavailable.

## Reasonable Pass 3 appraisal

The evidence is compatible with a real mortality benefit from LMWH, but the review does not establish that benefit with high confidence.

The evidence for recurrent VTE is even less stable because only three studies and 34 events contribute, the CI is very wide, and study-level directions differ.

The comparison is insufficient to establish a complete efficacy-and-safety superiority claim because the main safety outcomes are absent.

## Not supported by this source alone

This review does **not** establish:

- a precise mortality benefit magnitude;
- a reliable reduction in recurrent VTE;
- lower bleeding risk with LMWH;
- overall net clinical benefit;
- equivalence of all LMWH products;
- a treatment effect applicable uniformly across cancer types/stages;
- superiority of a modern full-course LMWH strategy over UFH;
- current guideline superiority as of 2026.

---

# 16. Pass 3 limitation register

| Limitation | Effect on interpretation |
|---|---|
| Only 5 RCTs / 418 participants in main mortality analysis | Limits precision |
| Only 3 RCTs / 422 participants in recurrent-VTE analysis | Sparse outcome evidence |
| 59 mortality events | Supports very-serious-imprecision downgrade |
| 34 recurrent-VTE events | Supports very-serious-imprecision downgrade |
| Both pooled CIs cross 1.0 | Benefit is uncertain |
| Recurrent VTE I² = 46% | Moderate heterogeneity / inconsistent study pattern |
| No separate recurrent DVT versus PE data | Cannot identify which VTE phenotype drives recurrence |
| No cancer-subgroup bleeding data | Net benefit cannot be directly assessed |
| No QoL, postphlebitic syndrome, thrombocytopenia data | Patient-important outcome coverage incomplete |
| Cancer participants are subgroups | Indirectness / subgroup provenance concern |
| Cancer type and stage not specified | Limited effect-modifier assessment and external validity |
| Seven LMWH-UFH trials sensitivity-only due secondary subgroup-data provenance | Main estimate uses narrower evidence base; sensitivity estimate has weaker provenance |
| Open-label treatment in most contributing trials | Potential performance/co-intervention effects |
| Breddin follow-up ~91%; Merli cancer follow-up unreported | Missing-data concern in sparse outcome sets |
| Missing-outcome sensitivity tests not performed because pooled results were non-significant | Robustness to missingness not fully stress-tested |
| Multiple LMWH/UFH regimens and care settings | Class-level clinical heterogeneity |
| Initial exposure generally 5–10 days followed by VKA | 3-month outcomes are not a full-course randomized LMWH-vs-UFH comparison |
| 11 potentially eligible cancer subgroups unavailable | Evidence completeness concern |
| Internal low-vs-moderate GRADE wording conflict | Source consistency issue |
| Search current only to August 2021 | Current-practice currency not established |

---

# 17. Pass 3 synthesis

## Source finding

The 2021 Cochrane review's principal LMWH-versus-UFH analyses numerically favor LMWH for both mortality and recurrent VTE at three months.

Mortality:
- RR 0.66 (95% CI 0.40–1.10)
- 5 RCTs / 418 participants
- 59 deaths
- I² = 0%
- low-certainty evidence

Recurrent VTE:
- RR 0.69 (95% CI 0.27–1.76)
- 3 RCTs / 422 participants
- 34 events
- I² = 46%
- low-certainty evidence

The broader mortality sensitivity analysis remains directionally favorable:
- RR 0.75 (95% CI 0.56–1.02)

## Pass-level appraisal

The mortality signal is plausible and directionally robust to the reported sensitivity analysis, but remains uncertain because the main and sensitivity confidence intervals cross the null and the structured evidence rating is low certainty.

The recurrent-VTE signal is less convincing because of sparse events, wide uncertainty, moderate heterogeneity, and conflicting study-level directions.

Most importantly, the source cannot directly balance efficacy against major bleeding or other patient-important harms for LMWH versus UFH in the cancer subgroup.

The review's strongest conclusion — that LMWH is "probably superior" — appears more assertive than its structured Summary of Findings evidence warrants.

---

# 18. Handoff to final hierarchical SEA

The final synthesis should preserve the following Pass 3 conclusions:

1. **Mortality is the strongest signal**, but it remains low certainty and imprecise.
2. **Recurrent VTE is directionally favorable but highly uncertain**, with moderate heterogeneity.
3. **No direct cancer-subgroup bleeding comparison exists** for LMWH versus UFH.
4. **The sensitivity mortality estimate supports directional robustness, not statistical confirmation.**
5. **Cancer-subgroup provenance and incomplete subgroup availability materially constrain confidence.**
6. **Class labels conceal product, regimen, route, and treatment-setting heterogeneity.**
7. **Initial randomized treatment was short relative to the 3-month outcome horizon.**
8. **Structured GRADE = low certainty; Discussion = moderate certainty is an unresolved source inconsistency.**
9. **The authors' "probably superior" language should be flagged for claim inflation relative to the review's own certainty and intervals.**
10. **No current-practice conclusion should be drawn without separate currency verification.**

---

# 19. Pass 3 QA checklist

- [x] Summary of Findings 1 reconciled
- [x] Analysis 1.1 mortality forest plot reconstructed
- [x] Analysis 1.2 recurrent-VTE forest plot reconstructed
- [x] Relative effects preserved
- [x] Absolute effects preserved
- [x] Participant counts preserved
- [x] Total event counts preserved
- [x] Study-level event counts preserved
- [x] Heterogeneity statistics preserved
- [x] Overall-effect P values preserved
- [x] GRADE downgrade reasons preserved
- [x] Source-internal GRADE conflict preserved rather than silently corrected
- [x] Main versus sensitivity mortality analyses distinguished
- [x] No unreported sensitivity denominator invented
- [x] Missing bleeding and patient-important outcomes explicitly retained
- [x] Cancer-subgroup provenance incorporated from Pass 2
- [x] Breddin denominator inconsistency preserved
- [x] Applicability constraints assessed
- [x] Source findings separated from Pass 3 appraisal
- [x] Final whole-source scores deferred
- [x] No external evidence used

**Pass 3 status:** **COMPLETE — ready for integration with Passes 0–2 and comparison Passes 4–5 before final SEA scoring.**
