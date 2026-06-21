---
id: src-cancer-032
type: source
title: "BB-Cl-Amidine as a novel therapeutic for canine and feline mammary cancer via activation of the endoplasmic reticulum stress pathway"
source_kind: paper
species: [feline, canine]
diseases: [cancer]
models: [mouse-xenograft]
endpoints: [cell-viability, tumorigenicity, ER-stress]
jurisdictions: [USA]
evidence_level: original-study
year: 2018
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
pmid: "29649984"
pmcid: "PMC5898062"
doi: "10.1186/s12885-018-4323-8"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, mammary, FMC, BB-Cl-Amidine, PAD-inhibitor, ER-stress, GRP78, DDIT3, in-vitro, xenograft, therapeutic]
links:
  doi: "10.1186/s12885-018-4323-8"
  url: "https://doi.org/10.1186/s12885-018-4323-8"
  pmc: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5898062/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "BB-CLA reduced viability and tumorigenicity of canine and feline mammary cancer cell lines in vitro."
    - "BB-CLA activates the endoplasmic reticulum stress pathway in these cells by downregulating 78 kDa Glucose-regulated Protein (GRP78) and upregulating the downstream target gene DNA Damage Inducible Transcript 3 (DDIT3)."
    - "GRP78 is a potential target in breast cancer for molecular therapy."
    - "We established a mouse xenograft model of both canine and feline mammary cancer in which we preliminarily tested the effects of BB-CLA in vivo."
  source_supported_conclusion:
    - "BB-Cl-Amidine (PAD inhibitor) is cytotoxic to feline and canine mammary cancer cells in vitro."
    - "Mechanism: ER stress pathway activation via GRP78 downregulation and DDIT3 upregulation."
    - "Mouse xenograft models established for future in vivo FMC/CMC therapeutic testing."
    - "PAD inhibition represents a novel therapeutic target for companion animal mammary cancer."
  llm_inference:
    - "In vitro only for cytotoxicity; xenograft results described as 'preliminary' — clinical translation requires further studies."
    - "GRP78 targeting may have broader applicability across FMC subtypes."
    - "Combination with existing chemotherapy (doxorubicin, carboplatin) not yet tested."
  # V2 enhanced fields
  study_design: "原始研究（2018 年 BMC Cancer），体外细胞系研究 + 小鼠异种移植初步测试，PAD 抑制剂 BB-Cl-Amidine 对犬猫乳腺癌细胞的作用"
  core_argument: "BB-Cl-Amidine（PAD 抑制剂）通过激活内质网应激通路（下调 GRP78、上调 DDIT3）在体外降低犬猫乳腺癌细胞活力和成瘤性——GRP78 是乳腺癌分子治疗的潜在靶点"
  implicit_premise: "假设体外细胞毒性可转化为临床疗效；假设内质网应激激活是足够的抗肿瘤机制而非仅仅是非特异性细胞毒性"
  unexpected_finding: "PAD 酶抑制通过内质网应激通路杀死乳腺癌细胞——这一机制连接了表观遗传调控（蛋白质瓜氨酸化）与细胞死亡通路——不同于传统化疗靶点"
  title_gap: "标题说 BB-Cl-Amidine 作为新型犬猫乳腺癌治疗药物，但真正发现是机制验证：GRP78 下调和 DDIT3 上调定义了内质网应激激活机制——但临床转化仍需后续研究"
  evidence_boundary: "主要是体外证据；异种移植结果描述为'初步'；2 周体内测试不足以评估临床疗效；与现有化疗（多柔比星、卡铂）的联合用药未测试"
---

# BB-Cl-Amidine as a novel therapeutic for canine and feline mammary cancer via activation of the endoplasmic reticulum stress pathway

## Evidence-Depth Caveat

**Deep-extracted from PMC full text (PMC5898062).** This 2018 study demonstrates BB-Cl-Amidine (PAD inhibitor) reduces FMC/CMC cell viability in vitro via ER stress pathway (GRP78 downregulation, DDIT3 upregulation). Includes preliminary mouse xenograft data. Evidence level: in vitro + preliminary in vivo. Not clinical guidance.

## Source Check, 2026-06-09

Europe PMC full text extraction.

- PMID: 29649984
- PMCID: PMC5898062
- DOI: 10.1186/s12885-018-4323-8
- Journal: BMC Cancer
- Year: 2018
- Open access: yes

## Abstract Summary

This study evaluated BB-Cl-Amidine (BB-CLA), a peptidylarginine deiminase (PAD) inhibitor, as a novel therapeutic approach for canine and feline mammary cancer.

**Mechanism of action:**
- BB-Cl-Amidine inhibits PAD enzymes
- Activates the endoplasmic reticulum (ER) stress pathway
- Downregulates GRP78 (78 kDa Glucose-regulated Protein) — a breast cancer molecular therapy target
- Upregulates DDIT3 (DNA Damage Inducible Transcript 3)
- ER stress activation leads to cancer cell death

**Efficacy findings:**
- Reduces viability of canine mammary cancer cells in vitro
- Reduces viability of feline mammary cancer cells in vitro
- Reduces tumorigenicity in vitro
- Preliminary in vivo testing in mouse xenograft models established

**Mouse xenograft models:**
- NSG mouse xenografts created using canine and feline mammary cancer cell lines
- BB-CLA tested for 2 weeks in vivo (preliminary)

**Therapeutic implications:**
- PAD inhibition represents a novel therapeutic target
- GRP78 is an actionable molecular target
- ER stress pathway activation as anti-cancer mechanism
- Mouse xenograft models established for future FMC/CMC therapeutic testing

**Boundary:** Primarily in vitro evidence; xenograft results described as "preliminary." Not clinical guidance.

## One-Line Summary

BB-Cl-Amidine (PAD inhibitor) reduces FMC/CMC cell viability in vitro via ER stress (GRP78↓, DDIT3↑); mouse xenograft models established for future therapeutic testing.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: BB-Cl-Amidine as a novel therapeutic for canine and feline mammary cancer via activation of the endoplasmic reticulum stress pathway.
- The intake sheet locator is: 10.1186/s12885-018-4323-8.

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
