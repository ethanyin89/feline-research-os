---
id: src-cancer-017-deep-extraction-round1
type: system
source_id: src-cancer-017
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-017

**Source:** Advances in immunotherapy for breast cancer and feline mammary carcinoma: From molecular basis to novel therapeutic targets
**Journal:** BBA Reviews on Cancer (2024)
**DOI:** 10.1016/j.bbcan.2024.189144
**PMID:** 38914239
**Evidence Level:** review

## Phase 0: Context

**Access status:** Full abstract available in source card. ScienceDirect (Elsevier).

**Source scope:** Comprehensive 2024 review on immunotherapy advances, focusing on five major immune checkpoints in breast cancer and FMC.

**Timeliness:** Most current (2024) immunotherapy review for FMC — high value for understanding research directions.

## Phase 1: Sequential Micro-Analysis

### 1.1 FMC Burden Context

| Claim | Value | Boundary |
|-------|-------|----------|
| FMC ranking | 3rd most frequent feline malignancy | epidemiology |
| Human parallel | Female breast cancer most prevalent malignancy | comparative context |

### 1.2 Immune Checkpoints Reviewed

| Checkpoint | Full Name | Function |
|------------|-----------|----------|
| CTLA-4 | Cytotoxic T-Lymphocyte-Associated Antigen 4 | T cell inhibition |
| LAG-3 | Lymphocyte Activation Gene-3 | T cell exhaustion |
| PD-1 | Programmed Cell Death Protein-1 | T cell inhibition |
| VISTA | V-domain Ig Suppressor of T cell Activation | T cell suppression |
| TIM-3 | T-cell Immunoglobulin and Mucin Domain 3 | T cell exhaustion |

**Key insight:** Complete enumeration of major immune checkpoints being investigated for cancer immunotherapy.

### 1.3 TME and Treatment

| Relationship | Effect |
|--------------|--------|
| TME → Immunotherapy | Modifies effectiveness |
| TME → Chemotherapy | Modulates outcomes and prognoses |
| TME → Other treatments | Affects anticancer treatment results |

**Therapeutic implication:** TME is a therapeutic target that influences multiple treatment modalities.

### 1.4 Research Status

| Aspect | Status (2024) |
|--------|---------------|
| Checkpoint inhibitors | Under investigation as prospective targets |
| FMC studies | Findings reported supporting model validity |
| Clinical translation | Ongoing investigations |

## Phase 2: Theme Reconstruction

### Theme A: Inflammation-Cancer Connection

Inflammation is "a defining characteristic of cancer" and a "compelling target for therapeutic interventions." This frames immunotherapy approaches as addressing fundamental tumor biology.

### Theme B: Five-Checkpoint Framework

The review provides a comprehensive framework covering five major checkpoints:
- **CTLA-4 and PD-1:** Most established targets (human)
- **LAG-3, VISTA, TIM-3:** Emerging targets

This framework organizes the immunotherapy landscape for both human and feline research.

### Theme C: FMC Model Strengthening

This 2024 review adds to the growing evidence (src-cancer-005, src-cancer-013, src-cancer-016) supporting FMC as a comparative oncology model. The immunotherapy angle adds a new dimension beyond molecular and TME similarities.

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-IMM1 | FMC is the 3rd most frequent feline malignancy | B | epidemiology, 2024 review |
| MC-IMM2 | Immune checkpoints (CTLA-4, LAG-3, PD-1, VISTA, TIM-3) are being investigated as therapeutic targets for FMC | B | research direction, not treatment |
| MC-IMM3 | TME modifies effectiveness of immunotherapy and chemotherapy in mammary carcinoma | B | mechanistic context |
| MC-IMM4 | FMC studies support its role as a model for human breast cancer immunotherapy research | B | comparative oncology |

**Section to add:** Immunotherapy / Immune Checkpoints

**Boundary rules:**
- Checkpoint inhibitor therapy for FMC is investigational
- Do not recommend immunotherapy for FMC patients
- Frame as research direction, not clinical practice

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] FMC is 3rd most frequent feline malignancy
- [x] Five major checkpoints are under investigation (CTLA-4, LAG-3, PD-1, VISTA, TIM-3)
- [x] TME modifies immunotherapy and chemotherapy effectiveness
- [x] FMC is being investigated as a model for immunotherapy research
- [x] Inflammation is a defining cancer characteristic

### not_safe_to_promote_yet

- [ ] Checkpoint inhibitor recommendations for cats
- [ ] Specific checkpoint expression levels in FMC
- [ ] Response rates to any immunotherapy
- [ ] Availability of checkpoint inhibitors for feline use

### open_questions

1. Which checkpoints are most highly expressed in FMC?
2. Are any checkpoint inhibitors in clinical trials for cats?
3. Does checkpoint expression predict prognosis in FMC?
4. How does FMC checkpoint profile compare to human breast cancer?
5. What is the safety profile of checkpoint inhibitors in cats?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 immunotherapy and model validation claims |
| Evidence level | review (2024, BBA Reviews on Cancer) |
| Key contribution | Five-checkpoint framework, FMC prevalence, immunotherapy research directions |
| Primary gap | Clinical checkpoint inhibitor data for FMC |
| Topic page targets | mammary-carcinoma.md (immunotherapy section) |
| Timeliness | High — 2024 most current review |
