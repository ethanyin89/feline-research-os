---
id: system-codex-next-session-prompt
type: system
topic: operating-system
question_type: workflow
language: bilingual
last_compiled_at: 2026-04-18
owner: jiawei
status: active
---

# Codex Next Session Prompt

这页存放下一个模型直接可用的 prompt。

当前 round 的目标也已经不是：

- `CKD source card deepening`
- `继续补 HCM image-ingest skeleton`

因为这两步都不再是 repo 的真实断点。

当前更需要的是：

`保证多模型接手时不断层，并把 CKD 真实图片落盘推进到能解锁第一轮 vision demo。`

如果需要更完整的 handoff 说明，先读：

- [Model continuity handoff, 2026-04-17](model-continuity-handoff-20260417.md)

如果你已经快到 usage limit，只想要 60 秒接手版，先读：

- [Usage-limit emergency handoff, 2026-04-17](usage-limit-emergency-handoff-20260417.md)

---

## 当前最优先任务：CKD Real Image Extraction Gate

把以下 prompt 直接粘贴给下一个模型：

```text
You are working in this repo:
/Users/jiawei/Desktop/insclaude/feline-research-os

Read these files first (in this order):
1. system/indexes/multi-model-collaboration-boundary.md
2. system/indexes/model-continuity-handoff-20260417.md
3. PLAN.md
4. system/indexes/image-ingest-protocol-20260416.md
5. system/indexes/ckd-image-download-checklist-20260417.md

Current date: 2026-04-17

Your role:
WRITER FOR ONE NARROW SCOPE ONLY

Current round goal:
Advance the CKD pilot from candidate image placeholders to real, verified local assets
that can unlock the first vision-integrated ask-the-vault demo.

Current reality you must respect:
- vision integration code is already implemented
- CKD/FIP/IBD/HCM image-ingest skeleton docs already exist
- raw/images/ckd/ already contains 8 verified CKD assets from src-ckd-001, src-ckd-017, src-ckd-022, and src-ckd-024
- do not redo HCM or other disease skeleton work
- verify state first; do not trust old handoff text if the filesystem now differs

Your write scope:
- raw/images/ckd/
- raw/papers/src-ckd-001.md
- raw/papers/src-ckd-013.md
- raw/papers/src-ckd-017.md
- raw/papers/src-ckd-022.md
- raw/papers/src-ckd-024.md
- system/indexes/ckd-image-download-checklist-20260417.md
- PLAN.md

Forbidden files:
- system/indexes/codex-next-session-prompt.md
- system/indexes/multi-disease-llm-wiki-status-audit-20260410.md
- system/indexes/disease-module-maturity-ladder.md
- system/indexes/cross-disease-densification-queue.md
- system/indexes/content-side-densification-queue.md
- system/indexes/hcm-image-ingest-pilot-20260417.md
- system/indexes/hcm-image-ingest-manifest-20260417.md
- system/indexes/hcm-image-download-checklist-20260417.md
- system/indexes/fip-image-ingest-pilot-20260417.md
- system/indexes/fip-image-ingest-manifest-20260417.md
- system/indexes/fip-image-download-checklist-20260417.md
- system/indexes/ibd-image-ingest-pilot-20260417.md
- system/indexes/ibd-image-ingest-manifest-20260417.md
- system/indexes/ibd-image-download-checklist-20260417.md
- topics/fip/
- topics/ibd/
- topics/hcm/
- scripts/
- outputs/

Hard rule:
- all material must be based on the real source links already present in the source cards
- no fake data is allowed
- before article-label verification, do not claim real fig/table numbers
- do not treat candidate assets as verified evidence

Do:
- work only on the 5 CKD pilot sources already named in the checklist
- continue from the existing src-ckd-001/src-ckd-017/src-ckd-024 assets and only add remaining verified CKD assets under raw/images/ckd/
- update checklist rows from no -> yes only when the file is truly present or verified
- rename candidate assets only after article-label verification is complete
- keep PLAN.md aligned with the real execution state

Do not:
- rewrite the image-ingest architecture
- create new pilot/manifest/checklist docs for other diseases
- change query.py, app.py, tests, or acceptance docs
- widen scope to new sources

If the required PDFs or image files are not available in the environment:
- do not fake progress
- stop after confirming the blocker
- report exactly which source(s) are blocked and why

Verify first with:
- find raw/images -maxdepth 2 -type f | sort
- sed -n '78,100p' PLAN.md
- sed -n '54,72p' system/indexes/ckd-image-download-checklist-20260417.md

At the end, return:
1. which CKD source cards were touched
2. which files were added under raw/images/ckd/
3. which checklist rows changed
4. whether PLAN.md status changed
5. any remaining blockers for the vision demo
```
