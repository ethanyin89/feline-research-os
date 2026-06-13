---
id: src-cancer-016-deep-extraction-round1
type: system
source_id: src-cancer-016
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-016

**Source:** Tumor microenvironment of human breast cancer, and feline mammary carcinoma as a potential study model
**Journal:** BBA Reviews on Cancer (2021)
**DOI:** 10.1016/j.bbcan.2021.188587
**PMID:** 34237352
**Evidence Level:** review

## Phase 0: Context

**Access status:** Full abstract available in source card. ScienceDirect (Elsevier).

**Source scope:** Comprehensive review of tumor microenvironment (TME) components in breast cancer, with FMC positioned as a comparative oncology model.

**Framework value:** Provides complete enumeration of TME cellular actors and validates FMC model.

## Phase 1: Sequential Micro-Analysis

### 1.1 TME Cellular Components

| Cell Type | Abbreviation | Role |
|-----------|--------------|------|
| Tumor Infiltrating Lymphocytes | TILs | Adaptive immunity |
| Natural Killer cells | NK | Innate immunity |
| Tumor Infiltrating Dendritic Cells | TIDCs | Antigen presentation |
| Tumor Associated Macrophages | TAMs | Variable (M1/M2) |
| Tumor Associated Neutrophils | TANs | Variable (N1/N2) |
| Cancer Associated Fibroblasts | CAFs | Stromal support |
| Myeloid-Derived Suppressor Cells | MDSCs | Immunosuppression |

**Key insight:** Complete enumeration of TME cellular actors provides framework for understanding tumor-immune interactions.

### 1.2 Non-Cellular TME Components

| Component | Category |
|-----------|----------|
| Pro-angiogenic factors | Vascular |
| Immune checkpoint biomarkers | Immunomodulatory |

### 1.3 Immune Escape Mechanism

| Process | Description |
|---------|-------------|
| Immunoediting | Cancer cells escape immune control |
| Communication networks | Complex signaling between immune and cancer cells |

**Therapeutic implication:** Understanding immunoediting informs immunotherapy approaches.

### 1.4 FMC Model Validation

| Shared Feature | Category |
|----------------|----------|
| Clinicopathological features | Clinical presentation |
| Histopathological features | Microscopic appearance |
| Epidemiological features | Disease patterns |
| Cancer initiation pathways | Molecular mechanisms |
| Cancer progression pathways | Molecular mechanisms |

**Conclusion:** FMC is "a reliable cancer model for the study of human breast cancer"

## Phase 2: Theme Reconstruction

### Theme A: TME Complexity

The tumor microenvironment involves multiple cell types with complex interactions:
- Immune cells (TILs, NK, TIDCs)
- Immunosuppressive cells (TAMs, MDSCs)
- Stromal cells (CAFs)
- Pro-tumor neutrophils (TANs)

Understanding these interactions is "crucial for the development of more effective therapeutic approaches."

### Theme B: Immunoediting and Escape

Cancer cells use immunoediting to escape immune control. This involves:
- Complex communication between cancer and immune cells
- Manipulation of immune checkpoint pathways
- Creation of immunosuppressive microenvironment

### Theme C: FMC as Reliable Model

FMC is validated as a comparative model across multiple dimensions:
- **Clinical:** Similar presentation and behavior
- **Pathological:** Similar histology and features
- **Epidemiological:** Similar disease patterns
- **Molecular:** Shared initiation/progression pathways

This strengthens the case for FMC research translating to human benefit.

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-TME1 | FMC tumor microenvironment includes TILs, TAMs, CAFs, and other immune cells | B | 2021 review framework |
| MC-TME2 | FMC shares clinicopathological, histopathological, and epidemiological features with human breast cancer | B | model validation |
| MC-TME3 | FMC shares cancer initiation and progression pathways with human breast cancer | B | mechanistic basis |
| MC-TME4 | FMC is validated as "a reliable cancer model" for human breast cancer research | B | comparative oncology |

**Section to add:** Tumor Microenvironment / Immunobiology

**Boundary rules:**
- TME description is for understanding, not treatment guidance
- Do not recommend immunotherapy without feline trial data
- Frame as research context, not clinical practice

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] TME component enumeration (TILs, TAMs, CAFs, etc.)
- [x] Immunoediting as immune escape mechanism
- [x] FMC shares clinicopathological features with human breast cancer
- [x] FMC shares molecular pathways with human breast cancer
- [x] FMC validated as reliable comparative model

### not_safe_to_promote_yet

- [ ] Specific immunotherapy recommendations
- [ ] Checkpoint inhibitor use in cats
- [ ] Prognostic significance of specific TME features
- [ ] TAM/TIL quantification protocols

### open_questions

1. What is the prognostic significance of TILs in FMC?
2. Are immune checkpoint inhibitors effective in FMC?
3. What is the M1/M2 TAM ratio in FMC?
4. How does FMC TME compare across molecular subtypes?
5. Are there validated TME biomarkers for FMC prognosis?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 TME and model validation claims |
| Evidence level | review (2021, BBA Reviews on Cancer) |
| Key contribution | TME framework, FMC model validation |
| Primary gap | Clinical application of TME knowledge |
| Topic page targets | mammary-carcinoma.md (tumor microenvironment) |
| Translational value | High — validates comparative model |
