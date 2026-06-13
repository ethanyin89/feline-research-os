---
id: src-cancer-052-deep-extraction-round1
type: system
source_id: src-cancer-052
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-052

**Source:** Immunohistochemical Expression and Prognostic Value of COX-2 and Alpha-Smooth Muscle Actin-positive Cancer-associated Fibroblasts in Feline Mammary Cancer
**Journal:** In Vivo (2024)
**DOI:** 10.21873/invivo.13478
**PMID:** 38418156
**Evidence Level:** original-study (prognostic biomarker)

## Phase 0: Context

**Access status:** Open access via In Vivo journal.

**Source scope:** 2024 prognostic biomarker study evaluating COX-2 and α-SMA+ cancer-associated fibroblasts (CAFs) in 50 feline malignant mammary tumors.

**Key contribution:** First study to demonstrate prognostic value of CAFs in feline mammary cancer; confirms COX-2 prognostic association.

**Critical boundary:** Prognostic marker evidence only. Does not establish treatment protocols.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Population | 50 felines with malignant mammary tumors |
| Markers | COX-2, α-SMA-positive CAFs |
| Methods | Immunohistochemistry |
| Outcomes | Disease-free survival (DFS), overall survival (OS) |

### 1.2 COX-2 Associations

| Feature | p-value |
|---------|---------|
| Mitotic index | 0.031 |
| Malignancy degree | ≤0.001 |
| Lymph node metastasis | ≤0.001 |
| Vascular invasion | 0.002 |
| Recurrence | 0.019 |
| Distant metastasis | 0.036 |

**COX-2 finding:** Strongly associated with aggressive features and poor outcomes.

### 1.3 α-SMA+ CAF Associations

| Feature | p-value |
|---------|---------|
| Mitotic index | 0.004 |
| Lymph node metastasis | 0.027 |
| Vascular invasion | 0.05 |
| Recurrence | ≤0.001 |
| Distant metastasis | ≤0.001 |

**CAF finding:** Also associated with aggressive features, particularly recurrence and distant metastasis.

### 1.4 Survival Outcomes

| Marker | DFS | OS |
|--------|-----|-----|
| COX-2 overexpression | Correlated (poor) | Correlated (poor) |
| High α-SMA+ CAFs | Correlated (poor) | Correlated (poor) |

**Both markers emerged as poor-prognosis predictors.**

## Phase 2: Theme Reconstruction

### Theme A: COX-2 as Prognostic Marker

COX-2 overexpression predicts:
- More aggressive tumor behavior
- Higher metastatic potential
- Worse survival outcomes
- Confirms prior FMC COX-2 studies (see src-cancer-034)

**Clinical implication:** COX-2 status may stratify risk.

### Theme B: Tumor Microenvironment (CAFs)

Cancer-associated fibroblasts:
- α-SMA positivity marks activated CAFs
- Associated with tumor progression
- Linked to metastasis (LN and distant)
- Novel finding in feline oncology

**Research direction:** TME targeting may be therapeutic avenue.

### Theme C: Combined Marker Value

Both markers together:
- Reinforce poor-prognosis signature
- Different mechanisms (inflammation vs stroma)
- May identify highest-risk subset

### Theme D: Therapeutic Implications

Potential targets suggested by findings:
- COX-2 inhibitors (NSAIDs) - must be studied separately
- CAF-targeting therapies - research stage only
- Neither represents current standard of care

**Boundary:** Prognostic evidence, not treatment recommendation.

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-PROG6 | COX-2 overexpression predicts poor DFS and OS in FMC | A | n=50, 2024 |
| MC-PROG7 | α-SMA+ CAFs predict poor DFS and OS in FMC | A | n=50, 2024 |
| MC-TME1 | High α-SMA+ CAFs associated with LN and distant metastasis | A | tumor microenvironment |
| MC-COX2 | COX-2 overexpression associated with vascular invasion and metastasis | A | complements src-cancer-034 |

**Section to update:** Prognostic Factors / Tumor Microenvironment

**Boundary rules:**
- Prognostic association only
- Not treatment selection criteria
- Does not validate COX-2 inhibitor therapy
- Single-center, moderate sample size

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] COX-2 overexpression is a poor-prognosis marker in FMC
- [x] α-SMA+ CAFs are a poor-prognosis marker in FMC
- [x] Both markers associated with metastasis
- [x] Both markers associated with survival outcomes

### not_safe_to_promote_yet

- [ ] Treatment selection based on COX-2/CAF status
- [ ] NSAID therapy efficacy in COX-2+ FMC
- [ ] CAF-targeting therapy options
- [ ] Cutoffs for clinical risk stratification

### open_questions

1. Do NSAIDs improve outcomes in COX-2+ FMC?
2. Can CAF status guide treatment selection?
3. Are COX-2 and CAF status independent predictors?
4. What is the optimal marker combination for prognosis?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 prognostic marker claims |
| Evidence level | original-study (prognostic, n=50) |
| Key contribution | First CAF prognostic data in FMC; confirms COX-2 |
| Primary gap | Treatment implications |
| Topic page targets | mammary-carcinoma.md (prognosis, TME) |
| Cross-reference | Complements src-cancer-034 (COX-2 expression) |
