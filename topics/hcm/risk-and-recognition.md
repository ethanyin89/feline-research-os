---
id: topic-hcm-risk-recognition
type: topic
topic: hcm
species: feline
disease: HCM
question_type: recognition
source_ids: [src-hcm-001, src-hcm-002, src-hcm-008, src-hcm-009, src-hcm-010, src-hcm-012, src-hcm-013, src-hcm-021, src-hcm-023, src-hcm-024]
last_compiled_at: 2026-05-06
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline HCM Risk And Recognition

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FR1 | HCM recognition should stay structure-first: echocardiographic phenotype and gross morphometry outrank biomarker-only or AI-only logic. | B | src-hcm-001, src-hcm-009, src-hcm-013 | recognition hierarchy, not full diagnostic protocol |
| FR2 | Mild to moderate hypertrophy remains exclusion-aware, while severe HCM is more directly echo-recognizable. | B | src-hcm-001, src-hcm-008 | clinical interpretation boundary, not single-measure certainty |
| FR3 | NT-proBNP and AI belong in bounded screening or routing augmentation, not phenotype-definition authority. | B | src-hcm-010, src-hcm-023 | augmentation, not replacement |
| FR4 | Genotype and age modify interpretation, but mutation-positive status does not equal current phenotype confirmation. | B | src-hcm-012 | risk modifier, not standalone diagnosis |
| FR5 | HCM should remain inside a broader feline cardiomyopathy frame so other myocardial phenotypes are not erased. | B | src-hcm-021 | boundary awareness, not full cardiomyopathy atlas |

## Evidence-Depth Caveat

This page sits on a fully deep-extracted HCM source-card layer (24/24 papers). Key anchors: broad HCM review/update sources (`src-hcm-001`, `src-hcm-002`, `src-hcm-008`), echocardiographic phenotype study (`src-hcm-009`), morphometry study (`src-hcm-013`), NT-proBNP screening study (`src-hcm-010`), genotype-severity study (`src-hcm-012`), myocardial-disease classification review (`src-hcm-021`), AI diagnosis paper (`src-hcm-023`), and pathology staging (`src-hcm-024`). This is now a recognition handbook rather than a routing page.

## Core Takeaway

HCM recognition is a hierarchy: cardiomyopathy-aware suspicion leads into structural phenotype confirmation; biomarkers, AI, genotype, and age sharpen interpretation but should not replace structure-first confirmation.

## Recognition Architecture

### Core Recognition Frame

Read first-pass HCM recognition in this order:

1. cardiomyopathy-aware suspicion
2. structural phenotype confirmation
3. bounded screening augmentation
4. genotype- and age-aware interpretation
5. broader cardiomyopathy boundary awareness

**Lead sources:** `src-hcm-001`, `src-hcm-008`, `src-hcm-021`

### Structural Phenotype Confirmation

Echocardiographic structure and gross morphometry are the lead operational branch. HCM phenotype is heterogeneous, and severe HCM is easier to confirm than mild-to-moderate or equivocal thickening.

**Lead sources:** `src-hcm-001`, `src-hcm-009`, `src-hcm-013`

**Current safe read:**
- phenotype definition should remain structural
- segmental and diffuse hypertrophy patterns both matter
- mild-to-moderate hypertrophy should stay exclusion-aware

### Screening Augmentation

NT-proBNP can flag severe disease burden but should not be written as a reliable mild-to-moderate screen. AI evidence adds a computational augmentation branch, especially for routing or support, but does not outrank structural workup.

**Lead sources:** `src-hcm-010`, `src-hcm-023`

**Current safe read:**
- augmentation can help suspicion and routing
- severe-disease signal is not the same as broad screening competence
- AI authority inherits the limits of its input data and validation setting

### Genotype- And Age-Aware Interpretation

Genotype pressure matters, especially where MYBPC3 p.A31P dosage and age-related penetrance shape severity and development. This branch modifies interpretation rather than replacing phenotype confirmation.

**Lead sources:** `src-hcm-012`

**Current safe read:**
- homozygous and heterozygous states should not be flattened
- age-related penetrance keeps genotype interpretation time-dependent
- mutation status is not immediate current-phenotype certainty

### Cardiomyopathy Boundary Awareness

HCM is the strongest current cardiomyopathy branch in the vault, but feline myocardial disease is broader than HCM. Recognition should keep that outer frame visible.

**Lead sources:** `src-hcm-021`

**Current safe read:**
- HCM is common and central, but not the entire feline myocardial-disease map
- classification context prevents over-HCM-centered routing
- non-HCM cardiomyopathy material belongs as adjacent boundary context

## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-hcm-001 | modern HCM review: echo-led recognition and biomarker-isolation warning | deep_extracted |
| src-hcm-002 | historical broad-update context | deep_extracted |
| src-hcm-008 | recent clinical-diagnostic review with multimodal but structure-aware framing | deep_extracted |
| src-hcm-009 | echocardiographic phenotype heterogeneity anchor | deep_extracted |
| src-hcm-010 | NT-proBNP severe-signal and mild-screening boundary | deep_extracted |
| src-hcm-012 | genotype dosage and age-related penetrance | deep_extracted |
| src-hcm-013 | gross morphometry discrimination boundary | deep_extracted |
| src-hcm-021 | broader myocardial-disease classification and clinical presentation | deep_extracted |
| src-hcm-023 | AI diagnosis augmentation branch | deep_extracted |
| src-hcm-024 | pathology staging and end-stage remodeling depth | deep_extracted |

## Current Owner Memo

- [HCM diagnostic-workup memo](../../system/indexes/hcm-diagnostic-workup-memo.md)
- [HCM biomarker use-case memo](../../system/indexes/hcm-biomarker-use-case-memo.md)
- [HCM AI augmentation boundary memo](../../system/indexes/hcm-ai-augmentation-boundary-memo.md)
- [HCM cardiomyopathy-boundary memo](../../system/indexes/hcm-cardiomyopathy-boundary-memo.md)

## Guardrail

Do not let HCM recognition become biomarker-first, AI-first, or genotype-first. Those branches are useful because they sharpen the workup hierarchy, not because they replace structural phenotype confirmation.

## What The Module Can Say Safely

- HCM recognition should remain structure-first
- biomarkers and AI are bounded augmentation channels
- genotype and age modify interpretation below phenotype confirmation
- broader cardiomyopathy context should remain visible

## What The Module Should Not Say Yet

- do not treat NT-proBNP as a reliable mild-to-moderate HCM screening solution
- do not treat AI as routine first-wave diagnostic authority
- do not let genotype status replace structural confirmation
- do not collapse all feline myocardial disease into HCM

## Current Role

Use this page as the HCM recognition handbook. The source-card layer is complete at 24/24 deep-extracted papers. Next gains come from output-specific precision where screening, AI, or genotype claims need narrower operational ranking.
