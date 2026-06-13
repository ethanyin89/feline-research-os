# Handoff: 呈现层讨论恢复 2026-06-11

**Status:** 核心约束已恢复，计划待重新评估
**Branch:** `idea-chatacademia-research-workbench`
**Date:** 2026-06-11
**Previous Terminal Interrupt:** 讨论上下文丢失后恢复

---

## 恢复的核心约束（之前terminal中断丢失）

### 1. 参考文献分类体系
一直都有这个划分：
- 综述
- 产品说明
- 宣传
- 监管
- 论文
- 内部文档

**这不是新设计，而是已存在的分类系统。**

### 2. Karpathy LLM Wiki Concept
- 参考文献需要按Karpathy LLM Wiki的concept去处理
- 隔一段时间检查与concept的差距
- 这是内容质量的持续评估机制

### 3. 页面呈现风格参考
- ii.inc 是**多个参考风格之一**，不是唯一方向
- 其他可能的参考风格待列举
- 呈现改进是在这个多参考框架下进行

### 4. 不允许一次性工作原则（CRITICAL）
```
如果某件事将来还会做：
1. 先手动跑 3-10 个样本
2. 批准后固化成技能文件 (.claude/skills/*.md)
3. 如果需要自动运行，就设 cron

测试标准：如果我为同一件事问你两次，你就失败了。
```

**这是项目的核心工作原则，不是建议。**

### 5. 接力文档要求
- 因为usage限制，需要做好接力文档
- 否则衔接会出错（如本次terminal中断）
- 每个session结束前必须写handoff

---

## 当前状态

### /autoplan 审查结果
- CEO Review: 0/6维度确认 — 计划太抽象
- Design Review: 0/6维度确认 — 缺少具体specs
- Eng/DX: 被阻塞

### 关键发现
1. 计划混淆了"参考ii.inc呈现逻辑"和"照抄ii.inc视觉风格"
2. 用户澄清：是参考呈现逻辑+简洁感，不是照抄亮色/衬线
3. 但计划仍缺少：
   - 信息层次定义
   - 状态矩阵
   - 结果页面anatomy
   - 具体像素级specs

### 用户新输入的影响
上述5个约束意味着：
1. **呈现改进**可能需要先手动做3-10个样本页面
2. 批准后固化成技能文件（如 `render-result-page.md`）
3. 不是一次性的设计重塑，而是可复用的呈现流程

---

## 待决策

### D1: 呈现改进的工作模式
**选项A:** 一次性设计重塑 — 写PLAN → 实现 → 完成
**选项B:** 按"不允许一次性工作"原则 — 手动3-10样本 → 固化skill → 可重复执行

用户原话暗示选择B。

### D2: 计划文件的处理
**选项A:** 继续完善 `PLAN-page-rendering-improvements.md`
**选项B:** 归档该计划，按skill模式重新开始
**选项C:** 先手动做样本，验证后再决定

### D3: ii.inc之外的其他参考风格
用户提到"提供了几个可能的风格"，但具体是哪些未在当前session恢复。需要用户补充或查找之前的记录。

---

## 已存在的相关Skills

检查 `.claude/skills/` 下是否有呈现相关的skill：
- `what-is-page.md` — 生成"what is X"概述页面
- 其他待确认

---

## 下一步建议

1. **确认工作模式** — 一次性重塑 vs 技能化流程
2. **如果技能化**：
   - 定义"呈现样本"任务的scope
   - 手动做3-10个结果页面样本
   - 用户批准后固化成skill
3. **如果继续PLAN**：
   - 补充Visual Hierarchy Spec
   - 补充State Matrix
   - 但这与"不允许一次性工作"原则可能冲突

---

## 关键文件位置

| 文件 | 用途 |
|------|------|
| `PLAN-page-rendering-improvements.md` | 当前计划（审查发现需补充） |
| `DESIGN.md` | 445行设计系统规范 |
| `scripts/app.py` | 3515行，17个render函数 |
| `.claude/skills/what-is-page.md` | 已有的页面生成skill |
| `HANDOFF-2026-06-06-II-COMMONS-SKILLS.md` | 6月6日II讨论 |

---

## Resume Instructions

1. 读取本handoff恢复上下文
2. 确认用户对D1/D2/D3的决策
3. 如果选择技能化模式：
   - 定义"呈现样本"任务
   - 执行3-10个手动样本
   - 批准后固化
4. 如果继续PLAN模式：
   - 补充缺失specs
   - 完成Eng/DX审查

---

## 约束备忘（每个session必读）

```
不允许一次性工作。
如果某件事将来还会做，就先手动跑 3-10 个样本，批准后固化成技能文件。
如果需要自动运行，就设cron。
测试标准：如果我为同一件事问你两次，你就失败了。
```

---

**Created:** 2026-06-11 19:45
**By:** Claude Code (Terminal Interrupt Recovery + Context Restoration)
