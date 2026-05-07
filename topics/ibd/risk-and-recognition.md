---
id: topic-ibd-risk-and-recognition
type: topic
topic: ibd
species: feline
disease: IBD
question_type: recognition
source_ids: [src-ibd-003, src-ibd-004, src-ibd-009, src-ibd-010, src-ibd-015, src-ibd-016, src-ibd-017, src-ibd-019, src-ibd-024]
last_compiled_at: 2026-05-06
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline IBD Risk And Recognition

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FR1 | Feline IBD recognition should begin as chronic-enteropathy suspicion and diagnosis of exclusion, not assumed idiopathic IBD. | B | src-ibd-003, src-ibd-024 | recognition frame, not final diagnosis |
| FR2 | FCEAI supports activity and response tracking but cannot classify IBD versus food-responsive enteropathy or lymphoma. | B | src-ibd-004 | burden tracking, not etiologic classification |
| FR3 | Muscularis thickening raises lymphoma pressure, while lymphadenopathy is less class-specific. | B | src-ibd-010 | suspicion-shaping, not lymphoma diagnosis |
| FR4 | Biopsy-site strategy matters because duodenal and ileal findings can disagree and lymphoma may be ileal-only. | B | src-ibd-015 | sampling completeness boundary |
| FR5 | Report-language normalization, tissue markers, fecal S100A12, and metabolomics support interpretation but should not replace tissue-centered workup. | B | src-ibd-009, src-ibd-016, src-ibd-017, src-ibd-019 | support / frontier layer, not routine class certainty |

## Evidence-Depth Caveat

This page sits on a fully deep-extracted IBD source-card layer (24/24 papers). Key anchors: broad IBD review (`src-ibd-003`), practice chronic-enteropathy review (`src-ibd-024`), FCEAI activity index (`src-ibd-004`), ultrasound muscularis boundary (`src-ibd-010`), duodenum/ileum biopsy-site study (`src-ibd-015`), pathology-report workflow paper (`src-ibd-009`), Bcl-2 tissue-marker boundary (`src-ibd-016`), fecal S100A12 support marker (`src-ibd-017`), and metabolomics frontier branch (`src-ibd-019`). This is now a recognition handbook rather than a routing page.

## Core Takeaway

IBD recognition is strongest when treated as an exclusion-first chronic-enteropathy workup. Activity scoring, imaging, biopsy-site choice, pathology interpretation, and bounded markers all matter, but none should shortcut the IBD-versus-small-cell-lymphoma boundary.

## Recognition Architecture

### Core Recognition Frame

Start from chronic enteropathy, not from confirmed idiopathic IBD. Dietary disease and well-differentiated alimentary lymphoma can mimic IBD clinically and histologically, so recognition must remain exclusion-first.

**Lead sources:** `src-ibd-003`, `src-ibd-024`

### Clinical Activity And Response Tracking

FCEAI gives the module a practical activity and treatment-response measure across IBD and food-responsive enteropathy contexts. It is operationally useful but not class-defining.

**Lead sources:** `src-ibd-004`

**Current safe read:**
- FCEAI can stage burden and track response
- activity reduction is not the same thing as etiologic diagnosis
- activity scoring should remain below exclusion-first classification

### Imaging Pressure

Ultrasound muscularis propria thickening should increase lymphoma concern, especially in older cats, while lymphadenopathy is less specific because it can appear in both IBD and lymphoma contexts.

**Lead sources:** `src-ibd-010`

**Current safe read:**
- muscularis thickening is lymphoma-leaning suspicion pressure
- imaging can guide biopsy urgency and suspicion, but not close the case
- lymphadenopathy should not be treated as class-specific

### Tissue Strategy And Pathology Interpretation

Endoscopic biopsy remains central, and site choice matters. Poor agreement between duodenal and ileal diagnoses means duodenal convenience is not diagnostic completeness.

**Lead sources:** `src-ibd-015`, `src-ibd-009`

**Current safe read:**
- ileal evaluation can change whether small-cell lymphoma is detected
- one-site nonlymphoma tissue is not strong exclusion when suspicion remains high
- pathology-report classification improves language workflow but does not solve biology

### Bounded Marker And Frontier Support

Bcl-2 is lymphoma-leaning but overlapping; fecal S100A12 supports disease-versus-health inflammation but does not separate IBD from lymphoma; metabolomics is the strongest frontier class-separation branch but is not routine-ready.

**Lead sources:** `src-ibd-016`, `src-ibd-017`, `src-ibd-019`

**Current safe read:**
- support markers add depth below tissue-centered workup
- marker differences are not one-marker diagnosis
- metabolomics is future stratification, not routine leadership

## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-ibd-003 | broad review: diagnosis-of-exclusion frame and mimic warning | deep_extracted |
| src-ibd-004 | FCEAI activity and response-tracking anchor | deep_extracted |
| src-ibd-009 | pathology-report workflow and classification-language support | deep_extracted |
| src-ibd-010 | ultrasound muscularis lymphoma-pressure boundary | deep_extracted |
| src-ibd-015 | duodenal/ileal biopsy-site completeness anchor | deep_extracted |
| src-ibd-016 | Bcl-2 tissue-marker boundary | deep_extracted |
| src-ibd-017 | fecal S100A12 noninvasive inflammatory support | deep_extracted |
| src-ibd-019 | metabolomics frontier class-separation branch | deep_extracted |
| src-ibd-024 | practice-oriented chronic-enteropathy frame | deep_extracted |

## Current Owner Memo

- [IBD diagnostic workup memo](../../system/indexes/ibd-diagnostic-workup-memo.md)
- [IBD-lymphoma boundary memo](../../system/indexes/ibd-lymphoma-boundary-memo.md)
- [IBD tissue-marker boundary memo](../../system/indexes/ibd-tissue-marker-boundary-memo.md)
- [IBD support and frontier marker memo](../../system/indexes/ibd-support-and-frontier-marker-memo.md)

## Guardrail

Do not let chronic-enteropathy activity, ultrasound pressure, one-site biopsy, report classification, or marker signal become a shortcut around exclusion-first workup and the small-cell lymphoma boundary.

## What The Module Can Say Safely

- IBD recognition begins as chronic-enteropathy suspicion
- FCEAI is useful for activity and response tracking
- muscularis thickening raises lymphoma concern but does not diagnose lymphoma
- ileal biopsy can be decisive for detecting small-cell lymphoma
- support markers and metabolomics deepen the boundary without replacing tissue-centered workup

## What The Module Should Not Say Yet

- do not treat chronic enteropathy as confirmed idiopathic IBD
- do not treat FCEAI response as disease-class proof
- do not treat one-site negative tissue as strong lymphoma exclusion
- do not promote fecal S100A12, Bcl-2, or metabolomics into routine stand-alone classification

## Current Role

Use this page as the IBD recognition handbook. The source-card layer is complete at 24/24 deep-extracted papers. Next gains come from full-text or image/table precision where workup sequence, biopsy strategy, or lymphoma-boundary outputs need tighter operational detail.
