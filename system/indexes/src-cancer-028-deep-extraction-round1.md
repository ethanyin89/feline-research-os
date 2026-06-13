---
id: src-cancer-028-deep-extraction-round1
type: system
source_id: src-cancer-028
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-028

**Source:** Prognostic histopathological and molecular markers in feline mammary neoplasia
**Journal:** Veterinary Journal (2012)
**DOI:** 10.1016/j.tvjl.2012.05.008
**PMID:** 22841451
**Evidence Level:** review

## Phase 0: Context

**Access status:** Full abstract available. ScienceDirect (Elsevier).

**Source scope:** Comprehensive 2012 review of histopathological and molecular prognostic markers in FMC with comparative oncology framing.

**Key contribution:** Validates tumor grade and mitotic index as reliable prognostic markers; positions FMC as model for late-stage ER-negative breast cancer.

## Phase 1: Sequential Micro-Analysis

### 1.1 Epidemiology

| Finding | Value |
|---------|-------|
| FMC prevalence | ~11% of feline non-integumentary neoplasms |
| Malignancy ratio | more commonly malignant than benign |
| Prognosis | poor — high local recurrence and metastasis |

### 1.2 Validated Prognostic Markers

| Marker | Status | Evidence |
|--------|--------|----------|
| Tumor grade | Validated | Correlates with survival |
| Mitotic index | Validated | Correlates with survival |
| Ki67 | Potential | Needs further corroboration |

**Key finding:** Grade and mitotic index are the most reliable prognostic markers in FMC. This aligns with src-cancer-012 (tumor size as predictor) for a coherent prognostic framework.

### 1.3 Molecular Markers ("Hallmarks of Cancer" Framework)

| Hallmark | Markers Investigated | Status |
|----------|---------------------|--------|
| Proliferation | Ki67, mitotic index | Ki67 needs validation |
| Apoptosis | Various | Surrogate marker studies |
| Angiogenesis | VEGF and others | Surrogate marker studies |
| Invasion/metastasis | Various | Surrogate marker studies |

**Caveat:** Many molecular marker studies used "surrogate markers" (correlation with grade) rather than clinical outcome. This weakens evidence.

### 1.4 Receptor Status Comparison

| Species | ER Status | Implication |
|---------|-----------|-------------|
| Human breast cancer | Variable (ER+ and ER-) | ER+ responds to hormone therapy |
| Feline mammary cancer | High ER-negative rate | Hormone therapy less applicable |

**Model specificity:** FMC is suitable as model for late-stage, ER-negative breast cancer — NOT all breast cancer subtypes.

### 1.5 Basal-Like Properties

| Feature | FMC | Human Basal-Like |
|---------|-----|------------------|
| ER status | Negative | Negative |
| Cytokeratin profile | Basal-like | Basal-like |
| Aggressiveness | High | High |
| Treatment response | Poor to chemotherapy | Poor to targeted therapy |

**Research direction:** Basal-like properties of FMC offer comparative oncology opportunities.

## Phase 2: Theme Reconstruction

### Theme A: Prognostic Marker Hierarchy

This review establishes a hierarchy of prognostic markers in FMC:

1. **Tier 1 (Validated):** Tumor grade, mitotic index
2. **Tier 2 (Promising):** Ki67, tumor size (from other sources)
3. **Tier 3 (Needs validation):** Other molecular markers (surrogate evidence only)

This hierarchy should guide clinical prognostication and research prioritization.

### Theme B: Comparative Oncology Model Specificity

FMC is NOT a general breast cancer model. It is specifically suitable for:
- Late-stage breast cancer
- ER-negative breast cancer
- Basal-like subtype

This is consistent with src-cancer-022 (TNBC phenotype) and src-cancer-005 (comparative oncology).

### Theme C: Evidence Quality Caveat

Many molecular marker studies have methodological limitations:
- Surrogate markers (grade correlation) instead of clinical outcome
- Need for standardized assays (Ki67 cutoffs, IHC protocols)
- Validation in prospective cohorts needed

This caveat should temper claims about molecular marker utility.

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC29 | FMC comprises ~11% of feline non-integumentary neoplasms | A | review estimate |
| MC30 | Tumor grade and mitotic index correlate with survival (validated) | A | prognostic hierarchy |
| MC31 | Ki67 has prognostic potential but needs validation | B | research direction |
| MC32 | High ER-negative rate makes FMC model for late-stage ER- breast cancer | B | model specificity |
| MC33 | Many molecular marker studies use surrogate markers (grade correlation) | B | evidence quality caveat |

**Section to update:** Prognostic Factors

**Boundary rules:**
- Grade and mitotic index are validated for prognostication
- Ki67 needs standardization before routine use
- Model specificity important for comparative oncology claims

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] FMC is ~11% of feline non-integumentary neoplasms
- [x] Tumor grade correlates with survival
- [x] Mitotic index correlates with survival
- [x] High ER-negative rate in FMC
- [x] FMC has basal-like properties
- [x] FMC is suitable model for late-stage ER-negative breast cancer

### not_safe_to_promote_yet

- [ ] Ki67 cutoffs for clinical use
- [ ] Specific molecular marker recommendations beyond grade/mitotic index
- [ ] Treatment selection based on marker status

### open_questions

1. What Ki67 cutoff should be used in FMC?
2. Have 2012 surrogate marker studies been validated with clinical outcomes?
3. Are there newer molecular markers with clinical-grade evidence?
4. How do basal-like FMC respond to targeted therapies?
5. Can molecular subtyping guide FMC treatment selection?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 5 prognostic marker claims |
| Evidence level | review (2012, Vet J) |
| Key contribution | Prognostic marker hierarchy; model specificity |
| Primary gap | Clinical validation of molecular markers beyond grade |
| Topic page targets | mammary-carcinoma.md (prognostic factors) |
| Cross-reference | src-cancer-012 (tumor size), src-cancer-022 (TNBC phenotype) |
