---
id: src-hcm-023
type: source
title: "Deep learning-based diagnosis of feline hypertrophic cardiomyopathy"
source_kind: paper
species: feline
diseases: [HCM]
models: [deep-learning]
endpoints: [ai-diagnosis]
jurisdictions: []
evidence_level: original-study
year: 2023
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [hcm, ai, diagnosis]
links:
  doi: "10.1371/journal.pone.0280438"
  url: "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0280438"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The abstract states that radiography and ultrasound are the gold standards in the diagnosis of feline HCM."
    - "The abstract reports that five residual-architecture models were trained on 231 ventrodorsal radiographic images from five institutions."
    - "The abstract reports that the source dataset included 273 ventrodorsal radiographic images, with 231 used for learning and 42 used for testing."
    - "The abstract reports 143 HCM and 88 normal images in the learning process."
    - "The abstract reports that all five models showed greater than 90% accuracy, with 95.45% reported for each model in prediction analysis."
    - "The abstract reports that a softmax voting strategy achieved 95% accuracy in combined test data."
    - "The abstract states that the automated deep-learning system can assist veterinary radiologists in screening HCM."
  source_supported_conclusion:
    - AI or computational diagnosis belongs in a frontier recognition branch, not in the core phenotype-definition branch.
    - The safest current use of this source is to make AI augmentation explicit while keeping it below structure-first confirmation.
    - AI-diagnosis work should be modeled as augmentation or support until input and use-case details justify more.
    - The evidence supports radiography-based screening assistance, not replacement of echocardiographic confirmation.
    - The model-performance signal should travel with dataset-size, image-view, and test-split caveats.
  llm_inference:
    - This may later become a useful screening-augmentation or diagnostic-support boundary paper.
    - Endpoint and recognition pages should keep augmentation-versus-replacement uncertainty explicit.
  # V2 enhanced fields
  study_design: "多中心回顾性研究，273 张腹背位胸片（231 训练 / 42 测试），5 种残差网络架构，softmax 投票集成"
  core_argument: "基于腹背位胸部 X 光片的深度学习模型可以辅助兽医放射科医师进行 HCM 筛查，但不能替代超声心动图作为金标准确诊手段"
  implicit_premise: "假设 231 张训练图像和 42 张测试图像足以代表临床场景的多样性；假设 HCM vs 正常的二分类任务可以泛化到区分 HCM 与其他心脏疾病"
  unexpected_finding: "五个 CNN 模型的准确率均超过 90%，且 softmax 投票策略达到 95%——对于仅 273 张图像的小数据集来说，这一表现出乎意料地好"
  title_gap: "标题说深度学习诊断，但真正边界是输入限制：仅用 VD 位 X 光片训练，不能区分 HCM 与其他心影增大疾病——这是筛查辅助而非超声心动图替代"
  evidence_boundary: "仅使用 VD 位 X 光片作为输入；不能区分 HCM 与其他导致心影增大的心脏疾病；临床工作流程整合和前瞻性验证未完成；测试集仅 42 张图像"
---

# One-line Summary

Deep-learning diagnosis study that widens the frontier recognition branch of HCM.

## Why It Matters For HCM

- adds an AI-assisted diagnosis branch to the module
- pressures clearer separation between core recognition and augmented screening

## Key Findings

- deep-learning diagnosis focus
- ventrodorsal radiograph input, not multimodal clinical diagnosis
- 273 images from five institutions; 231 used for learning and 42 for testing
- five CNN/residual architectures tested
- likely computational screening support rather than first-line clinical authority

## Why This Study Matters

This paper matters because modern recognition pages need a visible AI branch even when that branch does not deserve authority. If AI is omitted entirely, the module becomes outdated. If AI is promoted too early, the hierarchy becomes unreliable.

This source gives a better middle position. It makes deep-learning-based diagnosis explicit inside feline HCM, which means the recognition module can no longer pretend computational augmentation is hypothetical. The abstract also resolves the core input question: this is radiography-based, using ventrodorsal feline thoracic images, not an echocardiography replacement model.

The study trained five architectures on 231 images and tested on 42 images from a broader 273-image dataset collected from five institutions. The performance signal is high in the abstract: all five models exceeded 90% accuracy, each was reported at 95.45% in prediction analysis, and a softmax voting strategy reached 95% accuracy in combined test data. That is enough to make the AI branch concrete.

It is not enough to move the branch above structure-first confirmation. Radiography and ultrasound are described as diagnostic standards, and the authors frame the deep-learning system as assistance for veterinary radiologists in screening. The page-layer role should therefore be `screening augmentation / radiology support`, not `automated HCM diagnosis`.

That is why this paper improves the module even before it changes operational ranking. It makes the AI branch explicit and subordinate at the same time.

## AI-Augmentation Boundary

The strongest reusable write-back from this source is:

- HCM recognition now has a real AI-augmentation branch
- AI should remain below structure-first confirmation
- augmentation and replacement are distinct claims and should not be blended
- method and input dependence should block routine-ready authority claims
- performance claims should carry the VD-radiograph and dataset-size boundaries
- the correct comparison is assistance to radiologists, not displacement of echocardiography

That keeps the module current without letting frontier language outrun evidence.

## Limits / Caveats

- current card is abstract-weighted rather than full-text reviewed
- this card currently supports branch placement more strongly than diagnostic performance interpretation
- image-only performance may not generalize to broader clinical workflow without prospective validation
- HCM/normal label construction, institution effects, and peeking controls need full-text review before operational promotion

## Open Follow-up Questions

- how robust is the radiograph model across acquisition quality, positioning, disease stage, and non-HCM cardiac disease?
- is this paper closer to screening augmentation or diagnostic replacement?
- how much of the model depends on image-derived structure versus other data channels?
- what evidence would be required before this branch could move above bounded augmentation?

## Linked Entities

- HCM
- AI diagnosis
