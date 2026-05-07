---
id: system-diabetes-diagnostic-monitoring-workup-memo
type: system
topic: diabetes
last_compiled_at: 2026-04-24
owner: codex
status: active
language: en
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
---

# Diabetes Diagnostic Monitoring Workup Memo

- Date: `2026-04-24`
- Scope: `src-diabetes-014`, `src-diabetes-021`, `src-diabetes-005`, `src-diabetes-010`, `src-diabetes-013`, `src-diabetes-020`, `src-diabetes-024`, `src-reg-012`, `src-reg-013`

This memo exists to define a workup architecture without pretending to be a clinical protocol.

## Core Takeaway

`feline diabetes workup should be structured as diagnosis confirmation plus branch gating: default type-2-like disease, body-condition state, secondary endocrine disease, pancreatitis/DKA complexity, treatment candidacy, and monitoring intensity`

## What This Memo Is Not

This is not:

- an owner-facing diagnostic checklist
- a dosing protocol
- a replacement for veterinary judgment
- a full guideline extraction

It is a vault architecture memo for deciding where claims belong.

## Workup Layer 1: Confirm Diabetes And Baseline Clinical Context

Main owners:

- [src-diabetes-014 deep extraction round 1](src-diabetes-014-deep-extraction-round1.md)
- [src-diabetes-021 deep extraction round 1](src-diabetes-021-deep-extraction-round1.md)

Current role:

- diabetes is common enough to need a full module
- type-2-like disease is the default frame in many cats
- diagnosis may be straightforward, but management is decision-heavy
- most cats may be insulin-dependent at diagnosis in older overview framing

Boundary:

- do not promote exact diagnostic criteria without full-text or guideline support

## Workup Layer 2: Body Condition And Presentation State

Main owner:

- [diabetes obesity body-condition memo](diabetes-obesity-body-condition-memo.md)

Current role:

- obesity contributes to insulin resistance and beta-cell demand
- current presentation may include weight and muscle loss
- stabilization, glycemic control, diet composition, and weight loss need staging

Boundary:

- do not treat every diabetic cat as currently overweight
- do not jump from obesity history to immediate caloric restriction

## Workup Layer 3: Secondary Endocrine Gate

Main owner:

- [diabetes endocrine-secondary diabetes memo](diabetes-endocrine-secondary-diabetes-memo.md)

Current role:

- type-2-like disease is the default, not the universal explanation
- hypersomatotropism/acromegaly and hyperadrenocorticism need a named branch
- difficult control, high insulin requirement, variable insulin response, or unexpected non-remission should route to secondary-endocrine thinking

Boundary:

- do not provide full IGF1 or confirmatory testing algorithms from the current compiled layer

## Workup Layer 4: Pancreatitis / DKA Complexity Gate

Main owner:

- [diabetes pancreatitis comorbidity memo](diabetes-pancreatitis-comorbidity-memo.md)

Current role:

- pancreatitis and diabetes frequently coexist
- the pathogenetic association is most safely represented as bidirectional
- pancreatitis can make diabetes and DKA management harder

Boundary:

- do not claim one-way causality
- do not provide pancreatitis diagnostic algorithm from the current compiled layer alone

## Workup Layer 5: Treatment Candidacy Gate

Main owners:

- [diabetes treatment branch comparison memo](diabetes-treatment-branch-comparison-memo.md)
- [diabetes SGLT2 current label control memo](diabetes-sglt2-current-label-control-memo.md)

Current role:

- treatment branches differ by candidate selection, endpoint, route, and safety boundary
- SGLT2 current labels preserve otherwise-healthy, insulin-naive boundaries
- insulin, diet, SGLT2, alpha-glucosidase adjunct, and frontier incretin branches should not be ranked as one ladder

Boundary:

- do not treat oral route as automatically safer, easier, or preferable
- do not use SGLT2 labels to make patient-specific treatment choices

## Workup Layer 6: Monitoring Intensity And Endpoint Selection

Main owners:

- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md)
- [diabetes remission boundary memo](diabetes-remission-boundary-memo.md)
- [diabetes neuropathy boundary memo](diabetes-neuropathy-boundary-memo.md)

Current role:

- monitoring includes glycemic control, insulin independence/remission-like endpoints, body condition, safety, and complications
- SGLT2 monitoring must include ketonuria / DKA / euglycemic DKA awareness
- neuropathy and microvascular pathology belong to the complication endpoint branch

Boundary:

- no final monitoring schedule should be promoted without full-text or guideline support

## Routing Table

| If The Question Is About | Route To | Do Not Route To |
|---|---|---|
| basic disease framing | `src-diabetes-014`, `src-diabetes-021` | treatment ranking |
| body condition / obesity | obesity body-condition memo | generic lifestyle note |
| difficult control / high insulin need | endocrine-secondary memo | default type-2-only frame |
| pancreatitis / DKA complexity | pancreatitis comorbidity memo | one-way causality claim |
| SGLT2 candidacy | current-label control memo | route convenience |
| remission | remission boundary memo | single-protocol promise |
| neuropathy | neuropathy boundary memo | treatment efficacy claim |

## Best Write-Back Targets

- [risk and recognition](../../topics/diabetes/risk-and-recognition.md)
- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md)
- [translation brief](../../topics/diabetes/translation-brief.md)
- [regulatory brief](../../topics/diabetes/regulatory-brief.md)
- [synthesis index](../../topics/diabetes/synthesis-index.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for workup architecture; no, for clinical protocol`
- smallest durable home: `memo + recognition write-back + endpoint write-back`

### Decision

- promote
