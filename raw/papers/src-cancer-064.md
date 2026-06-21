---
id: src-cancer-064
type: source
title: "Feline paediatric oncology: retrospective assessment of 233 tumours from cats up to one year (1993 to 2008)"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2010
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
pmid: 20492453
doi: "10.1111/j.1748-5827.2010.00915.x"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, paediatric, oncology, retrospective, assessment, one, year]
links:
  doi: "10.1111/j.1748-5827.2010.00915.x"
  url: "https://doi.org/10.1111/j.1748-5827.2010.00915.x"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Feline paediatric oncology: retrospective assessment of 233 tumours from cats up to one year (1993 to 2008)."
    - "The intake sheet locator is: 10.1111/j.1748-5827.2010.00915.x."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
  # V2 enhanced fields
  study_design: "回顾性病理学实验室研究（2010 年 JSAP），233 例 ≤12 月龄猫肿瘤，英国 Idexx 实验室 1993-2008 活检提交"
  core_argument: "幼猫肿瘤谱系与成年猫不同——淋巴瘤最常见（22%）、软组织肉瘤（15%）、肥大细胞瘤（9%）、鳞状细胞癌（7%）——70% 为恶性——皮肤/软组织是最常见部位（41%）——血液肿瘤占 31%"
  implicit_premise: "假设活检提交比例代表真实肿瘤发生率（存在转诊和提交偏倚）；假设单一实验室数据集可代表更广泛的幼猫肿瘤流行病学"
  unexpected_finding: "淋巴瘤在幼猫中占主导地位——这与成年猫中淋巴瘤也是常见恶性肿瘤的发现一致——但幼猫淋巴瘤可能与 FeLV 关联更强（历史数据支持）"
  title_gap: "标题说幼猫肿瘤学的回顾性评估，但真正发现是分母纪律：活检提交比例（6% 为肿瘤性）不等于种群发病率——需要将幼猫肿瘤数据与全年龄数据分开标注"
  evidence_boundary: "活检提交队列，非种群发病率；支持幼猫肿瘤学概述和肿瘤类别架构，不支持全年龄患病率估计或种群风险计算"
---

# Feline paediatric oncology: retrospective assessment of 233 tumours from cats up to one year (1993 to 2008)

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 2010 JSAP: 233 tumors in cats ≤12 months (UK biopsies 1993-2008); lymphoma 22%, soft-tissue sarcoma 15%, MCT 9%, SCC 7%; hematopoietic 31%; 70% malignant; skin/soft tissue most common site (41%). [Deep extraction worksheet](../../system/indexes/src-cancer-064-deep-extraction-round1.md).

## Source Check, 2026-06-01

PubMed abstract fetched as a zero-cost extraction step.

- PMID: 20492453
- DOI: 10.1111/j.1748-5827.2010.00915.x
- Journal: Journal of Small Animal Practice
- Year: 2010

## Abstract Summary

This retrospective pathology-laboratory study described tumors in cats up to 12 months old using biopsy submissions to Idexx Laboratories, Wetherby, UK.

**Study design:**

| Feature | Abstract-Extracted Detail |
|---------|---------------------------|
| Population | Cats 12 months old or younger |
| Source | Biopsies submitted to Idexx Laboratories, Wetherby, UK |
| Period | September 1993 to March 2008 |
| Submissions screened | 4196 |
| Neoplastic biopsies meeting criteria | 233 |

**Findings:**

- 233/4196 submissions (6%) were neoplastic and met search criteria.
- Tumor categories included hematopoietic (73; 31%), malignant epithelial (44; 19%), malignant mesenchymal (38; 16%), benign epithelial (37; 16%), benign mesenchymal (30; 13%), and miscellaneous (11; 5%).
- The most frequent tumors were lymphoma (51; 22%), soft-tissue sarcoma (34; 15%), mast cell tumor (22; 9%), and squamous cell carcinoma (16; 7%).
- Skin and soft tissues were the most common tumor site (41% of tumors).
- 164 neoplasms (70%) were malignant or had malignant potential.

**Boundary:** These are pediatric-cat biopsy-submission proportions from one UK laboratory dataset, not population incidence or all-age feline cancer prevalence.

## One-Line Summary

Retrospective UK biopsy-submission study describing 233 tumors in cats up to 12 months old.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Feline paediatric oncology: retrospective assessment of 233 tumours from cats up to one year (1993 to 2008).
- The intake sheet locator is: 10.1111/j.1748-5827.2010.00915.x.

### source_supported_conclusion

- Pediatric feline oncology deserves separate denominator labels because this source covers cats 12 months or younger from biopsy submissions.
- Lymphoma, soft-tissue sarcoma, mast cell tumor, and squamous cell carcinoma were the most frequent tumors in this dataset.
- The dataset should not be treated as population incidence.

### llm_inference

- This source can support a future pediatric oncology or registry/prevalence caveat layer.

## Claim-Fit Judgment

Strongest safe use:

- pediatric feline oncology overview
- biopsy-submission denominator discipline
- tumor-category architecture

Must not control yet:

- reader-facing medical advice
- all-age feline tumor prevalence
- population incidence
- treatment or prognosis claims
- owner-facing risk ranking

## Image Asset TODO

- figures to capture: unknown until source text is read
- why these matter: tables or figures should remain behind the candidate gate until labels are verified

## Open Follow-Up Questions

- Does the full text provide site-by-tumor cross-tabulation useful for branch routing?
- How much referral or submission bias is discussed?
- Should pediatric oncology become a separate branch or remain a registry caveat?

## Linked Entities

- diseases: cancer
- models: pediatric feline biopsy-submission cohort
- endpoints: tumor category; tumor site; malignant potential
- mechanisms:
- regulations:
