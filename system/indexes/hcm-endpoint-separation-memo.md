---
id: system-hcm-endpoint-separation-memo
type: system
topic: hcm
last_compiled_at: 2026-04-10
owner: codex
status: active
language: en
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
---

# HCM Endpoint Separation Memo

- Date: `2026-04-10`
- Scope: `src-hcm-006`, `src-hcm-009`, `src-hcm-010`, `src-hcm-013`, `src-hcm-017`, `src-hcm-023`, `src-hcm-024`

This memo exists to prevent the current HCM endpoint branch from flattening into one vague category like:

`echo, biomarkers, and AI all help diagnose HCM`

That sentence is directionally useful, but it destroys the actual hierarchy.

## Core Takeaway

`the current HCM endpoint architecture is not flat: structural confirmation leads, screening augmentation stays separate, injury/severity markers sit below phenotype definition, and pathology depth belongs in a later layer`

## Current Endpoint Layers

### Layer 1: Structural Confirmation

This layer is mainly carried by:

- `src-hcm-009`
- `src-hcm-013`

Current meaning:

- echocardiographic and gross morphometric structure are still the lead operational branch
- phenotype definition should stay above blood biomarkers and computational augmentation
- HCM structural phenotype is heterogeneous and should not be collapsed into one uniform shape

### Layer 2: Screening Augmentation

This layer is mainly carried by:

- `src-hcm-010`
- `src-hcm-023`

Current meaning:

- augmentation tools can help suspicion and early routing
- NT-proBNP currently looks much stronger as a severe-disease signal than as a reliable mild-disease screen
- AI and augmentation branches should not be mistaken for structural confirmation authority

### Layer 3: Injury / Severity Signal

This layer is mainly carried by:

- `src-hcm-006`
- `src-hcm-017`

Current meaning:

- troponin-like markers belong more naturally to injury or burden interpretation than to primary phenotype definition
- biomarker elevation can be meaningful without becoming a structural surrogate
- this branch should stay below echo-led phenotype recognition

### Layer 4: Pathology-Depth And End-Stage Architecture

This layer is mainly carried by:

- `src-hcm-024`
- `src-hcm-019`

Current meaning:

- pathology staging belongs in the endpoint map, but not as first-pass routine authority
- end-stage HCM looks like a remodeled phenotype with fibrosis, dilation, and vascular change
- depth layers should clarify severity architecture rather than replace clinical structural recognition

## What The Module Can Already Say

- endpoint logic should be modeled as a hierarchy, not a list
- structural confirmation currently outranks biomarker and augmentation branches
- biomarker value is real, but split by use case rather than treated as one generic diagnostic bucket
- pathology-depth logic belongs in the module, but below first-pass structural confirmation

## What The Module Should Not Yet Say

- there is no safe flat endpoint ranking that treats all biomarkers and AI tools as interchangeable
- NT-proBNP should not be promoted into a reliable mild-disease screening claim
- troponin should not be promoted into a structural phenotype-definition claim
- pathology staging should not be mistaken for routine first-wave recognition authority

## Best Write-Back Targets

- [endpoint handbook](../../topics/hcm/endpoint-handbook.md)
- [risk and recognition](../../topics/hcm/risk-and-recognition.md)
- [synthesis index](../../topics/hcm/synthesis-index.md)
- [current state dashboard](../../topics/hcm/current-state-dashboard.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for endpoint hierarchy; no, for final all-context ranking`
- smallest durable home: `memo + topic update + dashboard update`

### Reason

- what is repeating:
  HCM endpoint questions keep arriving as if echo, biomarkers, and AI belong in one flat diagnostic bucket
- what becomes clearer:
  the branch now separates `structural confirmation`, `screening augmentation`, `injury/severity`, and `pathology depth`
- what is still too thin, if anything:
  full cross-endpoint ranking and routine-practice implementation logic still need later compression

### Decision

- promote
