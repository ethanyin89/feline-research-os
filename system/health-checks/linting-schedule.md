---
id: linting-schedule
type: protocol
topic: system
language: bilingual
last_compiled_at: 2026-04-11
owner: jiawei
status: active
---

# Linting Schedule

## 目的 / Purpose

把 health check 从事件驱动（一次性爆发）变成周期性维护。
Convert health checks from event-driven (one-time bursts) to periodic maintenance.

Prior pattern: 3 health check reports all on 2026-04-08, then nothing.
Target pattern: recurring cadence at two triggers.

---

## Trigger 1 — Per Batch (after every source deepening batch)

**When:** After completing a deepening pass on 3+ source cards.
**What to run:** Section A only (source layer integrity).
**Output file:** `system/health-checks/health-check-report-<YYYYMMDD>-round<N>.md`

Section A checklist:
- [ ] New source cards have `extraction_depth` field set
- [ ] New verbatim `quoted_fact` entries in frontmatter do not contradict existing topic pages
- [ ] Any new contradictions found → add entry to `conflict-register.md`
- [ ] Any new unresolved questions surfaced → add to `unresolved-questions.md`
- [ ] `source-depth-map.md` updated to reflect new depth tiers

Estimated time: 20-30 min (1 Claude session).

---

## Trigger 2 — Monthly (first of each month)

**When:** Monthly, approximately the 1st.
**What to run:** Full health check using `health-check-template.md`.
**Output file:** `system/health-checks/health-check-report-<YYYYMMDD>-round<N>.md`

Full checklist (from health-check-template.md):
- [ ] Source layer: all source cards have extraction_depth field
- [ ] Compiled layer: topic pages reference correct source_ids; no dead links
- [ ] Consistency: check for contradictions between topic pages on same claims
- [ ] Gaps: identify llm_inference claims that should be upgraded to source_supported_conclusion
- [ ] Conflicts: update conflict-register.md with new entries
- [ ] Unresolved: update unresolved-questions.md
- [ ] Source depth map: update tiers and priority queue
- [ ] question-router.md: check all linked files still exist

Estimated time: 45-60 min (1-2 Claude sessions).

---

## Report Naming Convention

```
health-check-report-YYYYMMDD-round1.md   — first round on that date
health-check-report-YYYYMMDD-round2.md   — second round (if needed)
```

All reports go in `system/health-checks/`.

---

## Health Check History

| Date       | Trigger    | Rounds | Key Findings |
|-----------|------------|--------|-------------|
| 2026-04-08 | Event      | 3      | Initial system audit; schema and protocol established |
| *(next)*   | Per-batch  | —      | After first source deepening batch |

---

## Using health-check-template.md

The existing `system/health-checks/health-check-template.md` is the runbook.
Load it + the current source-depth-map + conflict-register + the disease topic index
as context. Ask Claude to run through the checklist and produce the report.
