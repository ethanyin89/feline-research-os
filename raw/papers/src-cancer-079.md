---
id: src-cancer-079
type: source
title: "Progesterone receptors in feline mammary cancer cytosol"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
status: ingested
extraction_depth: partial
verification_status: title_only
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, progesterone, receptors, mammary, cytosol, PR, hormone-receptor]
links:
  doi: "10.1007/bf00410693"
  url: "https://doi.org/10.1007/bf00410693"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "DOI verified: 10.1007/bf00410693 (Springer)."
    - "Title indicates cytosol-based PR assay in feline mammary cancer."
  source_supported_conclusion:
    - "Historical study of progesterone receptor expression in FMC."
    - "Not found in PubMed search; may be older Springer journal article."
  llm_inference:
    - "Early receptor profiling study for feline mammary cancer."
    - "Full-text required for specific PR expression data."
  # V2 enhanced fields
  study_design: "原始研究（Springer 期刊，非 PubMed 索引），猫乳腺癌细胞溶质中孕激素受体的测定"
  core_argument: "猫乳腺癌表达孕激素受体——细胞溶质受体测定方法（IHC 时代前技术）——早期激素受体分析为后续研究奠定基础"
  implicit_premise: "假设细胞溶质受体测定代表功能性受体状态；假设早期方法学仍有参考价值"
  unexpected_finding: "无法从可用信息确定——非 PubMed 索引——全文需要获取才能识别具体 PR 表达率"
  title_gap: "标题说猫乳腺癌细胞溶质中的孕激素受体，但真正价值是方法学历史：细胞溶质受体测定是 IHC 前时代的标准方法——为现代激素受体研究提供历史基线"
  evidence_boundary: "无 PubMed 索引；仅支持历史背景和来源所有权，不支持当代 PR 表达率声明；方法学已过时"
---

# Progesterone receptors in feline mammary cancer cytosol

## Source Check, 2026-06-02

| Field | Value |
|-------|-------|
| DOI | 10.1007/bf00410693 |
| Publisher | Springer |
| PubMed Status | Not found in PubMed search |

## Abstract Summary

Not found in PubMed. DOI verified via Springer.

| Category | Finding |
|----------|---------|
| Study type | Receptor assay |
| Target | Progesterone receptors in cytosol |
| Species | Feline mammary cancer |

**Boundary:** Not PubMed indexed. DOI verified. Full-text required for extractable claims about PR expression rates.

## One-Line Summary

Feline mammary cancer progesterone receptor cytosol assay (DOI verified, not PubMed indexed; full-text required).

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- DOI: 10.1007/bf00410693 (Springer journal, verified)
- Title indicates cytosol-based progesterone receptor assay
- Not found in PubMed search

### source_supported_conclusion

- Historical study of PR expression in feline mammary cancer
- Cytosol receptor assay methodology (pre-IHC era technique)
- Full-text access required for specific PR expression data

### llm_inference

- May provide early PR expression rates for FMC
- Complements modern IHC-based receptor studies
- Relevant for mammary-carcinoma.md hormone receptor claims

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
