---
id: topic-diabetes-diagnostic-monitoring-workup-bilingual
type: topic
topic: diabetes
species: feline
disease: diabetes mellitus
question_type: recognition
source_ids: [src-diabetes-005, src-diabetes-010, src-diabetes-013, src-diabetes-014, src-diabetes-020, src-diabetes-021, src-diabetes-024, src-reg-012, src-reg-013]
last_compiled_at: 2026-04-28
confidence: low
verification_status: compiled
decision_grade: no
language: bilingual
owner: codex
status: active
---

# 猫糖尿病诊断与监测检查 / Feline Diabetes Diagnostic And Monitoring Workup

## 本页回答的问题 / Question This Page Answers

糖尿病识别、检查、治疗候选性和监测问题应如何路由？

How should diabetes recognition, workup, treatment candidacy, and monitoring questions be routed?

## 核心要点 / Core Takeaway

猫糖尿病检查应结构化为诊断确认加分支门控：默认 2 型样疾病、体况状态、继发性内分泌疾病、胰腺炎/DKA 复杂性、治疗候选性和监测强度。

Feline diabetes workup should be structured as diagnosis confirmation plus branch gating: default type-2-like disease, body-condition state, secondary endocrine disease, pancreatitis/DKA complexity, treatment candidacy, and monitoring intensity.

## 检查层 / Workup Layers

| 层 Layer | 路由到 | 当前角色 | 边界 |
|---|---|---|---|
| 确认糖尿病和基线背景 | src-diabetes-014, src-diabetes-021 | 基本疾病框架和临床背景 | 勿在没有全文或指南支持的情况下推广精确诊断标准 |
| 体况和表现状态 | 肥胖和体况 | 将肥胖历史与当前体重/肌肉状态分开 | 勿将每只糖尿病猫视为当前超重 |
| 继发性内分泌门控 | 内分泌继发性糖尿病 | 保留高生长激素血症/肢端肥大症和其他内分泌原因 | 勿仅从当前编译层提供完整筛查算法 |
| 胰腺炎/DKA 复杂性 | 胰腺炎共病 | 路由双向共病和 DKA 复杂性问题 | 勿声称确定的单向因果关系 |
| 治疗候选性 | 治疗分支图、SGLT2 标签控制 | 分离路线、终点和安全边界 | 勿将口服途径视为自动更安全或更可取 |
| 监测强度 | 终点手册、并发症神经病变 | 保持血糖、缓解、体况、安全和并发症终点分离 | 勿在没有更深证据的情况下推广最终监测计划 |

## 路由表 / Routing Table

| 如果问题关于 | 路由到 | 勿路由到 |
|---|---|---|
| 基本疾病框架 | src-diabetes-014, src-diabetes-021 | 治疗排名 |
| 体况/肥胖 | 肥胖和体况 | 一般生活方式注释 |
| 控制困难/高胰岛素需求 | 内分泌继发性糖尿病 | 默认仅 2 型框架 |
| 胰腺炎/DKA 复杂性 | 胰腺炎共病 | 单向因果声明 |
| SGLT2 候选性 | SGLT2 标签控制 | 路线便利性 |
| 缓解 | 缓解边界 | 单一方案承诺 |
| 神经病变 | 并发症神经病变 | 治疗疗效声明 |

## 护栏 / Guardrail

这是知识库架构页面，不是面向主人的诊断清单、剂量方案或兽医判断的替代品。

This is a vault architecture page, not an owner-facing diagnostic checklist, dosing protocol, or substitute for veterinary judgment.
