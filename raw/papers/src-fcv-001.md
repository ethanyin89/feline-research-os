---
id: src-fcv-001
type: source
title: "An Update on Feline Calicivirus"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [diagnosis, treatment, prevention, hygiene]
jurisdictions: []
evidence_level: review
year: 2022
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, review, diagnosis, vaccination, control]
links:
  doi: "10.17236/SAT00346"
  url: "https://pubmed.ncbi.nlm.nih.gov/35232714/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Accessible abstract/card extraction reports FCV is one of the most common viral pathogens in domestic cats worldwide."
    - "Accessible abstract/card extraction reports the review integrates FCV genetics, immunity, diagnosis, prevention, vaccination, and hygienic control."
    - "Accessible abstract/card extraction reports recent Swiss work is discussed as a check against assuming all FCV-suspect cats are FCV-positive."
  source_supported_conclusion:
    - This is the current modern clinician-facing shell-review anchor for the FCV module.
    - The paper should sit near the top of FCV broad-review and control-layer compression.
    - The source supports keeping recognition caution and hygienic control inside the disease shell rather than as detached afterthoughts.
    - The paper should control shell language more than narrow endpoint or product-ranking language.
  llm_inference:
    - This source now serves as the first modern deep-extracted broad-review shell anchor in the FCV module.
    - The safest downstream wording is `modern shell review for common, variable, control-relevant FCV`, not `final narrow-branch authority`.
  # V2 enhanced fields
  study_design: "综述性研究，整合全球范围内猫科杯状病毒（FCV）相关文献，涵盖遗传学、免疫学、诊断学、预防及卫生控制等多个方面"
  core_argument: "猫科杯状病毒具有高度变异性，临床识别时应保持谨慎，并且诊断与控制需要将卫生管理纳入疾病综合防控体系，而非仅作为附加措施"
  implicit_premise: "现有的文献与研究数据能够全面反映FCV的遗传变异、免疫应答及临床诊断挑战，从而支持构建统一且实用的临床诊疗框架"
  title_gap: "标题强调FCV的最新进展，但本文突出强调变异性和识别上的谨慎性，以及卫生控制的重要性——这些常被忽视却对临床决策关键"
  evidence_boundary: "本文未解决具体FCV治疗方案的效果评估，也未提供新疫苗的临床试验数据，且未涉及猫群体中病毒传播动力学的详细实证研究"
  unexpected_finding: "最新瑞士研究表明，并非所有疑似FCV感染的猫均为病毒阳性，提示传统诊断方法存在一定假阳性风险"
---

# An Update on Feline Calicivirus

## One-Line Summary

Modern broad FCV update integrating variability, diagnosis, recognition caution, vaccination, and hygienic control into one clinician-facing shell.

## Why It Matters For FCV

- useful as a recent overview before the module splits into vaccine, persistence, and extension branches
- likely the cleanest first clinician-facing anchor in the seed set
- now serves as the first modern deep-extracted broad-review shell anchor

## Key Findings

### quoted_fact

- Accessible abstract/card extraction reports FCV is one of the most common viral pathogens in domestic cats worldwide.
- Accessible abstract/card extraction reports the review integrates FCV genetics, immunity, diagnosis, prevention, vaccination, and hygienic control.
- Accessible abstract/card extraction reports recent Swiss work is discussed as a check against assuming all FCV-suspect cats are FCV-positive.

### source_supported_conclusion

- This source is the current best modern broad-review shell anchor for keeping FCV written as a common, variable, control-relevant pathogen.
- The paper supports keeping recognition caution, prevention, vaccination, and hygiene inside the same disease shell.
- The strongest safe read is `modern clinician-facing FCV shell`, not `final owner of narrow endpoint branches`.

### llm_inference

- If the module later builds a fuller FCV shell or synthesis page, this card should help anchor the opening overview and anti-overcompression language.

## Limits / Caveats

- current card is built from accessible abstract-level metadata and summary text rather than section-by-section full-text extraction
- do not use this card alone for precise assay, vaccine, or treatment ranking
- broad review authority should not be mistaken for narrow endpoint ownership

## Disease-Shell Logic

What can be promoted:

- FCV remains common, variable, and clinically important
- diagnosis, prevention, vaccination, and hygienic control belong in one clinician-facing shell
- recognition caution belongs inside the shell because FCV-suspect does not equal FCV-confirmed

What should be held:

- any narrow endpoint hierarchy
- any vaccine-product ranking
- any therapy recommendation or numeric workup rule

This card is therefore best reused as a disease-shell and control-architecture source rather than as a narrow branch authority.

Its main value is structural: it gives the module a modern overview layer that can hold commonness, variability, recognition caution, and hygienic control together.

## Write-Back Implications

- [topic index](../../topics/fcv/index.md) should treat this card as the first modern broad-review shell anchor.
- [mechanism overview](../../topics/fcv/mechanism-overview.md) can now lean more directly on a modern review that keeps FCV variable, common, and clinically heterogeneous.
- [FCV mechanism-control memo](../../system/indexes/fcv-mechanism-control-memo.md) can now carry more of the shell-plus-control language from this source.
- [current state dashboard](../../topics/fcv/current-state-dashboard.md) should treat the broad-review branch as having more than one deep-extracted review-grade anchor.

## Open Follow-Up Questions

- how does the review rank diagnosis versus control versus vaccination pressure?
- does it separate persistent shedding from acute disease cleanly?
- how much of the review's shell language should sit in mechanism pages versus recognition or translation pages?

## Linked Entities

- diseases: FCV
- models:
- endpoints: diagnosis, treatment, prevention, hygiene
- mechanisms: variability, persistence, immune evasion
- regulations:
