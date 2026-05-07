---
id: topic-diabetes-diagnostic-monitoring-workup
type: topic
topic: diabetes
species: feline
disease: diabetes mellitus
question_type: recognition
source_ids: [src-diabetes-005, src-diabetes-010, src-diabetes-013, src-diabetes-014, src-diabetes-020, src-diabetes-021, src-diabetes-024, src-reg-012, src-reg-013]
last_compiled_at: 2026-04-24
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline Diabetes Diagnostic And Monitoring Workup

## Question This Page Answers

How should diabetes recognition, workup, treatment candidacy, and monitoring questions be routed?

## Core Takeaway

Feline diabetes workup should be structured as diagnosis confirmation plus branch gating: default type-2-like disease, body-condition state, secondary endocrine disease, pancreatitis/DKA complexity, treatment candidacy, and monitoring intensity.

## Workup Layers

| Layer | Route To | Current Role | Boundary |
|---|---|---|---|
| Confirm diabetes and baseline context | [src-diabetes-014](../../raw/papers/src-diabetes-014.md), [src-diabetes-021](../../raw/papers/src-diabetes-021.md) | Basic disease framing and clinical context. | Do not promote exact diagnostic criteria without full-text or guideline support. |
| Body condition and presentation state | [obesity and body condition](obesity-and-body-condition.md) | Separates obesity history from current weight/muscle state. | Do not treat every diabetic cat as currently overweight. |
| Secondary endocrine gate | [endocrine secondary diabetes](endocrine-secondary-diabetes.md) | Preserves hypersomatotropism/acromegaly and other endocrine causes. | Do not provide a full screening algorithm from the current compiled layer alone. |
| Pancreatitis / DKA complexity | [pancreatitis comorbidity](pancreatitis-comorbidity.md) | Routes bidirectional comorbidity and DKA-complexity questions. | Do not claim settled one-way causality. |
| Treatment candidacy | [treatment branch map](treatment-branch-map.md), [SGLT2 label control](sglt2-label-control.md) | Separates route, endpoint, and safety boundaries. | Do not treat oral route as automatically safer or preferable. |
| Monitoring intensity | [endpoint handbook](endpoint-handbook.md), [complications neuropathy](complications-neuropathy.md) | Keeps glycemic, remission, body-condition, safety, and complication endpoints distinct. | Do not promote a final monitoring schedule without deeper evidence. |

## Routing Table

| If The Question Is About | Route To | Do Not Route To |
|---|---|---|
| basic disease framing | `src-diabetes-014`, `src-diabetes-021` | treatment ranking |
| body condition / obesity | [obesity and body condition](obesity-and-body-condition.md) | generic lifestyle note |
| difficult control / high insulin need | [endocrine secondary diabetes](endocrine-secondary-diabetes.md) | default type-2-only frame |
| pancreatitis / DKA complexity | [pancreatitis comorbidity](pancreatitis-comorbidity.md) | one-way causality claim |
| SGLT2 candidacy | [SGLT2 label control](sglt2-label-control.md) | route convenience |
| remission | [remission boundaries](remission-boundaries.md) | single-protocol promise |
| neuropathy | [complications neuropathy](complications-neuropathy.md) | treatment efficacy claim |

## Guardrail

This is a vault architecture page, not an owner-facing diagnostic checklist, dosing protocol, or substitute for veterinary judgment.
