---
id: src-fcv-002
type: source
title: "Feline calicivirus"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [clinical syndromes, persistence, vaccination]
jurisdictions: []
evidence_level: review
year: 2007
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, review, persistence, vaccination, virulent-systemic]
links:
  doi: "10.1051/vetres:2006056"
  url: "https://www.vetres.org/articles/vetres/abs/2007/02/v06220/v06220.html"
  local_assets: []
evidence_policy:
  quoted_fact:
    - FCV is an important and highly prevalent pathogen of cats.
    - Vaccination reduces clinical disease but does not prevent infection or persistent infection.
  source_supported_conclusion:
    - This is the classic broad FCV review anchor for diversity, persistence, and control limits.
    - The paper supports keeping carrier-state biology central to FCV epidemiology.
  llm_inference:
    - This is one of the best first FCV deep-extraction candidates.
---

# Feline calicivirus

## One-Line Summary

Classic broad review explaining FCV diversity, clinical range, persistence, virulent systemic emergence, and vaccine-control limits.

## Why It Matters For FCV

- gives the module an older but still structurally important whole-disease anchor
- makes it hard to flatten FCV into only mild respiratory disease

## Key Findings

### quoted_fact

- FCV is an important and highly prevalent pathogen of cats.
- Vaccination reduces clinical disease but does not prevent infection or persistent infection.

### source_supported_conclusion

- FCV genetic plasticity drives antigenic and clinical diversity.
- Disease ranges from inapparent infection to oral/upper respiratory disease and virulent systemic disease.
- A minority of cats can remain persistently infected and matter disproportionately for epidemiology.
- The review supports writing FCV control as risk reduction and disease mitigation rather than sterilising closure.

### llm_inference

- This source should remain a classic whole-disease review anchor beneath newer FCV update and vaccine-platform papers.
- Its safest role is `diversity-persistence-control limits`, not `current field-strain surveillance authority`.

## Deep Extraction Notes

### Unit 1: FCV is a variable disease shell, not a single syndrome

- core_claim: the review frames FCV as a broad pathogen with multiple clinical expressions.
- hard_details: the card preserves clinical range from inapparent infection through oral/upper respiratory disease to virulent systemic disease.
- implication: downstream FCV pages should not describe FCV as only mild cat-flu disease.
- boundary: this review can define the shell, but newer studies should own current prevalence, geography, and platform-vaccine details.

### Unit 2: Persistence is central to control logic

- core_claim: persistent infection and carrier-state biology are not side details.
- hard_details: the card preserves that a minority of cats can remain persistently infected.
- implication: prevention and outbreak-control pages should include persistence when discussing why vaccination and hygiene do not close the system.
- boundary: the card does not provide a modern numeric carrier-risk model and should not be used as one.

### Unit 3: Vaccination is beneficial but incomplete

- core_claim: vaccination reduces clinical disease but does not prevent infection or persistent infection.
- hard_details: this statement is preserved as a quoted fact in the source card.
- implication: owner-facing and clinician-facing copy should use `reduces disease` rather than `prevents FCV`.
- boundary: this source should be paired with later neutralisation, challenge, and platform papers for vaccine-performance specifics.

## Claim-Evidence Structure

| Claim | Evidence in this card | Safe downstream use | Do not use for |
|---|---|---|---|
| FCV is prevalent and clinically broad | quoted prevalence/commonness and clinical-spectrum language | broad disease overview | exact modern prevalence |
| Persistence matters | carrier-state and persistent-infection language | control and hygiene rationale | numeric carrier-risk prediction |
| Vaccines are incomplete control tools | vaccination reduces clinical disease but not infection/persistence | vaccination caveat language | product ranking or sterilising-immunity claims |
| Diversity complicates control | genetic plasticity and antigenic/clinical diversity | vaccine-breadth and strain-pressure framing | current strain map |

## Write-Back Implications

- [topic index](../../topics/fcv/index.md) should keep this as a classic FCV shell anchor.
- [current state dashboard](../../topics/fcv/current-state-dashboard.md) should use this source for older but still important persistence and control-limit architecture.
- [translation brief](../../topics/fcv/translation-brief.md) should preserve the vaccine wording distinction: reduce disease, not prevent infection or persistent infection.
- [endpoint handbook](../../topics/fcv/endpoint-handbook.md) should pair this card with newer vaccine-breadth and platform papers rather than letting it own all vaccine claims.

## Limits / Caveats

- review-era framing predates some newer vaccine and therapeutic work
- should not be used alone to represent current field-strain or VS-FCV control performance

## Open Follow-Up Questions

- which persistence claims still hold unchanged in the 2022 and 2025 reviews?
- how directly does this review connect persistence to vaccine failure versus immune escape?

## Linked Entities

- diseases: FCV
- models:
- endpoints: clinical syndromes, persistence, vaccination
- mechanisms: genome plasticity, virulence, carrier state
- regulations:
