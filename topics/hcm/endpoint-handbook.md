---
id: topic-hcm-endpoint
type: topic
topic: hcm
species: feline
disease: HCM
question_type: endpoint
source_ids: [src-hcm-006, src-hcm-009, src-hcm-010, src-hcm-013, src-hcm-017, src-hcm-019, src-hcm-023, src-hcm-024]
last_compiled_at: 2026-05-06
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline HCM Endpoint Handbook

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FE1 | HCM endpoint logic should be a hierarchy led by structural confirmation, not a flat biomarker ranking. | B | src-hcm-009, src-hcm-013 | endpoint placement, not complete diagnostic protocol |
| FE2 | Troponin I is best read as injury / burden pressure, not structural phenotype definition. | B | src-hcm-006 | moderate-to-severe signal, not mild-screening authority |
| FE3 | NT-proBNP is useful for severe-disease flagging but is not a reliable mild-to-moderate HCM screen in the studied colony. | B | src-hcm-010 | screening augmentation, not confirmation |
| FE4 | Novel biomarkers and AI widen endpoint architecture while remaining below routine structural confirmation. | C | src-hcm-017, src-hcm-023 | frontier / augmentation only |
| FE5 | Right-ventricular involvement and pathology staging deepen phenotype and severity architecture without changing frontline recognition authority. | B | src-hcm-019, src-hcm-024 | phenotype-depth, not first-pass replacement |

## Evidence-Depth Caveat

This page sits on a fully deep-extracted HCM source-card layer (24/24 papers). Key anchors: echocardiographic phenotype (`src-hcm-009`), gross morphometry (`src-hcm-013`), troponin I (`src-hcm-006`), NT-proBNP (`src-hcm-010`), novel biomarkers (`src-hcm-017`), AI diagnosis (`src-hcm-023`), right-ventricular involvement (`src-hcm-019`), and anatomopathological staging (`src-hcm-024`). This is now an endpoint handbook rather than a routing page.

## Core Takeaway

HCM endpoints should be ordered as structural confirmation -> screening augmentation -> injury/severity interpretation -> pathology-depth and phenotype-depth. Biomarkers, AI, and frontier markers are useful only when their use cases are kept separate from phenotype definition.

## Endpoint Hierarchy

### Endpoint 1: Structural Confirmation

Echocardiographic phenotype and gross morphometry are the lead operational endpoint layer. Structural heterogeneity is part of the phenotype, so HCM should not be reduced to one wall-thickness shortcut.

**Key boundary:** structural confirmation leads, but mild or equivocal thickening still needs exclusion-aware interpretation.

**Lead sources:** `src-hcm-009`, `src-hcm-013`

### Endpoint 2: Severe-Disease Screening Augmentation

NT-proBNP belongs in screening augmentation, with stronger signal for severe disease and a clear boundary against mild-to-moderate screening authority.

**Key boundary:** severe-disease flagging, not reliable mild-disease screening or confirmation.

**Lead sources:** `src-hcm-010`

### Endpoint 3: Injury / Burden Signal

Troponin I helps read myocardial injury and disease burden. Its signal in moderate-to-severe HCM and active congestive heart failure should not be turned into structural phenotype definition.

**Key boundary:** injury/severity interpretation, not phenotype definition.

**Lead sources:** `src-hcm-006`

### Endpoint 4: Frontier Biomarkers And AI Augmentation

Novel biomarkers and AI add frontier or augmentation pressure. They deepen the endpoint stack but should remain below routine structure-first authority until operational and validation boundaries are stronger.

**Key boundary:** potential stratification or routing support, not routine confirmation.

**Lead sources:** `src-hcm-017`, `src-hcm-023`

### Endpoint 5: Phenotype-Depth And End-Stage Architecture

Right-ventricular involvement and anatomopathological staging widen severity architecture. They help explain remodeled and advanced disease without replacing first-pass structural recognition.

**Key boundary:** phenotype-depth and advanced-disease interpretation, not first-wave diagnostic leadership.

**Lead sources:** `src-hcm-019`, `src-hcm-024`

## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-hcm-006 | troponin I injury / burden endpoint | deep_extracted |
| src-hcm-009 | echocardiographic structural phenotype anchor | deep_extracted |
| src-hcm-010 | NT-proBNP severe-signal and screening boundary | deep_extracted |
| src-hcm-013 | gross morphometry discrimination anchor | deep_extracted |
| src-hcm-017 | frontier biomarker branch | deep_extracted |
| src-hcm-019 | right-ventricular phenotype-depth anchor | deep_extracted |
| src-hcm-023 | AI augmentation endpoint branch | deep_extracted |
| src-hcm-024 | end-stage pathology and remodeling-depth anchor | deep_extracted |

## Current Owner Memo

- [HCM endpoint separation memo](../../system/indexes/hcm-endpoint-separation-memo.md)
- [HCM biomarker use-case memo](../../system/indexes/hcm-biomarker-use-case-memo.md)
- [HCM frontier augmentation memo](../../system/indexes/hcm-frontier-augmentation-memo.md)
- [HCM AI augmentation boundary memo](../../system/indexes/hcm-ai-augmentation-boundary-memo.md)
- [HCM phenotype-remodeling bridge memo](../../system/indexes/hcm-phenotype-remodeling-bridge-memo.md)

## Guardrail

Do not produce a flat HCM endpoint ranking that treats echo, gross morphometry, troponin, NT-proBNP, novel biomarkers, AI, RV involvement, and pathology staging as interchangeable diagnostic tools. The current source layer supports hierarchy placement better than universal ranking.

## What The Module Can Say Safely

- structural confirmation is the lead endpoint layer
- NT-proBNP is bounded screening augmentation, strongest for severe disease
- troponin I is injury and burden pressure rather than phenotype definition
- novel biomarkers and AI are frontier or augmentation layers
- RV involvement and pathology staging deepen phenotype and severity interpretation

## What The Module Should Not Say Yet

- do not promote NT-proBNP into reliable mild-disease screening language
- do not promote troponin into structural confirmation authority
- do not treat AI as routine first-wave confirmation
- do not treat pathology-depth endpoints as routine front-door diagnosis

## Current Role

Use this page as the HCM endpoint handbook. The source-card layer is complete at 24/24 deep-extracted papers. Next gains come from output-specific ranking where a concrete screening, biomarker, AI, or severity question requires narrower full-text comparison.
