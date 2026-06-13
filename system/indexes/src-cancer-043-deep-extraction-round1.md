---
id: src-cancer-043-deep-extraction-round1
type: system
source_id: src-cancer-043
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-043

**Source:** Identification of an immune-suppressed subtype of feline triple-negative basal-like invasive mammary carcinomas, spontaneous models of breast cancer
**Journal:** Tumour Biology (2020)
**DOI:** 10.1177/1010428319901052
**PMID:** 31959092
**Evidence Level:** original-study (large cohort with outcomes)

## Phase 0: Context

**Access status:** Abstract available from PubMed. SAGE journal access required for full-text.

**Source scope:** 2020 study of 180 surgically treated FMC cats with 2-year follow-up, evaluating regulatory T cells as prognostic markers and identifying immune-suppressed subtype.

**Key contribution:** Largest FMC regulatory T cell study; identifies immune-suppressed subgroup with worse prognosis.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Sample size | 180 female cats |
| Treatment | Surgery only |
| Follow-up | 2 years post-mastectomy |
| Outcomes | DFI, OS, CSS |

### 1.2 Molecular Subtyping

| Subtype | Count | Percentage |
|---------|-------|------------|
| Triple-negative (ER-, PR-, HER2-) | 123 | 68% |
| Luminal (ER+ and/or PR+) | 57 | 32% |

**Key finding:** 68% triple-negative rate confirms high TNBC prevalence in FMC (consistent with src-cancer-022).

### 1.3 Markers Assessed

| Marker | Type |
|--------|------|
| FoxP3 | Regulatory T cell marker |
| ER | Hormone receptor |
| PR | Hormone receptor |
| HER2 | Growth factor receptor |
| Ki-67 | Proliferation marker |
| CK14 | Basal cytokeratin |

### 1.4 Regulatory T Cell Findings

| Location | Abundance |
|----------|-----------|
| Peritumoral | 300× more abundant |
| Intratumoral | Reference |

**Key finding:** Tregs concentrate at tumor periphery, not within tumor mass.

### 1.5 Prognostic Associations

| Treg Status | Outcome |
|-------------|---------|
| High peritumoral Tregs | Shorter DFI, OS |
| High intratumoral Tregs | Shorter DFI, OS |
| Applies to | Both TNBC and luminal |

### 1.6 Immune-Suppressed Subtype

| Feature | Treg-enriched | Treg-poor |
|---------|---------------|-----------|
| Disease-free interval | Worse | Better |
| Overall survival | Worse | Better |
| Cancer-specific survival | Worse | Better |
| Subtype | TNBC + CK14+ (basal-like) | TNBC + CK14+ |

**Key finding:** Within basal-like TNBC, Treg-enriched tumors have significantly worse outcomes.

## Phase 2: Theme Reconstruction

### Theme A: Immunosuppressive Microenvironment

High Tregs indicate immune evasion:
- Tregs suppress anti-tumor immunity
- Peritumoral location suggests "immune barrier"
- May explain chemotherapy resistance
- Target for immunotherapy

### Theme B: TNBC Heterogeneity

Not all TNBC are equal:
- Treg-enriched vs Treg-poor subgroups
- Different prognosis within same receptor status
- Need for immune profiling beyond ER/PR/HER2

### Theme C: Immunotherapy Rationale

This study provides rationale for:
- Treg depletion strategies
- Immune checkpoint inhibitors
- Combination immunotherapy
- Patient selection based on Treg status

**Boundary:** Research direction, not treatment recommendation.

### Theme D: Comparative Oncology Model

FMC as immunotherapy model:
- Spontaneous immune-suppressed tumors
- Similar to human TNBC
- Can test immunotherapy strategies
- Outcomes measurable in 2 years

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC47 | 68% (123/180) of FMC are triple-negative | A | large cohort confirmation |
| MC48 | Peritumoral regulatory T cells are 300× more abundant than intratumoral | A | quantified finding |
| MC49 | High regulatory T cells associated with shorter survival in FMC | A | prognostic finding |
| MC50 | Treg-enriched basal-like TNBC is an immune-suppressed subtype with worse prognosis | B | subtype identification |

**Section to update:** Tumor Microenvironment / Immunology / Prognosis

**Boundary rules:**
- Prognostic marker, not treatment selection
- Research supports immunotherapy investigation
- Does not recommend Treg-targeted therapy (not available)

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] 68% of FMC are triple-negative
- [x] Peritumoral Tregs 300× more abundant than intratumoral
- [x] High Tregs associated with shorter DFI and OS
- [x] Treg-enriched basal-like TNBC has worse prognosis
- [x] FMC is model for immune-suppressed breast cancer

### not_safe_to_promote_yet

- [ ] Treg-targeted therapy recommendations
- [ ] Immunotherapy efficacy in FMC
- [ ] Treg cutoffs for clinical use
- [ ] Specific survival times by Treg status

### open_questions

1. Can Treg depletion improve FMC outcomes?
2. Are immune checkpoint inhibitors effective in Treg-high FMC?
3. What Treg cutoff is clinically meaningful?
4. Does Treg status predict immunotherapy response?
5. Are there other immune suppressive markers in FMC?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 immune microenvironment claims |
| Evidence level | original-study (n=180, 2-year follow-up) |
| Key contribution | Treg-enriched immune-suppressed TNBC subtype |
| Primary gap | Therapeutic application |
| Topic page targets | mammary-carcinoma.md (TME, immunology, prognosis) |
| Cross-reference | Validates src-cancer-022 (TNBC prevalence), complements src-cancer-016/017 (TME) |
