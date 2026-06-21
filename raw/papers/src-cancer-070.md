---
id: src-cancer-070
type: source
title: "Immunocytochemical analysis of the tumour suppressor protein (p53) in feline neoplasia"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2000
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
pmid: 10814873
doi: "10.1016/s0304-3835(00)00337-2"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, immunocytochemical, analysis, suppressor, protein, p53, neoplasia]
links:
  doi: "10.1016/s0304-3835(00)00337-2"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S0304383500003372?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Immunocytochemical analysis of the tumour suppressor protein (p53) in feline neoplasia."
    - "The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S0304383500003372?via%3Dihub."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
  # V2 enhanced fields
  study_design: "原始研究（2000 年 Cancer Letters），77 例猫肿瘤（代表 486 例诊断提交）的 p53 免疫细胞化学分析"
  core_argument: "p53 免疫反应性在不同猫肿瘤类型中变化很大——SCC 46%、骨肉瘤 50%、乳腺癌 33%、腺癌 16%、血管肉瘤 14% 呈阳性——恶性淋巴瘤和纤维肉瘤均为阴性——支持 p53 异常在某些猫肿瘤类型中的作用"
  implicit_premise: "假设免疫组化阳性代表功能性 p53 突变/蓄积；假设 77 例样本代表更广泛的猫肿瘤谱系"
  unexpected_finding: "淋巴瘤和纤维肉瘤中 p53 免疫反应性缺失——这与人类淋巴瘤中 p53 改变的作用形成对比——可能反映猫淋巴瘤的不同分子机制或技术局限性"
  title_gap: "标题说猫肿瘤中 p53 抑癌蛋白的免疫细胞化学分析，但真正发现是肿瘤类型特异性：上皮和间叶来源肿瘤（SCC、骨肉瘤、乳腺癌）显示 p53 阳性——而淋巴造血肿瘤和纤维肉瘤阴性——提示不同的肿瘤发生机制"
  evidence_boundary: "摘要级免疫组化证据；支持分子机制背景，不支持诊断、预后或治疗选择；2000 年研究可能有技术局限性"
---

# Immunocytochemical analysis of the tumour suppressor protein (p53) in feline neoplasia

## Evidence-Depth Caveat

This is a second-pass abstract-extracted source card. The abstract was fetched from PubMed (PMID 10814873) and key findings were extracted at abstract level only.

## Source Check, 2026-06-02

PubMed abstract fetched as a zero-cost extraction step.

- PMID: 10814873
- DOI: 10.1016/s0304-3835(00)00337-2
- Journal: Cancer Letters
- Year: 2000

## Abstract Summary

This study examined p53 immunoreactivity across feline tumour types.

**Study design:**

| Feature | Abstract-Extracted Detail |
|---------|---------------------------|
| Dataset context | 77 feline tumours selected as a representative sample of 486 diagnostic submissions |
| Assay | Immunocytochemical p53 staining |
| Positive staining | SCC 46%, osteosarcoma 50%, mammary carcinoma 33%, adenocarcinoma 16%, haemangiosarcoma 14% |
| Negative staining | No malignant lymphomas or fibrosarcomas examined showed p53 immunoreactivity |
| Interpretation | Abstract supports a role for p53 aberrations in certain feline tumour types |

**Boundary:** This is abstract-level immunostaining evidence. It should not be used alone for diagnosis, prognosis, or treatment selection.

## One-Line Summary

PubMed abstract supports this source as p53 immunoreactivity evidence across selected feline tumour types, not as stand-alone diagnostic guidance.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Immunocytochemical analysis of the tumour suppressor protein (p53) in feline neoplasia.
- The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S0304383500003372?via%3Dihub.

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
