---
id: src-cancer-065
type: source
title: "Feline Lymphoma in the Post—Feline Leukemia Virus Era"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: [USA]
evidence_level: retrospective-study
year: 2005
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: "15954547"
tags: [cancer, lymphoma, FeLV, intestinal-lymphoma, mediastinal, Siamese, IBD, epidemiology]
links:
  doi: "10.1892/0891-6640(2005)19[329:flitpl]2.0.co;2"
  url: "https://academic.oup.com/jvim/article/19/3/329/8454009"
  pubmed: "https://pubmed.ncbi.nlm.nih.gov/15954547/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Lymphoma is the most common neoplasm of the hematopoietic system of cats."
    - "The cat has the highest incidence for lymphoma of any species."
    - "A 21-year retrospective survey covering the period 1983-2003 was conducted at UC Davis VMTH."
    - "A significant decrease in the importance of FeLV-associated types of lymphoma in cats."
    - "The incidence of lymphoma in cats actually increased from 1982 to 2003."
    - "This increase was due largely to a rise in the incidence of intestinal lymphoma."
    - "A high incidence of mediastinal lymphomas in young Siamese or Oriental breeds."
    - "Associations of intestinal lymphoma and inflammatory bowel disease and diet should be further considered."
  source_supported_conclusion:
    - "This source directly addresses the FeLV-shift context needed for lymphoma branch."
    - "Despite FeLV decline, overall lymphoma increased due to intestinal lymphoma rise."
    - "Breed-specific patterns (Siamese mediastinal) are documented."
    - "IBD-lymphoma association is flagged for further investigation."
  llm_inference:
    - "Combined with src-cancer-063 (LGAL molecular) and src-cancer-068 (Australian demographics), provides modern lymphoma context."
    - "The IBD-diet-lymphoma connection needs explicit uncertainty framing."
  # V2 enhanced fields
  study_design: "回顾性流行病学研究（2005 年 JVIM），UC Davis VMTH 1983-2003 年 21 年猫淋巴瘤病例回顾"
  core_argument: "后 FeLV 时代淋巴瘤流行病学发生了根本转变——FeLV 相关淋巴瘤减少但总发病率反而增加——增加主要由肠道淋巴瘤驱动——暹罗/东方品种在年轻猫中纵隔淋巴瘤高发——IBD 和饮食与肠道淋巴瘤的关联值得进一步研究"
  implicit_premise: "假设单中心（UC Davis）数据可代表更广泛趋势；假设 FeLV 检测/疫苗接种是 FeLV 相关淋巴瘤减少的主因"
  unexpected_finding: "尽管 FeLV 相关淋巴瘤减少，总淋巴瘤发病率实际上增加了——这个'悖论'表明非 FeLV 因素在现代猫淋巴瘤中更重要——肠道淋巴瘤的崛起是主要驱动力"
  title_gap: "标题说后 FeLV 时代的猫淋巴瘤，但真正发现是流行病学转变的量化：FeLV-淋巴瘤减少同时总淋巴瘤增加——由肠道型驱动——暗示新的病因学关注点（IBD、饮食）"
  evidence_boundary: "单中心回顾性研究（UC Davis）；支持 FeLV 转变背景和肠道淋巴瘤崛起假说，不直接支持 IBD-饮食病因声明；2005 年发表可能不反映 2020s 模式"
---

# Feline Lymphoma in the Post—Feline Leukemia Virus Era

## Evidence-Depth Caveat

This card has deep extraction based on the PubMed abstract (PMID: 15954547). It is a 2005 UC Davis 21-year retrospective study (1983-2003) documenting the FeLV-to-intestinal lymphoma shift. This directly addresses the open synthesis question about FeLV context. [Deep extraction worksheet](../../system/indexes/src-cancer-065-deep-extraction-round1.md).

## One-Line Summary

21-year UC Davis retrospective showing FeLV-associated lymphoma decreased while intestinal lymphoma increased, with Siamese mediastinal lymphoma pattern and IBD association flagged.

## Why It Matters For Feline Cancer

This source directly answers the lymphoma branch's open question about FeLV/GI-shift claims (synthesis-index Q1). Key findings:

- Lymphoma is most common hematopoietic neoplasm in cats
- Cats have highest lymphoma incidence of any species
- FeLV testing/vaccination reduced FeLV-associated lymphoma
- But overall lymphoma incidence INCREASED 1982-2003
- Increase driven by intestinal lymphoma
- Siamese/Oriental breeds show high mediastinal lymphoma in young cats
- IBD and diet associations warrant further study

## Key Findings

### quoted_fact

- "Lymphoma is the most common neoplasm of the hematopoietic system of cats."
- "The cat has the highest incidence for lymphoma of any species."
- "A significant decrease in the importance of FeLV-associated types of lymphoma."
- "The incidence of lymphoma in cats actually increased from 1982 to 2003."
- "This increase was due largely to a rise in the incidence of intestinal lymphoma, and to a lesser degree, of atypical lymphoma."
- "A high incidence of mediastinal lymphomas in young Siamese or Oriental breeds."
- "Associations of intestinal lymphoma and inflammatory bowel disease and diet should be further considered."

### source_supported_conclusion

- FeLV decline paradoxically coincided with lymphoma increase.
- Intestinal lymphoma is the driver of modern lymphoma burden.
- Breed-specific patterns exist (Siamese mediastinal).
- IBD-lymphoma continuum deserves investigation.

### llm_inference

- Combined with src-cancer-063 (JAK/STAT, IBD continuum) and src-cancer-068 (Australian demographics), this completes the modern lymphoma context.
- The FeLV shift claim can now be promoted to the lymphoma page.

## Claim-Fit Judgment

Strongest safe use:

- FeLV-shift historical context
- Intestinal lymphoma rise documentation
- Breed-specific pattern (Siamese mediastinal)
- IBD-lymphoma hypothesis framing

Should use with caveats:

- Single-institution study (UC Davis)
- 2005 publication may not reflect 2020s patterns

Must not control yet:

- Diet recommendations
- IBD treatment guidance
- Prognosis or survival claims

## Open Follow-Up Questions

- Does full-text provide incidence rates per 100,000 cats?
- What IBD-lymphoma hypotheses are proposed?
- How do 2005 patterns compare to 2024 Australian data?

## Linked Entities

- diseases: cancer, lymphoma, intestinal lymphoma, mediastinal lymphoma
- models:
- endpoints: incidence, time-trend
- mechanisms: FeLV, IBD
- regulations:
