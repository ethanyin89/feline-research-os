---
id: src-ckd-027
type: source
title: "Metabolomics reveals alterations in gut-derived uremic toxins and tryptophan metabolism in feline chronic kidney disease"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2025
status: extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, metabolomics, reveals, alterations, gut-derived, uremic, toxins, tryptophan]
links:
  doi: "10.1080/01652176.2024.2447601"
  url: "https://doi.org/10.1080/01652176.2024.2447601"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The full PMC article compares serum and urine metabolomes from 94 cats with CKD and 84 healthy senior cats."
    - "The CKD cohort included 59 stage 2, 29 stage 3, and 6 stage 4 cats; untargeted analysis retained 183 CKD-associated compounds."
    - "The authors report increased indoxyl sulfate, p-cresyl sulfate, and TMAO and explicitly note that absolute quantification was not performed."
  source_supported_conclusion:
    - "The source supports a feline CKD metabolomics branch centered on tryptophan, tyrosine, urea-cycle, carnitine, and gut-derived uremic-toxin changes."
    - "The findings are discovery-grade associations and do not provide diagnostic thresholds or treatment recommendations."
  llm_inference:
    - "Impaired renal excretion is the leading explanation for toxin accumulation, while altered gut production or dietary precursor effects remain plausible but unproven contributors."
  # V2 enhanced fields
  study_design: "观察性代谢组学研究，94 只 CKD 猫（59 只 2 期、29 只 3 期、6 只 4 期）vs 84 只健康老年猫，非靶向血清和尿液代谢组分析"
  core_argument: "猫 CKD 存在广泛的色氨酸、酪氨酸、肉碱、尿素循环和肠源性尿毒症毒素代谢紊乱——吲哚酚硫酸盐、对甲酚硫酸盐和 TMAO 升高与疾病状态相关"
  implicit_premise: "假设非靶向代谢组学关联反映病理生理学而非混杂因素；假设肾脏排泄受损是毒素蓄积的主要解释"
  unexpected_finding: "色氨酸与分解代谢物比值在 2 期即发生逆转——提示代谢紊乱早于晚期 CKD"
  title_gap: "标题说肠源性尿毒症毒素和色氨酸代谢，但真正发现是早期紊乱：色氨酸/分解代谢物比值在 2 期即逆转——代谢组学可能检测比传统标志物更早的变化"
  evidence_boundary: "发现级关联，无绝对定量；不能提供诊断阈值或治疗建议；不能证明饮食或微生物组干预的因果效应"
---

# Metabolomics reveals alterations in gut-derived uremic toxins and tryptophan metabolism in feline chronic kidney disease

## Evidence-Depth Caveat

This card is based on complete PMC article text. It is deep-extracted for mechanism and research-target mapping, but remains non-decision-grade for diagnosis or treatment.

## Source Check, 2026-06-06

Crossref + PubMed abstract was checked as a repeatable second-pass intake step.

- Metadata resolved: yes
- Metadata provider: Crossref + PubMed abstract
- Container: Veterinary Quarterly
- Year: 2025
- Abstract available: yes

Use boundary:

- This source check was superseded by complete PMC review on 2026-06-06.
- Reuse must follow `system/indexes/src-ckd-027-deep-extraction-round1.md`.

Abstract lead for scope check only: Chronic Kidney Disease (CKD) is one of the most common conditions affecting felines, yet the metabolic alterations underlying its pathophysiology remain poorly understood, hinderi...

## Deep Extraction, 2026-06-06

- Access: complete PMC article, PMCID `PMC11703532`.
- Worksheet: `system/indexes/src-ckd-027-deep-extraction-round1.md`.
- Promotion boundary: mechanism and research-target mapping only; no diagnostic thresholds or treatment advice.

## One-Line Summary

Large observational serum-and-urine metabolomics study mapping tryptophan, tyrosine, carnitine, urea-cycle, and gut-derived uremic-toxin changes across feline CKD.

## Why It Matters For Feline CKD

This source adds a modern pathway-level mechanism map beyond conventional renal-function markers. It is most useful for prioritizing biomarker and uremic-toxin research, not for setting clinical thresholds.

## Key Findings

### quoted_fact

- Study groups: 94 CKD cats and 84 healthy senior controls.
- CKD stages: 59 stage 2, 29 stage 3, and 6 stage 4.
- Untargeted processing generated 7220 compounds and retained 183 CKD-associated compounds.
- A restricted validation comparison included 31 CKD and 34 healthy cats.

### source_supported_conclusion

- CKD was associated with broad disruption of tryptophan, tyrosine, carnitine, and urea-cycle metabolism.
- Circulating indoxyl sulfate, p-cresyl sulfate, and TMAO were higher in CKD.
- Lower tryptophan and higher catabolite abundance tracked disease-state and progression signals.
- The lack of absolute quantification blocks assay thresholds and direct clinical translation.

### llm_inference

- Renal retention is likely central, while diet- and microbiome-mediated production remains an unresolved causal branch.

## Claim-Fit Judgment

Strongest safe use:

- metabolomics branch architecture
- uremic-toxin research prioritization
- hypothesis generation for prospective biomarker or intervention studies

Must not control:

- diagnostic thresholds
- treatment selection
- protein-restriction or microbiome-product recommendations
- causal claims about diet, toxin production, or CKD progression

## Detailed Pathway Findings

### Tryptophan Metabolism

- Serum and urinary tryptophan were lower in CKD cats
- Tryptophan-to-catabolite ratio reversed at stage 2 onset
- Pathway disruption strengthened with CKD progression
- Indole, kynurenine, and serotonin pathway catabolites increased

### Gut-Derived Uremic Toxins

- Indoxyl sulfate, p-cresyl sulfate, and TMAO elevated in CKD
- Impaired renal excretion is the leading explanation
- Altered gut production from dietary precursors remains unproven
- No intervention study validates toxin-lowering benefit in cats

### Validation Analysis

- Restricted comparison: 31 CKD cats, 34 healthy controls
- Excluded medications: telmisartan, benazepril, amlodipine, mirtazapine, phosphate binders, lactulose
- Excluded renal diets to reduce confounding
- Residual age and disease burden differences may still affect results

## Image Assets

No figures captured. Tables and pathway diagrams are discovery-level and do not warrant reader-facing promotion without additional validation studies.

## Linked Entities

- diseases: CKD
- models: observational metabolomics cohort
- endpoints: serum metabolites, urinary metabolites, IRIS staging
- mechanisms: tryptophan metabolism, tyrosine metabolism, urea cycle, gut-derived uremic toxins (indoxyl sulfate, p-cresyl sulfate, TMAO)
- regulations: none applicable
