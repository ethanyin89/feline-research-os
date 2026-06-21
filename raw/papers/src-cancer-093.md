---
id: src-cancer-093
type: source
title: "Phosphoproteomic profiling of feline mammary carcinoma: Insights into tumor grading and potential therapeutic targets"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2025
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
pmid: 40839607
tags: [cancer, mammary, FMC, proteomics, phosphorylation, grading, biomarkers]
links:
  doi: "10.1371/journal.pone.0330520"
  url: "https://doi.org/10.1371/journal.pone.0330520"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "PubMed-indexed: PLoS One. 2025 Aug 21;20(8):e0330520."
    - "Authors: Aruvornlop P, Ploypetch S, Sakcamduang W, et al."
    - "FMC is most prevalent reproductive tumor in queens."
    - "Characterized by aggressive metastatic progression and short survival."
    - "Protein phosphorylation dysregulation linked to cancer progression."
  source_supported_conclusion:
    - "Phosphoproteomic profiling to identify FMC grading biomarkers."
    - "Therapeutic target identification through protein analysis."
  llm_inference:
    - "May inform mammary-carcinoma.md molecular grading section."
    - "Novel biomarker candidates for FMC prognosis."
  # V2 enhanced fields
  study_design: "磷酸化蛋白质组学研究（2025 年 PLoS One），31 例 FMC + 6 例正常对照，11942 个磷酸化蛋白分析"
  core_argument: "磷酸化蛋白质组学可识别 FMC 分级相关蛋白和治疗靶点——17 个显著下调的磷酸化蛋白——PRKAG3 与 Ki-67 显著相关（p=0.03）——高三阴性比例（35.5%）——但肿瘤分级间无显著差异"
  implicit_premise: "假设蛋白质磷酸化失调是 FMC 进展的驱动因素；假设识别的磷酸化蛋白差异具有功能意义而非旁观者效应"
  unexpected_finding: "尽管研究目标是识别分级生物标志物，但肿瘤分级间（G1 vs G2 vs G3）未发现显著差异——生物标志物区分恶性 vs 正常组织，但不能区分恶性程度——这限制了分级应用"
  title_gap: "标题说 FMC 磷酸化蛋白质组学分析提供分级和治疗靶点洞察，但真正发现是分级局限性：现有分级系统可能不能反映磷酸化蛋白差异——需要替代分子分级策略——ABCC3/ACPP/PPP1CA/PRKAG3/RNASEL 是治疗靶点候选"
  evidence_boundary: "探索性磷酸化蛋白质组学证据（n=31）；支持生物标志物发现假设生成，不支持诊断应用或预后预测——需要独立验证"
---

# Phosphoproteomic profiling of feline mammary carcinoma: Insights into tumor grading and potential therapeutic targets

## Deep Extraction, 2026-06-05

[Deep extraction worksheet](../../system/indexes/src-cancer-093-deep-extraction-round1.md)

Safe promoted role:

- phosphoproteomic biomarker identification in FMC
- PRKAG3-Ki-67 prognostic association (p=0.03)
- molecular subtype distribution (luminal B, HER2+, triple-negative)
- therapeutic target candidates (ABCC3, ACPP, PPP1CA, PRKAG3, RNASEL)

Do not use this source as:

- clinical diagnostic protocol (small sample, n=31)
- treatment selection guidance
- prognosis prediction (no follow-up data)
- tumor grade discrimination (no inter-grade differences found)

## Source Check, 2026-06-03

| Field | Value |
|-------|-------|
| PMID | 40839607 |
| DOI | 10.1371/journal.pone.0330520 |
| Journal | PLoS One |
| Year | 2025 |
| Authors | Aruvornlop P, Ploypetch S, Sakcamduang W, et al. |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Study type | Phosphoproteomic profiling |
| Focus | FMC grading and therapeutic targets |
| Key context | FMC is most prevalent reproductive tumor in queens |
| Prognosis | Aggressive metastatic progression, short survival |

**Boundary:** Abstract-level extraction. Phosphoproteomic findings may inform FMC molecular grading.

## One-Line Summary

Phosphoproteomic profiling of FMC identifies grading-associated proteins and potential therapeutic targets for aggressive metastatic disease.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- FMC is most prevalent reproductive tumor in queens
- Characterized by aggressive metastatic progression and short survival
- Protein phosphorylation dysregulation linked to cancer progression (as in human breast cancer)
- Phosphoproteomic profiling used to identify grading biomarkers

### source_supported_conclusion

- Phosphoproteomic analysis identifies tumor grading-associated proteins
- Potential therapeutic targets identified through protein analysis
- Molecular basis for FMC aggressiveness explored

### llm_inference

- May inform mammary-carcinoma.md molecular grading section
- Novel biomarker candidates for FMC prognosis
- Supports translational approach linking human breast cancer pathways to FMC

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

## Study Details

### Sample Composition

- 31 FMC samples total: Grade 1 (n=6), Grade 2 (n=11), Grade 3 (n=14)
- 6 normal mammary tissue controls
- 11,942 total phosphoproteins analyzed
- 17 significantly downregulated phosphoproteins identified

### Molecular Subtypes (Human Breast Cancer Framework)

| Subtype | Percentage |
|---------|------------|
| Luminal B/HER2-negative | 35.5% |
| Triple-negative basal-like | 19.4% |
| Luminal B/HER2-positive | 16.1% |
| Triple-negative normal-like | 16.1% |
| HER2-positive | 12.9% |

Note: High proportion of triple-negative subtypes (35.5% combined) - known to be aggressive with limited treatment options.

### Therapeutically Relevant Phosphoproteins

| Protein | Role | Clinical Relevance |
|---------|------|-------------------|
| ABCC3 | Multidrug resistance | Chemotherapy response prediction |
| ACPP | Tumor suppressor | Diagnostic biomarker candidate |
| PPP1CA | Growth promoter | Therapeutic target candidate |
| PRKAG3 | Ki-67 association (p=0.03) | Prognostic marker |
| RNASEL | Tumor suppressor | Diagnostic biomarker candidate |

### Key Limitation

No significant differences among tumor grades themselves - biomarkers distinguish malignant from normal tissue but do not discriminate between grade 1, 2, and 3.

## Image Assets

No figures captured. Phosphoproteomic data supports research prioritization but requires independent validation before clinical application.

## Linked Entities

- diseases: cancer (feline mammary carcinoma)
- models: phosphoproteomic profiling, Mills grading
- endpoints: phosphoprotein expression, Ki-67, molecular subtype
- mechanisms: phosphorylation, multidrug resistance, tumor suppression
- regulations: none applicable
