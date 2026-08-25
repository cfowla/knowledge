# Reference Task Queue — Bethune & Herriot 2019

Source article: **Bethune C, Herriot R. “Switching immunoglobulin products, what are the implications? Result of 2018 census of immunology centres.” Clinical Medicine. 2019;19(3):201–204.**

Source locator: References, article p. 204. Queue entries preserve the citations as printed in the retrieved primary article; no missing bibliographic details have been invented.

## Queue

- [ ] **Ref 1 — Misbah SA.** *Should therapeutic immunoglobulin be considered a generic product? An evidence-based approach.* J Allergy Clin Immunol Pract. 2013;567–72.
  - [ ] Acquire lawful full text or best available primary source.
  - [ ] Confirm complete citation/identifier from the acquired source.
  - [ ] Run `@ATOM` on the acquired source when eligible.
  - [ ] Run `@SEA` on the acquired source.
  - [ ] Cross-check the parent article’s claims about interchangeability, switch avoidance, adverse reactions, traceability, and infection-risk rationale.

- [ ] **Ref 2 — Ameratunga R, Sinclair J, Kolbe J.** *Increased risk of adverse events when changing immunoglobulin preparations.* Clin Exp Immunol. 2004;136:111–3.
  - [ ] Acquire lawful full text.
  - [ ] Confirm complete citation/identifier from the acquired source.
  - [ ] Run `@ATOM`.
  - [ ] Run `@SEA`.
  - [ ] Compare the reported adverse-event signal with the 2018 UKPIN/QPIDS census findings.

- [ ] **Ref 3 — Aghamohammadi A, Farhoudi A, Nikzad M, et al.** *Adverse reactions of prophylactic intravenous immunoglobulin infusions in Iranian patients with primary immunodeficiency.* Ann Allergy Asthma Immunol. 2004;92:60–4.
  - [ ] Acquire lawful full text.
  - [ ] Confirm complete citation/identifier from the acquired source.
  - [ ] Run `@ATOM`.
  - [ ] Run `@SEA`.
  - [ ] Extract reaction definitions, denominators, product/regimen details, and severity to assess comparability with switch-associated events in the parent article.

- [ ] **Ref 4 — Chapel HM.** *Safety and availability of immunoglobulin replacement therapy in relation to potentially transmissable agents.* Clin Exp Immunol. 1999;118(Suppl 1):22–34.
  - [ ] Acquire lawful full text.
  - [ ] Confirm complete citation/identifier from the acquired source.
  - [ ] Run `@ATOM` if the source contains independently reviewable primary-literature assertions suitable for the current schema.
  - [ ] Run `@SEA`.
  - [ ] Review evidence supporting traceability, donor-pool stability, and infectious-risk arguments around product switching.

- [ ] **Ref 5 — Royal College of Physicians.** *Quality in Primary Immunodeficiency Services.* `www.qpids.org.uk`.
  - [ ] Capture the relevant historical/current organizational material if accessible.
  - [ ] Determine whether this is background/accreditation infrastructure or contains a citable primary report requiring extraction.
  - [ ] Do **not** force into `@ATOM` as primary literature unless an eligible publication/source is identified.
  - [ ] Use for provenance of the QPIDS census platform and service-accreditation context.

## Completion rule

A reference is complete when the source has been acquired or formally marked unavailable, its bibliographic identity has been confirmed from the source itself, appropriate `@ATOM`/`@SEA` processing is finished, and any claim-level relationship to the Bethune–Herriot article is documented.
