---
marp: true
theme: default
paginate: true
title: Feline IBD Internal Research Brief
description: English derived deck from Feline Research OS V1
language: en
source_ids: [src-ibd-001, src-ibd-002, src-ibd-003, src-ibd-004, src-ibd-005, src-ibd-006, src-ibd-007, src-ibd-008, src-ibd-009, src-ibd-010, src-ibd-011, src-ibd-012, src-ibd-013, src-ibd-014, src-ibd-015, src-ibd-016, src-ibd-017, src-ibd-018, src-ibd-019, src-ibd-020, src-ibd-021, src-ibd-022, src-ibd-023, src-ibd-024]
derived_from: outputs/slides/out-ibd-slides-20260409-v1-working-en.md
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
---

# Feline IBD
## Internal Research Brief V1 (English)

Feline Research OS  
2026-04-09

---

# Why IBD Matters

- IBD is not a simple inflammation topic
- It forces the system to connect:
  - exclusion-first workup
  - lymphoma-boundary handling
  - marker hierarchy
  - early treatment logic
- This makes it a strong reusable disease-module pattern

---

# Current Corpus

- 24 IBD-related literature sources ingested
- all 24 IBD paper cards now have round-1 deep extraction coverage
- compiled topic pages now exist for:
  - mechanism
  - endpoints
  - recognition
  - translation
  - synthesis
- first reusable entity cards and English output layers now exist

---

# Language Note

- This deck is the derived English deck
- It is built from the `working-en` slide file
- It is not a bilingual deck
- It does not imply stronger evidence than the underlying slide source

---

# Core Disease Frame

- Feline IBD currently sits inside `chronic enteropathy`
- The strongest current top-line architecture is:
  - diagnosis of exclusion
  - IBD-versus-small-cell-lymphoma boundary
  - activity versus identity separation

Bottom line:

Do not model feline IBD as a one-test or one-marker disease.

---

# What Leads Workup

- `FCEAI` is useful for activity and response tracking
- `FCEAI` is not a disease-class discriminator
- `Biopsy site choice` matters:
  - duodenum
  - ileum
- `Muscularis thickening` is a lymphoma-leaning imaging signal

Internal implication:

Workup architecture matters more than any single marker.

---

# Boundary Logic

- The main nearby boundary disease is:
  - small-cell alimentary lymphoma
- Current boundary pressure comes from:
  - imaging
  - biopsy-site strategy
  - tissue-marker studies
  - microbiota studies
  - metabolomic frontier work

This is a multimodal problem, not a one-test problem.

---

# Marker Hierarchy

## Support markers

- vitamin D
- fecal S100A12

## Frontier marker

- metabolomics

## Rule

Do not collapse support markers and frontier markers into one biomarker tier.

---

# Pathology And Chronicity

- Idiopathic IBD now has its own immunopathology depth branch
- Fibrosis now has its own structural chronicity branch
- Fibrosis should not be treated as background histology

Internal implication:

The module now separates:
- activity
- pathology depth
- structural chronicity

---

# Early Treatment Anchor

## Clearest current direct anchor

- hydrolysed diet response

## What it means

- diet-first management is currently the cleanest practical treatment frame

## What it does not mean

- not idiopathic-IBD-specific proof
- not a final treatment hierarchy

---

# What We Can Say Now

## Defensible now

- IBD should be modeled inside chronic enteropathy
- exclusion-first workup is the right backbone
- the lymphoma boundary is central
- marker hierarchy is real
- fibrosis is a structural chronicity branch
- diet-first logic is the cleanest current practical treatment anchor

## Not defensible yet

- one-marker diagnosis
- final treatment ranking
- routine-ready metabolomic deployment
- regulatory path recommendation

---

# Immediate Next Steps

1. Keep paired `-zh` output layers aligned with the now-complete source-card layer
2. Add full-text, image/table, or regulatory precision only when a concrete output needs it
3. Keep entity coverage growing only where reuse is already obvious
4. Preserve the hierarchy:
   - workup
   - boundary
   - markers
   - pathology
   - treatment
