---
id: src-diabetes-120
type: source
title: "Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues"
source_kind: paper
species: feline
diseases: [diabetes, obesity]
models: []
endpoints: [insulin-signaling, incretin-signaling, GLUT, Akt-phosphorylation]
jurisdictions: [Canada]
evidence_level: original-study
year: 2024
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
pmid: "39684905"
doi: "10.3390/ijms252313195"
tags: [diabetes, insulin-signaling, insulin-receptor, IRS-1, IRS-2, GLUT-4, PI3K, Akt, incretin, GLP-1, GIP, ectopic-lipid, liver, muscle, pancreas]
links:
  doi: "10.3390/ijms252313195"
  url: "https://doi.org/10.3390/ijms252313195"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Diabetic cats had decreased transcript abundances of insulin, insulin receptor, insulin-receptor substrate (IRS)-1, glucose transporters (GLUT), and protein abundance of mitogen-activated protein kinase."
    - "Diabetic cats had reduced mRNA abundances of insulin receptor, IRS-1/2, and phosphatidylinositol-3-kinase, and reduced protein abundances of GLUT-4."
    - "Feline diabetes is associated with ectopic lipid deposition in the liver and skeletal muscle, deficits in insulin synthesis and incretin signaling in the pancreas, and impaired insulin signaling in the muscle and liver."
  source_supported_conclusion:
    - "n=54 cats: lean (15), overweight (15), diabetic (24)."
    - "Tissues examined: pancreas, liver, skeletal muscle."
    - "Pancreatic deficits: ↓insulin, ↓insulin receptor, ↓IRS-1, ↓GLUT, ↓MAPK."
    - "Muscle/liver deficits: ↓insulin receptor, ↓IRS-1/2, ↓PI3K, ↓GLUT-4."
    - "Treated diabetics show ↑GLP-1R, ↑GIP-R, ↑Akt, ↑GLUT-1 (compensation)."
    - "Ectopic lipid deposition in liver and muscle contributes to insulin resistance."
  llm_inference:
    - "Multi-tissue signaling defects explain insulin resistance pathophysiology."
    - "Incretin receptor upregulation in treated cats suggests therapeutic relevance."
    - "GLUT-4 reduction in muscle is key mechanism of peripheral insulin resistance."
---

# Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues

## Evidence-Depth Caveat

**Deep-extracted from PubMed abstract (PMID 39684905).** 2024 Int J Mol Sci: n=54 cats (lean/overweight/diabetic). Multi-tissue analysis (pancreas, liver, muscle) showing insulin and incretin signaling deficits, ectopic lipid deposition. Evidence level: original cross-sectional study.

## Source Check, 2026-06-17

PubMed abstract extracted.

- PMID: 39684905
- DOI: 10.3390/ijms252313195
- Journal: Int J Mol Sci (MDPI)
- Year: 2024
- Open access: yes

## Study Design

| Group | n | Description |
|-------|---|-------------|
| Lean | 15 | Non-diabetic, normal weight |
| Overweight | 15 | Non-diabetic, obese |
| Diabetic | 24 | Diabetic (treated/untreated) |
| **Total** | **54** | Client-owned cats |

**Tissues examined:** Pancreas, liver, skeletal muscle

**Markers:** mRNA and protein abundances of insulin and incretin signaling molecules

## Key Findings

### Pancreatic Deficits (Diabetic Cats)

| Marker | Change |
|--------|--------|
| Insulin mRNA | ↓ Decreased |
| Insulin receptor | ↓ Decreased |
| IRS-1 | ↓ Decreased |
| GLUT | ↓ Decreased |
| MAPK protein | ↓ Decreased |

### Muscle/Liver Deficits (Diabetic Cats)

| Marker | Change |
|--------|--------|
| Insulin receptor mRNA | ↓ Decreased |
| IRS-1/IRS-2 mRNA | ↓ Decreased |
| PI3K mRNA | ↓ Decreased |
| **GLUT-4 protein** | ↓ Decreased |

### Treatment Effects (Treated Diabetics)

| Marker | Change |
|--------|--------|
| GLP-1 receptor | ↑ Increased |
| GIP receptor | ↑ Increased |
| Total/phospho-Akt | ↑ Increased |
| GLUT-1 | ↑ Increased |

## Key Conclusions

**Quoted:** "Feline diabetes is associated with ectopic lipid deposition in the liver and skeletal muscle, deficits in insulin synthesis and incretin signaling in the pancreas, and impaired insulin signaling in the muscle and liver."

## One-Line Summary

2024 study (n=54): feline diabetes shows multi-tissue signaling deficits (↓insulin receptor, ↓IRS-1/2, ↓GLUT-4), ectopic lipid deposition, and impaired incretin signaling; treated cats show compensatory receptor upregulation.

## Claim-Fit Judgment

**Strongest safe use:**
- Insulin signaling pathway deficits in feline diabetes
- Multi-tissue insulin resistance mechanism
- Ectopic lipid deposition role
- Incretin signaling involvement

**May control:**
- diabetes/mechanism-overview.md insulin resistance section
- Molecular basis of feline T2DM

**Should use with caveats:**
- Cross-sectional (causation not established)
- Client-owned cats (selection bias possible)

**Must not control:**
- Treatment recommendations
- Biomarker-based diagnosis

## Deep Extraction Metadata

- **Extraction date:** 2026-06-17
- **Source:** PubMed abstract (PMID 39684905)
- **Full text verified:** Abstract-level
- **Citations in vault topic pages:** 5 (branch-controlling)

## Linked Entities

- diseases: diabetes, insulin resistance
- tissues: pancreas, liver, skeletal muscle
- signaling: insulin receptor, IRS-1, IRS-2, PI3K, Akt, MAPK
- transporters: GLUT-1, GLUT-4
- incretins: GLP-1, GIP
- pathology: ectopic lipid deposition
