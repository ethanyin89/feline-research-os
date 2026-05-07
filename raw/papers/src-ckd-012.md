---
id: src-ckd-012
type: source
title: "Case-Control Study of Risk Factors Associated with Feline and Canine Chronic Kidney Disease"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2010
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, risk-factors, case-control, comparative]
links:
  doi: "10.4061/2010/957570"
  url: "https://onlinelibrary.wiley.com/doi/10.4061/2010/957570"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The study was an age-matched case-control study designed to determine major risk factors associated with CKD in cats and dogs and to determine what clinical signs owners observed before diagnosis."
    - "Compared with controls, feline CKD cases were more likely to have had polydipsia and polyuria in the year before their cats were diagnosed with CKD."
    - "In dogs, owners recognized abnormal drinking and urination behavior more than half a year before veterinary CKD diagnosis."
    - "The authors concluded that earlier CKD diagnosis should have been possible in most cases and that clinical trials should measure the efficacy of early interventions."
  source_supported_conclusion:
    - This primary study is one of the best current anchors for adding an owner-observed recognition layer to feline CKD, because it shows that pre-diagnostic behavior changes were often already present.
    - The source is stronger for practical recognition timing than for mechanistic or biochemical endpoint logic.
    - The paper supports keeping delayed recognition visible as a human-observation and workflow problem, not only as a biomarker-development problem.
    - This study also strengthens the case for earlier-intervention trial design, even though it does not specify the optimal biochemical trigger package.
  llm_inference:
    - Early-detection summaries should probably include a bounded `owner-observed prompts` subsection rather than focusing exclusively on laboratory surveillance.
    - Recognition pages should treat polyuria and polydipsia as useful prompts for workup escalation, not as late-stage trivia.
---

# Case-Control Study of Risk Factors Associated with Feline and Canine Chronic Kidney Disease

## One-Line Summary

This age-matched case-control study found that owners of feline CKD cases more often noticed polyuria and polydipsia before veterinary diagnosis, supporting the idea that earlier recognition of CKD should often be possible.

## Why It Matters For CKD

This is one of the few primary-study entries in the seed corpus and may help separate feline-specific from cross-species risk signals.

## Key Findings

### quoted_fact

- The study was an age-matched case-control study designed to determine major risk factors associated with CKD in cats and dogs and to determine what clinical signs owners observed before diagnosis.
- Compared with controls, feline CKD cases were more likely to have had polydipsia and polyuria in the year before their cats were diagnosed with CKD.
- In dogs, owners recognized abnormal drinking and urination behavior more than half a year before veterinary CKD diagnosis.
- The authors concluded that earlier CKD diagnosis should have been possible in most cases and that clinical trials should measure the efficacy of early interventions.
- The study is especially useful because it ties delayed diagnosis to observable daily-life changes rather than only to laboratory lag.

### source_supported_conclusion

- This primary study supports moving owner-observable changes in drinking and urination into the early-detection discussion rather than treating them as incidental history.
- The study strengthens the case for a dedicated early-recognition subsection in the CKD index and endpoint pages, even though it does not itself define biochemical endpoints.
- Because this paper is comparative and symptom-focused, it is more useful for screening and recognition framing than for mechanistic claims.
- The strongest signal here is practical: earlier CKD workup should often have been possible before formal diagnosis.
- This paper complements biomarker-oriented early-detection sources by showing that recognition failures are partly behavioral and workflow-related.

### llm_inference

- The first CKD overview page may benefit from a “what gets noticed too late” section, because delayed recognition appears to be part of the practical disease problem.
- Owner-observed prompts should stay below biochemical confirmation in authority, but above incidental-history status in compilation.

## Why This Study Matters

This paper matters because it adds a layer that many CKD summaries miss: recognition does not fail only because biomarkers are imperfect. It also fails because observable changes in drinking and urination are not always converted into timely veterinary workup.

That makes this study unusually useful for the early-detection branch. It does not compete with creatinine, USG, SDMA, or proteinuria papers. Instead, it explains why earlier workup might have been possible before those tests were even ordered.

It also adds a more grounded reason to keep early intervention visible in the vault. The authors do not simply say earlier diagnosis would be nice. They argue that it should often have been possible, which turns recognition delay into a clinically actionable problem.

## Recognition Layer Signal

The safest promotion from this source is:

- polyuria and polydipsia belong in recognition logic
- owner-observed change can precede formal diagnosis
- earlier workup opportunities may often be missed
- trial design for early intervention makes more sense once recognition delay is acknowledged

This is why the card should be compiled into early-detection pages, not left as a thin comparative note.

## Limits / Caveats

- Current extraction is abstract-level and symptom-focused.
- The available abstract does not provide a detailed feline-specific risk factor table.
- Because the study is comparative and case-control in design, it is better for recognition framing than for causal ranking or endpoint hierarchy.

## Open Follow-Up Questions

- What additional feline-only risk factor evidence should be paired with this paper?
- How early before diagnosis were feline owner observations documented relative to formal staging?
- Which owner-observed changes beyond drinking and urination were tracked in feline cases?
- How should owner-observed prompts be integrated with serial-surveillance recommendations in compiled early-detection workflows?

## Linked Entities

- diseases: CKD
- models:
- endpoints: polyuria, polydipsia
- mechanisms:
- regulations:
