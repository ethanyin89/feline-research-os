---
id: topic-ckd-endpoint
type: topic
topic: ckd
species: feline
disease: CKD
question_type: endpoint
source_ids: [src-ckd-001, src-ckd-002, src-ckd-003, src-ckd-004, src-ckd-006, src-ckd-007, src-ckd-010, src-ckd-013, src-ckd-015, src-ckd-017, src-ckd-018, src-ckd-020, src-ckd-024]
last_compiled_at: 2026-05-06
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
language_qa_notes: "2026-05-06 recompiled to handbook status against 24/24 deep-extracted source-card layer."
owner: codex
status: active
---

# Feline CKD Endpoint Handbook

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| CE1 | Core operational CKD endpoints are creatinine, USG, UPCR, systolic blood pressure, and phosphorus; these bridge diagnosis, monitoring, and prognosis | B | src-ckd-004, src-ckd-010 | operational core, not exhaustive outcome set |
| CE2 | Different endpoints map to different structural lesion patterns: fibrosis-linked vs glomerulo-vascular injury-linked | B | src-ckd-010 | multi-axis interpretation, not one flat severity score |
| CE3 | Serial surveillance and creatinine trend from baseline are part of endpoint logic, not just follow-up housekeeping | B | src-ckd-004 | diagnostic method, not optional monitoring |
| CE4 | SDMA is an adjunctive early-detection aid, not a standalone screening replacement for the diagnostic core | B | src-ckd-004, src-ckd-024 | support marker, not replacement |
| CE5 | Phosphorus may stay normal early despite phosphate retention; PTH has a role as hidden-mineral-burden interpreter | B | src-ckd-006, src-ckd-015 | mineral-burden context, not single-marker closure |
| CE6 | Trial outcomes should minimally cover 29 parameters grouped into 9 core themes; this is trial breadth, not universal endpoint priority | C | src-ckd-013 | trial architecture, not clinical endpoint ranking |

## Evidence-Depth Caveat

This page sits on a fully deep-extracted CKD source-card layer (24/24 papers). Key anchors: ISFM guideline (`src-ckd-004`), histomorphometry correlation study (`src-ckd-010`), phosphorus-control review (`src-ckd-006`), CKD-MBD review (`src-ckd-015`), biomarker review (`src-ckd-024`), proteinuric kidney disease study (`src-ckd-017`), and core outcome set paper (`src-ckd-013`). This is now an endpoint handbook rather than a routing page.

## Core Takeaway

CKD endpoints should be understood in three layers: (1) core operational endpoints (creatinine, USG, UPCR, SBP, phosphorus), (2) early-detection support markers (SDMA), and (3) context markers (PTH, calcium, FGF23, anaemia, potassium). Different endpoints map to different structural lesion patterns. Serial surveillance is part of endpoint logic. Proteinuria, phosphorus, and blood pressure are cross-layer progression variables, not just monitoring numbers.

## Endpoint Hierarchy

### Core Tier: Operational CKD Endpoints

**Endpoint 1: Creatinine**

Primary use: diagnosis, staging, longitudinal monitoring. In practice, CKD diagnosis uses increased serum creatinine >140 µmol/l with persistence over time. A persistent increase >15% from baseline may indicate reduced renal function.

**Key boundary:** Rises relatively late, influenced by muscle mass. Not ideal for earliest detection.

**Lead sources:** `src-ckd-002`, `src-ckd-004`, `src-ckd-010`

**Endpoint 2: USG (Urine Specific Gravity)**

Primary use: diagnostic confirmation, context for azotemia. Inadequately concentrated urine (USG <1.035) combined with creatinine elevation supports CKD diagnosis.

**Key boundary:** Essential but not sufficient by itself for earliest detection.

**Lead sources:** `src-ckd-002`, `src-ckd-004`

**Endpoint 3: UPCR / Proteinuria**

Primary use: prognosis, substaging, progression interpretation, treatment targeting. Proteinuria is associated with interstitial fibrosis and glomerular hypertrophy. Major progression-linked factor.

**Key boundary:** Interpretation requires compartment awareness (primary glomerular vs broader CKD), blood-pressure context, and non-renal confounder exclusion.

**Lead sources:** `src-ckd-001`, `src-ckd-004`, `src-ckd-010`, `src-ckd-017`

**Endpoint 4: Systolic Blood Pressure**

Primary use: substaging, risk management, target-organ protection, progression context. Higher time-averaged SBP correlates with glomerulosclerosis and hyperplastic arteriolosclerosis. Prevalence of hypertension in CKD cats: 20-65%.

**Key boundary:** Under-measured in practice. Should be interpreted as repeated hemodynamic signal, not one-visit snapshot. Target <160 mmHg to minimize TOD risk.

**Lead sources:** `src-ckd-004`, `src-ckd-007`, `src-ckd-009`, `src-ckd-010`

**Endpoint 5: Phosphorus**

Primary use: monitoring, prognosis, progression control, treatment targeting. Each one-unit serum phosphorus increase was associated with 11.8% increased risk of death. Interstitial fibrosis is linked to hyperphosphatemia.

**Key boundary:** May stay normal early despite phosphate retention (PTH compensation). Should not be read in isolation from PTH context.

**Lead sources:** `src-ckd-003`, `src-ckd-004`, `src-ckd-006`, `src-ckd-010`

### Support Tier: Early-Detection Markers

**Endpoint 6: SDMA**

Primary use: early detection support, adjunct monitoring. Appears more sensitive than creatinine for early CKD detection, less affected by muscle mass.

**Key boundary:** Cannot currently be recommended as a single screening test. Useful adjunct, not standalone replacement.

**Lead sources:** `src-ckd-002`, `src-ckd-004`, `src-ckd-018`, `src-ckd-024`

**Endpoint 7: GFR**

Primary use: ideal early dysfunction detection reference. Gold standard for renal function assessment.

**Key boundary:** Practical limitations prevent routine use. Reference concept rather than routine working endpoint.

**Lead sources:** `src-ckd-002`, `src-ckd-004`, `src-ckd-024`

### Context Tier: Interpretation and Management Markers

**Endpoint 8: PTH**

Primary use: secondary hyperparathyroidism context, phosphate-retention interpretation, CKD-MBD framing. Increased PTH despite serum phosphorus remaining in range can indicate early mineral burden.

**Key boundary:** Important biologically; better as context than first-wave routine endpoint.

**Lead sources:** `src-ckd-006`, `src-ckd-015`

**Endpoint 9: Calcium / CKD-MBD Markers (FGF23)**

Primary use: mineral-management caution, calcification context. Cats with CKD have increased risk of total hypercalcaemia. FGF23 increases before azotaemic CKD.

**Key boundary:** Clinically relevant branch, but not yet first-wave routine endpoint.

**Lead sources:** `src-ckd-015`

**Endpoint 10: Anaemia**

Primary use: burden/progression context, treatment context. Interstitial fibrosis correlates with anaemia severity.

**Key boundary:** Important but currently context variable, not lead endpoint.

**Lead sources:** `src-ckd-003`, `src-ckd-010`

**Endpoint 11: Imaging (Renal Ultrasonography)**

Primary use: structural workup context, renal differential support. Reference imaging modality for feline kidney.

**Key boundary:** Important for structural context; diffuse changes harder to characterize than focal/multifocal disease. Not standalone CKD-defining endpoint.

**Lead sources:** `src-ckd-004`, `src-ckd-020`

## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-ckd-004 | ISFM guideline: diagnostic criteria, minimum workup, staging, surveillance | deep_extracted |
| src-ckd-010 | histomorphometry: lesion-marker correlations, multi-axis interpretation | deep_extracted |
| src-ckd-006 | phosphorus-control: hyperparathyroidism context, survival association | deep_extracted |
| src-ckd-015 | CKD-MBD: calcium disorders, FGF23, wider mineral frame | deep_extracted |
| src-ckd-017 | proteinuric kidney disease: compartment-aware proteinuria interpretation | deep_extracted |
| src-ckd-013 | core outcome set: minimum trial breadth (29 parameters, 9 themes) | deep_extracted |
| src-ckd-024 | biomarker review: SDMA, creatinine limitations, UPC specificity | deep_extracted |

## Endpoint Matrix by Use Case

| Use Case | Prioritize | Notes |
|---|---|---|
| **Diagnosis/Staging** | creatinine, USG, creatinine trend, UPCR, SDMA (support) | persistence over time required |
| **Progression/Prognosis** | UPCR, SBP, phosphorus, creatinine trend | proteinuria and SBP are cross-layer progression variables |
| **Treatment/Efficacy** | phosphorus, proteinuria, SBP, creatinine trend, context endpoints | depends on intervention class |
| **Early Detection** | serial surveillance, creatinine trend, USG, SDMA (adjunct), GFR (reference) | age-based surveillance is key |

## Multi-Axis Structural Mapping

The histomorphometry study (`src-ckd-010`) established that different endpoints carry different structural meanings:

| Endpoint Group | Associated Lesions | Clinical Implication |
|---|---|---|
| Creatinine, phosphorus, anaemia | Interstitial fibrosis | Core fibrosis-linked burden markers |
| Proteinuria | Interstitial fibrosis + glomerular hypertrophy | Progression-relevant, structural bridge |
| Systolic blood pressure | Glomerulosclerosis + hyperplastic arteriolosclerosis | Glomerulo-vascular injury signal |

This supports multi-axis endpoint interpretation rather than collapsing all markers into one severity score.

## Guardrail

Do not treat all endpoints as interchangeable. The safe architecture is:

1. **Core operational tier:** creatinine, USG, UPCR, SBP, phosphorus
2. **Support tier:** SDMA (adjunctive, not standalone)
3. **Context tier:** PTH, calcium, FGF23, anaemia, imaging
4. **Multi-axis interpretation:** different markers → different lesion patterns
5. **Serial surveillance:** part of endpoint logic, not optional follow-up

## What The Module Can Say Safely

- Not all endpoints do the same job; distinguish operational, support, and context tiers
- Serial surveillance and creatinine trend are part of diagnostic methodology
- Proteinuria, phosphorus, and blood pressure are cross-layer progression variables, not just monitoring numbers
- Different endpoints map to different structural lesion patterns (fibrosis-linked vs glomerulo-vascular)
- SDMA is an adjunctive support marker, not a standalone screening replacement
- Phosphorus may stay normal early despite phosphate retention; PTH helps interpret hidden mineral burden
- Trial outcome architecture (29 parameters, 9 themes) is separate from routine endpoint priority

## What The Module Should Not Say Yet

- do not treat all endpoints as interchangeable severity readouts
- do not position SDMA as a universal standalone screening shortcut
- do not ignore PTH context when interpreting phosphorus
- do not confuse imaging workup context with lead efficacy endpoints
- do not collapse trial minimum breadth into universal endpoint ranking

## Current Role

Use this page as the CKD endpoint handbook. The source-card layer is complete at 24/24 deep-extracted papers. Next gains come from tighter lesion-specific endpoint mapping and clearer trial-vs-routine endpoint distinction in product-specific contexts.
