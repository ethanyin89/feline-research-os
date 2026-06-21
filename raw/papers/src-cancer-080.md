---
id: src-cancer-080
type: source
title: "A novel MCT1 and MCT4 dual inhibitor reduces mitochondrial metabolism and inhibits tumour growth of feline oral squamous cell carcinoma"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2020
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: 31661586
tags: [cancer, FOSCC, MCT1, MCT4, metabolism, targeted-therapy, HNSCC-model, investigational]
links:
  doi: "10.1111/vco.12551"
  url: "https://doi.org/10.1111/vco.12551"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "MD-1 reduced viability of feline OSCC and human HNSCC cell lines in vitro."
    - "MD-1 altered glycolytic and mitochondrial metabolism."
    - "MD-1 synergized with platinum-based chemotherapies."
    - "MD-1 significantly inhibited tumour growth in subcutaneous xenograft model."
    - "MD-1 prolonged overall survival in orthotopic model of feline OSCC."
  source_supported_conclusion:
    - "MCT1/MCT4 dual inhibitor MD-1 shows preclinical efficacy in feline OSCC."
    - "Feline OSCC is a valid large animal model for MCT inhibitor development."
  llm_inference:
    - "Novel targeted therapy approach for FOSCC."
    - "Supports oral-squamous-cell-carcinoma.md investigational therapy section."
  # V2 enhanced fields
  study_design: "临床前研究（2020 年 Vet Comp Oncol），MCT1/MCT4 双重抑制剂 MD-1 在猫 OSCC 细胞系、异种移植和原位模型中的评估"
  core_argument: "MCT1/MCT4 双重抑制剂 MD-1 在猫 OSCC 中显示临床前疗效——体外降低活力、改变代谢、与铂类协同——体内抑制异种移植生长并延长原位模型生存——猫 OSCC 是人类 HNSCC MCT 抑制剂开发的有效大动物模型"
  implicit_premise: "假设体外/异种移植疗效可转化为临床获益；假设 MCT 靶向在猫体内与模型中类似有效"
  unexpected_finding: "MD-1 未改变猫 OSCC 细胞中的乳酸水平——这表明 MCT 非依赖性活性——机制比单纯 MCT 抑制更复杂"
  title_gap: "标题说新型 MCT1/MCT4 双重抑制剂降低线粒体代谢并抑制猫 OSCC 肿瘤生长，但真正发现是双重的：1）临床前疗效信号强；2）机制部分 MCT 非依赖性——需要进一步研究"
  evidence_boundary: "临床前证据（细胞系、异种移植、原位模型）；支持研究性治疗背景和比较肿瘤学模型价值，不支持临床治疗推荐"
---

# A novel MCT1 and MCT4 dual inhibitor reduces mitochondrial metabolism and inhibits tumour growth of feline oral squamous cell carcinoma

## Source Check, 2026-06-03

| Field | Value |
|-------|-------|
| PMID | 31661586 |
| DOI | 10.1111/vco.12551 |
| Journal | Vet Comp Oncol |
| Year | 2020 |
| Authors | Khammanivong A, Saha J, Spartz AK, et al. |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Target | MCT1 and MCT4 monocarboxylate transporters |
| Drug | MD-1 (dual MCT1/MCT4 inhibitor) |
| In vitro | Reduced viability, altered metabolism, synergized with platinum |
| In vivo | Inhibited xenograft growth, prolonged survival in orthotopic model |
| Mechanism | Altered glycolytic and mitochondrial metabolism |
| Model value | Supports feline OSCC as large animal model for human HNSCC |

**Boundary:** Abstract-level extraction. Preclinical study; investigational therapy not yet in clinical use.

## One-Line Summary

MCT1/MCT4 dual inhibitor MD-1 shows preclinical efficacy in feline OSCC: reduced viability, synergy with platinum, prolonged survival in orthotopic model.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- MD-1 reduced viability of feline OSCC and human HNSCC cell lines in vitro
- MD-1 altered glycolytic and mitochondrial metabolism
- MD-1 synergized with platinum-based chemotherapies
- MD-1 significantly inhibited tumour growth in subcutaneous xenograft model
- MD-1 prolonged overall survival in orthotopic model of feline OSCC
- MD-1 failed to alter lactate levels in feline OSCC cells (MCT-independent activity)

### source_supported_conclusion

- MCT1/MCT4 dual inhibition is a viable therapeutic strategy for feline OSCC
- Feline OSCC is a valid large animal model for MCT inhibitor development in human HNSCC
- Combination with platinum chemotherapy may enhance efficacy

### llm_inference

- Novel targeted therapy approach; preclinical stage
- Supports oral-squamous-cell-carcinoma.md investigational therapy claims
- MCT-independent mechanism in feline cells warrants further investigation

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
