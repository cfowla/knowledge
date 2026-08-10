# CIAG481 — HIERARCHICAL SEA DEEP PASS
## Section 3: Carbapenem-Resistant Enterobacterales (CRE)

## 0. Artifact status

artifact_type: SEA intermediate artifact
stage: Deep section pass
parent_context: CIAG481 — SEA Pass 0 Global Context Packet
source_file: ciag481.pdf
source_scope: PDF pp. 30–42
semantic_scope: Section 3 — Carbapenem-Resistant Enterobacterales (CRE)
questions_covered:
  - Q3.1 — CRE uncomplicated UTI
  - Q3.2 — CRE complicated UTI
  - Q3.3 — invasive non-carbapenemase-producing CRE
  - Q3.4 — invasive KPC-producing Enterobacterales
  - Q3.5 — invasive NDM-producing Enterobacterales
  - Q3.6 — invasive OXA-48-like-producing Enterobacterales
  - Q3.7 — tetracycline derivatives for CRE
  - Q3.8 — combination therapy for CRE

boundary_handling:
  page_30:
    - AmpC-E material before the Section 3 heading excluded.
    - CRE introductory material beginning on page 30 included.
  page_42:
    - Q3.8 rationale included in full.
    - Section 4 DTR P. aeruginosa material excluded.

final_appraisal_status: NOT YET PERFORMED
final_scores_status: WITHHELD
reason_scores_withheld: >
  This is one organism-level extraction packet in a hierarchical SEA.
  Final scoring requires reconciliation with the global Pass 0 packet,
  all other organism sections, Tables 1–2, disclosures, and the
  selective reference audit.

primary_grounding_rule: >
  Statements below represent what the IDSA guidance reports or suggests.
  Results attributed to cited studies have not been independently verified
  against the primary publications unless explicitly identified otherwise.

---

# 1. Section function and conceptual frame

section_role: >
  Section 3 converts the heterogeneous CRE phenotype into a treatment hierarchy
  based on infection site, carbapenem susceptibility, carbapenemase production,
  and specific carbapenemase family.

## 1.1 CRE definition

CRE are Enterobacterales that:

- are resistant to at least one carbapenem
  - ertapenem
  - imipenem
  - meropenem
- OR produce a carbapenemase.

important_exception:
  - Morganella spp.
  - Proteus spp.
  - Providencia spp.

These organisms may exhibit decreased imipenem susceptibility because of
structural features of their penicillin-binding proteins. For these species,
resistance to at least one carbapenem OTHER THAN imipenem is required for CRE
classification.

## 1.2 Major mechanistic division

CRE are divided into:

### Non-carbapenemase-producing CRE

Typical mechanism:

- amplification of non-carbapenemase beta-lactamases
  - e.g. ESBL enzymes
  - ampC
- PLUS decreased outer-membrane permeability/porin loss
  - OmpC/OmpF in E. coli or E. cloacae
  - OmpK35/OmpK36 in K. pneumoniae

### Carbapenemase-producing CRE

Reported to account for approximately 35%–83% of CRE in US cohorts, with the
estimated proportion strongly influenced by the CRE definition used.

Major families:

- KPC
  - serine carbapenemase
- OXA-48-like
  - serine carbapenemase
- NDM
  - metallo-beta-lactamase (MBL)
- VIM
  - MBL
- IMP
  - MBL

epidemiologic_trends_reported:
  - KPC historically concentrated in K. pneumoniae but increasingly identified
    in E. cloacae and E. coli.
  - Marked increase in NDM-producing Enterobacterales since 2021.
  - More gradual increase in OXA-48-like producers.

## 1.3 Central treatment principle

Carbapenemase identification is not merely descriptive.

The guidance treats identification of the carbapenemase FAMILY as a major
therapeutic decision point because:

- substrate profiles differ;
- beta-lactamase inhibitor activity differs;
- resistance mechanisms differ;
- preferred agents therefore differ substantially between KPC, NDM, and
  OXA-48-like infections.

Treatment suggestions assume demonstrated in-vitro activity of proposed agents.

SEA carry-forward:
  >
  CRE should not be appraised as one homogeneous resistance phenotype.
  Mechanism-directed treatment is a central architectural feature of this
  section and should remain visible in the final SEA.

---

# 2. High-level therapeutic decision architecture

SOURCE-DERIVED SYNTHESIS:

CRE infection
│
├── uUTI
│   ├── preferentially use active urinary/oral agents when possible
│   └── reserve newer broad IV CRE-active agents when alternatives exist
│
├── cUTI
│   ├── oral FQ/TMP-SMX if susceptible
│   ├── newer IV CRE-active beta-lactams preferred, especially if unstable
│   └── IV fosfomycin / aminoglycosides = alternatives
│
└── invasive infection
    │
    ├── non-carbapenemase-producing
    │   ├── meropenem/imipenem susceptible
    │   │   └── extended-infusion active carbapenem
    │   └── no carbapenem susceptible
    │       └── newer beta-lactam/beta-lactamase-inhibitor agents preferred
    │
    ├── KPC
    │   └── meropenem-vaborbactam /
    │       ceftazidime-avibactam /
    │       imipenem-relebactam
    │
    ├── NDM
    │   └── aztreonam-avibactam OR cefiderocol
    │       └── if aztreonam-avibactam unavailable:
    │           ceftazidime-avibactam + aztreonam
    │
    └── OXA-48-like
        └── ceftazidime-avibactam preferred

Cross-cutting:
- eravacycline/tigecycline are tissue-oriented alternatives, NOT preferred for
  bloodstream or urinary infections.
- routine continuation of combination therapy is NOT suggested once an active
  beta-lactam has been identified.

---

# 3. Question 3.1 — CRE uncomplicated UTI

source_pages: 31–33

question: >
  What are preferred antibiotics for the treatment of uUTIs caused by CRE?

## Suggested approach

preferred:
  - aminoglycoside as a single dose
  - ciprofloxacin
  - levofloxacin
  - nitrofurantoin
  - TMP-SMX

alternative:
  - colistin
  - oral fosfomycin
    restriction: E. coli only
  - gepotidacin
  - pivmecillinam

active_but_generally_reserved:
  - aztreonam-avibactam
  - cefiderocol
  - ceftazidime-avibactam
  - IV fosfomycin
    preference: particularly E. coli
  - imipenem-relebactam
  - meropenem-vaborbactam

reservation_principle: >
  Newer/broad IV CRE-active agents are likely effective but should generally be
  preserved for situations in which resistance, availability, or intolerance
  precludes narrower options, because they are valuable agents for invasive CRE.

## Important qualifiers

- Susceptibility to several "preferred" agents is expected to be low.
- uUTI courses may be completed before carbapenem resistance is recognized.
- Prior patient-specific urine cultures are therefore particularly important.
- Close clinical monitoring is necessary when empiric activity is uncertain.
- Mechanism may matter for pivmecillinam, particularly because KPC can hydrolyze
  mecillinam.

## Evidence architecture

- urinary PK/PD rationale
- US surveillance susceptibility studies
- clinical data extrapolated from broader uUTI evidence
- limited CRE-specific clinical outcomes
- mechanistic/in-vitro data
- murine UTI data for pivmecillinam/mecillinam
- expert-panel stewardship judgment

## Load-bearing quantitative findings

aminoglycoside_susceptibility_US_CRE:
  amikacin: 59%
  gentamicin: 47%
  plazomicin: 97%
  tobramycin: 27%
  source_citation: "[238]"

other_common_agents:
  fluoroquinolone_susceptibility: "<20%"
  TMP-SMX_susceptibility: "<20%"
  nitrofurantoin_susceptibility: "approximately 30%"
  source_citations: "[238, 240-243]"

colistin:
  CRE_collection_n: 117
  isolates_with_MIC_in_intermediate_range: "approximately 91%"
  breakpoint_note: >
    CLSI has no susceptible category for colistin against Enterobacterales;
    MIC <=2 µg/mL is categorized as intermediate.
  nephrotoxicity: "approximately 30%, even with relatively short courses"
  source_citations: "[238, 247-250]"

oral_fosfomycin:
  expected_susceptibility_carbapenem_resistant_E_coli: "approximately 80%"
  caveat: >
    Contemporary US data specifically evaluating carbapenem-resistant E. coli
    are unavailable; estimate relies on available breakpoint/surveillance data.
  source_citations: "[243, 251]"

gepotidacin:
  surveillance_collection: "approximately 600 AMR uropathogens"
  CRE_representation: "only a few isolates"
  observed_resistance: "<1%"
  CRE_specific_clinical_outcomes: "not available"
  source_citation: "[252]"

pivmecillinam_mecillinam_collection_1:
  KPC: "0% susceptible; n=174"
  NDM: "71%; n=1,094"
  OXA_48_like: "84%; n=4,042"
  non_carbapenemase_CRE: "70%; n=2,349"
  source_citation: "[253]"

pivmecillinam_collection_2:
  total_n: 105
  NDM_and_OXA48_activity: "<50%"
  KPC_activity: "none"
  source_citation: "[254]"

## Explicit uncertainty / limitations

- Direct CRE-uUTI clinical outcome data are sparse for several agents.
- Surveillance susceptibility may not translate directly to clinical efficacy.
- Gepotidacin has essentially no CRE-specific clinical outcomes evidence.
- Pivmecillinam activity varies markedly by carbapenemase type and between
  isolate collections.
- Oral fosfomycin susceptibility testing is not routinely performed.
- Colistin activity is being inferred despite absence of a CLSI susceptible category.

## Safety / toxicity

- Colistin nephrotoxicity is a major reason it remains an alternative rather
  than preferred therapy.
- Single-dose aminoglycosides reduce prolonged exposure but still require
  patient-specific toxicity consideration.

## Stewardship / resistance

- Preserve newer IV CRE-active beta-lactams when a narrower uUTI option is active.
- Review prior urine cultures when CRE is plausible.
- Do not infer pivmecillinam reliability without considering the likely
  carbapenemase mechanism.

## Global table dependencies

Table_1:
  - aminoglycoside single-dose regimens
  - fluoroquinolone dosing
  - nitrofurantoin
  - TMP-SMX
  - pivmecillinam
  - fosfomycin
  - newer IV agents

Table_2:
  - colistin: no susceptible category
  - oral fosfomycin criteria apply to E. coli urinary isolates
  - organism/agent-specific Enterobacterales breakpoints

Supplemental_Material:
  - aminoglycoside PK-guided dosing information is relevant.

## Cross-references

- Q1.1 for fuller uUTI pharmacology/efficacy discussion.
- Q3.2 for cUTI.
- Q3.4–Q3.6 for mechanism-directed newer beta-lactam selection.

## Candidate load-bearing citations for selective audit

high_priority:
  - "[238]" — CRE susceptibility distribution
  - "[243, 251]" — oral fosfomycin susceptibility
  - "[253, 254]" — mecillinam activity by carbapenemase mechanism
  - "[255]" — murine UTI mecillinam evidence
  - "[247-250]" — colistin nephrotoxicity
  - "[252]" — gepotidacin AMR surveillance

---

# 4. Question 3.2 — CRE complicated UTI

source_pages: 33–34

question: >
  What are the preferred antibiotics for the treatment of cUTI caused by CRE?

## Suggested approach

preferred_if_susceptible:
  - ciprofloxacin
  - levofloxacin
  - TMP-SMX

preferred_IV:
  - aztreonam-avibactam
  - cefiderocol
  - ceftazidime-avibactam
  - imipenem-relebactam
  - meropenem-vaborbactam

preferred_IV_context: >
  Particularly relevant when clinical instability is present.

alternative:
  - IV fosfomycin
    preference: particularly for E. coli
  - once-daily aminoglycosides
    - amikacin
    - gentamicin
    - plazomicin
    - tobramycin

## Important qualifiers

- Fluoroquinolones and TMP-SMX should be used only after susceptibility is demonstrated.
- Carbapenemase mechanism should guide choice among newer IV beta-lactams.
- IV fosfomycin should only be used after susceptibility confirmation.
- Aminoglycoside nephrotoxicity increases with duration.

## Evidence architecture

- clinical trial evidence for newer IV agents in UTI populations
- in-vitro susceptibility
- mechanism-based treatment selection
- pharmacokinetic rationale
- broader cUTI evidence
- relatively small proportion of CRE isolates within many registration trials

## Load-bearing quantitative findings

newer_IV_agents:
  trial_interpretation: >
    Trials support non-inferiority of several agents for UTI, but the proportion
    of CRE isolates enrolled across those trials was low.
  source_citations: "[138, 256-262]"

IV_fosfomycin:
  estimated_CRE_susceptibility: "approximately 50%"
  basis: application of IV fosfomycin breakpoints
  source_citations: "[251, 263]"

aminoglycosides:
  rationale: >
    High renal parenchymal concentrations support expected efficacy, but
    nephrotoxicity is duration-dependent.
  source_citations: "[72-74, 77, 79]"

## Explicit uncertainty / limitations

- Much of the "clinical trial evidence" for newer agents is not derived from
  CRE-enriched trial populations.
- Direct head-to-head trials stratified by carbapenemase mechanism are absent.
- IV fosfomycin activity is unreliable enough that AST confirmation is required.

## Safety

- Aminoglycoside duration-dependent nephrotoxicity.
- Patient stability should influence whether an oral agent is adequate.

## Stewardship

- Use oral active therapy when appropriate rather than defaulting to a
  broad-spectrum IV CRE-active agent.
- For unstable patients, early reliable IV activity takes precedence.

## Global table dependencies

Table_1:
  - newer IV beta-lactam dosing
  - aminoglycoside once-daily/PK-guided regimens
  - fluoroquinolone/TMP-SMX regimens
  - IV fosfomycin

Table_2:
  - IV fosfomycin breakpoint interpretation
  - susceptibility of all proposed agents

Supplemental_Material:
  - aminoglycoside dosing/PK details.

## Cross-references

- Q3.1 — baseline CRE susceptibility of oral/urinary agents.
- Q1.2 — broader cUTI treatment evidence.
- Q3.4–Q3.6 — carbapenemase-specific selection of newer agents.

## Candidate citations

high_priority:
  - "[138, 256-262]" — UTI registration/clinical trial evidence
  - "[251, 263]" — IV fosfomycin susceptibility
  - "[72-74]" — aminoglycoside renal PK and toxicity

---

# 5. Question 3.3 — Invasive non-carbapenemase-producing CRE

source_pages: 34–35

question: >
  What are the preferred antibiotics for invasive infections caused by CRE
  that are not carbapenemase producing?

## Suggested approach

### Phenotype A

criteria:
  - non-carbapenemase-producing
  - meropenem susceptible: MIC <=1 µg/mL
  - imipenem susceptible: MIC <=1 µg/mL
  - ertapenem non-susceptible: MIC >=1 µg/mL

suggested:
  - extended-infusion meropenem
  - OR extended-infusion imipenem

### Phenotype B

criteria:
  - non-carbapenemase-producing
  - ertapenem non-susceptible
  - susceptible to one of meropenem or imipenem but not the other

suggested:
  - extended-infusion active carbapenem MAY be considered

conditions:
  - patient not critically ill
  - adequate source control achieved

### Phenotype C

criteria:
  - non-carbapenemase-producing
  - no carbapenem susceptibility

preferred:
  - aztreonam-avibactam
  - ceftazidime-avibactam
  - imipenem-relebactam
  - meropenem-vaborbactam

alternative:
  - cefiderocol
  - eravacycline
  - tigecycline

tetracycline_restriction:
  - not appropriate for bacteremia
  - not appropriate for UTI

## Evidence architecture

- US surveillance/genotypic data
- resistance-mechanism reasoning
- beta-lactam PK/PD principles
- in-vitro beta-lactamase-inhibitor comparisons
- limited direct clinical outcome evidence
- expert consensus

## Load-bearing quantitative finding

ertapenem_resistant_but_imipenem_meropenem_susceptible_collection:
  n: 1249
  carbapenemase_gene_detected: "<3%"
  interpretation: >
    This phenotype usually reflects non-carbapenemase beta-lactamase
    amplification plus porin disruption rather than carbapenemase production.
  source_citation: "[266]"

## Mechanistic rationale

- Increased beta-lactamase expression plus impaired permeability may compromise
  ertapenem before imipenem or meropenem.
- Further increases in beta-lactamase production could theoretically compromise
  the active carbapenem during therapy.
- Newer beta-lactamase inhibitors may offer additional protection when
  beta-lactamase expression is substantial.

## Agent-ranking nuance

For isolates non-susceptible to all carbapenems:

- all four newer beta-lactam options above are preferred if active;
- the panel expresses a MODEST preference for:
  - ceftazidime-avibactam
  - imipenem-relebactam
- rationale:
  - avibactam and relebactam may inhibit the relevant enzymes somewhat more
    effectively than vaborbactam in this context.

cefiderocol:
  status: alternative
  rationale: >
    It may remain active, but absence of a companion beta-lactamase inhibitor
    creates a theoretical concern in the setting of high-level beta-lactamase
    expression.

## Explicit uncertainty / limitations

- No robust trials define optimal therapy for isolates susceptible to one
  carbapenem but resistant to another.
- Concern for on-therapy loss of carbapenem efficacy is mechanistically plausible
  rather than established through strong outcome data.
- The relative ranking of newer beta-lactam/beta-lactamase-inhibitor agents is
  supported substantially by in-vitro inhibitor activity.

## Clinical monitoring

If an active carbapenem is used:

- monitor response closely;
- reconsider mechanism or therapy if response is inadequate;
- critical illness and uncontrolled source favor moving toward newer
  beta-lactam/beta-lactamase-inhibitor therapy.

## Global table dependencies

Table_1:
  - extended-infusion meropenem
  - extended-infusion imipenem
  - newer CRE-active beta-lactam regimens

Table_2:
  - meropenem/imipenem susceptible MIC <=1 µg/mL
  - ertapenem non-susceptibility begins above its susceptible breakpoint

Supplemental_Material:
  - imipenem and meropenem administration details.

## Cross-references

- Q3.7 — tissue-oriented role and limitations of eravacycline/tigecycline.

## Candidate citations

high_priority:
  - "[266]" — phenotype/genotype surveillance study
  - "[225, 267]" — beta-lactamase amplification/porin mechanism
  - "[268]" — mechanistic rationale for newer inhibitor combinations
  - "[269, 270]" — inhibitor-activity comparisons

---

# 6. Question 3.4 — Invasive KPC-producing Enterobacterales

source_pages: 35–37

question: >
  What are the preferred antibiotics for the treatment of invasive infections
  caused by KPC-producing Enterobacterales?

## Suggested approach

preferred:
  - ceftazidime-avibactam
  - imipenem-relebactam
  - meropenem-vaborbactam

alternative:
  - aztreonam-avibactam
  - cefiderocol
  - eravacycline
  - tigecycline

tetracycline_restriction:
  - not suggested for bloodstream infection
  - not suggested for urinary tract infection

## Critical ranking nuance from the Rationale

Although the Suggested approach lists preferred options without a strict ranking,
the Rationale states a slight panel preference:

1. meropenem-vaborbactam
2. ceftazidime-avibactam
3. imipenem-relebactam

basis:
  - composite observational outcomes
  - apparent differences in treatment-emergent resistance
  - differences are generally not statistically definitive

This ranking must be preserved in final synthesis and should not be lost by
alphabetical presentation of the Suggested approach.

## Evidence architecture

- US surveillance
- observational comparative effectiveness studies
- small uncontrolled cohorts
- small clinical-trial subgroups
- resistance-mechanism studies
- comparison with historical polymyxin/aminoglycoside regimens
- no direct randomized head-to-head trial among the three preferred agents

## Load-bearing quantitative findings

in_vitro_activity:
  ceftazidime_avibactam: ">95%"
  imipenem_relebactam: ">95%"
  meropenem_vaborbactam: ">95%"
  source_citation: "[276]"

comparative_observational_study_1:
  population: CRE infections, approximately 73% KPC-E
  ceftazidime_avibactam:
    n: 105
    30_day_survival: "81% (85/105)"
    clinical_cure: "62% (65/105)"
  meropenem_vaborbactam:
    n: 26
    30_day_survival: "88% (23/26)"
    clinical_cure: "69% (18/26)"
  recurrent_infection_resistance:
    ceftazidime_avibactam: "20% (3/15)"
    meropenem_vaborbactam: "0% (0/3)"
  source_citation: "[279]"

comparative_observational_study_2:
  ceftazidime_avibactam_30_day_survival: "73% (38/52)"
  meropenem_vaborbactam_30_day_survival: "81% (29/36)"
  early_response: >
    Meropenem-vaborbactam recipients had approximately twice the odds of a
    favorable clinical response at 72 hours.
  source_citation: "[277]"

comparative_observational_study_3:
  invasive_KPC_E_n: 73
  overall_survival: "no difference reported"
  recurrent_infection_resistance:
    ceftazidime_avibactam: "12% (2/17)"
    meropenem_vaborbactam: "0% (0/7)"
  source_citation: "[278]"

imipenem_relebactam_observational:
  invasive_KPC_E_n: 6
  survival: "100%"
  clinical_cure: "100%"
  source_citation: "[280]"

imipenem_relebactam_trial_subgroup:
  imipenem_non_susceptible_Enterobacterales:
    favorable_response: "40% (2/5)"
  interpretation: >
    Sample is far too small for definitive inference but produces caution around
    assuming equivalence solely from in-vitro activity.
  source_citation: "[274]"

## Resistance emergence

ceftazidime_avibactam:
  approximate_frequency: "10%"
  common_mechanism:
    - substitutions within or adjacent to KPC omega-loop
    - less commonly AmpC alterations
  potential_phenotypic_effect:
    - enhanced ceftazidime hydrolysis
    - reduced avibactam binding
    - sometimes lower carbapenem MICs / apparent restored susceptibility
  clinical_significance_of_restored_carbapenem_susceptibility: unclear

imipenem_relebactam_and_meropenem_vaborbactam:
  reported_frequency: "<3%"
  principal_mechanism:
    - reduced outer-membrane permeability
    - e.g. ompK35/ompK36 disruption

shared_vulnerability:
  - blaKPC amplification / increased enzyme expression

## Alternative-agent evidence

aztreonam_avibactam:
  in_vitro_activity: ">95%"
  clinical_data: very limited

cefiderocol:
  in_vitro_activity: ">95%"
  KPC_E_trial_subgroup:
    cefiderocol_survival: "78% (7/9)"
    alternative_regimen_survival: "79% (11/14)"
  comparator: primarily polymyxin-based
  source_citation: "[259]"

## Explicit uncertainty / limitations

- No direct randomized comparison among preferred agents.
- Comparative evidence favoring meropenem-vaborbactam is observational.
- Several comparative studies contain very small meropenem-vaborbactam arms.
- Imipenem-relebactam clinical evidence in KPC-E is particularly sparse.
- Resistance-emergence estimates depend on selected observational cohorts and
  recurrent isolates.

## Safety / stewardship

Major source-level rationale:
  >
  Preferred newer agents have been associated with better outcomes and
  substantially less toxicity than older polymyxin- or aminoglycoside-based
  regimens.

## Global table dependencies

Table_1:
  - ceftazidime-avibactam
  - imipenem-relebactam
  - meropenem-vaborbactam
  - alternatives as applicable

Table_2:
  - agent-specific susceptibility criteria

## Cross-references

- Q3.7 — eravacycline/tigecycline restrictions.

## Candidate load-bearing citations

very_high_priority:
  - "[277]"
  - "[278]"
  - "[279]"
  - "[280]"
  - "[282-298]"

additional:
  - "[233, 271-275]" — newer agents versus older toxic regimens
  - "[276]" — US susceptibility
  - "[259]" — cefiderocol KPC subgroup

---

# 7. Question 3.5 — Invasive NDM-producing Enterobacterales

source_pages: 37–39

question: >
  What are the preferred antibiotics for the treatment of invasive infections
  caused by NDM-producing Enterobacterales?

## Suggested approach

preferred:
  - aztreonam-avibactam
  - cefiderocol

alternative_if_aztreonam_avibactam_unavailable:
  - ceftazidime-avibactam PLUS aztreonam

other_alternatives:
  - eravacycline
  - tigecycline

tetracycline_restriction:
  - only when infection does not involve bloodstream or urinary tract

## Mechanistic basis

NDM:
  class: metallo-beta-lactamase
  hydrolyzes:
    - essentially all traditional beta-lactams
  does_not_hydrolyze:
    - aztreonam

problem:
  >
  NDM-E commonly co-produce serine beta-lactamases such as ESBLs, AmpCs,
  or OXA enzymes that CAN hydrolyze aztreonam.

solution:
  >
  Avibactam inhibits the co-produced serine beta-lactamases, preserving
  aztreonam activity against its PBP3 target.

important_negative:
  >
  The preferred beta-lactam/beta-lactamase-inhibitor therapies for KPC are not
  intrinsically active against NDM because avibactam, relebactam, and
  vaborbactam do not inhibit NDM itself. Aztreonam supplies the NDM-stable
  beta-lactam component.

## Aztreonam-avibactam evidence

susceptibility_breakpoint: "<=4/4 µg/mL"
NDM_E_susceptibility: ">95%"
source_citations: "[228, 304-306]"

PK_PD_targets_supporting_dosing:
  aztreonam: ">=60% fT>MIC"
  avibactam: ">=50% fT>2.5 µg/mL"
  evidence:
    - population PK/PD modeling
    - animal model data
  source_citations: "[307-309]"

clinical_trial_subgroup_1:
  aztreonam_avibactam:
    n: 6
    clinical_cure: "33% (2/6)"
    28_day_survival: "83% (5/6)"
  meropenem:
    n: 1
    clinical_cure: "0% (0/1)"
    28_day_survival: "100% (1/1)"
  source_citation: "[302]"

clinical_trial_subgroup_2:
  aztreonam_avibactam:
    n: 9
    clinical_cure: "44% (4/9)"
    28_day_survival: "89% (8/9)"
  alternative_polymyxin_or_aminoglycoside:
    n: 2
    clinical_cure: "0% (0/2)"
    28_day_survival: "50% (1/2)"
  source_citation: "[310]"

interpretation: >
  Aztreonam-avibactam has strong mechanistic and in-vitro rationale but very
  limited direct clinical evidence, with outcome estimates based on extremely
  small NDM subgroups.

## Ceftazidime-avibactam PLUS aztreonam

status: >
  Reasonable alternative when aztreonam-avibactam is unavailable.

direct_comparison_with_aztreonam_avibactam: none

MBL_bloodstream_cohort:
  total_n: 102
  NDM_n: 82
  ceftazidime_avibactam_plus_aztreonam_30_day_survival: "81% (42/52)"
  polymyxin_or_tigecycline_regimen_survival: "56% (28/50)"
  source_citation: "[312]"

AST_issue:
  validated_MIC_method_for_combination: unavailable
  available_method:
    - CLSI-endorsed broth disk elution method

administration:
  >
  Exact administration strategy is dependent on Table 1 and Supplemental
  Material.

## Source-text verification flag

citation_313_statement:
  >
  The guidance next describes a cohort of 328 NDM-E isolates and reports
  30-day survival of 78% (167/215) with "ceftazidime-avibactam", 67%
  (22/33) with cefiderocol, and 50% (13/26) with colistin.

verification_issue:
  >
  This sentence appears inside a paragraph discussing ceftazidime-avibactam
  PLUS aztreonam, while ceftazidime-avibactam alone is not mechanistically
  expected to overcome NDM. The final SEA should verify the exact regimen
  reported in reference [313] rather than silently interpreting or correcting
  the wording.

status: HIGH-PRIORITY SELECTIVE REFERENCE AUDIT ITEM

## Hepatic safety

healthy_volunteer_ceftazidime_avibactam_plus_or_minus_aztreonam:
  asymptomatic_transaminase_elevation: "40%"
  pattern: >
    Primarily associated with aztreonam exposure of 8 g/day, either continuous
    infusion or every 6 hours.
  resolution: after drug cessation
  source_citation: "[317]"

aztreonam_avibactam_trials:
  aztreonam_total_daily_dose: "6 g/day"
  asymptomatic_transaminase_elevation: "approximately 6%"
  source_citations: "[302, 310]"

feasibility_advantage_of_fixed_aztreonam_avibactam:
  - fixed 3:1 formulation
  - synchronized beta-lactam/inhibitor exposure
  - improved probability of joint target attainment
  - single-agent administration

## Cefiderocol evidence

US_NDM_E_activity: "approximately 85%"
source_citations: "[322, 323]"

trial_subgroup_1:
  cefiderocol:
    clinical_cure: "60% (6/10)"
    28_day_survival: "90% (9/10)"
  alternative_primarily_polymyxin_based:
    clinical_cure: "20% (1/5)"
    28_day_survival: "40% (2/5)"
  source_citation: "[324]"

NDM_E_bloodstream_subgroup:
  cefiderocol_30_day_survival: "50% (8/16)"
  alternative_therapy_30_day_survival: "82% (9/11)"
  comparator: largely polymyxin-based
  source_citation: "[325]"

interpretation: >
  Clinical data are small and internally variable. The guidance does not claim
  superiority of aztreonam-avibactam over cefiderocol or vice versa and retains
  both as preferred agents.

## Dual-resistance problem in NDM-producing E. coli

mechanism:
  - four-amino-acid PBP3 insertions
    examples:
      - YRIN
      - YRIK
  - particularly when combined with CMY-type AmpC variants

effect:
  - reduced affinity for aztreonam
  - reduced affinity for ceftazidime
  - reduced affinity for cefiderocol

US_signal:
  region: mid-Atlantic
  reported_prevalence: "approximately 30% of NDM-producing E. coli isolates"
  source_citation: "[331]"

when_resistant_to_both_aztreonam_avibactam_and_cefiderocol:
  evidence: very limited
  individualized_options_mentioned:
    - IV fosfomycin
    - polymyxin B
    - tigecycline
  strategy: individualized combination regimen

additional_cefiderocol_resistance_mechanisms:
  - TonB-dependent iron-transport mutations
  - increased NDM expression
  - resistance propensity may vary by MBL family and specific NDM allele

## Explicit uncertainty / limitations

- Aztreonam-avibactam clinical evidence is dominated by very small trial subgroups.
- Cefiderocol NDM outcomes are inconsistent across small subgroup analyses.
- No direct aztreonam-avibactam versus cefiderocol comparative trial exists.
- Resistance mechanisms are evolving.
- Aztreonam-avibactam is newly introduced into clinical use, limiting real-world
  resistance experience.
- Optimal therapy for isolates resistant to both preferred options is undefined.

## Global table dependencies

Table_1:
  - aztreonam-avibactam loading/maintenance strategy
  - ceftazidime-avibactam PLUS aztreonam simultaneous administration strategy
  - cefiderocol dosing

Table_2:
  - aztreonam-avibactam <=4/4 µg/mL
  - cefiderocol susceptibility criteria
  - relevant Enterobacterales breakpoints

Supplemental_Material:
  - ceftazidime-avibactam PLUS aztreonam administration details are explicitly
    referenced.

## Cross-references

- Q3.7 — eravacycline/tigecycline role.
- Q3.8 — exceptional combination therapy when no active preferred beta-lactam exists.

## Candidate load-bearing citations

very_high_priority:
  - "[302]"
  - "[310]"
  - "[312]"
  - "[313] — regimen wording requires verification"
  - "[324]"
  - "[325]"
  - "[331]"

mechanistic_PKPD:
  - "[303]"
  - "[307-309]"
  - "[326-330]"
  - "[334-339]"

safety:
  - "[317]"

---

# 8. Question 3.6 — Invasive OXA-48-like-producing Enterobacterales

source_pages: 39–40

question: >
  What are the preferred antibiotics for invasive infections caused by CRE
  if OXA-48-like production is present?

## Suggested approach

preferred:
  - ceftazidime-avibactam

alternative:
  - aztreonam-avibactam
  - cefiderocol
  - eravacycline
  - tigecycline

tetracycline_restriction:
  - not for bloodstream infection
  - not for urinary infection

not_suggested_even_if_AST_reports_susceptibility:
  - meropenem-vaborbactam
  - imipenem-relebactam

## Mechanistic basis

- Avibactam has meaningful inhibitory activity against OXA-48-like enzymes.
- Vaborbactam and relebactam have limited inhibitory activity against OXA-48-like enzymes.
- Therefore a susceptible laboratory result for meropenem-vaborbactam or
  imipenem-relebactam does not cause the panel to endorse these agents for OXA-48-E.

## Load-bearing quantitative findings

ceftazidime_avibactam_in_vitro_activity:
  susceptible: ">95%"
  source_citations: "[340, 341]"

single_arm_cohort:
  n: 171
  clinical_cure: "79% (135/171)"
  day_30_survival: "78% (134/171)"
  source_citation: "[342]"

bloodstream_observational_study:
  ceftazidime_avibactam:
    n: 33
    clinical_success: "91% (30/33)"
    30_day_survival: "88% (29/33)"
  alternative_regimens:
    n: 43
    clinical_success: "58% (25/43)"
    30_day_survival: "74% (32/43)"
    comparator: predominantly polymyxin-based
  source_citation: "[343]"

animal_model:
  OXA48_E_isolates: 51
  finding: >
    Ceftazidime-avibactam had consistently greater in-vivo activity than
    meropenem-vaborbactam or imipenem-relebactam, regardless of MIC.
  source_citation: "[345]"

aztreonam_avibactam_and_cefiderocol:
  in_vitro_activity: ">95% of OXA-48-E isolates"
  source_citations: "[45, 299, 301]"

cefiderocol_trial_subgroup:
  n: 10
  clinical_cure: "70% (7/10)"
  day_28_survival: "100% (10/10)"
  source_citation: "[350]"

aztreonam_avibactam_clinical_outcomes:
  status: not available

## Treatment-emergent resistance

clinical_reports:
  status: exceedingly sparse

in_vitro_selected_mechanisms:
  - altered efflux
  - porin modification or loss
  - PBP3 structural changes
  - substitutions within OXA-48-like beta-lactamases

clinical_significance: unknown

## Evidence architecture

- in-vitro surveillance
- observational cohorts
- animal infection model
- very small clinical-trial subgroup
- mechanistic resistance studies
- no randomized direct comparative trial

## Explicit uncertainty / limitations

- Ceftazidime-avibactam recommendation rests largely on in-vitro and
  observational evidence.
- Comparator regimens in observational studies are often older polymyxin-based
  therapy.
- Aztreonam-avibactam lacks direct clinical outcomes evidence for OXA-48-E.
- Cefiderocol evidence consists of very small subgroups.
- Clinical incidence and importance of treatment-emergent resistance are uncertain.

## Global table dependencies

Table_1:
  - ceftazidime-avibactam
  - aztreonam-avibactam
  - cefiderocol
  - tetracycline derivatives

Table_2:
  - susceptibility criteria
  - important reminder that mechanistic appropriateness can supersede a seemingly
    favorable AST result for meropenem-vaborbactam or imipenem-relebactam.

## Cross-references

- Q3.7 — tetracycline derivative restrictions.

## Candidate citations

very_high_priority:
  - "[342]"
  - "[343]"
  - "[345]"
  - "[350]"

additional:
  - "[340, 341]"
  - "[344-349]"

---

# 9. Question 3.7 — Tetracycline derivatives

source_pages: 40–41

question: >
  What is the role of tetracycline derivatives for the treatment of infections
  caused by CRE?

## Suggested approach

preferred_status:
  - beta-lactam agents remain preferred for invasive CRE.

alternative_when_active_beta_lactam_unavailable_or_not_tolerated:
  - eravacycline
  - tigecycline

not_suggested:
  - CRE bloodstream infection
  - CRE urinary tract infection

potentially_reasonable_sites:
  - intra-abdominal infection
  - skin and soft tissue infection
  - osteomyelitis
  - pneumonia

## Pharmacologic rationale

Tetracycline derivatives:

- retain activity independent of carbapenemase production;
- distribute rapidly into tissues;
- achieve low serum concentrations;
- achieve low urinary concentrations.

The same distribution profile that may favor tissue infections limits reliability
for bacteremia and UTI.

## Evidence architecture

- PK/PD
- in-vitro susceptibility
- observational outcome studies
- extremely limited CRE-specific eravacycline clinical trial data
- post-marketing experience
- toxicity comparisons

## Load-bearing findings

tigecycline:
  evidence_volume: substantially greater than eravacycline
  MIC_signal:
    threshold_associated_with_poor_outcomes: ">=0.5 µg/mL"
    FDA_susceptible_breakpoint: "<=2 µg/mL"
    implication: >
      An isolate may fall within the FDA susceptible range while an MIC at or
      above 0.5 µg/mL is nevertheless associated with worse reported outcomes.
  source_citations: "[265, 356, 357]"

breakpoint_issue:
  CLSI_tigecycline_breakpoint: not established
  CLSI_eravacycline_breakpoint: not established

eravacycline:
  CRE_cases_across_clinical_trials: "<5"
  post_marketing_data: sparse
  source_citations: "[358-360]"

GI_tolerability:
  tigecycline_nausea: "approximately 20%–25%"
  eravacycline_nausea: "approximately 5%"
  source_citation: "[361]"

minocycline:
  CRE_clinical_data: limited
  susceptibility: lower than tigecycline or eravacycline

omadacycline:
  in_vitro_activity: greater than minocycline
  CRE_clinical_outcome_data: absent

panel_position:
  - caution with minocycline
  - caution with omadacycline

## Explicit uncertainty / limitations

- Tigecycline evidence is mostly nonrandomized.
- Direct comparisons with newer CRE-active beta-lactams are limited.
- Eravacycline has almost no CRE-specific trial population.
- Standard "susceptible" classification may inadequately reflect tigecycline
  outcome risk at MICs >=0.5 µg/mL.
- No CLSI breakpoint exists for tigecycline or eravacycline.

## Safety

- Tigecycline causes substantially more nausea than eravacycline.
- Low serum/urinary exposure is a pharmacologic limitation rather than simply a
  lack of clinical-trial evidence.

## Global table dependencies

Table_1:
  - high-exposure tigecycline regimen
  - eravacycline regimen

Table_2:
  - FDA rather than CLSI tigecycline criterion is represented in the global
    breakpoint table.
  - no CLSI tigecycline or eravacycline breakpoint.

## Candidate citations

high_priority:
  - "[264, 265]"
  - "[352-357]"
  - "[358-361]"

secondary:
  - "[351]"
  - "[362-366]"

---

# 10. Question 3.8 — Combination therapy

source_pages: 41–42

question: >
  What is the role of combination antibiotic therapy for the treatment of
  infections caused by CRE?

## Suggested approach

routine_combination_therapy: NOT SUGGESTED

definition_in_guidance:
  >
  A beta-lactam combined with an aminoglycoside, fluoroquinolone,
  IV fosfomycin, tetracycline, or polymyxin.

## Core distinction

empiric_phase:
  >
  Combination therapy may increase the probability that at least one active
  agent is present in a patient at risk for CRE infection.

definitive_phase:
  >
  Once a beta-lactam with confirmed in-vitro activity has been identified,
  available evidence does not support routine continuation of a second agent.

reasons:
  - no demonstrated improvement in clinical outcomes
  - increased antibiotic-associated adverse events
  - no clinical evidence that continued combination therapy prevents emergence
    of resistance

## Evidence architecture

- no randomized monotherapy-versus-combination trials with newer beta-lactams
- observational comparative studies
- heterogeneous observational IV fosfomycin literature
- toxicity rationale
- expert consensus

## Load-bearing quantitative finding

largest_observational_combination_study:
  population: KPC-E
  total_n: 577

  ceftazidime_avibactam_monotherapy:
    n: 165
    30_day_survival: "approximately 74% (122/165)"

  ceftazidime_avibactam_plus_second_agent:
    n: 412
    30_day_survival: "approximately 75% (309/412)"

  interpretation: >
    No apparent survival advantage from routine combination therapy.

  source_citation: "[369]"

## Exceptional scenario

IV_fosfomycin_combination_may_be_considered_when:
  - carbapenem-resistant E. coli
  - no active beta-lactam exists
  - example:
      NDM-producing E. coli with PBP3 insertion + CMY production
      resistant to BOTH:
        - aztreonam-avibactam
        - cefiderocol

if_used:
  - IV fosfomycin should be combined with another active agent
    examples:
      - tigecycline
      - polymyxin B

evidence_strength_for_exception:
  - limited
  - heterogeneous observational experience
  - individualized salvage decision rather than routine strategy

## Explicit uncertainty / limitations

- No trial has directly randomized a newer active beta-lactam alone versus the
  same beta-lactam plus a second active agent.
- Evidence against routine combination therapy is largely observational.
- Evidence that combination therapy prevents resistance emergence is absent.
- IV fosfomycin combination literature is highly heterogeneous.

## Safety / stewardship

- Continuing unnecessary second agents increases toxicity without demonstrated
  benefit.
- The section supports de-escalation to a single confirmed active beta-lactam
  once susceptibility is known.
- Combination therapy is retained as a salvage concept rather than a default
  definitive-treatment strategy.

## Cross-references

- Q3.5 — dual aztreonam-avibactam/cefiderocol resistance in NDM-producing E. coli.

## Candidate citations

very_high_priority:
  - "[369]"

additional:
  - "[342, 368]"
  - "[367]"
  - "[370-373]" — IV fosfomycin combination evidence

---

# 11. Cross-cutting evidence architecture

## 11.1 Evidence maturity is highly heterogeneous

Q3.1_CRE_uUTI:
  dominant_evidence:
    - surveillance susceptibility
    - urinary PK
    - extrapolation from general uUTI studies
  major_gap:
    - limited direct CRE-specific clinical outcome evidence

Q3.2_CRE_cUTI:
  dominant_evidence:
    - broader UTI clinical trials
    - AST
    - PK
  major_gap:
    - low CRE representation in many trials

Q3.3_non_carbapenemase_CRE:
  dominant_evidence:
    - microbiology
    - mechanism
    - surveillance
    - PK/PD
  major_gap:
    - limited comparative clinical outcomes

Q3.4_KPC:
  dominant_evidence:
    - observational comparative effectiveness
    - surveillance
    - resistance-emergence studies
  relative_strength_within_CRE_section:
    - comparatively mature clinical evidence
  major_gap:
    - no direct randomized comparison of preferred newer agents

Q3.5_NDM:
  dominant_evidence:
    - mechanistic rationale
    - PK/PD
    - surveillance
    - small trial subgroups
    - observational cohorts
  major_gap:
    - very small direct clinical datasets
    - no aztreonam-avibactam versus cefiderocol comparison

Q3.6_OXA48:
  dominant_evidence:
    - in-vitro data
    - observational cohorts
    - animal models
  major_gap:
    - no randomized comparative evidence

Q3.7_tetracyclines:
  dominant_evidence:
    - pharmacology
    - observational data
    - susceptibility studies
  major_gap:
    - extremely sparse eravacycline CRE trial evidence

Q3.8_combination:
  dominant_evidence:
    - observational comparative data
    - toxicity rationale
  major_gap:
    - no novel-beta-lactam monotherapy-versus-combination RCT

---

# 12. Cross-cutting pharmacotherapy principles

## 12.1 Infection site is a major pharmacologic filter

Urinary infection:
- favors urinary exposure and oral/renal-eliminated agents when active.

Bloodstream infection:
- requires reliable systemic exposure.
- argues against tetracycline derivatives.

Tissue infection:
- may permit eravacycline/tigecycline where beta-lactams cannot be used.

## 12.2 Carbapenemase mechanism is a treatment-selection variable

KPC:
  preferred_beta_lactamase_inhibitors:
    - vaborbactam
    - avibactam
    - relebactam

NDM:
  core_problem:
    - traditional beta-lactamase inhibitors do not inhibit NDM
  strategy:
    - use NDM-stable aztreonam protected from co-produced serine enzymes
    - OR cefiderocol

OXA_48_like:
  preferred_inhibitor:
    - avibactam
  avoid_relying_on:
    - vaborbactam
    - relebactam

## 12.3 AST must be interpreted in biological context

Examples:

- colistin has no CLSI susceptible category for Enterobacterales.
- oral and IV fosfomycin use different criteria.
- tigecycline may be FDA-susceptible while MIC >=0.5 µg/mL is associated with
  poor CRE outcomes.
- meropenem-vaborbactam or imipenem-relebactam may test susceptible against
  OXA-48-E yet are still not suggested by the panel.
- no validated MIC method exists for ceftazidime-avibactam PLUS aztreonam;
  broth disk elution is used instead.
- carbapenem MIC phenotype plus carbapenemase testing determines whether an
  older carbapenem remains appropriate.

## 12.4 Resistance emergence is treatment-specific

Highest explicit signal:
  - ceftazidime-avibactam in KPC-E: approximately 10%

Lower reported signal:
  - meropenem-vaborbactam: <3%
  - imipenem-relebactam: <3%

NDM-specific emerging problem:
  - PBP3 insertion + CMY variants may compromise BOTH aztreonam-avibactam
    and cefiderocol.

OXA48:
  - clinical treatment-emergent resistance reports remain sparse.

---

# 13. Cross-cutting safety signals

major_signals:

colistin:
  - nephrotoxicity approximately 30%
  - limits role even for uUTI

aminoglycosides:
  - duration-dependent nephrotoxicity
  - single-dose/short-course use more attractive than prolonged exposure

aztreonam_containing_regimens:
  - transaminase elevations
  - strongly exposure-dependent signal in healthy-volunteer data
  - approximately 40% with high aztreonam exposure in one study
  - approximately 6% in aztreonam-avibactam trials using 6 g/day aztreonam

tigecycline:
  - nausea approximately 20%–25%

eravacycline:
  - nausea approximately 5%

combination_therapy:
  - unnecessary second agents increase adverse-event burden without established
    improvement in definitive-treatment outcomes

---

# 14. Stewardship and implementation principles

1. Do not automatically escalate every CRE uUTI to a novel IV agent.
2. Use prior cultures and patient-level susceptibility history.
3. For cUTI or invasive disease, determine the carbapenemase mechanism whenever
   possible.
4. Preserve active oral therapy when clinically appropriate.
5. Treat KPC, NDM, and OXA-48-like CRE as distinct therapeutic entities.
6. Do not infer drug preference from alphabetical ordering of Suggested approaches;
   read the Rationale.
7. For KPC, the Rationale subtly favors meropenem-vaborbactam over
   ceftazidime-avibactam and imipenem-relebactam.
8. Monitor for treatment-emergent resistance, especially with
   ceftazidime-avibactam in KPC-E.
9. Avoid tetracycline derivatives for bacteremia and UTI because of exposure
   limitations.
10. Once an active beta-lactam is identified, do not routinely continue an
    aminoglycoside, polymyxin, tetracycline, fluoroquinolone, or IV fosfomycin
    solely for "combination coverage."
11. Reserve salvage combination therapy for exceptional organisms without an
    active preferred beta-lactam.

---

# 15. Global Table 1 dependencies for final reconciliation

CRE-relevant drug entries requiring preservation in the final SEA include:

urinary_agents:
  - amikacin
  - gentamicin
  - plazomicin
  - tobramycin
  - ciprofloxacin
  - levofloxacin
  - nitrofurantoin
  - TMP-SMX
  - fosfomycin
  - pivmecillinam

newer_CRE_active_agents:
  - aztreonam-avibactam
  - cefiderocol
  - ceftazidime-avibactam
  - ceftazidime-avibactam PLUS aztreonam
  - imipenem-relebactam
  - meropenem-vaborbactam

carbapenems:
  - imipenem
  - meropenem

tetracycline_derivatives:
  - eravacycline
  - tigecycline

important_dosing_features_to_reconcile:
  - extended-infusion carbapenems
  - PK-guided aminoglycoside dosing
  - aztreonam-avibactam loading + maintenance exposure
  - simultaneous administration strategy for ceftazidime-avibactam + aztreonam
  - high-exposure tigecycline regimen

Do not duplicate all Table 1 cells here; merge the exact global dosing table into
the final SEA.

---

# 16. Global Table 2 dependencies for final reconciliation

High-value CRE breakpoint/AST items:

- ertapenem
- imipenem
- meropenem
- aztreonam-avibactam
- cefiderocol
- ceftazidime-avibactam
- imipenem-relebactam
- meropenem-vaborbactam
- fluoroquinolones
- aminoglycosides
- TMP-SMX
- nitrofurantoin
- fosfomycin IV
- fosfomycin oral
- pivmecillinam
- colistin/polymyxin B
- tigecycline

critical_interpretive_points:
  - colistin/polymyxin B: no susceptible category
  - oral fosfomycin: E. coli urinary isolates only
  - IV fosfomycin and oral fosfomycin criteria are not interchangeable
  - tigecycline CLSI breakpoint absent; FDA criterion used in global table
  - combination ceftazidime-avibactam + aztreonam lacks a validated conventional
    MIC method
  - biological carbapenemase mechanism sometimes materially changes the
    interpretation of nominal AST susceptibility

---

# 17. Supplemental Material dependencies

explicit_or_material_dependencies:

aminoglycosides:
  - PK-guided dosing information

imipenem_meropenem:
  - administration/dosing details linked from global Table 1

ceftazidime_avibactam_plus_aztreonam:
  - administration strategy specifically referenced to Supplemental Material

coverage_status:
  - Supplemental Material has not been independently evaluated in this SEA run.

final_SEA_requirement:
  >
  Preserve this as a completeness limitation unless Supplemental Material is
  separately obtained and reviewed.

---

# 18. Provisional appraisal flags
## NOT final scores or verdicts

### A. Mechanism-directed precision is a major strength

The section generally avoids treating CRE as a single antibiogram phenotype and
instead links treatment to:

- carbapenemase presence;
- carbapenemase family;
- carbapenem MIC pattern;
- infection site;
- tissue/serum/urine pharmacology.

### B. Recommendation confidence varies dramatically by question

Some treatment choices are supported primarily by:

- PK/PD,
- surveillance,
- mechanistic reasoning,
- animal studies,
- or tiny clinical subgroups,

while others, particularly KPC therapy, have a larger observational clinical
evidence base.

The final SEA should therefore avoid assigning one uniform "evidence strength"
to the entire CRE section.

### C. KPC evidence is comparatively mature but not randomized head-to-head

The rationale's preference for meropenem-vaborbactam over other preferred KPC
agents is clinically meaningful but appears to rest mainly on nonrandomized
comparisons and resistance-emergence observations.

### D. NDM is an important uncertainty concentration

Aztreonam-avibactam has:

- excellent mechanistic rationale,
- >95% in-vitro activity,
- explicit PK/PD target support,

but very small direct clinical datasets.

Cefiderocol clinical subgroup findings are directionally inconsistent.

### E. OXA-48 recommendation illustrates limits of antibiogram-only reasoning

The panel advises against meropenem-vaborbactam and imipenem-relebactam even
when apparent in-vitro susceptibility is reported because their inhibitors have
weak OXA-48-like activity and animal-model efficacy is inferior.

### F. Tigecycline breakpoint discordance is clinically important

A reported FDA-susceptible MIC does not necessarily imply good CRE outcomes:
MIC >=0.5 µg/mL is associated with worse outcomes even though the FDA
susceptible threshold is <=2 µg/mL.

### G. Combination therapy is a de-escalation message, not an absolute prohibition

The guidance distinguishes:

- empiric combination coverage while activity is unknown
FROM
- continuing combination therapy after a reliable active beta-lactam is known.

Exceptional salvage combinations remain possible.

### H. Resistance emergence should appear prominently in final appraisal

Particularly:

- ceftazidime-avibactam resistance during KPC therapy;
- PBP3/CMY-mediated dual resistance in NDM-producing E. coli;
- evolving cefiderocol resistance mechanisms.

### I. Reference [313] requires direct verification

The wording of the 328-NDM-E cohort is potentially ambiguous in context.
Do not silently resolve it during final synthesis.

---

# 19. Selective reference-audit queue

PRIORITY 1 — likely to materially alter final appraisal:
  - "[266]" — non-carbapenemase phenotype characterization
  - "[277]" — ceftazidime-avibactam vs meropenem-vaborbactam
  - "[278]" — recurrent infection/resistance comparison
  - "[279]" — survival/cure/resistance comparison
  - "[280]" — imipenem-relebactam KPC cohort
  - "[282-298]" — KPC treatment-emergent resistance
  - "[302]" — aztreonam-avibactam NDM subgroup
  - "[310]" — aztreonam-avibactam NDM subgroup
  - "[312]" — ceftazidime-avibactam + aztreonam MBL bloodstream cohort
  - "[313]" — NDM cohort; exact regimen wording requires verification
  - "[324]" — cefiderocol NDM subgroup
  - "[325]" — cefiderocol NDM bloodstream subgroup
  - "[331]" — US NDM E. coli PBP3 insertion signal
  - "[342]" — OXA-48 ceftazidime-avibactam cohort
  - "[343]" — OXA-48 bloodstream comparative cohort
  - "[345]" — OXA-48 animal-model comparison
  - "[350]" — cefiderocol OXA-48 subgroup
  - "[356, 357]" — tigecycline MIC/outcome relationship
  - "[369]" — KPC monotherapy versus combination observational study

PRIORITY 2 — important pharmacology/susceptibility context:
  - "[238]"
  - "[251]"
  - "[253-255]"
  - "[269, 270]"
  - "[276]"
  - "[299-301]"
  - "[304-309]"
  - "[317]"
  - "[322, 323]"
  - "[326-330]"
  - "[334-339]"
  - "[340, 341]"
  - "[344-349]"
  - "[358-361]"
  - "[370-373]"

---

# 20. Final hierarchical handoff

## Preserve in final SEA

core_decision_points:
  - infection site
  - CRE carbapenemase status
  - carbapenemase family
  - carbapenem MIC phenotype
  - AST
  - patient clinical stability
  - source control
  - serum/urinary/tissue drug exposure
  - toxicity
  - treatment-emergent resistance

core_therapeutic_message: >
  CRE treatment is increasingly mechanism-directed. Traditional or narrower
  agents remain appropriate in selected urinary or non-carbapenemase phenotypes,
  while invasive carbapenemase-producing CRE generally require newer agents
  selected according to KPC, NDM, or OXA-48-like biology.

core_evidence_message: >
  The pharmacologic and mechanistic architecture is strong and internally
  coherent, but direct clinical evidence is uneven. Many recommendations rely
  on surveillance, PK/PD, observational cohorts, small trial subgroups, or
  animal/in-vitro evidence rather than definitive randomized comparative trials.

core_safety_message: >
  Selection should account for nephrotoxicity from polymyxins/aminoglycosides,
  hepatic enzyme elevations with high aztreonam exposure, gastrointestinal
  intolerance with tetracycline derivatives, and unnecessary toxicity from
  continued combination therapy.

core_resistance_message: >
  Emerging resistance can materially alter treatment, particularly KPC variants
  during ceftazidime-avibactam therapy and PBP3/CMY mechanisms compromising both
  aztreonam-avibactam and cefiderocol in NDM-producing E. coli.

do_not_overclaim:
  - superiority of one preferred KPC agent based on current observational data
  - superiority of aztreonam-avibactam versus cefiderocol for NDM-E
  - reliability of novel oral agents for CRE uUTI without direct outcome data
  - benefit of routine definitive combination therapy
  - efficacy inferred solely from nominal AST when mechanism or PK conflicts

remaining_dependencies_before_final_appraisal:
  - merge with global Pass 0 packet
  - reconcile exact Table 1 doses
  - reconcile Table 2 breakpoints
  - review Supplemental Material if obtainable
  - selectively inspect load-bearing primary references
  - resolve reference [313] regimen wording
  - integrate five other organism deep-pass artifacts
  - complete disclosure review
  - only then assign final SEA scores and verdict

DEEP_PASS_STATUS: COMPLETE
FINAL_SCORING_ALLOWED: NO