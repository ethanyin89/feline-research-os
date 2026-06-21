---
id: src-cancer-038
type: source
title: "Establishment and characterization of a new feline mammary cancer cell line, FkMTp"
source_kind: paper
species: feline
diseases: ['cancer']
models: ['clinical-study']
endpoints: ['remission']
evidence_level: original-study
year: 2016
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: yes
language_qa_status: bilingual_checked
tags: ['cancer', 'establishment', 'characterization', 'new', 'mammary', 'cell', 'line', 'fkmtp']
links:
  doi: "10.1007/s10616-015-9912-7"
  url: "https://doi.org/10.1007/s10616-015-9912-7"
  local_assets: []
abstract: "The study established and characterized a new feline mammary cancer cell line, FkMTp, derived from a cat mammary carcinoma. The cell line was characterized across passages up to the 160th, showing increased tumorigenic features like anchorage-independent growth, enhanced migration and invasion, and altered ploidy. Cryopreservation at ~every six passages allowed access to tumor progression stages. This model provides a promising tool for studying tumor microevolution and carcinogenesis in feline mammary cancer, paralleling human breast cancer characteristics."
methods_summary: "Tumor tissue from a feline mammary carcinoma was cultured to establish the FkMTp cell line. The cell line was characterized through assays including growth behavior evaluation, morphological differentiation assessment, anchorage-independent growth in soft agar, wound-healing assays for invasion and migration capability. These analyses were performed longitudinally from primary culture up to the 160th passage. Karyotyping assessed ploidy variations. Cryopreservation batches were maintained approximately every six passages for retrospective analysis."
evidence_policy:
  quoted_fact:
    - "FkMTp cell line characterized from primary cultures to the 160th passage."
    - "Demonstrated increased anchorage independence, migration, and invasion over time."
    - "Ploidy changes observed through passages indicating genomic instability."
    - "Cryopreserved samples available approximately every six passages."
  source_supported_conclusion:
    - "FkMTp cell line exhibits in vitro tumorigenicity evidenced by anchorage-independent growth and invasive capabilities."
    - "Model holds value for studying mechanisms of carcinogenesis and tumor progression in feline mammary cancer."
  llm_inference:
    - "FkMTp can facilitate comparative oncology research relevant to human breast cancer due to shared pathological features."
    - "Longitudinal sampling enables study of tumor evolution, potentially informing therapeutic target identification."
  # V2 enhanced fields
  study_design: "体外细胞系建立与表征研究，从猫乳腺癌原发肿瘤建立 FkMTp 细胞系，表征至第 160 代"
  core_argument: "FkMTp 细胞系在传代过程中表现出渐进性肿瘤特征增强（锚定非依赖性生长、迁移/侵袭能力、倍性变化）——每 6 代冷冻保存允许回顾性分析肿瘤进化阶段"
  implicit_premise: "假设体外传代的肿瘤特征变化反映体内肿瘤进化；假设细胞系模型可代表原发肿瘤生物学"
  unexpected_finding: "渐进性基因组不稳定（倍性变化）伴随传代——这不仅是细胞系'人工制品'，而是模拟了真实肿瘤的微进化过程"
  title_gap: "标题说建立和表征新猫乳腺癌细胞系，但真正发现是时间机器：每 6 代冷冻保存创造了肿瘤进化的'时间快照'——可以回溯研究肿瘤从早期到晚期的分子变化"
  evidence_boundary: "单一细胞系可能不代表 FMC 异质性；体外进化与体内进化的相关性需进一步验证"
---

# Establishment and characterization of a new feline mammary cancer cell line, FkMTp

## Evidence-Depth Caveat

This card is based on the full publication text, including experimental data and methods. It is deep-extracted as a clinical/preclinical study of a cancer model.

## One-Line Summary

A novel feline mammary cancer cell line (FkMTp) was established from a primary cat tumor and characterized through 160 passages, demonstrating increased tumorigenic characteristics such as anchorage-independent growth and enhanced migration/invasion, with periodic cryopreservation enabling tumor progression staging.

## Why It Matters For Feline ['cancer']

Feline mammary carcinomas share crucial biological and histological traits with human breast cancers, making FkMTp a highly relevant in vitro model to study tumor biology, progression, and potential therapeutic targets in both feline and comparative oncology contexts.

## Key Findings

### quoted_fact

* The FkMTp cell line was derived from a feline mammary carcinoma and successfully cultured up to at least the 160th passage.
* Anchorage-independent growth assessed via soft agar assay increased progressively from primary culture through later passages.
* Wound-healing assays demonstrated a time-dependent increase in migration and invasion capacities.
* Cytogenetic analysis revealed varying ploidy levels across passages, indicating genomic instability during immortalization.
* Cryopreservation was performed roughly every six passages, including at the primary culture stage, allowing retrospective analyses of tumor evolution stages.

### source_supported_conclusion

* The FkMTp cell line exhibits validated in vitro tumorigenicity demonstrated by enhanced anchorage independence, migration, and invasion capabilities correlated with passage number.
* Progressive alteration in ploidy suggests ongoing genomic changes during cell line establishment, reflecting tumor microevolution.
* The model provides a valuable tool for investigating carcinogenesis mechanisms in feline mammary tumors, with translational relevance to human breast cancer research.

### llm_inference

* Utilization of FkMTp can deepen understanding of tumor progression and drug resistance mechanisms by accessing distinct frozen passage stages.
* The model may inform development of novel therapeutic strategies targeting invasive and metastatic behaviors shared between feline and human mammary cancers.
* Future research could leverage this cell line for high-throughput screening of anti-cancer agents, considering its maintained tumorigenic phenotype.

## Study Design Details

### Cohort Summary

| Cohort/Stage           | Description                                      | Outcomes/Parameters Measured                         |
|-----------------------|------------------------------------------------|----------------------------------------------------|
| Primary tumor culture  | Cells established from feline mammary carcinoma | Baseline morphology, initial growth characteristics |
| Early passages (~P1-P6) | Cultured cells with cryopreservation cycles     | Anchorage-independent growth, migration, invasion   |
| Mid-late passages (up to P160) | Long-term cultured/immortalized cells         | Progressive increase in tumorigenic behaviors, ploidy shifts |
| Cryopreserved samples  | Periodic storage every ~6 passages               | Enable retrospective temporal analyses              |

## Linked Entities

- diseases: ['cancer']
- models: ['clinical-study']
- endpoints: ['remission']
- mechanisms: ['tumor microevolution', 'carcinogenesis', 'cell migration', 'anchorage independence', 'genomic instability']