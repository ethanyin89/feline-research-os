---
id: src-fcv-003
type: source
title: "Comparison of the ability of feline calicivirus (FCV) vaccines to neutralise a panel of current UK FCV isolates"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [cross-neutralisation, prevalence, vaccine breadth]
jurisdictions: [UK]
evidence_level: original-study
year: 2008
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, vaccine, neutralisation, uk, field-isolates]
links:
  doi: "10.1016/j.jfms.2007.06.011"
  url: "https://journals.sagepub.com/doi/10.1016/j.jfms.2007.06.011"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Accessible abstract/card extraction reports F9 antiserum neutralised 87.5% of tested isolates and strain 255 antiserum 75%."
    - "Accessible abstract/card extraction reports some field isolates were not neutralised by either antiserum."
    - "Accessible abstract/card extraction reports FCV was isolated from 122 of 1206 swabs, giving a prevalence of 10.1% in the sampled UK veterinary-visiting population."
  source_supported_conclusion:
    - This is the current main FCV neutralisation-breadth anchor in the seed set.
    - The study supports treating cross-reactivity as broad but incomplete.
    - The paper supports a UK-panel-specific vaccine-breadth signal, not universal coverage language.
    - The paper should control the breadth branch, not challenge, field-effectiveness, or carrier-state language.
  llm_inference:
    - This source now serves as the first deep-extracted neutralisation-breadth anchor in the FCV endpoint branch.
    - The safest downstream wording is `broad but incomplete breadth`, not `current vaccines cover FCV`.
  # V2 enhanced fields
  study_design: "原始实验室中和研究，采集1206份来自英国兽医就诊猫只的拭子，检测122例分离的猫杯状病毒株，评估两种疫苗血清对不同野外分离株的中和能力"
  core_argument: "目前使用的猫杯状病毒疫苗株能够对大部分英国野外分离的病毒株表现出较广泛的交叉中和活性，但无法完全覆盖所有采样的病毒多样性"
  implicit_premise: "实验室中和试验结果能代表体内疫苗对野外病毒株的免疫保护情况"
  title_gap: "标题强调不同疫苗对当前英国猫杯状病毒株的中和能力，但研究具体揭示了现有疫苗虽广泛交叉反应，却并未实现对病毒群体的完全覆盖——提示疫苗保护存在盲区"
  evidence_boundary: "未评估疫苗对病毒株体内保护力及临床预防效果；未涵盖英国以外的病毒株多样性；未检测疫苗对新兴变异株的中和能力"
  unexpected_finding: "即使是使用中的疫苗血清，也存在部分野外病毒分离株未被中和，说明病毒多样性带来的免疫逃逸风险"
---

# Comparison of the ability of feline calicivirus (FCV) vaccines to neutralise a panel of current UK FCV isolates

## One-Line Summary

UK field-isolate neutralisation study showing currently used vaccine strains remained broadly cross-reactive, but not completely covering sampled FCV diversity.

## Why It Matters For FCV

- gives the module a concrete vaccine-breadth anchor against contemporary field isolates
- helps separate reduction of disease risk from complete infection blocking
- now serves as the first FCV deep-extracted neutralisation-breadth anchor

## Key Findings

### quoted_fact

- Accessible abstract/card extraction reports F9 antiserum neutralised 87.5% of tested isolates and strain 255 antiserum 75%.
- Accessible abstract/card extraction reports some isolates were not neutralised by either antiserum.
- Accessible abstract/card extraction reports FCV was isolated from 122 of 1206 swabs, giving a prevalence of 10.1% in the sampled UK veterinary-visiting population.

### source_supported_conclusion

- This source is the current best FCV breadth paper for defending `broad but incomplete` cross-neutralisation language.
- The paper supports keeping neutralisation breadth high in endpoint architecture while holding it below challenge-protection and persistence claims.
- The strongest safe read is `contemporary UK breadth signal, not universal field closure`.

### llm_inference

- If the module later builds a stricter vaccine-comparison layer, this card should sit above generic vaccine rhetoric and below challenge or field-effectiveness claims.

## Limits / Caveats

- in-vitro neutralisation is one endpoint family, not a whole vaccine verdict
- in vitro neutralisation should not be promoted into direct clinical-protection certainty
- UK field-isolate coverage does not automatically generalise across geography or time
- current card is deep-extracted at worksheet level, but still not full-text reviewed section by section

## Vaccine-Breadth Branch Logic

What can be promoted:

- currently used FCV vaccine strains can retain broad cross-reactivity against sampled field isolates
- broad should be written as incomplete rather than complete
- field-isolate panel logic belongs in the breadth branch of FCV endpoint architecture

What should be held:

- any field-effectiveness winner language
- any sterilizing-immunity claim
- any universal or timeless coverage claim
- any carrier-state or persistence-control claim

This card is therefore best reused as a breadth anchor rather than as a whole-program vaccine conclusion.

Its main value is architectural: it lets the module say `breadth exists, but closure does not` with a concrete field-isolate paper behind it.

## Write-Back Implications

- [endpoint handbook](../../topics/fcv/endpoint-handbook.md) should treat this card as the first deep-extracted neutralisation-breadth anchor.
- [FCV vaccine-persistence boundary memo](../../system/indexes/fcv-vaccine-persistence-boundary-memo.md) can now lean more directly on `broad but incomplete cross-neutralisation`.
- [translation brief](../../topics/fcv/translation-brief.md) should keep this card below challenge and persistence claims.

## Source Family And Claim-Fit

Source family:

- original-study

Strongest safe use:

- vaccine-breadth anchor
- in-vitro cross-neutralisation boundary
- bounded field-isolate coverage signal

What this source must not control:

- field-effectiveness winner language
- sterilizing-immunity claims
- current-market product ranking
- whole-world prevalence or coverage generalization

## Open Follow-Up Questions

- how should this paper be placed against newer geographically specific vaccine arguments?
- what is the safest way to translate broad cross-reactivity into owner-facing language?
- how much of the preserved signal holds once challenge and cellular-immunity anchors are weighted beside it?

## Linked Entities

- diseases: FCV
- models:
- endpoints: cross-neutralisation, prevalence, vaccine breadth
- mechanisms: antigenic variability
- regulations:
