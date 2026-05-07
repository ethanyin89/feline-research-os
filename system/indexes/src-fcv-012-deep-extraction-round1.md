# Deep Extraction Worksheet

Source: `src-fcv-012`  
Title: `Use of serologic tests to predict resistance to feline herpesvirus 1, feline calicivirus, and feline parvovirus infection in cats`  
Method note: this worksheet is based on the PubMed abstract and mirrored abstract sources rather than a full section-by-section extraction of the complete article.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: This paper is a serology-boundary paper, not a vaccination-policy paper

- core_claim: the study tests whether virus-specific serum antibodies correlate with resistance to challenge in vaccinated cats and how common detectable antibodies are in client-owned cats.
- implicit_premise: FCV serology should be treated as an endpoint interpretation problem before it becomes a policy question.
- relation_to_previous: opening branch placement.
- hard_details: the abstract reports 72 laboratory-reared cats and 276 client-owned cats.
- tension_or_surprise: the paper matters because it gives FCV a real serology branch without automatically rewriting vaccination policy.

#### Unit 2: FCV ELISA performed strongly in vaccinated laboratory cats

- core_claim: positive FCV ELISA results were highly predictive of resistance in the vaccinated challenge cohort.
- implicit_premise: antibody detection can be clinically informative without becoming absolute.
- relation_to_previous: sharpens the useful part of the paper.
- hard_details: the abstract reports a positive predictive value of 100% for the FCV ELISA in vaccinated laboratory-reared cats.
- tension_or_surprise: this is unusually strong endpoint language, but it is still bounded by study frame.

#### Unit 3: The client-owned-cat population had widespread detectable FCV antibodies

- core_claim: most client-owned cats in the sampled population were FCV ELISA positive.
- implicit_premise: fixed booster routines may not map cleanly onto actual antibody distribution in the population.
- relation_to_previous: explains why policy pressure appears.
- hard_details: the abstract reports 255 of 276 client-owned cats, or 92.4%, were positive by FCV ELISA.
- tension_or_surprise: the policy question appears because antibody prevalence is high, not because vaccination becomes unimportant.

#### Unit 4: Arbitrary boosters are the target, not vaccination itself

- core_claim: the paper challenges arbitrary booster intervals, not vaccination as a whole.
- implicit_premise: the correct downstream sentence is `booster timing deserves evidence`, not `vaccines are unnecessary`.
- relation_to_previous: sets the overclaim boundary.
- hard_details: the abstract says arbitrary booster intervals are likely to lead to unnecessary vaccination of some cats.
- tension_or_surprise: this is exactly the kind of sentence that gets overpromoted if the branch is not controlled.

#### Unit 5: This source should own the FCV serology-resistance endpoint branch

- core_claim: `src-fcv-012` should become the default source when the module needs to explain how antibody detection fits under FCV endpoint logic.
- implicit_premise: without one owner paper, serology drifts into either overclaim or irrelevance.
- relation_to_previous: assigns durable role.
- hard_details: this card pairs naturally with `src-fcv-017` to block persistence overclaim and with `src-fcv-009` to keep top-layer control language broader than serology alone.
- tension_or_surprise: the right use is not `ELISA tells you the whole answer`, but `ELISA can be predictive in vaccinated cats while still sitting below policy authority`.

## Phase 1: Theme Reconstruction

## Theme: FCV now has a real serology-resistance endpoint branch

This paper upgrades FCV serology from a generic antibody note into a true endpoint layer. It supports saying that antibody detection can help predict resistance in vaccinated cats.

### Hard Information

- `72` laboratory-reared cats
- `276` client-owned cats
- vaccinated cats challenged `9 to 36 months` after vaccination

## Theme: Strong predictive performance does not eliminate boundary work

The paper is strongest when its positive predictive value is kept inside the study frame rather than generalized into universal protection claims.

### Hard Information

- FCV ELISA positive predictive value `100%` in vaccinated laboratory cats
- client-owned-cat FCV seropositivity `92.4%`

## Theme: The policy pressure is about arbitrary intervals

The study pushes on routine booster timing, not on vaccination itself.

### Hard Information

- arbitrary booster intervals likely to lead to unnecessary vaccination of some cats

## Phase 2: Claim-Evidence Structure

### Serology-Endpoint Key Points

**Claim 1**
- support: positive FCV ELISA results had a reported predictive value of `100%` in vaccinated laboratory-reared cats
- details: challenge-based vaccinated-cat study frame
- implicit_premise: serology can meaningfully inform resistance prediction

**Claim 2**
- support: 255 of 276 client-owned cats were FCV ELISA positive
- details: `92.4%` positivity
- implicit_premise: population antibody prevalence changes how arbitrary boosters should be read

**Claim 3**
- support: the authors explicitly question arbitrary booster intervals
- details: unnecessary vaccination concern
- implicit_premise: evidence-based booster logic is narrower than anti-vaccination rhetoric

### Boundary-Setting Key Points

**Claim 1**
- support: the predictive result is for vaccinated laboratory-reared cats
- details: not every real-world population, not every immune context
- implicit_premise: do not universalize the predictive value

**Claim 2**
- support: the paper studies resistance prediction, not sterilizing immunity or chronic-carrier prevention
- details: endpoint branch, not whole-program control answer
- implicit_premise: serology must stay below persistence and control architecture

## Phase 2.5: Write-Back Implications

### For `topics/fcv/endpoint-handbook.md`

- this becomes the first deep-extracted serology-resistance anchor in the endpoint branch

### For `system/indexes/fcv-vaccine-persistence-boundary-memo.md`

- this source can now carry more of the `resistance prediction is bounded endpoint logic` language directly

### For `system/indexes/fcv-source-depth-map.md`

- `src-fcv-012` should move from partial/source_checked into full/deep_extracted

### For `system/indexes/fcv-source-index.md`

- the source should no longer be described as first-pass ingest

## Phase 3: Promotion Check

- source_card_updates:
  - preserve serology-resistance authority
  - preserve anti-no-booster and anti-sterilizing-immunity boundaries
  - preserve vaccinated-cat study-frame limits
- topic_write_back_targets:
  - `topics/fcv/endpoint-handbook.md`
  - `system/indexes/fcv-vaccine-persistence-boundary-memo.md`
  - `system/indexes/fcv-source-depth-map.md`
  - `system/indexes/fcv-source-index.md`
- not_safe_to_promote_yet:
  - any universal no-booster recommendation
  - any statement equating antibody positivity with complete durable protection
  - any use of serology to override persistence or broader control guidance
- conflicts_with_existing_vault:
  - none; this worksheet gives the FCV branch its missing serology-resistance owner
