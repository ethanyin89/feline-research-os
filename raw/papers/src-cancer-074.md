---
id: src-cancer-074
type: source
title: "Investigation of immune cell markers in feline oral squamous cell carcinoma"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2018
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: 30078599
tags: [cancer, FOSCC, immune, Treg, FoxP3, CD3, CD79a, COX-2, HNSCC, immunotherapy]
links:
  doi: "10.1016/j.vetimm.2018.06.011"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S0165242717305032?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "T cell infiltrates (CD3+) detected in 92% of tumor biopsies."
    - "Treg infiltrates (FoxP3+) detected in 57% of biopsies, involving both neoplastic epithelium and stroma."
    - "COX-2 positive but weak staining in 75% of neoplastic epithelium cases."
    - "Increased circulating CD4+FoxP3+ T cells in OSCC patients vs healthy controls (P=0.045)."
  source_supported_conclusion:
    - "Feline OSCC shows immune infiltration patterns similar to human HNSCC."
    - "Treg enrichment in FOSCC suggests potential for immunotherapy targeting."
  llm_inference:
    - "Supports comparative oncology value of FOSCC as HNSCC model."
    - "Treg infiltration may explain poor immunotherapy response."
  # V2 enhanced fields
  study_design: "原始研究（2018 年 Vet Immunol Immunopathol），12 例 FOSCC IHC 分析 + 9 例流式细胞术分析循环免疫细胞"
  core_argument: "FOSCC 显示免疫浸润模式与人类 HNSCC 相似——92% CD3+ T 细胞浸润——57% FoxP3+ Treg 浸润——循环 Treg 升高（P=0.045）——COX-2 阳性 75%——支持 FOSCC 作为免疫治疗相关的 HNSCC 模型"
  implicit_premise: "假设免疫浸润模式相似性意味着免疫治疗反应可转化；假设小样本量足以得出有意义的结论"
  unexpected_finding: "57% FOSCC 有 Treg 浸润且循环 Treg 升高——这种 Treg 富集提示免疫抑制性肿瘤微环境——可能解释 FOSCC 对免疫治疗反应差"
  title_gap: "标题说调查 FOSCC 中的免疫细胞标记物，但真正发现是 Treg 富集：T 细胞浸润高（92%）但包含大量 Treg（57%）——局部和全身 Treg 升高——为免疫治疗靶向策略提供依据"
  evidence_boundary: "小样本免疫分析研究（n=12 IHC，n=9 流式）；支持肿瘤微环境特征和比较肿瘤学价值，不支持预后相关或免疫治疗反应预测"
---

# Investigation of immune cell markers in feline oral squamous cell carcinoma

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 2018 Vet Immunol Immunopathol: n=12 IHC, n=9 flow cytometry; 92% CD3+ T cells; 57% FoxP3+ Tregs; elevated circulating Tregs vs controls (P=0.045); COX-2+ in 75%; supports FOSCC as HNSCC immunotherapy model. [Deep extraction worksheet](../../system/indexes/src-cancer-074-deep-extraction-round1.md).

## Source Check, 2026-06-02

| Field | Value |
|-------|-------|
| PMID | 30078599 |
| DOI | 10.1016/j.vetimm.2018.06.011 |
| Journal | Vet Immunol Immunopathol |
| Year | 2018 |
| Authors | Sparger EE, Murphy BG, Kamal FM, et al. |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Cohort 1 | 12 patients, IHC analysis |
| T cell infiltrates (CD3+) | 92% positive (epithelium + stroma) |
| B cell infiltrates | CD79a/CD20+ in stroma only |
| Treg infiltrates (FoxP3+) | 57% positive (epithelium + stroma) |
| COX-2 expression | 75% positive (weak, epithelium + stroma) |
| Cohort 2 | 9 patients, blood analysis |
| Circulating Tregs | Increased CD4+FoxP3+ vs healthy controls (P=0.045) |
| Histologic subtypes | 75% conventional (50% well-differentiated, 50% moderately differentiated) |

**Boundary:** Abstract-level extraction. Immune infiltration patterns can inform FOSCC immunology claims. Prognostic correlations not detected due to small sample sizes.

## One-Line Summary

92% of FOSCC show T cell infiltrates; 57% have Treg (FoxP3+) infiltration; circulating Tregs elevated vs controls—supports FOSCC as immunotherapy-relevant HNSCC model.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- T cell infiltrates (CD3+) in 92% of biopsies (epithelium + stroma)
- B cell infiltrates (CD79a/CD20+) in stroma only
- Treg infiltrates (FoxP3+) in 57% of biopsies
- COX-2 positive (weak) in 75% of neoplastic epithelium
- Increased circulating CD4+FoxP3+ T cells in OSCC patients vs healthy controls (P=0.045)
- Histologic subtypes: 75% conventional (well/moderately differentiated)

### source_supported_conclusion

- Feline OSCC shares immune marker profiles with human HNSCC
- Treg enrichment suggests immunosuppressive tumor microenvironment
- COX-2 expression supports inflammation role in FOSCC
- Immune profiling provides foundation for immunotherapy target development

### llm_inference

- Strong support for oral-squamous-cell-carcinoma.md tumor microenvironment claims
- Treg enrichment aligns with findings in feline mammary cancer (src-cancer-043)
- May inform future immunotherapy approaches for FOSCC

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
