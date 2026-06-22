---
id: src-cancer-010
type: source
title: "Oncolytic virotherapy of canine and feline cancer"
source_kind: paper
species: [feline, canine]
diseases: [cancer, fibrosarcoma, mammary-carcinoma, soft-tissue-sarcoma]
models: [mouse-xenograft, clinical-trial]
endpoints: [tumor-regression, recurrence-prevention, immune-response]
evidence_level: review
year: 2014
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: bilingual_checked
tags: [cancer, oncolytic-virotherapy, adenovirus, vaccinia, poxvirus, myxoma, fibrosarcoma, mammary-carcinoma, IL-12, VEGF, tumor-immunology, experimental-therapy]
links:
  doi: "10.3390/v6052122"
  url: "https://www.mdpi.com/1999-4915/6/5/2122"
  pmc: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4036544/"
  local_assets:
    - "raw/images/cancer/src-cancer-010-fig1.jpg"
abstract: "Cancer is the leading cause of disease-related death in companion animals such as dogs and cats. Despite recent progress in the diagnosis and treatment of advanced canine and feline cancer, overall patient treatment outcome has not been substantially improved. Virotherapy using oncolytic viruses is one promising new strategy for cancer therapy. Oncolytic viruses (OVs) preferentially infect and lyse cancer cells, without causing excessive damage to surrounding healthy tissue, and initiate tumor-specific immunity. The current review describes the use of different oncolytic viruses for cancer therapy and their application to canine and feline cancer."
methods_summary: "A narrative review analyzing the clinical and preclinical studies of oncolytic virotherapy (OVs) in canine and feline oncology. It reviews preclinical studies in cell lines and mouse-xenograft models (e.g. vaccinia GLV-5b451 in feline mammary carcinoma xenografts) and clinical trials in feline patients (e.g. ALVAC-fIL2 and NYVAC-fIL2 combined with surgery/radiotherapy for feline fibrosarcomas)."
evidence_policy:
  quoted_fact:
    - "Oncolytic viruses (OVs) preferentially infect and lyse cancer cells, without causing excessive damage to surrounding healthy tissue, and initiate tumor-specific immunity."
    - "When combined with surgery and radiotherapy, treatment with either of these viruses [ALVAC-fIL2 and NYVAC-fIL2] prevented feline fibrosarcoma recurrence in cats."
    - "Both wild type and genetically engineered oncolytic virus therapy appears to be as safe as standard anti cancer therapies."
    - "There are very few clinical trials using OVs for canine or feline cancer patients."
  source_supported_conclusion:
    - "ALVAC-fIL2 and NYVAC-fIL2 combined with surgery and radiotherapy prevent or delay recurrence of feline fibrosarcomas."
    - "Vaccinia virus GLV-5b451 encoding anti-VEGF has demonstrated preclinical efficacy in feline mammary carcinoma xenografts."
    - "Oncolytic virotherapy is generally safe, showing a side-effect profile comparable to standard oncological therapies."
  llm_inference:
    - "Immunotherapy and gene-delivery OVs (such as IL-12 vectors) present a promising future direction for enhancing local antitumoral immunity in cats."
  # V2 enhanced fields
  study_design: "叙述性综述，分析溶瘤病毒治疗在犬猫肿瘤学中的临床前和临床研究"
  core_argument: "溶瘤病毒（OVs）选择性感染和裂解癌细胞并启动肿瘤特异性免疫——ALVAC/NYVAC-fIL2 联合手术和放疗可预防猫纤维肉瘤复发"
  implicit_premise: "假设临床前小鼠异种移植模型的疗效可外推至自发性猫肿瘤；假设安全性数据足以支持临床应用"
  unexpected_finding: "尽管溶瘤病毒疗法显示出良好的安全性，但犬猫癌症的临床试验极少——技术成熟度与临床应用之间存在巨大差距"
  title_gap: "标题说犬猫癌症的溶瘤病毒治疗，但真正发现是临床应用悖论：ALVAC-fIL2 已在临床试验中证明可预防猫纤维肉瘤复发，安全性与标准疗法相当——但实际临床试验极少，技术潜力远未转化"
  evidence_boundary: "2014 年综述，不包含后续临床试验进展；多数数据来自临床前模型而非猫患者队列"
---

# Oncolytic virotherapy of canine and feline cancer

## Evidence-Depth Caveat

This card is based on the complete publication text. It is deep-extracted as a narrative and clinical review.

## One-Line Summary

A comprehensive review of oncolytic virotherapy in veterinary medicine, highlighting that ALVAC/NYVAC-fIL2 combined with surgery and radiotherapy prevents recurrence in feline fibrosarcomas.

## Why It Matters For Feline Cancer

Oncolytic virotherapy represents an innovative class of feline cancer immunotherapy. This review provides the primary clinical evidence for poxvirus-based recurrence prevention in feline fibrosarcomas, as well as preclinical data on adenoviral and vaccinia treatments.

## Key Findings

### quoted_fact

* "When combined with surgery and radiotherapy, treatment with either of these viruses [ALVAC-fIL2 and NYVAC-fIL2] prevented feline fibrosarcoma recurrence in cats."
* "Both wild type and genetically engineered oncolytic virus therapy appears to be as safe as standard anti cancer therapies."
* "There are very few clinical trials using OVs for canine or feline cancer patients."

### source_supported_conclusion

* Poxvirus vectors ALVAC-fIL2 and NYVAC-fIL2 demonstrate clinical efficacy in preventing recurrence of feline fibrosarcoma when used as adjuvant therapy with surgery and radiotherapy.
* GLV-5b451 (vaccinia virus expressing anti-VEGF single-chain antibody) shows preclinical efficacy in feline mammary carcinoma mouse xenografts.
* Oncolytic virotherapy has a highly favorable safety profile in cats, comparable to traditional therapies.

### llm_inference

* Given the lack of widespread clinical trials, OV therapies remain experimental and should be considered as adjunctive, rather than alternative, to standard-of-care surgical resection and radiation therapy.

## Study Design Details

### Mechanisms of Oncolytic Virotherapy

![Possible mechanisms of oncolytic virus mediated tumor ablation](../../raw/images/cancer/src-cancer-010-fig1.jpg)

### Overview of Feline Applications

| Virus Family | Specific Agent | Feline Tumor Type | Stage of Evidence |
|---|---|---|---|
| Poxvirus | ALVAC-fIL2, NYVAC-fIL2 | Fibrosarcoma | **Clinical Trial** (Adjuvant) |
| Poxvirus | GLV-5b451 (anti-VEGF) | Mammary Carcinoma | Preclinical (Xenograft) |
| Adenovirus | Ad5-hsp-fIL-12 | Soft Tissue Sarcoma | Preclinical (In Vivo) |
| Poxvirus | Myxoma virus | Mammary Carcinoma / Fibrosarcoma | Preclinical (In Vitro) |

## Linked Entities

- diseases: [cancer, fibrosarcoma, mammary-carcinoma, soft-tissue-sarcoma]
- models: [mouse-xenograft, clinical-trial]
- endpoints: [tumor-regression, recurrence-prevention, immune-response]
- mechanisms: [oncolysis, anti-VEGF, IL-12-immunotherapy]
