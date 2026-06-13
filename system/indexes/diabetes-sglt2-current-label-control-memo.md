---
id: system-diabetes-sglt2-current-label-control-memo
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

# Diabetes SGLT2 Current Label Control Memo

- Date: `2026-04-24`
- Scope: `src-reg-010`, `src-reg-011`, `src-reg-012`, `src-reg-013`

This memo exists because the SGLT2 regulatory branch now has both FDA FOI summaries and current DailyMed label source cards.

## Core Takeaway

`Bexacat and Senvelgo can now be represented as U.S. primary-source-backed and current-label-controlled SGLT2 branches, but label control strengthens restrictions rather than loosening treatment claims`

## Source Stack

| Product | FOI Source | Current Label Source | Current Internal Role |
|---|---|---|---|
| Bexacat | [src-reg-010](../../raw/regulations/src-reg-010-bexacat-fda-foi.md) | [src-reg-012](../../raw/regulations/src-reg-012-bexacat-current-label.md), [label-section worksheet](src-reg-012-label-section-extraction.md) | bexagliflozin tablet branch |
| Senvelgo | [src-reg-011](../../raw/regulations/src-reg-011-senvelgo-fda-foi.md) | [src-reg-013](../../raw/regulations/src-reg-013-senvelgo-current-label.md), [label-section worksheet](src-reg-013-label-section-extraction.md) | velagliflozin oral-solution branch |

## Shared Current-Label Boundary

Both current-label cards support the same high-level boundary:

- otherwise healthy cats with diabetes mellitus
- not previously treated with insulin
- do not use in cats previously treated with insulin, receiving insulin, or with insulin-dependent diabetes mellitus
- diabetic ketoacidosis/euglycemic diabetic ketoacidosis is the governing safety warning

## Product-Specific Current-Label Notes

### Bexacat

- 15 mg bexagliflozin tablet
- once daily for cats weighing at least 3.0 kg
- with or without food and regardless of blood glucose level
- label-control source foregrounds pre-treatment screening and discontinuation/evaluation for DKA signs even when blood glucose is not high

### Senvelgo

- 15 mg/mL velagliflozin oral solution
- once daily at 1 mg/kg
- current DailyMed version updated April 1, 2026
- storage and six-month after-opening use instructions are label-controlled details

## What Label Control Changes

It changes the diabetes regulatory branch from:

`review abstract says FDA approved`

to:

`FOI summaries plus current label cards support U.S. product-specific SGLT2 source control`

The [SGLT2 label-section comparison memo](diabetes-sglt2-label-section-comparison-memo.md) now adds the next layer:

`shared class boundary plus product-specific monitoring gates`

It does not change the clinical claim to:

`SGLT2 is the preferred treatment`

## What The Module Can Say Now

- Bexacat and Senvelgo are U.S. FDA-regulated SGLT2 product branches with FOI and current-label source cards
- indication language should preserve otherwise-healthy and insulin-naive boundaries
- DKA/euglycemic DKA warnings must govern any treatment or owner-facing output
- product form differs: tablet versus oral solution
- product-specific monitoring gates differ enough that Bexacat and Senvelgo statements should not be merged at the schedule/detail level

## What The Module Should Not Say Yet

- do not rank Bexacat and Senvelgo
- do not infer global approval or availability
- do not promote use in complicated, insulin-dependent, or insulin-treated cats
- do not turn current-label dosing into patient-specific clinical instructions
- do not collapse current label cards into comparative efficacy evidence

## Key-Claim Traceability

| Claim ID | Key Claim | Claim Level | Supporting Source IDs | Notes |
|---|---|---|---|---|
| DSG1 | Bexacat and Senvelgo are U.S. FDA-regulated SGLT2 product branches with FOI and current-label source control. | B | src-reg-010, src-reg-011, src-reg-012, src-reg-013 | U.S. regulatory/source-control claim |
| DSG2 | Current label control preserves the otherwise-healthy, insulin-naive indication boundary for both Bexacat and Senvelgo. | B | src-reg-012, src-reg-013 | shared label boundary |
| DSG3 | SGLT2 label control strengthens restrictions rather than supporting broad treatment-preference claims. | B | src-reg-012, src-reg-013, diabetes-sglt2-label-section-comparison-memo | current-label boundary |
| DSG4 | DKA/euglycemic DKA warnings must govern SGLT2 treatment and owner-facing output. | B | src-reg-012, src-reg-013 | safety boundary |
| DSG5 | Bexacat and Senvelgo should not be ranked against each other or against insulin from current-label evidence alone. | B | src-reg-012, src-reg-013 | label evidence is not comparative efficacy evidence |
| DSG6 | Current U.S. label control does not establish global approval, complicated-diabetes use, or patient-specific dosing advice. | B | src-reg-012, src-reg-013 | scope boundary |

## Best Write-Back Targets

- [regulatory brief](../../topics/diabetes/regulatory-brief.md)
- [translation brief](../../topics/diabetes/translation-brief.md)
- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md)
- [SGLT2 safety/regulatory boundary memo](diabetes-sglt2-safety-regulatory-boundary-memo.md)
- [SGLT2 primary FDA source memo](diabetes-sglt2-primary-fda-source-memo.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for current-label control; no, for product ranking`
- smallest durable home: `memo + label source cards + regulatory write-back`

### Decision

- promote
