---
id: src-fcv-006
type: source
title: "Feline calicivirus and other respiratory pathogens in cats with Feline calicivirus-related symptoms and in clinically healthy cats in Switzerland"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [frequency, risk factors, co-infection, symptomatic association]
jurisdictions: [Switzerland]
evidence_level: original-study
year: 2015
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, epidemiology, switzerland, co-infection, symptomatic-vs-healthy]
links:
  doi: "10.1186/s12917-015-0595-2"
  url: "https://link.springer.com/article/10.1186/s12917-015-0595-2"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Accessible abstract reports that 200 FCV-suspect cats and 100 healthy cats from 19 Swiss cantons were sampled in 24 veterinary practices."
    - "Accessible abstract reports FCV PCR prevalences of 45% in FCV-suspect cats and 8% in healthy cats."
    - "Accessible abstract reports that FHV-1, Mycoplasma felis, Chlamydophila felis, and Bordetella bronchiseptica were also tested."
    - "Accessible abstract reports oral ulcerations, salivation, gingivitis, and stomatitis were significantly associated with FCV infection, whereas classical URTD signs were not."
    - "Accessible abstract reports group housing and intact reproductive status were associated with FCV infection."
  source_supported_conclusion:
    - This is the current key symptomatic-versus-healthy FCV epidemiology anchor.
    - The paper supports separating FCV suspicion from FCV confirmation because fewer than half of practitioner-judged suspect cats were FCV-positive.
    - The paper supports keeping co-pathogen structure and multi-cat exposure conditions visible in FCV recognition.
    - The paper supports an oral-disease-heavy FCV recognition read over a flat classical-URTD symptom list.
  llm_inference:
    - This source now serves as the first deep-extracted field-recognition anchor in the FCV module.
    - The safest downstream wording is `composite suspicion with oral weighting`, not `generic cat-flu shorthand`.
  # V2 enhanced fields
  study_design: "前瞻性现场流行病学研究，采样200只被怀疑感染猫杯状病毒的猫及100只临床健康猫，涉及瑞士19个州的24个兽医诊所，采用PCR检测多种呼吸道病原体及临床病征调查"
  core_argument: "在瑞士猫群中，杯状病毒感染与口腔溃疡、流涎、牙龈炎及口炎显著相关，而传统的上呼吸道感染症状并非其典型表现，且临床上对杯状病毒的怀疑并不能完全等同于确认感染，必须同时考虑共感染病原及多猫环境因素以实现准确诊断。"
  implicit_premise: "PCR检测能准确反映猫只杯状病毒感染状态，同时临床症状及其他病原体检测是评估杯状病毒感染的有效补充，且多猫环境增加感染风险。"
  title_gap: "标题仅指出杯状病毒及其他呼吸道病原体的存在，但研究揭示杯状病毒的典型临床表现主要为口腔病变而非传统呼吸道症状，同时健康猫也可能携带病毒，强调需要区分感染怀疑与确认。"
  evidence_boundary: "本研究未评估杯状病毒的具体治疗效果及病毒变异株差异，也未涉及病毒传播机制的实验验证，更未对长期感染后果及免疫状态进行分析。"
  unexpected_finding: "尽管被临床怀疑感染杯状病毒的猫比例高达200只，但实际PCR阳性率仅45%，表明超过一半的怀疑病例并非杯状病毒感染，显示临床症状与病毒检测结果存在明显不匹配。"
---

# Feline calicivirus and other respiratory pathogens in cats with Feline calicivirus-related symptoms and in clinically healthy cats in Switzerland

## One-Line Summary

Swiss field study comparing FCV-suspect and healthy cats, showing that FCV suspicion, healthy shedding, co-pathogens, and oral-disease weighting all need to stay in the same recognition frame.

## Why It Matters For FCV

- helps stop the module from equating FCV-suspect signs with FCV confirmation
- preserves the role of co-infections and healthy shedding in recognition logic
- now serves as the first FCV deep-extracted field-recognition anchor

## Key Findings

### quoted_fact

- Accessible abstract reports that the study sampled 200 FCV-suspect cats and 100 healthy cats from 19 Swiss cantons in 24 veterinary practices.
- Accessible abstract reports FCV PCR prevalences of 45% in suspect cats and 8% in healthy cats.
- Accessible abstract reports co-pathogen prevalences including FHV-1 20%/9%, C. felis 8%/1%, B. bronchiseptica 4%/2%, M. felis 47%/31%, and co-infections 40%/14% in suspect/healthy cats.
- Accessible abstract reports group housing and intact reproductive status were associated with FCV infection.
- Accessible abstract reports vaccinated suspect cats were significantly less often FCV-positive in a univariable approach.
- Accessible abstract/full-page summary reports oral ulcerations, salivation, gingivitis, and stomatitis were significantly associated with FCV infection, but classical URTD signs were not.

### source_supported_conclusion

- This source is the current best FCV recognition-control paper for separating syndrome suspicion from etiologic closure.
- The paper supports co-pathogen-aware recognition rather than FCV-only respiratory shorthand.
- The safest symptom read is that oral-disease-heavy findings are more discriminating than a flat classical-URTD sign list.

### llm_inference

- If the module later builds a diagnostic-workup page, this card should anchor the `less than half of suspect cats were FCV-positive` caution.

## Limits / Caveats

- Swiss practice-level data should not be promoted into universal prevalence claims
- current card is deep-extracted at worksheet level, but still not full-text reviewed section by section

## Recognition-Epidemiology Branch Logic

What can be promoted:

- FCV-compatible symptoms should be read as suspicion, not confirmation
- healthy carriers and co-pathogens are structural parts of recognition
- oral-disease-associated findings carry more recognition weight than a generic URTD symptom list

What should be held:

- any universal prevalence claim from Swiss field numbers
- any symptom-only diagnosis rhetoric
- any interpretation that removes co-pathogens from the front door

## Write-Back Implications

- [risk and recognition](../../topics/fcv/risk-and-recognition.md) should elevate oral-disease-heavy recognition over flat URTD shorthand.
- [FCV recognition architecture memo](../../system/indexes/fcv-recognition-architecture-memo.md) should treat this card as the first deep-extracted epidemiology anchor.
- [current state dashboard](../../topics/fcv/current-state-dashboard.md) can now describe recognition as having one deep-extracted field-control anchor.

## Open Follow-Up Questions

- which factors looked protective or risk-increasing after multivariable adjustment?
- how strongly do these oral-heavy recognition signals replicate in other geographies?

## Linked Entities

- diseases: FCV
- models:
- endpoints: frequency, risk factors, co-infection, symptomatic association
- mechanisms: shedding, co-pathogen interaction
- regulations:
