---
id: src-cancer-100
type: source
title: "High Drug Resistance in Feline Mammary Carcinoma Cell Line (FMCm) and Comparison with Human Breast Cancer Cell Line (MCF-7)"
source_kind: paper
species: feline
diseases: [cancer]
models: [human-breast-cancer, MCF-7]
endpoints: [drug-resistance, cell-viability, IC50]
jurisdictions: [Portugal]
evidence_level: original-study
year: 2021
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
pmid: "34438778"
pmcid: "PMC8388478"
doi: "10.3390/ani11082321"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, mammary, FMC, drug-resistance, 5-FU, chloroquine, verapamil, itraconazole, chemotherapy, repurposing]
links:
  doi: "10.3390/ani11082321"
  url: "https://www.mdpi.com/2076-2615/11/8/2321"
  pmc: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8388478/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The feline neoplastic cells demonstrated considerable resistance to the drugs tested in isolation, and the combination was not effective, which contrasted with the obtained MCF-7 cells' response."
    - "In MCF-7 cells, the drug with more efficacy regarding cell viability reduction was chloroquine (6.5 ± 0.4% of cellular viability)."
    - "5-FU in combination with verapamil and itraconazole led to a reduction in cellular viability of 23% for verapamil and 17% for itraconazole in MCF-7."
    - "Drug repurposing and drug combination are important therapeutic approaches in cancer therapy."
  source_supported_conclusion:
    - "FMCm cell line is highly drug resistant compared to human MCF-7 cells."
    - "Drug combinations effective in MCF-7 (5-FU + verapamil, 5-FU + itraconazole) were not effective in FMCm."
    - "FMC drug resistance may explain poor clinical response to chemotherapy."
    - "Different therapeutic strategies may be needed for FMC vs human breast cancer."
  llm_inference:
    - "FMC drug resistance may relate to triple-negative phenotype and efflux pump expression."
    - "Novel drug combinations or targets are needed for effective FMC therapy."
    - "MCF-7 (ER+) vs FMCm comparison may not reflect TNBC-specific resistance."
  # V2 enhanced fields
  study_design: "体外比较研究（2021 年 Animals），FMCm 猫乳腺癌细胞系 vs MCF-7 人乳腺癌细胞系，5-FU 联合药物重定位策略"
  core_argument: "FMCm 细胞系表现出高度耐药性——与 MCF-7 形成鲜明对比——在 MCF-7 中有效的药物组合（5-FU + 维拉帕米/伊曲康唑）在 FMCm 中无效——这可能解释 FMC 对化疗的临床不良反应"
  implicit_premise: "假设单细胞系结果可代表整体 FMC 耐药性；假设 MCF-7（ER+）是适当的比较对象——但 FMCm 是 TNBC 样"
  unexpected_finding: "FMCm 对几乎所有测试药物和组合都表现出耐药——不仅是单药无效，联合用药也无效——暗示 FMC 可能需要完全不同的治疗策略"
  title_gap: "标题说 FMC 细胞系的高耐药性及与 MCF-7 的比较，但真正发现是翻译差距：人乳腺癌有效的策略不能简单移植到 FMC——可能需要针对 FMC 特异性耐药机制的新方法"
  evidence_boundary: "体外单细胞系证据；支持 FMC 耐药性概念，但不支持临床治疗推荐——体外到体内转化和多细胞系验证需要"
---

# High Drug Resistance in Feline Mammary Carcinoma Cell Line (FMCm) and Comparison with Human Breast Cancer Cell Line (MCF-7)

## Evidence-Depth Caveat

**Deep-extracted from PMC full text (PMC8388478).** This 2021 study demonstrates FMCm cells are highly drug resistant compared to MCF-7. Drug combinations effective in MCF-7 (5-FU + verapamil/itraconazole) were ineffective in FMCm. Evidence level: in vitro comparative study.

## Source Check, 2026-06-09

Europe PMC full text extraction.

| Field | Value |
|-------|-------|
| PMID | 34438778 |
| PMCID | PMC8388478 |
| DOI | 10.3390/ani11082321 |
| Journal | Animals (MDPI) |
| Year | 2021 |
| Authors | Correia AS, Matos R, Gärtner F, Amorim I, Vale N |
| Open access | yes |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Study type | Cell line comparative study |
| Cell lines | FMCm (feline) vs MCF-7 (human ER+) |
| Drugs tested | 5-FU + repurposed drugs (verapamil, itraconazole, chloroquine, etc.) |
| MCF-7 response | Chloroquine 6.5% viability; 5-FU combinations effective |
| FMCm response | High resistance; combinations not effective |

**Boundary:** In vitro evidence. FMCm is metastatic TNBC-like; MCF-7 is ER+. Comparison has limitations.

## One-Line Summary

FMCm cells show high drug resistance vs MCF-7; 5-FU + verapamil/itraconazole combinations ineffective in FMC despite efficacy in human cells.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- Drug repurposing and drug combination are important therapeutic approaches in cancer therapy
- FMCm cell line compared with MCF-7 human breast cancer cell line
- FMCm shows high drug resistance

### source_supported_conclusion

- FMC cell lines may be more drug resistant than human equivalents
- Drug combination strategies may be needed for effective FMC treatment
- Comparative oncology approach validates feline model

### llm_inference

- May inform mammary-carcinoma.md chemotherapy resistance section
- Supports drug combination strategies over single-agent therapy
- Explains poor response to standard chemotherapy in clinical FMC cases

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
