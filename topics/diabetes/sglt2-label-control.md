---
id: topic-diabetes-sglt2-label-control
type: topic
topic: diabetes
species: feline
disease: diabetes mellitus
question_type: regulatory
source_ids: [src-diabetes-011, src-reg-010, src-reg-011, src-reg-012, src-reg-013]
last_compiled_at: 2026-04-24
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
language_qa_notes: "2026-04-24 checked for paper-card verification-state sync; page remains label-control guidance, not treatment ranking or decision-grade use instructions."
owner: codex
status: active
---

# Feline Diabetes SGLT2 Label Control

## Evidence-Depth Caveat

This page combines a now deep-extracted paper-card context with U.S. regulatory/label source cards. It is still not decision-grade treatment guidance or a product-ranking page.

## Question This Page Answers

How should Bexacat and Senvelgo be represented without turning label control into treatment ranking?

## Quantified Claim Traceability

| Claim | Source IDs | Boundary |
|---|---|---|
| Bexacat is represented as a 15 mg bexagliflozin tablet given once daily for cats weighing at least 3.0 kg. | src-reg-010, src-reg-012 | U.S. FDA FOI/current-label control; do not convert into patient-specific instructions. |
| Senvelgo is represented as a 15 mg/mL velagliflozin oral solution dosed once daily at 1 mg/kg, with current DailyMed version updated April 1, 2026. | src-reg-011, src-reg-013 | U.S. FDA FOI/current-label control; do not infer global availability or product superiority. |

## Core Takeaway

Bexacat and Senvelgo can be represented as U.S. primary-source-backed and current-label-controlled SGLT2 branches, but label control strengthens restrictions rather than loosening treatment claims.

## Source Stack

| Product | FOI Source | Current Label Source | Internal Role |
|---|---|---|---|
| Bexacat | [src-reg-010](../../raw/regulations/src-reg-010-bexacat-fda-foi.md) | [src-reg-012](../../raw/regulations/src-reg-012-bexacat-current-label.md) | bexagliflozin tablet branch |
| Senvelgo | [src-reg-011](../../raw/regulations/src-reg-011-senvelgo-fda-foi.md) | [src-reg-013](../../raw/regulations/src-reg-013-senvelgo-current-label.md) | velagliflozin oral-solution branch |

## Shared Current-Label Boundary

Both current-label cards preserve the same high-level boundary:

- otherwise healthy cats with diabetes mellitus
- not previously treated with insulin
- do not use in cats previously treated with insulin, receiving insulin, or with insulin-dependent diabetes mellitus
- diabetic ketoacidosis/euglycemic diabetic ketoacidosis is the governing safety warning

## Product-Specific Notes

| Product | Label-Controlled Detail | Boundary |
|---|---|---|
| Bexacat | 15 mg bexagliflozin tablet; once daily for cats at least 3.0 kg; pre-treatment screening and DKA evaluation language. | Do not convert label dosing into patient-specific instructions. |
| Senvelgo | 15 mg/mL velagliflozin oral solution; once daily at 1 mg/kg; current DailyMed version updated April 1, 2026. | Do not infer global availability or product superiority. |

## What The Module Can Say Now

- Bexacat and Senvelgo are U.S. FDA-regulated SGLT2 product branches with FOI and current-label source cards.
- Indication language should preserve otherwise-healthy and insulin-naive boundaries.
- DKA/euglycemic DKA warnings must govern any treatment or owner-facing output.
- Product form differs: tablet versus oral solution.
- Product-specific monitoring gates differ enough that Bexacat and Senvelgo statements should not be merged at the schedule/detail level.

## Guardrail

Do not rank Bexacat and Senvelgo. Do not infer global approval or availability. Do not promote use in complicated, insulin-dependent, or insulin-treated cats.
