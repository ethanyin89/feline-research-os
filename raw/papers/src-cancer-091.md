---
id: src-cancer-091
type: source
title: "Emerging Biomarkers and Targeted Therapies in Feline Mammary Carcinoma"
source_kind: paper
species: feline
diseases: [cancer]
models: [human-breast-cancer, human-HER2+, human-TNBC]
endpoints: [targeted-therapy, biomarkers, prognosis]
jurisdictions: [Portugal]
evidence_level: review
year: 2021
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
pmid: "34437486"
pmcid: "PMC8402877"
doi: "10.3390/vetsci8080164"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, mammary, FMC, HER2, TNBC, lapatinib, trastuzumab, pertuzumab, TKI, HDACi, biomarkers, targeted-therapy, review]
links:
  doi: "10.3390/vetsci8080164"
  url: "https://www.mdpi.com/2306-7381/8/8/164"
  pmc: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8402877/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "HER2-positive subtype is one of the most common in the cat (33% to 60% of all cases)."
    - "HER2-negative breast cancer has a reported rate of incidence of 70% in the cat."
    - "Feline and human HER2 share a 90% to 95% homology."
    - "Lapatinib exposure demonstrated a dose-dependent antiproliferative effect with a conserved mechanism of action."
    - "The feline HER2-negative cell line (FMCp) presented a 100% cytotoxic response to lapatinib."
    - "Combination therapy with pertuzumab and lapatinib shows synergistic effect in FMC cell-based models."
    - "Several HDACis and MTis show a dose-dependent antiproliferative effect and conserved cell death mechanism."
  source_supported_conclusion:
    - "FMC is a valid model for HER2-positive and triple-negative human breast cancer."
    - "TKIs (lapatinib, neratinib) show promising cytotoxic effects in FMC cells."
    - "Combination therapies (pertuzumab + lapatinib, trastuzumab + lapatinib) show synergistic effects."
    - "HDACis and MTis are promising agents for FMC molecular targeted therapy."
    - "FMC therapeutic options are limited to mastectomy and adjuvant protocols with limited success."
  llm_inference:
    - "Human HER2-targeted therapies may translate to FMC given 90-95% homology."
    - "Multi-target combination therapies may overcome single-agent resistance."
    - "Checkpoint inhibitors (anti-PD1) represent emerging therapeutic avenue."
  # V2 enhanced fields
  study_design: "综合综述（2021 年 Vet Sci），FMC 生物标志物和靶向治疗综述，葡萄牙研究团队"
  core_argument: "FMC 是研究 HER2+ 和三阴性人类乳腺癌的有效模型——HER2+ 占 33-60%——猫/人 HER2 同源性 90-95%——TKIs（拉帕替尼、奈拉替尼）和 mAbs（曲妥珠单抗、帕妥珠单抗）在体外显示疗效——联合治疗有协同效应"
  implicit_premise: "假设体外疗效可转化为临床疗效；假设人类 HER2 靶向药物的作用机制在猫中保守；假设 90-95% 同源性足以预测药物反应"
  unexpected_finding: "HER2 阴性细胞系（FMCp）对拉帕替尼显示 100% 细胞毒性反应——暗示 TKIs 可能通过非 HER2 靶点也有效——这扩展了潜在治疗人群"
  title_gap: "标题说 FMC 中新兴的生物标志物和靶向治疗，但真正发现是治疗策略框架：单药治疗 → 联合治疗 → 多靶点策略——HDACis 和 MTis 是新兴候选药物——但仍需要临床验证"
  evidence_boundary: "综述文章综合体外数据；支持靶向治疗研究方向和比较肿瘤学框架，不支持临床治疗推荐——体外到体内转化尚未证明"
---

# Emerging Biomarkers and Targeted Therapies in Feline Mammary Carcinoma

## Evidence-Depth Caveat

**Deep-extracted from PMC full text (PMC8402877).** Comprehensive 2021 review of FMC biomarkers and targeted therapies. HER2+ prevalence 33-60%; 70% HER2-negative. Covers TKIs (lapatinib, neratinib), mAbs (trastuzumab, pertuzumab), HDACis, MTis. Evidence level: narrative review with in vitro data synthesis.

## Source Check, 2026-06-09

Europe PMC full text extraction.

| Field | Value |
|-------|-------|
| PMID | 34437486 |
| PMCID | PMC8402877 |
| DOI | 10.3390/vetsci8080164 |
| Journal | Vet Sci (MDPI) |
| Year | 2021 |
| Authors | Gameiro A, Urbano AC, Ferreira F |
| Open access | yes |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Article type | Comprehensive review |
| HER2+ prevalence | 33-60% of FMC |
| HER2- prevalence | 70% of FMC |
| HER2 homology | 90-95% feline/human |
| TKIs tested | Lapatinib, neratinib (dose-dependent cytotoxicity) |
| Combination therapy | Pertuzumab + lapatinib, trastuzumab + lapatinib (synergistic) |
| Novel agents | HDACis, MTis (dose-dependent antiproliferative) |

**Boundary:** Review synthesizing in vitro evidence. Clinical translation not yet demonstrated.

## One-Line Summary

2021 comprehensive review: HER2+ (33-60%) and TNBC (70%) FMC subtypes; TKIs/mAbs show in vitro efficacy; FMC validated as HER2+/TNBC breast cancer model.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- FMC is a common aggressive malignancy with low survival rate
- Lacks viable therapeutic options beyond mastectomy
- Increasing efforts to understand molecular mechanisms using human breast cancer knowledge
- Reviews HER2-positive and triple-negative FMC subtypes
- Cat reinforced as cancer model for human breast cancer

### source_supported_conclusion

- Comprehensive review of FMC pathogenesis, biomarkers, and prognosis factors
- Molecular subtyping (HER2+, triple-negative) relevant for targeted therapy selection
- Novel therapeutic insights for specific FMC subtypes

### llm_inference

- Key review for mammary-carcinoma.md molecular subtyping and targeted therapy claims
- Full-text would provide specific biomarker panel recommendations
- Supports comparative oncology approach to FMC research

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
