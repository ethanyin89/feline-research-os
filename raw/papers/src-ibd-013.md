---
id: src-ibd-013
type: source
title: "Cats with Inflammatory Bowel Disease and Intestinal Small Cell Lymphoma Have Low Serum Concentrations of 25-Hydroxyvitamin D"
source_kind: paper
species: feline
diseases: [IBD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2014
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, vitamin-d, lymphoma-boundary]
links:
  doi: "10.1111/jvim.12294"
  url: "https://academic.oup.com/jvim/article/28/2/351/8452230"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The abstract reports 84 cats total, including 23 healthy cats, 41 hospitalized ill cats with nongastrointestinal disease, and 20 cats with IBD or intestinal small-cell lymphoma.
    - The abstract states that serum 25-hydroxyvitamin D concentrations were significantly lower in cats with IBD or small-cell lymphoma than in healthy cats and hospitalized ill cats.
    - The abstract reports a moderate positive correlation between serum albumin and 25-hydroxyvitamin D concentrations in the gastrointestinal disease group.
  source_supported_conclusion:
    - This source belongs in a shared support-marker branch rather than a clean discriminator branch.
    - The study supports vitamin D as a burden or complication-context marker, not as an IBD-versus-lymphoma separator.
  llm_inference:
    - This paper is best used to keep systemic nutritional-burden markers below frontier discriminators and below core workup layers.
  # V2 enhanced fields
  study_design: "前瞻性研究，84只猫分为健康组（23只）、非胃肠疾病住院组（41只）及IBD或肠道小细胞淋巴瘤组（20只），测定血清25-羟基维生素D浓度及血清白蛋白水平"
  core_argument: "患有炎症性肠病或肠道小细胞淋巴瘤的猫血清25-羟基维生素D浓度显著低于健康猫及非胃肠疾病住院猫，且维生素D水平与血清白蛋白呈中度正相关"
  implicit_premise: "血清25-羟基维生素D浓度能够反映猫体内的维生素D状态且与胃肠道病理状态相关"
  title_gap: "标题指出IBD及小细胞淋巴瘤猫血清维生素D浓度低，但研究发现维生素D更适合作为疾病负担或并发症指标，而非区分IBD与淋巴瘤的诊断标志——这提示维生素D水平在临床解读中应体现疾病严重程度而非病种差异"
  evidence_boundary: "本研究未能区分维生素D水平在诊断IBD与肠道小细胞淋巴瘤上的差异性，亦未探讨维生素D补充对疾病进展或预后的影响"
  unexpected_finding: "血清25-羟基维生素D浓度与血清白蛋白存在中度正相关，提示营养状态或蛋白质代谢异常可能影响维生素D水平"
---

# One-line Summary

Vitamin D paper that likely supports burden or systemic-context interpretation more than direct discrimination between IBD and small-cell lymphoma.

## Why It Matters For IBD

- adds a serum support-marker branch to the module
- may help keep `marker abnormality` separate from `marker discrimination`
- now serves as the first vitamin-D support-marker anchor in the IBD module

## Key Findings

- abstract includes healthy, nongastrointestinal ill, and gastrointestinal disease comparison groups
- abstract reports lower vitamin D in the IBD or small-cell lymphoma group than in both comparison groups
- abstract reports overlap across groups despite significant median differences
- abstract reports positive correlation between albumin and vitamin D in gastrointestinal disease cats

## Serum Support-Marker Role

This source should be used as a shared burden-marker anchor, not as an IBD-versus-lymphoma discriminator. The study included 84 cats total: healthy cats, hospitalized ill cats with nongastrointestinal disease, and cats with IBD or intestinal small-cell lymphoma. Serum 25-hydroxyvitamin D concentrations were lower in the gastrointestinal disease group than in both comparison groups, but the card must preserve the reported overlap across groups.

The albumin relationship is the most important placement clue. In the gastrointestinal disease group, serum albumin and 25-hydroxyvitamin D had a moderate positive correlation. That suggests vitamin D may belong near burden, malabsorption, nutritional state, inflammation, or complication context rather than near direct disease-class separation. The endpoint handbook should therefore place this below biopsy-centered and imaging-centered boundary work.

For wiki reuse, this card helps teach the difference between marker abnormality and marker discrimination. A marker can be significantly abnormal in sick cats and still fail as a boundary tool. That distinction is critical in feline chronic enteropathy because many markers may separate disease from health without separating IBD from small-cell lymphoma.

The source also pairs well with `src-ibd-017` on fecal S100A12. Both are support markers that signal abnormal chronic enteropathy or systemic burden but do not carry the main lymphoma-exclusion burden. It also pairs with `src-ibd-022`, because fibrosis-associated low albumin may make systemic burden language more coherent across the module.

The safe compiled rule is: low vitamin D is a real support-context finding in cats with IBD or intestinal small-cell lymphoma, but current evidence in this card does not make it a class-separating diagnostic test or a treatment-directing endpoint by itself.

That makes it useful for burden language, not for shortcut diagnosis.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- shared abnormality does not automatically make a good diagnostic separator
- do not infer vitamin D supplementation strategy from this card alone
- group overlap should stay visible whenever lower vitamin D is mentioned

## Open Follow-up Questions

- is vitamin D linked more to burden, malabsorption, inflammation, or prognosis?
- does the paper show meaningful differences between IBD and lymphoma?
- how should vitamin D be integrated with albumin, body weight, and fibrosis markers?
- does full-text analysis support prognosis or only cross-sectional burden framing?

## Deep Extraction

- [src-ibd-013 deep extraction round 1](../../system/indexes/src-ibd-013-deep-extraction-round1.md)

## Linked Entities

- vitamin D
- small-cell lymphoma
- support biomarker
