---
id: system-diabetes-sglt2-label-section-comparison-memo
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

# Diabetes SGLT2 Label-Section Comparison Memo

- Date: `2026-04-24`
- Scope: `src-reg-012`, `src-reg-013`, plus label-section worksheets

This memo exists to compare label-section control points without ranking products.

## Core Takeaway

`Bexacat and Senvelgo share the same high-level SGLT2 boundary, but their monitoring gates differ enough that product-specific label control is required before any external-facing output`

## Shared Label Boundary

Both labels support:

- prescription animal-drug status
- oral use in cats only
- SGLT2 mechanism class
- indication for otherwise healthy cats with diabetes mellitus not previously treated with insulin
- do-not-use boundary for insulin-treated, previously insulin-treated, or insulin-dependent diabetic cats
- DKA/euglycemic DKA warning as the dominant safety frame
- discontinuation and insulin transition logic when DKA/euglycemic DKA or poor control gates are met

## Product-Specific Monitoring Differences

| Branch | Bexacat | Senvelgo |
|---|---|---|
| form | 15 mg tablet | 15 mg/mL oral solution |
| early glycemic assessment | 2, 4, and 8 weeks | 1 and 4 weeks |
| glucose curve detail | 8-hour blood glucose curve | blood glucose curve |
| ketone emphasis | BHBA monitoring and BHBA discontinuation gates | urine ketone checks at 2-3 days and around 7 days |
| poor-control gate | average 8-hour curve >= 250 mg/dL and/or poor fructosamine at 8 weeks | average curve > 300 mg/dL or fructosamine > 450 umol/L after 4 weeks |
| pancreatitis signal | fPL > 5.3 mcg/L or pancreatitis history/signs block initiation | recent pancreatitis suspicion, fPL > 12 mcg/L, and/or imaging concern block initiation |
| renal/hepatic boundary | hepatic disease or reduced renal function contraindication | creatinine threshold and CKD stage caveats in label warnings/precautions |

## What The Module Can Say Now

- SGLT2 output needs product-specific label routing.
- The shared high-level branch is insulin-naive, otherwise-healthy feline diabetes.
- Bexacat monitoring is more BHBA / 2-4-8-week structured in this extracted layer.
- Senvelgo monitoring is more ketonuria / 2-3 day / 7 day / 1-4-week structured in this extracted layer.
- Neither label supports product superiority.

## What The Module Should Not Say

- do not rank Bexacat versus Senvelgo
- do not generalize one product's monitoring schedule to the other
- do not convert label dosing into patient-specific instructions
- do not weaken contraindication language into vague caution
- do not infer non-U.S. regulatory availability

## Write-Back Rule

Any SGLT2 statement should choose one of these layers:

1. class-level: SGLT2 inhibitors as a branch
2. shared-label: otherwise-healthy, insulin-naive, DKA/euglycemic DKA boundary
3. product-specific: Bexacat or Senvelgo label section
4. not established: comparative efficacy, global availability, or complicated-diabetes use

## Best Write-Back Targets

- [regulatory brief](../../topics/diabetes/regulatory-brief.md)
- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md)
- [translation brief](../../topics/diabetes/translation-brief.md)
- [SGLT2 current label control memo](diabetes-sglt2-current-label-control-memo.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for label-section comparison; no, for product ranking`
- smallest durable home: `memo + label-section worksheets + regulatory write-back`

### Decision

- promote
