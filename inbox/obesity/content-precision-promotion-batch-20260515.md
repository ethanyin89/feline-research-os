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
review_status: keep-with-blocker
review_decision: tier1-complete-tier2-held
---

# Content Precision Promotion Batch, 2026-05-15

## Classification

`方案 + 内容处理`

This is a manual 5-sample run under:

- [content precision promotion workflow](../../system/indexes/content-precision-promotion-workflow.md)
- [durable agent codification protocol](../../system/indexes/durable-agent-codification-protocol.md)
- [obesity source depth map](../../system/indexes/obesity-source-depth-map.md)

This is not a canonical obesity topic write-back. It is a staged decision note.

## Execution Update, 2026-05-17

**BATCH COMPLETE.** All 4 Tier 1 manual samples have been executed:

1. `src-obesity-008` - deep-extracted (mechanism / diabetes-bridge)
2. `src-obesity-004` - deep-extracted (risk factors / pathologies, 2024 JFMS review)
3. `src-obesity-005` - deep-extracted (prevention / target population, 2024 JFMS review)
4. `src-obesity-001` - deep-extracted (broad shell, 2016 comprehensive review)

**First architecture page written:** `topics/obesity/mechanism-overview.md`
- Establishes 5-branch architecture: prevalence, risk factors, pathogenesis, associated conditions, assessment
- Key-claim traceability table with 7 bounded claims
- Guardrails for what module can/cannot say

**Status:** Tier 1 complete. Tier 2 (src-obesity-080 and management sources) remain for future extraction if management/intervention detail is needed.

## Why This Batch Exists

The obesity corpus is now source-indexed but not decision-grade:

- `87` obesity source cards exist.
- `4` obesity source cards are deep-extracted.
- `41` cards are abstract-weighted.
- `42` cards are title-only.

Because "which obesity source should become the first real answer surface?" will recur,
this batch uses real candidates before any durable obesity page or recurring rule is
promoted.

## Candidates

| # | Disease | Object | Precision Type | Source Anchors | Decision | Target Surfaces |
|---|---|---|---|---|---|---|
| 1 | obesity | broad feline obesity shell / assessment | source-access / output-specific | `src-obesity-001`; obesity dashboard; obesity depth map | **DONE** | deep-extracted; anchors mechanism-overview 5-branch architecture |
| 2 | obesity | risk factors and associated pathologies | workup / recognition boundary | `src-obesity-004`; `src-obesity-004-deep-extraction-round1`; obesity dashboard | **DONE** | deep-extracted; anchors risk-factor framework (intrinsic/extrinsic) |
| 3 | obesity | prevention and target population | prevention boundary | `src-obesity-005`; `src-obesity-005-deep-extraction-round1`; obesity dashboard | **DONE** | deep-extracted; anchors prevention target (post-neuter kittens 5-12mo) |
| 4 | obesity / diabetes | obesity-to-insulin-sensitivity bridge | mechanism / endpoint boundary | `src-obesity-008`; `src-obesity-008-deep-extraction-round1`; `diabetes-obesity-body-condition-memo`; `src-diabetes-005` | **DONE** | deep-extracted; anchors diabetes-bridge mechanism |
| 5 | obesity | weight-loss diet / activity / microbiota intervention | treatment-order / endpoint boundary | `src-obesity-080`; `src-obesity-080-structured-abstract-round1`; obesity depth map | hold | queue after management/intervention need is proven |

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

**RESOLVED 2026-05-17.** The first obesity architecture page is now written.

| Rank | Candidate Owner | Status |
|---:|---|---|
| 1 | mechanism-overview (5-branch architecture) | **DONE** - `topics/obesity/mechanism-overview.md` |
| 2 | obesity-and-diabetes-bridge | supported by `src-obesity-008` deep extraction |
| 3 | risk-and-recognition | supported by `src-obesity-001`, `src-obesity-004` |
| 4 | prevention / target population | supported by `src-obesity-005` |
| 5 | management / weight-loss intervention | hold; `src-obesity-080` remains Tier 2 |

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

**PASSED 2026-05-17.**

All Tier 1 sources deep-extracted. All architecture pages written. All bilingual versions compiled.

Completed:
1. ✓ mechanism-overview + bilingual
2. ✓ risk-and-recognition + bilingual
3. ✓ prevention + bilingual
4. ✓ diabetes-bridge + bilingual

Next moves:
1. Deep-extract Tier 2 sources (src-obesity-080, management context) if intervention detail is needed
2. Write assessment-methods page after body condition full-text extraction
