# Handoff: 内容呈现逻辑样本 2026-06-11

**Status:** 样本已创建，待用户审批
**Branch:** `idea-chatacademia-research-workbench`
**Date:** 2026-06-11

---

## 本次Session完成的工作

### 1. 恢复上下文
- 从terminal中断恢复了5个核心约束
- 完成了/autoplan的CEO和Design审查（均为0/6确认，计划需补充specs）
- 用户确认选择A方案：技能化流程

### 2. A方案执行
按照"不允许一次性工作"原则，创建了3个手动样本：

| 样本 | 类型 | 文件 |
|------|------|------|
| 样本1 | What-Is概述页 | 教育性内容，普通用户 |
| 样本2 | 治疗决策支持 | 临床排名，专业用户 |
| 样本3 | 查询响应 | Ask the Vault实时回答 |

### 3. 测试页面
创建了可视化测试页面，展示3个样本的实际效果。

---

## 关键文件位置

| 文件 | 用途 |
|------|------|
| `system/indexes/presentation-logic-test-page.html` | **测试页面** — 浏览器打开查看效果 |
| `system/indexes/content-presentation-logic-samples-20260611.md` | 样本规格文档 |
| `HANDOFF-2026-06-11-AUTOPLAN-PRESENTATION-LAYER.md` | 完整/autoplan状态 |
| `HANDOFF-2026-06-11-PRESENTATION-LAYER.md` | 核心约束备忘 |
| `PLAN-page-rendering-improvements.md` | 原始计划（已标记blocked） |

---

## 如何查看测试页面

```bash
# 方法1: 直接打开
open /Users/jiawei/Desktop/insclaude/feline-research-os/system/indexes/presentation-logic-test-page.html

# 方法2: 本地服务器（如果需要）
cd /Users/jiawei/Desktop/insclaude/feline-research-os/system/indexes
python -m http.server 8080
# 然后访问 http://localhost:8080/presentation-logic-test-page.html
```

---

## 内容呈现逻辑核心规则

### 信息层次

| 层次 | 内容 | 默认状态 |
|------|------|----------|
| 第一层 | 核心答案/关键事实 | 完全展开 |
| 第二层 | 信任信号/来源 | 部分折叠 |
| 第三层 | 深入路径/相关问题 | 可选展示 |
| 第四层 | 边界声明/免责 | 简洁固定 |

### 间距规则

| 层级间隔 | 像素 |
|----------|------|
| 同层内元素 | 8-12px |
| 层级切换 | 24-32px |
| 主要分区 | 48px |

### 关键设计决策

1. **双语处理** — 默认单语+可展开（而非并列）
2. **置信度位置** — 答案前置顶部
3. **evidence_depth显示** — 来源卡片显示full_text/abstract标签
4. **折叠策略** — Tier 2+内容默认折叠
5. **✅ 引用格式（已确认）** — 用文献标题+DOI链接，不用内部ID
   - 旧格式：`[引用: src-ckd-003]`
   - 新格式：`ISFM CKD Guidelines (2019) ↗` (可点击跳转DOI)

---

## 下一步

### 如果用户批准样本

1. 固化成 `.claude/skills/render-result-page.md`
2. 包含呈现规则、决策逻辑、HTML/CSS模板
3. 后续呈现改进直接调用该skill

### 如果需要调整

1. 根据反馈修改测试页面
2. 迭代样本规格
3. 重新提交审批

---

## 约束备忘

```
1. 不允许一次性工作
   如果某件事将来还会做，就先手动跑 3-10 个样本，批准后固化成技能文件。

2. 内容呈现逻辑 > 视觉设计
   特别是在用户使用时。

3. ii.inc是参考之一
   参考其呈现逻辑和简洁感，不照抄视觉风格。
```

---

## Resume Instructions

1. 用户查看测试页面 `presentation-logic-test-page.html`
2. 收集反馈：
   - 信息层次是否合理？
   - 间距节奏感如何？
   - 哪些决策需要调整？
3. 根据反馈决定：
   - 批准 → 固化成skill
   - 调整 → 修改样本后重新提交

---

**Created:** 2026-06-11 21:15
**By:** Claude Code (A方案执行)

