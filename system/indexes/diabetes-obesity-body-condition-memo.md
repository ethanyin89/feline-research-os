---
id: system-diabetes-obesity-body-condition-memo
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

# Diabetes Obesity Body-Condition Memo

- Date: `2026-04-24`
- Scope: `src-diabetes-005`, with pathogenesis context from `src-diabetes-001` and diet context from `src-diabetes-006`

This memo exists to keep obesity from being treated as a generic risk-factor label.

## Core Takeaway

`obesity is a mechanism, recognition, endpoint, and sequencing branch in feline diabetes; body condition must be interpreted against current presentation state, not only historical overweight status`

## Main Source Logic

Main source:

- [src-diabetes-005 deep extraction round 1](src-diabetes-005-deep-extraction-round1.md)

Current compiled evidence supports:

- up to 40% of domestic cats are overweight or obese
- obesity reduces insulin sensitivity
- overt diabetes risk rises when insulin resistance coexists with beta-cell dysfunction
- diabetic control may need to precede caloric restriction in some obese diabetic cats because many present after weight and muscle loss

## Why Obesity Is Cross-Cutting

### Mechanism

Obesity belongs upstream of insulin resistance and beta-cell demand.

It should not replace beta-cell failure as the threshold event.

### Recognition

Body condition belongs in risk recognition because weight, inactivity, and obesity interact with diabetes risk.

But current presentation may include weight and muscle loss even when obesity contributed earlier.

### Endpoint

Body condition is not just an owner-visible descriptor.

It is a management endpoint tied to:

- insulin sensitivity
- caloric restriction
- muscle preservation
- glycemic control
- remission-related monitoring

### Translation

Treatment sequencing matters.

The current safe rule is:

`stabilization, glycemic control, diet composition, and weight loss must be staged rather than collapsed into immediate caloric restriction`

## What The Module Can Say Now

- obesity is a central insulin-resistance pressure branch
- obesity alone is not the whole diabetes mechanism because beta-cell dysfunction still matters
- body condition belongs in mechanism, recognition, endpoint, and translation pages
- weight-loss language needs a presentation-state caveat

## What The Module Should Not Say Yet

- do not prescribe exact calorie targets from the current compiled layer alone
- do not make universal sequencing rules
- do not treat every diabetic cat as currently overweight
- do not turn obesity into moralized owner-facing language
- do not isolate diet composition from body-condition state

## Key-Claim Traceability

| Claim ID | Key Claim | Claim Level | Supporting Source IDs | Notes |
|---|---|---|---|---|
| DOBC1 | Obesity is a causal mechanism branch in feline diabetes, not just a descriptive risk label. | B | src-diabetes-005, src-diabetes-001 | obesity belongs upstream of insulin resistance and beta-cell demand |
| DOBC2 | Up to 40% of domestic cats are overweight or obese, making obesity-linked insulin resistance a structurally common upstream pressure. | A | src-diabetes-005 | direct prevalence statement from abstract |
| DOBC3 | Overt diabetes risk rises when obesity-driven insulin resistance coexists with beta-cell dysfunction; obesity alone is not the threshold event. | B | src-diabetes-005, src-diabetes-001 | preserves beta-cell failure as overt-diabetes gatekeeper |
| DOBC4 | Body condition belongs in mechanism, recognition, endpoint, and translation framing; it is not only an owner-visible descriptor. | B | src-diabetes-005 | compiled architecture claim |
| DOBC5 | Treatment sequencing must account for current presentation state: diabetic control may need to precede caloric restriction when the cat presents with weight and muscle loss despite historical obesity. | B | src-diabetes-005 | sequencing caveat prevents unsafe immediate caloric restriction |
| DOBC6 | Weight-loss and obesity language must carry a presentation-state caveat; not every diabetic cat is currently overweight at diagnosis. | C | src-diabetes-005, compiled memo judgment | prevents moralized or overgeneralized obesity framing |

## Best Write-Back Targets

- [mechanism overview](../../topics/diabetes/mechanism-overview.md)
- [risk and recognition](../../topics/diabetes/risk-and-recognition.md)
- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md)
- [translation brief](../../topics/diabetes/translation-brief.md)
- [current state dashboard](../../topics/diabetes/current-state-dashboard.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for obesity/body-condition architecture; no, for diet prescription`
- smallest durable home: `memo + mechanism write-back + translation write-back`

### Decision

- promote
