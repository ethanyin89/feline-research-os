---
id: src-cancer-031
type: source
title: "Feline SCCs of the Head and Neck Display Partial Epithelial-Mesenchymal Transition and Harbor Stem Cell-like Cancer Cells"
source_kind: paper
species: feline
diseases: [cancer]
models: [human-HNSCC]
endpoints: [EMT-markers, cancer-stem-cells, tumor-invasion]
jurisdictions: [Austria]
evidence_level: original-study
year: 2023
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
pmid: 38003753
doi: "10.3390/pathogens12111288"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, FOSCC, HNSCC, EMT, partial-EMT, cancer-stem-cells, CD44, CD271, E-cadherin, vimentin, comparative-oncology, feline-papillomavirus]
links:
  doi: "10.3390/pathogens12111288"
  url: "https://www.mdpi.com/2076-0817/12/11/1288"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "All tumors except one corresponded to high-grade, invasive lesions and concurrently expressed epithelial (keratins, E-cadherin, β-catenin) and mesenchymal (vimentin, N-cadherin, CD146) proteins."
    - "CD44/CD271 double-positive cells were concentrated at invasive tumor margins."
    - "Feline tumors closely mirror human counterparts regarding cellular plasticity mechanisms."
  source_supported_conclusion:
    - "13/14 feline HNSCC tumors display partial EMT (pEMT), not complete EMT."
    - "pEMT is characterized by co-expression of epithelial markers (keratins, E-cadherin, β-catenin) and mesenchymal markers (vimentin, N-cadherin, CD146)."
    - "CD44+/CD271+ double-positive cells at invasive margins represent putative cancer stem cells."
    - "Feline HNSCC validates as a comparative oncology model for human HNSCC based on shared EMT/CSC biology."
  llm_inference:
    - "Targeting CD44/CD271+ cancer stem cells could be a therapeutic strategy for FOSCC."
    - "pEMT phenotype may explain local invasion and recurrence in FOSCC."
    - "FPV status was evaluated but specific findings not detailed in abstract."
  # V2 enhanced fields
  study_design: "原始研究（2023 年 Pathogens），n=14 猫头颈部肿瘤，免疫组化和免疫荧光分析 EMT 和癌症干细胞标记物"
  core_argument: "13/14 猫 HNSCC 肿瘤显示部分 EMT（pEMT），同时表达上皮标记物（角蛋白、E-钙粘蛋白、β-连环蛋白）和间充质标记物（波形蛋白、N-钙粘蛋白、CD146）——CD44+/CD271+ 癌症干细胞集中在侵袭性边缘"
  implicit_premise: "假设 pEMT 表型与临床侵袭性相关；假设人类 HNSCC 的 CSC 标记物可直接应用于猫"
  unexpected_finding: "猫 HNSCC 显示部分 EMT 而非完全 EMT——同时表达上皮和间充质标记物——这种'混合'表型可能解释局部侵袭性和复发"
  title_gap: "标题说猫头颈部 SCC 显示部分 EMT 并携带干细胞样癌细胞，但真正发现是模型验证：猫肿瘤在细胞可塑性机制上密切反映人类——验证 FOSCC 作为人类 HNSCC 比较肿瘤学模型"
  evidence_boundary: "n=14 小样本；pEMT 的预后价值和 CD44/CD271 靶向治疗效果未在本研究中评估"
---

# Feline SCCs of the Head and Neck Display Partial Epithelial-Mesenchymal Transition and Harbor Stem Cell-like Cancer Cells

## Evidence-Depth Caveat

**Deep-extracted from PubMed abstract (PMID 38003753).** 2023 Pathogens study (n=14 tumors): 13/14 feline HNSCC tumors display partial EMT with co-expression of epithelial and mesenchymal markers; CD44+/CD271+ cancer stem cells at invasive margins. Validates FOSCC as human HNSCC model. Evidence level: original study.

## Source Check, 2026-06-17

PubMed abstract extracted for deep extraction.

- PMID: 38003753
- DOI: 10.3390/pathogens12111288
- Journal: Pathogens (MDPI)
- Year: 2023
- Authors: University of Veterinary Medicine Vienna, Karl Landsteiner University
- Open access: yes

## Study Design

| Feature | Value |
|---------|-------|
| Sample size | n=14 feline head and neck tumors |
| Tumor grade | 13/14 high-grade, invasive lesions |
| Methods | Immunohistochemistry, immunofluorescence |
| Markers tested | Epithelial (keratins, E-cadherin, β-catenin), mesenchymal (vimentin, N-cadherin, CD146), stem cell (CD44, CD271) |
| FPV status | Evaluated across varying infection statuses |

## Key Findings

### Partial EMT (pEMT)

| Marker Type | Markers | Expression |
|-------------|---------|------------|
| Epithelial | Keratins, E-cadherin, β-catenin | Concurrent |
| Mesenchymal | Vimentin, N-cadherin, CD146 | Concurrent |
| Phenotype | Partial EMT (pEMT) | 13/14 tumors |

**Quoted finding:** "All tumors except one corresponded to high-grade, invasive lesions and concurrently expressed epithelial (keratins, E-cadherin, β-catenin) and mesenchymal (vimentin, N-cadherin, CD146) proteins."

### Cancer Stem Cells

| Marker | Location | Significance |
|--------|----------|--------------|
| CD44+/CD271+ | Invasive tumor margins | Putative cancer stem cells |
| Distribution | Double-positive cells concentrated at invasive fronts | Suggests CSC-driven invasion |

**Quoted finding:** "CD44/CD271 double-positive cells were concentrated at invasive tumor margins."

### Comparative Oncology

**Quoted finding:** "Feline tumors closely mirror human counterparts regarding cellular plasticity mechanisms."

## One-Line Summary

Feline HNSCC (n=14) shows partial EMT (13/14 tumors) with CD44+/CD271+ cancer stem cells at invasive margins, validating FOSCC as a human HNSCC model.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Feline SCCs of the Head and Neck Display Partial Epithelial-Mesenchymal Transition and Harbor Stem Cell-like Cancer Cells.
- The intake sheet locator is: https://www.mdpi.com/2076-0817/12/11/1288.

### source_supported_conclusion

- This is a first-pass source-card placeholder for triage and queue control.
- It should not support prevalence, diagnostic, treatment, management, or risk-ranking claims yet.

### llm_inference

- The title suggests a possible `cancer` role, but the actual claim-fit requires abstract or full-text review.

## Claim-Fit Judgment

**Strongest safe use:**
- FOSCC molecular characterization (pEMT, CSC markers)
- Comparative oncology model validation for human HNSCC
- Cancer stem cell biology in feline oral SCC
- Invasive front characterization

**May control:**
- oral-squamous-cell-carcinoma.md EMT section
- Translational model molecular layer

**Should use with caveats:**
- CSC-targeted therapy implications (not tested)
- Prognostic value of CD44/CD271 (not evaluated)

**Must not control:**
- Treatment recommendations
- Survival predictions based on EMT status
- Clinical grading systems

## Deep Extraction Metadata

- **Extraction date:** 2026-06-17
- **Source:** PubMed abstract (PMID 38003753)
- **Full text verified:** Abstract-level (MDPI 403 blocked full text)
- **Citations in vault topic pages:** 5 (branch-controlling source)

## Linked Entities

- diseases: cancer, oral squamous cell carcinoma, FOSCC
- models: human HNSCC comparative model
- endpoints: EMT markers, cancer stem cell markers, tumor invasion
- mechanisms: partial EMT, CD44/CD271 cancer stem cells, E-cadherin, vimentin
- treatments: N/A (mechanistic study)
