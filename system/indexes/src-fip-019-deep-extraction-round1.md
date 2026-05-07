# Deep Extraction Worksheet

Source: `src-fip-019`  
Title: `Thirty-two cats with effusive or non-effusive feline infectious peritonitis treated with a combination of remdesivir and GS-441524`  
Method note: this worksheet is based on accessible abstract-level treatment details already captured in the source card, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The paper is about a treatment package, not a single-drug baseline

- core_claim: this study describes protocols, responses, and outcomes for a combined remdesivir plus GS-441524 strategy.
- implicit_premise: once FIP treatment enters real-world practice, the relevant object is often a package or protocol rather than one isolated molecule.
- relation_to_previous: opening distinction from the earlier GS-only anchor.
- hard_details: the abstract explicitly describes injectable remdesivir and oral GS-441524.
- tension_or_surprise: this is already a different translational object from the baseline GS-441524 efficacy paper.

#### Unit 2: The cohort is broader and more practice-like than the first GS anchor

- core_claim: the study includes effusive and non-effusive FIP, plus ocular and neurologic involvement.
- implicit_premise: real-world treatment package logic matters most when it begins to cross disease-form boundaries.
- relation_to_previous: moves from protocol type to case-mix meaning.
- hard_details: the abstract reports ocular and neurological involvement within the 32-cat cohort.
- tension_or_surprise: this paper begins to widen the treatment branch beyond the exclusions in `src-fip-016`.

#### Unit 3: The outcomes are strong, but the design remains retrospective case-series evidence

- core_claim: the study reports high clinical response and remission rates, but still remains a retrospective series rather than comparative proof.
- implicit_premise: real-world effectiveness and definitive efficacy hierarchy are different claims.
- relation_to_previous: moves from case mix to evidence strength.
- hard_details: clinical response in 28 of 32 cats; remission at 12 weeks in 26 of 32 cats; 81.3% alive and in remission at 12 weeks.
- tension_or_surprise: the practical signal is strong, but the design still resists simple ranking claims.

#### Unit 4: Speed of response is part of the practical story

- core_claim: this paper adds operational detail about how quickly treatment response may become visible.
- implicit_premise: response tempo matters when a treatment branch moves from experimental promise into real management.
- relation_to_previous: expands from outcome proportion to treatment dynamics.
- hard_details: median clinical response was observed in 2 days.
- tension_or_surprise: this makes the treatment-package story more clinically tangible than a pure long-horizon remission paper.

#### Unit 5: This paper should sit between baseline efficacy and neurologic-complexity papers

- core_claim: the right role of this paper is to bridge `baseline GS efficacy` and `neurologic/high-complexity treatment`.
- implicit_premise: FIP treatment architecture needs an intermediate layer for real-world mixed-form management.
- relation_to_previous: defines placement in the treatment branch.
- hard_details: the cohort includes ocular and neurologic involvement, but the paper is still not exclusively a neurologic-treatment study.
- tension_or_surprise: this is probably the paper that keeps the treatment branch from staying too clean and too simple.

## Phase 1: Theme Reconstruction

## Theme: Real-world treatment package logic is now a separate evidence branch

This paper makes it clear that the FIP treatment branch cannot stay at the level of one foundational GS-441524 efficacy study. Real clinical management has already moved into protocol packages and mixed-form disease handling.

### Hard Information

- injectable remdesivir plus oral GS-441524
- 32-cat series
- retrospective outcome description

## Theme: Broader case mix changes what can be discussed

Compared with the baseline natural-disease GS paper, this study matters because it includes a more heterogeneous practical cohort, including ocular and neurologic involvement.

### Hard Information

- effusive and non-effusive FIP included
- ocular involvement included
- neurologic involvement included

## Theme: Strong practical signal does not equal definitive hierarchy proof

The paper strongly supports the practical importance of combined-treatment protocols, but it should not be rewritten as the final proof that one package is best.

### Hard Information

- clinical response: 28/32
- remission at 12 weeks: 26/32
- retrospective case-series design

## Phase 2: Claim-Evidence Structure

### Treatment-Package Key Points

**Claim 1**
- support: the study describes remdesivir plus GS-441524 protocols with outcome reporting
- details: this is a package-level treatment paper rather than a single-drug baseline
- implicit_premise: modern FIP treatment architecture needs a treatment-package layer

**Claim 2**
- support: the cohort includes ocular and neurologic involvement
- details: the case mix is broader than the baseline GS efficacy anchor
- implicit_premise: the paper helps widen the treatment branch beyond simpler form boundaries

**Claim 3**
- support: the study reports rapid response and high remission proportions
- details: median response in 2 days; remission at 12 weeks in 26/32 cats
- implicit_premise: the treatment branch now has strong real-world practical signal

### Boundary-Setting Key Points

**Claim 1**
- support: the study is a retrospective case series
- details: design strength is below comparative efficacy proof
- implicit_premise: package logic should not be promoted into final hierarchy certainty

**Claim 2**
- support: this is a mixed-form practical cohort, not a clean single-form controlled dataset
- details: broad inclusion helps realism but complicates direct comparison
- implicit_premise: practical breadth and methodological cleanliness trade off against each other

## Phase 2.5: Write-Back Implications

### For `topics/fip/translation-brief.md`

- add a distinction between `single-drug baseline anchor` and `real-world treatment package anchor`
- keep package logic important without overflattening the branch

### For `topics/fip/synthesis-index.md`

- add a fourth stabilizing rule:
  - baseline GS efficacy is one layer
  - remdesivir-plus-GS package logic is a second, more practice-like layer

### For later FIP treatment memo

- compare `src-fip-016`, `src-fip-019`, and `src-fip-024` as three different treatment objects

## Phase 3: Promotion Check

- source_card_updates:
  - preserve package-level framing
  - preserve retrospective case-series caution
  - preserve wider case-mix meaning
- topic_write_back_targets:
  - `topics/fip/translation-brief.md`
  - `topics/fip/synthesis-index.md`
  - `topics/fip/current-state-dashboard.md`
  - `system/indexes/fip-source-index.md`
- not_safe_to_promote_yet:
  - any claim that this paper definitively proves the best treatment protocol
  - any claim that this package paper replaces the need for neurologic-specific treatment evidence
  - any claim that broad real-world case mix removes methodological uncertainty
- conflicts_with_existing_vault:
  - none; this worksheet adds a second treatment layer rather than contradicting the baseline GS anchor

