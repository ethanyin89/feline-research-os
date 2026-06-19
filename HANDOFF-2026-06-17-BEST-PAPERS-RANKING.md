# HANDOFF: Research Mode "Best Papers" 排序标准定义

**Date:** 2026-06-17
**Branch:** idea-chatacademia-research-workbench
**Status:** COMPLETE

---

## Summary

定义了 Research Mode 中 "Best Papers" 排序标准，解决用户问题："为什么这篇排在前面？"

**设计原则**: 排序必须有明确、可解释、可审计的标准。

---

## What Was Built

### 1. 排序公式 (DESIGN.md)

```
ranking_score = (evidence_level × 0.35) + (recency × 0.25) +
                (source_kind × 0.25) + (extraction_depth × 0.15)
```

四个排序因子：

| 因子 | 权重 | 说明 |
|------|------|------|
| Evidence Level | 35% | 循证医学金字塔（meta-analysis > systematic-review > RCT > original-study） |
| Recency | 25% | 年份分档（2024-2026 → 10分，逐档递减） |
| Source Kind | 25% | 文献类型（guideline > paper > review > regulatory > product-info） |
| Extraction Depth | 15% | 提取深度（有 quoted_facts → 10分，仅元数据 → 3分） |

### 2. 用户提供的文献类型映射

| 用户命名 | 系统 source_kind | 分数 |
|----------|------------------|------|
| 综述 | `review-article` | 6 |
| 产品说明 | `product-info` | 3 |
| 宣传 | `marketing` | 1 |
| 监管 | `regulatory` | 5 |
| 论文 | `paper` | 7 |
| 内部文档 | `internal-doc` | 2 |

### 3. 可选加成因子

| 字段 | 加成 |
|------|------|
| citation_count ≥ 100 | +0.5 |
| impact_factor ≥ 5 | +0.3 |

（当前仅作为设计预留，citation_count 数据在 citation-graph.json 中仅部分覆盖）

### 4. 代码实现 (`research_mode.py`)

更新 `rank_sources()` 函数，从简单的 tuple 排序改为加权公式：

```python
def rank_sources(cards: list[SourceCard], top_n: int = 10) -> list[SourceCard]:
    """
    Rank sources using the 4-factor weighted formula defined in DESIGN.md.
    """
    def compute_score(card: SourceCard) -> float:
        evidence_score = evidence_scores.get(card.evidence_level or "", 0)
        recency_score = ...  # 按年份分档
        kind_score = kind_scores.get(card.source_kind or "", 5)
        depth_score = ...    # 按提取深度分档

        return (
            evidence_score * 0.35 +
            recency_score * 0.25 +
            kind_score * 0.25 +
            depth_score * 0.15
        )

    ranked = sorted(cards, key=compute_score, reverse=True)
    return ranked[:top_n]
```

---

## Python 3.9 Compatibility Fixes

同时修复了多个 Python 3.10+ 类型语法问题（`dict | None` → `Optional[dict]`）：

| 文件 | 修复 |
|------|------|
| `scripts/query.py` | `_CITATION_GRAPH_CACHE` 类型注解 |
| `scripts/compile_trigger.py` | `_extract_source_id` 返回类型 |
| `scripts/run_acceptance_checklist.py` | `summarize_row`, `render_question_block` 参数类型 |

---

## Tests

All tests pass: **113/113**

---

## Files Changed

| File | Changes |
|------|---------|
| `DESIGN.md` | +80 lines — 新增 "Research Mode — Best Papers 排序标准" 完整规范 |
| `scripts/research_mode.py` | 重写 `rank_sources()` 函数 |
| `scripts/compile_trigger.py` | Python 3.9 兼容性修复 |
| `scripts/run_acceptance_checklist.py` | Python 3.9 兼容性修复 |

---

## User Context

用户问题原文：
> "目前仔细想来，比如说research mode，用户或者内部研究者输入这个query是为了拿到什么东西呢？按照【Best recent papers...】来处理的是没有问题的，不过是否有定义过best的标准。"

用户提供的参考信息：
- 文献类型：综述、产品说明、宣传、监管、论文、内部文档
- 已有维度：引用、影响因子、IF

用户选择：**先定义标准**，再实现。

---

## What's Next

1. **UI 标签显示**: 在 Research Mode 输出中显示关键排序因子标签（如 `[综述]`、`[2024]`）
2. **Citation bonus 集成**: 当 citation-graph.json 数据更完整时，启用高引用加成
3. **Impact factor 字段**: 如果在 source cards 中添加 IF 字段，可启用期刊加成

---

## Verification Commands

```bash
# Check syntax
python3.9 -m py_compile scripts/research_mode.py scripts/query.py

# Run tests
python3.9 scripts/test_query.py

# Check DESIGN.md update
grep -A 5 "Research Mode.*Best Papers" DESIGN.md
```

---

## Related Documents

- DESIGN.md (新增 "Research Mode — Best Papers 排序标准" section)
- PLAN-researcher-presentation-layer.md (整体 Presentation Layer 规划)
- HANDOFF-2026-06-17-P3-REFERENCE-GRAPH.md (P3 Citation Graph 实现)
