---
id: topic-ibd-mechanism-overview
type: topic
topic: ibd
species: feline
disease: IBD
question_type: mechanism
source_ids: [src-ibd-001, src-ibd-003, src-ibd-006, src-ibd-008, src-ibd-012, src-ibd-018, src-ibd-019, src-ibd-022, src-ibd-024]
last_compiled_at: 2026-04-30
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: active
---

# Feline IBD Mechanism Overview

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| IM1 | IBD mechanism should be organized around mucosal inflammation, microbiota dysbiosis, fibrosis/remodeling, and the lymphoma boundary | B | src-ibd-001, src-ibd-003, src-ibd-022 | compiled mechanism frame |
| IM2 | Microbiota dysbiosis is a real mechanism branch that can touch the IBD-lymphoma boundary, not only generic inflammation | B | src-ibd-001, src-ibd-006, src-ibd-008, src-ibd-019 | not routine diagnostic authority |
| IM3 | Fibrosis should be modeled as a structural chronicity branch, not as background histology | B | src-ibd-022 | fibrosis-burden, not treatment route |
| IM4 | The IBD-lymphoma boundary is multimodal and must stay adjacent to mechanism | B | src-ibd-001, src-ibd-003 | boundary-adjacent, not pathology admin |
| IM5 | Extension branches (eosinophilic fibroplasia, granulomatous colitis) widen the disease map without replacing core idiopathic IBD | C | src-ibd-018, src-ibd-020 | extension-branch control |

## Evidence-Depth Caveat

This page sits on a fully deep-extracted IBD source-card layer (24/24 papers). Key anchors: IBD review (`src-ibd-003`), microbiota-lymphoma study (`src-ibd-001`), FISH microbiota study (`src-ibd-006`), cross-species microbiota review (`src-ibd-008`), idiopathic IBD immunopathology (`src-ibd-012`), fibrosis study (`src-ibd-022`), frontier metabolomics (`src-ibd-019`), eosinophilic fibroplasia extension (`src-ibd-018`), and German chronic enteropathy review (`src-ibd-024`). This is now a mechanism handbook rather than a routing page.

## Core Takeaway

Feline IBD is best modeled as chronic enteropathy with mucosal inflammation at the center, microbiota dysbiosis as a real mechanism branch, fibrosis/remodeling as structural chronicity, and the IBD-lymphoma boundary as an adjacent multimodal problem.

## Mechanism Hierarchy

### Layer 1: Chronic Enteropathy Frame

Chronic enteropathy is the broader framing layer. IBD sits within this frame as a diagnosis of exclusion.

**Lead sources:** `src-ibd-003`, `src-ibd-024`

**Current safe read:**
- IBD should not be equated with chronic vomiting/diarrhea
- exclusion-first recognition architecture matters before mechanism claims
- chronic enteropathy is the starting frame, not IBD identity

### Layer 2: Mucosal Inflammation

Mucosal inflammation is the central operational disease process. This is the histopathologic core of idiopathic IBD.

**Immunopathology:** Idiopathic-IBD immunopathology now has its own depth layer and should not be inferred only from lymphoma-comparison studies.

**Lead sources:** `src-ibd-003`, `src-ibd-012`

**Current safe read:**
- inflammatory infiltrate characterization anchors IBD identity
- immunopathology depth supports mechanistic understanding
- inflammation severity does not cleanly separate IBD from lymphoma

### Layer 3: Microbiota Dysbiosis

Microbiota dysbiosis is a plausible recurrent mechanism branch. Evidence suggests dysbiosis can touch the IBD-lymphoma boundary, not only generic inflammation.

**FISH-based anchoring:** Older FISH-based microbiota work anchors the pre-omics side of the dysbiosis branch.

**Cross-species context:** Review material widens the background frame without replacing feline-primary anchors.

**Frontier separation:** Metabolomics shows the strongest current IBD-lymphoma separation signal but remains future stratification rather than routine diagnostic leadership.

**Lead sources:** `src-ibd-001`, `src-ibd-006`, `src-ibd-008`, `src-ibd-019`

**Current safe read:**
- microbiota differences between IBD and small-cell lymphoma are real
- dysbiosis should not be equated with disease causation
- frontier separation signals are not routine diagnostic tools

### Layer 4: Fibrosis and Structural Remodeling

Fibrosis belongs to a real structural chronicity branch rather than background histology.

**Burden association:** Fibrosis tracks burden-related features such as lower body weight and lower serum albumin.

**Extension phenotypes:** Eosinophilic sclerosing fibroplasia can widen the remodeling map without being collapsed into core IBD.

**Lead sources:** `src-ibd-022`, `src-ibd-018`

**Current safe read:**
- fibrosis should sit above support-marker burden signals in the structural disease map
- chronic-enteropathy architecture becomes stronger when structural remodeling is separated from activity layers
- extension phenotypes remain extension branches, not core IBD

### Layer 5: IBD-Lymphoma Boundary

The IBD-versus-small-cell-lymphoma boundary is multimodal and must stay adjacent to mechanism, not be treated only as pathology admin.

**Boundary architecture:**
- diagnosis of exclusion is the top-level frame
- imaging can tilt suspicion (muscularis thickening → lymphoma)
- biopsy site selection materially changes detection
- molecular/tissue markers support but do not replace multimodal workup

**Lead sources:** `src-ibd-001`, `src-ibd-003`

**Current safe read:**
- the boundary is real and not resolved by single markers
- microbiota and metabolomic differences deepen explanation
- muscularis thickening is the strongest ultrasound pressure toward lymphoma

## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-ibd-001 | microbiota-lymphoma study: dysbiosis touches boundary | deep_extracted |
| src-ibd-003 | IBD review: mechanism frame | deep_extracted |
| src-ibd-006 | FISH microbiota: pre-omics anchoring | deep_extracted |
| src-ibd-008 | cross-species microbiota: background widening | deep_extracted |
| src-ibd-012 | idiopathic IBD immunopathology: own depth layer | deep_extracted |
| src-ibd-018 | eosinophilic fibroplasia: extension branch | deep_extracted |
| src-ibd-019 | metabolomics: frontier IBD-lymphoma separation | deep_extracted |
| src-ibd-022 | fibrosis: structural chronicity branch | deep_extracted |
| src-ibd-024 | German review: chronic enteropathy frame | deep_extracted |

## Current Owner Memos

- [IBD fibrosis memo](../../system/indexes/ibd-fibrosis-memo.md)
- [IBD lymphoma boundary memo](../../system/indexes/ibd-lymphoma-boundary-memo.md)
- [IBD idiopathic pathology memo](../../system/indexes/ibd-idiopathic-pathology-memo.md)
- [IBD extension branch memo](../../system/indexes/ibd-extension-branch-memo.md)

## Guardrail

Do not let one mechanistic slice dominate the page. IBD is not adequately explained by inflammation alone, microbiota alone, or fibrosis alone. The five-layer hierarchy (chronic enteropathy → inflammation → microbiota → fibrosis → lymphoma boundary) is stronger than any single causal story.

## What The Module Can Say Safely

- chronic enteropathy is the starting frame for IBD
- mucosal inflammation is the central operational process
- microbiota dysbiosis is a real mechanism branch
- fibrosis tracks structural chronicity and burden
- the IBD-lymphoma boundary is multimodal

## What The Module Should Not Say Yet

- microbiota correlation is not disease-cause certainty
- fibrosis depth is not a ready antifibrotic treatment route
- frontier markers are not routine diagnostic tools
- extension branches should not overwrite core IBD framing

## Current Role

Use this page as the IBD mechanism handbook. The source-card layer is complete at 24/24 deep-extracted papers. Next gains come from tighter recognition-boundary and treatment-branch compression.
