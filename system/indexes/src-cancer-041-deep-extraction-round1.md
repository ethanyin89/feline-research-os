---
id: src-cancer-041-deep-extraction-round1
type: system
source_id: src-cancer-041
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-041

**Source:** Prognostic Factors in Feline Mammary Carcinoma
**Journal:** Journal of the National Cancer Institute (JNCI) (1983)
**PMID:** 6572759
**Evidence Level:** original-study (prospective cohort, landmark)

## Phase 0: Context

**Access status:** Abstract available from PubMed. Full-text via Oxford Academic (JNCI).

**Source scope:** 1983 landmark prospective study of 202 surgically treated FMC cats evaluating 35 prognostic factors.

**Historical importance:** One of the largest and most rigorous early FMC prognostic factor studies. Published in JNCI (high-impact journal). Foundational for FMC prognosis understanding.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Study type | Prospective follow-up |
| Sample size | 202 cats |
| Treatment | Mastectomy + block dissection |
| Factors analyzed | 35 |
| Factor categories | General, anamnestic, clinical, histologic, therapy |
| Outcomes | Survival, local recurrence |

### 1.2 Univariate Analysis

17 factors related to survival in univariate analysis. After multivariate correction, 6 remained independent.

### 1.3 Independent Prognostic Factors

| Factor | Category | Direction |
|--------|----------|-----------|
| Age | General | Older = worse |
| Tumor diameter | Clinical | Larger = worse |
| Lymph node status (microscopic) | Staging | Positive = worse |
| Mitotic figures | Histologic | More = worse |
| Tumor necrosis | Histologic | Present = worse |
| Surgical completeness | Therapy | Incomplete = worse |

### 1.4 Factor Categories

| Category | Independent Factors |
|----------|---------------------|
| Patient factors | Age |
| Tumor burden | Diameter, lymph nodes |
| Tumor biology | Mitotic index, necrosis |
| Treatment | Surgical completeness |

## Phase 2: Theme Reconstruction

### Theme A: Tumor Size as Key Predictor

Tumor diameter as independent predictor is consistent with:
- src-cancer-012 (tumor size most significant, P<0.0001)
- src-cancer-028 (tumor grade/mitotic index validated)

This triad of studies establishes tumor size as the most robust prognostic factor.

### Theme B: Lymph Node Status

Microscopic lymph node involvement predicts worse outcome:
- Supports staging before treatment
- Requires histopathologic evaluation
- Palpation alone insufficient (microscopic involvement)

### Theme C: Tumor Biology Markers

Mitotic figures and necrosis as independent predictors:
- High mitotic index = aggressive tumor
- Necrosis = rapid growth outpacing blood supply
- Both accessible via routine histopathology

### Theme D: Surgical Quality Matters

Completeness of surgical treatment as independent predictor:
- Supports aggressive surgical approach
- Incomplete excision predicts recurrence
- Margin status implicitly important

### Theme E: Comparative Oncology Foundation

The study explicitly compared FMC and canine mammary cancer as experimental therapy models:
- Validates feline model for translational research
- 1983 foundation for comparative oncology

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC41 | Tumor diameter is independent prognostic factor (n=202, 1983) | A | landmark study |
| MC42 | Microscopic lymph node involvement is independent prognostic factor | A | staging importance |
| MC43 | Mitotic index is independent prognostic factor | A | tumor biology |
| MC44 | Tumor necrosis is independent prognostic factor | A | histopathology |
| MC45 | Surgical completeness is independent prognostic factor | A | treatment quality |
| MC46 | Age is independent prognostic factor in FMC | A | patient factor |

**Section to update:** Prognostic Factors

**Boundary rules:**
- 1983 study — surgical techniques may have evolved
- Independent factors remain foundational
- Multivariate analysis provides strong evidence

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Tumor diameter is independent prognostic factor
- [x] Lymph node status (microscopic) is independent prognostic factor
- [x] Mitotic index is independent prognostic factor
- [x] Tumor necrosis is independent prognostic factor
- [x] Surgical completeness affects outcome
- [x] Age is independent prognostic factor

### not_safe_to_promote_yet

- [ ] Specific survival times (may be outdated)
- [ ] Treatment recommendations based on prognostic factors
- [ ] Cutoff values for tumor size categories
- [ ] 1983 surgical technique details

### open_questions

1. Have these prognostic factors been validated in modern cohorts?
2. What tumor size cutoffs are prognostically meaningful?
3. How do modern surgical techniques compare?
4. Are there interaction effects between factors?
5. Can prognostic factors guide adjuvant therapy selection?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 6 independent prognostic factor claims |
| Evidence level | original-study (n=202, prospective, JNCI) |
| Key contribution | Landmark — established 6 independent FMC prognostic factors |
| Primary gap | Modern validation |
| Topic page targets | mammary-carcinoma.md (prognostic factors) |
| Cross-reference | Validates src-cancer-012 (tumor size), src-cancer-028 (grade) |
