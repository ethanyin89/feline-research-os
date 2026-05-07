# Deep Extraction Worksheet

Source: `src-fcv-006`  
Title: `Feline calicivirus and other respiratory pathogens in cats with Feline calicivirus-related symptoms and in clinically healthy cats in Switzerland`  
Method note: this worksheet is based on accessible abstract/full-page summary text from the open-access article landing pages, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The study tests FCV suspicion against reality

- core_claim: the paper compares FCV-suspect cats with healthy cats to see how often FCV is actually present and which factors shape that presence.
- implicit_premise: FCV-compatible symptoms should be tested against carrier-state and co-pathogen reality.
- relation_to_previous: opening recognition-control question.
- hard_details: 200 FCV-suspect cats and 100 healthy cats from 19 Swiss cantons were sampled in 24 veterinary practices.
- tension_or_surprise: the design is stronger than a simple symptomatic case series because healthy controls are built in.

#### Unit 2: FCV is common in suspect cats, but far from universal

- core_claim: FCV PCR prevalence was 45% in FCV-suspect cats and 8% in healthy cats.
- implicit_premise: FCV clinical suspicion is meaningful but not confirmatory.
- relation_to_previous: turns the design into a recognition boundary.
- hard_details: the abstract also reports FHV-1 20%/9%, C. felis 8%/1%, B. bronchiseptica 4%/2%, M. felis 47%/31%, and co-infections 40%/14% in suspect/healthy cats.
- tension_or_surprise: less than half of practitioner-judged FCV-suspect cats were FCV-positive by PCR.

#### Unit 3: Co-pathogen structure is not optional

- core_claim: respiratory-pathogen interpretation needs FCV, FHV-1, Mycoplasma felis, Chlamydophila felis, and Bordetella bronchiseptica in the same frame.
- implicit_premise: FCV cannot be interpreted as a stand-alone respiratory syndrome owner.
- relation_to_previous: explains why symptomatic judgment alone underperforms.
- hard_details: multivariable models identified co-infection with M. felis as a risk factor signal among FCV-suspect cats.
- tension_or_surprise: M. felis pressure is large enough that the paper naturally becomes a co-pathogen-control anchor.

#### Unit 4: Housing and intact status matter

- core_claim: group housing and intact reproductive status were associated with FCV infection, in both suspect and healthy cats.
- implicit_premise: FCV epidemiology is structured by multi-cat exposure conditions, not only by symptoms.
- relation_to_previous: extends recognition into risk architecture.
- hard_details: among suspect cats, group housing had OR 2.11 and intact status OR 1.80; among healthy cats, group housing had OR 46.4 and intact status OR 22.2.
- tension_or_surprise: the healthy-cat branch is epidemiologically important, not just a nuisance finding.

#### Unit 5: The sign profile is more oral than classical URTD

- core_claim: oral ulcerations, salivation, gingivitis, and stomatitis were significantly associated with FCV infection, while classical URTD signs were not.
- implicit_premise: FCV recognition should not flatten oral disease and respiratory disease into one equal-weight symptom list.
- relation_to_previous: gives a sharper clinical recognition boundary.
- hard_details: the article summary explicitly says classical sneezing and nasal/ocular discharge were not the discriminating signals.
- tension_or_surprise: this is one of the strongest current FCV sources against `cat flu signs = FCV` shorthand.

## Phase 1: Theme Reconstruction

## Theme: FCV suspicion needs recalibration

This paper is one of the best recognition-control anchors in the FCV seed set because it shows that practitioner FCV suspicion only partially overlaps with FCV detection.

### Hard Information

- FCV PCR prevalence 45% in suspect cats
- FCV PCR prevalence 8% in healthy cats
- FCV-positive healthy cats confirm asymptomatic-carrier relevance

## Theme: Co-pathogens and group housing are structural

The paper makes FCV recognition population-aware. Multi-cat settings and co-pathogens are not downstream complications; they shape the front-door interpretation.

### Hard Information

- M. felis signal present in both populations
- co-infections detected in 40% of suspect and 14% of healthy cats
- group housing associated with FCV infection in both suspect and healthy cats

## Theme: Oral disease signals outrank classical URTD signs for FCV association

This matters because many downstream readers will default to a generic upper-respiratory frame. The study says that is too broad.

### Hard Information

- oral ulcerations, salivation, gingivitis, and stomatitis were significantly associated with FCV infection
- classical URTD signs were not significantly associated

## Phase 2: Claim-Evidence Structure

### Recognition-Epidemiology Key Points

**Claim 1**
- support: FCV was found in fewer than half of FCV-suspect cats and in some healthy cats
- details: 45% in suspect cats, 8% in healthy cats
- implicit_premise: symptom-based suspicion and virologic detection should remain separated

**Claim 2**
- support: co-pathogens and co-infections were common
- details: FHV-1, M. felis, C. felis, B. bronchiseptica, and co-infection rates were all reported
- implicit_premise: FCV recognition belongs in a respiratory-pathogen network, not as a stand-alone syndrome owner

**Claim 3**
- support: oral lesion/stomatitis-style findings were associated with FCV, while classical URTD signs were not
- details: oral ulcerations, salivation, gingivitis, stomatitis significant; classical URTD signs not significant
- implicit_premise: recognition ordering should be recalibrated toward oral-disease-heavy interpretation

### Boundary-Setting Key Points

**Claim 1**
- support: this is a Swiss field study
- details: 19 cantons, 24 practices
- implicit_premise: epidemiologic architecture is portable; prevalence values are not universally portable

**Claim 2**
- support: vaccination showed an apparent protective association in a univariable approach
- details: suspect cats were significantly less often FCV-positive when vaccinated
- implicit_premise: the study supports vaccination as a control tool, but not a complete protection claim

## Phase 2.5: Write-Back Implications

### For `topics/fcv/risk-and-recognition.md`

- elevate oral disease signals above a flat classical-URTD list
- keep healthy shedding and co-pathogen structure explicit

### For `system/indexes/fcv-recognition-architecture-memo.md`

- this becomes the first deep-extracted epidemiology/control anchor

### For `topics/fcv/current-state-dashboard.md`

- recognition branch can now be described as having one deep-extracted field anchor, not only source-checked cards

## Phase 3: Promotion Check

- source_card_updates:
  - preserve suspect-vs-healthy comparison
  - preserve oral-disease-heavy recognition signal
  - preserve co-pathogen and group-housing architecture
- topic_write_back_targets:
  - `topics/fcv/risk-and-recognition.md`
  - `topics/fcv/current-state-dashboard.md`
  - `system/indexes/fcv-recognition-architecture-memo.md`
  - `topics/fcv/index.md`
- not_safe_to_promote_yet:
  - any universal prevalence claim
  - any statement that URTD signs alone are sufficient for FCV diagnosis
  - any vaccine-effectiveness ranking beyond bounded protective association
- conflicts_with_existing_vault:
  - none; this worksheet sharpens the current recognition architecture
