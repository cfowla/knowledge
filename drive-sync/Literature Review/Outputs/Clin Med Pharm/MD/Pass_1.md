# CIAG481 — HIERARCHICAL SEA DEEP PASS
## Section 1 — Extended-Spectrum β-Lactamase-Producing Enterobacterales (ESBL-E)

## 0. Artifact status

artifact_type: SEA intermediate artifact
stage: Deep section pass
parent_artifact: CIAG481 — SEA PASS 0 GLOBAL CONTEXT PACKET
source_file: ciag481.pdf
source_pages: 10–21
section: Section 1 — Extended-Spectrum β-Lactamase-Producing Enterobacterales (ESBL-E)
clinical_questions: 7
final_appraisal_status: NOT YET PERFORMED
final_scores_status: WITHHELD

boundary_note: >
  Question 1.7 begins and is substantially contained on page 21, but its final
  sentence continues onto page 22. This artifact intentionally remains scoped to
  pages 10–21 and therefore does not incorporate substantive content from the
  following AmpC-E batch.

evidence_boundary: >
  Quantitative findings below are results as summarized by the IDSA guidance.
  The underlying primary publications have not been independently appraised in
  this pass.

---

# 1. Section orientation

## 1.1 Mechanistic definition

ESBLs are β-lactamases that inactivate:

- most penicillins;
- most cephalosporins;
- aztreonam.

ESBL-producing Enterobacterales generally remain susceptible to carbapenems.

ESBL enzymes themselves do not inactivate non-β-lactam agents such as:

- ciprofloxacin;
- TMP-SMX;
- gentamicin;
- doxycycline.

However, ESBL genes commonly coexist with additional resistance genes or
mutations, so ESBL production does not imply susceptibility to these
non-β-lactam alternatives.

## 1.2 Organisms and epidemiology

ESBL genes can occur in any gram-negative organism but are especially prevalent in:

- Escherichia coli;
- Klebsiella pneumoniae;
- Klebsiella oxytoca.

CTX-M enzymes dominate in the United States, particularly CTX-M-15. ESBL variants
derived from TEM and SHV β-lactamases also occur and may have differing
hydrolytic properties.

## 1.3 Diagnostic / AST operationalization

routine_ESBL_testing: uncommon
CLSI_requires_routine_ESBL_testing: no

practical_surrogate_used:
  organisms:
    - E. coli
    - K. pneumoniae
    - K. oxytoca
  phenotype: ceftriaxone resistance
  threshold: ceftriaxone MIC >=4 µg/mL
  interpretation: commonly used surrogate for ESBL production

important_limitation: >
  Ceftriaxone resistance is a practical phenotype used to infer probable ESBL
  production; it is not equivalent to molecular confirmation of an ESBL gene.

section_assumption: >
  Preferred and alternative treatments assume demonstrated in-vitro activity
  of the selected agent unless a specific empiric-treatment discussion states
  otherwise.

---

# 2. Section-level synthesis

The ESBL-E section uses infection site and severity as the dominant therapeutic
stratifiers. For uncomplicated cystitis, the panel deliberately favors
urine-focused or relatively narrow agents and attempts to spare
fluoroquinolones, carbapenems, and newer broad-spectrum β-lactams. For cUTI,
systemically active oral TMP-SMX or fluoroquinolones become preferred when
susceptibility is demonstrated, with carbapenems or cefepime-enmetazobactam
preferred when these oral options cannot be used. For invasive non-urinary
infection, carbapenems remain the reference treatment class, with meropenem or
imipenem favored over ertapenem in critical illness or hypoalbuminemia.

A recurring theme is that laboratory susceptibility alone does not establish
clinical suitability. Piperacillin-tazobactam and cefepime may test susceptible
yet are discouraged for invasive ESBL-E disease because of microbiologic,
PK/PD, AST-reliability, and clinical-outcome concerns. Conversely,
cefepime-enmetazobactam is treated differently because the β-lactamase inhibitor
restores cefepime activity. The section also establishes an explicit stewardship
principle: agents designed or especially valuable for carbapenem-resistant
organisms should generally be conserved when conventional ESBL-active therapy
is sufficient.

---

# 3. Clinical question 1.1
## What are preferred antibiotics for the treatment of uUTIs caused by ESBL-E?

### Suggested approach

preferred:
  - aminoglycoside, single IV dose
  - gepotidacin
  - nitrofurantoin
  - pivmecillinam
  - sulopenem
  - TMP-SMX

ordering_note: >
  These preferred agents are listed alphabetically by the guidance and are not
  presented as intrinsically ranked within the Suggested approach.

alternative:
  - oral fosfomycin for ESBL-producing E. coli only

reserve_when_preferred_or_alternative_options_unavailable:
  - ciprofloxacin
  - levofloxacin
  - cefepime-enmetazobactam
  - ertapenem
  - meropenem
  - imipenem

specifically_not_suggested_or_avoided:
  - amoxicillin-clavulanate
  - doxycycline
  - oral fosfomycin for gram-negative species other than E. coli

traditional_beta_lactams_not_designated_preferred:
  - piperacillin-tazobactam
  - cefepime
  - cephamycins

### Clinical qualifiers

- uUTI courses are brief and ESBL status or susceptibility data may not be known
  before treatment is completed.
- Prior individual urine cultures and local epidemiology therefore have unusual
  importance when empiric ESBL-E coverage is being considered.
- US ESBL-producing E. coli prevalence among UTIs is estimated at approximately
  17%, with substantial regional variation.
- Several preferred/alternative agents retain >90% activity in surveillance
  datasets, but this should not be generalized to every agent or region.

### Evidence architecture

- surveillance epidemiology;
- systematic review;
- randomized clinical trials;
- randomized-trial ESBL subgroup analyses;
- observational studies;
- in-vitro susceptibility studies;
- PK/elimination rationale;
- mechanistic resistance considerations;
- panel consensus where direct ESBL-specific clinical evidence is sparse.

### Load-bearing findings

#### Single-dose aminoglycosides

systematic_review:
  studies: 13
  patients: 13,804
  pooled_microbiologic_cure: approximately 95%
  recurrence_free_at_day_30: 73%

additional_observational_support:
  patients: 13

interpretation: >
  Direct high-quality ESBL-specific randomized evidence is limited, but high
  urinary exposure, high observed cure, and low nephrotoxicity risk from a
  single dose underpin the panel's preferred designation.

#### Gepotidacin

regulatory_context:
  FDA_approval: March 2025
  indication: uUTI

in_vitro_ESBL_activity: >90%

ESBL_E_coli_subgroups:
  trial_1:
    gepotidacin: 70% (35/50)
    nitrofurantoin: 63% (25/40)
  trial_2:
    gepotidacin: 68% (23/34)
    nitrofurantoin: 40% (10/25)

common_adverse_event:
  - mild-to-moderate diarrhea

stewardship_concern: >
  Gepotidacin also has activity against Neisseria gonorrhoeae; excessive use
  could theoretically select gepotidacin-resistant gonococci.

#### Nitrofurantoin

ESBL_E_susceptibility: generally >90%

randomized_E_coli_uUTI_trial:
  nitrofurantoin_5_days: 70% (171/244)
  oral_fosfomycin_single_dose: 58% (139/241)

critical_limitation: >
  ESBL status was not reported in this trial, so applicability to ESBL-E is an
  extrapolation by the panel rather than direct ESBL-specific randomized evidence.

safety:
  - generally well tolerated
  - mild GI adverse effects most common

#### Pivmecillinam

US_approval: April 2024
ESBL_E_in_vitro_activity: >90%

three_day_uUTI_success: approximately 75–95%

observational_signal: >
  Some studies found greater failure with ESBL-E than non-ESBL-E isolates, but
  the difference was not observed with higher-dose mecillinam exposure
  (400 mg three times daily).

advantages:
  - narrow spectrum
  - favorable safety
  - low propensity for resistance emergence

Table_1_dependency: >
  The guideline's suggested pivmecillinam regimen differs from FDA-approved
  labeling.

#### Sulopenem

formulation:
  - oral sulopenem etzadroxil coformulated with probenecid

FDA_approval: October 2024
ESBL_E_in_vitro_activity: >95%

ESBL_E_uUTI_subgroup:
  sulopenem_5_days: 56% (41/73)
  ciprofloxacin_3_days: 47% (34/72)

common_adverse_event:
  - mild diarrhea

interaction_issue: >
  Probenecid inhibits renal tubular secretion and may increase concentrations
  of concomitant drugs including methotrexate, piperacillin, and sulfonamides.

#### TMP-SMX

evidence_summary: >
  Three-day TMP-SMX therapy is effective for susceptible ESBL-E uUTI and has
  efficacy comparable with short-course fluoroquinolone therapy.

US_ESBL_E_urinary_susceptibility: approximately 50%

implication: >
  It is preferred when susceptible, but empiric reliability is considerably
  lower than for several other uUTI options.

safety:
  - nausea
  - emesis
  - hypersensitivity reactions

#### Oral fosfomycin

role:
  alternative for ESBL-producing E. coli uUTI only

reason_to_limit_to_E_coli: >
  Organisms including K. pneumoniae frequently carry fosA genes capable of
  enzymatically inactivating fosfomycin.

important_uncertainty: >
  Clinical outcome studies directly establishing the clinical impact of fosA
  are unavailable.

randomized_E_coli_uUTI_trial:
  fosfomycin_single_dose: 58% (139/241)
  nitrofurantoin_5_days: 70% (171/244)

multidose_role: uncertain

#### Amoxicillin-clavulanate

recommendation: not suggested

randomized_trial:
  population: 370 women with E. coli uUTI
  amoxicillin_clavulanate_clinical_cure: 58% (93/160)
  ciprofloxacin_clinical_cure: 77% (124/162)
  persistent_vaginal_colonization:
    amoxicillin_clavulanate: 45% (68/151)
    ciprofloxacin: 10% (16/153)

critical_limitations:
  - ESBL-E proportion was not reported.
  - Both study regimens used lower doses than suggested in the guidance.
  - In-vitro clavulanate inhibition of ESBLs cannot be assumed to translate
    into adequate clinical efficacy.

#### Doxycycline

recommendation: avoid

PK_reason:
  unchanged_urinary_excretion: approximately 35–60%

evidence_limitation: >
  Available historical UTI studies are small and predominantly included
  P. aeruginosa, limiting relevance to ESBL-E urinary infection.

### Stewardship interpretation

The uUTI strategy is deliberately carbapenem-sparing and broad-spectrum-sparing.
Fluoroquinolones, cefepime-enmetazobactam, and carbapenems are acknowledged as
effective but generally reserved for cUTI or invasive disease because multiple
lower-impact options exist for uncomplicated cystitis.

### Cross-references

- Q1.2 — fluoroquinolones, carbapenems, cefepime-enmetazobactam, fosfomycin
- Q1.4 — piperacillin-tazobactam
- Q1.5 — cefepime
- Q1.6 — cephamycins

### Candidate load-bearing citations for later reference audit

- [25] — US ESBL-E uUTI epidemiology
- [26] — systematic review of single-dose aminoglycosides
- [31] — gepotidacin randomized trials
- [37] — nitrofurantoin versus fosfomycin
- [39,40] — pivmecillinam susceptibility
- [41–44] — pivmecillinam clinical/safety evidence
- [45,46] — sulopenem activity and clinical trial
- [48,49] — TMP-SMX efficacy and susceptibility
- [51–54] — fosfomycin susceptibility/fosA
- [57] — amoxicillin-clavulanate versus ciprofloxacin
- [61–63] — doxycycline PK and clinical evidence

---

# 4. Clinical question 1.2
## What are preferred antibiotics for the treatment of cUTI caused by ESBL-E?

### Suggested approach

preferred_when_susceptible:
  - TMP-SMX
  - ciprofloxacin
  - levofloxacin

preferred_when_above_agents_cannot_be_used:
  - cefepime-enmetazobactam
  - ertapenem
  - meropenem
  - imipenem

alternative:
  - IV fosfomycin
  - aminoglycosides
  - piperacillin-tazobactam

conditional_transition_option:
  - oral sulopenem after initial clinical improvement
  - multidose oral fosfomycin for selected ESBL E. coli cUTI when other oral
    options are unavailable

### Clinical qualifiers

- TMP-SMX or fluoroquinolones require confirmed susceptibility.
- If IV treatment is begun and susceptibility to TMP-SMX/ciprofloxacin/
  levofloxacin becomes available, oral transition to one of these agents is
  preferred.
- Piperacillin-tazobactam's alternative role is narrowed further by Q1.4:
  it is not suggested for critically ill patients or patients with concomitant
  bacteremia.
- Oral fosfomycin is not suggested as initial cUTI treatment because renal
  parenchymal concentrations are limited.

### Evidence architecture

- randomized clinical trials;
- open-label randomized trial;
- subgroup analyses;
- PK/urinary-concentration rationale;
- surveillance data;
- clinical experience;
- panel extrapolation where head-to-head evidence is absent.

### Load-bearing findings

#### Cefepime-enmetazobactam

surveillance: >
  Enmetazobactam restores cefepime activity against almost all ESBL-E isolates.

randomized_cUTI_ESBL_E_subgroup:
  cefepime_enmetazobactam: 74% (56/76)
  piperacillin_tazobactam: 52% (34/66)

limitation: >
  No direct randomized comparison with carbapenems for ESBL-E cUTI is cited.

panel_interpretation: >
  Cefepime-enmetazobactam and carbapenems are considered similarly effective
  options when susceptible oral agents cannot be used.

#### IV fosfomycin

FDA_approval: October 2025

trial_1_ESBL_E_cUTI:
  patients: 111
  IV_fosfomycin_7_days: 93% (52/56)
  piperacillin_tazobactam_7_days: 93% (51/55)

trial_2_presumed_ESBL_E_coli_cUTI_plus_bacteremia:
  IV_fosfomycin: 59% (23/39)
  meropenem: 71% (30/42)
  statistical_note: difference not statistically significant
  trial_level_note: fosfomycin failed to demonstrate noninferiority in the overall trial

K_pneumoniae_subgroup:
  IV_fosfomycin: 93% (25/27)
  piperacillin_tazobactam: 100% (25/25)

safety:
  - IV fosfomycin has substantial sodium content.
  - Caution is advised in older adults and patients at risk for heart failure.

species_nuance:
  E_coli: preferred organism for considering IV fosfomycin
  K_pneumoniae: >
    susceptibility criteria exist, but frequent fosA carriage creates residual
    efficacy concern despite reassuring subgroup results.

panel_uncertainty: >
  More supportive clinical data are required before IV fosfomycin could be
  promoted from an alternative to a preferred therapy.

#### Aminoglycosides

randomized_cUTI_trial:
  total_patients: 609
  ESBL_E_fraction: 28%
  clinical_cure:
    plazomicin: 89% (170/191)
    meropenem: 90% (178/197)
  acute_kidney_injury:
    plazomicin: 7% (21/300)
    meropenem: 4% (12/297)
  ESBL_E_microbiologic_eradication:
    plazomicin: 82% (42/51)
    meropenem: 75% (45/60)

additional_randomized_trial:
  total_patients: 61
  ESBL_E_patients: 40
  comparator:
    - amikacin 1 g every 48 hours for three doses
    - meropenem for 7 days
  finding: similar clinical cure

clinical_role: >
  Aminoglycosides may be especially useful for terminal doses of a treatment
  course because renal cortical exposure persists and once-daily administration
  can be logistically convenient.

principal_limitation:
  - duration-dependent nephrotoxicity

#### Sulopenem

randomized_cUTI_trial:
  initial_IV_therapy: 5 days in both arms
  combined_clinical_plus_microbiologic_response_day_21:
    sulopenem: 68% (301/444)
    ertapenem: 74% (325/440)
  noninferiority: not achieved
  clinical_success:
    sulopenem: 89% (397/444)
    ertapenem: 88% (389/440)
  ESBL_positive_favorable_response:
    sulopenem: 72% (79/110)
    comparator: 68% (85/125)

interpretive_limitation: >
  Because subjects received five initial days of IV therapy, the evidence does
  not establish oral sulopenem as adequate initial therapy for ESBL-E cUTI.

guidance_position: >
  Oral sulopenem is an alternative only after initial clinical improvement.

regulatory_note:
  - IV sulopenem is not FDA-approved.

#### Oral fosfomycin transition

initial_cUTI_therapy: not suggested

possible_role: >
  Transition therapy in selected ESBL E. coli cUTI when other oral options are
  unavailable.

evidence_limitation:
  - limited ESBL-E representation;
  - IV lead-in therapy in studies often approached the usual total duration
    required for cUTI;
  - therefore independent contribution of oral fosfomycin is uncertain.

### Table dependencies

Table_1:
  - TMP-SMX
  - ciprofloxacin
  - levofloxacin
  - cefepime-enmetazobactam
  - ertapenem
  - meropenem
  - imipenem
  - IV fosfomycin
  - aminoglycosides

Table_2:
  - IV fosfomycin breakpoint differs by organism:
      E_coli: <=8 µg/mL
      K_pneumoniae: <=32 µg/mL
  - oral fosfomycin breakpoint applies only to E. coli urinary isolates.

Supplemental_Material_dependency:
  - aminoglycoside PK-guided subsequent dosing
  - selected carbapenem dosing details
  - TMP-SMX dosing details

### Candidate load-bearing citations

- [64–66] — TMP-SMX/fluoroquinolone cUTI evidence
- [67,68] — cefepime-enmetazobactam
- [69] — IV fosfomycin versus piperacillin-tazobactam
- [70] — IV fosfomycin versus meropenem
- [72–79] — aminoglycoside PK, toxicity, and clinical trials
- [80] — sulopenem cUTI trial
- [56,81] — multidose oral fosfomycin transition

---

# 5. Clinical question 1.3
## What are preferred antibiotics for infections outside the urinary tract caused by ESBL-E?

### Suggested approach

preferred:
  - ertapenem
  - imipenem
  - meropenem

critical_illness_or_hypoalbuminemia:
  preferred:
    - imipenem
    - meropenem
  avoid_as_initial_preference:
    - ertapenem

alternative:
  - cefepime-enmetazobactam

oral_step_down_after_appropriate_response:
  - ciprofloxacin
  - levofloxacin
  - TMP-SMX

oral_step_down_requirements:
  - in-vitro susceptibility confirmed
  - hemodynamic stability
  - no concern for impaired GI absorption

not_suggested_for_ESBL_E_bloodstream_step_down:
  - nitrofurantoin
  - fosfomycin
  - amoxicillin-clavulanate
  - omadacycline
  - doxycycline
  - sulopenem pending additional evidence

### Evidence architecture

- randomized clinical trial of ESBL-E bloodstream infection;
- AST reanalysis using broth microdilution;
- subgroup analyses;
- PK/protein-binding rationale;
- observational hypoalbuminemia data;
- PK/PD modeling;
- clinical extrapolation from bloodstream infection to other invasive sites;
- expert-panel judgment.

### Load-bearing bloodstream-infection trial

initial_analysis:
  randomized_patients: 391
  confirmed_ESBL_gene: 86%
  piperacillin_tazobactam_30_day_survival: 88% (164/187)
  meropenem_30_day_survival: 96% (184/191)

broth_microdilution_reanalysis:
  isolates_available: 320 (82%)
  piperacillin_tazobactam_survival: 91% (134/147)
  meropenem_survival: 96% (149/155)
  absolute_difference_CI: 95% CI -1% to 11%
  statistical_interpretation: difference no longer statistically significant

panel_interpretation: >
  Carbapenems remain preferred because the mortality direction consistently
  favored meropenem in the overall trial and subgroup analyses.

extrapolation: >
  The bloodstream-infection evidence is extrapolated by the panel to
  intra-abdominal infection, skin/soft-tissue infection, and pneumonia.

appraisal_flag: >
  This is one of the section's strongest evidence anchors, but treatment
  recommendations for non-bloodstream invasive sites partly depend on
  extrapolation rather than site-specific randomized ESBL-E trials.

### Ertapenem in critical illness / hypoalbuminemia

mechanism:
  - ertapenem is highly protein bound;
  - hypoalbuminemia increases the unbound fraction;
  - increased free fraction can increase clearance;
  - serum half-life becomes shorter and less predictable.

observational_study:
  patients: 279
  hypoalbuminemia_definition: serum albumin <2.5 g/dL
  finding: >
    Hypoalbuminemia was associated with higher odds of 30-day mortality with
    ertapenem than with imipenem or meropenem.

limitations:
  - observational evidence;
  - comparative data in critically ill patients are limited and conflicting;
  - improved clinical outcomes with higher/more frequent ertapenem dosing have
    not been established.

possible_PK_mitigation_without_outcome_validation:
  - ertapenem 1.5 g daily
  - ertapenem every 12 hours

### Cefepime-enmetazobactam

supporting_basis:
  - extensive clinical experience with cefepime for invasive infection;
  - enmetazobactam inhibition of ESBLs;
  - PK/PD modeling;
  - intrapulmonary penetration;
  - high predicted target attainment for Enterobacterales MIC <=8/8 µg/mL.

limitation: >
  Direct clinical outcomes data for non-urinary ESBL-E infections remain
  limited.

guidance_position:
  alternative rather than preferred

### Oral step-down

supported_agents:
  - TMP-SMX
  - ciprofloxacin
  - levofloxacin

rationale:
  - high oral bioavailability
  - sustained systemic exposure

not_suggested_agents_and_reason:
  nitrofurantoin: inadequate systemic serum exposure
  fosfomycin: inadequate systemic serum exposure / insufficient bacteremia data
  amoxicillin_clavulanate: insufficient evidence / exposure concerns
  omadacycline: limited clinical evidence
  doxycycline: inadequate/uncertain systemic evidence
  sulopenem: insufficient PK/PD and clinical evidence

sulopenem_cUTI_bacteremia_subgroup:
  oral_sulopenem: 57% (25/44)
  comparator_oral_therapy: 65% (28/43)

sulopenem_intra_abdominal_trial:
  sulopenem_strategy: 82% (204/249)
  alternative_strategy: 88% (233/265)

### Candidate load-bearing citations

- [82] — randomized piperacillin-tazobactam versus meropenem ESBL-E BSI
- [22] — AST/broth microdilution reanalysis
- [83–91] — ertapenem PK/hypoalbuminemia/critical illness
- [67,92,93] — cefepime-enmetazobactam mechanism and PK/PD
- [80] — sulopenem cUTI/bacteremia subgroup
- [94] — sulopenem intra-abdominal trial

---

# 6. Clinical question 1.4
## Is there a role for piperacillin-tazobactam in ESBL-E infection?

### Suggested approach

uUTI:
  if_empirically_started_and_clinically_improving:
    - do not change therapy solely because ESBL-E is subsequently identified
    - do not extend treatment duration

cUTI:
  role: alternative
  conditions:
    - patient not critically ill
    - no concomitant bacteremia

outside_urinary_tract:
  role: not suggested
  applies_even_if_in_vitro_susceptibility_reported: yes

### Why susceptibility is not considered sufficient

concerns:
  1_MIC_reliability: >
    Piperacillin-tazobactam MIC testing may be inaccurate or poorly reproducible
    in ESBL-producing organisms, particularly with additional enzymes such as
    OXA-1.

  2_inoculum_effect: >
    Higher bacterial burdens may permit greater ESBL-E regrowth with
    piperacillin-tazobactam than with meropenem in preclinical systems.

  3_enzyme_burden: >
    Higher ESBL expression, multiple ESBLs, or additional β-lactamases such as
    AmpC may overwhelm tazobactam protection.

  4_inhibitor_exposure: >
    A 4.5-g piperacillin-tazobactam dose contains an 8:1 piperacillin:tazobactam
    ratio, whereas ceftolozane-tazobactam contains a 2:1 β-lactam:tazobactam ratio.

  5_breakpoint_design: >
    The Enterobacterales breakpoint substantially reflects piperacillin PK/PD
    and does not establish that the fixed tazobactam concentration used in AST
    reproduces effective inhibitor exposure in patients.

### cUTI evidence

systematic_review:
  evidence:
    - 1 randomized trial
    - 6 observational studies
  total_patients: 1,156
  finding: comparable treatment success with piperacillin-tazobactam and carbapenems

randomized_ESBL_E_cUTI_trial:
  piperacillin_tazobactam: 94% (31/33)
  ertapenem: 97% (32/33)

IV_fosfomycin_trial:
  IV_fosfomycin: 93% (52/56)
  piperacillin_tazobactam: 93% (51/55)

urinary_source_ESBL_E_bloodstream_subgroup:
  piperacillin_tazobactam_survival: 93% (95/102)
  meropenem_survival: 97% (124/128)

clinical_boundary: >
  The urinary-source bacteremia signal is one reason the panel excludes
  concomitant bacteremia from the cUTI scenario in which
  piperacillin-tazobactam is considered an alternative.

### Invasive infection evidence

major_randomized_trial:
  interpretation: >
    The randomized ESBL-E bloodstream-infection trial favored meropenem and
    remains the principal reason piperacillin-tazobactam is not suggested for
    invasive infection.

2023_meta_analysis:
  patients: 2,786
  studies:
    - major clinical trial
    - 25 observational studies
  comparison: beta-lactam/beta-lactamase inhibitor versus carbapenem
  result: no survival difference
  critical_limitation: >
    β-lactam/β-lactamase inhibitor therapy was not restricted exclusively to
    piperacillin-tazobactam.

subsequent_observational_study_1:
  patients: 644
  survival:
    piperacillin_tazobactam: 92% (283/309)
    comparator: 92% (308/335)

subsequent_observational_study_2:
  patients: 264
  survival:
    empiric_piperacillin_tazobactam: 86% (172/200)
    comparator: 96% (61/64)

overall_evidence_pattern: >
  Observational and meta-analytic evidence is mixed, whereas the randomized
  bloodstream-infection trial plus mechanistic/AST concerns push the panel
  toward carbapenems for invasive disease.

ongoing_evidence:
  - another bloodstream-infection trial is ongoing

### Table 2 dependency

piperacillin_tazobactam_Enterobacterales:
  susceptible: <=8/4 µg/mL
  susceptible_dose_dependent: 16/4 µg/mL

critical_interpretation: >
  The section explicitly warns that meeting a susceptibility criterion does not
  eliminate concerns regarding inhibitor adequacy or AST reliability in ESBL-E.

### Candidate load-bearing citations

- [22,96–98] — AST reliability
- [99–101] — inoculum effect
- [93,102] — inhibitor mechanism/exposure
- [104,105] — ESBL-E cUTI evidence
- [69] — fosfomycin versus piperacillin-tazobactam
- [82] — ESBL-E bloodstream randomized trial
- [107] — 2023 meta-analysis
- [108,109] — subsequent observational studies
- [106] — ongoing trial

---

# 7. Clinical question 1.5
## Is there a role for cefepime in ESBL-E infection?

### Suggested approach

uUTI:
  if_empirically_started_and_clinically_improving:
    - no change solely because ESBL-E is subsequently identified
    - no treatment extension

cUTI:
  - avoid cefepime

outside_urinary_tract:
  - avoid cefepime

applies_even_if_reported_susceptible: yes

### Mechanistic / AST basis

- ESBL enzymes commonly hydrolyze cefepime.
- Cefepime has no β-lactamase inhibitor unless paired with an inhibitor such as
  enmetazobactam.
- Commercial cefepime MIC testing may be inaccurate or poorly reproducible for
  ESBL-producing isolates.
- No randomized trial directly comparing cefepime with carbapenems for ESBL-E
  bloodstream infection is reported.

### cUTI evidence

observational_data:
  - some studies found no outcome difference versus carbapenems

randomized_trial_signal:
  cefepime_dose: 2 g IV every 12 hours
  isolate_MICs: 1–2 µg/mL
  cefepime_clinical_success: 33% (2/6)
  ertapenem_clinical_success: 97% (32/33)
  consequence: cefepime arm terminated early for clinical failure signal

critical_appraisal_signal: >
  Failure occurred despite cefepime MICs within the susceptible range, directly
  reinforcing the guidance's position that an apparently susceptible MIC does
  not guarantee clinical reliability in ESBL-E.

### Invasive infection evidence

observational_studies:
  pattern:
    - no difference in some studies
    - poorer cefepime outcomes in others

pneumonia_trial_subgroup:
  cefepime: 69% (9/13)
  imipenem: 100% (10/10)

limitations:
  - very small subgroup;
  - no dedicated ESBL-E bloodstream randomized trial;
  - observational evidence vulnerable to confounding.

### Table 2 dependency

cefepime_Enterobacterales:
  susceptible: <=2 µg/mL
  susceptible_dose_dependent: 4–8 µg/mL

notable_point: >
  The terminated cUTI cefepime arm involved MICs of only 1–2 µg/mL, so the
  guidance's concern is not limited to susceptible-dose-dependent isolates.

### Candidate load-bearing citations

- [93,110,111] — cefepime hydrolysis
- [112] — commercial AST reliability
- [104] — cUTI randomized-trial failure signal
- [114,115] — cUTI observational studies
- [116–120] — invasive observational studies
- [121] — pneumonia trial subgroup

---

# 8. Clinical question 1.6
## Is there a role for cephamycins in ESBL-E infection?

### Suggested approach

recommendation: >
  Cephamycins are not suggested for ESBL-E infection until additional clinical
  outcome data using cefoxitin or cefotetan are available and optimal dosing is
  defined.

US_available_agents:
  - cefoxitin
  - cefotetan

route:
  - IV only

### Mechanistic rationale

Cephamycins are generally stable against hydrolysis by ESBL enzymes, providing
a biologically plausible rationale for their use.

### Clinical evidence

comparative_observational_studies: at least 10

common_infection_types:
  - UTI
  - bloodstream infection of urinary origin

study_pattern:
  no_detected_difference: 8 studies
  poorer_cephamycin_outcomes: 2 studies

largest_study:
  population: ESBL-E bacteremia
  30_day_survival:
    cephamycins: 71% (94/132)
    carbapenems: 87% (115/132)

### Major limitations

- all comparative evidence is observational;
- infection sources are heterogeneous;
- substantial selection bias is possible;
- studies use different cephamycins;
- dosing strategies vary;
- durations of therapy vary;
- much of the most encouraging evidence concerns agents not available in the US;
- relatively few patients have been studied with US-available cefoxitin or cefotetan.

### Cefmetazole issue

most_encouraging_cephamycin_data:
  agent: cefmetazole
  US_clinical_availability: no

ongoing_trial:
  comparator: meropenem
  population: ESBL-E bacteremia

### Dosing / feasibility issue

limited_data:
  high_dose_continuous_infusion_cefoxitin: approximately 6 g/day

practical_limitations:
  - IV-only administration
  - short half-life, especially cefoxitin
  - no established clinical advantage over preferred agents

### Candidate load-bearing citations

- [122,123] — ESBL stability
- [124–130] — comparative observational studies
- [130] — largest survival analysis
- [128,129,131,132] — cefmetazole evidence
- [133] — ongoing cefmetazole trial
- [134,135] — cefoxitin dosing data

---

# 9. Clinical question 1.7
## What is the role of β-lactam agents with activity against carbapenem-resistant organisms for ESBL-E?

### Suggested approach
```
effective_but_preferentially_reserved:
  - aztreonam-avibactam
  - ceftazidime-avibactam
  - meropenem-vaborbactam
  - imipenem-relebactam
  - ceftolozane-tazobactam
  - cefiderocol

preferred_stewardship_destination:
  - infections caused by carbapenem-resistant organisms
```
### Mechanistic rationale
```
aztreonam_avibactam:
  - avibactam protects aztreonam from ESBL hydrolysis

ceftazidime_avibactam:
  - avibactam protects ceftazidime from ESBL hydrolysis
  - clinical-trial subgroup evidence supports efficacy

meropenem_vaborbactam:
  - meropenem itself generally provides sufficient ESBL-E activity

imipenem_relebactam:
  - imipenem itself generally provides sufficient ESBL-E activity

ceftolozane_tazobactam:
  - greater potency against ESBL-E than piperacillin-tazobactam
  - ceftolozane has greater intrinsic ESBL stability than piperacillin
  - formulation contains a more favorable β-lactam:tazobactam ratio (2:1 versus 8:1)

cefiderocol:
  - expected ESBL-E activity
```
### Ceftolozane-tazobactam clinical findings
```
intra_abdominal_plus_UTI_ESBL_E_subgroup:
  ceftolozane_tazobactam_clinical_cure: 97% (76/78)
  meropenem_clinical_cure: 89% (23/26)

ESBL_E_pneumonia_subgroup:
  ceftolozane_tazobactam_28_day_survival: 79% (66/84)
  meropenem_28_day_survival: 71% (52/73)

interpretation: >
  These data support efficacy but do not justify routine preferential use over
  conventional ESBL-active agents because preserving these drugs for organisms
  with carbapenem resistance is an explicit stewardship objective.
```
### Stewardship principle

The guidance separates "effective" from "appropriate to deploy routinely."
Activity against ESBL-E is insufficient reason by itself to consume agents with
greater strategic importance for CRE, DTR P. aeruginosa, or other
carbapenem-resistant organisms.
```
polymicrobial_exception: >
  The rationale begins to describe situations in which a newer agent may be
  useful when an ESBL-E infection occurs alongside a carbapenem-resistant
  organism. The final sentence extends beyond the requested page-21 boundary;
  that continuation is not incorporated into this artifact.
```
### Candidate load-bearing citations

- [45,136] — in-vitro activity
- [15,137] — avibactam protection
- [138–142] — ceftazidime-avibactam subgroup evidence
- [143–150] — ceftolozane-tazobactam potency/mechanistic comparisons
- [151] — ESBL-E intra-abdominal/UTI subgroup
- [152,153] — ESBL-E pneumonia subgroup

---

# 10. Cross-question treatment matrix

| Clinical situation | Preferred / favored | Alternative / conditional | Generally avoid / reserve |
|---|---|---|---|
| ESBL-E uUTI | Single-dose aminoglycoside; gepotidacin; nitrofurantoin; pivmecillinam; sulopenem; TMP-SMX | Fosfomycin for E. coli; FQ, cefepime-enmetazobactam, or carbapenem if necessary | Amox-clav; doxycycline; fosfomycin for non-E. coli; broadly active agents should generally be spared |
| ESBL-E cUTI | TMP-SMX, ciprofloxacin, levofloxacin if susceptible; cefepime-enmetazobactam or carbapenem if oral agents unsuitable | IV fosfomycin; aminoglycoside; piperacillin-tazobactam in selected noncritical nonbacteremic patients; oral sulopenem after improvement | Cefepime; initial oral fosfomycin |
| Invasive/non-urinary ESBL-E | Ertapenem, meropenem, imipenem | Cefepime-enmetazobactam; oral TMP-SMX/FQ step-down after stabilization | Piperacillin-tazobactam; cefepime; cephamycins |
| Critical illness / hypoalbuminemia | Meropenem or imipenem | — | Ertapenem as initial preference |
| ESBL-E bloodstream oral step-down | TMP-SMX, ciprofloxacin, levofloxacin when susceptible and clinically appropriate | — | Nitrofurantoin, fosfomycin, amox-clav, omadacycline, doxycycline, sulopenem |
| ESBL-E susceptible to CRE-directed newer β-lactams | Conventional ESBL-directed therapy generally preferred | CRE-active agent may have special polymicrobial utility | Routine use of aztreonam-avibactam, CZA, MVB, IMR, ceftolozane-tazobactam, cefiderocol should be conserved |

---

# 11. Cross-cutting pharmacotherapy principles

## 11.1 Infection site is a primary decision variable

The section does not treat "ESBL-E" as a single therapeutic category.
```
therapeutic_gradient:
  uUTI:
    emphasis: high urinary exposure + narrow-spectrum stewardship

  cUTI:
    emphasis: renal-parenchymal/systemic exposure + susceptibility + oral transition

  invasive_infection:
    emphasis: systemic reliability + clinical outcome evidence

  bloodstream_infection:
    emphasis: systemic exposure, randomized outcome evidence, avoidance of
      susceptibility-result overinterpretation
```
## 11.2 Susceptibility is necessary but sometimes insufficient

Examples:

- Piperacillin-tazobactam may test susceptible but is not suggested for
  invasive ESBL-E disease.
- Cefepime may test susceptible but is avoided for cUTI and invasive disease.
- A cefepime cUTI failure signal occurred even with MICs of 1–2 µg/mL.
- ESBL-E commonly carry resistance determinants unrelated to the ESBL enzyme,
  so non-β-lactam activity must be individually confirmed.

## 11.3 β-lactamase inhibitor choice matters

The guidance does not treat all β-lactam/β-lactamase inhibitor combinations as
interchangeable.

Examples:

- tazobactam may inadequately protect piperacillin under high enzyme burden;
- enmetazobactam restores cefepime activity against ESBLs;
- avibactam protects ceftazidime or aztreonam;
- ceftolozane is intrinsically more stable to common ESBLs than piperacillin.

## 11.4 Oral transition is evidence- and exposure-dependent
```
favored_systemic_step_down:
  - TMP-SMX
  - ciprofloxacin
  - levofloxacin

poor_or_unproven_bloodstream_step_down_options:
  - nitrofurantoin
  - fosfomycin
  - amoxicillin-clavulanate
  - omadacycline
  - doxycycline
  - sulopenem
```
## 11.5 Stewardship constrains otherwise-active therapy

Two conservation levels are evident:

1. For uUTI, preserve fluoroquinolones, carbapenems, and newer β-lactams when
   narrower options are adequate.
2. Across ESBL-E infection generally, preserve agents with major value against
   carbapenem-resistant organisms.

---

# 12. Relevant Table 1 dependencies

These are the main adult regimens from the global dosing table that materially
interact with the ESBL-E section. Doses assume normal renal/hepatic function
unless otherwise specified.
```
aminoglycosides:
  amikacin:
    uUTI: 15 mg/kg IV once
    cUTI: 15 mg/kg IV once, then PK-guided dosing
  gentamicin:
    uUTI: 5 mg/kg IV once
    cUTI: 7 mg/kg IV once, then PK-guided dosing
  plazomicin:
    uUTI: 15 mg/kg IV once
    cUTI: 15 mg/kg IV once, then PK-guided dosing

cefepime_enmetazobactam:
  standard: 2.5 g IV every 8 h infused over 2 h
  CrCl_ge_130: 2.5 g IV every 8 h infused over 4 h

ciprofloxacin:
  uUTI: 400 mg IV q12h OR 500 mg PO q12h
  other: 400 mg IV q8h OR 750 mg PO q12h

ertapenem:
  - 1 g IV every 24 h over 30 min
  - additional information in Supplemental Material

fosfomycin:
  uUTI: 3 g PO once
  cUTI: 6 g IV every 8 h infused over 1 h

gepotidacin:
  uUTI: 1.5 g PO every 12 h

imipenem_cilastatin:
  uUTI: 500 mg imipenem IV q6h over 30 min
  other:
    - 500 mg imipenem IV q6h over 3 h if feasible
    - OR 1,000 mg imipenem IV q8h over 1 h
  high_CrCl_note:
    CrCl_ge_90: 1 g imipenem IV q6h over 1 h

levofloxacin:
  - 750 mg IV/PO every 24 h

meropenem:
  uUTI: 1 g IV every 8 h over 30 min
  other: 1–2 g IV every 8 h over 3 h if feasible
  higher_dose_preferred_for:
    - obesity
    - CNS infection
    - ECMO
    - CrCl >=130 mL/min

nitrofurantoin:
  macrocrystal_monohydrate: 100 mg PO every 12 h
  oral_suspension: 50 mg PO every 6 h

pivmecillinam:
  uUTI: 370 mg PO every 8 h
  note: guidance dosing differs from FDA-approved labeling

sulopenem_etzadroxil_probenecid:
  - 500 mg/500 mg PO every 12 h

TMP_SMX:
  uUTI: 160 mg trimethoprim component IV/PO every 12 h
  other: 8–15 mg/kg/day trimethoprim component divided every 8–12 h

Supplemental_Material_dependency:
  - aminoglycoside subsequent dosing
  - ertapenem
  - imipenem
  - meropenem
  - TMP-SMX
```
---

# 13. Relevant Table 2 dependencies

## Enterobacterales breakpoints especially important to this section
```
cefepime:
  susceptible: <=2 µg/mL
  susceptible_dose_dependent: 4–8 µg/mL

cefepime_enmetazobactam:
  susceptible: <=8/8 µg/mL
  note: FDA criterion used where CLSI breakpoint unavailable

ciprofloxacin:
  susceptible: <=0.25 µg/mL

ertapenem:
  susceptible: <=0.5 µg/mL

fosfomycin_IV:
  E_coli: <=8 µg/mL
  K_pneumoniae: <=32 µg/mL

fosfomycin_oral:
  susceptible: <=64 µg/mL
  limitation: applies only to E. coli urinary isolates

imipenem:
  susceptible: <=1 µg/mL

levofloxacin:
  susceptible: <=0.5 µg/mL

meropenem:
  susceptible: <=1 µg/mL

nitrofurantoin:
  susceptible: <=32 µg/mL
  urinary_only: yes

piperacillin_tazobactam:
  susceptible: <=8/4 µg/mL
  susceptible_dose_dependent: 16/4 µg/mL

pivmecillinam_mecillinam:
  susceptible: <=8 µg/mL
  urinary_only: yes

TMP_SMX:
  susceptible: <=2/38 µg/mL

interpretive_warning: >
  The piperacillin-tazobactam and cefepime questions demonstrate why a numerical
  MIC categorized as susceptible should not be interpreted independently of the
  organism's ESBL phenotype and the clinical infection site.
```
---

# 14. Evidence-architecture map

| Question | Dominant evidence types | Directness of evidence | Major uncertainty |
|---|---|---|---|
| Q1.1 uUTI | RCTs/subgroups, systematic review, surveillance, PK | Mixed; strongest for general uUTI and selected ESBL subgroups | Several agents lack large ESBL-specific trials |
| Q1.2 cUTI | Multiple randomized trials/subgroups, PK, susceptibility | Relatively direct for several IV options | Species-specific fosfomycin uncertainty; oral transition evidence weaker |
| Q1.3 invasive | Major randomized BSI trial, reanalysis, observational PK, modeling | Strongest for carbapenem-vs-PTZ BSI; indirect for other invasive sites | Extrapolation from BSI; limited cefepime-enmetazobactam outcomes |
| Q1.4 PTZ | RCT, systematic review, observational studies, preclinical and AST evidence | Direct but internally mixed | Conflict between randomized BSI signal and some observational/meta-analytic data |
| Q1.5 cefepime | Small randomized cUTI signal, observational studies, mechanistic/AST evidence | Limited but consistently cautionary | Small RCT sample; no BSI head-to-head RCT |
| Q1.6 cephamycins | Observational studies + mechanism | Low-to-moderate | Selection bias, heterogeneous agents/dosing, limited US-agent data |
| Q1.7 CRE-active β-lactams | Trial subgroup analyses, in-vitro/mechanistic evidence | Adequate to establish likely activity | Primary question is stewardship prioritization rather than efficacy |

---

# 15. Important evidence tensions for final appraisal

## 15.1 Piperacillin-tazobactam

```
supportive:
  - randomized and observational cUTI data often show similar success to carbapenems;
  - meta-analysis of BSI data did not demonstrate a survival difference;
  - one large observational study found identical survival.

against:
  - randomized bloodstream trial favored meropenem;
  - urinary-source BSI subgroup numerically favored meropenem;
  - another observational study favored comparator therapy;
  - AST reliability, inoculum, inhibitor concentration, and enzyme-burden concerns
    create biologic plausibility for failure.

appraisal_target: >
  Determine whether the panel's strong site-specific restriction is proportionate
  to the combination of randomized evidence plus mechanistic uncertainty despite
  conflicting observational literature.
```

## 15.2 Cefepime
```
supportive:
  - some observational studies show no difference from carbapenems.

against:
  - ESBL hydrolysis;
  - AST reliability concerns;
  - cUTI trial arm stopped for failure despite low MICs;
  - pneumonia subgroup numerically favored imipenem.

appraisal_target: >
  Evidence is not large, but multiple independent lines of evidence point in the
  same cautionary direction.
```
## 15.3 Fosfomycin
```
supportive:
  - excellent urologic rationale;
  - strong E. coli activity;
  - IV trial demonstrated high cUTI cure in one comparison.

against:
  - single-dose oral therapy inferior to nitrofurantoin;
  - fosA concern in K. pneumoniae and other organisms;
  - IV fosfomycin failed noninferiority in another trial;
  - multidose oral cUTI transition evidence is difficult to isolate from long IV lead-ins.

appraisal_target: >
  Keep oral and IV formulations, infection sites, and species restrictions
  explicitly separated in final synthesis.
```
## 15.4 Ertapenem
```
strength:
  - carbapenem class efficacy against ESBL-E.

limitation:
  - highly protein-bound pharmacology becomes problematic in hypoalbuminemia;
  - clinical comparative data in critical illness are limited/conflicting;
  - alternative dosing strategies lack outcome validation.

appraisal_target: >
  Preserve the distinction between "preferred carbapenem generally" and
  "not preferred initial carbapenem in critical illness/hypoalbuminemia."
```
---

# 16. Safety / toxicity / interaction matrix

| Agent/class | Important concern highlighted by section |
|---|---|
| Aminoglycosides | Duration-dependent nephrotoxicity; much lower concern with a single uUTI dose |
| Gepotidacin | Mild/moderate diarrhea; stewardship concern regarding N. gonorrhoeae resistance |
| Nitrofurantoin | Generally mild GI effects |
| Pivmecillinam | Generally favorable safety |
| Sulopenem/probenecid | Mild diarrhea; probenecid-mediated drug interactions |
| TMP-SMX | Nausea, emesis, hypersensitivity |
| Oral fosfomycin | Mild diarrhea |
| IV fosfomycin | High sodium load; caution in older adults/heart-failure risk |
| Fluoroquinolones | No detailed toxicity discussion in these pages, but their use is deliberately spared in uUTI |
| Ertapenem | PK unpredictability with critical illness/hypoalbuminemia |
| Piperacillin-tazobactam | Reliability concern is primarily efficacy/AST rather than toxicity |
| Cefepime | Reliability concern is primarily ESBL hydrolysis/AST rather than toxicity |
| Cephamycins | IV-only administration and short half-life reduce practical advantage |

---

# 17. Stewardship architecture

The ESBL-E section contains three distinct stewardship strategies:

### Narrow-spectrum/site-focused stewardship
For uUTI, favor agents that provide adequate urinary activity without consuming
broader systemic options.

### Carbapenem stewardship
Use susceptible TMP-SMX or fluoroquinolones for cUTI when clinically appropriate
rather than defaulting automatically to carbapenems.

### Advanced-agent stewardship
Preserve aztreonam-avibactam, ceftazidime-avibactam,
meropenem-vaborbactam, imipenem-relebactam, ceftolozane-tazobactam, and
cefiderocol for carbapenem-resistant pathogens when conventional ESBL-active
therapy is adequate.
```
section_level_inference: >
  The guidance is not simply ranking drugs by probability of microbiologic
  success; it is balancing efficacy, infection-site exposure, toxicity,
  resistance ecology, and preservation of future therapeutic options.
```
---

# 18. Provisional appraisal signals
## NOT final SEA scores

### Evidence strengths

- A major randomized bloodstream-infection trial directly informs the central
  carbapenem-versus-piperacillin-tazobactam question.
- Several cUTI recommendations are supported by randomized clinical trials.
- Newer uUTI agents have direct randomized data or ESBL-specific subgroup data.
- The section repeatedly integrates clinical outcomes with PK/PD,
  susceptibility, resistance mechanisms, and site-specific drug exposure.
- Negative and conflicting evidence is generally acknowledged rather than
  omitted.
- The guidance differentiates direct evidence from panel extrapolation in
  several places.

### Evidence weaknesses

- No formal GRADE certainty or recommendation-strength framework is supplied.
- Some "preferred" uUTI options rely on small ESBL-specific subgroups,
  surveillance, or extrapolation from non-ESBL populations.
- Evidence for invasive infection at sites other than bloodstream infection is
  partly extrapolated from bacteremia.
- Cefepime recommendations rely partly on very small clinical-trial subgroups.
- Cephamycin evidence is wholly observational and heterogeneous.
- Several newer agents have limited post-approval clinical experience.
- Some recommendations depend heavily on mechanistic or PK/PD plausibility.
- Susceptibility rates and therapeutic options are temporally and
  geographically sensitive.

### Implementation strengths

- Strong syndrome separation: uUTI versus cUTI versus invasive infection.
- Explicit oral-transition logic.
- Useful distinction between susceptibility and clinical reliability.
- Strong stewardship guidance regarding carbapenem and novel-agent preservation.
- Table 1 and Table 2 provide directly operational dosing and AST context.

### Implementation constraints

- Many decisions require reliable current AST.
- ESBL molecular confirmation is often unavailable.
- Ceftriaxone resistance is only a surrogate for ESBL production.
- Newer-drug susceptibility testing may not be routinely available.
- Several dosing recommendations require Supplemental Material that is not in
  the evaluated PDF.
- Local ESBL epidemiology substantially affects empiric uUTI applicability.

---

# 19. Candidate reference-audit priority

## Tier 1 — likely load-bearing for final appraisal

- [26] — single-dose aminoglycoside systematic review
- [31] — gepotidacin randomized trials
- [37] — nitrofurantoin versus fosfomycin randomized trial
- [46] — sulopenem ESBL-E uUTI data
- [68] — cefepime-enmetazobactam cUTI randomized evidence
- [69] — IV fosfomycin versus piperacillin-tazobactam
- [70] — IV fosfomycin versus meropenem
- [75] — plazomicin versus meropenem
- [80] — sulopenem cUTI trial
- [82] — piperacillin-tazobactam versus meropenem ESBL-E bloodstream trial
- [22] — broth-microdilution reanalysis / AST implications
- [87] — ertapenem/hypoalbuminemia observational study
- [104] — cefepime/PTZ/ertapenem cUTI evidence
- [107] — 2023 BSI meta-analysis
- [121] — cefepime versus imipenem pneumonia subgroup
- [130] — largest cephamycin-versus-carbapenem study
- [151–153] — ceftolozane-tazobactam ESBL-E subgroup data

## Tier 2 — mechanistic / implementation relevance

- [52–54] — fosA
- [61–63] — doxycycline urinary PK/evidence
- [83–91] — ertapenem PK and critical illness
- [92,93] — cefepime-enmetazobactam PK/PD and inhibitor properties
- [96–102] — piperacillin-tazobactam AST, inoculum, inhibitor limitations
- [110–112] — cefepime hydrolysis and AST
- [122–135] — cephamycin evidence and dosing
- [136–150] — novel β-lactam/β-lactamase inhibitor mechanistic evidence

---

# 20. Section coverage status
```
section_introduction: PASS
Q1_1_uUTI: PASS
Q1_2_cUTI: PASS
Q1_3_nonurinary_invasive: PASS
Q1_4_piperacillin_tazobactam: PASS
Q1_5_cefepime: PASS
Q1_6_cephamycins: PASS
Q1_7_CRE_active_beta_lactams: PARTIAL_BY_PAGE_BOUNDARY

quantitative_findings_preserved: PASS
recommendation_hierarchy_preserved: PASS
negative_evidence_preserved: PASS
explicit_uncertainty_preserved: PASS
safety_considerations_preserved: PASS
stewardship_considerations_preserved: PASS
Table_1_dependencies_mapped: PASS
Table_2_dependencies_mapped: PASS
supplement_dependencies_flagged: PASS
candidate_reference_audit_list_created: PASS

final_section_score_assigned: NO
final_guideline_score_assigned: NO

remaining_section_specific_gap:
  - final continuation of Q1.7 on page 22 excluded by requested page boundary

DEEP_PASS_ESBL_STATUS: COMPLETE FOR REQUESTED PAGES 10–21
```
---

# 21. Handoff to hierarchical synthesis

The final whole-guideline SEA should carry forward the following ESBL-E
high-value synthesis points:

1. ESBL-E therapy must be stratified by infection site and severity rather than
   by resistance phenotype alone.

2. uUTI management is intentionally broad-spectrum-sparing, with multiple
   narrow or urine-focused preferred agents.

3. For cUTI, susceptible TMP-SMX or fluoroquinolones are preferred oral/systemic
   options; carbapenems and cefepime-enmetazobactam become preferred when these
   cannot be used.

4. Carbapenems remain the reference therapy for invasive ESBL-E infection,
   anchored principally by randomized bloodstream-infection evidence.

5. Meropenem or imipenem are preferred over ertapenem in critical illness or
   hypoalbuminemia because of ertapenem PK concerns.

6. Piperacillin-tazobactam occupies a narrow role:
   reasonable as an alternative for selected noncritical, nonbacteremic cUTI,
   but not suggested for invasive non-urinary infection.

7. Cefepime alone should not be equated with cefepime-enmetazobactam:
   cefepime is avoided for ESBL-E cUTI/invasive disease even when apparently
   susceptible, whereas enmetazobactam restores ESBL-directed activity.

8. Cephamycins remain biologically plausible but clinically under-supported,
   especially for US-available cefoxitin and cefotetan.

9. Oral bloodstream step-down is restricted to agents capable of reliable
   systemic exposure—principally susceptible TMP-SMX or fluoroquinolones.

10. Carbapenem-resistant-organism-directed newer β-lactams are generally active
    against ESBL-E but should be conserved rather than used routinely.

11. Across several questions, AST category, PK/PD, bacterial burden,
    β-lactamase inhibitor exposure, species, and infection site modify the
    clinical meaning of "susceptible."

12. Final appraisal should distinguish recommendations anchored in randomized
    clinical evidence from recommendations driven predominantly by PK/PD,
    surveillance, observational evidence, mechanistic reasoning, or expert
    consensus.