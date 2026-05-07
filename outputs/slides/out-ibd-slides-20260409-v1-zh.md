---
marp: true
theme: default
paginate: true
title: 猫 IBD 内部研究简报
description: Feline Research OS V1 的中文派生 slide deck
language: zh
source_ids: [src-ibd-001, src-ibd-002, src-ibd-003, src-ibd-004, src-ibd-005, src-ibd-006, src-ibd-007, src-ibd-008, src-ibd-009, src-ibd-010, src-ibd-011, src-ibd-012, src-ibd-013, src-ibd-014, src-ibd-015, src-ibd-016, src-ibd-017, src-ibd-018, src-ibd-019, src-ibd-020, src-ibd-021, src-ibd-022, src-ibd-023, src-ibd-024]
generated_at: 2026-04-09
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
---

# 猫 IBD
## 内部研究简报 V1（中文）

Feline Research OS  
2026-04-09

---

# 为什么 IBD 值得单列

- IBD 不是一个简单的 inflammation 主题
- 它要求系统同时处理：
  - 排除式诊断流程
  - lymphoma 边界
  - marker hierarchy
  - 早期治疗逻辑
- 这让它成为很强的可复用 disease-module pattern

---

# 当前 corpus

- 24 篇 IBD 相关文献已 ingest
- 24 张 IBD paper card 均已有 round-1 deep extraction coverage
- compiled topic pages 已覆盖：
  - mechanism
  - endpoints
  - recognition
  - translation
  - synthesis
- entity layer 与英文输出层已经存在

---

# 语言说明

- 这是中文派生 slide 文件
- 它不是 bilingual deck
- 它建立在英文 working / derived 输出层之上
- 它不代表比底层 slide source 更强的证据

---

# 核心疾病框架

- 猫 IBD 当前应放在 `chronic enteropathy` 内理解
- 当前最强的顶层架构是：
  - diagnosis of exclusion
  - IBD versus small-cell lymphoma boundary
  - activity versus identity separation

Bottom line:

不要把猫 IBD 建模成 one-test 或 one-marker disease。

---

# 什么主导诊断流程

- `FCEAI` 用于活动度与反应追踪
- `FCEAI` 不是 disease-class discriminator
- `Biopsy site choice` 很关键：
  - duodenum
  - ileum
- `Muscularis thickening` 是偏 lymphoma 的影像信号

内部含义：

诊断流程架构比任何单一 marker 都更重要。

---

# Boundary 逻辑

- 最重要的邻近边界疾病是：
  - small-cell alimentary lymphoma
- 当前边界压力来自：
  - imaging
  - biopsy-site strategy
  - tissue-marker studies
  - microbiota studies
  - metabolomic frontier work

这是一个 multimodal 问题，不是 one-test 问题。

---

# Marker hierarchy

## Support markers

- vitamin D
- fecal S100A12

## Frontier marker

- metabolomics

## Rule

不要把 support markers 和 frontier markers 压成一个 biomarker tier。

---

# Pathology 与 chronicity

- Idiopathic IBD 现在已经有自己的 immunopathology depth branch
- Fibrosis 现在已经有自己的 structural chronicity branch
- Fibrosis 不应再被当成 background histology

内部含义：

模块现在已经能分开：
- activity
- pathology depth
- structural chronicity

---

# 早期治疗锚点

## 当前最清楚的 direct anchor

- hydrolysed diet response

## 它意味着什么

- diet-first management 是当前最稳的 practical treatment frame

## 它不意味着什么

- 不是 idiopathic-IBD-specific proof
- 不是 final treatment hierarchy

---

# 我们现在能说什么

## 现在可以稳定说的

- IBD 应被放在 chronic enteropathy 内建模
- exclusion-first workup 是正确骨架
- lymphoma boundary 是核心问题
- marker hierarchy 已经存在
- fibrosis 是 structural chronicity branch
- diet-first logic 是最清楚的早期实践锚点

## 现在还不能稳定说的

- one-marker diagnosis
- 最终 treatment ranking
- routine-ready metabolomic deployment
- regulatory path recommendation
