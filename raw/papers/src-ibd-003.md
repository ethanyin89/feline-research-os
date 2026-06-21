---
id: src-ibd-003
type: source
title: "Feline inflammatory bowel disease"
source_kind: paper
species: feline
diseases: [IBD]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 1999
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, review, mechanism]
links:
  doi: "10.1016/S1098-612X(99)90204-8"
  url: "https://www.sciencedirect.com/science/article/pii/S1098612X99902048"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source is a review article on feline inflammatory bowel disease published in the Journal of Feline Medicine and Surgery in 1999.
    - The abstract states that feline IBD is a diagnosis of exclusion.
    - The abstract states that dietary intolerance or allergy and well-differentiated alimentary lymphosarcoma can mimic IBD clinically and histologically.
    - The abstract states that intestinal biopsies are useful but must be obtained carefully and interpreted by someone with expertise in alimentary tract pathology.
  source_supported_conclusion:
    - This is the best current broad feline IBD anchor in the seed corpus.
    - The review supports modeling the early IBD module around diagnostic exclusion and disease-boundary handling, not around one lead biomarker.
  llm_inference:
    - This was the correct first IBD deep extraction target because it stabilizes the whole workup architecture before narrower branches are deepened.
  # V2 enhanced fields
  study_design: "综述性研究，聚焦猫炎症性肠病，综合分析文献和病例资料"
  core_argument: "猫炎症性肠病是一种排除性诊断，必须排除饮食不耐受、过敏及肠道淋巴肉瘤等疾病才能确诊"
  implicit_premise: "临床与组织学表现相似的疾病能被准确区分，且有经验的病理专家能够正确解读肠道活检结果"
  title_gap: "标题提到炎症性肠病，但真正重点在于诊断过程中如何通过排除其他相似疾病来界定IBD的诊断边界"
  evidence_boundary: "本综述未明确指出具体治疗方案或长远预后，仅聚焦于诊断学层面"
  unexpected_finding: "饮食不耐受或过敏以及肠道淋巴肉瘤在临床和组织学上能高度模拟IBD，增加诊断复杂度"
---

# One-line Summary

Broad feline IBD review that should anchor the first full compile of the disease module.

## Why It Matters For IBD

- gives the module one broad reference point before the map fragments into workup, pathology, and treatment branches
- likely stabilizes baseline terminology around feline IBD and chronic enteropathy
- now serves as the first deep-extracted overview anchor in the IBD module

## Key Findings

- abstract frames feline IBD as a diagnosis of exclusion rather than a default label
- abstract explicitly warns that dietary intolerance or allergy can mimic IBD both clinically and histologically
- abstract explicitly warns that well-differentiated alimentary lymphosarcoma can be confused with IBD
- abstract supports biopsy utility but also emphasizes sample quality and specialist pathology interpretation
- abstract states that well-constructed dietary therapy can often benefit both dietary disease and IBD

## Broad-Frame Role

This review should anchor the IBD module's first principle: feline IBD is a diagnosis-of-exclusion architecture, not a default endpoint label. That one rule controls the rest of the wiki. Chronic vomiting, diarrhea, weight loss, intestinal inflammation, or biopsy changes should not be compressed too quickly into idiopathic IBD before food-responsive disease and alimentary lymphoma have been handled.

The source is especially valuable because it places the IBD-versus-mimic problem at the review level, not as a late specialist caveat. Dietary intolerance or allergy can mimic IBD clinically and histologically. Well-differentiated alimentary lymphosarcoma can also be confused with IBD. This means the module's recognition page should start with exclusion logic rather than with one biomarker, one diet, or one treatment.

Biopsy should be presented as necessary but not magical. The abstract supports intestinal biopsies, but it also stresses careful acquisition and expert alimentary-tract pathology interpretation. That creates the bridge to later biopsy-site and lymphoma-boundary sources such as `src-ibd-015`, `src-ibd-010`, and molecular/immunohistochemistry papers. The correct wiki sequence is: broad exclusion frame, diet/food-responsive branch, biopsy and pathology constraints, lymphoma boundary, then chronicity and treatment.

The diet point should remain bounded. The review says well-constructed dietary therapy can benefit dietary problems and IBD, but it does not turn diet into a universal diagnostic or treatment shortcut. It supports a practical first branch: diet matters early because food-responsive disease can resemble IBD, and because diet may improve some true IBD cases.

The claim ceiling is chronology. This is a 1999 review, so it should not override newer fibrosis, microbiota, metabolomic, biopsy-site, activity-index, or treatment papers. Its role is to hold the outer architecture together.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- older broad reviews may underweight newer fibrosis, metabolomic, and biopsy-boundary work
- do not use this review as a modern endpoint or treatment hierarchy by itself
- do not let broad IBD language erase food-responsive disease or lymphoma exclusion

## Image Asset TODO

- figures to capture:
  - exclusion-first workup overview figure
  - IBD-versus-mimic summary table
  - biopsy interpretation or sampling guidance figure
- why these matter:
  - this is still the broadest feline IBD anchor and should preserve the module's exclusion-first backbone visually
  - mimic conditions such as dietary disease and small-cell lymphoma are easy to flatten if they stay prose-only
  - if biopsy interpretation guidance is present, it would strengthen the workup layer without overpromoting any single marker

## Open Follow-up Questions

- how does it frame IBD relative to chronic enteropathy?
- how strongly does it separate IBD from alimentary lymphoma?
- how much of its treatment framing still holds up after later diet, fibrosis, and biomarker work?
- which full-text sections should be split into diagnosis, mimic exclusion, biopsy-quality, and diet-response notes?
- does the paper define IBD in a way that conflicts with later chronic-enteropathy terminology?

## Deep Extraction

- [src-ibd-003 deep extraction round 1](../../system/indexes/src-ibd-003-deep-extraction-round1.md)

## Linked Entities

- IBD
- chronic enteropathy
- gastrointestinal inflammation
