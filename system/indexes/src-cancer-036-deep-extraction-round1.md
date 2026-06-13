---
id: src-cancer-036-deep-extraction-round1
type: system
source_id: src-cancer-036
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-036

**Source:** Gene expression association study in feline mammary carcinomas
**Journal:** PLOS ONE (2019, Open Access CC-BY)
**DOI:** 10.1371/journal.pone.0221776
**PMID:** 31461477
**Evidence Level:** original-study

## Phase 0: Context

**Access status:** Open access (PLOS ONE). Full abstract available.

**Source scope:** 2019 study evaluating expression of 7 cancer-related genes in FMC vs disease-free tissue.

**Key contribution:** Identifies overexpressed genes (CCND1, PTBP1, PKM2) and clinical associations (oral contraceptives, tumor size, metastasis).

## Phase 1: Sequential Micro-Analysis

### 1.1 Genes Evaluated

| Gene | Full Name | Function |
|------|-----------|----------|
| TP53 | Tumor protein p53 | Tumor suppressor |
| CCND1 | Cyclin D1 | Cell cycle regulator |
| FUS | Fused in sarcoma | RNA-binding protein |
| YBX1 | Y-box binding protein 1 | Transcription factor |
| PTBP1 | Polypyrimidine tract binding protein 1 | RNA splicing |
| c-MYC | Cellular MYC | Oncogene |
| PKM2 | Pyruvate kinase M2 | Metabolic enzyme |

### 1.2 Expression Findings

| Gene | FMC vs Normal |
|------|---------------|
| CCND1 | **Overexpressed** |
| PTBP1 | **Overexpressed** |
| PKM2 | **Overexpressed** |
| TP53 | Normal |
| c-MYC | Normal |
| YBX1 | Normal |
| FUS | Normal |

**Key finding:** Three genes are consistently overexpressed in FMC: CCND1 (cell cycle), PTBP1 (RNA splicing), PKM2 (metabolism).

### 1.3 Clinical Associations

| Clinical Factor | Associated Gene(s) |
|-----------------|---------------------|
| Oral contraceptive use | TP53, YBX1, CCND1, FUS, PTBP1 |
| Tumor size | YBX1 |
| Lymph node metastasis | c-MYC |

**Oral contraceptive finding:** Multiple gene associations with oral contraceptive use supports hormonal influence on FMC molecular biology, even in ER-negative tumors.

### 1.4 Gene Correlations

| Pattern | Observation |
|---------|-------------|
| Most genes | Strong correlations with each other |
| Exceptions | c-MYC and PKM2 not correlated |

**Implication:** FMC involves coordinated dysregulation of multiple oncogenic pathways, not single-gene effects.

## Phase 2: Theme Reconstruction

### Theme A: Metabolic Reprogramming (PKM2)

PKM2 overexpression suggests Warburg effect:
- Tumor cells prefer glycolysis over oxidative phosphorylation
- PKM2 is rate-limiting for this metabolic shift
- May be therapeutic target

### Theme B: Cell Cycle Dysregulation (CCND1)

CCND1 overexpression indicates:
- Cyclin D1 drives G1/S transition
- Loss of cell cycle control
- May predict response to CDK4/6 inhibitors (palbociclib, etc.)

### Theme C: Oral Contraceptive Link

The association of oral contraceptive use with multiple gene expression levels:
- Supports hormonal etiology even in ER-negative tumors
- May reflect epigenetic or indirect mechanisms
- Reinforces spaying recommendation before first estrus

### Theme D: Metastasis Biomarker (c-MYC)

c-MYC association with lymph node metastasis suggests:
- c-MYC may be prognostic marker
- c-MYC drives metastatic phenotype
- Potential therapeutic target

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC37 | CCND1, PTBP1, PKM2 are overexpressed in FMC | A | gene expression study |
| MC38 | Oral contraceptive use associated with TP53, YBX1, CCND1, FUS, PTBP1 expression | A | clinical association |
| MC39 | c-MYC RNA levels associated with lymph node metastasis | A | prognostic association |
| MC40 | FMC involves coordinated dysregulation of multiple genes | B | network interpretation |

**Section to update:** Molecular Biology / Risk Factors

**Boundary rules:**
- Gene expression associations, not causal claims
- Research biomarkers, not clinical diagnostics
- Oral contraceptive finding strengthens hormonal risk factor narrative

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] CCND1 overexpressed in FMC
- [x] PTBP1 overexpressed in FMC
- [x] PKM2 overexpressed in FMC
- [x] Oral contraceptive use associated with gene expression levels
- [x] c-MYC associated with lymph node metastasis
- [x] Tumor size associated with YBX1 levels

### not_safe_to_promote_yet

- [ ] Gene expression as clinical diagnostic
- [ ] Therapeutic targeting of these genes
- [ ] Prognosis based on gene expression
- [ ] Oral contraceptive causation (association only)

### open_questions

1. Are CCND1/PKM2/PTBP1 prognostically significant?
2. Can CDK4/6 inhibitors target CCND1-overexpressing FMC?
3. Is metabolic targeting (PKM2 inhibition) feasible?
4. How do oral contraceptives affect gene expression mechanistically?
5. Can c-MYC predict metastatic risk clinically?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 molecular/association claims |
| Evidence level | original-study (2019, PLOS ONE) |
| Key contribution | Overexpressed genes + oral contraceptive associations |
| Primary gap | Clinical utility of gene expression findings |
| Topic page targets | mammary-carcinoma.md (molecular biology, risk factors) |
| Comparative oncology | CCND1/c-MYC relevant to human breast cancer research |
