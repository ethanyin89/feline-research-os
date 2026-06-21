---
id: src-fcv-011
type: source
title: "Characterization of an avirulent FCV strain with a broad serum cross-neutralization profile and protection against challenge of a highly virulent vs feline calicivirus"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [cross-neutralisation, challenge protection, mortality]
jurisdictions: []
evidence_level: original-study
year: 2014
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, vaccine, vs-fcv, challenge, neutralisation]
links:
  doi: "10.1016/j.virusres.2014.03.007"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S0168170214001129?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Accessible abstract/card extraction reports mortality after VS-FCV-33585 challenge was 78% in unvaccinated controls."
    - "Accessible abstract/card extraction reports vaccines containing FCV-21 reduced mortality to 0% in this challenge model."
    - "Accessible abstract/card extraction reports FCV-21 showed a broad serum cross-neutralisation profile."
  source_supported_conclusion:
    - This is the current main FCV challenge-protection anchor in the seed set.
    - The paper supports treating strain selection as a real vaccine-design lever.
    - The paper supports challenge protection as a separate endpoint family from neutralisation breadth alone.
    - The paper should control the challenge branch, not current-market or persistence language.
  llm_inference:
    - This source now serves as the first deep-extracted challenge-protection anchor in the FCV endpoint branch.
    - The safest downstream wording is `high-signal challenge benefit`, not `best current vaccine`.
  # V2 enhanced fields
  study_design: "原始实验研究，使用接种与未接种疫苗的猫进行体内挑战试验，评估不同FCV株对高度毒性猫杯状病毒的交叉中和和保护效果"
  core_argument: "具有广泛血清交叉中和能力的无毒性FCV株FCV-21能够在应激条件下提供比传统仅含F9株疫苗更优的对高度毒性系统性FCV的保护"
  implicit_premise: "血清中和广谱性是实现疫苗保护效果提升的关键指标，且体内挑战试验能真实反映疫苗保护能力"
  title_gap: "标题强调无毒性FCV株的特征与交叉中和能力，但真正的发现展示了其在高毒性FCV应激挑战下优于传统疫苗的保护效果——揭示疫苗株选择对实际保护力的实质影响"
  evidence_boundary: "本研究未评估该无毒性株在自然感染环境下的免疫持久性和安全性，也未探讨其在不同地理地域及多样病毒株中的保护广度"
  unexpected_finding: "无毒性FCV-21疫苗株在高致死性VS-FCV-33585病毒挑战中实现了零死亡率，而传统未含该株的疫苗组死亡率高达78%"
---

# Characterization of an avirulent FCV strain with a broad serum cross-neutralization profile and protection against challenge of a highly virulent vs feline calicivirus

## One-Line Summary

Challenge-model vaccine paper showing a broadly neutralising avirulent strain candidate could outperform F9-only logic against highly virulent systemic FCV in a controlled stress-test setting.

## Why It Matters For FCV

- gives the module a strong VS-FCV challenge anchor
- makes vaccine-strain choice feel mechanistically and clinically consequential
- now serves as the first FCV deep-extracted challenge-protection anchor

## Key Findings

### quoted_fact

- Accessible abstract/card extraction reports mortality after VS-FCV-33585 challenge was 78% in unvaccinated controls.
- Accessible abstract/card extraction reports vaccines containing FCV-21 reduced mortality to 0% in this challenge model.
- Accessible abstract/card extraction reports FCV-21 showed a broad serum cross-neutralisation profile.

### source_supported_conclusion

- This source is the current best FCV challenge paper for keeping challenge protection above simple titre rhetoric.
- The paper supports strain selection as a meaningful vaccine-design lever.
- The strongest safe read is `challenge benefit in a controlled VS-FCV model`, not `current-market winner`.

### llm_inference

- If the module later builds a fuller vaccine-comparison hierarchy, this card should sit above breadth-only papers and below field-effectiveness or current-label claims.

## Limits / Caveats

- challenge protection is one endpoint family, not a whole vaccine verdict
- challenge-model results are not the same as field effectiveness in mixed populations
- product-ranking claims should stay below deeper comparison work
- current card is deep-extracted at worksheet level, but still not full-text reviewed section by section

## Challenge-Protection Branch Logic

What can be promoted:

- challenge protection is a real FCV endpoint family
- strain-selection language now has a stronger anchor
- clinical benefit in a virulent-systemic challenge model should weigh more than generic vaccine rhetoric

What should be held:

- any current-market superiority claim
- any generic statement that one vaccine solves FCV control
- any persistence or carrier-state-control claim

This card is best reused as a challenge-protection source rather than as a direct market or policy answer.

Its main value is architectural: it lets the module talk about `high-signal challenge benefit` without pretending that challenge success equals routine field dominance.

## Write-Back Implications

- [endpoint handbook](../../topics/fcv/endpoint-handbook.md) should treat this card as the first deep-extracted challenge-protection anchor.
- [FCV vaccine-persistence boundary memo](../../system/indexes/fcv-vaccine-persistence-boundary-memo.md) can now lean more directly on the challenge branch.
- [translation brief](../../topics/fcv/translation-brief.md) should keep this card above breadth rhetoric and below current-market language.

## Source Family And Claim-Fit

Source family:

- original-study

Strongest safe use:

- challenge-protection anchor
- virulent-systemic FCV branch stress test
- strain-selection-as-design-lever signal

What this source must not control:

- current-market superiority claims
- routine-population field-effectiveness claims
- generic recommendation that one vaccine solves FCV control
- final vaccine ranking without breadth, persistence, and cellular-immunity integration

## Open Follow-Up Questions

- how should FCV-21 logic be reconciled with geographically specific vaccine arguments?
- which parts of the benefit came from FCV-21 alone versus FCV-21 plus F9?
- how much of this challenge benefit survives when persistence and carrier-state boundaries are reintroduced?

## Linked Entities

- diseases: FCV
- models:
- endpoints: cross-neutralisation, challenge protection, mortality
- mechanisms: strain selection, virulent-systemic challenge
- regulations:
