# Deep Extraction Worksheet

Source: `src-fcv-008`  
Title: `Sensitivity of FCV to recombinant feline interferon (rFeIFN)`  
Method note: this worksheet is based on accessible abstract and summary text from source landing pages and the current source card, not a full section-by-section extraction of the complete article PDF.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: This paper is a therapy-boundary paper, not a treatment-success paper

- core_claim: the study measures how 47 FCV field isolates vary in sensitivity to recombinant feline interferon.
- implicit_premise: the first therapy question is not only `does interferon work`, but `how variable is response across strains`.
- relation_to_previous: opening branch control.
- hard_details: the preserved abstract reports `47` field isolates and a sensitivity range summarized by log `PDD50`.
- tension_or_surprise: this paper is structurally valuable because it blocks oversimplified optimism.

#### Unit 2: Most strains cluster, but the outliers matter

- core_claim: sensitivity values were distributed around a moderate middle rather than collapsing into one common response class.
- implicit_premise: FCV therapy language should keep room for low- and high-sensitivity tails.
- relation_to_previous: sharpens the heterogeneity read.
- hard_details: the preserved abstract reports log `PDD50` values from `1.1` to `3.7`, mean `2.3 +/- 0.64`, with `68.3%` in the moderate range.
- tension_or_surprise: the middle dominates, but the therapeutic story is defined by the spread.

#### Unit 3: Vaccine-breakdown and interferon sensitivity are not the same problem

- core_claim: vaccine-breakdown status did not map cleanly onto interferon sensitivity.
- implicit_premise: prevention failure and treatment responsiveness should remain separate control layers.
- relation_to_previous: sets a critical anti-collapse boundary.
- hard_details: among `15` vaccine-breakdown strains, some were highly sensitive while `Fukuoka-9` was low sensitivity.
- tension_or_surprise: the paper is useful precisely because the expected shortcut does not hold.

#### Unit 4: Sequence differences may matter at the low-sensitivity edge

- core_claim: the low-sensitivity `Fukuoka-9` strain carried specific amino-acid changes.
- implicit_premise: therapy heterogeneity may have a sequence-level explanation rather than being random noise.
- relation_to_previous: adds a mechanism bridge.
- hard_details: the preserved abstract explicitly links amino-acid changes to the low-sensitivity strain.
- tension_or_surprise: even this older therapy paper hints that sequence-aware treatment thinking may matter.

#### Unit 5: This source should own the interferon-caution branch inside FCV therapy writing

- core_claim: `src-fcv-008` should become the default caution anchor whenever recombinant interferon is mentioned in FCV treatment prose.
- implicit_premise: therapy branches need one source that defines the overclaim boundary.
- relation_to_previous: assigns durable module role.
- hard_details: this source naturally pairs with `src-fcv-014` below it and `src-fcv-018` above it.
- tension_or_surprise: the right use is not `interferon failed` or `interferon succeeded`, but `interferon response is heterogeneous and strain-sensitive`.

## Phase 1: Theme Reconstruction

## Theme: FCV interferon response is heterogeneous

This paper upgrades recombinant interferon from a generic therapy idea into a heterogeneous response problem. It supports a treatment branch that is real, but not uniform.

### Hard Information

- `47` field isolates tested
- log `PDD50` range `1.1` to `3.7`
- mean `2.3 +/- 0.64`

## Theme: The moderate center does not erase meaningful outliers

Most strains cluster in a moderate range, but the low- and high-sensitivity tails are exactly what stop flat treatment language.

### Hard Information

- `68.3%` of values in the moderate range
- low- and high-sensitivity groups explicitly defined

## Theme: Vaccine-break logic and treatment-response logic must stay separate

The study is especially valuable because it breaks the temptation to infer drug response from vaccine-breakdown language.

### Hard Information

- `15` vaccine-breakdown strains assessed
- mixed sensitivity among those strains
- no clear association between vaccine-breakdown status and interferon sensitivity

## Phase 2: Claim-Evidence Structure

### Therapy-Boundary Key Points

**Claim 1**
- support: sensitivity was measured across `47` field isolates with a broad log `PDD50` range
- details: `1.1` to `3.7`, mean `2.3 +/- 0.64`
- implicit_premise: recombinant interferon response is not one flat antiviral class effect

**Claim 2**
- support: most isolates clustered in a moderate range but low- and high-sensitivity outliers remained
- details: `68.3%` within the mean +/- standard deviation band
- implicit_premise: FCV therapy writing should preserve the tails, not only the average

**Claim 3**
- support: vaccine-breakdown strains showed mixed interferon sensitivity
- details: some high, some low, no simple mapping
- implicit_premise: prevention failure and therapy response must not be conflated

### Boundary-Setting Key Points

**Claim 1**
- support: this is an isolate-sensitivity paper, not a naturally infected clinical trial
- details: antiviral response classification rather than patient recovery outcomes
- implicit_premise: do not promote this source into routine treatment guidance

**Claim 2**
- support: sequence changes were identified in the low-sensitivity `Fukuoka-9` strain
- details: mechanism hint, not finished predictive biomarker logic
- implicit_premise: sequence-aware therapy thinking is plausible, but not operationally settled

## Phase 2.5: Write-Back Implications

### For `topics/fcv/translation-brief.md`

- this becomes the first deep-extracted interferon-sensitivity caution anchor under the FCV therapy branch

### For `topics/fcv/current-state-dashboard.md`

- the therapy row can now distinguish `first in vivo anchor` from `strain-sensitive interferon caution`

### For `system/indexes/fcv-source-depth-map.md`

- `src-fcv-008` should move from partial/source_checked into full/deep_extracted

## Phase 3: Promotion Check

- source_card_updates:
  - preserve interferon-response heterogeneity
  - preserve vaccine-break-versus-treatment-response separation
  - preserve anti-clinical-overclaim boundary
- topic_write_back_targets:
  - `topics/fcv/translation-brief.md`
  - `topics/fcv/current-state-dashboard.md`
  - `system/indexes/fcv-source-depth-map.md`
  - `system/indexes/fcv-source-index.md`
- not_safe_to_promote_yet:
  - any clinical-efficacy recommendation for recombinant interferon
  - any shortcut from vaccine failure to interferon resistance
  - any statement that sequence differences already provide a usable treatment biomarker
- conflicts_with_existing_vault:
  - none; this worksheet gives the FCV therapy branch a stronger control anchor against overclaim
