# Deep Extraction Worksheet

Source: `src-fip-024`  
Title: `Antiviral treatment using the adenosine nucleoside analogue GS-441524 in cats with clinically diagnosed neurological feline infectious peritonitis`  
Method note: this worksheet is based on accessible abstract-level treatment details already captured in the source card, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The paper isolates the hardest treatment branch

- core_claim: this study specifically addresses neurologic FIP rather than general FIP treatment.
- implicit_premise: neurologic disease should be modeled as a separate treatment-complexity branch.
- relation_to_previous: opening branch distinction.
- hard_details: the abstract explicitly focuses on clinically diagnosed neurologic FIP with CNS involvement.
- tension_or_surprise: this is not just another efficacy paper; it is a complexity paper.

#### Unit 2: The cohort is tiny but clinically decisive

- core_claim: only four naturally occurring CNS-involved cases were treated, so evidence depth is limited but still highly decision-relevant.
- implicit_premise: in rare or hard disease forms, even small case series can shift how the branch must be modeled.
- relation_to_previous: sets the scale of evidence.
- hard_details: four cats were treated for at least 12 weeks.
- tension_or_surprise: the sample is very small, yet the branch is too important to ignore.

#### Unit 3: Dose and monitoring complexity differ from simpler FIP treatment stories

- core_claim: neurologic FIP treatment likely requires higher doses and closer multimodal follow-up than baseline non-neurologic treatment framing.
- implicit_premise: treatment form complexity changes protocol logic, not just prognosis.
- relation_to_previous: moves from sample size to what makes the branch special.
- hard_details: abstract reports dosing at 5-10 mg/kg and serial neurologic, ophthalmic, MRI, CSF, PCR, and imaging follow-up in at least one case.
- tension_or_surprise: this is qualitatively more complex than the baseline GS efficacy story.

#### Unit 4: Positive response is real, but relapse still matters

- core_claim: all four cats responded, but relapse and eventual euthanasia still occurred in one case.
- implicit_premise: neurologic FIP response should be framed as high-value but not frictionless rescue.
- relation_to_previous: moves from protocol complexity to outcome interpretation.
- hard_details: three cats were alive off treatment; one was euthanized after relapses.
- tension_or_surprise: the right conclusion is bounded clinical success, not clean cure language.

#### Unit 5: This paper should cap the treatment branch, not flatten it

- core_claim: neurologic FIP should be treated as the high-complexity edge of the antiviral branch.
- implicit_premise: if the module keeps only one generic antiviral story, it will understate dosing, monitoring, and relapse complexity.
- relation_to_previous: defines the role of the paper in the module.
- hard_details: abstract concludes higher doses are likely required than for non-neurologic disease.
- tension_or_surprise: neurologic rescue is not just “more of the same treatment”.

## Phase 1: Theme Reconstruction

## Theme: Neurologic FIP is a distinct treatment object

This paper makes it impossible to keep neurologic FIP inside the same simple treatment bucket as non-neurologic disease. The branch has its own dosing pressure, monitoring burden, and relapse sensitivity.

### Hard Information

- CNS involvement
- 5-10 mg/kg dosing
- serial neurologic and ophthalmic monitoring

## Theme: Small-sample evidence can still reshape architecture

The study is tiny, but it still changes the architecture of the treatment branch because it defines the existence of a high-complexity edge case that must be modeled separately.

### Hard Information

- four naturally occurring cases
- three long-term survivors off treatment
- one euthanized after relapses

## Theme: Higher-dose rescue and baseline treatment are not the same layer

The right relationship between this paper and `src-fip-016` is not duplication. `src-fip-016` is the baseline natural-disease anchor. This paper is the neurologic rescue-complexity anchor.

### Hard Information

- abstract concludes higher doses are likely needed than for non-neurologic disease

## Phase 2: Claim-Evidence Structure

### Neurologic-Treatment Key Points

**Claim 1**
- support: the study directly treats cats with clinically diagnosed neurologic FIP
- details: CNS-involved cases are the explicit subject
- implicit_premise: neurologic disease is not just a footnote to general FIP treatment

**Claim 2**
- support: all four cats showed positive response and three survived off treatment
- details: the study demonstrates meaningful clinical efficacy signal even in a difficult form
- implicit_premise: the modern antiviral branch extends into neurologic disease, not only easier forms

**Claim 3**
- support: the abstract indicates higher doses than baseline non-neurologic treatment
- details: 5-10 mg/kg and explicit statement that higher doses are likely required
- implicit_premise: neurologic treatment logic changes protocol architecture

### Boundary-Setting Key Points

**Claim 1**
- support: sample size is only four
- details: evidence weight is limited
- implicit_premise: this is branch-defining but not hierarchy-settling evidence

**Claim 2**
- support: one cat relapsed and was later euthanized
- details: response is real but not uniform rescue
- implicit_premise: neurologic treatment should not be presented as clean cure language

## Phase 2.5: Write-Back Implications

### For `topics/fip/translation-brief.md`

- add neurologic FIP as a distinct treatment-complexity layer
- explicitly separate baseline efficacy, treatment-package logic, and neurologic rescue logic

### For `topics/fip/synthesis-index.md`

- add a fifth stabilizing rule:
  - neurologic rescue is a distinct layer, not just an extension of the baseline GS story

### For later FIP treatment memo

- compare three treatment layers:
  - baseline GS efficacy
  - real-world package logic
  - neurologic rescue/high-complexity treatment

## Phase 3: Promotion Check

- source_card_updates:
  - preserve neurologic branch specificity
  - preserve higher-dose and relapse boundaries
  - preserve tiny-sample caution
- topic_write_back_targets:
  - `topics/fip/translation-brief.md`
  - `topics/fip/synthesis-index.md`
  - `topics/fip/current-state-dashboard.md`
  - `system/indexes/fip-source-index.md`
- not_safe_to_promote_yet:
  - any claim that neurologic FIP treatment is settled by this paper alone
  - any claim that neurologic rescue is just baseline treatment at slightly higher dose
  - any cure framing that ignores relapse risk
- conflicts_with_existing_vault:
  - none; this worksheet adds the high-complexity edge of the treatment branch

