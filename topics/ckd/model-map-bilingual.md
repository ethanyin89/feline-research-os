---
id: topic-ckd-model-bilingual
type: topic
topic: ckd
species: feline
disease: CKD
question_type: model
source_ids: [src-ckd-001, src-ckd-003, src-ckd-004, src-ckd-007, src-ckd-009, src-ckd-010, src-ckd-011, src-ckd-012, src-ckd-016, src-ckd-022]
last_compiled_at: 2026-04-27
confidence: medium
verification_status: compiled
language: bilingual
owner: codex
status: active
---

# 猫慢性肾病模型图谱 / Feline CKD Model Map

## 本页回答的问题 / Question This Page Answers

猫 CKD 存在什么模型证据，每种模型能回答什么问题？

What model evidence exists for feline CKD, and what can each model answer?

## 量化声明可追溯性 / Quantified Claim Traceability

| 声明 Claim | 来源 IDs | 边界 Boundary |
|---|---|---|
| 实验模型在单侧 90 分钟缺血事件后随访猫 6 个月，发现持续的功能加病变变化 | src-ckd-022 | 诱导的、单侧的、小型实验模型证据；非自发疾病普遍性 |

## 当前结论 / Current Conclusions

### 引用事实 / Quoted Fact

- 当前种子语料库仍以自然发生的猫 CKD 证据为主，而非诱导疾病模型文献
- 治疗和指南来源围绕临床疾病猫的连续监测、亚分期、蛋白尿、血压、磷控制和支持性管理组织 CKD
- 证据分级综述材料显示，许多常用干预尽管在现实世界使用，但仍然支持薄弱或不均衡
- 临床病理相关证据将结构性肾脏病变与可测量的功能障碍标志物联系起来
- 比较病例对照证据存在于诊断前的识别和症状时机
- 老年猫形态学综述材料现在为自然发生疾病层提供了更强的自然史和发病机制框架
- 实验模型论文显示猫在单侧 90 分钟缺血事件后 6 个月出现持续功能下降和慢性结构性肾脏病变

### 来源支持的结论 / Source-Supported Conclusion

- 当前知识库仍不支持猫 CKD 的经典密集"实验模型菜单"
- 更准确的 V1 图谱仍是从自然疾病管理、识别研究、临床病理相关、综述综合和一个缺血损伤模型构建的"类模型证据图谱"
- 自然发生的临床疾病仍是最强的类模型基底，因为它承载了整个知识库使用的实用诊断、终点和转化逻辑
- 证据分级材料现在加强了自然疾病层不仅因为现实主义有价值，还因为它暴露了常规管理在哪里超越证明的说法
- 血压和蛋白尿共病材料支持将自然疾病内的亚组结构视为重要的证据架构，而非背景噪声
- 纤维化中心机制综合使自然疾病层更可重用，因为它提供了稳定的病变骨架，即使启动原因仍然异质
- 模型图谱现在更强，因为老年猫自然史综述和实验缺血工作可以一起阅读而不将它们压缩为同一证据类型

### LLM 推理 / LLM Inference

- 如果未来工作扩展到药物开发规划，本页应分为自然疾病、纵向观察证据、干预研究和真正的实验模型证据

## 类模型证据矩阵 / Model-Like Evidence Matrix

| 模型/证据原型 | 知识库中当前存在 | 最佳用途 | 主要弱点 |
|---|---|---|---|
| 自然发生临床疾病 | 强 | 现实世界管理逻辑、终点选择、转化谨慎、亚组框架 | 因果隔离和正式模型设计较弱 |
| 老年猫自然史/形态学综述 | 中等且上升 | 组织病变身份、老年框架、自发疾病中的启动对进展逻辑 | 综述级别，部分假设引导 |
| 病例对照识别证据 | 中等 | 早期识别框架、症状时机、风险背景怀疑 | 机制和治疗疗效有限 |
| 临床病理相关 | 强且独特 | 机制-终点桥梁、标志物的结构解释 | 非前瞻性干预模型 |
| 机制综述综合 | 中等 | 纤维化中心病变和介质框架 | 综述级别，部分外推超出猫 |
| 实验缺血模型 | 现在存在但薄弱 | 病变进展、离散损伤后的功能-结构联系、机制锚定 | 单侧且诱导，因此与自发 CKD 的转化相关性仍有界 |

## 本页清楚表述的内容 / What This Page Says Clearly

1. 当前模型层是真实的，但仍不是密集的经典实验模型层
2. 当知识库同时使用自然发生疾病加临床病理相关时最强
3. 证据分级和共病来源使自然疾病层比简单的"临床背景"桶更有结构
4. 知识库现在有一个真正的实验模型锚点加更好的老年猫自然史框架，但用户仍应小心不要过度陈述模型强度
5. **模型类型≠任何目的的证据充分性**。不同的研究问题需要不同的模型类型

## 模型分类法（目的导向）/ Model Taxonomy (Purpose-Oriented)

关于按不同研究目的（机制、终点验证、药物疗效、监管转化）组织的模型类型完整分类法，见：

- [CKD 模型分类法备忘录 / CKD model taxonomy memo](../../system/indexes/ckd-model-taxonomy-memo-20260417.md)

该备忘录的关键见解：知识库的差距不是一般的"模型证据不足"——而是专门针对药物疗效问题的**类型 2（对照干预）覆盖**。自然疾病、临床病理相关和老年猫形态学对其能服务的目的相当强。

## 护栏 / Guardrail

模型类型不等于证据充分性。知识库对自然疾病和临床病理相关强，但对对照干预研究弱。不要将自然疾病强度误读为实验模型强度。

Model type does not equal evidence sufficiency. The vault is strong on natural disease and clinicopathology correlation but weak on controlled intervention studies. Do not misread natural-disease strength as experimental-model strength.
