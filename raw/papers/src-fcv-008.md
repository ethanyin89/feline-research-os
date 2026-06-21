---
id: src-fcv-008
type: source
title: "Sensitivity of FCV to recombinant feline interferon (rFeIFN)"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [interferon sensitivity, field isolates]
jurisdictions: [Japan]
evidence_level: original-study
year: 2007
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, interferon, therapy, field-isolates, japan]
links:
  doi: "10.1007/s11259-007-9019-5"
  url: "https://link.springer.com/article/10.1007/s11259-007-9019-5"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Accessible abstract/card extraction reports the sensitivity of 47 field isolates to recombinant feline interferon was assessed."
    - "Accessible abstract/card extraction reports log PDD50 values were normally distributed from 1.1 to 3.7 with a mean of 2.3 +/- 0.64."
    - "Accessible abstract/card extraction reports 68.3% of values fell within the mean +/- standard deviation range and were used to define moderate sensitivity."
    - "Accessible abstract/card extraction reports among 15 vaccine-breakdown strains, some were highly sensitive and at least one was low sensitivity, showing no clear association between vaccine breakdown and interferon sensitivity."
    - "Accessible abstract/card extraction reports amino-acid changes specific to the low-sensitivity Fukuoka-9 strain were identified."
  source_supported_conclusion:
    - This is an early therapy-response heterogeneity paper, not a clinical-efficacy proof.
    - The paper supports keeping FCV interferon claims strain-sensitive rather than writing recombinant interferon as a flat treatment class.
    - The paper supports a therapy-control layer distinct from in vivo clinical-response papers.
    - The paper supports separating vaccine-break logic from treatment-response logic.
  llm_inference:
    - This source now serves as the main FCV interferon-sensitivity caution anchor in the therapy branch.
    - The safest downstream wording is `heterogeneous interferon sensitivity`, not `generic interferon responsiveness`.
  # V2 enhanced fields
  study_design: "实验室体外试验，日本采集的47个猫杯状病毒现场分离株，采用重组猫干扰素敏感性评估法"
  core_argument: "猫杯状病毒现场分离株对重组猫干扰素的敏感性存在显著变异，且疫苗失效状态不能单独解释这种敏感性差异"
  implicit_premise: "体外干扰素敏感性测定反映了病毒对干扰素的潜在反应能力，并能代表实际治疗中的病毒异质性"
  title_gap: "标题强调FCV对重组猫干扰素敏感性，但真正发现是疫苗失效状态与干扰素敏感性无明确关联，提示治疗需考虑病毒株特异性差异"
  evidence_boundary: "本研究未评估临床干扰素治疗的疗效，仅限于病毒体外敏感性的测定，未涵盖体内治疗响应或临床预后"
  unexpected_finding: "部分疫苗失效株表现出高度敏感性，而至少有一株低敏感性病毒突变，显示病毒干扰素敏感性与疫苗保护状态解耦"
---

# Sensitivity of FCV to recombinant feline interferon (rFeIFN)

## One-Line Summary

Japanese field-isolate study showing FCV strains vary in interferon sensitivity and that vaccine-breakdown status alone does not explain that variation.

## Why It Matters For FCV

- gives the module a strain-response therapy boundary paper
- helps prevent generic interferon optimism
- now serves as the first FCV deep-extracted interferon-sensitivity control anchor

## Key Findings

### quoted_fact

- Accessible abstract/card extraction reports the sensitivity of `47` field isolates to recombinant feline interferon was assessed.
- Accessible abstract/card extraction reports log `PDD50` values ranged from `1.1` to `3.7` with a mean of `2.3 +/- 0.64`.
- Accessible abstract/card extraction reports `68.3%` of values fell within the mean +/- standard deviation range and were used to define moderate sensitivity.
- Accessible abstract/card extraction reports among `15` vaccine-breakdown strains, some were highly sensitive and at least one was low sensitivity, showing no clear association between vaccine breakdown and interferon sensitivity.
- Accessible abstract/card extraction reports amino-acid changes specific to the low-sensitivity `Fukuoka-9` strain were identified.

### source_supported_conclusion

- This source is the current best FCV paper for stopping the therapy branch from collapsing into `interferon works` language.
- The paper supports a real heterogeneity story across field isolates rather than a single class effect.
- The paper supports writing recombinant interferon as a strain-sensitive exploratory branch, not as a settled therapeutic answer.
- The strongest safe read is `response varies by strain and cannot be inferred from vaccine-break status alone`.

### llm_inference

- If the module later builds a treatment-comparison memo, this card should control the interferon-boundary subsection rather than remain a generic caution sentence.

## Limits / Caveats

- this is not a clinical outcome trial in naturally infected cats
- treatment translation should stay below routine protocol advice
- the current extraction is abstract-led rather than a full section-by-section article extraction

## Therapy-Boundary Logic

What can be promoted:

- FCV interferon sensitivity is heterogeneous across field isolates
- vaccine-breakdown status does not reliably predict interferon sensitivity
- low-sensitivity strains may carry specific sequence changes worth keeping visible in mechanism-aware therapy reading

What should be held:

- any statement that recombinant feline interferon has uniform FCV activity
- any shortcut from vaccine failure to interferon resistance
- any conversion of this isolate-sensitivity paper into direct clinical-efficacy guidance

## Operational Read

This paper matters because it gives the FCV therapy branch a control anchor, not a success anchor.
The preserved range of sensitivity values and the mixed behavior among vaccine-breakdown strains stop
the module from treating recombinant interferon as if it had one flat antiviral profile across FCV.

That is why this card pairs naturally with `src-fcv-018`. `src-fcv-018` keeps the branch from being
purely preclinical, while `src-fcv-008` keeps it from becoming naive treatment optimism. Together they
support one narrow sentence: FCV therapy is now a real branch, but response should still be written as
heterogeneous, exploratory, and strain-sensitive rather than routine.

Its main value is architectural: it stabilizes the boundary between therapy possibility and therapy
overclaim.

## Open Follow-Up Questions

- which viral sequence changes were linked to low interferon sensitivity?
- how should this paper be paired with later FCV therapeutic studies?
- does later in vivo work change the relevance of isolate-level interferon sensitivity classes or mostly bypass them?

## Linked Entities

- diseases: FCV
- models:
- endpoints: interferon sensitivity, field isolates
- mechanisms: strain variability
- regulations:
