---
id: topic-ckd-endpoint
type: topic
topic: ckd
species: feline
disease: CKD
question_type: endpoint
source_ids: [src-ckd-001, src-ckd-002, src-ckd-003, src-ckd-004, src-ckd-006, src-ckd-007, src-ckd-010, src-ckd-013, src-ckd-015, src-ckd-017, src-ckd-018, src-ckd-020, src-ckd-024]
language: bilingual
last_compiled_at: 2026-06-15
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
language_qa_notes: "Bilingual handbook aligned with translation standard. Terminology verified: creatinine -> 肌酐, proteinuria -> 蛋白尿, USG -> 尿比重."
owner: codex
status: active
---

# 猫 CKD 终点指标手册 / Feline CKD Endpoint Handbook

## Key-Claim Traceability

| ID | 声明 Claim | 证据等级 Level | 来源文献 Source ids | 证据边界 Boundary |
|---|---|---|---|---|
| CE1 | 核心临床 CKD 终点指标是肌酐、尿比重 (USG)、UPCR（尿蛋白肌酐比值）、收缩压和磷；它们连接了诊断、监测和预后评估 | B | src-ckd-004, src-ckd-010 | 属于核心临床指标，并非穷尽的结局指标集 |
| CE2 | 不同的终点指标对应不同的结构病变模式：肾小管间质纤维化关联病变 vs 肾小球-血管损伤关联病变 | B | src-ckd-010 | 属于多维度病理判读，而非简单坍缩为单一维度评分 |
| CE3 | 连续追踪以及从基线开始的肌酐趋势分析是终点指标逻辑的核心，而非可选的随访工作 | B | src-ckd-004 | 属于核心诊断方法，非可选的监测手段 |
| CE4 | SDMA 是辅助性的早期检测工具，而非直接替代诊断核心的独立筛查工具 | B | src-ckd-004, src-ckd-024 | 属于支持性标记物，非替代物 |
| CE5 | 尽管体内存在磷滞留，早期血磷仍可能保持正常；PTH 可作为提示隐匿性矿物质负荷的指标 | B | src-ckd-006, src-ckd-015 | 属于矿物质负荷背景，非单一标记物诊断定论 |
| CE6 | 临床试验结局应至少涵盖划分为 9 个核心主题的 29 个参数；这属于试验设计宽度，而非通用的终点指标临床优先级 | C | src-ckd-013 | 属于临床试验架构，非临床终点指标的推荐优先级排名 |

## Quantified Claim Traceability

| Claim | Source IDs | Boundary |
|---|---|---|
| Inadequately concentrated urine (USG <1.035) supports CKD diagnosis / 尿液浓缩不足（USG < 1.035）可辅助确诊 CKD | src-ckd-004 | ISFM guideline criteria |
| Each one-unit serum phosphorus increase was associated with an 11.8% increased risk of death / 血清磷每升高一个单位，死亡风险增加 11.8% | src-ckd-006 | Retrospective cohort study |

## 证据深度警告 / Evidence-Depth Caveat

**EN**
This page sits on a fully deep-extracted CKD source-card layer (24/24 papers). Key anchors: ISFM guideline (`src-ckd-004`), histomorphometry correlation study (`src-ckd-010`), phosphorus-control review (`src-ckd-006`), CKD-MBD review (`src-ckd-015`), biomarker review (`src-ckd-024`), proteinuric kidney disease study (`src-ckd-017`), and core outcome set paper (`src-ckd-013`). This is now an endpoint handbook rather than a routing page.

**ZH**
本页面基于完全深度提取的猫 CKD 基础文献卡片层（24/24 篇文献）。核心锚点包括：ISFM 指南（`src-ckd-004`）、组织形态学相关性研究（`src-ckd-010`）、控磷综述（`src-ckd-006`）、CKD-MBD 综述（`src-ckd-015`）、生物标记物综述（`src-ckd-024`）、蛋白尿性肾病研究（`src-ckd-017`）以及核心结局指标集文献（`src-ckd-013`）。本页面已改写为终点指标手册，不再是简单的路由导航页。

## 核心要点 / Core Takeaway

**EN**
CKD endpoints should be understood in three layers: (1) core operational endpoints (creatinine, USG, UPCR, SBP, phosphorus), (2) early-detection support markers (SDMA), and (3) context markers (PTH, calcium, FGF23, anaemia, potassium). Different endpoints map to different structural lesion patterns. Serial surveillance is part of endpoint logic. Proteinuria, phosphorus, and blood pressure are cross-layer progression variables, not just monitoring numbers.

**ZH**
猫 CKD 的终点指标应划分为三个层级进行理解：(1) 核心临床终点指标（肌酐、尿比重 USG、UPCR、收缩压、磷），(2) 辅助性早期检测标记物（SDMA），以及 (3) 背景解释与管理指标（PTH、钙、FGF23、贫血指标、钾）。不同的终点指标映射到不同的结构损伤病理模式。连续追踪是终点指标分析的必备组成部分。蛋白尿、磷和血压是跨层级的病程进展变量，而非单纯用来记录的监测数值。

## 终点指标层级 / Endpoint Handbook Hierarchy

### 核心层：临床 CKD 终点指标 / Core Tier: Operational CKD Endpoints

**终点指标 1：肌酐 / Endpoint 1: Creatinine**
- **EN:** Primary use: diagnosis, staging, longitudinal monitoring. In practice, CKD diagnosis uses increased serum creatinine >140 µmol/l with persistence over time. A persistent increase >15% from baseline may indicate reduced renal function.
  - *Key boundary:* Rises relatively late, influenced by muscle mass. Not ideal for earliest detection.
  - *Lead sources:* `src-ckd-002`, `src-ckd-004`, `src-ckd-010`
- **ZH:** 主要用途：诊断、分期、纵向追踪。在临床实践中，猫 CKD 的确诊基于血清肌酐持续升高（>140 µmol/L）。较基线持续升高 >15% 可能提示肾功能已经减退。
  - *关键边界：* 指标上升相对较晚，受肌肉量影响较大。不适合作为极早期筛查指标。
  - *主导文献：* `src-ckd-002`, `src-ckd-004`, `src-ckd-010`

---

**终点指标 2：尿比重 / Endpoint 2: USG (Urine Specific Gravity)**
- **EN:** Primary use: diagnostic confirmation, context for azotemia. Inadequately concentrated urine (USG <1.035) combined with creatinine elevation supports CKD diagnosis.
  - *Key boundary:* Essential but not sufficient by itself for earliest detection.
  - *Lead sources:* `src-ckd-002`, `src-ckd-004`
- **ZH:** 主要用途：辅助确诊、提供氮质血症的背景背景信息。当尿液浓缩不足（USG < 1.035）并伴有肌酐升高时，即可支持 CKD 的诊断。
  - *关键边界：* 必不可少，但单凭此指标不足以完成极早期诊断。
  - *主导文献：* `src-ckd-002`, `src-ckd-004`

---

**终点指标 3：UPCR / 蛋白尿 / Endpoint 3: UPCR / Proteinuria**
- **EN:** Primary use: prognosis, substaging, progression interpretation, treatment targeting. Proteinuria is associated with interstitial fibrosis and glomerular hypertrophy. Major progression-linked factor.
  - *Key boundary:* Interpretation requires compartment awareness (primary glomerular vs broader CKD), blood-pressure context, and non-renal confounder exclusion.
  - *Lead sources:* `src-ckd-001`, `src-ckd-004`, `src-ckd-010`, `src-ckd-017`
- **ZH:** 主要用途：评估预后、亚分期设定、解释病程进展、指导靶向治疗。蛋白尿与间质纤维化和肾小球肥大显著相关，是核心的病程进展关联因素。
  - *关键边界：* 临床解读需要明确病变部位（原发性肾小球病变 vs 广泛的慢性肾小管间质疾病）、结合血压背景，并排除肾脏以外的干扰因素。
  - *主导文献：* `src-ckd-001`, `src-ckd-004`, `src-ckd-010`, `src-ckd-017`

---

**终点指标 4：收缩压 / Endpoint 4: Systolic Blood Pressure**
- **EN:** Primary use: substaging, risk management, target-organ protection, progression context. Higher time-averaged SBP correlates with glomerulosclerosis and hyperplastic arteriolosclerosis. Prevalence of hypertension in CKD cats: 20-65%.
  - *Key boundary:* Under-measured in practice. Should be interpreted as repeated hemodynamic signal, not one-visit snapshot. Target <160 mmHg to minimize TOD risk.
  - *Lead sources:* `src-ckd-004`, `src-ckd-007`, `src-ckd-009`, `src-ckd-010`
- **ZH:** 主要用途：临床亚分期、风险控制、靶器官保护、病程进展解读。较高的时间平均收缩压与肾小球硬化和增生性小动脉硬化呈正相关。高血压在 CKD 猫中的流行率介于 20% 至 65% 之间。
  - *关键边界：* 临床实践中往往缺乏常规测量。应当视其为重复评估的血流动力学信号，而非单次门诊的瞬间读数。目标值应控制在 160 mmHg 以下，以最大程度降低靶器官损伤 (TOD) 风险。
  - *主导文献：* `src-ckd-004`, `src-ckd-007`, `src-ckd-009`, `src-ckd-010`

---

**终点指标 5：磷 / Endpoint 5: Phosphorus**
- **EN:** Primary use: monitoring, prognosis, progression control, treatment targeting. Each one-unit serum phosphorus increase was associated with 11.8% increased risk of death. Interstitial fibrosis is linked to hyperphosphatemia.
  - *Key boundary:* May stay normal early despite phosphate retention (PTH compensation). Should not be read in isolation from PTH context.
  - *Lead sources:* `src-ckd-003`, `src-ckd-004`, `src-ckd-006`, `src-ckd-010`
- **ZH:** 主要用途：临床监测、预后评估、控制进展、确定干预指征。血清磷每增加一个单位，猫的死亡风险即增加 11.8%。间质纤维化与高磷血症存在密切病理联系。
  - *关键边界：* 由于体内 PTH（甲状旁腺激素）的代偿性调节，即使在发生磷潴留的早期，血清磷仍可能维持在正常范围内。切勿脱离 PTH 等背景指标孤立解读。
  - *主导文献：* `src-ckd-003`, `src-ckd-004`, `src-ckd-006`, `src-ckd-010`

---

### 辅助层：辅助性早期检测标记物 / Support Tier: Early-Detection Markers

**终点指标 6：SDMA / Endpoint 6: SDMA**
- **EN:** Primary use: early detection support, adjunct monitoring. Appears more sensitive than creatinine for early CKD detection, less affected by muscle mass.
  - *Key boundary:* Cannot currently be recommended as a single screening test. Useful adjunct, not standalone replacement.
  - *Lead sources:* `src-ckd-002`, `src-ckd-004`, `src-ckd-018`, `src-ckd-024`
- **ZH:** 主要用途：辅助极早期发现、作为监控的辅助指标。在早期发现 CKD 方面，SDMA 似乎比肌酐更为敏感，且其几乎不受猫身体肌肉量的影响。
  - *关键边界：* 目前不推荐将其作为唯一的筛查手段。这是一个有用的辅助指标，绝非独立的诊断替代品。
  - *主导文献：* `src-ckd-002`, `src-ckd-004`, `src-ckd-018`, `src-ckd-024`

---

**终点指标 7：肾小球滤过率 (GFR) / Endpoint 7: GFR**
- **EN:** Primary use: ideal early dysfunction detection reference. Gold standard for renal function assessment.
  - *Key boundary:* Practical limitations prevent routine use. Reference concept rather than routine working endpoint.
  - *Lead sources:* `src-ckd-002`, `src-ckd-004`, `src-ckd-024`
- **ZH:** 主要用途：理想的肾功能减退极早期评估参考指标。被公认为评估肾脏滤过功能的黄金标准。
  - *关键边界：* 复杂的临床操作限制了其作为常规手段的普及。主要作为概念性参考，而非临床一线常规使用的指标。
  - *主导文献：* `src-ckd-002`, `src-ckd-004`, `src-ckd-024`

---

### 背景解释与管理指标层 / Context Tier: Interpretation and Management Markers

**终点指标 8：甲状旁腺激素 (PTH) / Endpoint 8: PTH**
- **EN:** Primary use: secondary hyperparathyroidism context, phosphate-retention interpretation, CKD-MBD framing. Increased PTH despite serum phosphorus remaining in range can indicate early mineral burden.
  - *Key boundary:* Important biologically; better as context than first-wave routine endpoint.
  - *Lead sources:* `src-ckd-006`, `src-ckd-015`
- **ZH:** 主要用途：评估继发性甲状旁腺功能亢进的发生状况、解释隐匿性的磷潴留过程、作为 CKD-MBD 整体图景的参考。当血清磷在正常范围但 PTH 异常升高时，往往提示体内已存在早期的矿物质潴留负荷。
  - *关键边界：* 生物学意义重大，但更适合作为评估背景参考，而非一线的常规监测项目。
  - *主导文献：* `src-ckd-006`, `src-ckd-015`

---

**终点指标 9：钙及 CKD-MBD 标记物 (FGF23) / Endpoint 9: Calcium / CKD-MBD Markers (FGF23)**
- **EN:** Primary use: mineral-management caution, calcification context. Cats with CKD have increased risk of total hypercalcaemia. FGF23 increases before azotaemic CKD.
  - *Key boundary:* Clinically relevant branch, but not yet first-wave routine endpoint.
  - *Lead sources:* `src-ckd-015`
- **ZH:** 主要用途：警示矿物质管理、提示组织异位钙化风险。患有 CKD 的猫总钙浓度升高的风险增加。FGF23 在氮质血症出现前就会升高。
  - *关键边界：* 临床意义显著，但目前仍不作为一线首选的常规必测指标。
  - *主导文献：* `src-ckd-015`

---

**终点指标 10：贫血指标 / Endpoint 10: Anaemia**
- **EN:** Primary use: burden/progression context, treatment context. Interstitial fibrosis correlates with anaemia severity.
  - *Key boundary:* Important but currently context variable, not lead endpoint.
  - *Lead sources:* `src-ckd-003`, `src-ckd-010`
- **ZH:** 主要用途：病程进展及疾病负荷的背景评估、指导治疗（如促红细胞生成素的应用）。肾间质纤维化程度与贫血的严重程度密切相关。
  - *关键边界：* 重要，但目前仅作为辅助评估的背景指标，非主导的临床终点。
  - *主导文献：* `src-ckd-003`, `src-ckd-010`

---

**终点指标 11：影像学评估（肾脏超声）/ Endpoint 11: Imaging (Renal Ultrasonography)**
- **EN:** Primary use: structural workup context, renal differential support. Reference imaging modality for feline kidney.
  - *Key boundary:* Important for structural context; diffuse changes harder to characterize than focal/multifocal disease. Not standalone CKD-defining endpoint.
  - *Lead sources:* `src-ckd-004`, `src-ckd-020`
- **ZH:** 主要用途：评估肾脏结构改变、为肾脏疾病鉴别诊断提供支持。是猫肾脏形态结构学评估的首选影像学方法。
  - *关键边界：* 对确认器官结构性病变不可或缺；然而，弥漫性改变较局灶性/多灶性改变更难定量，不能作为独立判定 CKD 的单一终点。
  - *主导文献：* `src-ckd-004`, `src-ckd-020`

## 文献层概况 / Source-Layer Reality

| 文献 ID | 角色 Role | 状态 Status |
|---|---|---|
| src-ckd-004 | ISFM 指南：诊断标准、临床最小数据库、分期指南、长期追踪 | deep_extracted (深挖提取) |
| src-ckd-010 | 组织形态学研究：病变-标记物关联分析、多维度病理解读 | deep_extracted (深挖提取) |
| src-ckd-006 | 控磷研究：甲状旁腺功能亢进背景、与猫生存率的相关性 | deep_extracted (深挖提取) |
| src-ckd-015 | CKD-MBD 综述：钙磷异常代谢、FGF23 指标、更广的矿物质紊乱框架 | deep_extracted (深挖提取) |
| src-ckd-017 | 蛋白尿性肾病研究：结合具体病理部位的蛋白尿临床解读 | deep_extracted (深挖提取) |
| src-ckd-013 | 核心结局指标集研究：最小试验宽度设计（包含 9 大主题的 29 个参数） | deep_extracted (深挖提取) |
| src-ckd-024 | 生物标记物综述：SDMA 性能、肌酐受限表现、UPC 临床特异性 | deep_extracted (深挖提取) |

## 基于不同应用场景的终点指标矩阵 / Endpoint Matrix by Use Case

| 临床应用场景 Use Case | 优先关注 Prioritize | 备注 Notes |
|---|---|---|
| **诊断与 staging (临床分期)** | 肌酐、尿比重 (USG)、肌酐趋势、UPCR、SDMA（辅助） | 诊断必须要求相关异常在时序上是**持续的** |
| **病程进展与 prognosis (预后评估)** | UPCR、收缩压、磷、肌酐趋势 | 蛋白尿与收缩压应作为跨层级的病程进展指示变量 |
| **评估治疗效果/药效** | 磷、蛋白尿、收缩压、肌酐趋势、相关背景指标 | 优先级完全取决于所使用的干预药物类别 |
| **早期发现** | 连续定期追踪、肌酐变化趋势、尿比重 (USG)、SDMA（辅助）、GFR（作为参考） | 基于年龄段的规律性临床排查是核心 |

## 多维病理结构映射关系 / Multi-Axis Structural Mapping

组织形态学研究（`src-ckd-010`）确立了不同的终点指标承载着完全不同的病理结构意义：

| 终点指标分组 Endpoint Group | 关联的结构性病变 Associated Lesions | 临床意义 Implication |
|---|---|---|
| 肌酐、磷、贫血指标 | 肾小管间质纤维化 | 代表核心纤维化相关的脏器病变负荷 |
| 蛋白尿 (UPCR) | 间质纤维化 + 肾小球肥大 | 指示病程进展的结构性桥梁指标 |
| 收缩压 | 肾小球硬化 + 增生性小动脉硬化 | 肾小球-血管损伤程度的血流动力学信号 |

这一映射支持多维度的指标综合解读，而不是将所有临床指标坍缩为一个所谓的严重程度评分。

## 护栏限制 / Guardrail

**EN**
Do not treat all endpoints as interchangeable. The safe architecture is:
1. **Core operational tier:** creatinine, USG, UPCR, SBP, phosphorus
2. **Support tier:** SDMA (adjunctive, not standalone)
3. **Context tier:** PTH, calcium, FGF23, anaemia, imaging
4. **Multi-axis interpretation:** different markers → different lesion patterns
5. **Serial surveillance:** part of endpoint logic, not optional follow-up

**ZH**
切勿将所有的终点指标混为一谈或进行简单替换。最安全的结构是：
1. **核心临床层：** 肌酐、尿比重 (USG)、UPCR、收缩压、磷。
2. **辅助层：** SDMA（辅助诊断，非独立判定标准）。
3. **背景解释层：** PTH、钙、FGF23、贫血指标、影像。
4. **多维度解读：** 不同的标记物 $\rightarrow$ 映射不同的结构病变模式。
5. **连续追踪：** 属于诊断与管理工作流的核心逻辑，而非可选的随访。

## 模块当前可以安全说的话 / What The Module Can Say Safely

**EN**
- Not all endpoints do the same job; distinguish operational, support, and context tiers
- Serial surveillance and creatinine trend are part of diagnostic methodology
- Proteinuria, phosphorus, and blood pressure are cross-layer progression variables, not just monitoring numbers
- Different endpoints map to different structural lesion patterns (fibrosis-linked vs glomerulo-vascular)
- SDMA is an adjunctive support marker, not a standalone screening replacement
- Phosphorus may stay normal early despite phosphate retention; PTH helps interpret hidden mineral burden
- Trial outcome architecture (29 parameters, 9 themes) is separate from routine endpoint priority

**ZH**
- 不同的终点指标承担不同的临床职责；应明确区分核心层、辅助层和背景解释层。
- 连续定期追踪以及肌酐变化趋势是诊断方法学不可分割的一部分。
- 蛋白尿、磷和血压是跨层级的病程进展指示变量，而不仅仅是记录随访结果的数字。
- 不同的终点指标对应不同的结构病理变化（纤维化相关病变 vs 肾小球-血管损伤病变）。
- SDMA 仅作为一个辅助诊断和监测的指标，并不能直接作为独立的替代筛查工具。
- 在发生磷潴留的早期，血磷可能保持正常；PTH 有助于评估和发现体内的隐匿性矿物质负荷。
- 针对学术临床试验的终点指标完整度架构（9 大主题下 29 个参数）应与日常的临床终点指标优先级明确区分。

## 模块当前尚不能说的话 / What The Module Should Not Say Yet

**EN**
- do not treat all endpoints as interchangeable severity readouts
- do not position SDMA as a universal standalone screening shortcut
- do not ignore PTH context when interpreting phosphorus
- do not confuse imaging workup context with lead efficacy endpoints
- do not collapse trial minimum breadth into universal endpoint ranking

**ZH**
- **切勿**将所有终点指标混淆为相互等效的疾病严重程度读数。
- **切勿**将 SDMA 吹捧为可以完全取代一线的、普适的独立筛查捷径。
- **切勿**在解读血磷指标时，忽略了 PTH 等代偿性背景指标。
- **切勿**将影像学所能提供的结构诊断背景，与药物主要药效评估指标相混淆。
- **切勿**将学术研究中所设计的试验最小宽度（多参数），等同于临床实用的通用指标优先级排序。

## 页面当前定位 / Current Role

**EN**
Use this page as the CKD endpoint handbook. The source-card layer is complete at 24/24 deep-extracted papers. Next gains come from tighter lesion-specific endpoint mapping and clearer trial-vs-routine endpoint distinction in product-specific contexts.

**ZH**
本页面作为猫 CKD 终点指标层的手册库。基础文献卡片层在 24/24 篇深挖提取文献的基础上已全部完成。下一步的工作重心在于针对具体药物产品上下文，提供更紧密的、与具体病损类型相绑定的终点指标映射，以及更清晰的临床试验 vs 临床一线常规终点指标的区分。
