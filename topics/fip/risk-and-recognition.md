---
id: topic-fip-risk-recognition
type: topic
topic: fip
species: feline
disease: FIP
question_type: recognition
source_ids: [src-fip-003, src-fip-005, src-fip-006, src-fip-007, src-fip-008, src-fip-012, src-fip-015, src-fip-020, src-fip-023]
last_compiled_at: 2026-05-06
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline FIP Risk And Recognition

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FR1 | FIP recognition should separate risk context from actual suspicion-building. | B | src-fip-003, src-fip-005, src-fip-008, src-fip-012, src-fip-020 | risk enrichment, not diagnosis |
| FR2 | Clinicopathology and disease form are the lead operational recognition layer. | B | src-fip-003, src-fip-006, src-fip-015 | suspicion-building, not standalone definitive diagnosis |
| FR3 | Effusive, non-effusive, and neurologic disease forms should shape workup order rather than sit as loose labels. | B | src-fip-006, src-fip-007, src-fip-015, src-fip-023 | form-aware recognition, not severity ranking |
| FR4 | Neurologic or ocular context is a branch shift before CSF support becomes central. | B | src-fip-015, src-fip-023 | specialized workup boundary, not generic assay leadership |
| FR5 | Supportive diagnosis remains composite: risk, clinicopathology, lower laboratory support, molecular support, and branch-specific tests do not all lead equally. | B | src-fip-003, src-fip-006, src-fip-015, src-fip-023 | order rule, not treatment or regulatory guidance |

## Evidence-Depth Caveat

This page sits on a fully deep-extracted FIP source-card layer (24/24 papers). Key anchors: modern broad review (`src-fip-003`), Australian risk-factor study (`src-fip-005`), multi-cat endemic-risk study (`src-fip-008`), breed-prevalence study (`src-fip-012`), VMTH epidemiology (`src-fip-020`), Sydney clinicopathology series (`src-fip-006`), Taiwan clinicopathology/staging series (`src-fip-015`), effusive immunology (`src-fip-007`), and CSF neurologic-extension study (`src-fip-023`). This is now a recognition handbook rather than a routing page.

## Core Takeaway

FIP recognition is an order problem. Risk context raises the index of suspicion, but clinicopathology and disease form lead the actual recognition frame; mutation or CSF support should strengthen a case only after the relevant suspicion or neurologic branch has already been established.

## Recognition Architecture

### Core Recognition Frame

Read FIP recognition as a sequence:

1. risk context can raise concern earlier
2. clinicopathology and disease form turn concern into structured suspicion
3. bounded laboratory and molecular support strengthen an already suspicious case
4. neurologic or ocular signs shift the case into a specialized branch
5. treatment response stays downstream and should not rewrite first-pass recognition

**Lead sources:** `src-fip-003`, `src-fip-006`, `src-fip-015`

### Risk Context

Young age, patterned breed signals, male over-representation, endemic multi-cat coronavirus exposure, and referral-population enrichment all matter as risk context. They are recognition accelerants, not disease proof.

**Lead sources:** `src-fip-005`, `src-fip-008`, `src-fip-012`, `src-fip-020`

**Current safe read:**
- signalment and environment can move FIP higher on the differential list
- risk-factor evidence should not outrank clinical pattern recognition
- breed and institutional signals are context-specific enrichment layers

### Clinicopathology And Disease Form

Clinicopathologic case-series evidence makes practical recognition stronger than a vague variable-disease summary. Wet/dry form, effusion-aware suspicion, and staged disease-form description should shape the workup early.

**Lead sources:** `src-fip-006`, `src-fip-007`, `src-fip-015`

**Current safe read:**
- clinicopathology is the lead operational recognition layer
- effusion is a high-value suspicion feature but not diagnostic closure
- non-effusive disease should remain visible in the recognition architecture

### Neurologic And Ocular Branch Shift

Neurologic or ocular signs change the workup category. CSF support becomes central only after that category shift, and a negative CSF result should not broadly exclude FIP.

**Lead sources:** `src-fip-015`, `src-fip-023`

**Current safe read:**
- neurologic FIP is a branch shift, not just more severe ordinary FIP
- CSF RT-PCR can strongly support the neurologic/ocular branch when positive
- CSF specificity must not backflow into generic workup leadership

### Supportive Diagnosis Boundary

FIP recognition should stay under a composite-support frame. Lower laboratory context, mutation-related support, and specialized assays all matter, but none should flatten the recognition sequence into a single-test story.

**Lead sources:** `src-fip-003`, `src-fip-010`, `src-fip-022`, `src-fip-023`

**Current safe read:**
- molecular support follows suspicion
- support channels do not all lead equally
- recognition pages should block assay-leaderboard drift

## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-fip-003 | broad review: non-specific findings and supportive-diagnosis frame | deep_extracted |
| src-fip-005 | Australian signalment and breed-risk anchor | deep_extracted |
| src-fip-006 | Sydney clinicopathology pattern-recognition anchor | deep_extracted |
| src-fip-007 | effusive immunopathology context | deep_extracted |
| src-fip-008 | multi-cat endemic coronavirus risk context | deep_extracted |
| src-fip-012 | breed-prevalence enrichment anchor | deep_extracted |
| src-fip-015 | Taiwan clinicopathology and staging anchor | deep_extracted |
| src-fip-020 | VMTH epidemiology and referral-population burden | deep_extracted |
| src-fip-023 | neurologic/ocular CSF support-test boundary | deep_extracted |

## Current Owner Memo

- [FIP diagnostic-workup memo](../../system/indexes/fip-diagnostic-workup-memo.md)
- [FIP support-order memo](../../system/indexes/fip-support-order-memo.md)
- [FIP clinicopathology memo](../../system/indexes/fip-clinicopathology-memo.md)
- [FIP risk epidemiology memo](../../system/indexes/fip-risk-epidemiology-memo.md)
- [FIP neurologic-workup branch-boundary memo](../../system/indexes/fip-neurologic-workup-branch-boundary-memo.md)

## Guardrail

Do not let recognition collapse into either risk-factor screening or assay ranking. Risk context starts attention, clinicopathology and disease form lead suspicion, and branch-specific tests stay downstream of the branch that makes them relevant.

## What The Module Can Say Safely

- risk context and recognition logic are adjacent but distinct
- clinicopathology and disease form are the current lead recognition layer
- effusive and non-effusive forms should both stay visible
- neurologic/ocular signs change the workup branch before CSF support takes priority

## What The Module Should Not Say Yet

- do not treat breed, age, sex, household, or referral context as diagnosis
- do not say effusion alone proves FIP
- do not use CSF RT-PCR as the best general FIP diagnostic test
- do not use treatment response to rewrite first-pass recognition order

## Current Role

Use this page as the FIP recognition handbook. The source-card layer is complete at 24/24 deep-extracted papers. Next gains come from full-text precision where clinicopathology tables, disease-form checklists, or non-CSF assay performance detail would change branch order.
