---
id: src-ibd-019
type: source
title: "Untargeted metabolomic analysis in cats with naturally occurring inflammatory bowel disease and alimentary small cell lymphoma"
source_kind: paper
species: feline
diseases: [IBD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2021
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, metabolomics, lymphoma-boundary]
links:
  doi: "10.1038/s41598-021-88707-5"
  url: "https://www.nature.com/articles/s41598-021-88707-5"
  local_assets:
    - raw/images/ibd/src-ibd-019-figure-1-pca-heatmap-ce-vs-control.png
evidence_policy:
  quoted_fact:
    - The abstract states that feline chronic enteropathy mainly comprises inflammatory bowel disease and small-cell lymphoma and that differentiation between them can be diagnostically challenging.
    - The study characterized the fecal metabolome of 14 healthy cats and 22 cats with chronic enteropathy, including 11 cats with IBD and 11 cats with small-cell lymphoma.
    - The abstract reports distinct clustering between cats with chronic enteropathy and healthy controls.
    - The abstract states that polyunsaturated fatty acids held discriminatory power in differentiating IBD from small-cell lymphoma.
  source_supported_conclusion:
    - This source belongs in a frontier stratification branch tied to the main disease-boundary problem.
    - The study supports metabolomics as a real frontier separation signal, but not yet as routine-ready workup leadership.
  llm_inference:
    - This paper is best modeled as a frontier-marker branch that sits above support markers but below biopsy-centered workup.
  # V2 enhanced fields
  study_design: "前瞻性病例对照研究，纳入14只健康猫和22只慢性肠病猫（包括11只炎症性肠病和11只小细胞淋巴瘤猫），采用无靶向粪便代谢组学分析"
  core_argument: "多元不饱和脂肪酸的粪便代谢物谱特征能区分猫的炎症性肠病与小细胞淋巴瘤，从而为二者的诊断提供代谢组学证据"
  implicit_premise: "粪便代谢物反映了肠道内的病理状态，且不同类型的慢性肠病在代谢产物组成上存在可检测的差异"
  title_gap: "标题强调无靶向代谢组学分析，但真正的新发现是多元不饱和脂肪酸代谢物在诊断炎症性肠病与小细胞淋巴瘤中具有辨别力——为疾病鉴别提供了新的生物标志物方向"
  evidence_boundary: "本研究未解决代谢组学指标与临床预后、治疗反应的关联性，也未评估其在日常临床诊断中的实用性和稳定性"
  unexpected_finding: "粪便代谢组数据不仅区分慢性肠病与健康猫，还能细分炎症性肠病与小细胞淋巴瘤，即使这两者在临床上极难区分"
---

# One-line Summary

Metabolomic frontier paper that likely deepens the IBD-versus-small-cell-lymphoma boundary without becoming a routine first-line workup tool.

## Why It Matters For IBD

- adds a modern omics branch to the disease-boundary problem
- may help distinguish explanation, stratification, and practical diagnosis
- now serves as the first metabolomic frontier anchor in the IBD module

## Key Findings

- abstract includes 14 healthy cats and 22 cats with chronic enteropathy, evenly split between IBD and small-cell lymphoma
- abstract reports distinct clustering between chronic enteropathy and healthy controls
- abstract reports 84 compounds differing between chronic enteropathy and healthy cats
- abstract states that polyunsaturated fatty acids had discriminatory power for differentiating IBD from small-cell lymphoma
- abstract notes altered metabolites related to tryptophan, arachidonic acid, and glutathione pathways

## Frontier-Stratification Role

This source is the strongest current frontier-marker anchor in the IBD-versus-small-cell-lymphoma branch. It should be placed above shared support markers such as vitamin D and S100A12 because it reports disease-class-relevant metabolomic separation, but it still belongs below biopsy, histopathology, imaging, and biopsy-site strategy in routine workup architecture.

The cohort structure is central. The study characterized fecal metabolomes in 14 healthy cats and 22 cats with chronic enteropathy, including 11 cats with IBD and 11 cats with small-cell lymphoma. Principal component and heat-map analyses showed distinct clustering between chronic enteropathy and healthy controls. Random forest classification had good prediction for healthy versus chronic-enteropathy cats, with an overall out-of-bag error reported in the worksheet as 16.7%. The abstract also states that polyunsaturated fatty acids had discriminatory power for differentiating IBD from small-cell lymphoma.

For wiki reuse, this card should be the prototype for a `frontier stratification, not routine diagnosis` rule. It supports the idea that IBD and small-cell lymphoma may have separable metabolic signatures, especially around polyunsaturated fatty acids and pathways involving tryptophan, arachidonic acid, and glutathione. But the card should not imply that fecal metabolomics is available, validated, or sufficient as a first-line diagnostic test.

This source also helps organize the marker hierarchy. Shared serum or fecal markers mostly separate sick from healthy. Metabolomics may begin to separate disease classes. Biopsy-site evidence still controls the practical workup. That three-layer distinction should be explicit in the endpoint handbook and synthesis page.

The next precision step is validation: which metabolite classes remain stable, how they perform against biopsy-confirmed cases, and whether they add value beyond imaging and paired biopsy strategy.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- frontier omics signals should not outrun biopsy, imaging, or clinical-index evidence
- do not treat random forest or clustering signals as routine clinical readiness
- individual metabolite findings need validation before becoming diagnostic claims

## Image Assets

- `raw/images/ibd/src-ibd-019-figure-1-pca-heatmap-ce-vs-control.png` — Scientific Reports article Figure 1; verified against the article page as the PCA / heatmap visual for chronic-enteropathy versus healthy-control metabolomic clustering

## Open Follow-up Questions

- does the metabolomic signature truly separate disease classes?
- is the signal clinically actionable or mainly descriptive?
- what validation cohort would be needed before this becomes workup-relevant?
- how should metabolomics be compared with microbiota and tissue-marker branches?

## Deep Extraction

- [src-ibd-019 deep extraction round 1](../../system/indexes/src-ibd-019-deep-extraction-round1.md)

## Linked Entities

- metabolomics
- alimentary small-cell lymphoma
- frontier markers
