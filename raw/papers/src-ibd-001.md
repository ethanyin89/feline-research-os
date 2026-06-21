---
id: src-ibd-001
type: source
title: "Relationship of the mucosal microbiota to gastrointestinal inflammation and small cell intestinal lymphoma in cats"
source_kind: paper
species: feline
diseases: [IBD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2018
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, microbiota, lymphoma-boundary]
links:
  doi: "10.1111/jvim.15291"
  url: "https://academic.oup.com/jvim/article/32/5/1692/8449664"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The abstract states that the gastrointestinal microbiota in healthy cats is altered in IBD and that little research has identified specific bacterial groups associated with small-cell gastrointestinal lymphoma.
    - The study included 14 cats with IBD and 14 cats with small-cell gastrointestinal lymphoma.
    - The abstract states that Enterobacteriaceae were more abundant in cats with small-cell lymphoma than in cats with IBD.
    - The abstract states that Bifidobacterium spp., Bacteroides spp., and Prevotella spp. were less abundant in small-cell lymphoma than in IBD.
  source_supported_conclusion:
    - This source sits at the microbiota-to-boundary interface of the IBD module.
    - The study supports microbiota differences as a real boundary-pressure branch, but not yet as a routine lead diagnostic layer.
  llm_inference:
    - This was a high-value early deep extraction because it prevents microbiota from being modeled as generic dysbiosis with no diagnostic consequences.
  # V2 enhanced fields
  study_design: "前瞻性病例对照研究，纳入14只炎症性肠病猫及14只小细胞肠道淋巴瘤猫，采用肠黏膜微生物群16S rRNA测序分析"
  core_argument: "小细胞肠道淋巴瘤猫的肠道黏膜微生物群与炎症性肠病猫存在显著差异，尤其是肠杆菌科丰度增加而双歧杆菌属、拟杆菌属及普氏菌属丰度降低"
  implicit_premise: "肠道黏膜微生物群的组成变化能够反映和影响猫的肠道炎症状态及肠道淋巴瘤的发生发展"
  title_gap: "标题强调肠道微生物群与炎症及淋巴瘤的关系，但真正发现是特定细菌群在炎症性肠病和小细胞肠道淋巴瘤中呈现对比丰度差异——提示微生物群可能参与不同病理机制"
  evidence_boundary: "研究未揭示这些微生物群变化是否具有诊断敏感性或预测价值，也未确定因果关系或治疗靶点"
  unexpected_finding: "小细胞肠道淋巴瘤猫中肠杆菌科明显增多，而通常认为益生的双歧杆菌属和普氏菌属却显著减少，提示肿瘤相关微生物失衡特征"
---

# One-line Summary

Microbiota paper that likely helps connect feline IBD inflammation with the neighboring small-cell lymphoma boundary.

## Why It Matters For IBD

- helps prevent microbiota discussion from floating free of actual disease-boundary questions
- may become a core anchor for `IBD versus small-cell lymphoma` compression
- now serves as the first microbiota-boundary anchor in the IBD module

## Key Findings

- abstract included 14 cats with IBD and 14 cats with small-cell gastrointestinal lymphoma
- abstract reports higher Enterobacteriaceae abundance in lymphoma than IBD
- abstract reports lower Bifidobacterium, Bacteroides, and Prevotella abundance in lymphoma than IBD
- abstract links bacterial findings with CD11b-positive and NF-kappaB expression rather than treating microbiota as an isolated signal

## Microbiota-Boundary Role

This source gives the IBD module a microbiota branch that is tied directly to the small-cell lymphoma boundary. That matters because microbiota discussions often drift into generic dysbiosis language. Here, the comparison is more pointed: cats with IBD are compared with cats with small-cell gastrointestinal lymphoma, and the bacterial shifts are linked with mucosal inflammatory signaling.

The reusable facts are specific. The study included 14 cats with IBD and 14 cats with small-cell gastrointestinal lymphoma. Enterobacteriaceae were more abundant in lymphoma than in IBD, while Bifidobacterium spp., Bacteroides spp., and Prevotella spp. were less abundant in lymphoma than in IBD. The methods also correlated bacterial groups identified by FISH in gastrointestinal biopsies with CD11b-positive and NF-kappaB expression. That makes the source a bridge between microbial composition, mucosal immune activation, and disease-boundary pressure.

The safe wiki role is below biopsy authority. Microbiota differences can help explain why inflammatory and neoplastic intestinal disease may not be biologically identical, and they may support future classifier hypotheses. But this paper should not be turned into a routine first-line diagnostic test or a causal claim that bacterial shifts produce lymphoma.

For the mechanism overview, this card should prevent the microbiota branch from being isolated from real diagnostic problems. For risk/recognition, it should be framed as boundary-supporting biology: useful for understanding the IBD-versus-lymphoma landscape, not a replacement for imaging, biopsy-site strategy, histopathology, or immunophenotyping.

This card also belongs near `src-ibd-006` and `src-ibd-008`. Together they can support a microbiota family, but `src-ibd-001` should remain the one that directly connects dysbiosis to the lymphoma boundary.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- microbiota correlation should not be promoted into causal certainty without deeper read
- do not promote bacterial abundance patterns into a validated diagnostic panel
- small cohort size should stay visible when using boundary-language

## Open Follow-up Questions

- does the study separate IBD and lymphoma cleanly or model them as adjacent states?
- which bacterial shifts are strongest and are they clinically reusable?
- how much do sampling location and FISH probe choice affect the observed signal?
- can this source support a future microbiota-boundary memo without overclaiming clinical readiness?

## Deep Extraction

- [src-ibd-001 deep extraction round 1](../../system/indexes/src-ibd-001-deep-extraction-round1.md)

## Linked Entities

- microbiota
- chronic enteropathy
- small-cell lymphoma
