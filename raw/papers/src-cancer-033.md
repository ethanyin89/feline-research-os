---
id: src-cancer-033
type: source
title: "Feline leukemia virus infection and diseases"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 1991
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
pmid: 1666070
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, leukemia, virus, infection, diseases]
links:
  doi: ""
  url: "https://pubmed.ncbi.nlm.nih.gov/1666070/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Feline leukemia virus infection and diseases."
    - "The intake sheet locator is: https://pubmed.ncbi.nlm.nih.gov/1666070/."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
  # V2 enhanced fields
  study_design: "综合综述（1991 年），FeLV 生物学、发病机制和疾病机制的全面回顾"
  core_argument: "FeLV 的效应是矛盾的——同时导致细胞增殖性疾病（淋巴瘤、骨髓增生性疾病）和细胞抑制性疾病（免疫缺陷、骨髓抑制）——感染结局取决于暴露后最初几周的宿主/病毒相互作用"
  implicit_premise: "假设 1991 年的分子机制描述在基本层面仍然有效；假设宿主免疫控制逆转录病毒的范式可指导疫苗开发"
  unexpected_finding: "FeLV 的致病性（胸腺淋巴瘤、急性免疫抑制或再生障碍性贫血）被定位到病毒表面糖蛋白和/或长末端重复区域——同一病毒的微小遗传变异可导致完全不同的疾病表型"
  title_gap: "标题说猫白血病病毒感染和疾病，但真正发现是宿主控制：许多猫能有效遏制和终止病毒复制——这是宿主免疫控制逆转录病毒感染的重要范例——疫苗可选择性增强这一过程"
  evidence_boundary: "1991 年综述，分子病毒学进展可能已扩展对毒株特异性发病机制的理解；现代 FeLV 检测和疫苗策略可能已演变"
---

# Feline leukemia virus infection and diseases

## Evidence-Depth Caveat

This is an abstract-weighted source card. Comprehensive 1991 review of FeLV biology, pathogenesis, and disease mechanisms.

## Full Abstract (PubMed)

Feline leukemia virus is a naturally occurring, contagiously transmitted and oncogenic immunosuppressive retrovirus of cats. The effects of FeLV are paradoxical, causing cytoproliferative and cytosuppressive disease (eg, lymphoma and myeloproliferative disorders vs immunodeficiency and myelosuppressive disorders). In the first few weeks after virus exposure, interactions between FeLV and hemolymphatic system cells determine whether the virus or the cat will dominate in the host/virus relationship--persistent viremia and progressive infection or self limiting, regressive infection will develop. The outcome of these early host/virus interactions is revealed in the diagnostic assays for FeLV antigenemia and viremia. The latter, in turn, predict the outcome of FeLV infection in cats. Known host resistance factors include age and immune system functional status. Known virus virulence factors are magnitude of exposure and virus genotype. Molecular analysis of FeLV strains indicated that natural virus isolates exist as mixtures of closely related virus genotypes and that minor genetic variations among FeLV strains can impart major differences in pathogenicity. The genetic coding regions responsible for cell targeting and specific disease inducing capacity (eg, thymic lymphoma, acute immunosuppression, or aplastic anemia) have been mapped to the virus surface glycoprotein and/or long terminal repeat regions for several FeLV strains. Infection by specific FeLV strains leads to either malignant transformation or cytopathic deletion of specific lymphocyte and hemopoietic cell population, changes that prefigure the onset of clinical illness. Another notable feature of the biology of FeLV is that many cats are able to effectively contain and terminate viral replication, an important example of host immunologic control of a retrovirus infection and a process that can be selectively enhanced by vaccination.

## Key Extracted Findings

| Finding | Value | Boundary |
|---------|-------|----------|
| FeLV disease paradox | causes both proliferative and suppressive disease | lymphoma vs immunodeficiency |
| Proliferative diseases | lymphoma, myeloproliferative disorders | oncogenic pathway |
| Suppressive diseases | immunodeficiency, myelosuppressive disorders | cytopathic pathway |
| Infection outcome determinants | early host/virus interactions in first weeks | persistent vs regressive |
| Host resistance factors | age, immune system functional status | predict outcome |
| Virus virulence factors | exposure magnitude, genotype | predict outcome |
| Disease-specific genetics | mapped to surface glycoprotein and/or LTR regions | thymic lymphoma, immunosuppression, aplastic anemia |
| Host immune control | many cats can contain and terminate viral replication | natural resistance |
| Vaccination effect | can selectively enhance host control of replication | immunoprophylaxis |

**Boundary:** This is a 1991 review. Molecular mechanisms remain valid but specific strain characterization may have expanded since publication.

## One-Line Summary

Candidate cancer source from sheet row 36. Use it for triage until abstract or full-text extraction proves a stronger role.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Feline leukemia virus infection and diseases.
- The intake sheet locator is: https://pubmed.ncbi.nlm.nih.gov/1666070/.

### source_supported_conclusion

- This is a first-pass source-card placeholder for triage and queue control.
- It should not support prevalence, diagnostic, treatment, management, or risk-ranking claims yet.

### llm_inference

- The title suggests a possible `cancer` role, but the actual claim-fit requires abstract or full-text review.

## Claim-Fit Judgment

Strongest safe use:

- intake ownership
- source queue placement
- deduplication and future extraction planning

Must not control yet:

- reader-facing medical advice
- numeric claims
- comparative ranking
- guideline-like recommendations
- mechanism closure

## Image Asset TODO

- figures to capture: unknown until source text is read
- why these matter: tables or figures should remain behind the candidate gate until labels are verified

## Open Follow-Up Questions

- What source family is confirmed by the abstract or article body?
- Which claims, if any, are reusable for the cancer module?
- Does this source deserve deep extraction, or should it remain queue context?
- Are there tables or figures that change the module structure?

## Linked Entities

- diseases: cancer
- models:
- endpoints:
- mechanisms:
- regulations:
