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
  local_assets: ["../../raw/deep-extractions/ext-src-diabetes-025.md"]
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

## Why This Paper Matters

**Core contribution:** This paper advances feline diabetes from "obesity-related, similar to human T2DM" clinical consensus to a molecular signaling defect map across pancreas, skeletal muscle, and liver.

**For model researchers:**
- Provides tissue-level molecular readouts beyond blood glucose and insulin levels
- Demonstrates that insulin resistance has a concrete molecular basis (GLUT-4, PI3K, IRS pathway deficits), not just clinical speculation
- Shows ectopic lipid deposition correlates with signaling defects — glucose metabolism must be understood alongside lipid metabolism

**For drug evaluation:**
- The paper suggests GLP-1/GIP therapy evaluation should measure receptor downstream signaling, not just plasma incretin concentrations
- Evaluation matrices should include: pancreatic incretin/insulin signaling + muscle GLUT-4/PI3K + hepatic lipid/ACC/HSL status
- Study design must stratify by treatment status: obese non-diabetic, untreated diabetic, and treated diabetic cats show different molecular profiles

**Critical reading note:** This is cross-sectional tissue mechanism research — it cannot prove causation. Treated diabetic cats showing some elevated signals may represent compensation, not therapeutic recovery.

## Key Findings

### quoted_fact

- 54 client-owned cats: lean (n=15), overweight (n=15), diabetic (n=24).
- Diabetic cats showed increased liver and muscle adiposity (ectopic lipid deposition).
- Insulin mRNA abundance decreased in pancreas of both untreated and treated diabetic cats.
- GLUT-4 protein abundance decreased in muscle of diabetic cats.
- Untreated diabetic cats showed decreased insulin receptor mRNA in muscle.

### source_supported_conclusion

- Feline diabetes involves deficits at both pancreatic secretion (insulin synthesis) and peripheral response (muscle/liver insulin signaling).
- Ectopic lipid deposition in liver and muscle is associated with feline diabetes.
- The molecular defects parallel human T2DM but with species-specific incretin response differences.

### llm_inference

- GLUT-4 and PI3K may be therapeutic targets for improving insulin sensitivity in cats.
- Incretin receptor downstream signaling dysfunction may limit GLP-1 agonist efficacy in cats.
- Low-carbohydrate diet + insulin + weight management may work by controlling glucotoxicity and reducing ectopic fat deposition.

## Evidence Boundary

- Cross-sectional design cannot establish causation between signaling defects and clinical diabetes.
- Sample size is modest (n=24 diabetic), with treated group only n=8 using different insulin products (Lantus, ProZinc, Caninsulin).
- Diet information not consistently reported — important limitation for feline diabetes research.
- mRNA/protein abundance ≠ functional activity; no direct glucose uptake or dynamic insulin secretion measurements.

## Linked Entities

- diseases: diabetes mellitus, insulin resistance, obesity
- models: tissue mRNA/protein expression analysis
- endpoints: insulin mRNA, GLUT-4 protein, PI3K-p85α, insulin receptor, IRS-1, IRS-2, GLP-1R, GIP-R, ACC, HSL, liver/muscle fat percentage
- mechanisms: insulin signaling pathway, incretin signaling, ectopic lipid deposition, glucotoxicity
- regulations:
