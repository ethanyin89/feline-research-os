---
id: handoff-20260428-session3
type: handoff
created_at: 2026-04-28
session_focus: content-health-live-acceptance-hardening
status: complete
---

# 交接文档 / Handoff Document — 2026-04-28 (Session 3)

## 本次会话完成内容 / Completed This Session

### 1. 项目状态检查与任务归类 / Project State Review

根据用户要求，先查看项目执行情况和接力文档，并按 `$autoplan` 判断任务类型。

**判断结果 / Classification:** 本轮属于 **检查 + 内容优化执行**，不是纯想法、方案或故障排查。实际流程为先验收当前结构，再修复健康检查和 Ask the Vault 可用性问题。

已阅读的关键上下文包括：

- `HANDOFF-2026-04-27-SESSION.md`
- `system/indexes/handoff-20260428.md`
- `system/indexes/handoff-20260428-session2.md`
- `CLAUDE.md`
- `README.md`
- `PLAN.md`
- 当日 health report 与 acceptance report

### 2. 内容健康检查修复 / Content Health Cleanup

已补齐并标准化高可见双语页面的结构字段，使 health checker 能稳定识别。

主要修复：

- 统一 `## Key-Claim Traceability` 标题。
- 统一 `## Quantified Claim Traceability` 标题。
- 为高可见双语页面补充 `language_qa_status: bilingual_checked`。
- 补充 `language_qa_notes`，明确这些页面已完成中英一致性审阅。
- 修复部分页面中标题不完全匹配导致的误报。

重点涉及页面分布：

- `topics/ckd/`
- `topics/diabetes/`
- `topics/fcv/`

### 3. Ask the Vault 运行链路修复 / Ask the Vault Runtime Fixes

本轮重点修复了自动验收中暴露出的真实查询链路问题。

已修改 `scripts/run_acceptance_checklist.py`：

- 子查询不再硬编码调用 `python3`。
- 改为使用 `sys.executable`，确保 `.venv` 内的依赖和当前运行环境一致。

已修改 `scripts/query.py`：

- 增加 frontmatter `source_ids` 解析。
- 支持 inline list 与 block list 两种 source ID 写法。
- 增加 compiled page frontmatter source fallback，避免页面内容能加载但 provenance 无法回填。
- 增加相对路径解析，支持从当前页面解析 `../../topics/...` 这类链接。
- 调整 query type 判定顺序，使 recognition、boundary、recognition+endpoints 优先于 endpoints 或 synthesis。
- 增加 `FIRST_FAMILY` stderr 元数据，方便 acceptance 判断首个加载家族是否符合预期。

这些修复解决了 HCM recognition、IBD boundary、source provenance 和 route miss 问题。

### 4. 回归测试补强 / Regression Test Hardening

已修改 `scripts/test_query.py`，补充并纳入测试入口：

- recognition 查询优先于 endpoints 的路由回归。
- IBD boundary 查询不应被误判为 synthesis 的路由回归。
- frontmatter source IDs inline list 解析。
- frontmatter source IDs block list 解析。
- 缺失 source IDs 时返回空列表。

当前查询测试结果：

```bash
.venv/bin/python scripts/test_query.py
```

结果：`84 passed | 0 failed | 84 total`

### 5. Live Acceptance 验收 / Live Acceptance

已使用 OpenRouter 后端执行真实 Ask the Vault acceptance。

命令：

```bash
OPENROUTER_DAILY_BUDGET_USD=1.00 OPENROUTER_MODEL=openai/gpt-4.1-mini .venv/bin/python scripts/run_acceptance_checklist.py --backend openrouter
```

结果写入：

- `system/health-checks/ask-the-vault-acceptance-report-20260428.md`

当前状态：

- Acceptance status: `pass`
- Automated answers: `8/8`
- Execution failures: `0`
- Provenance misses: `0`
- Route misses: `0`

## 当前验证状态 / Current Verification State

最新 health report：

```bash
python3 scripts/health.py
```

当前状态：

- Markdown links: PASS
- Query tests: PASS, `84 passed | 0 failed | 84 total`
- Key-claim traceability: PASS
- Quantified claim traceability: PASS
- High-visibility language QA: PASS
- Acceptance report: PASS, mode `executed`, status `pass`
- Compile trigger: PASS
- Next actions: `No immediate structural action from this report.`

Continuation update after FCV source-card work:

- Query tests: PASS, `84 passed | 0 failed | 84 total`
- Health report: PASS across structural checks
- FCV source-card reality: `24/24 full`, `24/24 deep_extracted`
- Compile trigger remains PASS and now reports changed FCV source cards with downstream files to reconcile, which is informational rather than a structural failure.

Continuation update after HCM/IBD source-card status reconciliation:

- HCM source-card reality: `24/24 full`, `24/24 deep_extracted`
- IBD source-card reality: `24/24 full`, `24/24 deep_extracted`
- Overall paper-card reality: all six disease modules are now `24/24 full` and `24/24 deep_extracted`.
- Compile trigger remains PASS and now reports changed source cards with downstream files to reconcile, which should be treated as a topic-page recompilation queue.

Continuation update after downstream status-text reconciliation:

- Cleared stale `17/24`, `23/24`, `source_checked` source-depth wording from current handoff, source-depth, source-index-adjacent, dashboard, maturity, and processing-ledger surfaces.
- HCM, IBD, and FCV current pages now consistently describe the paper-card layer as `24/24 full` and `24/24 deep_extracted`.
- Historical enum/policy pages still mention `source_checked` as a valid verification status by design; those were not changed.
- Compile trigger still reports the same source-card diff queue because it is based on changed source cards in the working tree, not because health failed.

Continuation update after FCV topic-page boundary reconciliation:

- Updated FCV translation and recognition pages to stop referring to generic source-card deep extraction as the next step.
- FCV translation now frames the next work as output-specific compression, full-text/field-effectiveness precision, or product/label evidence when needed.
- FCV vaccine-persistence memo now includes the `src-fcv-013` replication-deficient platform branch with an explicit non-market/non-label boundary.
- FCV index and mechanism overview now say the next work is output-specific topic compression, not more source-card extraction.

Continuation update after output/materials reconciliation:

- Updated HCM slides, briefings, and dossiers so they no longer say only 12 HCM sources have round-1 deep extraction.
- Updated IBD slides from 14-source extraction language to `24/24` round-1 deep extraction coverage.
- Added `src-ibd-009` to IBD briefing/dossier source_ids where pathology/workup materials needed the workflow source in provenance.
- Updated CKD slides, briefings, and dossiers so they no longer say 15 CKD papers or abstract-weighted source cards remain.
- Output materials scan no longer finds stale `12`, `14`, `15`, `23/24`, `17/24`, `source_checked`, or partial-card status language in `outputs/briefings`, `outputs/dossiers`, or `outputs/slides`.

## 关键修复点 / Key Fixes

- Health checker 依赖精确标题匹配，因此 traceability 标题必须保持 `## Key-Claim Traceability` 和 `## Quantified Claim Traceability`。
- 高可见双语页需要 `language_qa_status: bilingual_checked`，否则会被语言 QA 检查标记。
- Ask the Vault 不能只依赖 raw source card 加载，compiled page 的 frontmatter `source_ids` 也必须能回填 provenance。
- 查询路由中 recognition 和 boundary 类问题必须先于 broad synthesis 或 endpoints 判定。
- Acceptance runner 必须使用当前解释器 `sys.executable`，否则 `.venv` 中的 OpenAI/OpenRouter 依赖不会生效。

## 当前真实状态 / Current Reality

项目结构健康状态已经转为绿色，无立即结构性待办。

源卡片深度状态已全部闭合：

- CKD、FIP、HCM、IBD、Diabetes、FCV: 均为 24 张源卡片 full/deep extraction。

图片资产现实状态：

- CKD: 8 张。
- FIP、HCM、IBD、Diabetes: 各 1 张。
- FCV: 0 张。

## 建议下一步 / Suggested Next Steps

最高价值下一步已经不再是 Ask the Vault 基础设施修复，而是按目标选择内容深挖或产品表面优化。

可选方向：

- 优先处理 downstream recompilation queue，使 HCM、IBD、FCV 相关主题页完全吃到最新 `24/24` deep source-card layer。
- 如果目标转向普通用户使用，下一步应优化 Streamlit UI、示例问题、结果解释层和 provenance 展示方式。
- 除非修改了 query/runtime 代码，或用户明确要求，不建议频繁重跑 live OpenRouter acceptance，因为会消耗真实 API 预算。

## 常用命令 / Commands

```bash
cd /Users/jiawei/Desktop/insclaude/feline-research-os
.venv/bin/python scripts/test_query.py
python3 scripts/health.py
OPENROUTER_DAILY_BUDGET_USD=1.00 OPENROUTER_MODEL=openai/gpt-4.1-mini .venv/bin/python scripts/run_acceptance_checklist.py --backend openrouter
```

Live acceptance 需要 OpenRouter key，并受 `OPENROUTER_DAILY_BUDGET_USD=1.00` 预算保护。

## 本轮关键变更文件 / Key Files Changed This Session

- `scripts/query.py`
- `scripts/run_acceptance_checklist.py`
- `scripts/test_query.py`
- `system/health-checks/health-report-20260428.md`
- `system/health-checks/ask-the-vault-acceptance-report-20260428.md`
- `raw/papers/src-hcm-003.md`
- `raw/papers/src-ibd-009.md`
- `system/indexes/src-ibd-009-deep-extraction-round1.md`
- `HANDOFF-2026-04-27-SESSION.md`
- `system/indexes/handoff-20260428.md`
- `system/indexes/handoff-20260428-session2.md`
- `system/indexes/source-depth-map.md`
- `system/indexes/disease-module-maturity-ladder.md`
- `system/indexes/karpathy-gap-analysis.md`
- `system/indexes/source-processing-ledger-120-20260421.md`
- `system/indexes/legacy-96-source-processing-ledger-20260421.md`
- `system/indexes/hcm-source-depth-map.md`
- `system/indexes/ibd-source-depth-map.md`
- `system/indexes/ibd-diagnostic-workup-memo.md`
- `topics/hcm/current-state-dashboard.md`
- `topics/hcm/current-state-dashboard-bilingual.md`
- `topics/hcm/index.md`
- `topics/hcm/mechanism-overview.md`
- `topics/hcm/navigation.md`
- `topics/ibd/current-state-dashboard.md`
- `topics/ibd/index.md`
- `topics/ibd/synthesis-index.md`
- `topics/ibd/synthesis-index-bilingual.md`
- `raw/papers/src-fcv-002.md`
- `raw/papers/src-fcv-005.md`
- `raw/papers/src-fcv-013.md`
- `raw/papers/src-fcv-016.md`
- `raw/papers/src-fcv-019.md`
- `raw/papers/src-fcv-023.md`
- `raw/papers/src-fcv-024.md`
- `system/indexes/fcv-source-depth-map.md`
- `system/indexes/fcv-source-index.md`
- `system/indexes/fcv-reading-plan-round-1.md`
- `system/indexes/fcv-content-handoff-20260424.md`
- `topics/fcv/current-state-dashboard.md`
- `topics/fcv/current-state-dashboard-bilingual.md`
- `topics/fcv/synthesis-index.md`
- `topics/fcv/synthesis-index-bilingual.md`
- `topics/fcv/endpoint-handbook.md`
- `topics/fcv/endpoint-handbook-bilingual.md`
- `topics/fcv/mechanism-overview.md`
- `topics/fcv/mechanism-overview-bilingual.md`
- `topics/fcv/translation-brief.md`
- `topics/fcv/translation-brief-bilingual.md`
- `topics/fcv/risk-and-recognition.md`
- `system/indexes/fcv-vaccine-persistence-boundary-memo.md`
- `topics/fcv/index.md`
- `outputs/slides/out-hcm-slides-20260410-v1-working-en.md`
- `outputs/slides/out-hcm-slides-20260410-v1-en.md`
- `outputs/slides/out-hcm-slides-20260410-v1-zh.md`
- `outputs/slides/out-ibd-slides-20260409-v1-working-en.md`
- `outputs/slides/out-ibd-slides-20260409-v1-en.md`
- `outputs/slides/out-ibd-slides-20260409-v1-zh.md`
- `outputs/slides/out-ckd-slides-20260408-v1-working-en.md`
- `outputs/slides/out-ckd-slides-20260408-v1-en.md`
- `outputs/slides/out-ckd-slides-20260408-v1-zh.md`
- `outputs/briefings/out-hcm-briefing-20260410-round1-working-en.md`
- `outputs/briefings/out-hcm-briefing-20260410-round1-en.md`
- `outputs/briefings/out-hcm-briefing-20260410-round1-zh.md`
- `outputs/dossiers/out-hcm-dossier-20260410-v1-working-en.md`
- `outputs/dossiers/out-hcm-dossier-20260410-v1-en.md`
- `outputs/dossiers/out-hcm-dossier-20260410-v1-zh.md`
- `outputs/briefings/out-ibd-briefing-20260409-round1-working-en.md`
- `outputs/briefings/out-ibd-briefing-20260409-round1-en.md`
- `outputs/briefings/out-ibd-briefing-20260409-round1-zh.md`
- `outputs/dossiers/out-ibd-dossier-20260409-v1-working-en.md`
- `outputs/dossiers/out-ibd-dossier-20260409-v1-en.md`
- `outputs/dossiers/out-ibd-dossier-20260409-v1-zh.md`
- `outputs/briefings/out-ckd-briefing-20260408-round1-working-en.md`
- `outputs/briefings/out-ckd-briefing-20260408-round1-en.md`
- `outputs/briefings/out-ckd-briefing-20260408-round1-zh.md`
- `outputs/dossiers/out-ckd-dossier-20260408-v1-working-en.md`
- `outputs/dossiers/out-ckd-dossier-20260408-v1-en.md`
- `topics/ckd/` 下多篇高可见双语页面
- `topics/diabetes/` 下多篇高可见双语页面
- `topics/fcv/` 下多篇高可见双语页面
