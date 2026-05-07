# Deep Extraction Worksheet

Source: `src-fcv-017`  
Title: `Mechanisms for persistence of acute and chronic feline calicivirus infections in the face of vaccination`  
Method note: this worksheet is based on accessible PubMed abstract text plus existing source-card metadata, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The paper is about persistence, not just vaccine performance

- core_claim: this study asks why acute disease, chronic disease, and sustained oral carriage persist despite routine FCV vaccination.
- implicit_premise: FCV control failure is not reducible to one vaccine-efficacy number.
- relation_to_previous: opening control problem.
- hard_details: the abstract explicitly frames persistence of acute and chronic FCV-induced disease plus sustained oral carriage.
- tension_or_surprise: the paper starts from epidemiologic durability, not from a simple efficacy comparison.

#### Unit 2: Broad cross-reactivity does not solve the field problem

- core_claim: the original F9 strain still generated cross-reactive antibodies against almost all examined California field strains, and whole inactivated FCV-2280 also showed broad cross-reactivity.
- implicit_premise: vaccine breadth can be real while epidemiologic persistence still remains.
- relation_to_previous: separates breadth from field resolution.
- hard_details: the abstract distinguishes original F9 from some derived vaccine strains and states broad neutralizing reactivity for F9 and FCV-2280.
- tension_or_surprise: persistence survives even when cross-reactivity looks broad.

#### Unit 3: Vaccine-derived viruses and within-host change matter

- core_claim: orally administered vaccine strains caused acute disease signs and prolonged oral shedding, and post-inoculation oral isolates could differ from parental virus and appear more vaccine resistant.
- implicit_premise: vaccine-virus behavior can itself be part of the persistence story.
- relation_to_previous: moves from serology to within-host/within-lineage dynamics.
- hard_details: the abstract mentions oral administration, protracted shedding, and oral isolates differing from parental virus five to ten weeks later.
- tension_or_surprise: the paper does not let the module place all blame on field-virus escape alone.

#### Unit 4: Prior exposure reduces severity but not chronic-carrier state

- core_claim: cats previously infected with field or vaccine strains developed much less severe acute illness after heterologous challenge but were not protected against the chronic carrier state.
- implicit_premise: acute-disease reduction and chronic-carrier prevention are different endpoint families.
- relation_to_previous: defines the main endpoint boundary the module needs.
- hard_details: heterologous challenge, milder acute illness, and failure to prevent chronic carriage are all explicit in the abstract.
- tension_or_surprise: this is the strongest single reason not to flatten FCV vaccine benefit into total control.

#### Unit 5: Persistence is multi-causal

- core_claim: field persistence cannot be explained solely by vaccine-resistant strain emergence; vaccine virus itself may contribute to both acute and chronic infection and disease.
- implicit_premise: FCV persistence is a systems problem.
- relation_to_previous: integrates the whole branch.
- hard_details: the abstract closes with a multi-cause interpretation rather than a single escape-mutation answer.
- tension_or_surprise: this paper is structurally more important than a conventional vaccine-comparison study.

## Phase 1: Theme Reconstruction

## Theme: Breadth and persistence must be separated

This paper is the main FCV source preventing broad neutralisation from being misread as chronic-carrier control. It upgrades `disease mitigation vs persistence` into a first-order architectural split.

### Hard Information

- original FCV-F9 remained broadly cross-reactive against almost all examined California field strains
- whole inactivated FCV-2280 also evoked broadly cross-reactive neutralising antibodies
- previously infected cats were not protected against the chronic carrier state

## Theme: Vaccine-virus behavior belongs inside the control model

The paper does not frame persistence as only a field-strain escape problem. It also keeps vaccine-virus shedding and post-inoculation viral change visible.

### Hard Information

- vaccine strains caused acute disease signs when administered orally
- protracted oral shedding occurred
- isolates collected five to ten weeks later could differ from parental virus and appear more vaccine resistant

## Theme: FCV control is a systems problem

This paper is not just older historical context. It is a systems-control anchor because it ties together serologic breadth, within-host change, shedding, challenge outcomes, and carriage.

### Hard Information

- heterologous challenge after prior exposure reduced acute illness severity
- persistence in the field could not be explained solely by vaccine-resistant strains

## Phase 2: Claim-Evidence Structure

### Vaccine-Persistence Key Points

**Claim 1**
- support: broad cross-reactive antibody generation was still observed for core vaccine strains
- details: original F9 and inactivated FCV-2280 retained broad neutralising profiles in the reported setting
- implicit_premise: vaccine breadth is real and should not be erased

**Claim 2**
- support: vaccine breadth did not prevent chronic carrier-state persistence
- details: prior infection reduced acute illness but did not protect against chronic carriage
- implicit_premise: endpoint separation is mandatory

**Claim 3**
- support: vaccine-virus shedding and later oral isolates with altered resistance profiles were observed
- details: post-inoculation isolates collected five to ten weeks later could differ from parental virus
- implicit_premise: FCV persistence is partly a within-host evolutionary problem

### Boundary-Setting Key Points

**Claim 1**
- support: the study is California-centered and older
- details: geography and time limit direct present-day prevalence generalization
- implicit_premise: the paper is architecture-defining, not a current product-comparison result

**Claim 2**
- support: the paper studies persistence mechanisms in the face of vaccination rather than current-market vaccine labels
- details: conclusions belong to control architecture, not to current product selection
- implicit_premise: do not turn this source into a commercial vaccine ranking

## Phase 2.5: Write-Back Implications

### For `topics/fcv/endpoint-handbook.md`

- keep acute-disease mitigation and chronic-carrier prevention in separate endpoint buckets
- keep serology and neutralisation below persistence-aware interpretation

### For `topics/fcv/translation-brief.md`

- keep vaccine language at disease reduction and control architecture rather than infection elimination

### For `system/indexes/fcv-vaccine-persistence-boundary-memo.md`

- this worksheet becomes the first deep-extracted anchor for the memo's persistence-control claims

## Phase 3: Promotion Check

- source_card_updates:
  - preserve broad-but-incomplete coverage logic
  - preserve vaccine-virus shedding and within-host change logic
  - preserve acute-disease-vs-carriage endpoint separation
- topic_write_back_targets:
  - `topics/fcv/endpoint-handbook.md`
  - `topics/fcv/translation-brief.md`
  - `topics/fcv/current-state-dashboard.md`
  - `system/indexes/fcv-vaccine-persistence-boundary-memo.md`
- not_safe_to_promote_yet:
  - any current-market vaccine superiority claim
  - any claim that broad neutralisation solves field persistence
  - any statement that persistence is explained only by vaccine escape
- conflicts_with_existing_vault:
  - none; this worksheet strengthens the existing boundary architecture
