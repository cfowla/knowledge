# CIAG481 — HIERARCHICAL SEA DEEP-PASS ARTIFACT
## Section 6 — *Stenotrophomonas maltophilia*

---

## 0. Artifact status

artifact_type: SEA hierarchical intermediate artifact
stage: section-level deep pass
parent_artifact: CIAG481 — SEA PASS 0 GLOBAL CONTEXT PACKET
source_file: ciag481.pdf
source_title: >
  Infectious Diseases Society of America 2026 Guidance on the Treatment
  of Antimicrobial-Resistant Gram-Negative Infections
doi: 10.1093/cid/ciag481
issuing_body: Infectious Diseases Society of America
publication_year: 2026
evidence_current_as_of: 2026-03-01

section: >
  SECTION 6: Stenotrophomonas maltophilia

primary_page_scope: 60–66
clinical_questions: 6

boundary_handling:
  page_60: >
    Include only text beginning with the Section 6 S. maltophilia material;
    preceding page-60 CRAB carryover belongs to Section 5 and is excluded.
  page_66: >
    Includes completion of Question 6.6.
  page_67: >
    Global Conclusions and governance material are outside this section-level
    artifact and remain assigned to the Pass 0/global synthesis packet.

source_methodology_inherited_from_Pass_0:
  - Expert-panel treatment guidance.
  - Comprehensive but not necessarily systematic literature review.
  - Clinical expertise and panel consensus contribute to recommendations.
  - GRADE methodology not used.
  - Formal recommendation-strength and evidence-certainty labels not provided.

final_SEA_scores: WITHHELD
final_verdict: WITHHELD

reason_scores_withheld: >
  This artifact supplies section-level extraction and appraisal flags for a
  later hierarchical synthesis. Final ratings should be assigned only after
  all six organism sections, global tables, methodological context, and
  cross-section evidence have been reconciled.

grounding_boundary: >
  Numerical results and study descriptions below are findings as reported by
  the IDSA guidance. The cited primary studies were not independently retrieved
  or critically appraised during this pass. Bracketed reference numbers are
  the citation numbers used by the source document.

---

# 1. Coverage manifest

SOURCE COVERAGE MANIFEST

source_id: DOI 10.1093/cid/ciag481

section_scope:
  - Section 6 introductory clinical/microbiologic frame
  - Question 6.1 — cefiderocol
  - Question 6.2 — aztreonam-avibactam
  - Question 6.3 — levofloxacin
  - Question 6.4 — minocycline
  - Question 6.5 — TMP-SMX
  - Question 6.6 — ceftazidime

figures_within_section: 0

tables_within_pages_60_66: 0

global_table_dependencies:
  - Table 1 — adult antimicrobial dosing
  - Table 2 — susceptibility breakpoints

formal_algorithms_or_workflows: 0

implicit_clinical_workflow:
  1. Determine whether S. maltophilia represents true invasive infection.
  2. Establish available and interpretable susceptibility data.
  3. Select an active regimen while accounting for major AST limitations.
  4. Cefiderocol monotherapy is the panel's preferred initial option.
  5. Several alternative agents are suggested initially as components of
     combination therapy.
  6. Consider monotherapy step-down for selected alternatives only after
     clear and sustained clinical improvement and, where specified,
     confirmation of susceptibility.
  7. Avoid ceftazidime.

supplement_dependencies:
  - Ceftazidime-avibactam plus aztreonam administration details.
  - TMP-SMX additional dosing information.

coverage_status: COMPLETE for Section 6 main-text content
primary_study_verification_status: NOT PERFORMED
supplemental_material_review_status: NOT PERFORMED

---

# 2. Section-level clinical question / PICO frame

population: >
  Patients with invasive Stenotrophomonas maltophilia infection.

important_population_boundary: >
  The guidance specifically limits this section's therapeutic recommendations
  to invasive infection. Isolation of S. maltophilia alone does not establish
  the need for treatment.

interventions:
  - cefiderocol
  - aztreonam-avibactam
  - ceftazidime-avibactam plus aztreonam
  - levofloxacin
  - minocycline
  - trimethoprim-sulfamethoxazole
  - ceftazidime

comparators:
  - other active anti-S. maltophilia agents
  - monotherapy versus combination therapy
  - placebo or untreated controls in selected animal studies
  - alternative therapy in small clinical-trial subgroups
  - often no standardized comparator in observational evidence

outcomes_considered:
  - clinical survival
  - microbiologic eradication / bacterial burden
  - PK/PD target attainment
  - bacterial stasis
  - ≥1-log bacterial reduction
  - in-vitro susceptibility
  - treatment-emergent resistance
  - toxicity
  - feasibility of IV-to-oral transition
  - ability to interpret AST

central_clinical_problem: >
  Treatment selection is occurring in a setting where diagnosis of true
  infection can be difficult, resistance mechanisms are numerous, AST itself
  has important limitations, direct comparative clinical trials are largely
  absent, and the value of combination therapy remains uncertain.

---

# 3. Organism and disease frame

## 3.1 Organism characteristics

S. maltophilia is described as:

- an aerobic gram-negative bacillus;
- a glucose non-fermenter;
- ubiquitous in water environments;
- capable of producing biofilm and other virulence factors.

Colonization or infection is especially associated with vulnerable hosts,
including patients with:

- prolonged hospitalization;
- extensive prior antibiotic exposure;
- particularly substantial carbapenem exposure.

The guidance reports accumulating evidence that early initiation of an
antimicrobial regimen active against S. maltophilia is important in invasive
infection [575–581].

## 3.2 Colonization-versus-infection problem

This is a major interpretive problem rather than a minor diagnostic caveat.

Particularly difficult populations include:

- patients with cystic fibrosis;
- ventilator-dependent patients;
- other patients with chronic pulmonary disease or frequent respiratory
  cultures.

Additional complexity arises because S. maltophilia is frequently isolated as
part of polymicrobial infection [582].

Consequences for later evidence appraisal:

1. Respiratory isolation does not reliably establish attributable disease.
2. Observational treatment cohorts are vulnerable to infection/colonization
   misclassification.
3. Apparent outcomes after S. maltophilia therapy may partly reflect treatment
   of co-pathogens.
4. Comparisons among antibiotic regimens may be confounded before drug efficacy
   itself is considered.

## 3.3 High-consequence invasive disease

Despite its frequent role as a colonizer, S. maltophilia can produce severe
invasive disease.

The guidance particularly emphasizes:

- bacteremia;
- hemorrhagic pneumonia;
- severe disease in patients with hematologic malignancies [583–587].

Therefore, the section simultaneously warns against unnecessary treatment of
colonization and against dismissing S. maltophilia when the clinical syndrome
supports invasive disease.

---

# 4. Resistance architecture

## 4.1 Intrinsic beta-lactam resistance

Two intrinsic beta-lactamases are central to therapeutic reasoning:

L1:
  type: metallo-beta-lactamase
  consequence: >
    Hydrolyzes essentially all conventional beta-lactams except aztreonam.

L2:
  type: cephalosporinase
  consequence: >
    Hydrolyzes aztreonam and other beta-lactams.

Combined consequence:
  - Most conventional beta-lactams are intrinsically unreliable.
  - Aztreonam alone is not protected from L2.
  - Avibactam inhibition of L2 provides the mechanistic basis for
    aztreonam-avibactam.
  - The intrinsic L1/L2 system provides the principal rationale against
    ceftazidime monotherapy.

## 4.2 Aminoglycoside resistance

Chromosomal aminoglycoside acetyltransferases contribute to intrinsic
aminoglycoside resistance [590].

## 4.3 Adaptive/acquired resistance

Important additional mechanisms include:

Sme multidrug efflux pumps:
  affected_agents:
    - TMP-SMX
    - tetracyclines
    - fluoroquinolones
  consequence: increased MICs

Smqnr:
  affected_agents:
    - fluoroquinolones
  consequence: reduced fluoroquinolone activity

additional_agent_specific_mechanisms:
  cefiderocol:
    - mutations affecting iron transport, including tonB
  TMP-SMX:
    - acquired sul genes
    - acquired dfrA genes
  aztreonam-avibactam:
    - L1/L2 overexpression
    - Sme efflux upregulation
  minocycline:
    - Sme efflux overexpression

---

# 5. Antimicrobial susceptibility testing problem

AST is itself a major weakness in the evidence-to-treatment chain.

CLSI has established S. maltophilia breakpoints for six agents:

1. cefiderocol
2. chloramphenicol
3. levofloxacin
4. minocycline
5. ticarcillin-clavulanate
6. TMP-SMX

Practical reduction of this list:

- ticarcillin-clavulanate manufacturing has been discontinued;
- chloramphenicol is rarely used in the United States because of toxicity.

This leaves four routinely interpretable agents emphasized by the guidance:

- cefiderocol
- levofloxacin
- minocycline
- TMP-SMX

Confidence in AST remains limited because of:

- reproducibility concerns with commonly used susceptibility methods [594,595];
- limited PK/PD data supporting several breakpoints;
- inadequate data linking MIC values directly to clinical outcomes.

### Relevant 2026 Table 2 breakpoints

| Agent | S. maltophilia susceptible breakpoint |
|---|---:|
| Cefiderocol | ≤1 µg/mL |
| Levofloxacin | ≤2 µg/mL |
| Minocycline | ≤1 µg/mL |
| TMP-SMX | ≤2/38 µg/mL |
| Aztreonam-avibactam | No CLSI/FDA S. maltophilia breakpoint |
| Ceftazidime | No current CLSI/FDA S. maltophilia breakpoint |

critical_interpretive_rule: >
  The >90% frequency of aztreonam-avibactam MICs ≤4/4 µg/mL must not be
  rewritten as ">90% susceptible." The 4/4 µg/mL threshold is an
  Enterobacterales susceptibility breakpoint used by the authors as contextual
  information; it is not a validated S. maltophilia breakpoint.

---

# 6. Treatment hierarchy reconstructed from the section

| Therapy | Source-designated role | Initial monotherapy? | Main reason |
|---|---|---|---|
| Cefiderocol | **Preferred** | **Yes** | Very high in-vitro activity + consistent bactericidal animal-model activity |
| Aztreonam-avibactam | Alternative | Prefer combination | Mechanistically attractive but sparse clinical and incomplete PK/PD evidence |
| Ceftazidime-avibactam + aztreonam | Alternative when aztreonam-avibactam unavailable | Combination by definition | Similar mechanistic activity; greater administration complexity |
| Levofloxacin | Alternative | No; component of combination | Resistance emergence + weak bactericidal PK/PD support |
| Minocycline | Alternative | No; component of combination | Favorable tetracycline PK/PD but limited clinical data and serum-exposure concerns |
| TMP-SMX | Alternative | No; component of combination | Historical activity but primarily bacteriostatic PK/PD and weak comparative evidence |
| Ceftazidime | **Not suggested** | No | Intrinsic L1/L2 beta-lactamases and absent current breakpoints |

Additional tetracycline hierarchy:

- Minocycline is favored over tigecycline when a tetracycline derivative is
  chosen.
- Eravacycline and omadacycline are not suggested because available data are
  sparse or unfavorable.

Important interpretation:
The section does **not** demonstrate that combination therapy is clinically
superior to monotherapy for levofloxacin, minocycline, or TMP-SMX. The panel's
combination-therapy approach should therefore be preserved as a recommendation
made under evidentiary uncertainty, rather than converted into a proven
comparative-effectiveness finding.

---

# 7. Question 6.1 — Cefiderocol

## Clinical question

**What is the role of cefiderocol for the treatment of invasive
S. maltophilia infections?**

## Suggested approach

**Cefiderocol monotherapy is the preferred treatment for invasive
S. maltophilia infection.**

Critical qualification explicitly supplied by the panel:

> The preference is largely based on evidence from neutropenic animal infection
> models rather than clinical-outcomes studies.

## Evidence architecture

evidence_types:
  - U.S./international susceptibility surveillance
  - resistance-mechanism studies
  - PK/PD modeling
  - neutropenic murine infection models
  - neutropenic rabbit pneumonia model
  - observational clinical cohorts
  - meta-analysis of alternative therapies
  - extremely small clinical-trial subgroup analyses
  - expert-panel synthesis

direct_comparative_human_evidence: very limited

## In-vitro activity / resistance

- Susceptibility approaches **100%** in surveillance studies, including isolates
  resistant to other commonly used agents [45,322,596–599].
- Cefiderocol resistance, described as MIC ≥2 µg/mL in this discussion,
  remains uncommon [403,599,600].
- Mutations in iron-transport machinery, including **tonB**, are an important
  mechanism associated with increased cefiderocol MICs [599].

## PK/PD and animal evidence

Multiple neutropenic thigh and pulmonary infection models demonstrate:

- potent cefiderocol activity;
- concordance between in-vitro susceptibility and in-vivo efficacy;
- activity using human-simulated exposures [535,601–603].

Modeling suggests:

- **>90% probability** of attaining PK/PD exposures associated with
  bactericidal activity in animal models [604].

### Load-bearing animal comparison

Neutropenic rabbit pneumonia model [603]:

| Outcome | Cefiderocol | TMP-SMX | Untreated |
|---|---:|---:|---:|
| Survival | 88% (7/8) | 25% (2/8) | 0% |
| Lung microbiology | Eradication reported | Residual bacterial burden | — |

This is one of the strongest quantitative findings in the section but remains
preclinical evidence.

## Human clinical evidence

Observational cohorts:

- survival approximately **70%** [403,605–607];
- heterogeneous populations and lack of direct comparisons prevent confident
  attribution of outcomes to cefiderocol.

Meta-analysis of alternative agents:

- 14 studies;
- 663 patients;
- alternative agents included TMP-SMX and fluoroquinolones;
- survival likewise approximately **70%** [608].

Thus, the approximately 70% observational survival associated with cefiderocol
does not itself demonstrate superiority.

### Clinical-trial subgroup signals

Trial subgroup 1 [259]:

- cefiderocol-treated S. maltophilia patients: n=5;
- survivors: 1/5 (**20%**).

Trial subgroup 2 [325]:

- cefiderocol: 3/5 (**60%**) 30-day survival;
- alternative levofloxacin-based therapy: 3/3 (**100%**) 30-day survival.

These samples are far too small for meaningful comparative inference.

## Panel synthesis

Despite:

- sparse clinical data;
- lack of adequately powered direct comparison;
- small trial subgroups that are not clearly favorable to cefiderocol;

the panel designates cefiderocol as preferred because of:

1. near-universal expected in-vitro activity;
2. consistent bactericidal activity across animal models;
3. favorable modeled target attainment.

There are **insufficient data** to establish that adding a second agent to
cefiderocol improves clinical outcomes.

## Adult dosing dependency — Table 1

standard_normal_renal_hepatic_function:
  dose: 2 g IV every 8 hours
  infusion: 3 hours

augmented_clearance:
  criterion: CrCl ≥120 mL/min
  dose: 2 g IV every 6 hours
  infusion: 3 hours

## Breakpoint dependency — Table 2

cefiderocol_S_maltophilia_susceptible: ≤1 µg/mL

## Safety / implementation

section_specific_safety_signal: >
  No cefiderocol-specific toxicity is used as a major determinant of the
  Q6.1 recommendation in this section.

implementation_constraints:
  - Confirm that isolation represents invasive infection.
  - Require interpretable susceptibility where available.
  - Adjust dosing for renal function; Pass 0 dosing assumes normal function
    except for the augmented-clearance instruction.
  - Recognize that "preferred" does not imply high-certainty human comparative
    efficacy.

## Explicit evidence limitations

- Preferred therapy is supported principally by preclinical evidence.
- Human cohorts are uncontrolled/heterogeneous.
- Direct comparative human evidence is lacking.
- Clinical-trial subgroups contain only single-digit numbers of patients.
- Available small trial subgroups do not demonstrate a clear cefiderocol
  advantage.
- Combination benefit is unproven.

## Candidate references for selective audit

HIGH PRIORITY:
  - [603] rabbit pneumonia cefiderocol versus TMP-SMX
  - [604] PK/PD target-attainment modeling
  - [608] meta-analysis, 14 studies / 663 patients
  - [259] very small clinical-trial subgroup
  - [325] cefiderocol versus levofloxacin-based trial subgroup

SUPPORTING:
  - [45,322,596–600] surveillance / resistance
  - [535,601,602] animal-model evidence
  - [403,605–607] observational clinical outcomes

### SEA appraisal flag — NOT A SCORE

The source is unusually transparent that its preferred therapy is being selected
primarily from microbiologic and animal evidence rather than demonstrated
human comparative benefit. Final SEA appraisal should explicitly test whether
the strong "preferred" positioning is proportionate to that indirect evidence.

---

# 8. Question 6.2 — Aztreonam-avibactam

## Clinical question

**What is the role of aztreonam-avibactam for the treatment of invasive
S. maltophilia infections?**

## Suggested approach

**Aztreonam-avibactam, preferably in combination with a second agent, is an
alternative treatment option.**

## Mechanistic rationale

S. maltophilia produces:

- L1 MBL:
  - hydrolyzes essentially all beta-lactams except aztreonam;
- L2 cephalosporinase:
  - hydrolyzes aztreonam.

Avibactam inhibits L2.

Therefore:

1. aztreonam escapes L1;
2. avibactam protects aztreonam from L2;
3. protected aztreonam can bind its primary target, PBP3 [589,609–611].

The mechanistic logic is strong, but mechanistic plausibility is not itself
clinical efficacy.

## AST / surveillance

As of 2026:

- no CLSI susceptibility breakpoint exists for aztreonam-avibactam against
  S. maltophilia;
- no FDA breakpoint exists.

Surveillance data:

- **>90%** of isolates have aztreonam-avibactam MICs ≤4/4 µg/mL [612–615].

Important:
4/4 µg/mL is the Enterobacterales susceptibility breakpoint and should not be
presented as a validated S. maltophilia susceptibility threshold.

Potential resistance mechanisms include:

- L1 overexpression;
- L2 overexpression;
- Sme multidrug-efflux upregulation [609,616].

## PK/PD evidence

Neutropenic murine thigh model [617]:

- 27 S. maltophilia isolates;
- range of aztreonam-avibactam MICs;
- human-simulated Enterobacterales dosing;
- among infections with isolates having MIC ≤4/4 µg/mL,
  **72%** achieved at least a **1-log10 CFU reduction**.

Major limitation:

- the S. maltophilia PD target required for 1-log killing has not been defined.

Consequence:

- animal results are difficult to translate precisely to human dosing efficacy;
- Monte Carlo simulation of human probability of target attainment cannot be
  performed with a validated S. maltophilia target.

## Clinical evidence

Evidence consists largely of:

- favorable case reports [618–621];
- tiny S. maltophilia subgroups from broader clinical trials.

Two trial subgroup analyses [259,310]:

total_S_maltophilia_patients: 4
all_received: aztreonam-avibactam

outcomes:
  favorable: 1
  indeterminate: 1
  unfavorable: 2

Interpretation:
No meaningful clinical efficacy estimate can be generated from four patients.

## Combination and step-down strategy

Because PK/PD and clinical evidence are limited:

- panel favors aztreonam-avibactam as part of combination therapy;
- transition to monotherapy should occur only after:
  1. clear clinical improvement;
  2. sustained clinical improvement;
  3. confirmation of in-vitro susceptibility.

## If aztreonam-avibactam is unavailable

**Ceftazidime-avibactam plus aztreonam is considered reasonable.**

Mechanistically informed PD modeling suggests similar activity [622].

Advantages of fixed aztreonam-avibactam:

- single-agent administration;
- greater practical convenience [623].

Limitations of ceftazidime-avibactam + aztreonam:

- same general scarcity of S. maltophilia clinical-outcome data;
- similar PK/PD uncertainty;
- greater administration complexity.

## Adult dosing dependencies — Table 1

### Aztreonam-avibactam

loading:
  dose: 2.67 g
  components:
    aztreonam: 2 g
    avibactam: 0.67 g
  route: IV
  infusion: 3 hours

maintenance:
  dose: 2 g
  components:
    aztreonam: 1.5 g
    avibactam: 0.5 g
  route: IV
  frequency: every 6 hours
  infusion: 3 hours

### Ceftazidime-avibactam PLUS aztreonam

ceftazidime_avibactam:
  dose: 2.5 g
  components:
    ceftazidime: 2 g
    avibactam: 0.5 g
  route: IV
  frequency: every 8 hours
  infusion: 3 hours

aztreonam:
  dose: 2 g IV
  frequency: every 8 hours
  infusion: 3 hours

administration:
  simultaneous_via_Y_site: yes

supplement_dependency: yes

## Breakpoint dependency

S_maltophilia_specific_breakpoint: NONE

## Explicit evidence limitations

- No organism-specific validated breakpoint.
- S. maltophilia PD target for killing undefined.
- Human PTA therefore cannot be robustly modeled.
- Clinical experience consists principally of case reports.
- Trial subgroup evidence totals only four patients.
- Combination strategy has not been proven superior in comparative trials.

## Candidate references for selective audit

HIGH PRIORITY:
  - [617] 27-isolate murine PK/PD study
  - [259,310] clinical-trial subgroups
  - [622] mechanistically informed PD modeling

SUPPORTING:
  - [589,609–611] beta-lactamase/PBP mechanism
  - [612–615] MIC surveillance
  - [616] resistance mechanisms
  - [618–621] case reports
  - [623] administration feasibility
  - [315–317] ceftazidime-avibactam + aztreonam administration

### SEA appraisal flag — NOT A SCORE

This recommendation has high mechanistic coherence but very low direct clinical
precision. Final appraisal should avoid allowing elegant beta-lactamase biology
to substitute for demonstrated patient-centered efficacy.

---

# 9. Question 6.3 — Levofloxacin

## Clinical question

**What is the role of levofloxacin for the treatment of invasive
S. maltophilia infections?**

## Suggested approach

**Levofloxacin, as a component of combination therapy, is an alternative
treatment option.**

## Susceptibility and resistance

U.S. surveillance:

- approximately **90% susceptible**;
- susceptible MIC threshold: **≤2 µg/mL** [612,624].

Treatment-emergent resistance:

- approximately **20% of cases** [625–628].

Mechanisms:

- Smqnr-related interference with fluoroquinolone target binding;
- Sme multidrug efflux overexpression [591,629–631].

These mechanisms may be selected or amplified under levofloxacin treatment
pressure.

## PK/PD evidence

The section describes levofloxacin as frequently failing to produce:

- sustained bacterial suppression;
- reliable attainment of killing-associated PK/PD targets [632–635].

### Key murine thigh model [632]

regimen: levofloxacin 750 mg IV every 24 hours
isolate_MIC: 2 µg/mL

probability_of_target_attainment:
  bacterial_stasis: approximately 50%
  ≥1_log_bacterial_reduction: approximately 27%

The tested MIC equals the CLSI susceptible breakpoint.

This creates a clinically important tension:
an isolate can satisfy the susceptibility criterion while modeled exposures
still have a relatively low probability of producing bactericidal activity.

### Murine pneumonia model [636]

survival:
  levofloxacin: 50%
  placebo: 0%

However:

- microbiologic eradication was inconsistent.

## Clinical evidence

No clinical trials specifically establish levofloxacin efficacy for
S. maltophilia infection.

Observational evidence is limited by:

- small samples;
- heterogeneous infection sites;
- colonization-versus-infection misclassification;
- concurrent antimicrobial therapy;
- inconsistent levofloxacin dosing [580,608,626,627,637–644].

Across available studies:

- levofloxacin has not been definitively shown superior to minocycline or
  TMP-SMX;
- no one of these three agents has consistently produced better patient outcomes.

Combination cohorts:

- have not clearly shown that combinations of levofloxacin, minocycline, or
  TMP-SMX improve outcomes over monotherapy [580,645,646].

## Why the panel retains combination therapy

The panel cites four principal concerns:

1. variable baseline susceptibility;
2. approximately 20% treatment-emergent resistance;
3. limited PK/PD support for bactericidal activity;
4. difficult-to-interpret clinical outcomes data.

Therefore levofloxacin is suggested initially as a **component of combination
therapy**, despite the absence of evidence clearly demonstrating that the
combination itself improves outcomes.

## Step-down

Levofloxacin monotherapy should be considered only after:

- clear clinical improvement;
- sustained clinical improvement;
- confirmation of susceptibility.

## Safety

Levofloxacin-associated toxicities highlighted by the section include [647]:

- tendinopathy;
- QT prolongation;
- dysglycemia;
- increased risk of *C. difficile* infection;
- central nervous system effects.

## IV-to-oral applicability

- Oral levofloxacin has high bioavailability.
- Systemic exposure is comparable to IV administration [648].

This makes oral step-down pharmacokinetically feasible when the broader clinical
and susceptibility criteria are satisfied.

## Adult dose — Table 1

levofloxacin: 750 mg IV/PO every 24 hours

## Breakpoint — Table 2

S_maltophilia_susceptible: ≤2 µg/mL

## Stewardship/resistance issue

The approximately 20% reported rate of resistance emergence is one of the
section's clearest agent-specific resistance warnings and materially weakens
confidence in levofloxacin monotherapy during active invasive disease.

## Candidate references for selective audit

HIGH PRIORITY:
  - [625–628] treatment-emergent resistance
  - [632] murine PK/PD target attainment
  - [637–644] comparative observational evidence
  - [645,646] combination versus monotherapy evidence

SUPPORTING:
  - [612,624] surveillance susceptibility
  - [591,629–631] resistance mechanisms
  - [633–636] additional PK/PD and animal evidence
  - [647] toxicity
  - [648] oral/IV pharmacokinetics

### SEA appraisal flag — NOT A SCORE

The breakpoint/PK-PD discordance is load-bearing: approximately 90% in-vitro
susceptibility should not be interpreted as approximately 90% probability of
adequate bactericidal exposure or clinical success.

---

# 10. Question 6.4 — Minocycline

## Clinical question

**What is the role of minocycline for the treatment of invasive
S. maltophilia infections?**

## Suggested approach

**Minocycline, as a component of combination therapy, is an alternative
treatment option.**

## Susceptibility / resistance

U.S. surveillance:

- approximately **90% susceptible**;
- MIC ≤1 µg/mL [612].

Major resistance mechanism:

- Sme multidrug-efflux overexpression [649].

Breakpoint advantage:

- CLSI susceptibility criterion exists for minocycline;
- neither CLSI nor FDA provides breakpoints for the other tetracycline
  derivatives discussed.

## PK/PD evidence

The source describes PK/PD studies as the strongest evidence supporting
minocycline [635,650,651].

### Key neutropenic murine thigh model [651]

regimen: minocycline 200 mg IV every 12 hours
MIC: 1 µg/mL

target_attainment:
  bacterial_stasis: >90%
  ≥1_log_bacterial_reduction: approximately 50%

Compared with levofloxacin at its breakpoint, minocycline has substantially more
favorable modeled target attainment for stasis and greater, although still
incomplete, target attainment for killing.

Equivalent investigations have not been performed for other tetracycline
derivatives.

## Clinical evidence

- No dedicated clinical trials.
- Observational studies do not clearly favor:
  - minocycline;
  - levofloxacin;
  - TMP-SMX [641,642,652–654].
- Combination cohorts likewise have not clearly established improved outcomes
  versus monotherapy [580,645,646].

## Bloodstream-infection concern

Minocycline produces relatively low sustained serum concentrations [61].

The panel therefore raises particular concern about reliance on minocycline
monotherapy for invasive disease involving the bloodstream.

## Combination and step-down

Initial:
- minocycline should be a component of combination therapy.

Monotherapy transition:
- only after clear and sustained clinical improvement.

## IV-to-oral applicability

Oral bioavailability: approximately **95%**.

The guidance considers IV and oral minocycline interchangeable because oral
therapy produces comparable:

- serum concentrations;
- steady-state trough concentrations;
- elimination half-life [562].

## Safety

Common adverse effects emphasized:

- gastrointestinal symptoms;
- vestibular effects;
- skin reactions [561,562].

## Tetracycline hierarchy

The panel prefers:

**minocycline > tigecycline**

because minocycline has:

- established susceptibility criteria;
- better-characterized PD targets from animal models.

Not suggested:

- eravacycline;
- omadacycline.

Reason:

- evidence is sparse and/or unfavorable [655,656].

## Adult dose — Table 1

minocycline: 200 mg IV/PO every 12 hours

## Breakpoint — Table 2

S_maltophilia_susceptible: ≤1 µg/mL

## Candidate references for selective audit

HIGH PRIORITY:
  - [651] minocycline PK/PD target attainment
  - [641,642,652–654] observational clinical comparisons
  - [580,645,646] combination versus monotherapy

SUPPORTING:
  - [612] susceptibility surveillance
  - [649] resistance mechanism
  - [635,650] PK/PD
  - [61] serum exposure
  - [561,562] safety and oral PK
  - [655,656] eravacycline/omadacycline evidence

### SEA appraisal flag — NOT A SCORE

Among traditional alternatives, minocycline has comparatively coherent
breakpoint and PK/PD support, but the transition from those surrogate data to
patient-centered benefit remains largely observational.

---

# 11. Question 6.5 — Trimethoprim-sulfamethoxazole

## Clinical question

**What is the role of TMP-SMX for the treatment of invasive
S. maltophilia infections?**

## Suggested approach

**TMP-SMX, as a component of combination therapy, is an alternative treatment
option.**

This is notably more restrictive than treating historical use of TMP-SMX as an
automatic standard of care.

## Susceptibility / resistance

U.S. surveillance:

- **>90% susceptible**;
- breakpoint: TMP-SMX MIC ≤2/38 µg/mL [612,657].

Resistance mechanisms include:

- multidrug-efflux overexpression;
- acquired **sul** genes;
- acquired **dfrA** genes [593,658,659].

## PK/PD evidence

Despite extensive historical clinical use, multiple PK/PD investigations
consistently indicate that TMP-SMX:

- lacks reliable bactericidal activity;
- remains non-bactericidal even at high doses;
- remains non-bactericidal even against isolates with low TMP MICs
  [596,650,660–662].

Across multiple in-vitro and PK/PD models:

- best observed effect is generally **bacterial stasis**;
- enhanced activity may occur in combination regimens [650,661].

Important distinction:
enhanced activity in experimental combination models is not equivalent to
demonstrated improvement in patient outcomes from clinical combination therapy.

## Rabbit pneumonia comparison [603]

TMP-SMX:

- reduced bacterial burden;
- did not eradicate S. maltophilia.

Survival:

| Regimen | Survival |
|---|---:|
| Cefiderocol | 88% (7/8) |
| TMP-SMX | 25% (2/8) |

Critical limitation:

- TMP-SMX exposures in the rabbits were unknown.

Therefore, the magnitude should be preserved but not overinterpreted as a
validated human comparative-effectiveness estimate.

## Clinical evidence

Clinical trials specifically evaluating TMP-SMX for S. maltophilia infection
are lacking.

Observational studies:

- do not establish a clear relative-effectiveness advantage for TMP-SMX over
  levofloxacin or minocycline [641,642,652–654].

Major study limitations:

- heterogeneous infection syndromes;
- small sample sizes;
- frequent concomitant antibiotics;
- colonization/infection misclassification.

Combination versus monotherapy:

- unresolved;
- available cohorts do not establish improved outcomes from TMP-SMX-based
  combinations [580,645,646].

## Panel rationale for combination therapy

Despite the absence of consistent evidence that combination therapy improves
clinical outcomes, the panel limits TMP-SMX to a component of combination
therapy for initial invasive treatment because of:

- weak bactericidal PK/PD support;
- uncertain comparative clinical outcomes.

## Step-down

TMP-SMX monotherapy should be considered only after:

- clear clinical improvement;
- sustained clinical improvement.

## Safety and monitoring

Toxicities emphasized [663]:

- hypersensitivity reactions;
- hematologic abnormalities;
- gastrointestinal intolerance;
- hepatotoxicity;
- renal dysfunction;
- electrolyte disturbances.

The source explicitly states that these warrant close monitoring.

## IV-to-oral applicability

- Oral TMP-SMX has essentially complete bioavailability.
- Systemic exposure is equivalent to IV administration [664].

## Adult dosing — Table 1

For infections other than uncomplicated UTI:

TMP_component:
  total_daily_dose: 8–15 mg/kg/day
  route: IV or PO
  schedule: divided every 8–12 hours

supplement_dependency: yes

## Breakpoint — Table 2

S_maltophilia_susceptible: ≤2/38 µg/mL

## Candidate references for selective audit

HIGH PRIORITY:
  - [596,650,660–662] non-bactericidal PK/PD
  - [603] rabbit cefiderocol comparison
  - [641,642,652–654] observational comparative evidence
  - [580,645,646] combination versus monotherapy

SUPPORTING:
  - [612,657] susceptibility
  - [593,658,659] resistance mechanisms
  - [663] toxicity
  - [664] oral bioavailability

### SEA appraisal flag — NOT A SCORE

Historical familiarity should not be used as a surrogate for evidence strength.
This section specifically undermines an assumption that high susceptibility
rates plus long-standing use necessarily establish TMP-SMX as the strongest
agent for invasive disease.

---

# 12. Question 6.6 — Ceftazidime

## Clinical question

**What is the role of ceftazidime for the treatment of invasive
S. maltophilia infections?**

## Suggested approach

**Ceftazidime is not suggested for S. maltophilia infection.**

## Rationale

Intrinsic beta-lactamase biology predicts inactivity:

- L1 beta-lactamase;
- L2 beta-lactamase.

Preclinical evidence:

- ceftazidime is unable to substantially prevent S. maltophilia growth [650].

Clinical evidence:

- comparative-effectiveness studies are described as virtually non-existent.

Regulatory/AST context:

- as of 2024, neither CLSI nor FDA maintains a susceptibility breakpoint for
  ceftazidime against S. maltophilia [21].

## Adult dosing dependency

None required for this section because the drug is not suggested.

## Breakpoint dependency

No current CLSI/FDA S. maltophilia breakpoint.

## Candidate references for selective audit

- [589] intrinsic L1/L2 beta-lactamase biology
- [650] preclinical ceftazidime activity
- [21] breakpoint status

### SEA appraisal flag — NOT A SCORE

Unlike several positive recommendations in this section, the negative
ceftazidime recommendation is mechanistically straightforward and aligned with
the absence of a current susceptibility breakpoint; however, direct comparative
clinical evidence is also nearly absent.

---

# 13. Cross-question pharmacotherapy matrix

| Feature | Cefiderocol | Aztreonam-avibactam | Levofloxacin | Minocycline | TMP-SMX |
|---|---|---|---|---|---|
| Source role | Preferred | Alternative | Alternative | Alternative | Alternative |
| Initial use | Monotherapy | Prefer combination | Combination | Combination | Combination |
| Approx. surveillance activity | Approaches 100% | >90% MIC ≤4/4; **not validated susceptibility rate** | ~90% susceptible | ~90% susceptible | >90% susceptible |
| CLSI S. maltophilia breakpoint | ≤1 | None | ≤2 | ≤1 | ≤2/38 µg/mL |
| Strongest evidence domain | Animal + PK/PD + surveillance | Mechanism + animal PK/PD | Surveillance + observational + PK/PD | PK/PD + observational | Surveillance + PK/PD + observational |
| Dedicated clinical trials | No | No | No | No | No |
| Major clinical-data problem | Tiny/unfavorable subgroups; uncontrolled cohorts | Only four trial-subgroup patients | Observational confounding | Observational confounding | Observational confounding |
| Important resistance issue | Iron-transport mutations | L1/L2 overexpression; Sme | ~20% emergence; Smqnr/Sme | Sme | Efflux; sul/dfrA |
| Killing support | Strongest preclinical signal | Incomplete target definition | Weak | Intermediate | Generally stasis |
| Oral option | No | No | Yes | Yes | Yes |
| Monotherapy step-down explicitly supported | Already monotherapy | After sustained improvement + susceptibility | After sustained improvement + susceptibility | After sustained improvement | After sustained improvement |
| Major section-specific safety issue | Not emphasized | Not emphasized | FQ toxicities | GI/vestibular/skin | Multiple systemic toxicities |
| Supplement dependency | No | CZA+ATM alternative: yes | No | No | Yes |

---

# 14. Cross-cutting evidence architecture

## 14.1 What the section has

The S. maltophilia treatment framework draws from:

- antimicrobial-surveillance datasets;
- resistance-mechanism studies;
- AST-methodology studies;
- in-vitro experiments;
- mechanistic pharmacology;
- PK/PD modeling;
- neutropenic murine thigh models;
- murine pneumonia models;
- neutropenic rabbit pneumonia models;
- case reports;
- retrospective observational cohorts;
- meta-analysis;
- tiny organism-specific subgroups nested within broader clinical trials;
- expert-panel synthesis.

## 14.2 What the section largely does not have

The section lacks:

- adequately powered randomized trials comparing standard active agents;
- a clearly established standard-of-care comparator;
- robust trials of combination versus monotherapy;
- consistent syndrome-specific comparative data;
- strong evidence linking MIC directly to clinical outcome;
- strong evidence establishing the optimal initial combination partner;
- validated S. maltophilia aztreonam-avibactam breakpoint;
- high-certainty patient-centered evidence supporting the rank order of most
  therapies.

---

# 15. Central contradiction / tension for final SEA synthesis

The section must solve a high-stakes treatment problem despite a weak direct
comparative evidence base.

The resulting hierarchy is:

**cefiderocol monotherapy preferred**

versus

**aztreonam-avibactam, levofloxacin, minocycline, and TMP-SMX generally
positioned as combination-therapy alternatives**

yet:

- comparative clinical trials are absent;
- combination therapy has not clearly outperformed monotherapy in available
  cohorts;
- cefiderocol's preferred status is driven predominantly by susceptibility,
  PK/PD, and animal bactericidal evidence rather than proven superior human
  outcomes.

This tension is not hidden by the authors; it is repeatedly acknowledged in the
text and should remain visible in the final SEA rather than being compressed
away.

---

# 16. Major section-level limitations to carry into final appraisal

## 16.1 Diagnostic misclassification

S. maltophilia frequently represents:

- colonization;
- polymicrobial recovery;
- true invasive disease.

Clinical cohorts may mix these states.

## 16.2 Confounding in observational comparisons

Likely contributors include:

- illness-severity differences;
- different infection syndromes;
- concomitant active antimicrobials;
- selection of therapy based on susceptibility;
- source-control differences;
- host immunologic status;
- clinician selection of combination therapy for sicker patients.

The guidance identifies several of these directly; others should be assessed
during primary-study audit rather than assumed corrected.

## 16.3 Surrogate-to-clinical translation

Much of the rank ordering depends on:

- MIC distributions;
- stasis targets;
- 1-log bacterial reduction;
- animal survival;
- animal tissue eradication.

These are biologically useful but remain indirect relative to human survival,
clinical cure, toxicity, and relapse.

## 16.4 Very small trial subgroups

Examples:

cefiderocol:
  trial_subgroup_1: 1/5 survival
  trial_subgroup_2: 3/5 versus 3/3 survival

aztreonam_avibactam:
  total_trial_subgroup_patients: 4

These results should be preserved for completeness but should carry very little
comparative inferential weight.

## 16.5 AST uncertainty

Even "susceptible" is less secure than usual because:

- testing-method reproducibility may be problematic;
- PK/PD support for breakpoints is incomplete;
- MIC-outcome relationships are underdeveloped.

## 16.6 Combination-therapy uncertainty

The panel repeatedly favors combination therapy for alternatives, but:

- available cohorts have not clearly demonstrated superiority;
- partner selection is not established;
- optimal duration of combination therapy is not established;
- step-down thresholds rely on clinical improvement rather than comparative
  trial evidence.

## 16.7 External validity

The guidance is U.S.-focused.

Surveillance susceptibility estimates therefore require caution when
extrapolated to:

- other countries;
- different hospital ecologies;
- local outbreaks;
- highly selected resistance phenotypes.

---

# 17. Quantitative anchor register

The following values should survive hierarchical condensation:

1. Cefiderocol susceptibility approaches **100%**.
2. Cefiderocol modeled bactericidal target attainment: **>90%**.
3. Rabbit pneumonia survival:
   - cefiderocol **88% (7/8)**
   - TMP-SMX **25% (2/8)**
   - untreated **0%**
4. Cefiderocol observational survival: approximately **70%**.
5. Alternative-agent meta-analysis:
   - **14 studies**
   - **663 patients**
   - survival approximately **70%**
6. Cefiderocol trial subgroup:
   - **1/5 (20%)** survival.
7. Second cefiderocol trial subgroup:
   - cefiderocol **3/5 (60%)**
   - levofloxacin-based alternative **3/3 (100%)**
8. Aztreonam-avibactam surveillance:
   - **>90%** isolates MIC ≤4/4 µg/mL
   - NOT equivalent to validated S. maltophilia susceptibility.
9. Aztreonam-avibactam murine model:
   - **27 isolates**
   - ≥1-log10 CFU reduction in **72%** for isolates MIC ≤4/4.
10. Aztreonam-avibactam trial subgroup:
    - **4 total patients**
    - 1 favorable
    - 1 indeterminate
    - 2 unfavorable.
11. Levofloxacin:
    - approximately **90% susceptible**
    - approximately **20%** resistance emergence.
12. Levofloxacin 750 mg q24h at MIC 2:
    - ~**50%** PTA for stasis
    - ~**27%** PTA for ≥1-log reduction.
13. Levofloxacin murine pneumonia survival:
    - **50%** versus **0%** placebo.
14. Minocycline:
    - approximately **90% susceptible**.
15. Minocycline 200 mg q12h at MIC 1:
    - **>90%** PTA for stasis
    - ~**50%** PTA for ≥1-log reduction.
16. Minocycline oral bioavailability:
    - approximately **95%**.
17. TMP-SMX:
    - **>90% susceptible**
    - generally no greater than bacterial stasis in PK/PD models.
18. TMP-SMX rabbit comparison:
    - **25% (2/8)** survival versus cefiderocol **88% (7/8)**.

---

# 18. Candidate reference-audit queue

## Tier 1 — likely load-bearing for final appraisal

### Diagnostic / AST
- [594,595] susceptibility-test reproducibility
- [21] breakpoint framework

### Cefiderocol
- [603] rabbit pneumonia model
- [604] PK/PD target attainment
- [608] 14-study / 663-patient meta-analysis
- [259,325] clinical-trial subgroup data

### Aztreonam-avibactam
- [617] 27-isolate murine PK/PD study
- [259,310] trial subgroup data
- [622] mechanistically informed PD comparison

### Levofloxacin
- [625–628] treatment-emergent resistance
- [632] PK/PD target attainment
- [637–644] clinical comparative cohorts
- [645,646] combination-versus-monotherapy cohorts

### Minocycline
- [651] PK/PD target attainment
- [641,642,652–654] comparative observational evidence

### TMP-SMX
- [596,650,660–662] bacteriostatic PK/PD findings
- [603] cefiderocol/TMP-SMX animal comparison
- [641,642,652–654] comparative observational evidence

## Tier 2 — mechanism / implementation

- [575–581] epidemiology and importance of timely active therapy
- [583–587] severe invasive disease
- [589–593] intrinsic/acquired resistance architecture
- [609–616] aztreonam-avibactam mechanism and MIC data
- [623] aztreonam-avibactam feasibility
- [315–317] CZA + aztreonam administration
- [647,648] levofloxacin safety / oral PK
- [561,562] minocycline safety / oral PK
- [663,664] TMP-SMX safety / oral PK

---

# 19. Hierarchical synthesis statements

These statements are suitable for later incorporation into the global SEA.

## Source-derived synthesis

1. The S. maltophilia section addresses invasive infection only and makes
   distinguishing infection from colonization a prerequisite to rational
   treatment.

2. There is no clearly established clinical standard-of-care comparator, and
   direct trials comparing commonly used S. maltophilia therapies are lacking.

3. Cefiderocol monotherapy is the panel's preferred therapy, principally because
   of near-universal in-vitro activity and reproducible bactericidal activity in
   animal models rather than demonstrated superiority in clinical-outcome
   studies.

4. Aztreonam-avibactam, levofloxacin, minocycline, and TMP-SMX are alternative
   options generally initiated as components of combination therapy because each
   has important PK/PD, resistance, or clinical-evidence limitations.

5. The evidence does not clearly establish that combination therapy produces
   better patient outcomes than monotherapy with levofloxacin, minocycline, or
   TMP-SMX.

6. TMP-SMX retains high in-vitro susceptibility but experimental PK/PD evidence
   indicates primarily bacteriostatic rather than bactericidal activity.

7. Levofloxacin is limited by approximately 20% reported treatment-emergent
   resistance and relatively poor modeled bactericidal target attainment at the
   susceptible breakpoint.

8. Minocycline has comparatively favorable PK/PD target attainment among the
   traditional alternatives but limited clinical comparative evidence and
   potential concern about sustained serum exposure in bloodstream infection.

9. Aztreonam-avibactam has strong mechanistic rationale but lacks an
   S. maltophilia-specific breakpoint, validated killing target, and meaningful
   clinical sample size.

10. Ceftazidime should not be used because intrinsic L1/L2 beta-lactamases are
    expected to confer inactivity and contemporary susceptibility breakpoints no
    longer exist.

## Appraisal hypotheses for final SEA — NOT FINAL JUDGMENTS

A. The S. maltophilia recommendations are clinically useful but unusually
   dependent on mechanistic, surveillance, PK/PD, and animal evidence.

B. The clinical evidence is weakest exactly where therapeutic ranking is most
   consequential.

C. The panel appropriately exposes much of this uncertainty rather than
   presenting the hierarchy as high-certainty comparative evidence.

D. "Preferred" cefiderocol and "combination therapy" for alternatives should be
   appraised independently:
   - cefiderocol preference is primarily a preclinical-evidence decision;
   - combination therapy is primarily a risk-management strategy under
     uncertainty rather than an established comparative benefit.

E. AST uncertainty and colonization misclassification should probably function
   as major evidence-strength modifiers in the final appraisal.

F. Final SEA should avoid equating:
   - susceptibility with bactericidal target attainment;
   - animal efficacy with proven human superiority;
   - historical use with clinical evidence quality;
   - panel recommendation strength of wording with formal evidence certainty.

---

# 20. Implementation implications to preserve

Before targeted treatment:

- establish a plausible invasive syndrome;
- distinguish colonization whenever possible;
- assess whether polymicrobial infection better explains the presentation;
- obtain and critically interpret AST.

Initial treatment according to this source:

preferred:
  - cefiderocol monotherapy

alternatives:
  - aztreonam-avibactam, preferably with another active agent
  - levofloxacin as combination therapy
  - minocycline as combination therapy
  - TMP-SMX as combination therapy

if_aztreonam_avibactam_unavailable:
  - ceftazidime-avibactam plus aztreonam
  - administer according to the Table 1/Supplemental Material strategy

avoid:
  - ceftazidime

Potential oral transition agents:

- levofloxacin
- minocycline
- TMP-SMX

But oral bioavailability alone does not authorize step-down. The section
requires clear/sustained clinical improvement before transition to monotherapy
for these agents, with susceptibility confirmation explicitly required for
levofloxacin and aztreonam-avibactam.

Monitoring priorities carried directly from section content:

levofloxacin:
  - clinical response
  - emergence of resistance
  - tendinopathy
  - QT effects
  - dysglycemia
  - CNS toxicity
  - C. difficile risk

minocycline:
  - clinical response
  - GI intolerance
  - vestibular toxicity
  - skin reactions
  - particular caution if bloodstream infection

TMP_SMX:
  - clinical response
  - hypersensitivity
  - blood counts
  - hepatic toxicity
  - renal dysfunction
  - electrolyte disturbances

---

# 21. Data that should NOT be overclaimed in final SEA

Do not state:

- "Cefiderocol has been proven superior to TMP-SMX in humans."
- "Cefiderocol improves human survival."
- "Aztreonam-avibactam is >90% susceptible against S. maltophilia."
- "Combination therapy is superior to monotherapy."
- "Levofloxacin susceptibility predicts bactericidal exposure."
- "Minocycline is clinically superior to TMP-SMX or levofloxacin."
- "TMP-SMX is the standard of care because it has historically been used."
- "The rabbit cefiderocol/TMP-SMX comparison proves comparative clinical
  efficacy."
- "A CLSI breakpoint validates clinical efficacy."
- "S. maltophilia isolated from a respiratory culture necessarily requires
  treatment."

---

# 22. Section-level completion gate

section_intro_extracted: PASS
colonization_infection_boundary_extracted: PASS
resistance_architecture_extracted: PASS
AST_limitations_extracted: PASS

Q6_1_cefiderocol:
  suggested_approach: PASS
  evidence_architecture: PASS
  quantitative_results: PASS
  limitations: PASS
  dosing_dependency: PASS
  breakpoint_dependency: PASS

Q6_2_aztreonam_avibactam:
  suggested_approach: PASS
  mechanism: PASS
  evidence_architecture: PASS
  quantitative_results: PASS
  limitations: PASS
  dosing_dependency: PASS
  supplement_dependency: PASS
  breakpoint_gap: PASS

Q6_3_levofloxacin:
  suggested_approach: PASS
  resistance_emergence: PASS
  PK_PD: PASS
  clinical_evidence: PASS
  toxicity: PASS
  oral_transition: PASS
  dosing_dependency: PASS
  breakpoint_dependency: PASS

Q6_4_minocycline:
  suggested_approach: PASS
  PK_PD: PASS
  clinical_evidence: PASS
  bloodstream_caution: PASS
  toxicity: PASS
  oral_transition: PASS
  dosing_dependency: PASS
  breakpoint_dependency: PASS

Q6_5_TMP_SMX:
  suggested_approach: PASS
  PK_PD: PASS
  clinical_evidence: PASS
  toxicity: PASS
  oral_transition: PASS
  dosing_dependency: PASS
  supplement_dependency: PASS
  breakpoint_dependency: PASS

Q6_6_ceftazidime:
  negative_recommendation: PASS
  mechanistic_basis: PASS
  clinical_evidence_gap: PASS
  breakpoint_status: PASS

figures_reconciled: PASS — none in section
section_specific_tables_reconciled: PASS — none
global_Table_1_dependencies_reconciled: PASS
global_Table_2_dependencies_reconciled: PASS

primary_study_independent_verification: NOT PERFORMED
supplemental_material_independent_review: NOT PERFORMED
final_appraisal_scores_allowed: NO
hierarchical_handoff_ready: YES

SECTION_6_DEEP_PASS_STATUS: COMPLETE