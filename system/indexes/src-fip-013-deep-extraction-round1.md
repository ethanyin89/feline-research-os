# Deep Extraction Worksheet

Source: `src-fip-013`  
Title: `Long-term follow-up of cats in complete remission after treatment of feline infectious peritonitis with oral GS-441524`  
Method note: this worksheet is based on abstract-level follow-up details already available from the journal article page, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: This paper changes the treatment branch from response to durability

- core_claim: the study exists to evaluate long-term outcome after successful oral GS-441524 treatment rather than initial treatment response.
- implicit_premise: initial remission and durable remission are different treatment objects.
- relation_to_previous: opening architectural placement.
- hard_details: the objective is long-term follow-up in cats already successfully treated for 84 days.
- tension_or_surprise: this is not another efficacy-establishing paper; it is a durability paper.

#### Unit 2: The cohort is selected for success, so interpretation must stay bounded

- core_claim: the study follows 18 successfully treated cats, which makes it highly useful for durability but structurally optimistic.
- implicit_premise: post-remission cohorts cannot be read as whole-branch efficacy cohorts.
- relation_to_previous: defines evidence shape.
- hard_details: 18 cats entered follow-up, with 15 available at week 36 and 14 at week 48.
- tension_or_surprise: the paper is strong for post-treatment stability, but not for relapse risk in the full treatment population.

#### Unit 3: Virologic and laboratory stability matter as much as survival language

- core_claim: remission durability in this paper is supported by serial laboratory and virologic follow-up, not by casual owner-report language alone.
- implicit_premise: durable remission should be modeled through serial stability, not just absence of death.
- relation_to_previous: adds outcome texture.
- hard_details: follow-up included physical examination, hematology, serum biochemistry, ultrasound, blood and fecal FCoV RNA, and antibody titers.
- tension_or_surprise: this paper gives the branch a richer post-treatment monitoring architecture than a generic survivor follow-up.

#### Unit 4: No confirmed relapse is powerful, but not the same as “nothing happened”

- core_claim: no confirmed relapse during one-year follow-up is a major result, but recurrence-like signals and unresolved late signs still existed.
- implicit_premise: durability can be strong without being frictionless.
- relation_to_previous: moves from monitoring design to interpretation.
- hard_details: no confirmed relapse was reported; five cats had recurrent fecal shedding, four had transient antibody rises, and two developed mild neurologic signs that later resolved.
- tension_or_surprise: the cleanest headline is not “all cured forever,” but `durability without confirmed relapse despite residual complexity`.

#### Unit 5: This paper should cap the remission branch, not replace the baseline treatment anchor

- core_claim: `src-fip-013` belongs above baseline efficacy as a follow-up and post-treatment meaning paper, not beside it as another generic GS success paper.
- implicit_premise: outcome architecture should distinguish initial response from remission durability.
- relation_to_previous: final vault role.
- hard_details: one-year follow-up after treatment initiation and nine months after treatment completion were explicitly evaluated.
- tension_or_surprise: the more encouraging the durability signal becomes, the more important it is to keep selection and follow-up framing visible.

## Phase 1: Theme Reconstruction

## Theme: Remission durability is now a real branch in FIP treatment architecture

This paper prevents the modern antiviral story from stopping at initial clinical response. It says the branch now has a legitimate post-treatment layer.

### Hard Information

- 18 successfully treated cats entered long-term follow-up
- follow-up extended to one year after treatment initiation

## Theme: Durability should be modeled through serial stability

The paper matters because it tracks clinical, laboratory, imaging, virologic, and serologic stability rather than relying on a minimal survival update.

### Hard Information

- serial hematology and serum biochemistry
- ultrasound
- blood and fecal FCoV RNA
- anti-FCoV antibody titers

## Theme: No confirmed relapse is not the same as zero residual complexity

The strongest correct summary is durable remission without confirmed relapse, not a frictionless cure story.

### Hard Information

- no confirmed relapse during one-year follow-up
- recurrent fecal shedding in five cats
- transient antibody rise in four cats
- mild delayed neurologic signs in two cats that resolved

## Phase 2: Claim-Evidence Structure

### Durability Key Points

**Claim 1**
- support: the study prospectively follows successfully treated cats after completion of therapy
- details: this is a post-treatment outcome paper rather than a baseline efficacy paper
- implicit_premise: FIP treatment architecture now includes a durability layer

**Claim 2**
- support: laboratory parameters remained stable and blood viral loads were undetectable except for one isolated occasion
- details: remission is supported by serial objective monitoring
- implicit_premise: durable remission should be tracked with repeated clinical and virologic readouts

**Claim 3**
- support: no confirmed relapse was reported during one-year follow-up
- details: the paper gives the branch a strong post-treatment stability signal
- implicit_premise: the modern antiviral branch is no longer only about immediate rescue

### Boundary-Setting Key Points

**Claim 1**
- support: only successfully treated cats entered the study
- details: this is a selected remission cohort
- implicit_premise: the paper should not be used as a whole-population efficacy estimate

**Claim 2**
- support: recurrent fecal shedding, transient antibody rises, and late mild neurologic signs still occurred
- details: durability does not erase follow-up complexity
- implicit_premise: post-treatment monitoring remains part of the branch

## Phase 2.5: Write-Back Implications

### For `system/indexes/fip-treatment-evidence-memo.md`

- strengthen `remission durability` from a placeholder branch into a defined post-treatment outcome layer
- explicitly separate durable remission from baseline efficacy and from neurologic rescue

### For `topics/fip/translation-brief.md`

- sharpen the distinction between `clinical remission data` and `post-treatment durability`
- add that no confirmed relapse is strong but still belongs inside selected-cohort framing

### For `topics/fip/synthesis-index.md`

- add remission durability as another stabilizing rule in the treatment branch

## Phase 3: Promotion Check

- source_card_updates:
  - preserve selected-remission-cohort framing
  - preserve no-confirmed-relapse language
  - preserve residual complexity and follow-up burden
- topic_write_back_targets:
  - `system/indexes/fip-treatment-evidence-memo.md`
  - `topics/fip/translation-brief.md`
  - `topics/fip/synthesis-index.md`
  - `topics/fip/current-state-dashboard.md`
  - `system/indexes/fip-source-index.md`
- not_safe_to_promote_yet:
  - any claim that this paper proves universal cure
  - any claim that post-treatment monitoring is unnecessary after remission
  - any use of this selected cohort as a whole-branch success rate
- conflicts_with_existing_vault:
  - none; this gives the remission-durability branch its first real extraction anchor
