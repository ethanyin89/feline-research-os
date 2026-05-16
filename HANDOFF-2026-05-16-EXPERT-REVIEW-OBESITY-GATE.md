# Handoff, 2026-05-16 Expert Review, Obesity Gate, And Content Continuation

This is the current handoff for the next model. It supersedes the 2026-05-15 handoff
as the first file to read, but the 2026-05-15 file remains useful background.

## Binding Rule

The user explicitly restated this operating rule:

`不允许做一次性工作。如果某件事将来还会做，就先手动跑 3-10 个样本，批准后固化成技能文件。如果需要自动运行，就设 cron。测试标准：如果同一件事问两次，就失败。`

How this was applied in the latest work:

- Judgment-heavy obesity content promotion was handled as a 5-sample manual batch in
  `inbox/`, not as direct canonical topic-page write-back.
- The deterministic repeat-risk from that batch was codified in `scripts/health.py`,
  not left as a one-off instruction.
- No cron was added because this repo currently uses `python3 scripts/health.py` as
  the durable health command; cron / launchd should only be added if the user wants
  health checks scheduled automatically.

## Current Git State

Branch: `main`

Uncommitted changes intentionally present:

- `HANDOFF.md`
- `HANDOFF-2026-05-15-EXPERT-REVIEW-SOURCE-DEPTH.md`
- `HANDOFF-2026-05-16-EXPERT-REVIEW-OBESITY-GATE.md` (this file)
- `scripts/app.py`
- `scripts/expert_review.py` (new)
- `scripts/health.py`
- `scripts/test_query.py`
- `system/health-checks/health-report-20260514.md`
- `system/health-checks/health-report-20260515.md` (new)
- `system/indexes/ask-the-vault.md`
- `system/indexes/expert-answer-review-prototype-20260514.md`
- `system/indexes/source-depth-map.md`
- `inbox/obesity/content-precision-promotion-batch-20260515.md` (new)

Do not revert these. They are the active continuation batch.

## What Changed

### 1. Ask The Vault Expert Review Loop

New helper:

- [scripts/expert_review.py](scripts/expert_review.py)

App integration:

- [scripts/app.py](scripts/app.py)

Tests:

- [scripts/test_query.py](scripts/test_query.py)

The app now exposes:

`Expert review loop -> Download review prompt`

under rendered answers. The prompt includes the original question, answer, disease,
question type, confidence, source IDs, reviewer-selection prompt, and strict review
instructions.

Boundary:

`Expert chat is review input, not source evidence.`

Do not automate expert review yet. Current manual sample count is still `1/3-10`.

### 2. Expert Review Docs

Updated:

- [system/indexes/ask-the-vault.md](system/indexes/ask-the-vault.md)
- [system/indexes/expert-answer-review-prototype-20260514.md](system/indexes/expert-answer-review-prototype-20260514.md)

The docs now record that the expert-review loop is visible in the app but remains a
manual prompt-export surface.

### 3. Source Depth Map Reality Sync

Updated:

- [system/indexes/source-depth-map.md](system/indexes/source-depth-map.md)

The cross-disease map now reflects `325` strict disease paper cards:

| Disease | Cards | Current Source Reality |
|---|---:|---|
| CKD | 24 | 24 full / 24 deep_extracted |
| FIP | 24 | 24 full / 24 deep_extracted |
| HCM | 24 | 24 full / 24 deep_extracted |
| IBD | 24 | 24 full / 24 deep_extracted |
| Diabetes | 118 | 24 full seed cards, 94 partial extension cards |
| FCV | 24 | 24 full / 24 deep_extracted |
| Obesity | 87 | 87 partial, 0 deep_extracted |

Current content read:

- Do not reopen CKD / FIP / HCM / IBD broad thickening.
- Diabetes seed corpus is full; extension corpus is non-decision-grade until a narrow
  use case justifies extraction.
- Obesity is the only large corpus with `0` deep-extracted source cards.

### 4. Obesity 5-Sample Content Batch

Added:

- [inbox/obesity/content-precision-promotion-batch-20260515.md](inbox/obesity/content-precision-promotion-batch-20260515.md)

This is a staged note, not canonical topic write-back.

Manual samples:

- `src-obesity-001`: broad shell / assessment
- `src-obesity-004`: risk factors / associated pathologies
- `src-obesity-005`: prevention / target population
- `src-obesity-008`: obesity-to-insulin-sensitivity bridge
- `src-obesity-080`: weight-loss diet / activity / microbiota intervention

Batch decision:

- Do not write a broad obesity overview yet.
- `src-obesity-008` can only partial-promote to branch placement.
- `src-obesity-001` remains a source-access blocker.
- `src-obesity-004`, `src-obesity-005`, and `src-obesity-080` remain hold.
- Best next content move is deeper extraction of `src-obesity-008` or `src-obesity-001`.

### 5. Obesity Compiled Guidance Health Gate

Updated:

- [scripts/health.py](scripts/health.py)
- [scripts/test_query.py](scripts/test_query.py)
- [system/health-checks/health-report-20260515.md](system/health-checks/health-report-20260515.md)

New deterministic health row:

`Obesity compiled guidance gate`

It flags obesity reader pages that exceed shell/source-indexed status while obesity has
`0` deep-extracted source cards.

This is now a system asset. The next model should not ask again whether this repeated
risk needs protection; it is protected by `python3 scripts/health.py`.

## Verification Already Run

Passed:

```bash
python3 scripts/test_query.py
python3 scripts/check_markdown_links.py
python3 scripts/health.py
python3 -m py_compile scripts/app.py scripts/search.py scripts/query.py scripts/expert_review.py scripts/health.py scripts/test_query.py
git diff --check
```

Observed:

- Query tests: `106 passed | 0 failed | 106 total`
- Markdown links: `PASS: checked 1090 markdown files, no local link issues found.`
- Health report: [system/health-checks/health-report-20260515.md](system/health-checks/health-report-20260515.md)
- `Obesity compiled guidance gate`: PASS
- Inbox backlog: WARN because the staged obesity batch is active
- `8502` test server was stopped; no listener remains there
- Existing `8501` process was intentionally left untouched

Expected test warnings:

- `scripts/test_query.py` warns that one CKD image is too large
- `scripts/test_query.py` warns that path traversal was blocked

Those are expected test fixtures, not failures.

## Current Health Read

Latest full health report:

- [system/health-checks/health-report-20260515.md](system/health-checks/health-report-20260515.md)

Important rows:

- `Thin source usage`: WARN, because obesity shell pages cite abstract-weighted/title-only sources
- `Thin source caveats`: PASS
- `Obesity compiled guidance gate`: PASS
- `Inbox backlog`: WARN, because `inbox/obesity/content-precision-promotion-batch-20260515.md` is active

This is correct. Do not "fix" it by deleting the staged note.

## Next Work

If continuing content:

1. Read [inbox/obesity/content-precision-promotion-batch-20260515.md](inbox/obesity/content-precision-promotion-batch-20260515.md).
2. Do not promote canonical obesity pages from the staged note alone.
3. The best next manual content work is deeper extraction of either:
   - `src-obesity-008`, if building the obesity-diabetes bridge
   - `src-obesity-001`, if unblocking the broad obesity shell / assessment owner
4. Stage any new judgment-heavy movement through `inbox/`.

If continuing expert review:

1. Run another real manual expert-review sample.
2. Record it before changing `EXPERT_REVIEW_SAMPLE_COUNT`.
3. Do not codify a final expert-review workflow until at least `3` successful samples exist.

If continuing UI:

1. Preserve the `Expert review loop` expander.
2. Keep expert review separate from source evidence.
3. Do not hide provenance, uncertainty, or confidence.

If asked to ship:

1. Review the whole diff as one coherent batch.
2. Commit expert-review UI, source-depth sync, obesity staged batch, and health gate together
   only if the user wants this batch landed.

## Files To Read First

1. [HANDOFF.md](HANDOFF.md)
2. [HANDOFF-2026-05-15-EXPERT-REVIEW-SOURCE-DEPTH.md](HANDOFF-2026-05-15-EXPERT-REVIEW-SOURCE-DEPTH.md)
3. [scripts/expert_review.py](scripts/expert_review.py)
4. [scripts/app.py](scripts/app.py)
5. [scripts/health.py](scripts/health.py)
6. [scripts/test_query.py](scripts/test_query.py)
7. [system/indexes/source-depth-map.md](system/indexes/source-depth-map.md)
8. [inbox/obesity/content-precision-promotion-batch-20260515.md](inbox/obesity/content-precision-promotion-batch-20260515.md)
9. [system/health-checks/health-report-20260515.md](system/health-checks/health-report-20260515.md)

## Do Not Do

- Do not revert the uncommitted active batch.
- Do not treat expert-review chat as source evidence.
- Do not create a final expert-review skill yet.
- Do not write canonical obesity guidance while obesity has `0` deep-extracted source cards.
- Do not bypass the `Obesity compiled guidance gate`.
- Do not reopen generic thickening for CKD / FIP / HCM / IBD.
- Do not kill the existing `8501` process unless the user explicitly asks.

## One Line

Continue from the durable assets now in place: expert-review prompt export stays manual,
obesity promotion stays staged, and obesity guidance drift is now guarded by `health.py`.
