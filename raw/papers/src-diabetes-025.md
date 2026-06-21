---
id: src-diabetes-025
type: source
title: "Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues"
source_kind: paper
species: feline
diseases: [diabetes mellitus]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2024
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
pmid: "39684832"
pmcid: "PMC11642086"
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, insulin-signaling, insulin-resistance, incretin, GLP-1, GIP, GLUT, IRS, PI3K, ectopic-lipid, pancreas, liver, muscle]
links:
  doi: "10.3390/ijms252313195"
  url: "https://doi.org/10.3390/ijms252313195"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "54 client-owned cats: lean (n=15), overweight (n=15), diabetic (n=24)."
    - "Diabetic cats showed increased liver and muscle adiposity (ectopic lipid deposition)."
    - "Insulin mRNA abundance decreased in pancreas of both untreated and treated diabetic cats."
    - "GLUT-1 and GLUT-2 mRNA levels decreased in pancreas of both diabetic groups."
    - "Insulin receptor mRNA abundance decreased in muscle of untreated diabetic cats."
    - "PI3K-p85α protein abundance tended to decrease in muscle of diabetic cats."
    - "GLUT-4 protein abundance decreased in muscle of diabetic cats."
  source_supported_conclusion:
    - "Feline diabetes is associated with ectopic lipid deposition in liver and skeletal muscle."
    - "Deficits in insulin synthesis and incretin signaling in pancreas contribute to feline diabetes."
    - "Peripheral insulin resistance in muscle involves reduced GLUT-4 and PI3K signaling."
    - "Feline diabetes parallels human T2DM in molecular mechanisms."
  llm_inference:
    - "GLUT-4 and PI3K may be therapeutic targets for improving insulin sensitivity in cats."
    - "Incretin-based therapies (GLP-1 agonists) may have relevance for feline diabetes."
  # V2 enhanced fields
  study_design: "观察性队列研究，纳入54只客户拥有的家猫，分为瘦猫、超重猫和糖尿病猫，采用组织mRNA和蛋白质表达分析"
  core_argument: "猫糖尿病与外周组织中胰岛素信号标志物的缺失密切相关，表现为胰腺胰岛素合成减少及肝肌组织异位脂质沉积"
  implicit_premise: "外周组织中胰岛素信号标志物的mRNA及蛋白表达水平变化直接反映糖尿病病理生理机制"
  title_gap: "标题强调猫糖尿病与胰岛素信号标志物缺失有关，但真正发现是这种缺失伴随肝脏和骨骼肌的异位脂质沉积，对糖尿病的发生机制具有重要影响"
  evidence_boundary: "未探讨糖尿病治疗的临床疗效及干预策略，因研究为观察性质，无法建立因果关系"
  unexpected_finding: "未治疗糖尿病猫的肌肉胰岛素受体mRNA显著降低，而治疗组则未表现出同样明显的受体mRNA减少"
---

# Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues

## Evidence-Depth Caveat

**Deep-extracted from PMC full text (PMC11642086).** 2024 IJMS: 54 cats (lean/overweight/diabetic); first comprehensive characterization of insulin and incretin signaling deficits in feline diabetes at molecular level. Shows ectopic lipid deposition, reduced GLUT-4 and PI3K in muscle, decreased insulin/incretin signaling in pancreas. Evidence level: original study with RT-qPCR and Western blot.

## Source Check, 2026-06-09

Europe PMC full text extraction.

| Field | Value |
|-------|-------|
| PMID | 39684832 |
| PMCID | PMC11642086 |
| DOI | 10.3390/ijms252313195 |
| Journal | Int J Mol Sci (MDPI) |
| Year | 2024 |
| Authors | Malatesta D, Fowler I, Aldrich M, et al. |
| Open access | yes |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Study size | 54 cats: 15 lean, 15 overweight, 24 diabetic |
| Key tissues | Pancreas, liver, skeletal muscle |
| Ectopic lipid | Increased liver fat (untreated DM), muscle fat (overweight + treated DM) |
| Pancreas findings | Decreased insulin mRNA, GLUT-1/2 mRNA in both diabetic groups |
| Muscle findings | Decreased insulin receptor mRNA, PI3K-p85α protein, GLUT-4 protein |
| Incretin signaling | Deficits in GLP-1R and GIP-R in untreated diabetics |
| Human parallel | Similar to human T2DM mechanisms |

**Boundary:** This is an observational study. Treatment implications are inferences, not clinical recommendations.

## One-Line Summary

Candidate diabetes source from sheet row 27. Use it for triage until abstract or full-text extraction proves a stronger role.

## Why It Matters For Feline Diabetes

This source was included in the 2026-05-13 feline diabetes / obesity intake sheet and classified as `new-diabetes` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues.
- The intake sheet locator is: 10.3390/ijms252313195.

### source_supported_conclusion

- This is a first-pass source-card placeholder for triage and queue control.
- It should not support prevalence, diagnostic, treatment, management, or risk-ranking claims yet.

### llm_inference

- The title suggests a possible `diabetes` role, but the actual claim-fit requires abstract or full-text review.

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
- Which claims, if any, are reusable for the diabetes module?
- Does this source deserve deep extraction, or should it remain queue context?
- Are there tables or figures that change the module structure?

## Linked Entities

- diseases: diabetes mellitus
- models:
- endpoints:
- mechanisms:
- regulations:
