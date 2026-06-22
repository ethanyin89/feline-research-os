---
id: src-ibd-008
type: source
title: "Impact of Changes in Gastrointestinal Microbiota in Canine and Feline Digestive Diseases"
source_kind: paper
species: feline
diseases: [IBD]
models: [canine]
endpoints: []
jurisdictions: []
evidence_level: review
year: 2020
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, microbiota, review]
links:
  doi: ""
  url: "https://www.sciencedirect.com/science/article/pii/S0195561620301029?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source reviews microbiota changes in canine and feline digestive diseases.
  source_supported_conclusion:
    - This source likely works as a broad dysbiosis-context page rather than a feline IBD-specific authority by itself.
  llm_inference:
    - This may be a good secondary review anchor once the feline-primary branch is denser.
  # V2 enhanced fields
  study_design: "综述性研究，涵盖犬猫消化系统疾病中的肠道微生物群变化，基于已发表文献的综合分析（2020 年）"
  core_argument: "犬猫消化系统疾病中肠道微生物群的紊乱是病理机制的关键组成部分——但微生物群失调是疾病的关联因素还是因果因素仍需区分"
  implicit_premise: "已有文献中关于犬猫肠道微生物群的研究结果具有较高的可比性与综述整合价值"
  title_gap: "标题提及犬猫消化疾病中的微生物变化，但覆盖两个物种意味着猫特异性证据被稀释——真正价值是提供微生物失调的广泛背景视角，而非猫 IBD 的权威分析"
  evidence_boundary: "综述性质无法提供原始菌群数据或干预效应量；犬猫合并分析可能掩盖物种特异性差异；未针对猫 IBD 的具体诊断标准、治疗方案或微生物干预提供实证数据"
---

# One-line Summary

Cross-species microbiota review that likely broadens background framing for feline digestive disease without leading the core IBD module.

## Why It Matters For IBD

- helps keep feline microbiota findings inside a wider digestive-disease context
- may support later explanation pages for dysbiosis without replacing feline-primary evidence

## Key Findings

- title spans both canine and feline digestive disease
- likely useful for background mechanism and translation context

## Cross-Species Microbiota Review Role

This review belongs in the broad dysbiosis-context branch. It reviews gastrointestinal microbiota changes in canine and feline digestive diseases, which makes it useful for framing but not sufficient for feline IBD-specific diagnostic authority. The key value is comparative context: feline microbiota findings sit inside a wider small-animal digestive-disease literature rather than appearing as isolated one-off observations.

For wiki reuse, this card should support introductory microbiota paragraphs after feline-primary anchors have done the evidence work. `src-ibd-006` gives older targeted FISH-based feline IBD microbiota context. `src-ibd-001` connects microbiota to the IBD-versus-small-cell-lymphoma boundary. `src-ibd-019` adds fecal metabolomic frontier stratification. This review can help explain the broader dysbiosis landscape, but it should not displace those feline-primary sources.

The source is also useful for preventing overnarrow mechanism writing. IBD and chronic enteropathy are not only pathology labels; they involve host-microbe interactions, mucosal immune context, and possibly metabolic effects. A broad review can make that terrain easier to summarize for non-specialist outputs.

The claim ceiling is species and scope. Because the title spans canine and feline disease, every feline-specific claim must either come from full-text feline subsections or be supported by feline-primary studies elsewhere. The card should not be used to make IBD-versus-lymphoma boundary claims, treatment recommendations, or feline-specific diagnostic rankings unless those are directly recovered.

The safest output use is background: `microbiota changes are part of digestive-disease context, but feline IBD workup still depends on exclusion, biopsy strategy, imaging support, and bounded marker interpretation`.

This card is particularly useful for cross-disease comparison. Canine and feline digestive disease may share broad dysbiosis themes, while feline-specific workup remains constrained by the IBD-versus-lymphoma boundary. That distinction lets the module use comparative review material without importing canine certainty into feline decision-making.

The card should also help with language in broad outputs. Instead of saying `IBD is caused by dysbiosis`, the safer construction is `microbiota changes are part of the digestive-disease landscape and may interact with inflammation, but the feline evidence base still requires source-specific boundaries`.

If later full-text review finds clear feline subsections, those should be extracted into specific support claims. Until then, this source remains a secondary review context source and should not be used for numeric or diagnostic statements.

That makes it useful for synthesis prose, not for endpoint tables. It can explain why the microbiota family exists while leaving hard feline claims to primary feline studies and full-text checks later instead.

Its role is broad orientation, not proof.

## Limits / Caveats

- current card is title-led ingest, not full-text reviewed
- cross-species reviews should not replace feline-primary diagnosis or treatment evidence
- do not convert canine-heavy review claims into feline-specific rules without checking full text
- do not use this review as the lead source for the lymphoma boundary

## Deep Extraction

- [src-ibd-008 deep extraction round 1](../../system/indexes/src-ibd-008-deep-extraction-round1.md)

## Open Follow-up Questions

- how much feline-specific content does the review actually contain?
- does it distinguish inflammatory disease from lymphoma or only discuss dysbiosis broadly?
- which claims remain after strict feline-only filtering?
- does it discuss therapeutic microbiota interventions, or mainly mechanism?

## Linked Entities

- microbiota
- dysbiosis
- digestive disease
- comparative review
