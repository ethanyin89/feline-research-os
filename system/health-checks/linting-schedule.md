---
id: linting-schedule
type: protocol
topic: system
language: bilingual
last_compiled_at: 2026-06-02
owner: jiawei
status: active
---

# Linting Schedule

## 目的 / Purpose

把 health check 从事件驱动（一次性爆发）变成周期性维护。
Convert health checks from event-driven (one-time bursts) to periodic maintenance.

Prior pattern: 3 health check reports all on 2026-04-08, then nothing.
Current pattern: `scripts/health.py` is the single health entrypoint and is run by the existing daily launchd job. Keep per-batch manual review for source-deepening judgment, but do not create separate cron jobs for checks already covered by `health.py`.

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

## Trigger 2 — Daily Automated Health

**When:** Daily via the existing launchd health job.
**What to run:** `python3 scripts/health.py`
**Output file:** `system/health-checks/health-report-<YYYYMMDD>.md`

Current `health.py` covers:
- [x] markdown links
- [x] query tests
- [x] ordinary-user vault eval for default free-mode answer surfaces
- [x] source-card inventory and schema
- [x] source-link proof
- [x] compiled source refs and reader-page `source_ids`
- [x] thin-source caveats
- [x] traceability gates
- [x] language-QA gates
- [x] decision-grade gates
- [x] inbox backlog
- [x] acceptance report status
- [x] compile-trigger drift
- [x] API-key presence

The ordinary-user vault eval is intentionally no-API. It currently runs:

```bash
.venv/bin/python scripts/ordinary_user_vault_eval.py
```

through `scripts/health.py`, and should show:

```text
Ordinary-user vault eval | PASS | All ordinary-user free-mode samples passed without API calls.
```

Estimated manual review time after a clean report: 5-10 min.

---

## Report Naming Convention

```
health-report-YYYYMMDD.md                — current scripted health report
health-check-report-YYYYMMDD-round<N>.md — older/manual round reports
```

All reports go in `system/health-checks/`.

---

## Health Check History

| Date       | Trigger    | Rounds | Key Findings |
|-----------|------------|--------|-------------|
| 2026-04-08 | Event      | 3      | Initial system audit; schema and protocol established |
| 2026-05-17 | Daily health | —    | `scripts/health.py` established as single report entrypoint; launchd daily execution active |
| 2026-06-02 | Daily health | —    | ordinary-user free-mode vault eval included in `health.py` |

---

## Using health-check-template.md

The older `system/health-checks/health-check-template.md` remains useful for deep manual audits.
For routine checks, run `python3 scripts/health.py` first and use template-driven review only when the scripted report surfaces a structural issue or a source-deepening batch needs judgment.
