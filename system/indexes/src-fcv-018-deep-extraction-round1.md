# Deep Extraction Worksheet

Source: `src-fcv-018`  
Title: `Identification of prevalent Feline Calicivirus strains and novel antiviral efficacy of CpG49 stimulus in Feline Calicivirus-infected cats`  
Method note: this worksheet is based on the PubMed abstract, article-summary metadata, and the current source card rather than a full section-by-section extraction of the complete article PDF.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: This paper is a therapy paper with a real in vivo branch, not only another FCV prevention paper

- core_claim: the study builds an infection model from a prevalent clinical FCV strain and tests CpG49 as an active therapy.
- implicit_premise: FCV literature is not only about vaccines once a paper reports treatment-linked recovery and shedding change in infected cats.
- relation_to_previous: opening branch upgrade.
- hard_details: the preserved abstract says the model used the prevalent strain `FG24-1` isolated from clinical samples.
- tension_or_surprise: the paper matters because it moves from prevention-heavy FCV literature into treatment.

#### Unit 2: The therapy signal is immunologic and antiviral at the same time

- core_claim: CpG49 acts through Th1-biased interferon stimulation and replication inhibition rather than through generic supportive care language.
- implicit_premise: the FCV therapy branch should be written as immune-modulation plus antiviral pressure, not as symptom care alone.
- relation_to_previous: explains why the paper is structurally stronger than a generic treatment note.
- hard_details: the preserved abstract reports type I and II interferon responses and significant inhibition of FCV replication in vitro and in vivo.
- tension_or_surprise: the paper is not just clinically descriptive; it gives a mechanistic route for the treatment signal.

#### Unit 3: The paper connects immune activation to recovery and shedding endpoints

- core_claim: the value of the study is the linked endpoint package rather than any one biomarker alone.
- implicit_premise: FCV treatment evidence becomes more reusable when inflammation, symptoms, and shedding move in the same direction.
- relation_to_previous: sharpens the endpoint architecture.
- hard_details: the preserved abstract reports up to `40.38%` lower fSAA, up to `2.14-fold` higher IFN-gamma, `3-day` shorter oral-inflammation recovery, `2-day` less fever, and lower shedding on days 6 and 9.
- tension_or_surprise: this is stronger than in vitro antiviral screening because it changes both clinical course and shedding.

#### Unit 4: A strong in vivo therapy signal is still not routine-care authority

- core_claim: the paper supports a real treatment branch, but not standard-of-care language.
- implicit_premise: one modern in vivo study can create branch legitimacy without settling comparative therapy hierarchy.
- relation_to_previous: sets the control ceiling.
- hard_details: the current preserved layer does not provide replicated comparative trials, broad population validation, or product-level practice guidance.
- tension_or_surprise: the paper sounds close to a treatment answer, but the safe downstream role is still bounded.

#### Unit 5: This paper should own the first in vivo therapeutic anchor in the FCV module

- core_claim: `src-fcv-018` should become the default source when the module needs to show FCV has moved beyond purely exploratory in vitro treatment ideas.
- implicit_premise: therapy branches drift into hand-wavy optimism unless one paper clearly owns the first in vivo signal.
- relation_to_previous: assigns durable module role.
- hard_details: this paper naturally pairs with `src-fcv-008` for strain-sensitive interferon caution and `src-fcv-014` for assay-stage discovery below clinical translation.
- tension_or_surprise: the right use is not `CpG49 is the answer`, but `the FCV therapy branch now has a real in vivo anchor`.

## Phase 1: Theme Reconstruction

## Theme: FCV now has a real in vivo therapeutic branch

This paper upgrades the FCV therapy layer from preclinical possibility into a true in vivo branch. It supports saying that treatment-focused FCV writing no longer has to stop at supportive care or screening assays.

### Hard Information

- infection model built with the prevalent clinical strain `FG24-1`
- CpG49 tested therapeutically against FCV infection
- in vitro and in vivo replication inhibition reported

## Theme: The strongest signal is a linked endpoint package

The study matters because immune, inflammatory, symptomatic, and shedding endpoints move together. That makes the treatment branch more reusable than a one-number antiviral paper.

### Hard Information

- up to `40.38%` lower fSAA
- up to `2.14-fold` higher IFN-gamma
- `3-day` shorter oral-inflammation recovery
- `2-day` less fever duration
- `53.4%` lower shedding on day 6 and `97.4%` lower on day 9

## Theme: Treatment optimism still needs a hard ceiling

The paper is structurally important, but it does not justify routine protocol language, final treatment ranking, or broad control claims.

### Hard Information

- one current study
- abstract-led extraction
- no replicated comparative treatment hierarchy preserved in the current source layer

## Phase 2: Claim-Evidence Structure

### Therapy-Branch Key Points

**Claim 1**
- support: the source reports an infection model using the prevalent clinical strain `FG24-1`
- details: current clinical-strain model rather than only cell-line screening
- implicit_premise: this belongs above pure assay-stage therapy discussion

**Claim 2**
- support: CpG49 elicited Th1-biased interferon responses and inhibited FCV replication in vitro and in vivo
- details: type I and II interferon response language is explicit in the preserved abstract
- implicit_premise: the therapy signal is mechanistically structured, not only symptomatic

**Claim 3**
- support: lower fSAA, higher IFN-gamma, faster symptom recovery, and lower viral shedding all move in the same direction
- details: inflammatory, clinical, and shedding endpoints all improved
- implicit_premise: this is the current best first in vivo FCV treatment anchor in the seed set

### Boundary-Setting Key Points

**Claim 1**
- support: the paper is still one study and the current extraction is abstract-led
- details: no broad replicated therapy hierarchy is yet preserved in the vault
- implicit_premise: do not promote CpG49 into routine-care authority

**Claim 2**
- support: this source is a therapeutic branch paper, not a vaccine or carrier-state control paper
- details: shedding reduction matters, but it does not answer the whole persistence or population-control question
- implicit_premise: treatment benefit should not be collapsed into vaccine-control language

## Phase 2.5: Write-Back Implications

### For `topics/fcv/translation-brief.md`

- this becomes the first deep-extracted in vivo therapeutic anchor in the FCV translation layer

### For `topics/fcv/current-state-dashboard.md`

- the therapy / antiviral frontier can now be described as having one deep-extracted in vivo anchor plus lower-tier exploratory papers

### For `system/indexes/fcv-source-depth-map.md`

- `src-fcv-018` should move from partial/source_checked into full/deep_extracted

### For `topics/fcv/endpoint-handbook.md`

- the handbook can now acknowledge a therapeutic endpoint branch around clinical recovery and shedding reduction without turning that branch into treatment guidance

## Phase 3: Promotion Check

- source_card_updates:
  - preserve first in vivo therapy-anchor authority
  - preserve linked immune/inflammation/recovery/shedding endpoint package
  - preserve anti-standard-of-care and anti-ranking boundaries
- topic_write_back_targets:
  - `topics/fcv/translation-brief.md`
  - `topics/fcv/current-state-dashboard.md`
  - `system/indexes/fcv-source-depth-map.md`
  - `topics/fcv/endpoint-handbook.md`
- not_safe_to_promote_yet:
  - any routine treatment recommendation
  - any claim that one CpG49 study settles FCV therapy hierarchy
  - any statement that therapeutic shedding reduction solves broader persistence/control questions
- conflicts_with_existing_vault:
  - none; this worksheet upgrades the FCV therapy branch from exploratory possibility to a real but bounded in vivo branch
