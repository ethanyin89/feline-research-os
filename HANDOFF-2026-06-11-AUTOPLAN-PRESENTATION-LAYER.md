# Handoff: /autoplan 呈现层审查 2026-06-11

**Status:** /autoplan 部分完成 — CEO/Design 完成(有顾虑)，Eng/DX 被阻塞
**Branch:** `idea-chatacademia-research-workbench`
**Date:** 2026-06-11
**Plan File:** `PLAN-page-rendering-improvements.md`

---

## /autoplan 审查结果摘要

### Phase 1: CEO Review — DONE_WITH_CONCERNS

**双声共识表:**
```
CEO DUAL VOICES — CONSENSUS TABLE:
═══════════════════════════════════════════════════════════════
  Dimension                           Claude  Codex  Consensus
  ──────────────────────────────────── ─────── ─────── ─────────
  1. Premises valid?                   ❌      ❌     DISAGREE
  2. Right problem to solve?           ⚠️      ⚠️     DISAGREE
  3. Scope calibration correct?        ❌      ❌     DISAGREE
  4. Alternatives sufficiently explored?❌     ❌     DISAGREE
  5. Competitive/market risks covered? N/A     N/A    N/A
  6. 6-month trajectory sound?         ⚠️      ⚠️     DISAGREE
═══════════════════════════════════════════════════════════════
```

**关键发现:**
- 计划混淆了"技术重构"和"视觉品牌重塑"
- 两个模型都建议拒绝/重写计划
- 用户澄清后：参考ii.inc的**呈现逻辑**，不是视觉风格

### Phase 2: Design Review — DONE_WITH_CONCERNS

**设计评分:** 0/6 维度确认

**关键缺失:**
1. **信息层次未定义** — Answer→Reasoning→Inspection的具体规格缺失
2. **12+状态未定义** — loading/partial/error/success状态矩阵缺失
3. **结果页面anatomy未定义** — 具体像素级specs缺失
4. **仍混淆serif/navy** — 需明确约束：保持Geist Sans+暗色

### Phase 3: Eng Review — SKIPPED_BLOCKED

被Design问题阻塞 — 需先完成Visual Hierarchy Spec

### Phase 3.5: DX Review — SKIPPED_BLOCKED

被Design问题阻塞 — 组件API取决于页面结构决策

---

## 用户关键澄清

### 1. 内容呈现逻辑 > 视觉设计

用户原话：
> "对我来说，设计很重要，内容的呈现逻辑更重要。特别是在用户使用时。"
> "都重要，只是权重不一样"

**含义:**
- 内容如何组织给用户看（Answer→Evidence→Sources→Uncertainty）是首要关注点
- 视觉美感是次要的，但仍然重要

### 2. ii.inc 参考范围

用户澄清：
> "关于 ii.inc 体验过它的research 的结果呈现逻辑，不错，是可以参考的。另外，关于它的页面让人觉得的简单干净有设计感，当然这个是参考的一个维度。"

**含义:**
- 参考ii.inc的信息组织方式（标题→徽章→描述→链接）
- 参考其"简单干净有设计感"的感觉
- **不是**照抄其亮色+衬线视觉风格

### 3. 不允许一次性工作原则

用户原话：
> "你不允许做一次性工作。如果某件事将来还会做，就先手动跑 3-10 个样本，批准后固化成技能文件。如果需要自动运行，就设cron。测试标准很简单：如果我为同一件事问你两次，你就失败了。"

**对当前计划的影响:**
- 不应该做一次性的"设计重塑"
- 应该先手动做3-10个呈现样本
- 用户批准后固化成可复用的skill

---

## 当前内容呈现逻辑分析

### app.py 中的渲染流程

```
render_answer_block() @ line 2197
├── Answer Text (markdown)
├── Copy Button
├── render_trust_block() @ line 2122
│   ├── Confidence Level (HIGH/MEDIUM/LOW)
│   ├── Reason
│   └── Source Titles
├── render_research_trace() @ line 2157
│   └── Audit Trail (expandable)
├── Figures (if any)
└── Sources List
```

### ii.inc 呈现模式对比

```
ii.inc Result Card:
├── Title (large, serif)
├── Badge (category indicator)
├── Description (2-3 lines)
└── Links (multiple exit points)

Key patterns:
- 24-56px whitespace between sections
- Hover lift effect
- Opacity-based hierarchy
- Tab navigation for categories
```

### 差距分析

| 维度 | 当前状态 | ii.inc参考 | 差距 |
|------|----------|------------|------|
| 信息层次 | Answer→Trust→Trace→Sources | Title→Badge→Desc→Links | 层次不够清晰 |
| 视觉间距 | 16px uniform | 24-56px graded | 缺乏节奏感 |
| 状态处理 | 部分处理 | 未知 | 需要State Matrix |
| 交互反馈 | 基础 | Hover lift | 可改进 |

---

## 决策记录

### D1: 呈现改进工作模式 — 待决策

**选项A:** 一次性设计重塑
- 写完整PLAN → 实现 → 完成
- ❌ 违反"不允许一次性工作"原则

**选项B:** 技能化流程（推荐）
- 手动做3-10个呈现样本
- 用户批准后固化成 `.claude/skills/render-result-page.md`
- ✅ 符合项目工作原则

### D2: 计划文件处理 — 待决策

**选项A:** 继续完善当前PLAN
- 补充Visual Hierarchy Spec
- 补充State Matrix
- ⚠️ 可能仍是一次性工作

**选项B:** 归档当前PLAN，按skill模式重新开始
- 创建手动样本任务
- 验证后固化
- ✅ 符合项目工作原则

**选项C:** 先手动做样本，验证后再决定
- 低承诺起步
- 根据样本结果决定后续
- ✅ 最低风险

### D3: 内容呈现逻辑定义 — 需要具体化

需要回答：
1. 用户看到答案时，第一眼应该看到什么？
2. 信任信号（confidence/sources）应该在什么位置？
3. 审计轨迹（research trace）是默认展开还是折叠？
4. 不确定性提示（evidence-depth caveat）应该多显眼？

---

## 已存在的相关Skills

| Skill | 用途 | 相关性 |
|-------|------|--------|
| `what-is-page.md` | 生成"what is X"概述页面 | 高 — 定义页面结构 |
| `structured-abstract-extract.md` | 提取结构化摘要 | 中 — 内容处理 |
| `literature-sheet-intake.md` | 批量文献导入 | 低 — 数据导入 |

---

## A方案执行进度

### 已完成

1. **✅ 定义内容呈现规格**
   - 4层信息层次：答案→信任信号→深入路径→边界声明
   - 间距规则：8-12px / 24-32px / 48px
   - 交互模式：折叠/展开、复制、跳转

2. **✅ 创建3个呈现样本**
   - 样本1：What-Is概述页（教育性内容）
   - 样本2：治疗决策支持（临床排名）
   - 样本3：实时查询响应（Ask the Vault）

   **文件位置：** `system/indexes/content-presentation-logic-samples-20260611.md`

### 待批准

3. **⏳ 用户审批**
   - 审核3个样本的呈现逻辑
   - 确认关键决策点
   - 决定是否固化

4. **⏳ 固化成Skill**（批准后）
   - 创建 `.claude/skills/render-result-page.md`
   - 包含呈现规则和决策逻辑

---

## 关键文件位置

| 文件 | 用途 |
|------|------|
| `PLAN-page-rendering-improvements.md` | 当前计划（审查发现需补充） |
| `DESIGN.md` | 445行设计系统规范 |
| `scripts/app.py` | 3515行，17个render函数 |
| `.claude/skills/what-is-page.md` | 已有的页面生成skill |
| `HANDOFF-2026-06-11-PRESENTATION-LAYER.md` | 核心约束恢复文档 |

---

## Resume Instructions

1. 读取本handoff恢复上下文
2. 决定工作模式（技能化 vs 一次性）
3. 如果技能化：
   - 定义内容呈现规格
   - 创建3-10个手动样本
   - 批准后固化成skill
4. 如果继续PLAN：
   - 补充Visual Hierarchy Spec
   - 补充State Matrix
   - 完成Eng/DX审查

---

## 约束备忘（每个session必读）

```
1. 不允许一次性工作。
   如果某件事将来还会做，就先手动跑 3-10 个样本，批准后固化成技能文件。

2. 内容呈现逻辑 > 视觉设计
   特别是在用户使用时。

3. ii.inc是参考之一
   参考其呈现逻辑和简洁感，不照抄视觉风格。

4. 参考文献分类已存在
   综述、产品说明、宣传、监管、论文、内部文档

5. Karpathy LLM Wiki concept
   参考文献按此处理，定期检查差距。
```

---

**Created:** 2026-06-11 20:30
**By:** Claude Code (/autoplan partial completion + context restoration)
**For:** Next session continuation on presentation layer improvements

