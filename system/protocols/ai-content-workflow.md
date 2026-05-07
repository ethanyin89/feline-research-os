---
id: ai-content-workflow
type: protocol
topic: system
language: bilingual
last_compiled_at: 2026-04-11
owner: jiawei
status: active
---

# AI Content Workflow — Inbox Staging Protocol

## 目的 / Purpose

防止 AI 生成内容直接写入 live wiki，确保进入 topics/ 和 entities/ 的内容经过人工确认。

Prevent AI-generated content from writing directly to the live wiki.
All LLM-compiled wiki pages stage in `inbox/` first.
Human review gates promotion to `topics/` or `entities/`.

This is the Karpathy "clean vault / dirty vault" pattern adapted for solo use.

---

## Scope / 适用范围

**Applies to:** All new or substantially revised pages in `topics/` and `entities/`.

**Does NOT apply to:**
- `outputs/` files (briefings, slides, qa) — these are ephemeral outputs, not wiki content
- `raw/` files — source cards are inputs, not compiled wiki
- `system/` files — operational files edited directly

---

## Workflow / 流程

### Step 1 — AI writes to inbox/

AI-generated wiki pages land in:
```
inbox/<disease>/         e.g. inbox/ckd/
inbox/entities/<type>/   e.g. inbox/entities/mechanisms/
```

Naming: same filename as the target destination.
Example: `inbox/ckd/mechanism-overview.md` → will promote to `topics/ckd/mechanism-overview.md`

### Step 2 — Human spot-check

Before promoting, verify:
- [ ] Factual claims have provenance tags (`[quoted_fact]`, `[source_supported_conclusion]`, `[llm_inference]`)
- [ ] No unsupported assertions in sections that should be `quoted_fact`
- [ ] `source_ids` in frontmatter match actual loaded sources
- [ ] No obvious contradictions with existing wiki pages
- [ ] Language QA passed (if bilingual)

The check does not need to be exhaustive — it is a sanity gate, not a full review.
Spot-check 2-3 claims per page against the source cards they cite.

### Step 3 — Promote or reject

**Promote:** Move file from `inbox/` to target directory. Update frontmatter:
```yaml
verification_status: human-reviewed
last_compiled_at: <date>
```

**Reject:** Move file to `inbox/rejected/` with a one-line note at the top:
```
<!-- REJECTED: <reason> — <date> -->
```
Do not delete. Keep for reference in case the content is partially useful later.

### Step 4 — Clear inbox

After each compile-and-review batch, `inbox/` (excluding `inbox/rejected/`) should be empty.
A non-empty `inbox/` is a signal that staging is backed up.

---

## Exceptions / 例外

- **Emergency hotfix**: If a factual error in a live wiki page is found, it can be edited directly
  without going through inbox/. Note the change in the next health check report.
- **Minor edits** (typo, frontmatter field update, link fix): Direct edit is fine. No staging needed.
- **Major rewrites**: Always stage in inbox/ even if rewriting an existing page.

---

## inbox/ Directory Structure

```
inbox/
  ckd/           — staged CKD topic pages
  fip/           — staged FIP topic pages
  hcm/           — staged HCM topic pages
  ibd/           — staged IBD topic pages
  entities/
    mechanisms/
    models/
    endpoints/
    diseases/
    ...
  rejected/      — rejected drafts with rejection notes
```
