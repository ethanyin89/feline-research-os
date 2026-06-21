---
id: src-fip-031
type: source
title: "Curing Cats with Feline Infectious Peritonitis with an Oral Multi-Component Drug Containing GS-441524"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: [cure-rate, clinical-improvement, laboratory-parameters]
jurisdictions: [Germany]
evidence_level: original-study
year: 2021
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
pmid: "34835034"
doi: "10.3390/v13112228"
tags: [fip, gs-441524, oral-treatment, Xraphconn, cure, antiviral, 84-day-protocol, neurological-dose, ocular-dose]
links:
  doi: "10.3390/v13112228"
  url: "https://doi.org/10.3390/v13112228"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "All cats recovered with dramatic improvement of clinical and laboratory parameters."
    - "Oral treatment with Xraphconn® containing GS-441524 was highly effective for FIP without causing serious adverse effects."
  source_supported_conclusion:
    - "100% survival (18/18 cats) with oral GS-441524 (Xraphconn®)."
    - "Two-tier dosing: 10 mg/kg (neurological/ocular) vs 5 mg/kg (non-neurological)."
    - "84-day treatment duration."
    - "Dramatic improvement within first few days of treatment."
    - "No serious adverse effects reported."
    - "Mass spectrometry confirmed GS-441524 as active component."
  llm_inference:
    - "Oral formulation provides practical alternative to injectable GS-441524."
    - "Higher dose for CNS/ocular disease reflects need for better tissue penetration."
    - "100% cure rate is exceptional but n=18 is modest sample size."
  # V2 enhanced fields
  study_design: "前瞻性队列研究，18 只自发性 FIP 猫使用口服 Xraphconn®（含 GS-441524）84 天方案治疗"
  core_argument: "口服 GS-441524 制剂高效治愈 FIP（18/18 即 100% 存活）——双层剂量方案（神经/眼部 10 mg/kg，非神经 5 mg/kg）无严重不良反应"
  implicit_premise: "假设口服制剂提供注射 GS-441524 的实用替代；假设质谱确认活性成分可以验证产品成分"
  unexpected_finding: "临床和实验室参数在治疗最初几天内即有显著改善——比预期更快的反应时间表"
  title_gap: "标题说用口服药物治愈 FIP 猫，但真正发现是双层剂量方案：神经/眼部 10 mg/kg vs 非神经 5 mg/kg，且最初几天内即有显著改善——质谱确认活性成分验证了产品成分"
  evidence_boundary: "n=18 的适度样本量；100% 治愈率可能不可推广到更大更多样化群体；品牌/制剂特异性"
---

# Curing Cats with Feline Infectious Peritonitis with an Oral Multi-Component Drug Containing GS-441524

## Evidence-Depth Caveat

**Deep-extracted from PubMed abstract (PMID 34835034).** 2021 Viruses prospective study: n=18 cats with spontaneous FIP treated with oral Xraphconn® (GS-441524). 100% survival, 84-day protocol, two-tier dosing. No serious adverse effects. Evidence level: prospective cohort.

## Source Check, 2026-06-17

PubMed abstract extracted.

- PMID: 34835034
- DOI: 10.3390/v13112228
- Journal: Viruses (MDPI)
- Year: 2021
- Open access: yes

## Study Design

| Feature | Value |
|---------|-------|
| Design | Prospective cohort |
| Sample size | n=18 cats |
| Disease | Spontaneous FIP |
| Drug | Xraphconn® (oral multi-component) |
| Active ingredient | GS-441524 (confirmed by mass spectrometry, NMR) |

## Treatment Protocol

| Presentation | Dose | Duration |
|--------------|------|----------|
| Neurological/ocular FIP | **10 mg/kg** | 84 days |
| Non-neurological FIP | **5 mg/kg** | 84 days |

## Outcomes

| Metric | Result |
|--------|--------|
| Survival | **100% (18/18)** |
| Clinical improvement | Dramatic, within first few days |
| Laboratory improvement | Normalized parameters |
| Serious adverse effects | **None** |

**Quoted:** "All cats recovered with dramatic improvement of clinical and laboratory parameters."

**Quoted:** "Oral treatment with Xraphconn® containing GS-441524 was highly effective for FIP without causing serious adverse effects."

## One-Line Summary

2021 prospective study: oral GS-441524 (Xraphconn®) cured 18/18 FIP cats (100%) over 84 days with two-tier dosing (10 mg/kg neuro/ocular, 5 mg/kg other); no serious adverse effects.

## Claim-Fit Judgment

**Strongest safe use:**
- Oral GS-441524 efficacy evidence
- Two-tier dosing protocol (neuro vs non-neuro)
- 84-day treatment duration
- Safety profile (no serious AEs)

**May control:**
- FIP treatment-overview.md oral therapy section
- GS-441524 dosing recommendations

**Should use with caveats:**
- 100% cure rate (small sample, n=18)
- Xraphconn® specific (brand/formulation)

**Must not control:**
- Universal cure claims
- Specific brand recommendations
- Comparative efficacy vs injectable

## Deep Extraction Metadata

- **Extraction date:** 2026-06-17
- **Source:** PubMed abstract (PMID 34835034)
- **Full text verified:** Abstract-level
- **Citations in vault topic pages:** 6 (branch-controlling)

## Linked Entities

- diseases: FIP
- drugs: GS-441524, Xraphconn®
- endpoints: cure rate, clinical improvement, laboratory parameters
- protocols: 84-day, two-tier dosing
- mechanisms: nucleoside analog, RdRp inhibition
