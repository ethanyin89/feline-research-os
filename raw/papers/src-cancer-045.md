---
id: src-cancer-045
type: source
title: "Treatment of mammary cancer with focused ultrasound: A pilot study in canine and feline patients"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2023
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
pmid: 36917874
doi: "10.1016/j.ultras.2023.106974"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, treatment, mammary, focused, ultrasound, pilot, study, patients]
links:
  doi: "10.1016/j.ultras.2023.106974"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S0041624X23000501?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Treatment of mammary cancer with focused ultrasound: A pilot study in canine and feline patients."
    - "The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S0041624X23000501?via%3Dihub."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
  # V2 enhanced fields
  study_design: "前瞻性先导研究（2023 年 Ultrasonics），9 只犬猫表浅乳腺癌，2-MHz 聚焦超声消融后立即手术切除"
  core_argument: "热聚焦超声可在犬猫乳腺肿瘤中产生明确的凝固性坏死——组织病理学证实所有治疗肿瘤有效消融——但需要更大研究确认安全性和深部肿瘤完全消融的可行性"
  implicit_premise: "假设聚焦超声在人类乳腺癌中的疗效可转移到伴侣动物；假设先导研究的安全性可扩展到更大群体"
  unexpected_finding: "摘要未报告脱靶损伤——在表浅肿瘤中实现了精确消融——但立即手术切除使长期结局无法评估"
  title_gap: "标题说聚焦超声治疗乳腺癌的先导研究，但真正发现是可行性验证：9 例混合犬猫样本仅证明技术可行——临床采用或结局获益需要更大研究"
  evidence_boundary: "小样本混合犬猫先导研究，FUS 后立即切除；仅支持可行性研究而非临床采用或结局获益"
---

# Treatment of mammary cancer with focused ultrasound: A pilot study in canine and feline patients

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 2023 Ultrasonics: 9 dogs and cats with superficial mammary cancer; 2-MHz focused ultrasound produced coagulative necrosis in all tumors; feasibility only, not a treatment recommendation. [Deep extraction worksheet](../../system/indexes/src-cancer-045-deep-extraction-round1.md).

## Source Check, 2026-06-01

PubMed abstract fetched as a zero-cost extraction step.

- PMID: 36917874
- DOI: 10.1016/j.ultras.2023.106974
- Journal: Ultrasonics
- Year: 2023

## Abstract Summary

This pilot study assessed thermal focused ultrasound (FUS) feasibility for canine and feline mammary cancer therapy.

**Study design:**

| Feature | Abstract-Extracted Detail |
|---------|---------------------------|
| Technology | 2-MHz single-element spherically focused ultrasonic transducer integrated with robotic positioning |
| Preclinical validation | Rabbit thigh model used to validate tissue ablation protocol |
| Veterinary patients | 9 dogs and cats with superficial mammary cancer |
| Clinical protocol | FUS ablation followed by immediate surgical resection |
| Safety selection | Animals recruited under specific safety criteria |

**Key findings:**

- Histopathology demonstrated well-defined coagulative necrosis in all treated tumors.
- No off-target damage was reported in the abstract.
- The authors state that larger studies are needed to confirm safety and feasibility, especially for complete ablation of deep-seated tumors.

**Boundary:** This is a small mixed canine/feline pilot with immediate resection after FUS. It supports feasibility research only, not clinical adoption or outcome benefit.

## One-Line Summary

Focused ultrasound produced targeted coagulative necrosis without abstract-reported off-target damage in a 9-patient canine/feline mammary cancer pilot, but remains feasibility-stage evidence.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Treatment of mammary cancer with focused ultrasound: A pilot study in canine and feline patients.
- The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S0041624X23000501?via%3Dihub.

### source_supported_conclusion

- This is a first-pass source-card placeholder for triage and queue control.
- It should not support prevalence, diagnostic, treatment, management, or risk-ranking claims yet.

### llm_inference

- The title suggests a possible `cancer` role, but the actual claim-fit requires abstract or full-text review.

## Claim-Fit Judgment

Strongest safe use:

- intake ownership
- source queue placement
- deduplication and future extraction planning

Must not control yet:

- reader-facing medical advice
- numeric claims
- comparative ranking
- guideline-like recommendations
- mechanism closure

## Image Asset TODO

- figures to capture: unknown until source text is read
- why these matter: tables or figures should remain behind the candidate gate until labels are verified

## Open Follow-Up Questions

- What source family is confirmed by the abstract or article body?
- Which claims, if any, are reusable for the cancer module?
- Does this source deserve deep extraction, or should it remain queue context?
- Are there tables or figures that change the module structure?

## Linked Entities

- diseases: cancer
- models:
- endpoints:
- mechanisms:
- regulations:
