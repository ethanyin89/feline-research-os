# Handoff

If you are a new model taking over this repo because of token loss, model switch, or usage limit, do this first.

## Current Override, 2026-06-25

The current production-facing branch is `main`.

Read this current handoff first:

- [HANDOFF-2026-06-25-SOURCE-GROUNDED-RESEARCH-WORKSPACE.md](HANDOFF-2026-06-25-SOURCE-GROUNDED-RESEARCH-WORKSPACE.md) — Homepage radical simplification + conclusion-first results + evidence trace infrastructure
- [deep-extraction-v3-handoff-20260622-next.md](file:///Users/jiawei/Desktop/insclaude/feline-research-os/system/handoffs/deep-extraction-v3-handoff-20260622-next.md)
- [HANDOFF-2026-06-21-CONSOLIDATED.md](HANDOFF-2026-06-21-CONSOLIDATED.md)
- [HANDOFF-2026-06-20-DEEP-EXTRACTION-COMPLETE.md](HANDOFF-2026-06-20-DEEP-EXTRACTION-COMPLETE.md)
- [HANDOFF-2026-06-19-RESEARCH-MODE-PRESENTATION-DEPTH-QUEUE.md](HANDOFF-2026-06-19-RESEARCH-MODE-PRESENTATION-DEPTH-QUEUE.md)

Current shipped state:

- **Homepage simplified:** "今天想研究什么？" replaces verbose "证据研究工作台". Only title + input + modes + examples on main area.
- **Result page conclusion-first:** Direct conclusion displayed first, details in expanders (not 5-tab layout).
- **Evidence trace infrastructure:** EvidenceTrace dataclass for claim-level source passage tracing.
- Deep extraction resolved for 5 key placeholder sources (`src-ckd-128`, `src-hcm-169`, `src-fip-070`, `src-diabetes-035`, `src-obesity-039`) with complete abstracts, methods summaries, clinical findings, and safety boundaries.
- Research Mode output is Chinese-first with an English report preserved.
- Reader-facing research recommendations should not expose internal `src-*` IDs.
- Title-only / placeholder records are excluded from main recommendations and routed to `system/indexes/research-depth-queue.*`.
- Current HEAD is `47b3428` on `main`.


## Authoritative Current State

Read this file before every other handoff:

- [HANDOFF-2026-06-17-BEST-PAPERS-RANKING.md](HANDOFF-2026-06-17-BEST-PAPERS-RANKING.md) — Research Mode "Best Papers" 排序标准定义: 4-factor weighted formula (evidence_level 35%, recency 25%, source_kind 25%, extraction_depth 15%)
- [HANDOFF-2026-06-17-P3-REFERENCE-GRAPH.md](HANDOFF-2026-06-17-P3-REFERENCE-GRAPH.md) — P3 Reference Graph complete: citation-graph.json index, vault status indicators, "Cited By" display
- [HANDOFF-2026-06-17-RESEARCH-MODE-IMPLEMENTATION.md](HANDOFF-2026-06-17-RESEARCH-MODE-IMPLEMENTATION.md) — Research Mode (agent.ii.inc style) implemented, presentation layer fixes, 13 screenshots discussion context preserved

For legacy worktree state (outdated):
- [HANDOFF-2026-06-11-WORKTREE-STATE.md](HANDOFF-2026-06-11-WORKTREE-STATE.md) — historical worktree inventory

## Latest Session Handoff

After the authoritative handoff, use these for historical context:

- [HANDOFF-2026-06-17-BEST-PAPERS-RANKING.md](HANDOFF-2026-06-17-BEST-PAPERS-RANKING.md) — Research Mode "Best Papers" ranking standard with explicit 4-factor formula
- [HANDOFF-2026-06-17-P3-REFERENCE-GRAPH.md](HANDOFF-2026-06-17-P3-REFERENCE-GRAPH.md) — P3 Reference Graph: citation graph index, reference links with vault status, "Cited By" display
- [HANDOFF-2026-06-17-RESEARCH-MODE-IMPLEMENTATION.md](HANDOFF-2026-06-17-RESEARCH-MODE-IMPLEMENTATION.md) — Research Mode with PubMed integration, presentation layer formatting, context loss root cause analysis
- [HANDOFF-2026-06-15-BILINGUAL-CKD-INDEX-ROUTING.md](HANDOFF-2026-06-15-BILINGUAL-CKD-INDEX-ROUTING.md) — Bilingual CKD Topic Index implemented, routed and verified for Chinese/bilingual sessions (all checks PASS)
- [HANDOFF-2026-06-15-GATE6D-SEARCH-INDEX-OPTIMIZATION.md](HANDOFF-2026-06-15-GATE6D-SEARCH-INDEX-OPTIMIZATION.md) — Gate 6D Search Index optimization implemented & health checker timeout updated (all checks PASS)
- [HANDOFF-2026-06-15-GATE6A-AUTOPLAN-APPROVED.md](HANDOFF-2026-06-15-GATE6A-AUTOPLAN-APPROVED.md) — Gate 6A/B/C /autoplan approved with sequence diagram, UI state table, bilingual labels, and implementation wire-up
- [HANDOFF-2026-06-15-CONTENT-COMPILATION.md](HANDOFF-2026-06-15-CONTENT-COMPILATION.md) — Content compilation updates
- [HANDOFF-2026-06-15-GATE6A-SCHEMA.md](HANDOFF-2026-06-15-GATE6A-SCHEMA.md) — Schema updates for Gate 6A
- [HANDOFF-2026-06-12-PHASE6-PRESENTATION-CLOSEOUT.md](HANDOFF-2026-06-12-PHASE6-PRESENTATION-CLOSEOUT.md) — latest Phase 6 implementation, local page QA, hosted acceptance boundary, and restart sequence
- [HANDOFF-2026-06-12-PHASE6-AUTOPLAN-REVIEW.md](HANDOFF-2026-06-12-PHASE6-AUTOPLAN-REVIEW.md) — approved gated plan and product-safety decisions
- [HANDOFF-2026-06-12-POST-PHASE5.md](HANDOFF-2026-06-12-POST-PHASE5.md) — result-presentation static adapter state before Phase 6
- [HANDOFF-2026-06-11-RESEARCH-CASE-VALIDATION.md](HANDOFF-2026-06-11-RESEARCH-CASE-VALIDATION.md) — Persisted Research Case integrity gate and real CKD case validation
- [HANDOFF-2026-06-11-II-COMMONS-CONTINUATION.md](HANDOFF-2026-06-11-II-COMMONS-CONTINUATION.md) — Search-depth execution contract completed for the June 6 Research OS lane
- [HANDOFF-2026-06-11-MODULE-DEEPENING.md](HANDOFF-2026-06-11-MODULE-DEEPENING.md) — committed module deepening chronology
- [HANDOFF-2026-06-11-EXTENDED-COMPLETION.md](HANDOFF-2026-06-11-EXTENDED-COMPLETION.md) — diabetes extension chronology
- [HANDOFF-2026-06-11-FINAL-SESSION.md](HANDOFF-2026-06-11-FINAL-SESSION.md) — earlier completion snapshot; not current worktree truth
- [HANDOFF-2026-06-09-KARPATHY-GAP-NARROWED.md](HANDOFF-2026-06-09-KARPATHY-GAP-NARROWED.md) — Gap narrowed from 334 → 63 sources
- [HANDOFF-2026-06-09-CHATACADEMIA-CONTENT.md](HANDOFF-2026-06-09-CHATACADEMIA-CONTENT.md) — ChatAcademia infrastructure complete

For the prior CKD evidence gap review:

- [HANDOFF-2026-06-08-CKD-EVIDENCE-GAP-REVIEW.md](HANDOFF-2026-06-08-CKD-EVIDENCE-GAP-REVIEW.md)

For the June 6 II-Commons-Skills / Research OS direction and its cross-model
usage-limit handoff:

- [HANDOFF-2026-06-06-II-COMMONS-SKILLS.md](HANDOFF-2026-06-06-II-COMMONS-SKILLS.md)

For the prior CKD material completion:

- [HANDOFF-2026-06-06-CKD-MATERIAL-COMPLETION.md](HANDOFF-2026-06-06-CKD-MATERIAL-COMPLETION.md)

For the original CKD sheet intake:

- [HANDOFF-2026-06-05-CKD-SHEET-INTAKE.md](HANDOFF-2026-06-05-CKD-SHEET-INTAKE.md)

For the prior content claim-evidence workbench pass, read:

- [HANDOFF-2026-06-05-CONTENT-CLAIM-EVIDENCE.md](HANDOFF-2026-06-05-CONTENT-CLAIM-EVIDENCE.md)

For the prior business-critical planning handoff, read:

- [HANDOFF-2026-06-04-BUSINESS-CRITICAL-PLAN.md](HANDOFF-2026-06-04-BUSINESS-CRITICAL-PLAN.md)

For the query-architecture and local answer-surface implementation handoff, read:

- [HANDOFF-2026-06-04-QUERY-ARCHITECTURE.md](HANDOFF-2026-06-04-QUERY-ARCHITECTURE.md)

For the two planning artifacts behind the latest product direction, read:

- [PLAN-business-critical-feline-research-os.md](PLAN-business-critical-feline-research-os.md)
- [PLAN-researcher-answer-satisfaction-ckd.md](PLAN-researcher-answer-satisfaction-ckd.md)

For the prior answer quality gate handoff, read:

- [HANDOFF-2026-06-02-ANSWER-QUALITY-GATE.md](HANDOFF-2026-06-02-ANSWER-QUALITY-GATE.md)

For the prior CKD answer mode comparison handoff, read:

- [HANDOFF-2026-06-02-CKD-ANSWER-MODE-COMPARISON.md](HANDOFF-2026-06-02-CKD-ANSWER-MODE-COMPARISON.md)

For the prior cancer abstract extraction sample handoff, read:

- [HANDOFF-2026-06-02-CANCER-ABSTRACT-SAMPLE.md](HANDOFF-2026-06-02-CANCER-ABSTRACT-SAMPLE.md)

For the prior Streamlit/API-cost guard handoff, read:

- [HANDOFF-2026-06-01-STREAMLIT-API-COST-GUARD.md](HANDOFF-2026-06-01-STREAMLIT-API-COST-GUARD.md)

For the prior public-test link refresh handoff, read:

- [HANDOFF-2026-05-25-PUBLIC-TEST-LINK-REFRESH.md](HANDOFF-2026-05-25-PUBLIC-TEST-LINK-REFRESH.md)

For the prior ordinary-user HTTP public test handoff, read:

- [HANDOFF-2026-05-22-ORDINARY-USER-HTTP-PUBLIC-TEST.md](HANDOFF-2026-05-22-ORDINARY-USER-HTTP-PUBLIC-TEST.md)

For the prior Streamlit public-tunnel investigation, read:

- [HANDOFF-2026-05-21-ORDINARY-USER-PUBLIC-TEST.md](HANDOFF-2026-05-21-ORDINARY-USER-PUBLIC-TEST.md)

For the prior public-test recovery step, read:

- [HANDOFF-2026-05-20-ORDINARY-USER-PUBLIC-TEST.md](HANDOFF-2026-05-20-ORDINARY-USER-PUBLIC-TEST.md)

For the prior Karpathy gap-analysis / ordinary-user prep session, read:

- [HANDOFF-2026-05-17-KARPATHY-GAP-ANALYSIS.md](HANDOFF-2026-05-17-KARPATHY-GAP-ANALYSIS.md)

For the prior obesity Tier 1 completion, read:

- [HANDOFF-2026-05-17-OBESITY-TIER1-COMPLETE.md](HANDOFF-2026-05-17-OBESITY-TIER1-COMPLETE.md)

For the prior autoplan gap analysis, read:

- [HANDOFF-2026-05-17-AUTOPLAN-KARPATHY-GAP.md](HANDOFF-2026-05-17-AUTOPLAN-KARPATHY-GAP.md)

For the prior expert-review / obesity-gate handoff, read:

- [HANDOFF-2026-05-16-EXPERT-REVIEW-OBESITY-GATE.md](HANDOFF-2026-05-16-EXPERT-REVIEW-OBESITY-GATE.md)

For the prior expert-review / source-depth handoff, read:

- [HANDOFF-2026-05-15-EXPERT-REVIEW-SOURCE-DEPTH.md](HANDOFF-2026-05-15-EXPERT-REVIEW-SOURCE-DEPTH.md)

For the previous ordinary-user presentation handoff, read:

- [HANDOFF-2026-05-07-CONTENT-PRESENTATION.md](HANDOFF-2026-05-07-CONTENT-PRESENTATION.md)

For the longer session log behind it, read:

- [HANDOFF-2026-05-06-SESSION-2.md](HANDOFF-2026-05-06-SESSION-2.md)

## Task Type

This is a `plan`, not a narrow blocker check.

The current repo-level job is no longer "continue only the CKD image gate".
The current job is to hold two tracks at once:

1. `325-source content pipeline` (7 disease modules)
2. `ordinary-user usage surface`

## Read These 4 Files

1. [Two-track operating plan, 2026-04-18](system/indexes/two-track-operating-plan-20260418.md)
2. [Karpathy alignment handoff, 2026-04-18](system/indexes/karpathy-alignment-handoff-20260418.md)
3. [UX improvement handoff, 2026-04-18](system/indexes/ux-improvement-handoff-20260418.md)
4. [Content vs frontend collaboration plan](system/indexes/content-vs-frontend-collaboration-plan.md)

If you are continuing the content line specifically, also read:

5. [Content-side densification queue](system/indexes/content-side-densification-queue.md)
6. [120 source processing ledger, 2026-04-21](system/indexes/source-processing-ledger-120-20260421.md)
7. [Legacy 96 source processing ledger, 2026-04-21](system/indexes/legacy-96-source-processing-ledger-20260421.md)
8. [Cross-disease source depth map](system/indexes/source-depth-map.md)

If you are continuing the ordinary-user line specifically, also read:

9. [Ordinary-user LLM wiki usability audit, 2026-04-10](system/indexes/ordinary-user-llm-wiki-usability-audit-20260410.md)

## 30-Second Reality (Updated 2026-06-17)

- The repo has `1414` strict disease paper cards across 8 disease modules.
- All tests pass: `127/127` (113 query + 4 research + 10 intent classification).
- Research Mode (agent.ii.inc style) implemented with PubMed integration.
- **P4 Decision Tree UI complete:** intent classification, decision tree index, example questions (basic + research).
- **P3 Reference Graph complete:** citation-graph.json, vault status indicators, "Cited By" display.
- Current HEAD is on `idea-chatacademia-research-workbench`.
- Active plan: `PLAN-researcher-presentation-layer.md` (P1/P3/P4 complete)
- Design doc: `~/.gstack/projects/feline-research-os/idea-chatacademia-research-workbench-design-20260617.md`
- Health report: `system/health-checks/health-report-20260617.md`
- QA report: `.gstack/qa-reports/qa-report-localhost-2026-06-17.md` (health score 95/100, no dead links)

## Verify In 4 Commands

```bash
python3 scripts/test_query.py
python3 -m py_compile scripts/app.py scripts/search.py scripts/query.py
find raw/images -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \) | sort
python3 - <<'PY'
from pathlib import Path
import re
root = Path('raw/papers')
for disease in ['ckd', 'fip', 'hcm', 'ibd', 'diabetes', 'fcv', 'obesity']:
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

## Default Owner Split

- content side owns truth, evidence, write-back, queue reality, and system state
- frontend side owns presentation, interaction, and ordinary-user polish

Do not silently let frontend edits rewrite truth claims.
Do not let content work drift back into presentation-only cleanup unless the user asks.

## Default Next Move

If no one has given a narrower instruction, the safest default is:

1. continue the content line
2. continue only full-text / official-source / image-table / output-specific precision; do not reopen generic source-card thickening for any of the seven disease modules
3. stage write-back through `inbox/`
4. refresh broader system owners like `source-depth-map` only after this batch is coherent

## Do Not Regress To

- "continue only the CKD image gate"
- treating presentation polish as the content-side default
- re-opening architecture decisions that are already locked
- re-asking the user for confirmation on repeated source-card processing steps

## One Line

Do not continue "the old blocker".
Continue `the two-track repo plan`.
