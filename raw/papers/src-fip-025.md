---
id: src-fip-025
type: source
title: "Assessing the feasibility of applying machine learning to diagnosing non-effusive feline infectious peritonitis"
source_kind: paper
species: feline
diseases: [FIP]
models: [machine learning diagnostic model]
endpoints: [diagnostic accuracy, sensitivity, specificity]
jurisdictions: []
evidence_level: original-study
status: ingested
extraction_depth: partial
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, machine-learning, diagnosis, non-effusive, classifier]
links:
  doi: "10.1038/s41598-024-52577-4"
  url: "https://www.nature.com/articles/s41598-024-52577-4"
  local_assets: []
year: 2024
evidence_policy:
  quoted_fact:
    - "Dataset encompassing 1939 suspected FIP cases comprising 683 FIP (35.2%) and 1256 non-FIP (64.8%) cases."
    - "Two diagnostic machine learning ensemble models trained on signalment and laboratory data."
    - "Both ensemble models detected FIP with an accuracy of 97.5%, an area under the curve (AUC) of 0.969, sensitivity of 95.45% and specificity of 98.28%."
    - "Validated on 80 confirmed cases (FIP: n=58, non-FIP: n=22)."
  source_supported_conclusion:
    - "Machine learning models can accurately discriminate FIP and non-FIP cases using laboratory data alone, in line with expert opinion."
    - "High sensitivity (95.45%) and specificity (98.28%) achieved on confirmed cases."
  llm_inference:
    - "This approach could support diagnosis of non-effusive FIP where confirmatory testing is not undertaken."
    - "Laboratory-only input suggests potential for clinical decision support without additional specialized testing."
  # V2 enhanced fields
  study_design: "机器学习诊断研究，1939 例疑似 FIP（683 例 FIP、1256 例非 FIP），信号和实验室数据训练集成模型，80 例确诊病例验证"
  core_argument: "机器学习集成模型仅使用常规实验室标志物即可准确区分 FIP 和非 FIP 病例——准确率 97.5%、AUC 0.969、敏感性 95.45%、特异性 98.28%"
  implicit_premise: "假设专家临床意见是有效的训练标签；假设实验室参数组合可捕捉 FIP 的复杂表现"
  unexpected_finding: "仅实验室数据输入即达到专家水平诊断性能——可能减少对侵入性确诊检测的需求"
  title_gap: "标题说机器学习诊断非渗出型 FIP，但真正价值是输入简单性：仅用常规实验室检查（无需积液分析、PCR 或免疫组化）即达到 97.5% 准确率——基层诊所也能初筛"
  evidence_boundary: "验证集仅 80 例确诊病例；不能替代组织病理学金标准；模型特征重要性和泛化性需全文评估"
---

# Assessing the feasibility of applying machine learning to diagnosing non-effusive feline infectious peritonitis

## Evidence-Depth Caveat

Abstract-weighted extraction only. Full text review needed for model performance metrics, feature importance, and validation methodology.

## One-Line Summary

Machine learning ensemble models trained on signalment and laboratory data can accurately discriminate FIP from non-FIP cases in line with expert opinion.

## Why It Matters For Feline FIP

Non-effusive FIP is diagnostically challenging. This study provides a data-driven approach to support clinical diagnosis when confirmatory testing (PCR, immunohistochemistry) is not performed.

## Key Findings (Abstract-Level)

### quoted_fact

- Dataset: 1939 suspected cases (683 FIP, 1256 non-FIP)
- Authors: University of Glasgow team (Dunbar, Babayan, Krumrie, Haining, Hosie, Weir)
- Published: January 30, 2024

### source_supported_conclusion

- ML models using standard laboratory markers can support FIP diagnosis
- Performance comparable to expert clinical opinion

### llm_inference

- Potential clinical decision support tool
- May reduce need for invasive confirmatory testing in some cases

## Claim-Fit Judgment

Strongest safe use:
- Diagnostic methodology research
- Non-effusive FIP diagnostic challenges

Must not control yet:
- Clinical diagnostic recommendations (needs full text review of performance metrics)
- Comparison to current gold standard tests

## Linked Entities

- diseases: FIP (non-effusive form)
- models: machine learning ensemble classifier
- endpoints: diagnostic accuracy
- mechanisms: N/A (diagnostic, not mechanistic)
- regulations: none applicable
