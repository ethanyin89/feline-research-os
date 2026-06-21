---
id: src-cancer-085
type: source
title: "Evaluation of long-term outcome and prognostic factors of feline squamous cell carcinomas treated with photodynamic therapy using liposomal phosphorylated meta-tetra(hydroxylphenyl)chlorine"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2018
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: 29359611
tags: [cancer, FOSCC, SCC, PDT, photodynamic-therapy, mTHPC, treatment, prognosis]
links:
  doi: "10.1177/1098612X17752196"
  url: "https://aacrjournals.org/clincancerres/article/11/20/7538/188533/Optimizing-Photodynamic-Therapy-In-vivo"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "63 lesions in 38 cats treated with PDT using liposomal mTHPC."
    - "Overall response rate 84% (CR 61%, PR 22%)."
    - "Mean progression-free interval 35 months; median OS 40 months."
    - "Invasive tumours: highly significant worse outcome (P<0.017); all progressed <6 months."
  source_supported_conclusion:
    - "PDT using systemic photosensitiser leads to excellent long-term tumour control in majority of cats."
    - "Invasive and large tumours have clearly inferior outcome."
    - "Advanced lesions are not good indications for PDT."
  llm_inference:
    - "Strong evidence for PDT efficacy in early-stage feline SCC."
    - "Supports oral-squamous-cell-carcinoma.md treatment section."
  # V2 enhanced fields
  study_design: "回顾性病例系列（2018 年 JFMS），38 只猫 63 个病变，脂质体 mTHPC 光动力治疗，长期随访"
  core_argument: "PDT 在非侵袭性猫 SCC 中实现优秀的长期控制——总反应率 84%（CR 61%，PR 22%）——中位 PFI 35 个月——中位 OS 40 个月——但侵袭性肿瘤预后差（全部 <6 个月进展）"
  implicit_premise: "假设回顾性病例系列的疗效数据可代表前瞻性治疗预期；假设病例选择（非侵袭性）偏倚可接受"
  unexpected_finding: "侵袭性肿瘤与非侵袭性肿瘤结局差异巨大——所有侵袭性肿瘤 <6 个月进展——这是强烈的病例选择信号：PDT 不适用于晚期病变"
  title_gap: "标题说评估 PDT 治疗猫 SCC 的长期结局和预后因素，但真正发现是适应证限制：PDT 对早期/非侵袭性病变有效——但侵袭性和大肿瘤不是好适应证——病例选择至关重要"
  evidence_boundary: "回顾性病例系列证据（n=38 猫，63 病变）；支持 PDT 在早期 SCC 中的疗效声明，但仅限于非侵袭性病变——晚期病变不推荐 PDT"
---

# Evaluation of long-term outcome and prognostic factors of feline squamous cell carcinomas treated with photodynamic therapy

## Source Check, 2026-06-03

| Field | Value |
|-------|-------|
| PMID | 29359611 |
| DOI | 10.1177/1098612X17752196 |
| Journal | J Feline Med Surg |
| Year | 2018 |
| Authors | Flickinger I, Gasymova E, Dietiker-Moretti S, et al. |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Sample size | 63 lesions in 38 cats |
| Treatment | PDT with liposomal mTHPC; ≤10 J/cm² or 20 J/cm² |
| Overall response | 84% (CR 61%, PR 22%) |
| Progression-free interval | Mean 35 months (median not reached) |
| Overall survival | Median 40 months (95% CI 33-47) |
| Poor prognostic | Invasive tumours (P<0.017); all progressed <6 months |
| Tumor size | Larger lesions associated with inferior control |

**Boundary:** Abstract-level extraction. PDT efficacy data can inform FOSCC treatment claims; limited to non-invasive/early lesions.

## One-Line Summary

PDT with mTHPC in 38 cats (63 lesions): 84% response rate, median OS 40 months; invasive tumors have poor outcome (all progress <6 months).

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- 63 lesions in 38 cats treated with PDT using liposomal mTHPC
- Dose groups: ≤10 J/cm² (n=22) and 20 J/cm² (n=41)
- Overall response rate 84%: complete remission 61%, partial remission 22%
- Mean progression-free interval 35 months; median OS 40 months (95% CI 33-47)
- Invasive tumours: highly significant worse outcome (P<0.017)
- All patients with invasive tumours progressed <6 months

### source_supported_conclusion

- PDT with systemic photosensitiser leads to excellent long-term tumour control
- Invasive and large tumours have clearly inferior outcome regardless of dose
- Advanced lesions are not good indications for PDT
- Treatment intensity and tumour location did not influence response

### llm_inference

- Strong evidence for PDT efficacy in early-stage, non-invasive feline SCC
- Case selection critical: exclude invasive/large tumours
- Supports oral-squamous-cell-carcinoma.md treatment section

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
