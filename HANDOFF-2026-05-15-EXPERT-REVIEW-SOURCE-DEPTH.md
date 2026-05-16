# Handoff, 2026-05-15 Expert Review And Source Depth Sync

This is the focused handoff for the next model after the expert-review UI slice and
cross-disease source-depth-map sync.

## Task Type

按当前 repo 状态，这次接力属于：

`普通用户 Ask the vault 表面 + 内容状态写回`

不是重新开一轮广义 source-card thickening，也不是继续做前端展示美化。

The binding operating rule still applies:

`No one-off work. If a task will recur, first run 3-10 real samples manually, then codify it. Use cron only for deterministic automation, not judgment-heavy content promotion.`

## Current Git State

Branch: `main`

Uncommitted changes intentionally present:

- `scripts/app.py`
- `scripts/health.py`
- `scripts/test_query.py`
- `scripts/expert_review.py` (new)
- `system/health-checks/health-report-20260515.md` (new)
- `system/health-checks/health-report-20260514.md`
- `system/indexes/ask-the-vault.md`
- `system/indexes/expert-answer-review-prototype-20260514.md`
- `system/indexes/source-depth-map.md`
- `inbox/obesity/content-precision-promotion-batch-20260515.md` (new)

Do not assume these are user edits to revert. They are the active continuation batch.

## What Changed

### Ask The Vault Expert Review Loop

The app now exposes a manual expert-review loop under each rendered answer:

`Expert review loop -> Download review prompt`

Files:

- [scripts/expert_review.py](scripts/expert_review.py)
- [scripts/app.py](scripts/app.py)
- [scripts/test_query.py](scripts/test_query.py)

The helper module is pure:

- no Streamlit import
- no API calls
- no file writes

It builds a copy-ready expert-review prompt containing:

- original user question
- Ask the vault answer
- disease / question type / confidence metadata
- cited source IDs
- reviewer-selection prompt
- strict review instructions
- current manual sample gate: `manual sample 1/3-10`

Important policy boundary:

`Expert chat is review input, not source evidence.`

Do not automate this yet. The prototype currently has only `1` real manual sample.
It needs at least `3` successful samples before codifying a final workflow or skill.

### Expert Review Docs

Updated:

- [system/indexes/ask-the-vault.md](system/indexes/ask-the-vault.md)
- [system/indexes/expert-answer-review-prototype-20260514.md](system/indexes/expert-answer-review-prototype-20260514.md)

The docs now state that the review loop is user-facing but still manual. It is allowed
because it exports a prompt and does not make judgment-heavy write-back decisions.

### Health Report

Updated:

- [system/health-checks/health-report-20260514.md](system/health-checks/health-report-20260514.md)

Changes:

- Query tests now read `104 passed | 0 failed | 104 total`.
- Added `Expert review UI surface` PASS row.

### Source Depth Map Sync

Updated:

- [system/indexes/source-depth-map.md](system/indexes/source-depth-map.md)

The old cross-disease snapshot still described the repo as a `120`-card / five-disease
world. It now reflects the current `325` strict disease paper-card reality:

| Disease | Cards | Depth Reality | Verification Reality |
|---|---:|---|---|
| CKD | 24 | 24 full | 24 deep_extracted |
| FIP | 24 | 24 full | 24 deep_extracted |
| HCM | 24 | 24 full | 24 deep_extracted |
| IBD | 24 | 24 full | 24 deep_extracted |
| Diabetes | 118 | 24 full, 94 partial | 24 deep_extracted, 59 abstract_weighted, 35 title_only |
| FCV | 24 | 24 full | 24 deep_extracted |
| Obesity | 87 | 87 partial | 44 abstract_weighted, 43 title_only |

New default next-move read:

1. Obesity is the only large corpus with `0` deep-extracted source cards, but do not
   extract it generically. Move only when tied to a specific obesity/diabetes bridge
   or first obesity answer surface.
2. Diabetes seed corpus is full; extension corpus remains source-check /
   structured-abstract material until a narrow clinical, regulatory, obesity, or
   output-order question justifies deeper extraction.
3. FCV source layer is full; next gains are field-effectiveness, label/regulatory,
   therapy, image, or output-specific precision.
4. IBD / FIP / HCM should move only on full-text, official-source, image/table, or
   output-specific precision that changes branch order.
5. CKD bootstrap should not be reopened.

### Obesity Content Precision Batch

Added:

- [inbox/obesity/content-precision-promotion-batch-20260515.md](inbox/obesity/content-precision-promotion-batch-20260515.md)

This is a 5-sample manual run, not a canonical topic-page write-back.

Samples:

- `src-obesity-001`: broad shell / assessment
- `src-obesity-004`: risk factors / associated pathologies
- `src-obesity-005`: prevention / target population
- `src-obesity-008`: obesity-to-insulin-sensitivity bridge
- `src-obesity-080`: weight-loss diet / activity / microbiota intervention

Decision:

- Do not write broad obesity overview yet.
- `src-obesity-008` can only partial-promote to branch placement.
- `src-obesity-001` remains a source-access blocker.
- `src-obesity-004`, `src-obesity-005`, and `src-obesity-080` remain hold.

### Obesity Health Gate

Updated:

- [scripts/health.py](scripts/health.py)
- [scripts/test_query.py](scripts/test_query.py)
- [system/health-checks/health-report-20260515.md](system/health-checks/health-report-20260515.md)

The health report now has a deterministic row:

`Obesity compiled guidance gate`

Purpose:

- flag obesity reader pages that exceed shell/source-indexed status while obesity still
  has `0` deep-extracted source cards
- keep this as automation, not judgment-heavy promotion

No cron was added for judgment-heavy content promotion. This repo's current durable
automation path is `python3 scripts/health.py`; cron should only be added if health
checks become a scheduled operator requirement.

## Verification Already Run

These passed after the current edits:

```bash
python3 scripts/test_query.py
python3 -m py_compile scripts/app.py scripts/search.py scripts/query.py scripts/expert_review.py scripts/health.py scripts/test_query.py
python3 scripts/check_markdown_links.py
python3 scripts/health.py
git diff --check
```

Observed results:

- Query tests: `106 passed | 0 failed | 106 total`
- Markdown links: `PASS: checked 1090 markdown files, no local link issues found.`
- Health report: [system/health-checks/health-report-20260515.md](system/health-checks/health-report-20260515.md)
- Py compile: pass
- Diff check: pass

Streamlit UI smoke:

- Existing `8501` was already occupied and was left untouched.
- A temporary app server on `8502` returned HTTP 200.
- Streamlit `AppTest` with a seeded assistant answer rendered:
  - `Expert review loop`
  - `Download review prompt`
- The temporary `8502` process was stopped.

Handoff reality commands also completed:

```bash
find raw/images -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \) | sort
python3 - <<'PY'
from pathlib import Path
import re
root = Path('raw/papers')
for disease in ['ckd', 'fip', 'hcm', 'ibd', 'diabetes']:
    cards = sorted(root.glob(f'src-{disease}-*.md'))
    statuses = {}
    for p in cards:
        text = p.read_text(encoding='utf-8')
        m = re.search(r'^status:\s*(.+)$', text, re.M)
        s = m.group(1).strip() if m else 'missing'
        statuses[s] = statuses.get(s, 0) + 1
    print(disease.upper(), len(cards), statuses)
PY
```

The source-depth-map sync used a broader source-card count across CKD, FIP, HCM, IBD,
Diabetes, FCV, and obesity.

## Known Caveats

- `scripts/test_query.py` emits expected warnings during image/path-traversal tests:
  - large CKD image skipped
  - path traversal blocked
- Browser text inspection via gstack was not reliable for Streamlit state because one
  browse instance reset to `about:blank`; the decisive UI verification came from
  Streamlit `AppTest` plus HTTP 200.
- No live LLM answer-generation run was performed in this continuation. This slice is
  prompt-export/UI and source-state sync, not live OpenRouter answer acceptance.
- The `EXPERT_REVIEW_SAMPLE_COUNT` is still hardcoded at `1`; do not bump it without
  another real manual sample and staged write-back note.

## Next Work

If continuing this exact batch:

1. Review the current diff as one coherent change.
2. If acceptable, commit it as an expert-review UI + source-depth sync batch.
3. Do not create a final expert-review workflow/skill yet.

If continuing content:

1. Use [system/indexes/source-depth-map.md](system/indexes/source-depth-map.md) as the
   current cross-disease owner.
2. Review [inbox/obesity/content-precision-promotion-batch-20260515.md](inbox/obesity/content-precision-promotion-batch-20260515.md).
3. The best content-side next move is deeper extraction of `src-obesity-008` or
   `src-obesity-001`, not generic broad thickening.
4. Stage any judgment-heavy write-back through `inbox/` before promoting durable changes.

If continuing ordinary-user UI:

1. Preserve the expert-review loop as an expander under answers.
2. Keep expert review visibly separate from source evidence.
3. Do not hide provenance, uncertainty, or confidence to make answers feel smoother.

## Files To Read First

1. [HANDOFF.md](HANDOFF.md)
2. [system/indexes/expert-answer-review-prototype-20260514.md](system/indexes/expert-answer-review-prototype-20260514.md)
3. [scripts/expert_review.py](scripts/expert_review.py)
4. [scripts/app.py](scripts/app.py)
5. [scripts/test_query.py](scripts/test_query.py)
6. [scripts/health.py](scripts/health.py)
7. [system/indexes/source-depth-map.md](system/indexes/source-depth-map.md)
8. [inbox/obesity/content-precision-promotion-batch-20260515.md](inbox/obesity/content-precision-promotion-batch-20260515.md)
9. [system/health-checks/health-report-20260515.md](system/health-checks/health-report-20260515.md)

## Do Not Do

- Do not revert the uncommitted expert-review/source-depth changes.
- Do not treat expert-review prompt output as source evidence.
- Do not cron expert-review judgments.
- Do not reopen CKD/FIP/HCM/IBD generic source-card thickening.
- Do not turn obesity partial cards into answer evidence without deeper extraction.
- Do not create obesity compiled guidance while `Obesity compiled guidance gate` would fail.
- Do not kill the existing `8501` process unless the user explicitly asks.

## One Line

The next model should preserve the new manual expert-review prompt surface, keep it
below the evidence boundary, and use the synced source-depth map as the current
content-state owner before choosing any new densification work.
