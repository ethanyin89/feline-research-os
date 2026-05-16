---
id: inbox-obesity-content-precision-promotion-batch-20260515
type: inbox
topic: obesity
disease: obesity
question_type: content-precision-promotion
source_ids: [src-obesity-001, src-obesity-004, src-obesity-005, src-obesity-008, src-obesity-080, src-diabetes-005]
last_compiled_at: 2026-05-15
verification_status: staged
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Content Precision Promotion Batch, 2026-05-15

## Classification

`方案 + 内容处理`

This is a manual 5-sample run under:

- [content precision promotion workflow](../../system/indexes/content-precision-promotion-workflow.md)
- [durable agent codification protocol](../../system/indexes/durable-agent-codification-protocol.md)
- [obesity source depth map](../../system/indexes/obesity-source-depth-map.md)

This is not a canonical obesity topic write-back. It is a staged decision note.

## Why This Batch Exists

The obesity corpus is now source-indexed but not decision-grade:

- `87` obesity source cards exist.
- `0` obesity source cards are deep-extracted.
- `44` cards are abstract-weighted.
- `43` cards are title-only.

Because "which obesity source should become the first real answer surface?" will recur,
this batch uses real candidates before any durable obesity page or recurring rule is
promoted.

## Candidates

| # | Disease | Object | Precision Type | Source Anchors | Decision | Target Surfaces |
|---|---|---|---|---|---|---|
| 1 | obesity | broad feline obesity shell / assessment | source-access / output-specific | `src-obesity-001`; obesity dashboard; obesity depth map | needs source access | no topic write-back; keep as first extraction priority |
| 2 | obesity | risk factors and associated pathologies | workup / recognition boundary | `src-obesity-004`; `src-obesity-004-structured-abstract-round1`; obesity dashboard | hold | no reader-facing claims; queue as risk-and-recognition owner candidate |
| 3 | obesity | prevention and target population | prevention boundary | `src-obesity-005`; `src-obesity-005-structured-abstract-round1`; obesity dashboard | hold | no prevention advice; queue as prevention owner candidate |
| 4 | obesity / diabetes | obesity-to-insulin-sensitivity bridge | mechanism / endpoint boundary | `src-obesity-008`; `src-obesity-008-structured-abstract-round1`; `diabetes-obesity-body-condition-memo`; `src-diabetes-005` | partial-promote | allow branch placement only; no numeric or clinical claims |
| 5 | obesity | weight-loss diet / activity / microbiota intervention | treatment-order / endpoint boundary | `src-obesity-080`; `src-obesity-080-structured-abstract-round1`; obesity depth map | hold | queue after first obesity page proves intervention need |

## Decisions

### 1. Broad feline obesity shell / assessment

Source check:

- `src-obesity-001` is feline-specific and broad: prevalence, risk factors, pathogenesis,
  associated conditions, and assessment.
- The current card is `title_only`; it has no abstract worksheet.
- It is useful for module architecture and extraction priority only.

Decision:

`needs source access`

What to promote:

- Do not promote claims.
- Keep it as the first extraction priority because it is the cleanest feline-specific
  broad shell.

What not to say:

- Do not give prevalence numbers.
- Do not state risk-factor ranking.
- Do not cite body-condition scoring thresholds.
- Do not make owner-facing assessment guidance from this card.

Write-back target:

- None yet. If approved later, update only the obesity depth map / queue status after
  abstract or full-text extraction.

### 2. Risk factors and associated pathologies

Source check:

- `src-obesity-004` is a 2024 JFMS source.
- Its structured abstract worksheet detects review family and branch signals:
  insulin, weight, obesity, overweight, risk factor.
- The worksheet explicitly says it supports branch placement only, not reader-facing
  clinical claims.

Decision:

`hold`

What to promote:

- Treat as a strong candidate for the first `risk-and-recognition` owner.
- Use only for queue placement until full abstract review or full-text extraction is done.

What not to say:

- Do not rank risk factors.
- Do not claim causal associated pathologies.
- Do not use it for prevalence, risk magnitude, or management recommendations.

Write-back target:

- None yet. After deeper extraction, likely targets are:
  - `topics/obesity/current-state-dashboard.md`
  - a future `topics/obesity/risk-and-recognition.md`

### 3. Prevention and target population

Source check:

- `src-obesity-005` is a 2024 JFMS source.
- Its worksheet detects review family and prevention signal.
- The current card can locate the prevention branch but cannot define target populations
  or intervention recommendations.

Decision:

`hold`

What to promote:

- Treat as the likely first prevention owner.
- Keep prevention separate from treatment/weight-loss management.

What not to say:

- Do not define exact prevention target groups.
- Do not recommend prevention programs.
- Do not make owner behavior, feeding-environment, or indoor-lifestyle claims.

Write-back target:

- None yet. After deeper extraction, likely target is a narrow prevention / target-population
  memo before any owner-facing prevention page.

### 4. Obesity-to-insulin-sensitivity bridge

Source check:

- `src-obesity-008` is an original feline study.
- Its worksheet detects `16 cats` and branch signals: insulin, glucose, weight, obesity.
- The existing diabetes obesity/body-condition memo already supports obesity as a
  diabetes mechanism / recognition / endpoint / translation branch through `src-diabetes-005`.

Decision:

`partial-promote`

What to promote:

- Promote only branch placement:
  `obesity deserves an obesity-diabetes bridge lane because there is feline-source support
  linking weight gain / obesity with insulin sensitivity and glucose metabolism.`
- This can support choosing `obesity-and-diabetes-bridge` as a plausible first narrow
  obesity owner.

What not to say:

- Do not quote exact effect size.
- Do not state that all obese cats become glucose intolerant.
- Do not create screening rules.
- Do not turn this into weight-loss treatment advice.

Write-back target:

- Staged only for now.
- If approved, smallest canonical write-back would be:
  - update [obesity source depth map](../../system/indexes/obesity-source-depth-map.md)
    to mark `obesity-and-diabetes-bridge` as the leading first-owner candidate
  - update [topics/obesity/current-state-dashboard.md](../../topics/obesity/current-state-dashboard.md)
    with branch-placement wording only
  - do not create a public bridge page until `src-obesity-008` receives fuller extraction

### 5. Weight-loss diet / activity / microbiota intervention

Source check:

- `src-obesity-080` is an original study candidate.
- Its worksheet detects objective / animals / procedures / results / conclusions /
  clinical relevance sections and branch signals: weight, body condition, overweight,
  microbiota, activity.
- It is relevant only after the module needs an intervention or management lane.

Decision:

`hold`

What to promote:

- Keep as a second-wave intervention candidate.
- Use after the first obesity owner proves whether weight-loss intervention detail is
  needed.

What not to say:

- Do not rank moderate-protein / high-fiber diets.
- Do not make diet advice.
- Do not claim microbiota or activity outcomes without deeper extraction.

Write-back target:

- None yet. Potential future target:
  - management-boundary memo
  - endpoint / intervention queue

## Batch Decision

The first obesity content surface should not be a broad obesity overview yet.

Current best read:

1. `src-obesity-001` still needs source access and remains first broad-shell extraction priority.
2. `src-obesity-004` and `src-obesity-005` are plausible first owner candidates but remain
   too thin for claims.
3. `src-obesity-008` is the only candidate in this batch that can safely change branch
   placement now, because it aligns with the existing diabetes obesity/body-condition
   memo and has an original-study worksheet.
4. `src-obesity-080` should wait until management/intervention need is proven.

Provisional first-owner ranking:

| Rank | Candidate Owner | Status |
|---:|---|---|
| 1 | obesity-and-diabetes-bridge | branch-placement candidate; needs deeper `src-obesity-008` extraction before public page |
| 2 | risk-and-recognition | strong candidate; needs deeper `src-obesity-004` extraction |
| 3 | prevention / target population | strong candidate; needs deeper `src-obesity-005` extraction |
| 4 | broad shell / assessment | source-access blocker at `src-obesity-001` |
| 5 | management / weight-loss intervention | second wave; hold `src-obesity-080` |

## Health Check Read

Should this become a recurring check?

Not as automatic promotion.

Judgment-heavy promotion should not be cron'd. However, a deterministic health check
is now implemented in [scripts/health.py](../../scripts/health.py):

- flag any obesity page that moves from `source-indexed` / `shell` to compiled guidance
  while obesity still has `0` deep-extracted source cards
- flag obesity pages that cite `title_only` or `abstract_weighted` sources without a
  visible evidence-depth caveat

Current health reports now include:

- `Obesity compiled guidance gate`
- existing thin-source usage / caveat checks

No cron was added for judgment-heavy promotion. The deterministic gate runs through the
existing health command:

```bash
python3 scripts/health.py
```

## Approval Gate

Do not write canonical obesity pages from this batch alone.

The smallest approval-worthy next move is:

`deep-extract src-obesity-008 or src-obesity-001, then rerun this batch decision before writing a public obesity page`
