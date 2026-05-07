---
id: topic-ibd-endpoint-handbook
type: topic
topic: ibd
species: feline
disease: IBD
question_type: endpoints
source_ids: [src-ibd-004, src-ibd-010, src-ibd-013, src-ibd-015, src-ibd-017, src-ibd-019, src-ibd-022]
last_compiled_at: 2026-05-06
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline IBD Endpoint Handbook

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FE1 | FCEAI is the strongest current operational activity-and-response endpoint, but it does not classify disease identity. | B | src-ibd-004 | activity endpoint, not etiology |
| FE2 | Histopathology and biopsy-site yield belong to confirmation and lymphoma-boundary workup rather than routine activity tracking. | B | src-ibd-015 | tissue strategy, not simple score |
| FE3 | Muscularis propria thickening is a lymphoma-leaning imaging endpoint, not an IBD-defining endpoint. | B | src-ibd-010 | suspicion support, not diagnosis |
| FE4 | Vitamin D and fecal S100A12 are bounded support markers that indicate abnormal burden more than class separation. | B | src-ibd-013, src-ibd-017 | support markers, not discriminator endpoints |
| FE5 | Metabolomics is the strongest current frontier-separation endpoint, while fibrosis is structural chronicity / burden architecture. | C | src-ibd-019, src-ibd-022 | future stratification and chronicity, not routine endpoint leadership |

## Evidence-Depth Caveat

This page sits on a fully deep-extracted IBD source-card layer (24/24 papers). Key anchors: FCEAI activity index (`src-ibd-004`), biopsy-site utility (`src-ibd-015`), ultrasound muscularis boundary (`src-ibd-010`), vitamin D support marker (`src-ibd-013`), fecal S100A12 support marker (`src-ibd-017`), metabolomics frontier branch (`src-ibd-019`), and intestinal fibrosis/chronicity anchor (`src-ibd-022`). This is now an endpoint handbook rather than a routing page.

## Core Takeaway

IBD endpoint architecture should separate activity tracking, tissue-centered diagnostic workup, imaging suspicion pressure, support markers, frontier class-separation, and structural chronicity. The current source layer does not support a single-marker endpoint that leads the whole module.

## Endpoint Hierarchy

### Endpoint 1: Clinical Activity And Response

FCEAI is the most operational endpoint in the current seed corpus. It tracks severity and response across IBD and food-responsive enteropathy contexts.

**Key boundary:** activity and response tracking, not disease-class definition.

**Lead sources:** `src-ibd-004`

### Endpoint 2: Tissue-Centered Confirmation

Histopathology and biopsy-site yield are central to diagnostic confirmation and lymphoma-boundary workup. Ileal sampling can change whether small-cell lymphoma is detected.

**Key boundary:** tissue strategy and confirmation, not routine activity scoring.

**Lead sources:** `src-ibd-015`

### Endpoint 3: Imaging Support

Muscularis propria thickening is a workup-shaping endpoint because it raises lymphoma suspicion. It should guide suspicion and tissue strategy, not define IBD.

**Key boundary:** lymphoma-leaning pressure, not standalone diagnosis.

**Lead sources:** `src-ibd-010`

### Endpoint 4: Support Markers

Vitamin D and fecal S100A12 show abnormal disease burden or inflammation but overlap too much to separate IBD from lymphoma by themselves.

**Key boundary:** bounded support, not class separation.

**Lead sources:** `src-ibd-013`, `src-ibd-017`

### Endpoint 5: Frontier Separation And Structural Chronicity

Metabolomics is the strongest current frontier-separation signal, while fibrosis belongs to structural chronicity and burden interpretation.

**Key boundary:** metabolomics is not routine-ready; fibrosis is not inflammatory activity or antifibrotic treatment readiness.

**Lead sources:** `src-ibd-019`, `src-ibd-022`

## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-ibd-004 | FCEAI activity and response endpoint | deep_extracted |
| src-ibd-010 | ultrasound muscularis lymphoma-pressure endpoint | deep_extracted |
| src-ibd-013 | vitamin D burden / complication support marker | deep_extracted |
| src-ibd-015 | duodenal/ileal biopsy-site yield and confirmation strategy | deep_extracted |
| src-ibd-017 | fecal S100A12 inflammatory support marker | deep_extracted |
| src-ibd-019 | metabolomics frontier class-separation branch | deep_extracted |
| src-ibd-022 | intestinal fibrosis structural chronicity anchor | deep_extracted |

## Current Owner Memo

- [IBD diagnostic workup memo](../../system/indexes/ibd-diagnostic-workup-memo.md)
- [IBD support and frontier marker memo](../../system/indexes/ibd-support-and-frontier-marker-memo.md)
- [IBD fibrosis memo](../../system/indexes/ibd-fibrosis-memo.md)
- [IBD tissue-marker boundary memo](../../system/indexes/ibd-tissue-marker-boundary-memo.md)

## Guardrail

Do not turn endpoint evidence into class certainty. FCEAI, imaging, vitamin D, fecal S100A12, metabolomics, and fibrosis each answer different endpoint questions; none replaces the exclusion-first IBD-versus-lymphoma workup.

## What The Module Can Say Safely

- FCEAI is the strongest current activity-and-response endpoint
- biopsy-site strategy belongs to diagnostic confirmation and lymphoma exclusion
- muscularis thickening is lymphoma-leaning workup support
- vitamin D and fecal S100A12 are support markers rather than class discriminators
- metabolomics is promising frontier separation, and fibrosis is structural chronicity

## What The Module Should Not Say Yet

- do not treat activity scoring as etiologic classification
- do not treat muscularis thickening as definitive lymphoma diagnosis
- do not treat vitamin D or fecal S100A12 as IBD-versus-lymphoma separators
- do not treat metabolomics or fibrosis as routine-ready lead endpoints

## Current Role

Use this page as the IBD endpoint handbook. The source-card layer is complete at 24/24 deep-extracted papers. Next gains come from full-text precision where endpoint ranking, workup sequence, or output claims need stronger class-separation detail.
