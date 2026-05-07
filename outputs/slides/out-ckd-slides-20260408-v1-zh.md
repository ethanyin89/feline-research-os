---
marp: true
theme: default
paginate: true
title: Feline CKD 内部研究简报
description: Chinese derived deck from Feline Research OS V1
language: zh
source_ids: [src-ckd-001, src-ckd-002, src-ckd-003, src-ckd-004, src-ckd-005, src-ckd-006, src-ckd-007, src-ckd-008, src-ckd-009, src-ckd-010, src-ckd-011, src-ckd-012, src-ckd-013, src-ckd-014, src-ckd-015, src-ckd-016, src-ckd-017, src-ckd-018, src-ckd-019, src-ckd-020, src-ckd-021, src-ckd-022, src-ckd-023, src-ckd-024, src-reg-001, src-reg-002, src-reg-003, src-reg-004, src-reg-005, src-reg-006, src-reg-007, src-reg-008, src-reg-009]
derived_from: outputs/slides/out-ckd-slides-20260408-v1-working-en.md
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
---

# Feline CKD
## 内部研究简报 V1（中文）

Feline Research OS  
2026-04-09

---

# 为什么先做 CKD

- CKD 会强迫四层同时连起来：
  - mechanism
  - model relevance
  - translation
  - regulatory path
- 当前语料已经足够支撑一张可用的内部地图
- 因此，CKD 比更窄的 feline topic 更适合当第一楔子

---

# 当前语料

- 已收录 24 篇 CKD 文献来源
- 已收录 9 篇监管与指导来源
- 24 张 CKD paper card 均已有 round-1 deep extraction coverage
- 机制、模型、终点、转化、监管这几层都已有编译页面
- 现在已经同时存在双语编译资产、英文输出和中文输出

---

# 语言说明

- 这份 deck 是中文派生输出
- 它建立在 `working-en` 幻灯片文件之上
- 它不是双语 deck
- 它不意味着比底层幻灯片来源有更强证据地位

---

# 机制骨架

- 当前最强的疾病骨架：`renal fibrosis / tubulointerstitial fibrosis`
- primary-study 支持把 fibrosis 与以下因素连起来：
  - azotemia
  - hyperphosphatemia
  - anaemia
- 重要桥接变量：
  - proteinuria
  - phosphorus
  - systolic blood pressure

底线判断：

CKD 不应被写成松散的症状集合。  
它是一种进行性的结构性疾病，并且有可测的下游信号。

---

# 当前最关键的机制节点

## 目前最强

- renal fibrosis
- glomerulosclerosis
- 与 progression 相关的变量：
  - proteinuria
  - phosphorus
  - blood pressure

## 下一步机制扩展

- TGF-beta

## 目前还不够强

- 没有直接 CKD 支持的宽泛 cat-species difference 叙事

---

# 模型层

- 当前模型层是真实存在的，但仍然偏薄
- 目前最强的转化基础是：
  - naturally occurring disease
  - observational clinical evidence
  - clinicopathology correlation
- 当前最好的桥梁不是 induced challenge model
- 而是结构性病变与临床变量之间的关系

---

# 第一波终点集合

V1 核心终点短名单：

- creatinine
- USG
- UPCR 或 proteinuria
- systolic blood pressure
- phosphorus
- SDMA

重要背景终点：

- PTH
- anaemia
- potassium
- appetite 或 uraemic clinical signs

---

# 终点逻辑

终点系统应分成三个桶：

1. diagnosis and staging
   - creatinine
   - USG
   - SDMA

2. monitoring and prognosis
   - UPCR 或 proteinuria
   - systolic blood pressure
   - phosphorus

3. pathology-linked context
   - anaemia
   - PTH
   - potassium

这样拆分很重要，因为有些变量临床上容易使用，但另一些变量在机制上更有解释力。

---

# 治疗层

## 当前支持最清楚

- renal diet

## 重要但支持不等强

- phosphate binders
- antihypertensive therapy
- ACE-inhibitor strategies
- long-term subcutaneous fluids

## 内部规则

不要把所有治疗压成一张列表。

每张治疗总结都应携带：

- intended goal
- key endpoints
- evidence strength

---

# 识别与早期发现

- Early detection 最好被理解为持续随访监测
- 它不是单一检测指标就能解决的故事
- 老年猫和高风险猫需要明确的识别逻辑
- 由 owner-observed 提示的：
  - polyuria
  - polydipsia
  已经应该进入地图

---

# CKD 与 Hypertension

- Hypertension 不是边角问题
- 它会和以下因素一起作用：
  - proteinuria
  - target-organ damage
  - progression logic
- 血压监测属于 CKD 核心地图的一部分

内部含义：

任何未来的 CKD 评估框架都应保留独立的 hypertension 小节。

---

# 监管视角

## China

- registration framework
- approval-number execution
- 如有需要，再走 import branch

## FDA

- full approval 与 conditional approval 的分叉
- cats 属于 major species
- conditional approval 必须被论证，不能默认成立

## EMA

- 应尽早测试 limited-market eligibility

## VMD

- 是 route selection 加 dossier logic 的问题

---

# 现在能说什么

## 现在可辩护

- 在当前语料里，CKD 是一个以纤维化为中心的疾病
- 第一波终点短名单已经可用
- 治疗证据不均匀，必须标注层级
- 监管路径是一个分叉问题，不是一句答案

## 现在还不能说

- submission-grade pathway recommendation
- final endpoint ranking
- 完整完成的 experimental-model map
- 很强的 SDMA positioning

---

# 下一步

1. 继续加深 SDMA 相关研究
2. 继续补更强的治疗原始研究
3. 只有在证据包更厚之后，才把监管从 route-level 推到 product-specific
4. 继续在最高价值论文上跑 deep extraction
5. 继续把双语派生限制在编译层和输出层

---

# 工作原则

只要这套系统能把一件事做好，它就已经有价值：

把分散的 CKD 证据压成可追踪、可复用、可继续加深的研究工作层。
