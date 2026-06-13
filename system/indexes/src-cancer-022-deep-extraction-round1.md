---
id: src-cancer-022-deep-extraction-round1
type: system
source_id: src-cancer-022
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-022

**Source:** Triple-negative vimentin-positive heterogeneous feline mammary carcinomas as a potential comparative model for breast cancer
**Journal:** BMC Veterinary Research (2014, Open Access)
**DOI:** 10.1186/s12917-014-0185-8
**PMID:** 25249140
**Evidence Level:** original-study (large phenotyping cohort)

## Phase 0: Context

**Access status:** Open access. Full abstract available in source card.

**Source scope:** Large phenotyping study (156 feline mammary lesions) characterizing molecular subtypes using IHC and gene expression.

**Key contribution:** Establishes that majority of FMCs are triple-negative with vimentin positivity, resembling human basal-like/claudin-low TNBC.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Total lesions | 156 |
| Types included | FMCs, benign neoplasms, hyperplastic/dysplastic tissues |
| Methods | Histology + IHC |
| Gene expression subset | 37 FMCs with 27 matched non-neoplastic controls |
| Markers assessed (IHC) | basal CK, luminal CK, vimentin, α-SMA, calponin, ERα, PR |
| Markers assessed (gene) | ERα, ERβ, PR, HER2 |

### 1.2 Human Breast Cancer Classification Context

| Molecular Subtype | Receptor Status | Notes |
|-------------------|-----------------|-------|
| Luminal A | ER+/PR+, HER2- | good prognosis |
| Luminal B | ER+/PR+, HER2+ | intermediate |
| HER2-overexpressing | ER-/PR-, HER2+ | aggressive |
| Basal-like | ER-/PR-/HER2- (TNBC) | aggressive |
| Claudin-low | TNBC + stem-like features | aggressive |
| Normal-breast like | — | rare |

**Key insight:** Human TNBCs (basal-like + claudin-low) are the most heterogeneous and therapeutically challenging.

### 1.3 FMC Phenotype Findings

| Phenotype | Prevalence | Features |
|-----------|------------|----------|
| HR-negative aggressive | majority | vimentin+, CK14+, CK5/6+ |
| HR-positive aggressive | 10.8% | bilineage differentiation |
| HR-positive benign | 8% | bilineage differentiation |

**Key finding:** ~81% of FMCs are HR-negative (triple-negative), matching the human TNBC pattern.

### 1.4 Molecular Markers Detailed

| Marker | FMC Expression | Human TNBC | Implication |
|--------|----------------|------------|-------------|
| Vimentin | + in HR- tumors | + in basal-like/claudin-low | mesenchymal marker |
| CK14 | + | + | basal cytokeratin |
| CK5/6 | + | + | basal cytokeratin |
| ER | - (majority) | - | hormone receptor |
| PR | - (majority) | - | hormone receptor |
| HER2 | not overexpressed | not overexpressed | growth receptor |

### 1.5 Cell of Origin Hypothesis

| Finding | Interpretation |
|---------|----------------|
| CKs/vimentin co-expressing luminal cells | Potential progenitor for TNBC phenotype |
| Bilineage differentiation in HR+ tumors | Luminal + myoepithelial features suggest stem cell origin |

## Phase 2: Theme Reconstruction

### Theme A: FMC as TNBC Model

This study provides robust evidence for FMC as a naturally-occurring model for human TNBC:
1. **Phenotypic match:** vimentin+, CK14+, CK5/6+
2. **Receptor status match:** ER-/PR-/HER2- (triple-negative)
3. **Prevalence match:** majority are TNBC (vs minority HR+)
4. **Heterogeneity:** similar complexity to human TNBCs

This strengthens the comparative oncology case for using FMC to test TNBC therapies.

### Theme B: HR-Positive Minority

The 10.8% + 8% HR-positive subset is noteworthy:
- These cats might respond to hormone therapy
- Bilineage differentiation suggests different biology
- Important for personalized treatment approaches

### Theme C: Molecular Phenotyping for Clinical Use

The study demonstrates that molecular phenotyping is feasible in cats:
- IHC panel: vimentin, CKs, ER, PR
- Gene expression: ERα, ERβ, PR, HER2
- Could guide treatment selection (hormone therapy for HR+, targeted for HER2+)

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC22 | ~81% of FMCs are HR-negative (triple-negative) | A | 156 lesions, single study |
| MC23 | FMC TNBC phenotype: vimentin+, CK14+, CK5/6+ | A | IHC characterization |
| MC24 | Only 10.8% aggressive + 8% benign FMCs are HR+ | A | molecular prevalence |
| MC25 | FMC resembles human basal-like/claudin-low TNBC | B | comparative oncology |
| MC26 | Bilineage differentiation in HR+ tumors suggests stem cell origin | C | research direction |

**Section to update:** Molecular Subtypes / Comparative Oncology

**Boundary rules:**
- 156-lesion dataset provides good statistical power
- Single institution — generalization caution
- TNBC model validation for translational research

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] ~81% of FMCs are HR-negative (triple-negative)
- [x] FMC TNBC: vimentin+, CK14+, CK5/6+
- [x] 10.8% aggressive + 8% benign are HR+
- [x] FMC resembles human basal-like/claudin-low TNBC
- [x] Molecular phenotyping feasible with IHC + gene expression

### not_safe_to_promote_yet

- [ ] Treatment response prediction by phenotype
- [ ] Hormone therapy efficacy in HR+ cats
- [ ] Cell of origin confirmation (progenitor hypothesis)

### open_questions

1. Do HR+ FMCs respond to tamoxifen or other hormone therapies?
2. Is vimentin expression prognostic in FMC?
3. What is the claudin expression pattern in FMC?
4. Are there FMC cell lines representing each molecular subtype?
5. Can phenotype-directed therapy improve FMC outcomes?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 5 molecular phenotyping claims |
| Evidence level | original-study (156 lesions) |
| Key contribution | Largest FMC phenotyping study, confirms TNBC model |
| Primary gap | Treatment response by subtype |
| Topic page targets | mammary-carcinoma.md (molecular subtypes) |
| Comparative oncology value | High — quantifies TNBC prevalence |
