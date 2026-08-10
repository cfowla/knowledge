# CIAG481 — HIERARCHICAL SEA DEEP PASS
## Section 5 — Carbapenem-Resistant *Acinetobacter baumannii* Complex (CRAB)

---

# 0. Artifact status

artifact_type: SEA intermediate artifact
stage: Hierarchical deep section pass
parent_artifact: CIAG481 — SEA PASS 0 GLOBAL CONTEXT PACKET
source_file: ciag481.pdf
source_section: Section 5 — Carbapenem-resistant Acinetobacter baumannii complex (CRAB)
source_scope:
  start: PDF p. 52, beginning at "SECTION 5"
  end: PDF p. 60, immediately before "SECTION 6: Stenotrophomonas maltophilia"
boundary_exclusions:
  - p. 52 material preceding SECTION 5 belongs to DTR P. aeruginosa Question 4.7
  - p. 60 material beginning with SECTION 6 belongs to S. maltophilia
clinical_questions_extracted: 6
figures_in_section: 0
tables_in_section: 0
global_table_dependencies:
  - Table 1 — adult dosing
  - Table 2 — susceptibility breakpoints
final_appraisal_status: NOT YET PERFORMED
final_scores_status: WITHHELD

deep_pass_contract:
  - preserve Suggested approach separately from Rationale
  - reconstruct evidence architecture question by question
  - preserve load-bearing quantitative findings
  - preserve explicit uncertainty and negative evidence
  - preserve safety, PK/PD, AST, and resistance constraints
  - identify candidate load-bearing citations
  - do not independently validate cited primary studies
  - do not assign final SEA scores

---

# 1. Section-level clinical frame

section_population: >
  Patients with invasive infections caused by carbapenem-resistant
  Acinetobacter baumannii complex.

section_scope_boundary: >
  The guidance explicitly focuses this section on invasive CRAB infections.
  Recovery of CRAB from a clinical culture alone does not establish invasive
  disease.

clinical_context:
  - CRAB is primarily a nosocomial pathogen.
  - Respiratory-tract and wound cultures are common sources of recovery.
  - Colonization versus infection can be especially difficult to distinguish:
      - in mechanically ventilated patients
      - in patients with extensive burns
  - Invasive infections occur predominantly in critically ill patients with
    substantial comorbidities.
  - Host factors and severity of illness independently contribute to poor
    outcomes and complicate attribution of mortality or cure to antimicrobial
    selection alone.

nomenclature_constraint: >
  "CRAB" is used pragmatically because many clinical microbiology laboratories
  cannot reliably distinguish A. baumannii from other organisms within the
  A. baumannii-calcoaceticus complex.

major_resistance_mechanisms_described:
  beta_lactamases:
    - Acinetobacter-derived cephalosporinases (ADCs)
    - OXA-type carbapenemases, including OXA-23, OXA-24/40, and OXA-58
  aminoglycoside_resistance:
    - aminoglycoside-modifying enzymes
    - 16S rRNA methyltransferases
  permeability:
    - loss or alteration of porins such as CarO and OmpA
    - increased outer-membrane hydrophobicity
  efflux:
    - AdeABC
    - AdeIJK
  target_modification:
    - PBP1a/1b and PBP3 alterations reducing sulbactam activity
    - DNA gyrase/topoisomerase IV mutations reducing fluoroquinolone activity

section-level_problem_statement: >
  CRAB management is constrained simultaneously by extensive multidrug
  resistance, uncertainty regarding whether an isolate represents infection,
  limited reliable therapeutic options, AST limitations, and a patient
  population with high baseline mortality.

---

# 2. Reconstructed treatment hierarchy

IMPORTANT:
The following hierarchy is an interpretive synthesis across Questions 5.1–5.5.
The source does not present it as a single graphical algorithm.

## Preferred strategy

invasive_CRAB:
  preferred:
    - sulbactam-durlobactam
    - PLUS imipenem OR meropenem

## If sulbactam-durlobactam is not immediately available

temporary_bridge:
  - high-dose ampicillin-sulbactam providing 9 g/day of sulbactam
  - PLUS at least one additional active agent:
      - cefiderocol
      - minocycline
      - polymyxin B

duration_of_bridge: >
  Only until sulbactam-durlobactam plus a carbapenem can be initiated.

## If sulbactam-durlobactam resistance or an MBL is identified

trigger_examples:
  - sulbactam-durlobactam MIC >=16/4 µg/mL
  - blaNDM or another relevant MBL

panel_preference:
  non_sulbactam_based_combination_options:
    - cefiderocol
    - minocycline
    - polymyxin B
    - tigecycline

rationale: >
  Durlobactam inhibits class A, C, and D beta-lactamases but not class B
  metallo-beta-lactamases, and sulbactam-based therapy is considered unlikely
  to add meaningful activity when clinically relevant resistance is present.

uncertainty: >
  Clinical outcome data defining the optimal regimen for
  sulbactam-durlobactam-resistant CRAB are lacking.

## CRAB pneumonia

routine_nebulized_antibiotics: NOT SUGGESTED

selective_adjunctive_use_may_be_reasonable_if:
  - documented resistance to sulbactam-durlobactam
  - OR clinical response to systemic therapy is suboptimal

---

# 3. Question 5.1 — Sulbactam-durlobactam

question: >
  What is the role of sulbactam-durlobactam for the treatment of invasive
  CRAB infections?

## Suggested approach

preferred_therapy:
  - sulbactam-durlobactam
  - PLUS imipenem OR meropenem

recommendation_position: preferred treatment

## Mechanistic rationale

sulbactam:
  - possesses intrinsic antibacterial activity against A. baumannii through
    binding of PBP1a/1b and PBP3
  - is vulnerable to hydrolysis by class A, C, and D beta-lactamases

durlobactam:
  class: diazabicyclooctane beta-lactamase inhibitor
  inhibits:
    - class A
    - class C
    - class D
  does_not_inhibit:
    - class B metallo-beta-lactamases such as NDM

US_surveillance_activity:
  sulbactam_durlobactam_active_against: ">95% of CRAB isolates"

geographic_resistance_context:
  - NDM-producing CRAB remains uncommon in the United States.
  - NDM-producing isolates are increasingly reported in South Asia and
    the Middle East.

## Load-bearing comparative clinical evidence

randomized_trial_ref_501:
  population: 125 patients with CRAB pneumonia or bloodstream infection
  intervention: sulbactam-durlobactam + imipenem
  comparator: colistin + imipenem

  28_day_survival:
    intervention: "81% (51/63)"
    comparator: "68% (42/62)"

  clinical_cure:
    intervention: "62% (39/63)"
    comparator: "40% (25/62)"

interpretive_limit: >
  The comparator regimen, colistin plus imipenem, is itself not considered a
  preferred or alternative contemporary CRAB regimen by this guidance.

contextual_support: >
  The panel notes that survival in other CRAB trials has frequently been below
  60%, increasing the perceived importance of the survival observed in the
  sulbactam-durlobactam arm.

## Why add a carbapenem?

mechanistic_basis:
  sulbactam:
    preferential_targets:
      - PBP1a/1b
      - PBP3
  imipenem:
    preferential_target:
      - PBP2

in_vitro_combination_findings:
  sulbactam_MIC_change: approximately 1–2-fold reduction
  time_kill_effect: ">2-log CFU/mL reduction"
  comparison: >
    The reported degree of killing was not observed with
    sulbactam-durlobactam alone in the cited experiments.

clinical_validation_of_combination_increment: NOT ESTABLISHED

panel_inference: >
  Despite absence of direct confirmation that the carbapenem adds clinical
  benefit, complementary PBP binding and in-vitro findings support adding
  imipenem or meropenem.

## Prolonged treatment nuance

example: CRAB osteomyelitis

source_position: >
  For prolonged courses, there are no data establishing the value of maintaining
  the carbapenem throughout therapy. After sustained clinical improvement,
  discontinuing the carbapenem component may be reasonable.

evidence_level_for_this_step: panel judgment / no direct clinical data reported

## Resistance and AST

resistance_mechanisms_incompletely_characterized: true

reported_candidates:
  - PBP1a/1b mutations
  - PBP3 mutations
  - AdeIJK efflux overexpression

confirmatory_AST_suggested: true

empiric_CRAB_specific_exception: >
  Because >95% of United States CRAB isolates are reported susceptible,
  the panel supports empiric initiation of sulbactam-durlobactam for suspected
  invasive CRAB while AST is pending.

sulbactam_durlobactam_resistance_threshold_reported:
  MIC: ">=16/4 µg/mL"

if_resistant_or_MBL:
  preferred_direction: non-sulbactam-based combination therapy
  options:
    - cefiderocol
    - minocycline
    - polymyxin B
    - tigecycline

special_uncertainty: >
  Limited in-vitro data suggest that sulbactam-durlobactam may enhance
  cefiderocol activity even in sulbactam-durlobactam-resistant or MBL-producing
  settings, but the panel does not elevate this observation over its preference
  for non-sulbactam regimens.

## Safety

section_specific_major_safety_signal: not identified in the Question 5.1 discussion

## Evidence architecture

evidence_types:
  - randomized comparative clinical trial
  - US surveillance studies
  - resistance-mechanism studies
  - in-vitro combination studies
  - mechanistic PBP-binding evidence
  - expert-panel extrapolation

candidate_load_bearing_citations:
  - 493
  - 494
  - 495
  - 501
  - 503
  - 504
  - 505
  - 506
  - 507
  - 508
  - 509
  - 510
  - 511

principal_uncertainties:
  - Incremental clinical benefit of adding imipenem or meropenem has not been
    directly demonstrated.
  - Optimal management of sulbactam-durlobactam-resistant CRAB is undefined.
  - Resistance emergence during therapy remains incompletely characterized.
  - Evidence for de-escalating the carbapenem during prolonged therapy is absent.

table_dependencies:
  Table_1:
    sulbactam_durlobactam:
      normal_renal_hepatic_function: >
        2 g total (1 g sulbactam + 1 g durlobactam) IV every 6 h,
        infused over 3 h.
      augmented_clearance_CrCl_ge_130: >
        2 g IV every 4 h, infused over 3 h.
      supplemental_material_dependency: true
    imipenem_or_meropenem:
      use_global_Table_1_dosing: true

  Table_2:
    sulbactam_durlobactam_CRAB_susceptible_breakpoint: "<=4/4 µg/mL"

---

# 4. Question 5.2 — High-dose ampicillin-sulbactam

question: >
  What is the role of ampicillin-sulbactam for the treatment of invasive
  CRAB infections?

## Suggested approach

role: TEMPORARY BRIDGING THERAPY ONLY

regimen:
  - high-dose ampicillin-sulbactam
  - total daily sulbactam dose: 9 g
  - PLUS at least one additional agent:
      - cefiderocol
      - minocycline
      - polymyxin B

stop_bridge_when: >
  Sulbactam-durlobactam plus imipenem or meropenem becomes available and
  can be initiated.

## Mechanistic rationale

sulbactam:
  - at sufficiently high exposure binds and saturates PBP1a/1b and PBP3
  - has demonstrated activity in pharmacodynamic studies, animal models,
    and clinical-outcome studies
  - may show activity even when isolates are categorized as nonsusceptible
    by standard testing

major_disadvantage_vs_sulbactam_durlobactam: >
  Ampicillin-sulbactam lacks a beta-lactamase inhibitor that protects
  sulbactam against the beta-lactamases commonly produced by CRAB.

## Susceptibility framework

ampicillin_sulbactam_fixed_ratio: "2:1"
example:
  reported_MIC: "8/4 µg/mL"
  inferred_sulbactam_MIC: "4 µg/mL"

surveillance:
  CRAB_susceptible_to_sulbactam: approximately 10%

AST_problem: >
  Non-reference susceptibility methods may inaccurately categorize
  ampicillin-sulbactam susceptibility in CRAB. The guidance specifically
  raises concern that isolates called susceptible by methods other than
  reference broth microdilution may actually be nonsusceptible.

clinical_consequence: >
  False susceptibility is especially consequential because invasive CRAB
  infections have substantial mortality.

## Dose-exposure rationale

high_dose_example:
  ampicillin_sulbactam: "9 g IV every 8 h by prolonged infusion"
  composition_per_9_g_dose:
    ampicillin: 6 g
    sulbactam: 3 g
  total_daily_sulbactam: 9 g

murine_lung_PKPD:
  total_daily_sulbactam_4_g:
    probability_target_attainment: ">90%"
    reported_MIC_limit: "<=4 µg/L"
  total_daily_sulbactam_9_g:
    reported_coverage_extension: "MIC up to 8 µg/mL"

SOURCE_INTEGRITY_FLAG_1:
  issue: >
    Page 55 reports the lower MIC threshold as "<=4 µg/L", whereas the
    immediately adjacent threshold and the guideline breakpoint framework are
    expressed in µg/mL.
  status: >
    Preserve exactly as reported; do not silently normalize.
  action_for_final_SEA: >
    Check cited PK/PD source(s) [517,518] or an erratum before reproducing
    the lower threshold as a definitive clinical value.

## Clinical evidence

meta_analyses_refs_519_520:
  scope:
    studies: ">20 observational studies and/or clinical trials"
    patients: ">2,000 CRAB infections"
  direction:
    - sulbactam-containing regimens associated with improved clinical outcomes
      versus alternative regimens
  common_comparators:
    - polymyxin-based regimens
    - tetracycline-based regimens

major_limitations:
  - predominantly observational evidence
  - small component studies
  - heterogeneous regimens
  - heterogeneous dosing
  - inadequate distinction between colonization and infection
  - many patients infected with sulbactam-resistant isolates

five_clinical_trials_with_sulbactam_arm:
  citations:
    - 501
    - 502
    - 527
    - 528
    - 529
  survival_pattern:
    - only one trial reported a statistically significant survival advantage
      according to the guidance
    - all reportedly showed numerically greater survival in the
      sulbactam-containing arm

safety:
  high_dose_sulbactam: >
    The guidance reports no identified safety signal across the clinical studies
    reviewed.

## Why the panel still favors high dose even if AST says susceptible

source_logic:
  1: Standard dosing may be pharmacologically sufficient for truly susceptible isolates.
  2: AST can misclassify susceptibility.
  3: High-dose exposure has not shown an important toxicity signal in the cited evidence.
  4: Undertreatment of invasive CRAB has potentially severe consequences.
  5: Therefore, the panel favors high-dose prolonged-infusion therapy even when
     susceptibility is reported.

## Combination requirement

clinical_proof_that_combination_is_superior: limited

mechanistic_reasoning: >
  Sulbactam remains vulnerable to hydrolysis without durlobactam; therefore the
  panel favors adding another active agent.

## Evidence architecture

evidence_types:
  - pharmacodynamic models
  - animal infection models
  - surveillance/AST studies
  - susceptibility-method comparison studies
  - meta-analyses
  - clinical trials
  - observational studies
  - expert-panel risk-benefit judgment

candidate_load_bearing_citations:
  - 517
  - 518
  - 519
  - 520
  - 521
  - 522
  - 523
  - 524
  - 525
  - 526
  - 501
  - 527
  - 528
  - 529
  - 530

principal_uncertainties:
  - No strong clinical evidence establishes that combination therapy is superior.
  - Optimal dose according to true sulbactam MIC remains complicated by AST reliability.
  - Evidence supporting sulbactam regimens includes considerable observational
    and heterogeneous data.
  - Ampicillin-sulbactam is explicitly subordinated to sulbactam-durlobactam
    in this 2026 guidance.

table_dependencies:
  Table_1:
    high_dose_ampicillin_sulbactam:
      target_total_daily_sulbactam: 9 g
      option_A: >
        9 g ampicillin-sulbactam (6 g ampicillin + 3 g sulbactam)
        IV every 8 h infused over 4 h.
      option_B: >
        27 g ampicillin-sulbactam (18 g ampicillin + 9 g sulbactam)
        IV as continuous infusion over 24 h.
      supplemental_material_dependency: true

  Table_2:
    ampicillin_sulbactam_CRAB_susceptible_breakpoint: "<=8/4 µg/mL"

---

# 5. Question 5.3 — Cefiderocol

question: >
  What is the role of cefiderocol therapy for the treatment of invasive
  CRAB infections?

## Suggested approach

role: alternative combination agent

regimen:
  - cefiderocol
  - PLUS at least one other active agent:
      - high-dose ampicillin-sulbactam
      - minocycline
      - polymyxin B

rationale_based_positioning: >
  Reserve primarily for sulbactam-durlobactam resistance or as bridging
  therapy while awaiting sulbactam-durlobactam.

## Microbiologic activity

overall_CRAB_in_vitro_susceptibility: ">90%"

NDM_producing_CRAB:
  cefiderocol_susceptibility: approximately 60%
  US_frequency: described as uncommon

resistance_during_therapy:
  frequency: not well quantified
  mechanisms_described:
    - disruption/downregulation of iron uptake pathways
    - pirA alterations
    - piuA alterations
    - increased beta-lactamase expression, including ADCs

PKPD_problem: >
  A. baumannii appears to require higher cefiderocol PK/PD exposures for
  optimal killing than several other gram-negative pathogens, and animal
  infection models have shown variable bactericidal activity.

## Randomized clinical evidence summarized by guidance

trial_ref_259:
  source_reported_subgroup_size: 54
  28_day_survival:
    cefiderocol: "51% (20/39)"
    alternative_predominantly_polymyxin: "82% (14/17)"

SOURCE_INTEGRITY_FLAG_2:
  issue: >
    The source states that this randomized-trial subgroup contained 54 patients,
    but the displayed treatment-arm denominators are 39 and 17, which sum to 56.
  status: unresolved internal numerical inconsistency
  action_for_final_SEA: >
    Audit citation 259 before reproducing the subgroup size or denominators as
    independently confirmed data.

trial_ref_539:
  population: 47 patients with CRAB pneumonia
  endpoint: 14-day survival
  cefiderocol: "78% (18/23)"
  high_dose_extended_infusion_meropenem: "83% (20/24)"
  panel_concern: >
    Similar outcome to a comparator considered to lack meaningful CRAB activity
    was viewed as concerning despite the small sample.

trial_ref_325:
  population: 25 patients with CRAB bacteremia
  endpoint: 30-day survival
  cefiderocol: "55% (6/11)"
  alternative_mostly_ampicillin_sulbactam_plus_polymyxin: "50% (7/14)"

## Observational/meta-analytic evidence

meta_analysis_ref_540:
  included:
    - 1 clinical trial
    - 7 observational studies
  pooled_30_day_survival:
    cefiderocol_based: "58% (200/345)"
    alternative: "40% (182/455)"

meta_analysis_ref_541:
  included:
    - 4 observational studies
  30_day_survival:
    cefiderocol: "62% (104/169)"
    alternative: "37% (95/257)"

important_comparator_limitation: >
  No alternative-treatment patients in these observational analyses received
  sulbactam-durlobactam.

heterogeneity: significant

## Core evidence tension

randomized_evidence:
  direction: uncertain to concerning

observational_evidence:
  direction: comparatively favorable

panel_resolution: >
  Because clinical-trial findings remain uncertain and direct comparison with
  sulbactam-durlobactam is absent, cefiderocol is not elevated to preferred
  therapy despite strong in-vitro susceptibility.

## Evidence architecture

evidence_types:
  - surveillance studies
  - resistance-mechanism studies
  - animal PK/PD models
  - randomized clinical trials/subgroup analyses
  - observational studies
  - meta-analyses

candidate_load_bearing_citations:
  - 300
  - 322
  - 437
  - 494
  - 259
  - 325
  - 539
  - 540
  - 541
  - 531
  - 532
  - 533
  - 534
  - 535
  - 536
  - 537
  - 538

principal_uncertainties:
  - No direct comparative study versus sulbactam-durlobactam.
  - Randomized and observational evidence point in different directions.
  - Resistance emergence during therapy is incompletely quantified.
  - NDM substantially reduces expected susceptibility.

table_dependencies:
  Table_1:
    cefiderocol:
      standard: "2 g IV every 8 h, infused over 3 h"
      CrCl_ge_120: "2 g IV every 6 h, infused over 3 h"
  Table_2:
    cefiderocol_CRAB_susceptible_breakpoint: "<=4 µg/mL"

---

# 6. Question 5.4 — Minocycline and tetracycline derivatives

question: >
  What is the role of minocycline for the treatment of invasive CRAB infections?

## Suggested approach

role: alternative combination agent

regimen:
  - minocycline
  - PLUS at least one additional active agent:
      - high-dose ampicillin-sulbactam
      - cefiderocol
      - polymyxin B

rationale_based_positioning: >
  Use principally for sulbactam-durlobactam resistance or as interim therapy
  pending sulbactam-durlobactam availability.

## Minocycline susceptibility and PK/PD

formulations:
  - IV
  - oral

CLSI_2025_susceptible_breakpoint: "<=1 µg/mL"

in_vitro_activity_at_revised_breakpoint: "<50% of CRAB isolates"

resistance_mechanisms:
  - AdeABC overexpression
  - TetB-associated efflux

resistance_emergence_frequency: not well described

suggested_dose:
  - 200 mg every 12 h

PK_model:
  at_MIC_le_1:
    stasis_target: high probability of attainment
    1_log_kill_target: not reliably attained

important_pharmacologic_constraint: >
  Minocycline rapidly distributes into tissues, producing relatively low serum
  and urinary concentrations.

## Clinical evidence

randomized_CRAB_trials_of_minocycline: none

observational_evidence:
  limitations:
    - small samples
    - frequently absent comparator groups
    - colonization-versus-infection ambiguity
    - heterogeneous populations
  direction:
    - several reports describe favorable outcomes

## Tigecycline context

formulation: IV only
A_baumannii_breakpoint:
  CLSI: none
  FDA: none

high_dose_regimen:
  loading: 200 mg IV once
  maintenance: 100 mg IV every 12 h

clinical_direction: >
  High-dose tigecycline has produced outcomes comparable with alternative agents
  in cited clinical-outcome studies.

preclinical_support:
  - dose-dependent activity in hollow-fiber models

PKPD_warning: >
  Reduced efficacy is suggested when MIC values exceed 1 µg/mL.

minocycline_vs_tigecycline_direct_comparative_trials: none

panel_preference_between_tetracyclines: >
  Minocycline is preferred when a tetracycline derivative is selected because
  a susceptibility breakpoint exists for minocycline.

## Omadacycline context

formulations:
  - IV
  - oral

A_baumannii_breakpoints:
  CLSI: none
  FDA: none

PKPD:
  - activity appears limited to stasis
  - higher exposure appears necessary than for other organisms

animal_model:
  - similar efficacy to tigecycline in a neutropenic murine thigh model

clinical_data: limited

observational_CRAB_pneumonia_study:
  n: 40
  28_day_survival:
    omadacycline: "60% (12/20)"
    tigecycline: "60% (12/20)"

panel_position: >
  Omadacycline is not suggested unless neither minocycline nor tigecycline
  is available.

## Safety

minocycline_GI_intolerance:
  approximate_frequency: "20–25%"
  principal_event: nausea
  comparison: similar frequency to tigecycline

## Evidence architecture

evidence_types:
  - susceptibility surveillance
  - population PK modeling
  - observational clinical reports
  - hollow-fiber models
  - animal infection models
  - limited comparative observational evidence
  - expert-panel synthesis

candidate_load_bearing_citations:
  - 542
  - 543
  - 544
  - 545
  - 546
  - 547
  - 364
  - 548
  - 549
  - 550
  - 551
  - 552
  - 553
  - 554
  - 555
  - 556
  - 557
  - 558
  - 559
  - 560

principal_uncertainties:
  - No randomized clinical trial of minocycline for CRAB.
  - Less than half of CRAB isolates are susceptible under the revised breakpoint.
  - Modeled exposures reliably support stasis rather than 1-log killing.
  - No comparative effectiveness study versus sulbactam-durlobactam.
  - Oral availability should NOT be interpreted as evidence supporting oral
    step-down for invasive CRAB; this is not established by the section.

table_dependencies:
  Table_1:
    minocycline: "200 mg IV/PO every 12 h"
    tigecycline: "200 mg IV loading dose, then 100 mg IV every 12 h"
  Table_2:
    minocycline_CRAB_susceptible_breakpoint: "<=1 µg/mL"

---

# 7. Question 5.5 — Polymyxin B

question: >
  What is the role of polymyxin B for the treatment of invasive CRAB infections?

## Suggested approach

role: alternative combination agent

regimen:
  - polymyxin B
  - PLUS at least one other agent:
      - high-dose ampicillin-sulbactam
      - cefiderocol
      - minocycline

rationale_based_positioning: >
  Reserve for sulbactam-durlobactam resistance or as interim therapy while
  awaiting sulbactam-durlobactam.

## Susceptibility framework

CRAB_with_polymyxin_MIC_le_2: approximately 85%

CLSI_category_at_MIC_le_2: intermediate

CLSI_susceptible_category: NONE

activity_when_MIC_gt_2: diminished

polymyxin_B_vs_colistin:
  PK_profile: >
    Polymyxin B is described as having a more favorable pharmacokinetic profile.

## Comparative clinical evidence

ref_501_repeated:
  population: 125 CRAB pneumonia or bloodstream infections
  colistin_plus_imipenem_28_day_survival: "68% (42/62)"
  sulbactam_durlobactam_plus_imipenem_28_day_survival: "81% (51/63)"
  colistin_plus_imipenem_clinical_cure: "40% (25/62)"
  sulbactam_durlobactam_plus_imipenem_clinical_cure: "62% (39/63)"

colistin_monotherapy_trials:
  number_of_trials: 6
  approximate_total_n: 500
  reported_survival_range: "27–57%"

extrapolation_limit: >
  It is unknown whether these outcomes would have been better if polymyxin B,
  rather than colistin, had been used.

## Pharmacologic limitations

serum_exposure:
  - highly variable
  - may be inadequate for bactericidal activity

lung_exposure:
  - IV polymyxin activity in epithelial lining fluid is suboptimal
  - bacterial killing in lung models is inadequate

therapeutic_window:
  approximate_concentration_for_1_log10_reduction: "2 µg/mL"
  approximate_nephrotoxicity_threshold: "2 µg/mL"

clinical_implication: >
  Exposure required for meaningful systemic antibacterial activity approaches
  the exposure associated with nephrotoxicity.

## Evidence architecture

evidence_types:
  - surveillance
  - PK/PD studies
  - animal lung models
  - randomized comparative trial data involving colistin
  - multiple older colistin trials
  - expert extrapolation from colistin to polymyxin B

candidate_load_bearing_citations:
  - 563
  - 564
  - 565
  - 244
  - 247
  - 501
  - 566
  - 567
  - 568
  - 569
  - 570
  - 571
  - 572
  - 573
  - 574

principal_uncertainties:
  - Much of the clinical evidence is for colistin rather than polymyxin B.
  - No susceptible CLSI category exists.
  - Effective and nephrotoxic exposure ranges overlap substantially.
  - Pulmonary pharmacology is unfavorable.
  - Comparative effectiveness against sulbactam-durlobactam strongly favors
    avoiding polymyxins as routine preferred therapy.

table_dependencies:
  Table_1:
    polymyxin_B: >
      Dosing is not specified directly; the guidance refers to international
      consensus guidance on polymyxins.
  Table_2:
    polymyxin_CRAB:
      susceptible_category: none
      MIC_le_2: intermediate

---

# 8. Question 5.6 — Nebulized antibiotics for CRAB pneumonia

question: >
  What is the role of nebulized antibiotics for the treatment of CRAB pneumonia?

## Suggested approach

routine_use: NOT SUGGESTED

possible_selective_adjunctive_use:
  - documented sulbactam-durlobactam resistance
  - inadequate clinical response to systemic treatment

## Randomized evidence

RCT_1_ref_461:
  nebulized_agent: colistin
  total_n: 100
  A_baumannii_fraction: 65%

RCT_2_ref_462:
  nebulized_agent: amikacin/fosfomycin
  total_n: 142
  A_baumannii_fraction: 20%

RCT_3_ref_463:
  nebulized_agent: amikacin
  total_n: 508
  A_baumannii_fraction: 29%

common_design_feature:
  - concomitant systemic antibiotics permitted

survival_result:
  - no demonstrated survival improvement in the overall populations
  - no demonstrated survival improvement in drug-resistant-pathogen subgroups

## Synthesized evidence

systematic_reviews_and_meta_analyses:
  citations:
    - 464
    - 465
    - 466
    - 467
  survival:
    benefit_identified: false
  clinical_response:
    - some analyses report modest improvement

## PK/PD versus clinical-outcome tension

PKPD:
  aerosolized_antibiotics:
    - can achieve high epithelial-lining-fluid concentrations

clinical_delivery_constraints:
  - poor penetration into consolidated lung parenchyma
  - heterogeneous distribution throughout infected airways
  - difficulty sustaining bactericidal exposure
  - off-label use of parenteral formulations
  - nebulization devices such as jet nebulizers may not be optimized for
    pulmonary drug delivery

professional_society_consensus: inconsistent

## Adverse effects

important_events:
  - bronchoconstriction
  - laryngeal injury
  - hypersensitivity pneumonitis

## Evidence architecture

evidence_types:
  - randomized placebo-controlled adjunctive-treatment trials
  - systematic reviews/meta-analyses
  - observational studies
  - PK/PD modeling
  - drug-delivery/device literature
  - expert-panel synthesis

candidate_load_bearing_citations:
  - 461
  - 462
  - 463
  - 464
  - 465
  - 466
  - 467
  - 468
  - 469
  - 470
  - 471
  - 472
  - 473
  - 474
  - 475
  - 476
  - 477

principal_uncertainties:
  - A. baumannii represented only subsets of several pneumonia trials.
  - High modeled lung concentrations have not translated into survival benefit.
  - Delivery techniques and formulations may limit generalizability of older studies.
  - Selective salvage use remains based more on biological plausibility and
    clinical necessity than demonstrated survival benefit.

---

# 9. Cross-question evidence matrix

| Therapy / strategy | Panel position | Strongest evidence architecture | Load-bearing result | Major limitation |
|---|---|---|---|---|
| Sulbactam-durlobactam + imipenem/meropenem | Preferred | Randomized trial + surveillance + mechanistic/in-vitro | 28-d survival 81% vs 68%; cure 62% vs 40% against colistin+imipenem | Comparator is not a preferred modern regimen; incremental benefit of carbapenem not clinically proven |
| High-dose ampicillin-sulbactam + second agent | Bridge only | Meta-analyses + clinical trials + PK/PD + animal models | >2,000 patients represented in two meta-analyses; consistent numerical direction favoring sulbactam-containing regimens | Highly heterogeneous and largely observational; AST reliability problem |
| Cefiderocol + second agent | Alternative / resistant or bridge | RCT subgroups + observational meta-analyses + PK/PD | Observational pooled survival favors cefiderocol, while RCT findings are inconsistent/concerning | No comparison with sulbactam-durlobactam; discordant evidence; source denominator inconsistency |
| Minocycline + second agent | Alternative / resistant or bridge | PK modeling + observational evidence | High probability of stasis target attainment at MIC <=1 µg/mL | <50% susceptibility; no CRAB RCT; does not reliably attain 1-log-kill target |
| Polymyxin B + second agent | Alternative / resistant or bridge | PK/PD + colistin clinical trials | Colistin monotherapy trial survival generally 27–57% | Narrow therapeutic index, nephrotoxicity, poor pulmonary PK, indirect evidence for polymyxin B |
| Adjunctive nebulized therapy | Not routine | 3 RCTs + meta-analyses + PK/PD | No survival benefit demonstrated | Heterogeneous delivery; organism subgroups; modeled concentrations do not translate to outcome benefit |

---

# 10. CRAB-specific dosing and breakpoint crosswalk

## Dosing dependencies from global Table 1

sulbactam_durlobactam:
  standard:
    dose: 2 g total
    components:
      sulbactam: 1 g
      durlobactam: 1 g
    route: IV
    interval: q6h
    infusion: 3 h
  CrCl_ge_130:
    interval: q4h
    infusion: 3 h
  supplemental_material: referenced

ampicillin_sulbactam_high_dose:
  target_sulbactam_daily_dose: 9 g
  regimen_A:
    total_product_dose: 9 g
    components:
      ampicillin: 6 g
      sulbactam: 3 g
    route: IV
    interval: q8h
    infusion: 4 h
  regimen_B:
    total_product_daily_dose: 27 g
    components:
      ampicillin: 18 g
      sulbactam: 9 g
    route: IV continuous infusion
    infusion_duration: 24 h
  supplemental_material: referenced

cefiderocol:
  standard: "2 g IV q8h over 3 h"
  CrCl_ge_120: "2 g IV q6h over 3 h"

minocycline:
  dose: "200 mg IV/PO q12h"

tigecycline:
  load: "200 mg IV once"
  maintenance: "100 mg IV q12h"

polymyxin_B:
  dosing: delegated to international polymyxin consensus guidance

## CRAB breakpoint dependencies from global Table 2

ampicillin_sulbactam:
  susceptible: "<=8/4 µg/mL"

sulbactam_durlobactam:
  susceptible: "<=4/4 µg/mL"
  section_reported_resistance_trigger: ">=16/4 µg/mL"

cefiderocol:
  susceptible: "<=4 µg/mL"

minocycline:
  susceptible: "<=1 µg/mL"

polymyxins:
  susceptible_category: none
  MIC_le_2: intermediate

implementation_warning: >
  CRAB is unusually dependent on correct interpretation of AST methodology,
  not simply the reported S/I/R category. This is especially important for
  ampicillin-sulbactam, where the section explicitly warns about misclassification
  with non-reference methods.

---

# 11. Cross-cutting section synthesis

## 11.1 Sulbactam-centered treatment architecture

The section is organized around sulbactam as the principal active pharmacophore
for invasive CRAB. Durlobactam changes the usefulness of sulbactam by protecting
it from common class A, C, and D beta-lactamases. This produces a hierarchy in
which sulbactam-durlobactam plus a carbapenem is preferred, while unprotected
high-dose sulbactam is relegated to temporary bridging therapy.

This distinction should be preserved in the final SEA. Treating
sulbactam-durlobactam and high-dose ampicillin-sulbactam as two coequal
"sulbactam options" would misrepresent the 2026 guidance.

## 11.2 Combination therapy is the default architecture

Every systemic regimen endorsed for invasive CRAB in this section is combination
based:

- sulbactam-durlobactam + carbapenem
- high-dose ampicillin-sulbactam + another active drug
- cefiderocol + another active drug
- minocycline + another active drug
- polymyxin B + another active drug

However, the evidentiary basis for combination therapy is not uniform.
For the preferred sulbactam-durlobactam regimen, addition of a carbapenem is
supported largely by mechanistic and in-vitro evidence rather than a clinical
trial comparing sulbactam-durlobactam monotherapy with combination therapy.
For the alternative agents, combination use reflects concerns regarding uncertain
clinical effectiveness, resistance, PK/PD limitations, and high CRAB mortality.

## 11.3 In-vitro susceptibility does not map cleanly to clinical confidence

Examples:

- Sulbactam-durlobactam:
    >95% US susceptibility and the strongest clinical evidence in the section.

- Cefiderocol:
    >90% susceptibility overall, yet clinical trial data remain uncertain and
    cefiderocol is only an alternative.

- Minocycline:
    <50% susceptible using the revised <=1 µg/mL breakpoint, and modeled exposure
    supports stasis more reliably than 1-log killing.

- Polymyxins:
    approximately 85% have MIC <=2 µg/mL, but this corresponds only to the
    CLSI intermediate category and exposures required for efficacy approach
    nephrotoxic concentrations.

- Ampicillin-sulbactam:
    only approximately 10% of CRAB are reported susceptible, but high-dose
    pharmacology may partially extend activity beyond the susceptible range;
    AST itself may also be unreliable.

The final SEA should therefore avoid using percent susceptibility as a proxy for
comparative therapeutic quality.

## 11.4 Colonization bias affects much of the evidence base

CRAB is frequently recovered from respiratory and wound cultures, and the source
emphasizes difficulty distinguishing infection from colonization. This is
particularly relevant when appraising observational studies and meta-analyses,
because inadequate case definition may bias estimates of treatment effectiveness.

## 11.5 Mortality endpoints are strongly host-confounded

Patients with invasive CRAB are often critically ill with major comorbidity.
Mortality therefore reflects:

- antimicrobial activity
- underlying illness
- severity of infection
- source control
- baseline prognosis

This does not invalidate comparative survival endpoints, particularly randomized
comparisons, but it increases caution when interpreting uncontrolled studies.

---

# 12. Safety and implementation synthesis

highest_priority_safety_concerns:

polymyxins:
  - nephrotoxicity
  - narrow therapeutic window
  - variable systemic exposure
  - poor pulmonary pharmacology

tetracyclines:
  - minocycline/tigecycline gastrointestinal intolerance
  - low serum and urinary concentrations for minocycline
  - uncertain bactericidal exposure

nebulized_antibiotics:
  - bronchoconstriction
  - laryngeal injury
  - hypersensitivity pneumonitis
  - delivery-device limitations

sulbactam_regimens:
  - high-dose sulbactam has not produced an important safety signal in the
    clinical literature summarized by the guidance
  - implementation complexity includes prolonged/continuous infusion and
    dependence on supplemental dosing information

operational_requirements:
  - rapid access to sulbactam-durlobactam
  - reliable CRAB AST
  - awareness of local NDM/MBL epidemiology
  - ability to administer prolonged infusions
  - renal-function-based adjustment outside the normal-function Table 1 assumptions
  - toxicity monitoring when polymyxins are required
  - stewardship review before treating respiratory/wound isolates
  - reassessment of need for combination components during prolonged courses

oral_transition_warning: >
  Although minocycline is available orally, this CRAB section does not establish
  oral step-down therapy as effective for invasive CRAB. Its relatively low
  serum concentrations reinforce the need not to infer an oral-transition
  recommendation solely from formulation availability.

---

# 13. Evidence architecture summary

evidence_maturity_by_domain:

sulbactam_durlobactam:
  direct_clinical_evidence: strongest within CRAB section
  includes_randomized_trial: yes
  direct_modern_comparator: limited
  mechanistic_support: strong
  surveillance_support: strong

ampicillin_sulbactam:
  direct_clinical_evidence: moderate but heterogeneous
  preclinical_support: extensive
  meta_analytic_support: yes
  major_methodological_problem: heterogeneity + observational bias + AST uncertainty

cefiderocol:
  direct_clinical_evidence: mixed
  randomized_evidence: concerning/inconclusive
  observational_evidence: favorable
  evidence_conflict: substantial

minocycline:
  direct_clinical_evidence: weak-to-limited
  randomized_CRAB_trial: no
  PKPD_support: stasis-level target attainment
  observational_support: limited

polymyxin_B:
  direct_specific_evidence: limited
  evidence_often_extrapolated_from_colistin: yes
  toxicity_constraint: major

nebulized_antibiotics:
  randomized_evidence: multiple trials
  survival_benefit: not demonstrated
  biological_PKPD_rationale: present
  clinical_translation: poor

---

# 14. Preliminary appraisal flags
## MODEL INFERENCE — NOT FINAL SEA SCORES

These flags identify issues for final appraisal; they are not final judgments.

1. **The preferred regimen has materially better evidence than the alternatives,
   but not every component of the preferred combination has equivalent evidentiary
   support.**
   - Sulbactam-durlobactam itself has randomized comparative evidence.
   - The added carbapenem relies importantly on mechanistic/in-vitro evidence.

2. **The comparator in the key sulbactam-durlobactam trial limits comparative
   inference.**
   - Colistin plus imipenem is not considered a preferred or alternative regimen
     by the same guidance.
   - The trial supports superiority/noninferiority relative to that regimen,
     not necessarily relative to every plausible modern CRAB strategy.

3. **Ampicillin-sulbactam evidence is clinically substantial but methodologically
   heterogeneous.**
   - More than 2,000 patients appear in the cited meta-analytic evidence.
   - Much of the evidence is observational, with variable dosing and imperfect
     infection-versus-colonization classification.

4. **AST uncertainty is not a peripheral laboratory issue; it directly alters
   treatment selection.**
   - High-dose ampicillin-sulbactam is favored even when reported susceptible
     partly because of concern for false susceptibility classification.

5. **Cefiderocol contains the section's clearest conflict between evidence streams.**
   - In-vitro activity and observational meta-analyses are favorable.
   - Randomized clinical findings are inconsistent or concerning.
   - No comparative data against sulbactam-durlobactam are reported.

6. **Minocycline's clinical role is constrained more by evidence quality and
   pharmacodynamic limits than by tolerability alone.**
   - No CRAB RCT.
   - <50% susceptibility at the revised breakpoint.
   - Modeled exposure supports stasis more reliably than bactericidal killing.

7. **Polymyxin B is a salvage option whose pharmacology and toxicity materially
   weaken its implementation value.**
   - The source explicitly describes overlap between concentrations needed for
     antibacterial effect and nephrotoxicity.

8. **Nebulized therapy demonstrates an important surrogate-versus-outcome mismatch.**
   - High epithelial-lining-fluid exposure is pharmacologically achievable.
   - Survival benefit has not been demonstrated.

9. **Combination therapy is a strong guidance-level recommendation architecture,
   but the comparative evidence proving the superiority of combination therapy
   per se is incomplete.**

10. **The section contains at least two source-integrity issues that should be
    resolved before final quantitative reproduction.**
    - p. 55: `<=4 µg/L` versus surrounding µg/mL breakpoint units.
    - p. 56: randomized cefiderocol subgroup reported as n=54 while displayed
      denominators 39 + 17 = 56.

---

# 15. Candidate selective reference audit

Priority A — directly load-bearing for final recommendation hierarchy:
  - [501] randomized sulbactam-durlobactam comparative trial
  - [517, 518] high-dose sulbactam PK/PD and murine lung exposure
  - [519, 520] sulbactam-regimen meta-analyses
  - [525, 526] ampicillin-sulbactam AST reliability
  - [259] cefiderocol randomized CRAB subgroup; also resolve denominator discrepancy
  - [539] cefiderocol versus high-dose meropenem CRAB pneumonia trial
  - [325] cefiderocol CRAB bacteremia randomized data
  - [540, 541] cefiderocol meta-analyses
  - [547] minocycline population PK/PD
  - [569–574] colistin trial evidence underlying polymyxin concerns
  - [461–467] nebulized-antibiotic randomized and synthesized evidence

Priority B — important mechanistic/implementation support:
  - [493–507] sulbactam-durlobactam mechanism and carbapenem combination rationale
  - [508–511] sulbactam-durlobactam resistance mechanisms
  - [521–524] sulbactam surveillance/high-dose exposure
  - [531–538] cefiderocol resistance and PK/PD
  - [542–546] minocycline susceptibility/resistance
  - [551–560] tigecycline/omadacycline context
  - [563–568] polymyxin susceptibility and PK/PD
  - [468–477] nebulized drug delivery, society guidance, and adverse effects

audit_objectives:
  - verify trial population and endpoint denominators
  - verify the p. 55 sulbactam MIC unit
  - distinguish randomized from observational evidence
  - identify whether meta-analyses pooled monotherapy and combination therapy
  - characterize comparator regimens
  - preserve whether endpoints are mortality, clinical cure, microbiological
    response, or PK/PD surrogates
  - avoid treating the guidance's secondary summaries as independent primary-study appraisal

---

# 16. Section-specific omissions and unresolved items

not_evaluated_in_this_deep_pass:
  - primary articles cited by the guidance
  - study-level risk of bias beyond limitations explicitly reported by the guidance
  - supplemental dosing material
  - renal/hepatic dose adjustments beyond global Table 1
  - local formulary/access considerations
  - post-March-1-2026 evidence
  - final recommendation certainty using a formal framework
  - final SEA numeric ratings

known_unresolved_items:
  - p. 55 MIC unit inconsistency
  - p. 56 cefiderocol subgroup denominator inconsistency
  - exact incremental benefit of carbapenem addition to sulbactam-durlobactam
  - optimal therapy for sulbactam-durlobactam-resistant/MBL-producing CRAB
  - optimal duration of combination therapy
  - whether and when carbapenem de-escalation during prolonged therapy is beneficial
  - clinical superiority of combination therapy versus optimally selected monotherapy
  - role of oral minocycline as step-down therapy for invasive infection

---

# 17. Handoff synthesis for final hierarchical SEA

CRAB_SECTION_THESIS: >
  The 2026 IDSA guidance establishes sulbactam-durlobactam plus imipenem or
  meropenem as the preferred treatment architecture for invasive CRAB.
  High-dose ampicillin-sulbactam is no longer positioned as a coequal definitive
  alternative when sulbactam-durlobactam is available; instead, it serves as
  combination bridging therapy. Cefiderocol, minocycline, and polymyxin B are
  similarly relegated to combination-based alternatives, principally for
  sulbactam-durlobactam resistance or temporary lack of access.

EVIDENCE_THESIS: >
  Sulbactam-durlobactam has the strongest direct comparative clinical evidence
  within the section, supported by high US susceptibility and mechanistic data.
  The alternative regimens have important but less direct or less internally
  consistent evidence: ampicillin-sulbactam relies heavily on heterogeneous
  sulbactam literature and PK/PD; cefiderocol has discordant randomized and
  observational outcomes; minocycline lacks randomized CRAB trials and has
  limited susceptibility/PK target attainment; and polymyxins are constrained
  by toxicity and unfavorable PK.

IMPLEMENTATION_THESIS: >
  Successful implementation depends on distinguishing infection from
  colonization, obtaining reliable AST, rapidly accessing sulbactam-durlobactam,
  using prolonged-infusion/high-exposure dosing when required, recognizing MBL
  resistance, and avoiding routine reliance on polymyxins or nebulized therapy.

MAJOR_CAUTION: >
  High in-vitro susceptibility should not be treated as equivalent to strong
  clinical evidence. Cefiderocol is the clearest example; conversely,
  ampicillin-sulbactam illustrates how PK/PD and uncertainty in AST can support
  treatment at exposures extending beyond conventional susceptibility
  interpretation.

FINAL_SYNTHESIS_REQUIREMENTS:
  - retain CRAB as its own major section in the final HTML
  - preserve the treatment hierarchy rather than presenting an undifferentiated drug list
  - explicitly distinguish preferred treatment from bridge/salvage options
  - include the sulbactam-durlobactam randomized quantitative findings
  - include the cefiderocol randomized-versus-observational evidence conflict
  - include the AST reliability issue for ampicillin-sulbactam
  - include the revised minocycline breakpoint and PK/PD limitation
  - include the polymyxin efficacy-toxicity overlap
  - include the negative survival evidence for nebulized antibiotics
  - resolve the two identified source-integrity flags before final quantitative publication
  - perform final scoring only after all organism sections are reconciled

---

# 18. Deep-pass gate status

section_boundary_verified: PASS
global_context_applied: PASS
all_CRAB_questions_extracted: PASS — 6/6
suggested_approaches_preserved: PASS
therapy_hierarchy_reconstructed: PASS
quantitative_results_preserved: PASS
negative_and_conflicting_evidence_preserved: PASS
mechanistic_context_preserved: PASS
AST_constraints_preserved: PASS
PKPD_constraints_preserved: PASS
safety_constraints_preserved: PASS
stewardship_constraints_preserved: PASS
Table_1_dependencies_mapped: PASS
Table_2_dependencies_mapped: PASS
supplement_dependencies_mapped: PASS
candidate_reference_audit_created: PASS
source_integrity_flags_identified: PASS — 2
primary_study_verification: NOT PERFORMED
final_SEA_scores: WITHHELD
final_verdict: WITHHELD

CRAB_DEEP_PASS_STATUS: COMPLETE
READY_FOR_HIERARCHICAL_SYNTHESIS: YES