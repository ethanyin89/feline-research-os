---
id: src-ibd-009
type: source
title: "Identifying free-text features to improve automated classification of structured histopathology reports for feline small intestinal disease"
source_kind: paper
species: feline
diseases: [IBD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2018
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, histopathology, informatics, lymphoma-boundary, machine-learning]
links:
  doi: "10.1177/1040638717744002"
  url: "https://journals.sagepub.com/doi/10.1177/1040638717744002"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source compared free-text microscopic findings with WSAVA-style structured microscopic features for classifying feline IBD, alimentary lymphoma, and normal duodenal biopsy reports.
    - The study used 60 client-owned cats: 20 with IBD, 20 with alimentary lymphoma, and 20 classified as otherwise normal.
    - The structured dataset was created by rescoring duodenal biopsy slides under WSAVA guidelines by a single board-certified pathologist blinded to diagnosis.
    - The machine-learning comparison used naive Bayes, C4.5 decision tree, and artificial neural network classifiers in WEKA.
    - Free-text models reached higher average classification performance than WSAVA-structured models for naive Bayes and artificial neural networks.
    - Adding a lamina propria plasma-cell feature improved structured-report classifier performance across all three tested algorithms.
  source_supported_conclusion:
    - This source belongs in the pathology-report workflow and diagnostic-boundary branch, not in IBD mechanism or treatment leadership.
    - The study supports a narrow claim that structured WSAVA microscopic features may lose discriminating information found in free-text pathology descriptions.
    - Plasma-cell quantification is the most reusable candidate feature for future report-structure or pathology-language normalization.
    - The source can help explain why biopsy evidence is not only about tissue acquisition; report structure and feature capture also shape downstream classification.
  llm_inference:
    - In this vault, the safest role is workflow support beneath biopsy strategy, imaging pressure, and pathologist interpretation.
    - This source is useful for LLM-wiki design because it turns pathology-report wording into an explicit information-model problem.
  # V2 enhanced fields
  study_design: "原始研究，纳入 60 只临床病例猫（20 例 IBD，20 例肠淋巴瘤，20 例正常对照），采用 WSAVA 指南下单一病理学家盲法重评分及多种机器学习分类器（朴素贝叶斯、C4.5 决策树、人工神经网络）进行自由文本与结构化显微镜特征分类比较"
  core_argument: "WSAVA 结构化显微镜特征在猫小肠疾病分类中可能遗漏自由文本病理描述中包含的重要判别信息，利用自由文本特征的机器学习模型表现更优"
  implicit_premise: "基于文本挖掘和机器学习技术，自由文本中的细节能够提供比结构化分数更丰富、更有区分力的诊断信息"
  title_gap: "标题强调自由文本特征提升自动分类，但真正发现是自由文本模型优于结构化模型表明传统 WSAVA 评分可能丢失关键细节——这对标准化病理报告提出了重要反思"
  evidence_boundary: "本研究未探讨 IBD 或肠淋巴瘤的发病机制、治疗效果评估或长期预后，仅限于诊断报告文本分类性能比较"
  unexpected_finding: "朴素贝叶斯和人工神经网络模型利用自由文本特征的分类性能超过了使用 WSAVA 规范结构化特征的模型，表明结构化标准未必是最高效的信息表达方式"
---

# One-line Summary

Pathology-informatics study showing that free-text duodenal biopsy report features can carry classification signal that is partly lost when reports are compressed into the current WSAVA structured microscopic feature set.

## Source Access Note

The DOI article page is the canonical source link. The DOI page and PMC page were not directly downloadable in the shell on 2026-04-23. The source-card upgrade is based on the article metadata plus the matching Virginia Tech dissertation chapter containing the same study text and tables. This card is now marked `deep_extracted` because the source layer has structured methods, quantitative results, and a matching worksheet, but it remains non-decision-grade because the journal full text was not independently rendered in that shell.

## Why It Matters For IBD

- adds a pathology-reporting workflow layer to the IBD-versus-alimentary-lymphoma workup branch
- provides a concrete example of information loss when free-text microscopic descriptions are converted into a structured report schema
- identifies plasma-cell quantity as a candidate report feature that may improve automated classification
- helps the wiki separate biopsy acquisition, pathologist interpretation, report structure, and machine classification as different layers

## Key Findings

- retrospective dataset: 60 client-owned cats from a veterinary teaching hospital, grouped as 20 normal, 20 IBD, and 20 small-cell alimentary lymphoma cases
- tissue basis: upper GI endoscopic duodenal biopsies, with the original slides retrieved and rescored in structured WSAVA format
- blinded rescoring: a single board-certified pathologist rescored the slides using WSAVA microscopic features while blinded to diagnosis
- structured variables: nine WSAVA-style microscopic variables, including villous stunting, epithelial injury, crypt distension, lacteal dilation, mucosal fibrosis, intraepithelial lymphocytes, lamina propria lymphocytes/plasma cells, eosinophils, and neutrophils
- unstructured variables: original free-text microscopic descriptions transformed into word-occurrence vectors using WEKA text processing
- algorithms: naive Bayes, C4.5 decision tree, and artificial neural networks were trained separately on structured and unstructured datasets
- average classifier performance was higher for free text than for WSAVA-structured reports with naive Bayes and artificial neural networks
- adding `lamina propria plasma cells` to the structured feature set improved average performance from 0.735 to 0.792 for naive Bayes, 0.717 to 0.770 for decision tree, and 0.717 to 0.782 for artificial neural networks

## Pathology-Workflow Role

This card now has enough source detail to move out of title-only status. It should still stay below the primary diagnostic workup anchors. The study is about report features and automated classification, not about replacing tissue diagnosis or proving a new biological discriminator.

The central reuse point is that pathology reports are data structures as well as clinical communications. The source compared original free-text microscopic descriptions against WSAVA-style structured features. In that comparison, free-text models retained stronger classification signal for IBD, alimentary lymphoma, and normal reports than the structured feature set did for two of the three algorithms.

For the IBD module, the useful conclusion is narrow. Report structure can shape how much diagnostic information survives into downstream classification. The current WSAVA microscopic feature set may not fully preserve information that pathologists include in free-text descriptions. The most actionable recovered feature is plasma-cell quantity, because adding it to the structured feature set improved model performance across the tested algorithms.

This strengthens the diagnostic-workup memo in a specific way: biopsy is not just a sampling question. The module should distinguish `where tissue came from`, `who interpreted it`, `which microscopic features were captured`, and `how reports are normalized for retrieval or classification`.

The source should not be used to claim that machine learning can diagnose feline IBD or lymphoma in clinical practice. The corpus was small and intentionally simple: normal, IBD, and small-cell alimentary lymphoma cases, with no broad differential set. The dissertation chapter also flags pathologist reporting-style bias and the need for larger validation.

## Best Safe Promotion

Use this wording when promoting to reader pages:

`Histopathology-report structure can affect downstream classification because free-text microscopic descriptions may preserve discriminating features that are not fully captured by the current WSAVA structured feature set; plasma-cell quantity is the clearest candidate feature recovered from this study.`

## Limits / Caveats

- deep-extracted from canonical DOI metadata plus a matching dissertation chapter, not from a directly rendered journal PDF in the 2026-04-23 shell
- small retrospective corpus of 60 cats
- all cases came from one veterinary teaching hospital
- only duodenal biopsy reports were used
- the diagnosis classes were intentionally limited to normal, IBD, and small-cell alimentary lymphoma
- machine-learning classification performance should not be treated as clinical diagnostic validation
- report-style bias is possible because original free-text reports came from multiple pathologists
- decision-grade diagnostic or regulatory claims should not rest on this source alone

## Deep Extraction

- [src-ibd-009 deep extraction round 1](../../system/indexes/src-ibd-009-deep-extraction-round1.md)

## Open Follow-up Questions

- does the final journal article add any post-dissertation changes to the methods or tables?
- can a validated plasma-cell count field be reconciled with the existing WSAVA combined lymphocyte/plasma-cell variable?
- would the signal hold in a broader differential set beyond normal, IBD, and small-cell alimentary lymphoma?
- how much of the performance difference comes from true disease signal versus pathologist reporting style?

## Linked Entities

- histopathology reports
- biopsy interpretation
- WSAVA GI standardization
- alimentary lymphoma
- plasma cells
- pathology informatics
