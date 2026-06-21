---
id: src-fcv-004
type: source
title: "Feline Calicivirus Infection: ABCD Guidelines on Prevention and Management"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [diagnosis, management, prevention, disinfection]
jurisdictions: []
evidence_level: guideline
year: 2009
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, guideline, diagnosis, prevention, management]
links:
  doi: "10.1016/j.jfms.2009.05.004"
  url: "https://journals.sagepub.com/doi/10.1016/j.jfms.2009.05.004"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Accessible abstract reports that sick, acutely infected, or carrier cats shed FCV in oronasal and conjunctival secretions."
    - "Accessible abstract reports infection occurs mainly through direct contact."
    - "Accessible abstract reports diagnosis can be achieved by virus isolation or reverse-transcriptase PCR."
    - "Accessible abstract reports positive PCR results should be interpreted with caution because of low-level shedding by persistently infected carriers."
    - "Accessible abstract reports FCV can persist in the environment for about 1 month and is resistant to many common disinfectants."
  source_supported_conclusion:
    - This is the main practical prevention-and-management guideline anchor in the FCV seed set.
    - The paper supports keeping diagnosis explicitly below one-test certainty because carrier-state shedding complicates PCR interpretation.
    - The paper supports FCV management as supportive-care plus environmental-control architecture, not as a drug-first branch.
    - The paper keeps hygiene and disinfectant resistance visible as real prevention logic rather than background detail.
  llm_inference:
    - This source now serves as the first deep-extracted practical-control guideline anchor in the FCV module.
    - The safest downstream read is `carrier-aware diagnosis plus supportive/environmental control`, not `test-first certainty`.
  # V2 enhanced fields
  study_design: "指南型研究，基于已有文献和专家共识，聚焦猫杯状病毒感染的预防与管理"
  core_argument: "猫杯状病毒感染的诊断与管理应警惕携带猫的低水平病毒排泄，诊断不宜仅依赖单一PCR检测，应综合环境控制与支持治疗措施"
  implicit_premise: "PCR检测结果在携带猫中可能产生假阳性，且病毒环境中可持续存在较长时间，影响防控策略效果"
  title_gap: "标题强调防治指南，但实际揭示了携带猫病毒持续排泄对诊断解读和环境消毒策略的复杂挑战"
  evidence_boundary: "本指南未系统评估特异性药物治疗效果，也未覆盖病毒突变株的流行病学变化"
  unexpected_finding: "猫杯状病毒在环境中能存活近一个月且对多种常用消毒剂具高度抗性，这超出常规病毒存活预期"
---

# Feline Calicivirus Infection: ABCD Guidelines on Prevention and Management

## One-Line Summary

ABCD guideline anchor for FCV prevention, diagnosis, carrier-aware interpretation, environmental control, and supportive management.

## Why It Matters For FCV

- gives the module a practical control layer, not just virology and vaccine theory
- explicitly guards against overreading PCR positivity in carrier-prone populations
- now serves as the first FCV deep-extracted guideline/control anchor

## Key Findings

### quoted_fact

- Accessible abstract reports FCV is highly variable and that more severe systemic forms had been observed.
- Accessible abstract reports sick, acutely infected, or carrier cats shed FCV in oronasal and conjunctival secretions.
- Accessible abstract reports virus isolation or RT-PCR can be used for diagnosis.
- Accessible abstract reports PCR positivity should be interpreted carefully because persistently infected carriers may shed at low levels.
- Accessible abstract reports supportive therapy, good nursing care, palatable feeding, mucolytics/nebulisation, and antibiotics for secondary bacterial infection as core management elements.
- Accessible abstract reports FCV can persist in the environment for about one month and resists many common disinfectants.

### source_supported_conclusion

- This source is the current best FCV control guideline anchor for keeping diagnosis, management, and environmental hygiene in one frame.
- The strongest reusable diagnostic boundary is `PCR can detect virus, but context is still required`.
- The strongest reusable management boundary is `supportive and environmental control first`, not treatment ranking.

### llm_inference

- If the module later builds a diagnostic-workup or infection-control page, this card should anchor the carrier-aware caution language.

## Limits / Caveats

- this is a 2009 guideline and needs to be read beside newer FCV reviews
- current card is deep-extracted at worksheet level, but still not full-text reviewed section by section
- the card should not be overused as proof of current vaccine breadth against modern field strains

## Guideline-Control Branch Logic

What can be promoted:

- FCV control needs transmission, diagnosis, nursing care, and hygiene in one frame
- carrier-state shedding is a structural reason to read PCR carefully
- supportive care and environmental control are central management branches

What should be held:

- any current-market vaccine coverage claim
- any one-test diagnosis rhetoric
- any drift from guideline control language into label-style product claims

This card should therefore be reused as a control-architecture source, not as a modern product-comparison source. Its strongest value is that it binds testing caution, carrier-state biology, supportive care, and environmental persistence into one durable operational frame.

## Write-Back Implications

- [risk and recognition](../../topics/fcv/risk-and-recognition.md) should keep PCR positivity below causal certainty.
- [translation brief](../../topics/fcv/translation-brief.md) should keep supportive-care and hygiene central.
- [regulatory brief](../../topics/fcv/regulatory-brief.md) should keep this guideline below jurisdiction-specific label language.

## Open Follow-Up Questions

- which management and disinfection statements remain unchanged in the 2022 review?
- how should this guideline sit under newer VS-FCV and vaccine-diversity papers?

## Linked Entities

- diseases: FCV
- models:
- endpoints: diagnosis, management, prevention, disinfection
- mechanisms: shedding, carrier state
- regulations:
