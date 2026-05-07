# FCV Source Index

## Seed Corpus

| ID | Title | Primary Layer | Evidence Level | Status |
|---|---|---|---|---|
| src-fcv-001 | An Update on Feline Calicivirus | review | review | deep_extracted; modern shell-review anchor |
| src-fcv-002 | Feline calicivirus | review | review | deep_extracted; classic diversity-persistence-control anchor |
| src-fcv-003 | Comparison of the ability of feline calicivirus (FCV) vaccines to neutralise a panel of current UK FCV isolates | vaccine | original-study | deep_extracted; neutralisation-breadth anchor |
| src-fcv-004 | Feline Calicivirus Infection: ABCD Guidelines on Prevention and Management | guidance | guideline | deep_extracted; practical-control guideline anchor |
| src-fcv-005 | Epidemiological Investigation of Feline Upper Respiratory Tract Infection Encourages a Geographically Specific FCV Vaccine | epidemiology | original-study | deep_extracted; regional epidemiology and vaccine-locality anchor |
| src-fcv-006 | Feline calicivirus and other respiratory pathogens in cats with Feline calicivirus-related symptoms and in clinically healthy cats in Switzerland | epidemiology | original-study | deep_extracted; field-recognition anchor |
| src-fcv-007 | Feline Calicivirus Infection: Current Understanding and Implications for Control Strategies | review | review | deep_extracted; modern broad-control anchor |
| src-fcv-008 | Sensitivity of FCV to recombinant feline interferon (rFeIFN) | therapy | original-study | deep_extracted; interferon-sensitivity caution anchor |
| src-fcv-009 | Calicivirus Infection in Cats | guidance | review | deep_extracted; diagnosis/control bridge anchor |
| src-fcv-010 | Neutralizing Feature of Commercially Available Feline Calicivirus (FCV) Vaccine Immune Sera against FCV Field Isolates | vaccine | original-study | deep_extracted; early field-fit stress-test anchor |
| src-fcv-011 | Characterization of an avirulent FCV strain with a broad serum cross-neutralization profile and protection against challenge of a highly virulent vs feline calicivirus | vaccine | original-study | deep_extracted; challenge-protection anchor |
| src-fcv-012 | Use of serologic tests to predict resistance to feline herpesvirus 1, feline calicivirus, and feline parvovirus infection in cats | endpoint | original-study | deep_extracted; serology-resistance anchor |
| src-fcv-013 | A novel replication-deficient FCV vaccine provides strong immune protection in cats | vaccine | original-study | deep_extracted; replication-deficient platform-vaccine anchor |
| src-fcv-014 | Potential Therapeutic Agents for Feline Calicivirus Infection | therapy | original-study | deep_extracted; assay-stage therapy anchor |
| src-fcv-015 | Molecular Virology of Feline Calicivirus | mechanism | review | deep_extracted; mechanism-spine anchor |
| src-fcv-016 | Distribution of the Feline Calicivirus Receptor Junctional Adhesion Molecule A in Feline Tissues | mechanism | original-study | deep_extracted; JAM-A receptor/tropism anchor |
| src-fcv-017 | Mechanisms for persistence of acute and chronic feline calicivirus infections in the face of vaccination | persistence | original-study | deep_extracted; persistence-control anchor |
| src-fcv-018 | Identification of prevalent Feline Calicivirus strains and novel antiviral efficacy of CpG49 stimulus in Feline Calicivirus-infected cats | therapy | original-study | deep_extracted; first in vivo therapy anchor |
| src-fcv-019 | Advances in Feline Viruses and Viral Diseases | context | commentary | deep_extracted; context-only literature-map anchor |
| src-fcv-020 | Identification of feline calicivirus in cats with enteritis | extension | original-study | deep_extracted; enteric-extension anchor |
| src-fcv-021 | Feline calicivirus: a neglected cause of feline ocular surface infections? | recognition | original-study | deep_extracted; ocular-extension anchor |
| src-fcv-022 | Modified-Live Feline Calicivirus Vaccination Elicits Cellular Immunity against a Current Feline Calicivirus Field Strain in an Experimental Feline Challenge Study | vaccine | original-study | deep_extracted; cellular-immunity anchor |
| src-fcv-023 | Nucleotide sequence of UK and Australian isolates of feline calicivirus (FCV) and phylogenetic analysis of FCVs | mechanism | original-study | deep_extracted; foundational phylogeny/diversity anchor |
| src-fcv-024 | The use of sequence analysis of a feline calicivirus (FCV) hypervariable region in the epidemiological investigation of FCV related disease and vaccine failures | epidemiology | original-study | deep_extracted; sequence-epidemiology and vaccine-failure boundary anchor |

## First-Pass Reading Priorities

### Tier A

- `src-fcv-001`
- `src-fcv-002`
- `src-fcv-004`
- `src-fcv-007`
- `src-fcv-009`
- `src-fcv-015`

### Tier B

- `src-fcv-003`
- `src-fcv-005`
- `src-fcv-006`
- `src-fcv-011`
- `src-fcv-017`
- `src-fcv-022`

## Source Family / Claim-Fit Map

| Family | FCV sources | Strongest safe use | Must not control |
|---|---|---|---|
| guideline / practical guidance | `src-fcv-004` | diagnosis/management order, supportive-control architecture, hygiene/disinfection framing | current product superiority, present-day field coverage claims |
| broad review / synthesis review | `src-fcv-001`, `src-fcv-002`, `src-fcv-007`, `src-fcv-009`, `src-fcv-015` | disease shell, mechanism spine, control architecture, branch naming | one-study-like numeric winner language, jurisdiction-specific label claims |
| original study | `src-fcv-003`, `005`, `006`, `008`, `010`, `011`, `012`, `013`, `014`, `016`, `017`, `018`, `020`, `021`, `022`, `023`, `024` | endpoint ownership, branch-specific detail, field/challenge/mechanism anchors | automatic standard-of-care authority, universal generalization, label truth |
| commentary / editorial context | `src-fcv-019` | context only, literature-map support, subtopic discovery | disease hierarchy, treatment claims, quantitative or decision-bearing conclusions |

## Current FCV Hierarchy Read

- the FCV module should currently be organized by `guideline + broad review + strongest original-study anchors`
- `src-fcv-004` should control practical order more than any single study
- `src-fcv-015` should control mechanism compression more than lighter context reviews
- `src-fcv-003` should control breadth language, `src-fcv-011` should control challenge language, and `src-fcv-017` / `src-fcv-022` should control persistence and cellular-immunity language more than broad review slogans
- `src-fcv-019` should stay low and context-only even if it sounds broad or current

## Current Do-Not-Control Notes

- do not let `src-fcv-019` control disease, treatment, or regulatory prose
- do not let label-like or guidance-like language from reviews drift into jurisdiction-specific approval claims
- do not let single vaccine studies collapse breadth, challenge protection, cellular immunity, and chronic-carrier control into one bucket

## Notes

- All 24 FCV seed paper cards are now deep-extracted at the source-card layer.
- The highest-value compression problem remains `vaccination breadth vs persistent shedding vs recognition heterogeneity`, but the blocker has moved from source-card depth to downstream synthesis and ordinary-user presentation.
- FCV currently has no dedicated regulatory corpus in the seed set; vaccine/control questions are still paper-led.

## Current Status Note

The FCV seed corpus is now mapped into source cards and all 24 paper cards are deep-extracted. The next gains should come from:

- recompiling the current-state, synthesis, endpoint, mechanism, and recognition pages against the now-complete source-card layer
- keeping vaccine, therapy, and regulatory claims below product-ranking or label-language status until dedicated field-effectiveness and regulatory corpora exist

## Started Outputs

- [FCV topic index](../../topics/fcv/index.md)
- [FCV navigation](../../topics/fcv/navigation.md)
- [FCV current state dashboard](../../topics/fcv/current-state-dashboard.md)
- [FCV source depth map](fcv-source-depth-map.md)
- [src-fcv-001 deep extraction round 1](src-fcv-001-deep-extraction-round1.md)
- [src-fcv-003 deep extraction round 1](src-fcv-003-deep-extraction-round1.md)
- [src-fcv-004 deep extraction round 1](src-fcv-004-deep-extraction-round1.md)
- [src-fcv-006 deep extraction round 1](src-fcv-006-deep-extraction-round1.md)
- [src-fcv-007 deep extraction round 1](src-fcv-007-deep-extraction-round1.md)
- [src-fcv-008 deep extraction round 1](src-fcv-008-deep-extraction-round1.md)
- [src-fcv-009 deep extraction round 1](src-fcv-009-deep-extraction-round1.md)
- [src-fcv-010 deep extraction round 1](src-fcv-010-deep-extraction-round1.md)
- [src-fcv-011 deep extraction round 1](src-fcv-011-deep-extraction-round1.md)
- [src-fcv-012 deep extraction round 1](src-fcv-012-deep-extraction-round1.md)
- [src-fcv-014 deep extraction round 1](src-fcv-014-deep-extraction-round1.md)
- [src-fcv-015 deep extraction round 1](src-fcv-015-deep-extraction-round1.md)
- [src-fcv-017 deep extraction round 1](src-fcv-017-deep-extraction-round1.md)
- [src-fcv-018 deep extraction round 1](src-fcv-018-deep-extraction-round1.md)
- [src-fcv-020 deep extraction round 1](src-fcv-020-deep-extraction-round1.md)
- [src-fcv-021 deep extraction round 1](src-fcv-021-deep-extraction-round1.md)
- [src-fcv-022 deep extraction round 1](src-fcv-022-deep-extraction-round1.md)
- [FCV mechanism-control memo](fcv-mechanism-control-memo.md)
- [FCV recognition architecture memo](fcv-recognition-architecture-memo.md)
- [FCV vaccine-persistence boundary memo](fcv-vaccine-persistence-boundary-memo.md)
