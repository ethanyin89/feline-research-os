# Handoff: ChatAcademia Research Workbench + Content Layer

**Date:** 2026-06-09
**Status:** ChatAcademia infrastructure complete; content maintenance mode

---

## Session Summary

### 1. ChatAcademia Research Workbench — COMPLETE

基于 II (Intelligent Internet) 材料实现的 Feline-RALPH harness loop 已完成：

| 模块 | 文件 | 状态 |
|------|------|------|
| Schemas | `core/schemas.py` | ✓ |
| Record Store | `core/record_store.py` | ✓ |
| Evidence Card | `core/evidence_card.py` | ✓ |
| Task Evaluator | `core/task_evaluator.py` | ✓ |
| Gap Checker | `core/gap_checker.py` | ✓ |
| Verifier | `core/verifier.py` | ✓ |
| Harness Loop | `scripts/harness_loop.py` | ✓ |
| Research Record UI | `scripts/research_record_ui.py` | ✓ |
| Benchmark Runner | `scripts/benchmark_runner.py` | ✓ |

**Benchmark:** 20/20 (100% pass rate)

**Merge Guide:** `MERGE-GUIDE-CHATACADEMIA.md`

等待 Codex usage 恢复后进行合并协调。

### 2. FIP Treatment Guidance Updated

更新 `topics/fip/what-is-fip.md` 加入 molnupiravir：

- 新增 src-fip-028 到 source_ids
- 新增量化追溯：两药等效 (118 cats, p=0.326)
- 治疗段落列出 GS-441524 和 molnupiravir 为等效选项

---

## Current Vault State

### Source Cards: 541 total

| Disease | Total | Deep Extracted | Abstract Weighted | Title Only |
|---------|-------|----------------|-------------------|------------|
| cancer | 102 | 9 | 89 | 1 |
| ckd | 50 | 28 | 19 | 1 |
| diabetes | 118 | 24 | 85 | 8 |
| fcv | 103 | 24 | 79 | 0 |
| fip | 28 | 26 | 2 | 0 |
| hcm | 24 | 24 | 0 | 0 |
| ibd | 24 | 24 | 0 | 0 |
| obesity | 92 | 4 | 80 | 7 |

### What-Is Pages: 8/8 complete

所有疾病模块都有双语 what-is 页面。

### Health Check Status

| Check | Status |
|-------|--------|
| Query tests | PASS (111/111) |
| Paper source cards | PASS (541) |
| Low-word cards | PASS |
| Source schema | PASS |
| Markdown links | FAIL (2 template placeholders - false positive) |
| Ordinary-user eval | FAIL (eval script issue) |

---

## Available Work (No Blockers)

### 1. Structured Abstract Extraction — BLOCKED

17 个 title_only 源卡已验证无法从 Crossref/PubMed 恢复 abstract：

| Disease | Count | Verified Blocker |
|---------|-------|------------------|
| diabetes | 8 | src-diabetes-084 (PMID 3538892, 1986, pre-abstract era) |
| obesity | 7 | src-obesity-073 (PMID 30375945, consensus doc, no abstract) |
| cancer | 1 | 1981年文献 |
| ckd | 1 | 无 PubMed 记录 |

**Session 验证：** 尝试 Crossref + PubMed API 查询，确认这些源卡需要全文访问才能升级。

### 2. Deep Extraction Upgrades

355 个 abstract_weighted 源卡可升级到 deep_extracted：

| Disease | Abstract Weighted |
|---------|-------------------|
| cancer | 89 |
| diabetes | 85 |
| obesity | 80 |
| fcv | 79 |
| ckd | 19 |
| fip | 2 |

**Blocker:** 需要全文访问权限。

### 3. Skill Maintenance

已固化的技能：

| Skill | File | Samples |
|-------|------|---------|
| `/literature-sheet-intake` | `.claude/skills/literature-sheet-intake.md` | 33+ |
| `/doi-recovery` | `.claude/skills/doi-recovery.md` | CKD batch |
| `/structured-abstract-extract` | `.claude/skills/structured-abstract-extract.md` | 54 |
| `/what-is-page` | `.claude/skills/what-is-page.md` | 5 |
| `/low-word-card-enrich` | `.claude/skills/low-word-card-enrich.md` | 5 |

---

## Blocked Work

### Full Text Access Needed

| Category | Sources | Notes |
|----------|---------|-------|
| FIP ML diagnosis | src-fip-025 | 2024 ML paper |
| FIP molnupiravir trial | src-fip-027 | Clinical trial |
| CKD extension | src-ckd-047, src-ckd-049, src-ckd-032 | Priority sources |
| Cancer deep extraction | 89 sources | abstract_weighted |
| Obesity Tier 2 | src-obesity-080 | Weight loss microbiome |

### Google Sheet Access

Google Sheet CSV export 返回 "Page Not Found"（可能权限变化）。最后验证的计数：
- FCV: 106+ entries
- Diabetes/Obesity: 289 entries

---

## Key Files

### New This Session

| File | Purpose |
|------|---------|
| `MERGE-GUIDE-CHATACADEMIA.md` | Codex 合并协调指南 |
| `ARCHITECTURE.md` | 六层架构文档 |
| `core/*.py` | ChatAcademia 核心模块 |
| `scripts/harness_loop.py` | Harness loop 包装器 |
| `scripts/research_record_ui.py` | Research Records UI |
| `scripts/benchmark_runner.py` | 20 题基准测试 |

### Modified This Session

| File | Change |
|------|--------|
| `topics/fip/what-is-fip.md` | 新增 molnupiravir |
| `scripts/app.py` | 集成 harness loop |
| `core/task_evaluator.py` | 改进中英文 pattern |

---

## Next Session Priorities

### P0: Codex Merge Coordination
- 等待 Codex usage 恢复
- 读取 `MERGE-GUIDE-CHATACADEMIA.md` 了解集成点
- 合并任何 Codex 并行工作（agent profiles, prompts, visual direction）

### P1: Content Layer
- ~~尝试 title_only → abstract_weighted 升级（17 sources）~~ **BLOCKED** — 本 session 验证无法从 API 恢复
- 如有全文访问，执行 deep extraction
- Obesity 模块需要 Tier 2 deep extraction 才能进入 synthesis 阶段

### P2: Test Page Validation
- 验证 FIP 治疗更新在测试页正确显示
- 修复 ordinary-user eval script 问题

---

## Commands Reference

```bash
# Health check
python3 scripts/health.py

# Query tests
python3 scripts/test_query.py

# Benchmark
python3 scripts/benchmark_runner.py

# Run Streamlit app
streamlit run scripts/app.py

# Run public test page
python3 scripts/public_test_app.py --port 8080
```

---

## Content Layer Deep Dive

### Module Maturity

| Disease | Synthesis Index | Deep Extracted | Status |
|---------|-----------------|----------------|--------|
| cancer | 2026-06-03 | 9/102 | active |
| ckd | 2026-04-10 | 28/50 | active |
| diabetes | 2026-04-24 | 24/118 | active |
| fcv | 2026-04-30 | 24/103 | active |
| fip | 2026-04-22 | 26/28 | active |
| hcm | 2026-04-24 | 24/24 | complete |
| ibd | 2026-04-28 | 24/24 | complete |
| obesity | **NONE** | 4/92 | source-indexed |

**Obesity Next Steps (blocked on full text):**
- Deep-extract Tier 2 sources (002, 003, 006, 007, 080)
- Compile bilingual architecture pages
- Write assessment-methods page

### Title-Only Recovery Attempt

本 session 验证了 17 个 title_only 源卡无法从 Crossref/PubMed 升级：

| Source | Verification |
|--------|--------------|
| src-diabetes-084 | PMID 3538892 exists, 1986 paper has no abstract |
| src-obesity-073 | PMID 30375945 exists, consensus doc has no abstract |
| Others | No DOI/PMID or Crossref has no abstract |

---

## Session Metrics

| Metric | Value |
|--------|-------|
| Source cards | 541 |
| Query tests | 111/111 |
| Benchmark | 20/20 |
| What-is pages | 8/8 |
| Skills codified | 5 |
| Title-only verified blocked | 17 |
