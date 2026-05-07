---
id: system-hcm-biomarker-use-case-memo
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

# HCM Biomarker Use-Case Memo

- Date: `2026-04-10`
- Scope: `src-hcm-006`, `src-hcm-010`, `src-hcm-017`, `src-hcm-023`

This memo exists to stop the HCM biomarker branch from drifting into one vague sentence like:

`biomarkers help diagnose HCM`

That sentence is directionally fine.

It is not specific enough for this vault.

## Core Takeaway

`the current HCM biomarker branch is best read by use case, not by one flat ranking`

Right now the safest branch split is:

- troponin I for injury / burden pressure
- NT-proBNP for severe-disease flagging and bounded screening augmentation
- novel biomarkers for frontier stratification, not routine authority

## Current Use-Case Layers

### Layer 1: Injury / Burden Interpretation

This layer is mainly carried by:

- `src-hcm-006`

Current meaning:

- troponin I belongs most naturally to myocardial injury and disease-burden reading
- higher signal with moderate-to-severe disease does not make troponin a structural phenotype definition tool
- this branch can sharpen severity reading without replacing echocardiographic confirmation

### Layer 2: Severe-Disease Flagging And Bounded Screening

This layer is mainly carried by:

- `src-hcm-010`

Current meaning:

- NT-proBNP can help detect more advanced or heavier-burden disease
- the current vault does not support promoting it into a reliable mild-to-moderate screening solution
- this branch belongs in screening augmentation, not structural confirmation

### Layer 3: Frontier Stratification

This layer is mainly carried by:

- `src-hcm-017`

Current meaning:

- novel biomarkers deepen the endpoint map beyond routine markers
- novelty is useful because it may improve stratification, not because it is already routine-ready
- this branch should remain explicitly below routine biomarker authority

### Layer 4: Non-Biomarker Augmentation Boundary

This layer is carried by:

- `src-hcm-023`

Current meaning:

- AI is not itself a biomarker branch
- it is useful to keep it adjacent here because it competes for the same mistaken role: shortcutting structure-first recognition
- AI belongs with augmentation logic, not with routine marker authority

## Current Working Hierarchy

| Marker / Augmentation Branch | Current Position In Vault | Strongest Safe Claim | Main Boundary |
|---|---|---|---|
| Troponin I | injury / burden branch | meaningful severity pressure signal | not structural phenotype definition |
| NT-proBNP | severe-disease flag and bounded screening augmentation | useful for heavier-burden cases | not reliable mild-disease screening authority |
| Novel biomarkers | frontier stratification branch | promising depth beyond routine markers | not routine-ready authority |
| AI augmentation | adjacent augmentation boundary | may help route or support suspicion | not biomarker replacement or phenotype confirmation |

## What The Module Can Already Say

1. HCM biomarker logic should be separated by use case.
2. Troponin and NT-proBNP do not do the same job.
3. Novel biomarkers currently deepen stratification more than they reorder routine authority.
4. Structural phenotype confirmation still outranks every biomarker branch.

## What The Module Should Not Yet Say

- there is no safe flat biomarker ranking that works across all HCM contexts
- troponin should not be promoted into phenotype-definition authority
- NT-proBNP should not be promoted into reliable mild-disease screen language
- frontier biomarkers should not be promoted into routine-ready marker authority
- AI should not be mistaken for part of the biomarker hierarchy itself

## Best Write-Back Targets

- [endpoint handbook](../../topics/hcm/endpoint-handbook.md)
- [risk and recognition](../../topics/hcm/risk-and-recognition.md)
- [synthesis index](../../topics/hcm/synthesis-index.md)
- [current state dashboard](../../topics/hcm/current-state-dashboard.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for biomarker use-case separation; no, for final cross-context ranking`
- smallest durable home: `memo + topic update + dashboard update`

### Reason

- what is repeating:
  HCM biomarker questions keep arriving as if troponin, NT-proBNP, frontier markers, and AI belong in one shared diagnostic bucket
- what becomes clearer:
  the branch now separates `injury/burden`, `severe-disease flagging`, and `frontier stratification`, while keeping AI outside routine biomarker authority
- what is still too thin, if anything:
  full comparative ranking and practice-level implementation rules are still too thin for stronger claims

### Decision

- promote
