---
id: topic-ckd-model-summary
type: topic
topic: ckd
species: feline
disease: CKD
question_type: model
source_ids: [src-ckd-010, src-ckd-012, src-ckd-022]
last_compiled_at: 2026-04-08
confidence: low
owner: ""
status: active
---

# Feline CKD Model Summary / 猫慢性肾脏病（CKD）模型总结

## Question This Page Answers

目前有哪些模型或类模型证据支持猫慢性肾脏病（CKD）的阐释，以及这些模型实际上能解答什么问题？
What model or model-like evidence currently supports feline CKD interpretation, and what can it actually answer?

## Current Conclusions

### quoted_fact

- 当前种子语料库中包含一项临床病理学相关的初级研究，该研究将肾脏病变与可测量的功能障碍指标联系在一起。
  The current seed corpus contains a pathology-linked primary study that correlates renal lesions with measurable dysfunction markers.
- 当前种子语料库还包含一项对照病例研究，该研究捕获了正式诊断前宠主观察到的猫症状模式。
  The current seed corpus also contains a comparative case-control study that captures owner-observed symptom patterns before formal diagnosis.
- 针对治疗的综述材料主要基于自然发生 CKD 的猫，而不是诱导挑战模型的逻辑。
  Treatment-oriented review material is largely built on cats with naturally occurring CKD rather than challenge-model logic.
- 关于肾脏纤维化的综述材料指出，大多数猫 CKD 的底层病因尚不明确，主要通过病变和介质框架进行讨论。
  Fibrosis review material says most feline CKD has unknown underlying aetiology and is discussed through lesion and mediator framing.
- 实验模型论文 `src-ckd-022` 追踪了 6 只在单侧 90 分钟缺血损伤事件后的猫，长达 6 个月，并发现了持续的功能下降以及慢性结构性肾脏病变。
  The experimental-model paper `src-ckd-022` followed 6 cats for 6 months after a unilateral 90-minute ischemic event and found persistent functional decline plus chronic structural renal lesions.

### source_supported_conclusion

- 当前 V1 版的“模型层”并不是一个强大的诱导模型体系。它主要由以下方面支撑：
  The current V1 “model layer” is not a strong induced-model landscape. It is primarily supported by:
  - 自然发生疾病的观察性证据 (natural-disease observational evidence)
  - 临床病理学相关性证据 (clinicopathology correlation evidence)
- 目前的模型层比以往更强大，因为包含了一个明确的猫实验模型锚点（单侧肾缺血模型），而不仅是观察性逻辑。
  The model layer is now stronger than before because it includes one explicit feline experimental-model anchor, not only observational logic.
- 当前知识库在“证据原型”上的支撑要强于经典的“模型分类”。
  The current vault is stronger on `evidence archetypes` than on classic `model taxonomy`.
- 纤维化综述材料最适合作为病变和介质的分析框架，而非正式的实验模型架构。
  The fibrosis review material is better read as lesion and mediator framing than as formal experimental model architecture.
- 对于猫 CKD 而言，当前最实用的转化桥梁不是实验性挑战模型，而是肾脏结构病变与临床可观察指标之间的关系。
  For feline CKD, the most useful current translational bridge is not an experimental challenge model, but the relationship between structural kidney lesions and clinically observable markers.
- 这意味着 CKD 系统应当明确将当前的模型层标记为“自然疾病/观察性证据主导”。
  This means the CKD system should explicitly label the current model layer as `natural disease / observational evidence dominant`.
- 当前语料库中最合理的模型拆分方式为：
  The most defensible model split in the current corpus is:
  - 自然疾病临床管理证据 (natural-disease clinical management evidence)
  - 观察性识别/风险证据 (observational recognition/risk evidence)
  - 临床病理相关性证据 (clinicopathology correlation evidence)
  - 机制综述框架 (mechanism review framing)
  - 实验性缺血损伤证据 (experimental ischemic injury evidence)

### llm_inference

- 如果项目后续需要更强的临床前模型推导，应启动一个独立的专门工作流，搜索猫 CKD 的干预性、纵向或模型设计相关文献。
  If the project later needs stronger preclinical model reasoning, a dedicated search for feline CKD interventional, longitudinal, or model-design literature should be run as a separate workstream.
- 目前而言，在尝试回答“哪种实验模型最好”之前，模型层应当首先回答“我们实际上在使用哪种证据”。
  For now, the model layer should answer `what kind of evidence are we actually using?` before it tries to answer `which experimental model is best?`
- 下一个模型层的里程碑应当是比对该缺血模型与自然发生疾病的相关性，而不是简单为了数量而收集模型论文。
  The next model-layer milestone should be comparing this ischemia model against spontaneous disease relevance, not simply collecting model papers for volume.

## Evidence Map / 证据图谱

- `src-ckd-010` 提供了病理指标相关性证据 / gives pathology-marker correlation evidence
- `src-ckd-012` 提供了症状识别与病例对照框架 / gives symptom-recognition and case-control framing
- `src-ckd-003` 提供了自然发生疾病的治疗与管理框架 / gives naturally occurring disease treatment-management framing
- `src-ckd-011` 提供了以纤维化为中心的病变/介质框架 / gives fibrosis-centered lesion/mediator framing
- `src-ckd-022` 提供了明确的缺血实验模型锚点 / gives an explicit ischemic experimental-model anchor

## Conflicts / Uncertainty

- 我们现在有了一个实验模型锚点，但尚未形成完善的分类体系。
  We now have one experimental-model anchor, but not a developed taxonomy.
- 当前页面在“实践中存在哪些证据”上强于“正式的模型架构”。
  The current page is stronger on “what evidence exists in practice” than on “formal model architecture.”
- 目前仍不清楚，当前的转化推理中有多少能真正被称为“基于模型”的，有多少其实只是“自然临床证据”。
  It remains unclear how much of the current translational reasoning can be called `model-based` versus simply `natural clinical evidence`.

## Gaps

- 尚未建立专用的自然史页面 (no dedicated natural-history page yet)
- 尚未建立明确的观察性研究索引 (no explicit observational-study index yet)
- 尚未建立干预模型总结 (no intervention-model summary yet)
- 系统层面的词汇中尚未明确区分“模型”与“证据原型” (no explicit distinction yet between `model` and `evidence archetype` in system-wide vocabulary)
- 目前仅锚定了一篇实验模型论文 (only one experimental-model paper is currently anchored)

## Next Sources To Ingest

- 猫 CKD 纵向观察性研究 (feline CKD longitudinal observational studies)
- 任何专门设计为猫 CKD 干预模型的研究 (any study explicitly designed as a feline CKD intervention model)
- 具有更强前瞻性设计的生物标志物验证论文 (biomarker-validation papers with stronger prospective design)

## Current Model Stack

| Evidence / Model Type <br>证据/模型类型 | What It Looks Like In This Vault <br>在本知识库中的呈现形式 | What It Can Answer <br>能回答什么问题 | What It Cannot Yet Answer <br>目前还无法回答什么问题 | Key Source IDs <br>关键文献ID |
|---|---|---|---|---|
| 自然发生疾病的临床管理证据<br>Natural-disease clinical management evidence | 自然发生 CKD 病猫的综述和治疗逻辑<br>reviews and treatment logic from cats with naturally occurring CKD | 临床实践做法、哪些终点在操作上重要、哪些地方的证据强或弱<br>what is done in practice, which endpoints matter operationally, where evidence is stronger or weaker | 正式的临床前模型选择或受控挑战模型的比较<br>formal preclinical model selection or controlled challenge-model comparison | src-ckd-003, src-ckd-004, src-ckd-007 |
| 观察性识别/风险证据<br>Observational recognition / risk evidence | 病例对照和以风险为导向的识别逻辑<br>case-control and risk-oriented recognition logic | 哪些猫被发现较晚、什么症状或风险背景应触发筛查<br>which cats get recognized late, what symptom or risk context should trigger workup | 因果疾病机制的证明或干预效力<br>causal disease-mechanism proof or intervention efficacy | src-ckd-012, src-ckd-005 |
| 临床病理学相关性证据<br>Clinicopathology correlation evidence | 自然发病猫中病变与指标的关联<br>lesion-marker linkage in naturally diseased cats | 结构性病变如何与终点（如磷、蛋白尿、血压、贫血）相关联<br>how structural lesions connect to endpoints such as phosphorus, proteinuria, blood pressure, anaemia | 前瞻性治疗响应建模<br>prospective treatment-response modeling | src-ckd-010 |
| 机制综述框架<br>Mechanism review framing | 以纤维化为中心的介质与病变合成<br>fibrosis-centered mediator and lesion synthesis | 哪些机制解释最合理、哪些介质值得进一步提取分析<br>which mechanistic story is most defensible, which mediators deserve deeper extraction | 针对猫的特异性干预效应大小的直接评估<br>direct cat-specific intervention effect sizes | src-ckd-001, src-ckd-011 |
| 实验性缺血损伤模型<br>Experimental ischemic injury model | 单侧缺血，追踪 6 个月<br>unilateral ischemia followed over 6 months | 单次急性损伤是否会导致持续的功能和结构性肾脏疾病<br>whether a single acute insult can lead to lasting functional and structural renal disease in cats | 广泛的自发性疾病外推或针对产品开发计划的模型选择<br>broad spontaneous-disease generalization or model selection for product programs | src-ckd-022 |

## Feline CKD Model Verification & Construction Insights / 猫CKD模型验证与构建解析

为了让研究人员在阅读本库文献（如 `src-ckd-022`、`src-ckd-050` 等）时能够准确把握模型的构建细节与局限性，特别归纳以下几点指引：

1.  **造模成功判断指标 (Model Success Indicators)**：
    *   **肾小球滤过率 (GFR)**：若文献所建模型在急性期后能稳定表现出 **GFR 显著下降（约 30% 左右）** 且持续数月不恢复，通常表明该模型已成功进入慢性肾功能不全阶段。
    *   **血清肌酐 (Creatinine)**：血清肌酐的持续升高（如 [src-ckd-022](../../raw/papers/src-ckd-022.md) 报道的 **42% 涨幅**）是体内法造模成功的生化核心表征。
2.  **关键病理形态学特征 (Pathological Features)**：
    *   构建体内慢性模型时，最终的病理学终点必须涵盖：**肾小管萎缩 (tubular atrophy)、间质炎症 (interstitial inflammation) 以及间质纤维化 (interstitial fibrosis)**。
    *   观察是否有“**无小管肾小球 (atubular glomeruli)**”的形成，这是判断急性缺血成功转化为慢性硬化病变的关键金标准之一。
3.  **细胞系 vs 活体转化差距 (Cell vs In-Vivo Gap)**：
    *   在读类似 [src-ckd-050](../../topics/ckd/model-map.md) 的原代细胞模型文献时，需清醒认识到：TGF-beta1 虽能在成纤维细胞上顺利诱导出促纤维化表型，但这仅能用于测试**受体靶向结合与分子的直接信号阻断**。体外的药效不可直接等同于活体肾脏复杂的微环境，在方案制定中，它仅可作为临床前漏斗的筛药第一步。

## What This Page Now Says Clearly / 本页已明确说明的内容

1. 当前猫 CKD 模型层主要是证据堆栈问题，而不是一个现成的诱导模型目录。
   The current CKD model layer is mostly an evidence-stack problem, not an induced-model catalog.
2. 自然发生的猫病变是当前知识库的主要基底。
   Naturally occurring feline disease is the main substrate of the current vault.
3. 当前最可用的转化桥梁是临床病理学相关性，而不是挑战模型设计。
   The best translational bridge currently available is clinicopathology correlation, not challenge-model design.
4. 如果未来的项目需要更强的临床前规划，必须将模型专用的文献作为独立轨道进行吸收。
   If a future project requires stronger preclinical planning, model-specific literature must be ingested as a separate track.
5. 本知识库已不再完全缺乏实验模型证据，但目前仍然只有一个明确的锚点。
   The vault is no longer entirely without experimental-model evidence, but it still has only one clear anchor.
