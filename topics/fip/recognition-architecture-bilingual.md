---
id: topic-fip-recognition-architecture-bilingual
type: topic
topic: fip
species: feline
disease: FIP
question_type: recognition
source_ids: [src-fip-002, src-fip-003, src-fip-005, src-fip-006, src-fip-008, src-fip-010, src-fip-011, src-fip-012, src-fip-015, src-fip-020, src-fip-022, src-fip-023]
last_compiled_at: 2026-04-27
confidence: low
verification_status: compiled
decision_grade: no
language: bilingual
owner: codex
status: active
---

# 猫传染性腹膜炎 (FIP) 识别架构 / Feline FIP Recognition Architecture

## 本页回答的问题 / Question This Page Answers

在模块漂移为单一测试思维或单一病例形式思维之前，FIP 识别应如何结构化？

How should FIP recognition be structured before the module drifts into one-test thinking or one-case-form thinking?

## 核心立场 / Core Position

FIP 识别应建模为三层：
1. 谁处于风险中 / Who is at risk
2. 什么模式引起怀疑 / What pattern raises suspicion
3. 神经复杂性需要什么额外分支 / What additional branch is needed for neurologic complexity

## 第一层：风险背景 / Layer 1: Risk Context

**包括 Includes:**
- 多猫环境逻辑 / Multi-cat environment logic
- 地方性冠状病毒暴露背景 / Endemic coronavirus exposure
- 年轻年龄信号 / Young-age signal
- 模式化品种或群体结构信号 / Patterned breed/population signal
- 雄性过度代表信号 / Male over-representation
- 转诊/医院流行病学背景 / Referral/hospital epidemiology

**回答 Answers:** 谁应该让你更早担心 / Who should make you worry earlier

**具体解读 Concrete read:**
- 年轻年龄是最强的当前早期风险杠杆
- 品种信号是模式化的，不仅是"纯种猫"
- 性别信号重要，但应保持在年龄和生态下方

## 第二层：怀疑模式 / Layer 2: Suspicion Pattern

**包括 Includes:**
- 临床病理模式识别 / Clinicopathologic pattern recognition
- 渗出性 vs 非渗出性疾病形式怀疑 / Effusive vs non-effusive form
- 分期和形式感知描述 / Staged and form-aware description

**回答 Answers:** 什么星座看起来足够像 FIP 以建立复合支持

**具体解读 Concrete read:**
- 临床病理应领导怀疑模式分支
- 渗出是怀疑模式识别中最干净的早期疾病形式触发器
- 怀疑模式在有界分子强化之前

## 第三层：神经扩展 / Layer 3: Neurologic Extension

**包括 Includes:**
- 神经体征背景 / Neurologic-sign context
- 基于 CSF 的诊断扩展 / CSF-based diagnostic extension
- 与通用检查逻辑分离 / Separation from generic workup

**回答 Answers:** 何时检查必须成为不同分支

**具体解读 Concrete read:**
- 神经体征应在专门支持测试之前触发分支转移
- CSF 支持在分支转移后才有意义
- 神经复杂性不应被压缩为普通怀疑加一个额外测试

## 本架构防止什么 / What This Architecture Prevents

- 防止风险被误认为诊断 / Risk ≠ diagnosis
- 防止临床病理被误认为确定性 / Clinicopathology ≠ certainty
- 防止神经疾病被视为"更严重的普通 FIP" / Neurologic ≠ just severe FIP

## 护栏 / Guardrail

识别架构是一个层级模型，不是一个测试阶梯。年轻+多猫+渗出模式不等于确认诊断。

Recognition architecture is a layered model, not a test ladder. Young + multi-cat + effusive pattern ≠ confirmed diagnosis.
