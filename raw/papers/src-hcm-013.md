---
id: src-hcm-013
type: source
title: "Diagnostic Value of Morphometry in Feline Hypertrophic Cardiomyopathy"
source_kind: paper
species: feline
diseases: [HCM]
models: []
endpoints: [morphometry]
jurisdictions: []
evidence_level: original-study
year: 2011
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [hcm, diagnosis, morphometry]
links:
  doi: ""
  url: "https://www.sciencedirect.com/science/article/abs/pii/S0021997511003537?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The summary states that the study aimed to identify morphometric criteria that clearly distinguish feline HCM from normal hearts."
    - "The summary states that hearts from 15 cats with HCM had increased relative heart weights compared with 15 matched controls."
    - "The summary states that several macroscopically defined areas, including ventricular walls and septum, were significantly increased in HCM."
    - "The summary states that histological morphometric analyses did not identify significant differences in cardiomyocyte size, branching, or myocardial fibrosis."
    - "The summary states that only relative heart weight and macroscopical analyses were useful in distinguishing HCM from normal hearts."
  source_supported_conclusion:
    - Morphometry is already a distinct recognition and endpoint branch in the HCM seed set.
    - The paper supports gross morphometry more strongly than histologic micromorphometry for distinguishing HCM from normal hearts.
    - The study argues against overassuming that cardiomyocyte diameter is the principal diagnostic change in feline HCM.
    - The safest promotion from this source is a `macrostructure > micromorphometry` rule, not a universal pathology-ranking claim.
    - The paper helps keep structural recognition quantitative without letting cell-level pathology metrics outrun their actual discriminative support.
  llm_inference:
    - This may become a useful boundary source between phenotype definition and pathology staging.
    - Risk-recognition pages should probably keep gross structural morphometry inside the recognition branch while holding histologic micromorphometry lower in the depth layer.
  # V2 enhanced fields
  study_design: "原始研究，15 只 HCM 猫与 15 只匹配对照比较形态测量标准"
  core_argument: "相对心脏重量和宏观结构测量可区分 HCM 与正常心脏——但组织学微形态测量（心肌细胞大小、分支、纤维化）未显示显著差异"
  implicit_premise: "假设病理形态计量可以转化为诊断实践；假设宏观结构优于微观结构用于首要诊断区分"
  unexpected_finding: "心肌细胞直径和纤维化量化在此数据集中无法可靠区分 HCM——这挑战了细胞级病理测量作为常规诊断标准的假设"
  title_gap: "标题说形态测量诊断价值，但真正发现是组织学的局限：心肌细胞大小和纤维化量化无法可靠区分 HCM——只有宏观结构指标有效"
  evidence_boundary: "15 只猫的数据集限制精确阈值推广；形态测量边界不能直接推断到生前成像实践"
---

# One-line Summary

Morphometry-based diagnosis paper that strengthens structural phenotype recognition and sharply bounds what histologic micromorphometry can actually discriminate.

## Why It Matters For HCM

- adds a quantitative structural branch beneath echocardiography
- may sharpen phenotype-definition language
- now gives the HCM shell a safer rule that gross morphometry can help more than cell-level histologic quantification for diagnosis

## Key Findings

- diagnostic value focus
- summary supports relative heart weight and macrostructural measurements as discriminative
- summary does not support cardiomyocyte-size or fibrosis quantification as clear diagnostic separators in this dataset

## Why This Study Matters

This paper matters because it sharpens a part of HCM recognition that can easily become sloppy in compiled pages. Once morphology enters the discussion, it is tempting to flatten all quantitative pathology into one bucket and imply that every microscopic abnormality is equally useful for diagnosis.

This source argues against that shortcut. Its positive signal sits at the gross morphometric level: relative heart weight and macroscopically defined ventricular and septal measures helped separate HCM from controls. Its negative signal is just as important: histologic micromorphometry, including cardiomyocyte-size and fibrosis-related measures, did not clearly discriminate groups in this dataset.

That makes the source structurally valuable. It does not just add one more morphometry citation. It gives the module a safer rule for endpoint and recognition compression: quantified structure is useful, but the useful layer here is macrostructure, not every plausible microscopic pathology metric.

## Macro-Versus-Micro Boundary

The most reusable write-back from this study is:

- quantified gross structure can support phenotype recognition
- relative heart weight and gross sectional enlargement belong in the recognition-facing branch
- histologic micromorphometry should stay bounded below first-pass diagnostic authority
- fibrosis and cell-level pathology may still matter for staging or depth, but this paper does not justify promoting them as routine diagnostic discriminators

That boundary is what keeps the page layer from overstating how much pathology detail is already operational at diagnosis.

## Limits / Caveats

- current card is abstract-weighted, not full-text reviewed
- The summary supports direction and branch placement, but not precise morphometric thresholds for routine use.
- The negative micromorphometry finding should be treated as a dataset-bounded caution, not as proof that microscopic pathology never matters in feline HCM.

## Open Follow-up Questions

- which morphometric measures are most discriminative?
- how does morphometry interact with echocardiography in this paper?
- how strongly should this paper limit future claims about histologic micro-measures as routine diagnostic criteria?
- which gross measures carried the clearest separation signal?
- how closely do these pathologic morphometric distinctions map onto ante-mortem imaging practice?

## Linked Entities

- HCM
- morphometry
