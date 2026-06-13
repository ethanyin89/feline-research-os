# Handoff: Research OS 差距分析 2026-06-11

**Status:** Context恢复 — 6月6日架构设计未落地
**Branch:** `idea-chatacademia-research-workbench`
**Date:** 2026-06-11
**Reference:**
- `/Users/jiawei/Desktop/raw-2.md` — Research OS理念
- `/Users/jiawei/Downloads/260606-handoff(1).md` — **6月6日完整架构设计**

---

## 重要：Context丢失问题

**6月6日已完成详细的架构设计，但今天的session像第一次阅读一样。**

这说明：
1. Handoff文档没有被正确传递到后续session
2. 6月6日的分析成果没有在代码中落地
3. 今天的"呈现样本"工作是重复劳动

---

## 核心认知升级

### 原来的理解
做一个内容呈现逻辑的改进：信息层次、间距、折叠策略。

### 现在的理解
Feline Research OS 的核心不是"呈现"，而是把研究流程变成可交互的工作台：

```
人提出研究问题 → 系统选择知识源 → 检索证据 → 组织成结构化上下文
→ 交给 LLM 综合 → 输出可复核的研究判断
```

---

## 两个不可接受的问题

### 1. DOI链接必须真实可用

当前测试页面的DOI链接是占位符，点击无效。

**要求：**
- 每个来源卡片必须显示真实的 PMCID / PMID / DOI
- 链接必须可点击跳转到PubMed/PMC/期刊
- 无DOI时明确标注"DOI unavailable"

### 2. 与Research OS的差距

当前样本只是静态呈现，缺少：
- **Query interpretation** — 系统如何理解问题
- **Retrieval scope** — 查了哪些来源，为什么
- **Research value statement** — 每条结果的使用价值
- **Quick take** — 证据归纳成领域地图
- **Next research moves** — 下一步研究分支

---

## II-Commons 参考模式

从截图分析，II-Commons的输出结构：

```
┌─────────────────────────────────────────────────────────────┐
│  RESEARCH AGENT HEADER                                       │
│  ────────────────────────────────────────────────────────── │
│  Here are relevant PubMed articles on [topic].               │
│  I prioritized [criteria] that cover [scope].                │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  EVIDENCE CARD (每篇文献)                                    │
│  ────────────────────────────────────────────────────────── │
│  1. [Title] ⊕                                               │
│                                                             │
│  [One-line research value statement]                        │
│  这篇适合了解X，重点讨论Y，如果你想Z可以从这里开始。            │
│                                                             │
│  · Authors: [authors]                                       │
│  · Journal: [journal name]                                  │
│  · Cite as: PMCID:XXX, PMID:XXX, DOI:10.xxx/xxx ← 可点击     │
│  · Categories: [tags]                                       │
│  · Publish Date: YYYY-MM-DD                                 │
│  · ID: PMCID:XXX                                            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  QUICK TAKE (领域地图)                                       │
│  ────────────────────────────────────────────────────────── │
│  这些文献覆盖的主要群组：                                      │
│  · CSF biomarkers: Aβ42, total tau, phosphorylated tau      │
│  · Blood biomarkers: plasma NfL, blood-based amyloid/tau    │
│  · Imaging-linked biomarkers: ...                           │
│  · Clinical use cases: diagnosis, progression, recruitment  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  NEXT RESEARCH MOVES                                         │
│  ────────────────────────────────────────────────────────── │
│  If you want, I can next do one of these:                   │
│  1. Find only recent studies from 2024–2026                 │
│  2. Find blood-based biomarker studies only                 │
│  3. Find original research only, excluding reviews          │
│  4. Summarize the top 5 biomarkers and what each measures   │
└─────────────────────────────────────────────────────────────┘
```

---

## Research Record 最小结构

每次研究任务应生成可保存的记录：

```yaml
request: 用户原始问题
scope: 检索范围和数据库
sources:
  - id: src-ckd-003
    pmcid: PMC6416642
    pmid: 30911600
    doi: 10.1016/j.dadm.2019.01.008
    title: "ISFM Consensus Guidelines on Feline CKD"
    journal: "J Feline Med Surg"
    year: 2019
    research_value: "最佳作为猫CKD管理框架入口"
    categories: [guideline, consensus]
decision: 为什么选择这些结果
output: 最终输出
next_moves: 下一步建议
handoff: 给下一位agent/人类的交接摘要
```

---

## Source Card 元数据状态（已检查）

### 已有字段 ✅

```yaml
# src-ckd-003.md 示例
links:
  doi: "10.1177/1098612X13495241"
  url: "https://journals.sagepub.com/doi/10.1177/1098612X13495241"
year: 2014
evidence_level: review
```

**结论：** DOI数据已存在于source card中，问题是测试页面用了假占位符而没有引用真实数据。

### 可能缺失的字段

- PMID / PMCID — 需要检查覆盖率
- Journal name — 部分可能缺失
- Authors — 部分可能缺失

---

## 下一步行动

### 立即（本session或下session）

1. **检查现有source card元数据完整性**
   - 哪些字段已有
   - 哪些需要补充（DOI, PMID, PMCID）

2. **设计Research Agent Answer Pattern技能**
   - 不只是呈现逻辑
   - 包含完整的研究输出结构

### 短期

3. **实现Research Record**
   - 每次查询生成可保存的记录
   - 支持检索历史研究

4. **DOI Recovery流程**
   - 已有skill: `.claude/skills/doi-recovery.md`
   - 需要批量补充现有source card的DOI

---

## 文件位置

| 文件 | 用途 |
|------|------|
| `/Users/jiawei/Desktop/raw-2.md` | 完整的Research OS理念文档 |
| `presentation-logic-test-page.html` | 当前测试页面（需升级） |
| `content-presentation-logic-samples-20260611.md` | 当前样本（需升级） |
| `.claude/skills/doi-recovery.md` | DOI补充技能 |

---

## 关键引用

> "你的产品核心不是'做了一个猫研究知识库网页'，而是把一个垂直领域研究流程，压缩成了一个可交互的 Research OS。"

> "它不是直接回答，而是把回答组织成了一个'可继续研究的入口'。"

> "真正有用的是：这一轮先帮我定位材料；下一轮帮我收窄；再下一轮帮我做证据表；再下一轮帮我转成方案；最后帮我转成客户可读稿件。"

> "Feline Research OS 的核心不是'输出答案'，而是'把研究问题推进一步'。"

---

## 约束备忘

```
1. DOI链接必须真实可用 — 占位符不可接受

2. Research Agent Answer Pattern:
   - Query interpretation
   - Retrieval scope
   - Ranked evidence cards (with research value)
   - Quick take (domain map)
   - Next research moves

3. Research Record 是持久化单元
   - 每次任务生成可保存记录
   - 支持未来检索和复用
```

---

**Created:** 2026-06-11 21:45
**By:** Claude Code (认知升级后)
**Triggered by:** 用户反馈 — DOI链接不可用 + Research OS差距

