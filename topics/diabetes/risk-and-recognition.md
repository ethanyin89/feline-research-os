---
id: topic-diabetes-risk-and-recognition
type: topic
topic: diabetes
species: feline
disease: diabetes mellitus
question_type: recognition
source_ids: [src-diabetes-005, src-diabetes-009, src-diabetes-010, src-diabetes-012, src-diabetes-013, src-diabetes-020, src-diabetes-023]
last_compiled_at: 2026-05-06
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline Diabetes Risk And Recognition

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FR1 | Diabetes recognition should not be reduced to hyperglycemia alone; body condition, secondary endocrine disease, pancreatitis/DKA complexity, and treatment candidacy all shape routing. | B | src-diabetes-005, src-diabetes-010, src-diabetes-013, src-diabetes-020 | architecture, not diagnostic checklist |
| FR2 | Obesity is a mechanism-linked risk branch, but current presentation may include weight and muscle loss. | B | src-diabetes-005 | body-condition gate, not universal weight-loss instruction |
| FR3 | Hypersomatotropism/acromegaly is the highest-priority named endocrine-secondary recognition branch. | B | src-diabetes-013, src-diabetes-020 | secondary gate, not full testing algorithm |
| FR4 | Pancreatitis is a frequent bidirectional comorbidity and DKA-complexity branch. | B | src-diabetes-010, src-diabetes-023 | comorbidity recognition, not causality proof |
| FR5 | Burmese breed-risk appears in UK and Australian data but must remain denominator-bound and population-level. | B | src-diabetes-009, src-diabetes-012 | risk context, not individual prediction or mechanism proof |

## Evidence-Depth Caveat

This page sits on a fully deep-extracted diabetes source-card layer (24/24 papers). Key anchors: obesity/body-condition source (`src-diabetes-005`), UK prevalence and risk-factor study (`src-diabetes-009`), Australian frequency/breed-risk study (`src-diabetes-012`), pancreatitis comorbidity review (`src-diabetes-010`), endocrine-secondary anchors (`src-diabetes-013`, `src-diabetes-020`), and comparative pancreatic disease/DKA context (`src-diabetes-023`). This is now a recognition handbook rather than a routing page.

## Core Takeaway

Diabetes recognition is a routing problem: confirm diabetes, then keep body-condition state, endocrine-secondary disease, pancreatitis/DKA complexity, breed/population risk, and treatment candidacy visible without converting any one branch into a patient-level prediction rule.

## Recognition Architecture

### Core Recognition Frame

First-pass recognition should route through diagnosis confirmation plus major gates: body condition, secondary endocrine disease, pancreatitis/DKA complexity, treatment candidacy, and monitoring intensity.

**Lead sources:** `src-diabetes-005`, `src-diabetes-010`, `src-diabetes-013`, `src-diabetes-020`

### Body-Condition Gate

Obesity increases insulin resistance and diabetes risk, but recognition must account for current presentation. Some cats present after weight and muscle loss, so stabilization may need to precede weight-loss framing.

**Lead sources:** `src-diabetes-005`

**Current safe read:**
- obesity is a central risk and mechanism branch
- body condition should be assessed as current state, not assumed history
- weight-loss language needs sequencing caveats

### Secondary Endocrine Gate

Hypersomatotropism/acromegaly and hyperadrenocorticism prevent a universal type-2-like interpretation. Difficult glycemic control, high insulin requirements, variable response, or unexpected non-remission should keep this gate open.

**Lead sources:** `src-diabetes-013`, `src-diabetes-020`

**Current safe read:**
- hypersomatotropism-induced diabetes is a major named secondary branch
- IGF1 is important but marginal values and insulin exposure complicate interpretation
- full screening algorithms need stronger guideline/full-text support

### Pancreatitis / DKA Complexity Gate

Pancreatitis and diabetes frequently coexist, and pancreatitis with DKA creates a higher-complexity recognition and management branch. The causal direction should remain cautious.

**Lead sources:** `src-diabetes-010`, `src-diabetes-023`

**Current safe read:**
- pancreatitis is management-complicating comorbidity
- DKA context should increase branch complexity
- cross-species pancreatic disease context stays secondary to feline-only anchors

### Breed And Population Risk Context

UK insured-population and Australian clinic-period data both support Burmese risk signal, but denominators differ. Breed risk is context for suspicion, not a mechanism or individual-cat prediction rule.

**Lead sources:** `src-diabetes-009`, `src-diabetes-012`

**Current safe read:**
- Burmese predisposition is visible across two population frames
- male sex, neuter status, inactivity, weight, and medication exposure remain denominator-bound signals
- population risk should not be written as individual certainty

## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-diabetes-005 | obesity/body-condition risk and sequencing gate | deep_extracted |
| src-diabetes-009 | UK insured-population prevalence and risk-factor signal | deep_extracted |
| src-diabetes-010 | pancreatitis bidirectional comorbidity and DKA complexity | deep_extracted |
| src-diabetes-012 | Australian frequency and Burmese predisposition anchor | deep_extracted |
| src-diabetes-013 | endocrine-secondary diabetes boundary | deep_extracted |
| src-diabetes-020 | hypersomatotropism-induced diabetes recognition pressure | deep_extracted |
| src-diabetes-023 | comparative pancreatic disease and DKA context | deep_extracted |

## Current Owner Memo

- [diabetes diagnostic monitoring workup memo](../../system/indexes/diabetes-diagnostic-monitoring-workup-memo.md)
- [diabetes obesity body-condition memo](../../system/indexes/diabetes-obesity-body-condition-memo.md)
- [diabetes endocrine-secondary diabetes memo](../../system/indexes/diabetes-endocrine-secondary-diabetes-memo.md)
- [diabetes pancreatitis comorbidity memo](../../system/indexes/diabetes-pancreatitis-comorbidity-memo.md)
- [diabetes breed-risk synthesis memo](../../system/indexes/diabetes-breed-risk-synthesis-memo.md)

## Guardrail

Do not turn risk factors into individual-cat prediction or owner-facing diagnostic instructions. This page routes recognition pressure; it does not replace diagnosis confirmation, comorbidity workup, or treatment-candidacy checks.

## What The Module Can Say Safely

- diabetes recognition should include body-condition and comorbidity gates
- obesity is a major risk branch but current body state can vary
- endocrine-secondary diabetes is a named high-priority branch
- pancreatitis/DKA complexity should remain visible
- Burmese risk is denominator-bound population context

## What The Module Should Not Say Yet

- do not reduce recognition to hyperglycemia alone
- do not treat every diabetic cat as currently overweight
- do not provide endocrine screening algorithms from this page alone
- do not turn breed-risk studies into patient-level prediction rules

## Current Role

Use this page as the diabetes recognition handbook. The source-card layer is complete at 24/24 deep-extracted papers. Next gains come from output-specific compression where diagnostic criteria, monitoring cadence, or treatment-candidacy gates need guideline-level detail.
