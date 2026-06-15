---
id: topic-ckd-current-state-dashboard
type: topic
topic: ckd
species: feline
disease: CKD
question_type: overview
source_ids: [src-ckd-001, src-ckd-002, src-ckd-003, src-ckd-004, src-ckd-005, src-ckd-006, src-ckd-007, src-ckd-008, src-ckd-009, src-ckd-010, src-ckd-011, src-ckd-012, src-ckd-013, src-ckd-014, src-ckd-015, src-ckd-016, src-ckd-017, src-ckd-018, src-ckd-019, src-ckd-020, src-ckd-021, src-ckd-022, src-ckd-023, src-ckd-024]
language: bilingual
last_compiled_at: 2026-04-11
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: active
---

# Feline CKD Current State Dashboard / 猫慢性肾脏病（CKD）当前状态仪表盘

## Quick Helpers / 快速辅助入口

- if you want to trace a claim back down:
  [verify a claim](../../system/indexes/verify-a-claim.md)
- 如果您想回溯某项论断：
  [验证论断](../../system/indexes/verify-a-claim.md)
- if you want to see real `promote / hold / partial promotion` examples:
  [promotion examples index](../../system/indexes/promotion-examples-index.md)
- 如果您想查看真实的 `晋级 / 搁置 / 部分晋级` 案例：
  [晋级示例索引](../../system/indexes/promotion-examples-index.md)

If you want to enter this vault by question rather than by file tree, start here:
如果您想通过问题而不是文件树进入本知识库，请从这里开始：

- [ask the vault / 询问知识库](../../system/indexes/ask-the-vault.md)

## Top Questions / 高频问题入口

If your real question is one of these, go straight there:
如果您的实际问题是以下之一，请直接前往对应页面：

- `What is the strongest current CKD mechanism reading? / 当前最强的 CKD 机制解读是什么？`
  Open: [mechanism overview / 机制概述](mechanism-overview.md)
- `Which CKD endpoints are operational versus contextual? / 哪些 CKD 终点指标是可操作的，哪些仅具背景参考价值？`
  Open: [endpoint handbook / 终点手册](endpoint-handbook.md)
- `How strong is the current CKD treatment branch? / 当前 CKD 治疗分支的证据有多强？`
  Open: [translation brief / 转化简报](translation-brief.md)
- `How far can the current CKD regulatory reading go? / 当前 CKD 监管解读能走到多远？`
  Open: [regulatory brief / 监管简报](regulatory-brief.md)
- `Which CKD claims should I verify back in the papers? / 哪些 CKD 论断应该回原文核查？`
  Open: [verify a claim / 验证论断](../../system/indexes/verify-a-claim.md)

## If This Page Exposes A Repeated Gap / 如果此页面暴露出重复出现的缺口

Do not treat every question as a write-back candidate.
不要将每个问题都视为回写（write-back）候选对象。

Promote it only if it keeps recurring and clearly improves structure, for example:
只有当它反复出现且能明显改善结构时，才将其晋级，例如：

- a branch boundary is still blurry / 某条分支边界仍然模糊
- a `support` versus `lead` distinction is missing / 缺少 `support` 与 `lead` 级别证据的区分
- a better landing page is needed for the same recurring question / 针对同一反复出现的问题需要一个更好的着陆页

If you want the full operating logic, use:
如果您需要完整的运行逻辑，请使用：

- [query to write-back / 从查询到回写](../../system/indexes/query-to-writeback.md)

Use this page when you want the fastest possible answer to:
当您想最快地获得以下问题的答案时，请使用此页面：

- what already exists / 已经存在什么
- what is solid / 哪些部分是稳固的
- what is still thin / 哪些部分仍然单薄
- what to do next / 下一步该做什么

## Current Status / 当前状态

## Current Status / 当前状态

### Usable Now / 现在可用

**EN**
- CKD topic structure is in place
- CKD source corpus has expanded from 12 to 24 ingested papers
- core mechanism, endpoint, translation, and regulatory pages exist
- deep extraction workflow exists and now covers the full 24-paper CKD seed corpus
- bilingual derived outputs now exist
- first clean Chinese-facing outputs now exist
- health check has been run through round 3
- CKD is now mature enough to serve as the reusable disease-module template for future disease rollout

**ZH**
- CKD 主题结构已经搭建完毕
- CKD 文献语料已从 12 篇扩展到 24 篇已收录论文
- 核心机制、终点指标、转化和监管页面已存在
- 深提炼（deep extraction）工作流已建立，且目前已覆盖全部 24 篇 CKD 种子文献语料
- 双语派生输出已存在
- 首批面向中文用户的清晰输出已存在
- 健康检查已进行到第 3 轮
- CKD 模块目前已足够成熟，可作为未来其他疾病模块推广的复用模板

### Strongest Areas / 最强领域

**EN**
- fibrosis-centered mechanism framing
- pathology-to-endpoint linkage
- endpoint shortlist and tiering
- trial-outcome logic
- first-pass treatment ranking
- recognition logic around older/high-risk cats
- route-level regulatory orientation
- archetype-versus-route comparison logic

**ZH**
- 以纤维化为中心的机制框架搭建
- 病理改变与终点指标的链接
- 终点指标候选名单及分层
- 临床试验结局逻辑
- 第一版治疗手段排序
- 围绕老年猫/高风险猫的识别逻辑
- 路径级别的监管定位
- 治疗原型（archetype）与监管路径（route）对比逻辑

### Still Weak / 仍然薄弱

**EN**
- intervention-by-intervention treatment ranking
- treatment primary-study density
- product-specific regulatory strategy
- final route recommendation beyond the current comparison layer
- Type 2 (controlled intervention) model coverage for drug-efficacy questions

**ZH**
- 针对逐项干预措施的治疗手段排序
- 治疗相关的原始研究密度
- 针对具体产品的监管策略
- 超出当前对比层面的最终路径推荐
- 用于药物疗效评估的 2 型（受控干预型）动物模型覆盖度

## Page Status / 页面状态

| Area / 领域 | Main Page / 主要页面 | State / 状态 | Notes / 备注 |
|---|---|---|---|
| Mechanism / 机制 | [mechanism overview](mechanism-overview.md) | strong (handbook) / 强 (手册级) | 2026-05-06 recompiled to handbook status with Key-Claim Traceability / 2026-05-06 重编译为手册状态，并附带关键论断追溯 |
| Pathology bridge / 病理桥梁 | [pathology correlations](pathology-correlations.md) | strong / 强 | one of the best current bridge pages / 目前最好的桥梁页面之一 |
| Endpoints / 终点指标 | [endpoint handbook](endpoint-handbook.md) | strong (handbook) / 强 (手册级) | 2026-05-06 recompiled to handbook status with Key-Claim Traceability / 2026-05-06 重编译为手册状态，并附带关键论断追溯 |
| SDMA frontier / SDMA 前沿 | [CKD SDMA frontier memo](../../system/indexes/ckd-sdma-frontier-memo.md) | usable and improving / 可用且在完善 | clarifies SDMA support logic versus metabolomic-panel frontier logic / 阐明了 SDMA 支持逻辑与代谢物组检测前沿逻辑的对比 |
| Early detection / 早期检测 | [early detection](early-detection.md) + [frontier branch memo](../../system/indexes/ckd-early-detection-frontier-branch-memo-20260417.md) | two named parallel branches / 两个并行的命名分支 | Branch A: serial surveillance (operational); Branch B: pre-clinical metabolomics/ML frontier (research-stage, distinct question) / 分支 A：连续监测（可操作）；分支 B：临床前代谢组学/机器学习前沿（研究阶段，独立问题） |
| Risk recognition / 风险识别 | [risk and recognition](risk-and-recognition.md) | strong (handbook) / 强 (手册级) | 2026-05-06 recompiled to handbook status with Key-Claim Traceability / 2026-05-06 重编译为手册状态，并附带关键论断追溯 |
| Hypertension / 高血压 | [hypertension and comorbidity](hypertension-and-comorbidity.md) | usable and improving / 可用且在完善 | implementation gap around SBP measurement is now explicit / 围绕收缩压（SBP）测量的执行缺口现已明确 |
| Hypertension-proteinuria junction / 高血压-蛋白尿交叉点 | [CKD hypertension-proteinuria junction memo](../../system/indexes/ckd-hypertension-proteinuria-junction-memo.md) | usable and improving / 可用且在完善 | clarifies where hemodynamic management and proteinuria-oriented management overlap without collapsing into one claim / 澄清了血流动力学管理与以蛋白尿为导向的管理在何处重合，而未混淆为单一论断 |
| Translation / 转化 | [translation brief](translation-brief.md) | usable and improving / 可用且在完善 | trial-outcome logic, implementation-friction layer, and first-pass treatment ranking are now explicit / 临床试验结局逻辑、执行摩擦层和第一版治疗手段排序现已明确 |
| Disease-modification boundary / 疾病修饰边界 | [CKD disease-modification boundary memo](../../system/indexes/ckd-disease-modification-boundary-memo.md) | usable / 可用 | clarifies where management and progression-control language stop and true disease-modification overclaim begins / 澄清了管理与控制进展的表述在何处止步，以及真正的“疾病修饰”过度宣称在何处开始 |
| Proteinuria treatment evidence / 蛋白尿治疗证据 | [CKD proteinuria treatment evidence memo](../../system/indexes/ckd-proteinuria-treatment-evidence-memo.md) | usable and improving / 可用且在完善 | clarifies proteinuria as endpoint, pathology signal, and bounded treatment branch / 明确了蛋白尿作为终点指标、病理信号和受限治疗分支的定位 |
| Phosphorus-control evidence / 控磷证据 | [CKD phosphorus-control evidence memo](../../system/indexes/ckd-phosphorus-control-evidence-memo.md) | usable and improving / 可用且在完善 | separates renal-diet phosphorus logic, adjunct binder logic, and wider CKD-MBD burden logic / 区分了肾脏配方粮控磷逻辑、辅助排磷药逻辑以及更广泛的 CKD-MBD 负担逻辑 |
| Mineral burden / 矿物质负担 | [CKD mineral-burden memo](../../system/indexes/ckd-mineral-burden-memo.md) | usable and improving / 可用且在完善 | lifts the branch above phosphorus alone and organizes PTH, calcium risk, and FGF23 into one CKD-MBD frame / 将该分支提升至仅关注磷之上，并将 PTH、血钙风险和 FGF23 整合进统一的 CKD-MBD 框架中 |
| Supportive care evidence / 支持性护理证据 | [CKD supportive-care evidence memo](../../system/indexes/ckd-supportive-care-evidence-memo.md) | usable and improving / 可用且在完善 | separates potassium, anaemia, appetite-support, and subcutaneous-fluid branches instead of flattening them / 区分了补钾、贫血、食欲支持和皮下输液等分支，而非将其扁平化对待 |
| Outcome architecture / 结局架构 | [CKD outcome architecture memo](../../system/indexes/ckd-outcome-architecture-memo.md) | usable and improving / 可用且在完善 | separates routine operational endpoints from broader treatment-trial outcome architecture / 将常规操作终点与更广泛的治疗试验结局架构区分开 |
| Treatment ranking / 治疗手段排序 | [CKD treatment ranking memo](../../system/indexes/ckd-treatment-ranking-memo.md) | usable / 可用 | formalizes the current intervention hierarchy without overclaiming proof depth / 规范了当前的干预层级，且未过度宣称证据深度 |
| Product archetypes / 产品原型 | [CKD treatment product archetype memo](../../system/indexes/ckd-treatment-product-archetype-memo.md) | usable / 可用 | converts intervention classes into first-pass asset types for later regulatory work / 将干预类别转化为第一版资产类型，以便后续的监管工作 |
| Archetype-versus-route comparison / 原型与监管路径对比 | [CKD archetype-route cleanliness memo](../../system/indexes/ckd-archetype-route-cleanliness-memo.md) | usable / 可用 | shows why the strongest treatment archetype is not automatically the cleanest route archetype / 展示了为什么最强的治疗原型并不自动等同于最清晰的监管路径原型 |
| Product-specific route memo / 特定产品路径备忘录 | [CKD renal diet route memo](../../system/indexes/ckd-renal-diet-route-memo.md) | usable / 可用 | first real jurisdiction-by-jurisdiction route test for one clean archetype / 针对一个清晰原型的首个逐个司法管辖区的实际监管路径测试 |
| Product-specific route memo 2 / 特定产品路径备忘录 2 | [CKD hemodynamic management route memo](../../system/indexes/ckd-hemodynamic-management-route-memo.md) | usable / 可用 | shows where the current official-source pack becomes more useful for drug-like products / 展示了当前的官方资源包在何处对类药产品更具价值 |
| Product-specific route memo 3 / 特定产品路径备忘录 3 | [CKD proteinuria-oriented renoprotective route memo](../../system/indexes/ckd-proteinuria-renoprotective-route-memo.md) | usable / 可用 | shows where route-fit remains usable even as claim-fit becomes more fragile / 展示了即使论断匹配变得更为脆弱，监管路径匹配在何处依然可用 |
| Product-specific route memo 4 / 特定产品路径备忘录 4 | [CKD phosphorus-control adjunct route memo](../../system/indexes/ckd-phosphorus-control-route-memo.md) | usable / 可用 | shows where phosphorus endpoint strength is cleaner than product-category fit / 展示了磷终点指标的强度在何处比产品类别的适配度更清晰 |
| Next route-memo priority / 下一监管路径优先项 | [CKD next route-memo priority memo](../../system/indexes/ckd-next-route-memo-priority-memo.md) | usable / 可用 | shows why proteinuria is the best next borderline route stress test and why phosphorus should pause at route level / 展示了为什么蛋白尿是下一个最好的边界路径压力测试，以及为什么磷在路径层面上应该暂停 |
| Traceability rollout / 追溯性落地 | [sentence-level traceability standard](../../system/indexes/sentence-level-traceability-standard.md) | usable and expanding / 可用且在扩展 | key-claim-level traceability now exists on translation, regulatory, synthesis, and core strategy memos / 关键论断级别的追溯现已在转化、监管、综合和核心策略备忘录中实现 |
| Implementation realism / 执行现实性 | [implementation friction](implementation-friction.md) | usable / 可用 | separates evidence logic from execution friction / 将证据逻辑与执行摩擦分离开 |
| Imaging realism / 影像学现实性 | [imaging context](imaging-context.md) | usable / 可用 | separates structural workup context from endpoint overclaim / 将结构检查背景与终点的过度宣称分离开 |
| Model / 动物模型 | [model map](model-map.md) + [model taxonomy memo](../../system/indexes/ckd-model-taxonomy-memo-20260417.md) | taxonomy explicit / 分类法已明确 | model types now separated by purpose; Type 2 (experimental intervention) remains the main gap / 动物模型类型现按用途分离；2 型（实验性干预）仍是主要缺口 |
| Regulatory / 监管 | [regulatory brief](regulatory-brief.md) | usable / 可用 | route-level, not product-specific / 属于路径级别，而非针对具体产品 |
| Global synthesis / 全局综合 | [synthesis index](synthesis-index.md) | strong / 强 | best compiled overview in one language / 单一语言中最佳的编译概述 |
| Global synthesis bilingual / 双语全局综合 | [synthesis index bilingual](synthesis-index-bilingual.md) | usable / 可用 | good cross-language entry page / 良好的跨语言入口页 |
| Trust audit / 信任审计 | [CKD accuracy and verifiability audit](../../system/indexes/ckd-accuracy-and-verifiability-audit.md) | usable / 可用 | states which layers are auditable, which remain working judgment only / 说明了哪些层级是可审计的，哪些仍仅属于工作评判 |
| Claim protocol / 论断协议 | [claim audit protocol](../../system/indexes/claim-audit-protocol.md) | usable / 可用 | defines what must be traced, downgraded, or blocked before reuse / 定义了在复用前必须追溯、降级或阻断的内容 |
| Language QA / 语言质控 | [language QA protocol](../../system/indexes/language-qa-protocol.md) | usable / 可用 | defines which high-visibility pages need wording and bilingual-alignment checks / 定义了哪些高能见度页面需要进行措辞和双语对齐检查 |
| Language naming / 语言命名 | [language filename alignment standard](../../system/indexes/language-filename-alignment-standard.md) | usable / 可用 | defines how filename, frontmatter, and actual page language must align / 定义了文件名、元数据以及实际页面语言必须如何对齐 |
| Output language matrix / 输出语言矩阵 | [CKD output language matrix](../../system/indexes/ckd-output-language-matrix.md) | usable / 可用 | defines the current working-en, derived-en, zh, and bilingual output layers / 定义了当前工作英文、派生英文、中文和双语输出层 |
| Chinese outputs / 中文输出 | [briefing zh](../../outputs/briefings/out-ckd-briefing-20260408-round1-zh.md) | usable / 可用 | first clean Chinese-facing output layer now exists for briefing, dossier, and slides / 面向中文的简报、卷宗和幻灯片首个清晰输出层已存在 |
| Karpathy gap roadmap / Karpathy 框架缺口路线图 | [Karpathy framework gap roadmap](../../system/indexes/karpathy-framework-gap-roadmap.md) | usable / 可用 | defines the remaining control-layer gaps to stay inside the LLM KB framework / 定义了在 LLM 知识库框架内保持所需解决的控制层缺口 |

## Workflow Status / 工作流状态

### Ingest Workflow / 收录工作流

**EN**
- first-pass ingest: complete for the current 24-source seed corpus
- source-card structure: complete for the current 24-source seed corpus
- verification-status frontmatter is now clean for the CKD paper-card layer: `24/24` cards are marked `deep_extracted`; decision-grade reuse still follows the CKD trust audit and claim protocol
- topic write-back: working

**ZH**
- 初步收录：已完成当前 24 篇文献的种子语料库收录
- 源卡片（source-card）结构：已完成当前 24 篇文献的种子语料库源卡片构建
- 验证状态元数据在 CKD 论文卡片层已清理：`24/24` 张卡片已被标记为 `deep_extracted`；决策级复用仍遵循 CKD 信任审计与论断协议
- 主题回写（topic write-back）：正常运行

### Deep Extraction Workflow / 深提炼工作流

**EN**
- deep extraction: complete for the current 24-source seed corpus
- prompt: [deep extraction prompt v1](../../system/prompts/deep-extraction-prompt-v1.md)
- workflow page: [deep extraction workflow](../../system/indexes/deep-extraction-workflow.md)
- examples:
  - [src-ckd-004](../../system/indexes/src-ckd-004-deep-extraction-round1.md)
  - [src-ckd-010](../../system/indexes/src-ckd-010-deep-extraction-round1.md)
  - [src-ckd-011](../../system/indexes/src-ckd-011-deep-extraction-round1.md)
  - [src-ckd-024](../../system/indexes/src-ckd-024-deep-extraction-round1.md)
  - [src-ckd-013](../../system/indexes/src-ckd-013-deep-extraction-round1.md)
  - [src-ckd-022](../../system/indexes/src-ckd-022-deep-extraction-round1.md)
  - [src-ckd-017](../../system/indexes/src-ckd-017-deep-extraction-round1.md)
  - [src-ckd-016](../../system/indexes/src-ckd-016-deep-extraction-round1.md)
  - [src-ckd-018](../../system/indexes/src-ckd-018-deep-extraction-round1.md)
  - [src-ckd-015](../../system/indexes/src-ckd-015-deep-extraction-round1.md)
  - [src-ckd-019](../../system/indexes/src-ckd-019-deep-extraction-round1.md)
  - [src-ckd-020](../../system/indexes/src-ckd-020-deep-extraction-round1.md)
  - [src-ckd-021](../../system/indexes/src-ckd-021-deep-extraction-round1.md)
  - [src-ckd-023](../../system/indexes/src-ckd-023-deep-extraction-round1.md)
  - [src-ckd-014](../../system/indexes/src-ckd-014-deep-extraction-round1.md)
  - [src-ckd-001](../../system/indexes/src-ckd-001-deep-extraction-round1.md)
  - [src-ckd-002](../../system/indexes/src-ckd-002-deep-extraction-round1.md)
  - [src-ckd-003](../../system/indexes/src-ckd-003-deep-extraction-round1.md)
  - [src-ckd-005](../../system/indexes/src-ckd-005-deep-extraction-round1.md)
  - [src-ckd-006](../../system/indexes/src-ckd-006-deep-extraction-round1.md)
  - [src-ckd-007](../../system/indexes/src-ckd-007-deep-extraction-round1.md)
  - [src-ckd-008](../../system/indexes/src-ckd-008-deep-extraction-round1.md)
  - [src-ckd-009](../../system/indexes/src-ckd-009-deep-extraction-round1.md)
  - [src-ckd-012](../../system/indexes/src-ckd-012-deep-extraction-round1.md)

**ZH**
- 深提炼：已完成当前 24 篇文献种子语料库的提炼
- 提示词： [深提炼提示词 v1](../../system/prompts/deep-extraction-prompt-v1.md)
- 工作流页面： [深提炼工作流](../../system/indexes/deep-extraction-workflow.md)
- 示例：
  - [src-ckd-004](../../system/indexes/src-ckd-004-deep-extraction-round1.md)
  - [src-ckd-010](../../system/indexes/src-ckd-010-deep-extraction-round1.md)
  - [src-ckd-011](../../system/indexes/src-ckd-011-deep-extraction-round1.md)
  - [src-ckd-024](../../system/indexes/src-ckd-024-deep-extraction-round1.md)
  - [src-ckd-013](../../system/indexes/src-ckd-013-deep-extraction-round1.md)
  - [src-ckd-022](../../system/indexes/src-ckd-022-deep-extraction-round1.md)
  - [src-ckd-017](../../system/indexes/src-ckd-017-deep-extraction-round1.md)
  - [src-ckd-016](../../system/indexes/src-ckd-016-deep-extraction-round1.md)
  - [src-ckd-018](../../system/indexes/src-ckd-018-deep-extraction-round1.md)
  - [src-ckd-015](../../system/indexes/src-ckd-015-deep-extraction-round1.md)
  - [src-ckd-019](../../system/indexes/src-ckd-019-deep-extraction-round1.md)
  - [src-ckd-020](../../system/indexes/src-ckd-020-deep-extraction-round1.md)
  - [src-ckd-021](../../system/indexes/src-ckd-021-deep-extraction-round1.md)
  - [src-ckd-023](../../system/indexes/src-ckd-023-deep-extraction-round1.md)
  - [src-ckd-014](../../system/indexes/src-ckd-014-deep-extraction-round1.md)
  - [src-ckd-001](../../system/indexes/src-ckd-001-deep-extraction-round1.md)
  - [src-ckd-002](../../system/indexes/src-ckd-002-deep-extraction-round1.md)
  - [src-ckd-003](../../system/indexes/src-ckd-003-deep-extraction-round1.md)
  - [src-ckd-005](../../system/indexes/src-ckd-005-deep-extraction-round1.md)
  - [src-ckd-006](../../system/indexes/src-ckd-006-deep-extraction-round1.md)
  - [src-ckd-007](../../system/indexes/src-ckd-007-deep-extraction-round1.md)
  - [src-ckd-008](../../system/indexes/src-ckd-008-deep-extraction-round1.md)
  - [src-ckd-009](../../system/indexes/src-ckd-009-deep-extraction-round1.md)
  - [src-ckd-012](../../system/indexes/src-ckd-012-deep-extraction-round1.md)

### Bilingual Workflow / 双语工作流

**EN**
- policy: [bilingual content policy](../../system/prompts/bilingual-content-policy.md)
- rules: [bilingual output rules](../../system/prompts/bilingual-output-rules.md)
- output matrix: [CKD output language matrix](../../system/indexes/ckd-output-language-matrix.md)
- current best examples:
  - [core paper synthesis memo bilingual](../../system/indexes/core-paper-synthesis-memo-ckd-round1-bilingual.md)
  - [synthesis index bilingual](synthesis-index-bilingual.md)
  - [dossier en](../../outputs/dossiers/out-ckd-dossier-20260408-v1-en.md)
  - [dossier zh](../../outputs/dossiers/out-ckd-dossier-20260408-v1-zh.md)

**ZH**
- 政策： [双语内容政策](../../system/prompts/bilingual-content-policy.md)
- 规则： [双语输出规则](../../system/prompts/bilingual-output-rules.md)
- 输出矩阵： [CKD 输出语言矩阵](../../system/indexes/ckd-output-language-matrix.md)
- 当前最佳示例：
  - [核心论文综合备忘录双语版](../../system/indexes/core-paper-synthesis-memo-ckd-round1-bilingual.md)
  - [综合索引双语版](synthesis-index-bilingual.md)
  - [卷宗英文版](../../outputs/dossiers/out-ckd-dossier-20260408-v1-en.md)
  - [卷宗中文版](../../outputs/dossiers/out-ckd-dossier-20260408-v1-zh.md)

## Quality Status / 质量状态

**EN**
- latest quality report: [health check round 3](../../system/health-checks/health-check-report-20260408-round3.md)
- current main bottleneck:
  - uneven evidence density across layers
  - especially treatment primary-study density, model taxonomy, and newer early-detection literature
- control-layer note:
  - verification status and key-claim traceability now exist on the main compiled pages
  - language QA is now a separate required gate for high-visibility pages

**ZH**
- 最新质量报告： [第 3 轮健康检查报告](../../system/health-checks/health-check-report-20260408-round3.md)
- 当前主要瓶颈：
  - 各层证据密度不均衡
  - 尤其是治疗相关的原始研究密度、动物模型分类法以及较新的早期检测文献
- 控制层说明：
  - 验证状态和关键论断追溯目前已存在于主要编译页面中
  - 语言质控（language QA）目前是高能见度页面单独要求的必要门槛

## Recommended Next Moves / 推荐的下一步工作

### Highest Value / 最高价值

**EN**
1. begin the next disease shells, using CKD as the default reusable module for `FIP / IBD / HCM`
2. keep CKD open for incremental source additions rather than waiting for a fictional fully-finished state
3. continue denser CKD write-back under the outcome architecture when new high-value papers arrive
4. use `src-ckd-003` and `src-ckd-014` to sharpen supportive-care and implementation-burden outcomes when CKD densification resumes

**ZH**
1. 开始下一个疾病外壳（disease shell）的构建，使用 CKD 作为 `FIP / IBD / HCM` 的默认可复用模块
2. 保持 CKD 开放以增量添加文献源，而不是等待虚构的“完全完成”状态
3. 当新的高价值论文到来时，继续在结局架构下进行更密集的 CKD 回写（write-back）
4. 在 CKD 证据增密恢复时，使用 `src-ckd-003` and `src-ckd-014` 来提炼支持性护理与执行负担结局

### Round 2 Tier A Cluster: Completed / 第二轮 Tier A 文献簇：已完成

**EN**
- [src-ckd-024 biomarker review](../../raw/papers/src-ckd-024.md)
- [src-ckd-013 core outcome set](../../raw/papers/src-ckd-013.md)
- [src-ckd-022 experimental model](../../raw/papers/src-ckd-022.md)
- [src-ckd-017 proteinuric kidney disease](../../raw/papers/src-ckd-017.md)
- [src-ckd-016 aged-cat morphology and pathogeneses](../../raw/papers/src-ckd-016.md)

See:
请参阅：

- [CKD reading plan round 2](../../system/indexes/ckd-reading-plan-round-2.md)
- [CKD Round 2 Tier A synthesis memo](../../system/indexes/ckd-round-2-tier-a-synthesis-memo.md)
- [CKD Round 2 late-cluster synthesis memo](../../system/indexes/ckd-round-2-late-cluster-synthesis-memo.md)

**ZH**
- [src-ckd-024 生物标志物综述](../../raw/papers/src-ckd-024.md)
- [src-ckd-013 核心结局集](../../raw/papers/src-ckd-013.md)
- [src-ckd-022 实验动物模型](../../raw/papers/src-ckd-022.md)
- [src-ckd-017 蛋白尿性肾病](../../raw/papers/src-ckd-017.md)
- [src-ckd-016 老年猫形态学与发病机制](../../raw/papers/src-ckd-016.md)

### Current Light-Source Cleanup: Completed / 当前轻量文献源清理：已完成

**EN**
- [src-ckd-020 ultrasonography review](../../raw/papers/src-ckd-020.md)
- [src-ckd-014 Portugal practice-pattern study](../../raw/papers/src-ckd-014.md)

**ZH**
- [src-ckd-020 超声检查综述](../../raw/papers/src-ckd-020.md)
- [src-ckd-014 葡萄牙诊疗模式研究](../../raw/papers/src-ckd-014.md)

### Do Not Do Yet / 先不要做

**EN**
- do not translate raw source cards by default
- do not overbuild new structure before adding more source depth
- do not make submission-grade regulatory claims from the current corpus

**ZH**
- 默认情况下不要翻译原始源卡片（source cards）
- 在添加更多文献源深度之前，不要过度构建新结构
- 不要基于当前语料库做出申报级（submission-grade）的监管断言

## One-Sentence State / 一句话状态

**EN**
This CKD vault is now a real working research system with a completed second Tier A densification cluster, a formal first-pass treatment ranking, a first-pass product-archetype layer, four product-specific route memos, and an explicit next-route priority layer, and its next gains will come from carefully chosen evidence additions rather than more framework.

**ZH**
这个 CKD 知识库目前已是一个实际运行的研究系统，完成了解析第二组 Tier A 增密文献簇、正式的第一版治疗手段排序、第一版产品原型层、四份特定产品的监管路径备忘录以及明确的下一路径优先级层，其后续的提升将来自于审慎选择 of 证据增补，而非更多框架的搭建。

## New Densification Note / 新增密说明

- [CKD outcome primary-study densification memo / CKD 结局原始研究增密备忘录](../../system/indexes/ckd-outcome-primary-study-densification-memo.md)
- [CKD completion and multi-disease rollout memo / CKD 完成与多疾病推广备忘录](../../system/indexes/ckd-completion-and-multi-disease-rollout-memo.md)
