---
id: src-diabetes-009
type: source
title: "Feline diabetes mellitus in the UK: The prevalence within an insured cat population and a questionnaire-based putative risk factor analysis"
source_kind: paper
species: feline
diseases: [diabetes mellitus]
models: []
endpoints: [prevalence, risk-factors]
jurisdictions: [UK]
evidence_level: original-study
year: 2007
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, epidemiology, prevalence, risk-factors, UK]
links:
  doi: "10.1016/j.jfms.2007.02.001"
  url: "https://doi.org/10.1016/j.jfms.2007.02.001"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Diabetes prevalence was 1 in 230 cats (0.43%) in a UK insured cat population."
    - "Burmese cats were 3.7 times more likely to develop diabetes than non-pedigree cats."
    - "Male sex was identified as a significant risk factor for diabetes."
    - "Neutered cats had higher diabetes risk than intact cats."
    - "Physical inactivity was associated with increased diabetes risk."
    - "Body weight of at least 5 kg was associated with increased diabetes risk."
    - "History of corticosteroid treatment was associated with diabetes risk."
    - "Multivariate tree model identified gender as the most important overall risk factor."
  source_supported_conclusion:
    - "This 2007 JFMS study provides UK population-level prevalence and risk-factor data for feline diabetes."
    - "The 1:230 prevalence estimate is population-specific (UK insured cats) and should not be generalized globally."
    - "The 3.7x Burmese risk is a strong breed signal that aligns with Australian data."
    - "Multi-factor risk structure (sex, neuter status, weight, activity, medications) supports comprehensive risk assessment."
    - "Risk associations are correlational, not causal proof."
  llm_inference:
    - "Risk assessment should include breed, sex, neuter status, body weight, activity level, and medication history."
    - "The 5 kg weight threshold provides a practical screening cutoff for weight-related risk."
    - "Burmese breed risk appears consistent across UK and Australian populations."
  # V2 enhanced fields
  study_design: "横断面研究，英国投保猫群体中，采用问卷调查与保险数据库分析糖尿病患病率及潜在风险因素"
  core_argument: "英国投保猫中糖尿病的患病率为0.43%，且缅甸猫、雄性及绝育猫的糖尿病风险显著升高，表明这些为主要的潜在风险因素。"
  implicit_premise: "保险猫群体的健康状况和疾病报告能代表英国整体猫群的糖尿病流行特征及风险因素。"
  title_gap: "标题仅表明患病率及风险因素分析，但实际发现缅甸猫糖尿病风险高出非纯种猫3.7倍，这与其他国家数据一致，揭示了强烈的品种遗传风险信号——强调遗传背景在猫糖尿病中的作用。"
  evidence_boundary: "结果仅适用于英国投保的猫群体，未涵盖未投保猫或其他国家的猫，且未探讨糖尿病的发病机制或治疗效果。"
  unexpected_finding: "绝育猫糖尿病风险显著高于未绝育猫，暗示激素变化可能对糖尿病发病有重要影响。"
---

# Feline diabetes mellitus in the UK

## One-Line Summary

UK insured-population prevalence and putative risk-factor study for feline diabetes.

## Why It Matters For Feline Diabetes

- gives the risk page population-level grounding
- should be compared with Australian breed-predisposition data before any broad risk claim

## Key Findings

- abstract-level extraction confirms an insured-population prevalence estimate and questionnaire-based risk-factor analysis
- Burmese cats show a strong risk signal in the abstract
- multivariate tree analysis identified gender as the most important overall risk factor
- activity and breed appear in the interaction structure described by the abstract
- the source adds a structured risk-factor map: breed, sex/neuter status, activity, body weight, and medication exposure
- the strongest safe use is population-level risk context, not patient-level prediction

## Limits / Caveats

- extraction is abstract-weighted, not full-text
- insured-population and questionnaire designs limit generalizability
- risk-factor associations should not be treated as causal
- do not generalize the prevalence estimate outside the UK insured-population context without a denominator check
- do not interpret Burmese risk as mechanism proof from this source alone

## UK Risk-Map Logic

This source is the main UK epidemiology and putative risk-factor anchor.

What can be promoted:

- prevalence was estimated in a UK insured cat population
- Burmese cats had a strong risk signal compared with non-pedigree cats
- male sex, neuter status, inactivity, weight at least 5 kg, and corticosteroid history were univariate risk factors
- gender led the multivariate tree model

What should be held:

- universal prevalence
- causal interpretation
- individual prediction
- breed mechanism
- generalization outside insured UK cats

## Relationship To Australian Breed-Risk Source

This card should be paired with [src-diabetes-012](src-diabetes-012.md).

The safe synthesis is:

- UK data support Burmese and multi-factor risk signals
- Australian data support a Burmese period-prevalence signal
- cross-population agreement strengthens breed-risk visibility
- denominator differences still block a single global prevalence claim

## Write-Back Implications

- [risk and recognition](../../topics/diabetes/risk-and-recognition.md) should include breed, sex/neuter status, inactivity, weight, and medication exposure as bounded risk factors.
- [diabetes breed-risk synthesis memo](../../system/indexes/diabetes-breed-risk-synthesis-memo.md) should keep UK/Australian denominator differences visible.
- [synthesis index](../../topics/diabetes/synthesis-index.md) should treat risk as context, not causality.

## Full-Text Target If Needed

If later outputs need a risk table, extract case definition, insured-population denominator, survey response bias, multivariable tree details, interaction nodes, and how corticosteroid or megestrol exposure was measured. Also separate risk-factor association from screening or prevention advice, because the abstract supports branch visibility more strongly than clinical prediction.

## Current Safe Role

Use this source to build the risk map and to remind outputs that epidemiology is population-bound. It is strong enough to name UK risk signals, but not strong enough to tell an individual owner that one factor caused a cat's diabetes.

## Open Follow-Up Questions

- what population denominator was used?
- which risk factors survived analysis?
- how does it compare with Australian prevalence and breed findings?

## Linked Entities

- diseases: diabetes mellitus
- models:
- endpoints: prevalence, risk factors
- mechanisms:
- regulations:
