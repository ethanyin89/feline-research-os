---
id: src-cancer-101
type: source
title: "Evaluation of TFR-1 Expression in Feline Mammary Cancer and In Vitro Antitumor Efficacy Study of Doxorubicin-Loaded H-Ferritin Nanocages"
source_kind: paper
species: feline
diseases: [cancer]
models: [human-breast-cancer]
endpoints: [TFR-1-expression, cell-proliferation, apoptosis]
jurisdictions: [Italy]
evidence_level: original-study
year: 2021
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
pmid: "33809013"
pmcid: "PMC8000254"
doi: "10.3390/cancers13061248"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, mammary, FMC, TFR-1, transferrin, nanocage, doxorubicin, HFn, targeted-therapy, nanomedicine]
links:
  doi: "10.3390/cancers13061248"
  url: "https://www.mdpi.com/2072-6694/13/6/1248"
  pmc: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8000254/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The H-score showed an increased protein level of TFR-1 in feline mammary carcinomas with nodal metastasis (mean 112.28 ± SD 40.51) versus healthy mammary gland tissues (mean 40.07 ± SD 38.95) (p < 0.05)."
    - "The expression of TFR-1 was identified in 95% of the cells."
    - "The proliferation rate of FMCm treated with HFn(DOX) was lower (p < 0.05) than that treated with DOX at 0.01 μM, 72 h after treatment."
    - "The sequencing showed that the fragment amplified had 99% homology with the Felis catus transferrin receptor gene (TFRC)."
    - "The use of HFn(DOX) resulted in less proliferation of cells and increased apoptosis when compared to the drug alone."
  source_supported_conclusion:
    - "TFR-1 expression increases with FMC metastatic progression: healthy (40.07) → FMC no mets (78.72) → FMC with mets (112.28)."
    - "Doxorubicin-loaded H-ferritin nanocages (HFn-DOX) are more effective than free doxorubicin in vitro."
    - "TFR-1 is a valid target for FMC nanomedicine therapy."
    - "First demonstration of HFn nanocage efficacy in veterinary oncology."
  llm_inference:
    - "TFR-1 may serve as a prognostic marker (higher expression in metastatic disease)."
    - "HFn-DOX could reduce doxorubicin systemic toxicity via targeted delivery."
    - "In vitro efficacy requires in vivo confirmation before clinical application."
  # V2 enhanced fields
  study_design: "体外研究 + IHC（2021 年 Cancers），FMCm 细胞系 + FMC 组织样本，TFR-1 表达分析和 HFn-DOX 纳米笼疗效测试"
  core_argument: "TFR-1 是 FMC 治疗的有效靶点——表达随转移进展递增（健康 40 → 无转移 79 → 有转移 112）——95% 的 FMCm 细胞 TFR-1 阳性——HFn-DOX 比游离 DOX 更有效（更低增殖、更高凋亡）——首次在兽医肿瘤学中证明 HFn 纳米笼疗效"
  implicit_premise: "假设 TFR-1 表达与转移的相关性暗示因果关系；假设单细胞系结果可代表整体 FMC 反应；假设体外疗效可转化为体内疗效"
  unexpected_finding: "猫 TFRC 与已知序列的同源性达 99%——暗示 TFR-1 靶向策略可能跨物种适用——人类和猫乳腺癌可能共享这一治疗靶点"
  title_gap: "标题说评估 FMC 中 TFR-1 表达和 HFn-DOX 纳米笼的体外抗肿瘤疗效，但真正发现是转移预测：TFR-1 H-score 可能作为转移风险分层工具——而 HFn-DOX 是概念验证靶向递送系统"
  evidence_boundary: "体外证据；支持 TFR-1 作为靶点和 HFn-DOX 概念验证，不支持临床治疗推荐——体内验证需要；H-score 阈值需要前瞻性队列验证"
---

# Evaluation of TFR-1 Expression in Feline Mammary Cancer and In Vitro Antitumor Efficacy Study of Doxorubicin-Loaded H-Ferritin Nanocages

## Evidence-Depth Caveat

**Deep-extracted from PMC full text (PMC8000254).** This 2021 study demonstrates TFR-1 expression increases with FMC metastatic progression. HFn(DOX) nanocages showed superior efficacy vs free doxorubicin in vitro. First veterinary nanomedicine HFn study. Evidence level: in vitro.

## Source Check, 2026-06-09

Europe PMC full text extraction.

| Field | Value |
|-------|-------|
| PMID | 33809013 |
| PMCID | PMC8000254 |
| DOI | 10.3390/cancers13061248 |
| Journal | Cancers (MDPI) |
| Year | 2021 |
| Authors | Rensi N, Sammarco A, Moccia V, et al. |
| Open access | yes |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Study type | In vitro targeted therapy + IHC |
| Target | Transferrin receptor 1 (TFR-1) |
| Approach | Doxorubicin-loaded H-ferritin nanocages (HFn-DOX) |
| TFR-1 H-score | Healthy 40.07 → FMC no mets 78.72 → FMC with mets 112.28 |
| Cell line | FMCm (feline metastatic mammary cancer) |
| TFR-1 positivity | 95% of FMCm cells |
| Efficacy | HFn-DOX < DOX proliferation at 0.01-0.1 μM (p<0.05) |

**Boundary:** In vitro evidence only. TFR-1 as therapeutic target and HFn-DOX efficacy require in vivo confirmation.

## One-Line Summary

TFR-1 expression increases with FMC metastatic progression (H-score 40→79→112); doxorubicin-loaded H-ferritin nanocages outperform free doxorubicin in vitro.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- TFR-1 overexpressed in broad range of solid tumors in humans
- TFR-1 is recognized by H-Ferritin (HFn)
- HFn nanocages allow selective binding and drug internalization
- Doxorubicin loaded into HFn nanocages for targeted delivery

### source_supported_conclusion

- TFR-1 expression evaluated in feline mammary cancer
- HFn-doxorubicin nanocages tested for in vitro antitumor efficacy
- Nanomedicine approach for FMC treatment

### llm_inference

- May inform mammary-carcinoma.md targeted therapy section
- Novel drug delivery approach alternative to conventional chemotherapy
- Supports comparative oncology nanomedicine development

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
