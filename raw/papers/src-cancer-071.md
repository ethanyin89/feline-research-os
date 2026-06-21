---
id: src-cancer-071
type: source
title: "Expression of Cat Podoplanin in Feline Squamous Cell Carcinomas"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2017
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: 29090969
tags: [cancer, podoplanin, squamous-cell-carcinoma, OSCC, antibody-therapy, biomarker, CLEC-2]
links:
  doi: "10.1089/mab.2017.0046"
  url: "https://doi.org/10.1089/mab.2017.0046"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Of 40 feline SCCs, 38 (95%) showed positive staining for podoplanin (PMab-52)."
    - "12 cases (30%) showed strong membrane-staining pattern."
    - "Sample: 14 mouth floor, 13 skin, 9 ear, 4 tongue."
  source_supported_conclusion:
    - "Podoplanin is highly expressed in feline squamous cell carcinomas."
    - "PMab-52 antibody can be useful for antibody therapy against podoplanin-expressing feline SCCs."
  llm_inference:
    - "Podoplanin represents a potential therapeutic target for feline OSCC."
    - "Supports oral-squamous-cell-carcinoma.md biomarker and targeted therapy claims."
  # V2 enhanced fields
  study_design: "原始研究（2017 年 Monoclon Antib），40 例猫 SCC（口底 14、皮肤 13、耳 9、舌 4），PMab-52 抗体免疫组化染色"
  core_argument: "Podoplanin 在猫 SCC 中高度表达——95%（38/40）阳性——30%（12/40）强膜染色——Podoplanin 通过 CLEC-2 激活血小板聚集参与转移——PMab-52 抗体可用于靶向治疗"
  implicit_premise: "假设免疫组化表达模式代表功能性 podoplanin 活性；假设抗 podoplanin 抗体治疗在猫体内与体外模型类似有效"
  unexpected_finding: "95% 的猫 SCC 表达 podoplanin——这种高表达率使其成为理想的治疗靶点——跨解剖部位（口腔、皮肤、耳）一致性强"
  title_gap: "标题说猫 podoplanin 在猫 SCC 中的表达，但真正发现是治疗潜力：高表达率（95%）+ 抗体开发（PMab-52）+ 转移相关机制（CLEC-2）——为抗体靶向治疗奠定基础"
  evidence_boundary: "摘要级免疫组化和抗体开发证据；支持生物标记物和潜在治疗靶点声明，不支持临床治疗推荐；抗体治疗仍处于研究阶段"
---

# Expression of Cat Podoplanin in Feline Squamous Cell Carcinomas

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 2017 Monoclon Antib Immunodiagn Immunother: 40 feline SCCs (oral, skin, ear); 95% podoplanin positive; 30% strong membrane staining; PMab-52 antibody developed; podoplanin/CLEC-2 pathway involved in metastasis; potential therapeutic target. [Deep extraction worksheet](../../system/indexes/src-cancer-071-deep-extraction-round1.md).

## Source Check, 2026-06-02

| Field | Value |
|-------|-------|
| PMID | 29090969 |
| DOI | 10.1089/mab.2017.0046 |
| Journal | Monoclon Antib Immunodiagn Immunother |
| Year | 2017 |
| Authors | Itai S, Yamada S, Kaneko MK, et al. |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Sample size | 40 feline SCCs |
| Anatomic sites | Mouth floor (14), skin (13), ear (9), tongue (4) |
| Podoplanin positivity | 95% (38/40) |
| Strong membrane staining | 30% (12/40) |
| Antibody used | PMab-52 (anti-cat podoplanin mAb) |
| Mechanism | Podoplanin binds CLEC-2, activates platelet aggregation involved in metastasis |

**Boundary:** Abstract-level extraction. Podoplanin expression rates can inform OSCC biomarker claims. Therapeutic applications are preclinical/investigational.

## One-Line Summary

95% (38/40) of feline SCCs express podoplanin; PMab-52 antibody developed for potential targeted therapy against CLEC-2-mediated metastasis.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- 40 feline SCCs analyzed (mouth floor 14, skin 13, ear 9, tongue 4)
- 95% (38/40) showed positive podoplanin staining with PMab-52
- 30% (12/40) showed strong membrane-staining pattern
- Podoplanin binds CLEC-2, activates platelet aggregation involved in metastasis

### source_supported_conclusion

- Podoplanin is highly expressed across anatomic sites in feline SCC
- Anti-cat podoplanin antibody PMab-52 developed via cell-based immunization and screening (CBIS)
- Potential for antibody-based targeted therapy against feline SCCs

### llm_inference

- Supports oral-squamous-cell-carcinoma.md claims about biomarkers and potential therapeutic targets
- Podoplanin could be used alongside COX-2 and other markers for FOSCC characterization
- Investigational therapeutic approach; not yet clinical

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
