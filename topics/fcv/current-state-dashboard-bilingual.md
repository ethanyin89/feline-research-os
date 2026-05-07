---
id: topic-fcv-current-state-dashboard-bilingual
type: topic
topic: fcv
species: feline
disease: feline calicivirus infection
question_type: state-dashboard
source_ids: [src-fcv-001, src-fcv-002, src-fcv-003, src-fcv-004, src-fcv-005, src-fcv-006, src-fcv-007, src-fcv-008, src-fcv-009, src-fcv-010, src-fcv-011, src-fcv-012, src-fcv-013, src-fcv-014, src-fcv-015, src-fcv-016, src-fcv-017, src-fcv-018, src-fcv-019, src-fcv-020, src-fcv-021, src-fcv-022, src-fcv-023, src-fcv-024]
last_compiled_at: 2026-04-27
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
language: bilingual
owner: codex
status: active
---

# 猫杯状病毒 (FCV) 当前状态仪表盘 / Feline FCV Current State Dashboard

## 模块当前状态 / Current Module State

FCV 已作为 24 篇来源种子语料库进入知识库，且所有 24 篇论文来源卡片现在均为 full/deep-extracted。模块在主题页层面仍处于初始阶段，但来源卡片层已覆盖综述/控制、流行病学/识别、疫苗/免疫、治疗和机制/扩展分支。

FCV has entered the vault as a 24-source seed corpus, and all 24 paper source cards are now full/deep-extracted. The module is still bootstrap-stage at the topic-page layer, but the source-card layer now covers broad review/control, epidemiology/recognition, vaccine/immunity, therapy, and mechanism/extension branches.

## 最强早期分支 / Strongest Early Branches

| 分支 Branch | 当前信号 Current Signal | 主要来源 Lead Sources |
|---|---|---|
| 综述/控制逻辑 Broad review/control | 多个现代和经典综述锚点存在 | src-fcv-001, src-fcv-002, src-fcv-004, src-fcv-007, src-fcv-009, src-fcv-015 |
| 疫苗广度/突破边界 Vaccine breadth/break | 强交叉中和、挑战、细胞免疫、持久性、平台疫苗和疫苗失败边界分支均已有 full source-card depth | src-fcv-003, src-fcv-010, src-fcv-011, src-fcv-012, src-fcv-013, src-fcv-017, src-fcv-022, src-fcv-024 |
| 流行病学/携带者 Epidemiology/carriage | 现场流行病学、区域疫苗适配压力、共病原路由和序列流行病学边界均已可见 | src-fcv-005, src-fcv-006, src-fcv-024 |
| 治疗/抗病毒前沿 Therapy/antiviral | 体外试验发现、干扰素敏感性警示、体内CpG49治疗锚点 | src-fcv-008, src-fcv-014, src-fcv-018 |
| 扩展分支 Extension | 眼部、肠道、受体/趋向性分支可见 | src-fcv-016, src-fcv-020, src-fcv-021, src-fcv-023 |

## 来源家族解读 / Source-Family Read

- 指南和综述来源应控制疾病框架、控制架构和机制压缩
- 原始研究应控制终点所有权、挑战细节、现场识别细节
- 评论/背景材料应保持低权重，不应控制 FCV 层级或治疗语言

Guideline and broad review sources should control disease shell and mechanism compression. Original studies should control endpoint ownership and challenge detail. Commentary/context material should remain low-weight.

## 当前声明适配警告 / Current Claim-Fit Warnings

- 不要将 src-fcv-003、src-fcv-011、src-fcv-017、src-fcv-022 压缩为单一"疫苗成功"桶
- 不要让体外广度、挑战保护、细胞免疫、慢性携带者控制漂移为单一保护声明
- 不要让 src-fcv-019 等背景材料控制疾病架构或治疗语言

Do not flatten vaccine studies into one generic "vaccine success" bucket. Do not let in-vitro breadth, challenge protection, cellular immunity, and carrier control drift into one protection claim.

## 仍然薄弱 / Still Thin

- 所有 24 张 FCV 来源卡片均已 full/deep-extracted
- 机制/识别/终点/翻译/监管主题页面存在，但仍需按完整来源层进一步重编译
- 首批窄域所有者备忘录存在，分支声明已不再依赖 source_checked FCV 卡片
- 除论文级疫苗/控制讨论外，无监管语料库

## 下一步 / Next Moves

1. 按 24/24 deep source-card layer 重编译主要 FCV 主题页
2. 使用当前所有者备忘录保持机制、识别、终点语言稳定
3. 在现场有效性、标签/监管和治疗分支更密集之前，保持治疗和疫苗声明低于最终排名

## 核心表面 / Core Surfaces

- [FCV 来源索引 / source index](../../system/indexes/fcv-source-index.md)
- [FCV 阅读计划 / reading plan](../../system/indexes/fcv-reading-plan-round-1.md)
- [FCV 来源深度图 / source depth map](../../system/indexes/fcv-source-depth-map.md)
