---
id: src-hcm-012
type: source
title: "Influence of Clinical Aspects and Genetic Factors on Feline HCM Severity and Development"
source_kind: paper
species: feline
diseases: [HCM]
models: []
endpoints: [severity]
jurisdictions: []
evidence_level: original-study
year: 2024
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [hcm, genetics, severity]
links:
  doi: ""
  url: "https://www.mdpi.com/2306-7381/11/5/214"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The abstract states that feline HCM is primarily related to mutations in the MYBPC3 and MYH7 genes."
    - "The abstract studies heterozygosity and homozygosity for the p.A31P mutation in MYBPC3 in relation to HCM severity and development."
    - "The abstract states that homozygous cats had moderate to severe HCM, with higher penetrance and significant risk of cardiac death compared with heterozygous cats."
    - "The abstract states that HCM showed age-related penetrance, with no disease in cats up to 1 year and the highest proportion in cats aged 7 years and older."
  source_supported_conclusion:
    - Genotype-phenotype and severity pressure are already real branches in the HCM seed set.
    - The study supports keeping genotype dosage visible because homozygous and heterozygous states do not appear clinically equivalent.
    - The study supports age-aware penetrance as part of HCM recognition and risk framing.
    - This paper is one of the strongest current bridges between the genetics branch and the recognition/risk branches because it makes dosage and timing clinically meaningful.
    - The source argues against binary mutation language by showing that genotype state affects severity, penetrance, and cardiac-death risk differently.
  llm_inference:
    - This may become a key bridge between genetics and recognition after deep extraction.
    - HCM pages should keep genetics stratified by dosage and age-related penetrance instead of flattening mutation-positive cats into one uniform risk class.
  # V2 enhanced fields
  study_design: "原始研究，研究 MYBPC3 p.A31P 突变杂合子和纯合子猫的 HCM 严重程度和发展"
  core_argument: "基因型剂量影响临床表型——纯合子猫有中重度 HCM，更高外显率和显著心脏死亡风险；年龄相关外显率使遗传风险无法直接转化为即时表型确定性"
  implicit_premise: "假设单一突变的剂量效应可以推广到其他 HCM 变异；假设年龄相关外显率使识别需要时间感知"
  unexpected_finding: "1 岁以下猫无疾病，7 岁及以上猫比例最高——这挑战了突变阳性等于即时风险的简化叙事"
  title_gap: "标题说临床和遗传因素，但真正发现是时间维度：1 岁以下无疾病，7 岁及以上最高——突变阳性≠即时风险，需要年龄感知的筛查策略"
  evidence_boundary: "聚焦 p.A31P 突变，不应过度泛化到所有猫 HCM 变异或品种"
---

# One-line Summary

Clinical-genetic severity paper that strengthens the genotype-phenotype branch and makes mutation dosage and age-related penetrance explicit.

## Why It Matters For HCM

- links genetics to clinical severity rather than leaving genetics abstract
- may become central for prognosis and recognition depth
- now gives the HCM shell a safer rule that genotype pressure should stay stratified, not flattened into simple mutation present/absent language

## Key Findings

- severity and development framing
- abstract links MYBPC3 p.A31P genotype dosage to severity differences
- abstract supports earlier and more severe disease in homozygous cats than in heterozygous cats
- abstract supports age-related penetrance

## Why This Study Matters

This study matters because it keeps the HCM genetics branch clinically grounded.

Without a paper like this, genetics can drift in one of two bad directions. It can become too abstract, where variants are mentioned but never tied to real disease pressure, or too simplistic, where mutation-positive status gets treated as one flat risk bucket. This source pushes against both errors.

Its main contribution is to make genotype dosage clinically meaningful. Homozygous and heterozygous p.A31P MYBPC3 states do not behave the same way. Severity, penetrance, and cardiac-death risk all move in the same direction, which gives the HCM module a more realistic genotype-to-phenotype bridge.

It also adds time structure. Age-related penetrance means genetic risk cannot be read as immediate phenotype certainty. That is important because it keeps recognition architecture connected to age, not only to mutation status.

## Genotype-Severity Signal

The safest promotion from this source is:

- genotype dosage should remain visible
- homozygous and heterozygous states should not be treated as clinically equivalent
- age-aware penetrance is part of recognition and risk framing
- genetics can influence risk and severity without becoming a standalone phenotype substitute

That makes this card more than a genetics paper. It is a bridge source linking mechanism, recognition, and risk.

## Limits / Caveats

- current card is abstract-weighted, not full-text reviewed
- The source is strongest for dosage-sensitive genotype framing around the studied mutation, not for universal claims across every feline HCM variant or breed.

## Image Asset TODO

- figures to capture:
  - penetrance curve by age
  - genotype outcome table
- candidate target paths are tracked in [HCM image ingest manifest](../../system/indexes/hcm-image-ingest-manifest-20260417.md) until article labels are verified.

## Open Follow-up Questions

- which clinical factors and which genetic factors dominate severity?
- does the paper change recognition or prognosis more?
- how much of this genotype-severity signal is reusable outside the studied mutation and breeds?
- how should genotype dosage be represented in a stable HCM risk-stratification page without overgeneralizing beyond p.A31P?
- what additional breed-specific or variant-specific contexts does the full paper discuss beyond the abstract framing?

## Linked Entities

- HCM
- genetics
- severity
