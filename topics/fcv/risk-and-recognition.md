---
id: topic-fcv-risk-and-recognition
type: topic
topic: fcv
species: feline
disease: feline calicivirus infection
question_type: recognition
source_ids: [src-fcv-001, src-fcv-004, src-fcv-005, src-fcv-006, src-fcv-009, src-fcv-020, src-fcv-021, src-fcv-024]
last_compiled_at: 2026-04-30
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline FCV Risk And Recognition

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FRR1 | FCV recognition should start from oral/upper-respiratory suspicion, but not stop there | B | src-fcv-004, src-fcv-009 | recognition architecture, not diagnostic rule |
| FRR2 | Healthy shedding and co-pathogen structure block symptom-only diagnosis of FCV | B | src-fcv-005, src-fcv-006 | not prevalence generalization outside study settings |
| FRR3 | Ocular and possible enteric findings are real extension branches, but should not replace the core respiratory/oral recognition frame | B | src-fcv-020, src-fcv-021 | extension-branch control only |
| FRR4 | Vaccine failure and apparent resistance require molecular interpretation, not narrative closure | B | src-fcv-024 | sequence-epidemiology, not product ranking |
| FRR5 | Regional strain distribution affects both recognition and vaccine-fit assessment | B | src-fcv-005, src-fcv-024 | epidemiology boundary |

## Evidence-Depth Caveat

This page sits on a fully deep-extracted FCV source-card layer (24/24 papers). Key recognition anchors: practical guideline (`src-fcv-004`), diagnosis/control bridge (`src-fcv-009`), modern shell review (`src-fcv-001`), field recognition study (`src-fcv-006`), regional epidemiology (`src-fcv-005`), ocular extension (`src-fcv-021`), enteric extension (`src-fcv-020`), and sequence-epidemiology/vaccine-failure boundary (`src-fcv-024`). This is now a recognition handbook rather than a routing page.

## Core Takeaway

FCV recognition stays composite: oral and upper-respiratory disease are core, but healthy shedding, co-pathogens, regional strain variation, ocular disease, and possible enteric extension prevent one-symptom or one-test diagnosis.

## Recognition Architecture

### Core Recognition Frame

FCV recognition starts from oral ulceration and upper-respiratory disease clustering together. The classic syndrome includes sneezing, nasal discharge, conjunctivitis, and oral ulcers. However, FCV-suspect signs are not the same as FCV confirmation.

**Lead sources:** `src-fcv-004`, `src-fcv-009`

### Diagnostic Testing

RT-PCR is the best detection tool, but interpretation requires caution:

- negative results do not exclude infection
- healthy cats may test positive (carrier state)
- detection does not equal causation in symptomatic cases
- PCR should be written as `best-but-bounded`, not as one-test closure

**Lead sources:** `src-fcv-006`, `src-fcv-009`

### Carrier State and Healthy Shedding

Healthy cats can shed FCV. This creates a fundamental recognition problem: a positive PCR in a symptomatic cat does not prove FCV caused the symptoms.

Key finding from `src-fcv-006`: fewer than half of practitioner-judged FCV-suspect cats were FCV-positive. Oral-disease-heavy findings carry more weight than a flat classical-URTD symptom list.

**Lead sources:** `src-fcv-005`, `src-fcv-006`

### Co-Pathogen Structure

Symptomatic respiratory presentations often involve co-pathogens. Co-pathogen structure must be preserved in recognition thinking rather than defaulting to FCV-alone causation.

**Lead sources:** `src-fcv-006`

### Regional Strain Variation

Strain distribution and vaccine fit may vary by region. Geography-specific epidemiology affects both recognition and vaccine-break interpretation.

**Lead sources:** `src-fcv-005`, `src-fcv-024`

### Extension Branches

**Ocular:** FCV can cause ocular-surface disease. This branch should remain syndrome-aware and co-pathogen-aware rather than becoming a first-line diagnostic shortcut.

**Enteric:** Enteric FCV association is visible in differential thinking but should not become a lead-cause shortcut without stronger clinical-routing evidence.

**Lead sources:** `src-fcv-020`, `src-fcv-021`

## Working Recognition Order

1. Suspect FCV when oral ulceration and upper-respiratory disease cluster together
2. Keep carriage and healthy shedding in view before overcalling causality
3. Actively preserve co-pathogen structure in respiratory cases
4. Route ocular and enteric signals as extension branches, not first-line proof
5. Consider regional strain distribution when interpreting vaccine-break cases

## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-fcv-001 | modern shell review: commonness, variability, recognition caution | deep_extracted |
| src-fcv-004 | practical guideline: carrier-aware diagnostic caution, supportive control | deep_extracted |
| src-fcv-005 | regional epidemiology: geography-specific strain distribution, vaccine locality | deep_extracted |
| src-fcv-006 | field recognition: symptomatic vs healthy comparison, co-pathogen structure | deep_extracted |
| src-fcv-009 | diagnosis/control bridge: PCR-best-but-bounded, carrier-state interpretation | deep_extracted |
| src-fcv-020 | enteric extension: differential visibility without lead-cause authority | deep_extracted |
| src-fcv-021 | ocular extension: syndrome-aware, co-pathogen-aware | deep_extracted |
| src-fcv-024 | sequence-epidemiology: vaccine-failure molecular interpretation | deep_extracted |

## Current Owner Memo

- [FCV recognition architecture memo](../../system/indexes/fcv-recognition-architecture-memo.md)

## Guardrail

Do not convert FCV recognition into a one-sign or one-test page. The safe architecture is:

1. Suspicion first (oral/respiratory cluster)
2. Composite interpretation second (PCR bounded by carrier-state and co-pathogen logic)
3. Extension branches third (ocular, enteric as visible but secondary)
4. Regional context fourth (strain distribution affects vaccine-break interpretation)

## What The Module Can Say Safely

- FCV-suspect is not the same as FCV-confirmed
- healthy cats can shed FCV
- co-pathogens matter in symptomatic presentations
- ocular and enteric branches are real but secondary
- vaccine-failure cases need molecular interpretation, not narrative closure

## What The Module Should Not Say Yet

- do not claim prevalence generalizations outside study settings
- do not reduce recognition to one sign or one test
- do not let extension branches replace core oral/respiratory framing
- do not interpret vaccine-break cases without sequence context

## Current Role

Use this page as the FCV recognition handbook. The source-card layer is complete at 24/24 deep-extracted papers. Next gains come from tighter audience-specific compression (owner vs clinician workup).
