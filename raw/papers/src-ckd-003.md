---
id: src-ckd-003
type: source
title: "Feline CKD: Current therapies – what is achievable?"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: [phosphorus, potassium, systolic blood pressure, proteinuria, appetite, anaemia]
jurisdictions: []
evidence_level: review
year: 2014
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, therapy, treatment]
links:
  doi: "10.1177/1098612X13495241"
  url: "https://journals.sagepub.com/doi/10.1177/1098612X13495241"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Treatment of feline CKD generally focuses on minimising the adverse effects of reduced renal function, rather than the underlying cause."
    - "Strong evidence supports the use of renal diets with restricted protein and phosphorus content."
    - "Gradual transition to the renal diet improves acceptance and compliance."
    - "Phosphate binders may help achieve further phosphate restriction when diet alone is insufficient."
    - "It is unknown whether phosphate binders provide comparable survival benefit to a renal diet."
    - "Control of hypokalaemia is important because severe potassium depletion can cause cervical ventroflexion and muscle weakness."
    - "Control of hypertension is important to reduce the risk of target-organ damage."
    - "Benazepril treatment improved appetite in cats with proteinuric kidney disease but did not improve survival."
    - "As CKD progresses, many cats benefit from treatment directed at uraemic gastroenteritis and anaemia."
  source_supported_conclusion:
    - This review is the clearest current source for keeping CKD treatment logic anchored in supportive management rather than overclaiming true disease reversal.
    - Renal diet belongs at the top of the current feline CKD treatment hierarchy because this paper treats it as the strongest-supported branch.
    - Phosphate binders, potassium correction, blood-pressure management, appetite support, GI support, and anaemia support should be modeled as context-dependent adjuncts rather than as equal peers to renal diet.
    - Proteinuria-oriented RAAS therapy needs careful wording because this review preserves benefit signals while explicitly failing to upgrade benazepril into a survival-supported tier.
    - Appetite, GI signs, anaemia, potassium, blood pressure, and phosphorus all matter for treatment evaluation, but they do not carry the same evidence weight.
  llm_inference:
    - Translation pages should separate `baseline-supported interventions` from `widely used but more weakly bounded adjuncts`.
    - The safest treatment narrative remains `improve quality of life and complication control first`, with disease-modification claims left bounded.
---

# Feline CKD: Current therapies – what is achievable?

## One-Line Summary

This review says treatment usually targets the consequences of reduced renal function rather than the underlying cause, but still can improve quality of life and extend survival for many cats.

## Why It Matters For CKD

This should anchor the current-treatment baseline before adding newer options or pathway analysis.

## Key Findings

### quoted_fact

- Treatment of feline CKD usually focuses on minimising the adverse effects of reduced renal function rather than correcting the underlying cause.
- Strong evidence supports renal diets that restrict protein and phosphorus.
- Gradual dietary transition improves compliance with renal diets.
- Phosphate binders can provide additional phosphorus restriction when diet alone is insufficient, but it is unknown whether they provide survival benefits comparable to renal diets.
- Control of hypokalaemia is important because severe deficiency can produce muscle weakness and cervical ventroflexion.
- Control of hypertension is important to reduce target-organ damage risk rather than being treated as a cosmetic lab abnormality.
- Benazepril in cats with proteinuric kidney disease improved appetite but did not improve survival.
- As CKD progresses, many cats benefit from treatment of uraemic gastroenteritis and anaemia.

### source_supported_conclusion

- Renal diet belongs at the center of the initial CKD treatment baseline, with stronger support than most adjunct therapies in this source.
- The endpoint page should track phosphorus, potassium, blood pressure, proteinuria, appetite or clinical signs, and anaemia-related measures because the treatment review ties them to management decisions.
- This source supports separating supportive management from any claim of disease modification.
- This source also supports separating survival-linked interventions from symptom-relief interventions, because some commonly used therapies improve management without improving hard outcomes.
- Benazepril should remain a bounded proteinuria/appetite branch rather than a survival-proven centerpiece.

### llm_inference

- The translation layer will likely need a simple evidence hierarchy for therapies, with renal diet at the top and several adjuncts treated as context-dependent.
- The treatment matrix should not flatten phosphate binders, RAAS therapy, potassium supplementation, anaemia support, and GI support into one undifferentiated "supportive care" bucket.

## Treatment Hierarchy Signal

This review is thin compared with a decision-grade intervention guideline, but it still provides a usable hierarchy.

### Highest-confidence branch

- renal diet with protein and phosphorus restriction

### Important but bounded adjunct branches

- phosphate binders when diet alone does not control phosphorus
- hypokalaemia correction
- hypertension management
- uraemic gastroenteritis support
- anaemia support

### Caution branch

- benazepril or proteinuria-oriented RAAS therapy may improve appetite or management context, but this paper does not justify upgrading it into a survival-proven intervention tier

## Why This Changes The Vault

This paper matters less because it introduces novel interventions, and more because it imposes discipline on treatment wording.

The safe translational reading is:

- treatment can be worthwhile
- survival benefit is not equally supported across interventions
- supportive management should not be mislabeled as disease modification
- treatment evaluation should consider both hard outcomes and complication control

That makes this source a good anchor for keeping the treatment branch practical without drifting into therapeutic overclaim.

## Limits / Caveats

- This remains a review-level source rather than a treatment-by-treatment primary evidence synthesis.
- The paper gives a usable intervention hierarchy, but not a fully quantified ranking table for every adjunct branch.
- Product-specific dosing, protocol details, and stage-specific monitoring cadence are still not extracted densely enough for decision-grade treatment algorithms.

## Open Follow-Up Questions

- What does the full paper say about ongoing monitoring and treatment prioritisation?
- Which treatment claims are tied to survival, which to quality of life, and which only to biochemical control?

## Linked Entities

- diseases: CKD
- models:
- endpoints: phosphorus, potassium, systolic blood pressure, proteinuria, anaemia
- mechanisms:
- regulations:
