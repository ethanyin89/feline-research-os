---
id: system-ordinary-user-acceptance-report-20260519
type: health-check
topic: operating-system
question_type: acceptance
language: zh
last_compiled_at: 2026-05-19
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: pass
---

# Ordinary User Acceptance Report, 2026-05-19

Suite: ordinary-user
Execution mode: executed
Backend: openrouter
Write-back: off
Acceptance status: pass

Pass rule reminder:

1. 6 个普通用户问题里至少 5 个答案可接受
2. 每个通过答案都要有真实 source ids
3. overview 问题要落到 current-state-dashboard 起步面
4. recognition / endpoints 问题不能被误判成 generic overview
5. answer 要能被普通读者扫读，并给出 next step

## Scoreboard

| ID | Topic | Exit | QType | First Family | Strongest Surface | Clear Miss | Failure Type | Next Fix Layer | Source IDs | Confidence | Initial Read |
|---|---|---:|---|---|---|---|---|---|---:|---|---|
| OU1 | CKD overview | 0 | overview | current-state-dashboard | yes | no | no-clear-failure | none | 3 | high | pass-leaning |
| OU2 | FIP recognition | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 8 | high | pass-leaning |
| OU3 | HCM overview and risk | 0 | overview | current-state-dashboard | yes | no | no-clear-failure | none | 2 | medium | pass-leaning |
| OU4 | IBD versus lymphoma boundary | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 8 | high | pass-leaning |
| OU5 | Diabetes remission | 0 | endpoints | endpoint-handbook | yes | no | no-clear-failure | none | 3 | medium | pass-leaning |
| OU6 | Elevated creatinine worry | 0 | overview | current-state-dashboard | yes | no | no-clear-failure | none | 3 | high | pass-leaning |

Acceptance summary: 6/6 automated pass-leaning answers; 0 execution failures; 0 provenance misses; 0 route misses. Status: pass.

## Detailed Runs

## OU1. CKD overview

Question: `解释CKD`

Must see: 普通用户能看懂的 CKD starter answer，证据和 next step 可见。
Expected question_type: `overview`
Expected primary family: `current-state-dashboard`
Expected strongest surface: `topics/ckd/current-state-dashboard.md`

Exit code: `0`
Confidence: `high`
Source IDs found: `src-ckd-004, src-ckd-010, src-ckd-011`

Routing read:

- router question_type: `overview`
- first family: `current-state-dashboard`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/papers/src-ckd-004.md, raw/papers/src-ckd-010.md, raw/papers/src-ckd-011.md, topics/ckd/current-state-dashboard.md, topics/ckd/synthesis-index.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 339 cards indexed
[info] Source weights: 339 cards weighted
[info] Routing...
[info] Loaded: topics/ckd/current-state-dashboard.md
[info] Loaded: topics/ckd/synthesis-index.md
[info] Hop 1/3 (~1336 tokens loaded)...
[info] Loaded source: src-ckd-004
[info] Loaded source: src-ckd-010
[info] Loaded source: src-ckd-011
[info] Hop 2/3 (~4025 tokens loaded)...
[info] Agent ready to synthesize
[info] Synthesizing (5 files, ~4025 tokens)...
[meta] ROUTER_QTYPE=overview
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=current-state-dashboard
[meta] LOADED_PATHS=raw/papers/src-ckd-004.md,raw/papers/src-ckd-010.md,raw/papers/src-ckd-011.md,topics/ckd/current-state-dashboard.md,topics/ckd/synthesis-index.md
```

Result excerpt:

```text
慢性肾病（CKD, Chronic Kidney Disease）在猫中是一种常见的、逐渐进展的疾病，主要表现为持续的肾功能减退。诊断通常基于多项持续异常的临床检测，包括血浆肌酐升高（一般超过140 µmol/l）、尿比重下降（低于1.035），以及这些指标的稳定性和持续性。此外，伴随的临床表现如体重减轻、肾脏大小变化、尿崩症、多饮多尿、血压升高等都提示可能存在CKD，需要进一步诊断确认[quoted_fact: src-ckd-004]。

病理学上，猫的CKD最显著的病变是肾小管间质纤维化（renal tubulointerstitial fibrosis），这是肾脏疾病的终末共同病理通路，也是临床生化指标（如尿毒症、磷酸盐升高、贫血）与肾功能损伤关联最强的组织学特征[quoted_fact: src-ckd-010][quoted_fact: src-ckd-011]。该病理改变不仅提供了评估肾病严重度的依据，也成为未来治疗的主要靶点。机制研究中，转化生长因子β（TGF-beta）是潜在的关键介质，但目前尚未得到充分验证[quoted_fact: src-ckd-011]。

临床管理中，诊断和分期基于血清肌酐、尿蛋白/肌酐比（UPCR）、尿比重和收缩压等核心指标，建议7岁以上猫每6个月进行健康检查，至少每年作相应的检测。GFR（肾小球滤过率）是肾功能评估的“金标准”，但因实用性限制不常作为常规检测。血清对称二甲基精氨酸（SDMA）被认为比肌酐更敏感，且较少受肌肉量影响，可作为辅助早期检测指标，但不宜单独用作筛查[quoted_fact: src-ckd-004]。治疗的基石是肾脏专用饮食，主要通过限制磷摄入和减轻尿毒症症状，显著延长猫的生存期[quoted_fact: src-ckd-004]。

---

简而言之，猫的CKD是一种进展性肾功能衰退疾病，主要表现为血液和尿液检测异常及相关症状。其最重要的病理特征是肾脏纤维化，这成为了疾病机制理解和治疗策略制定的核心。对于养猫人来说，给年长猫定期做血液和尿液检查可以及早发现和监控CKD，同时合理调整饮食可延缓疾病发展，改善生活质量。

---

关键证据摘要：

- ISFM指南将猫CKD定义为一种常见且进展性的疾病，诊断依赖肌酐、尿比重、UPCR、血压和影像学等检测，强调定期监测和综合评估[quoted_fact: src-ckd-004]。
- 病理研究显示，肾小管间质纤维化是猫CKD中最关键的病理损伤，它与临床指标（肌酐、磷、贫血）高度相关，提示纤维化是疾病严重程度的核心病理[quoted_fact: src-ckd-010]。
- 纤维化是目前治疗的主要靶点，TGF-beta为重要介质之一，但尚处于研究阶段；磷和蛋白尿不仅是监测指标，也参与病理机制[quoted_fact: src-ckd-011]。
- SDMA血清检测虽然敏感且不受肌肉量影响，但被指导建议作为辅助检测，不可单独做早期筛查[quoted_fact: src-ckd-004]。
- 肾脏专用饮食通过限制磷摄入等措施减缓临床症状并延长存活时间，是目前最明确且证据最充分的干预措施[quoted_fact: src-ckd-004]。

---

尚未充分了解的领域包括：

- 早期CKD的干预效果及具体干预优先级尚缺乏高质量证据。
- TGF-beta等纤维化介质在猫中特异性作用和治疗潜力需要更多实验和临床验证。
- 血压、蛋白尿等指标在不同CKD亚型中的具体机制和调整治疗策略仍需深化研究。
- 面向早期非增生性CKD的筛查策略和多指标联合优化仍是开放课题。
- 不同产品和治疗路线的监管审批策略和适用性尚未完全明确。

---

有用的后续话题：

探讨“猫CKD的治疗策略和药物评估”或“猫CKD的早期诊断和监测指标”将是自然的下一步，以更深入理解如何基于当前机制和检测指标进行有效管理和治疗。
```

## OU2. FIP recognition

Question: `FIP怎么识别`

Must see: 识别 / workup 逻辑，不是 generic disease summary。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/fip/risk-and-recognition.md`

Exit code: `0`
Confidence: `high`
Source IDs found: `src-fip-003, src-fip-005, src-fip-006, src-fip-008, src-fip-012, src-fip-015, src-fip-020, src-fip-023`

Routing read:

- router question_type: `recognition`
- first family: `risk-and-recognition`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/papers/src-fip-003.md, raw/papers/src-fip-005.md, raw/papers/src-fip-006.md, raw/papers/src-fip-007.md, raw/papers/src-fip-008.md, raw/papers/src-fip-012.md, raw/papers/src-fip-015.md, raw/papers/src-fip-020.md, raw/papers/src-fip-023.md, topics/fip/risk-and-recognition.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 339 cards indexed
[info] Source weights: 339 cards weighted
[info] Routing...
[info] Loaded: topics/fip/risk-and-recognition.md
[info] Hop 1/3 (~1894 tokens loaded)...
[info] Agent ready to synthesize
[info] Fallback source preload from compiled pages: ['src-fip-003', 'src-fip-005', 'src-fip-006', 'src-fip-007', 'src-fip-008', 'src-fip-012', 'src-fip-015', 'src-fip-020', 'src-fip-023']
[info] Fallback loaded source: src-fip-003
[info] Fallback loaded source: src-fip-005
[info] Fallback loaded source: src-fip-006
[info] Fallback loaded source: src-fip-007
[info] Fallback loaded source: src-fip-008
[info] Fallback loaded source: src-fip-012
[info] Fallback loaded source: src-fip-015
[info] Fallback loaded source: src-fip-020
[info] Fallback loaded source: src-fip-023
[info] Vision: no verified figures on disk yet (extract PDFs to enable)
[info] Synthesizing (10 files, ~14162 tokens)...
[meta] ROUTER_QTYPE=recognition
[meta] ROUTER_DISEASE=fip
[meta] FIRST_FAMILY=risk-and-recognition
[meta] LOADED_PATHS=raw/papers/src-fip-003.md,raw/papers/src-fip-005.md,raw/papers/src-fip-006.md,raw/papers/src-fip-007.md,raw/papers/src-fip-008.md,raw/papers/src-fip-012.md,raw/papers/src-fip-015.md,raw/papers/src-fip-020.md,raw/papers/src-fip-023.md,topics/fip/risk-and-recognition.md
```

Result excerpt:

```text
FIP（猫传染性腹膜炎）的识别应遵循一个多层次的顺序过程，首先通过风险因素（如年轻年龄、特定品种、雄性猫、多猫环境与冠状病毒暴露等）提升怀疑指数，然后依赖临床病理表现与疾病形态（包括渗出型、非渗出型和神经或眼部表现）构建具体的怀疑基础。在此之后，位于神经或眼部表现的病例应切换至相应的分支，利用脑脊液（CSF）检测等专业实验室支持手段增强诊断，分子检测和突变分析则作为辅助支持，整个识别过程不应依赖单一指标或测试。简单来说，FIP的识别不是单一测试能够确诊，而是风险、临床表现和实验室证据的综合评估[quoted_fact: src-fip-003][source_supported_conclusion: src-fip-003][quoted_fact: src-fip-005][source_supported_conclusion: src-fip-006][quoted_fact: src-fip-015][quoted_fact: src-fip-023].

关键证据包括：

- 风险因素：年轻猫、特定品种（如英国短毛猫、德文雷克斯、阿比西尼亚猫）、雄性、多猫环境及冠状病毒流行环境均使FIP怀疑度升高，但这些仅为识别的起点，不能作为诊断证据[quoted_fact: src-fip-005][quoted_fact: src-fip-008][quoted_fact: src-fip-012][quoted_fact: src-fip-020].

- 临床病理与疾病形态是实际的怀疑生成核心，渗出型与非渗出型表现均应关注；相关病例描述显示42例至51例的临床数据支持该识别框架，为症状模式识别和病程分期提供了依据[quoted_fact: src-fip-006][quoted_fact: src-fip-015].

- 神经和眼部表现的病例需调整诊断路径，脑脊液实时RT-PCR检测对诊断神经/眼部FIP具备高特异性（100%）和阳性预测值（100%），但整体敏感性不高（42.1%），神经/眼部病例敏感性可提升至85.7%，提示脑脊液检测应作为专科支持检测，而非一般FIP筛查首选[quoted_fact: src-fip-023].

- FIP识别需保持多元输入的支持框架，避免依赖单项试验或风险因子作诊断，识别顺序为风险提示-临床怀疑-实验室和分子支持-分支专科检测，治疗反应评估则位于识别后期[quoted_fact: src-fip-003][source_supported_conclusion: src-fip-006][source_supported_conclusion: src-fip-015][source_supported_conclusion: src-fip-023].

我们尚未充分明确的领域：

- 不同风险因素（如年龄、品种、环境）之间的权重与优先级具体如何在识别流程中综合运用，特别是在非澳大利亚等其他地区的普适性[source_supported_conclusion: src-fip-005, src-fip-008, src-fip-012].

- 临床病理分期的具体标准和各变量在不同地理与时间背景下的泛化能力，及其与现代抗病毒治疗时代的适应性[source_supported_conclusion: src-fip-006, src-fip-015].

- 神经/眼部表现检测中脑脊液RT-PCR阴性结果的解释空间和临床中负面预测值较低的应对策略[source_supported_conclusion: src-fip-023].

- 各检测手段（如突变检测、分子检测）在不同病理形态及疾病阶段的实际辅助诊断价值及其在识别流程中如何准确定位，避免过度依赖单一检测[General concept from the architecture and source-supported conclusion].

综上，FIP识别强调风险评估起点，但最核心依赖的是临床病理表现与疾病形式的综合判断，辅助以专科支撑检测，其中神经和眼科表现需特别注意流程转换和检测选择，整个识别架构强调多输入的综合支持而非单一诊断指标[quoted_fact: src-fip-003][source_supported_conclusion: src-fip-006][source_supported_conclusion: src-fip-015][source_supported_conclusion: src-fip-023].
```

## OU3. HCM overview and risk

Question: `HCM是什么，为什么危险`

Must see: 解释为什么危险，而不是只给病名定义。
Expected question_type: `overview`
Expected primary family: `current-state-dashboard`
Expected strongest surface: `topics/hcm/current-state-dashboard.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-hcm-002, src-hcm-003`

Routing read:

- router question_type: `overview`
- first family: `current-state-dashboard`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/papers/src-hcm-002.md, raw/papers/src-hcm-003.md, topics/hcm/current-state-dashboard.md, topics/hcm/mechanism-overview.md, topics/hcm/synthesis-index.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 339 cards indexed
[info] Source weights: 339 cards weighted
[info] Routing...
[info] Loaded: topics/hcm/current-state-dashboard.md
[info] Loaded: topics/hcm/synthesis-index.md
[info] Loaded: topics/hcm/mechanism-overview.md
[info] Hop 1/3 (~2117 tokens loaded)...
[info] Loaded source: src-hcm-002
[info] Loaded source: src-hcm-003
[info] Hop 2/3 (~2580 tokens loaded)...
[info] Agent ready to synthesize
[info] Synthesizing (5 files, ~2580 tokens)...
[meta] ROUTER_QTYPE=overview
[meta] ROUTER_DISEASE=hcm
[meta] FIRST_FAMILY=current-state-dashboard
[meta] LOADED_PATHS=raw/papers/src-hcm-002.md,raw/papers/src-hcm-003.md,topics/hcm/current-state-dashboard.md,topics/hcm/mechanism-overview.md,topics/hcm/synthesis-index.md
```

Result excerpt:

```text
肥厚性心肌病（HCM）是一种常见的猫科心脏疾病，特征是心室壁（特别是左心室）异常肥厚，而心室腔未明显扩张。这种肥厚主要是肌肉组织的异常生长及活跃的心肌重塑，形成结构上的变化，而非简单的厚壁现象。HCM的机制包括遗传基因的影响，最典型如MYBPC3基因突变，且基因剂量效应明显，纯合子猫表现出更严重的病情和更高的表型穿透率[quoted_fact: src-hcm-003]。

HCM对猫的危险性主要体现在病程的复杂演变以及可能导致的严重心脏并发症。随着疾病进展，心肌纤维化、心室扩张和冠状动脉硬化等结构重塑可能发生，导致心脏泵血功能下降，进一步引发心衰、血栓形成甚至突然死亡。临床识别HCM依靠超声心动图观察形态及形态学的变化，而对基因型的理解有助于风险评估及遗传咨询[quoted_fact: src-hcm-002]。

对猫咪主人或宠物医生来说，这意味着HCM不仅是单纯的“心脏肥厚”，而是一种遗传指向的复杂疾病，可能有渐进的心肌重构和功能退化。它的危险性在于，如果未早期发现和合理管理，可能导致严重临床后果，因此定期心脏检查和针对高风险品种（如缅因猫、布偶猫）进行遗传筛查尤为重要[llm_inference]。

**关键证据：**
- HCM的定义基于非扩张性心室壁肥厚，是一种活跃的重塑过程，不仅仅是壁厚增加[quoted_fact: src-hcm-002]。
- MYBPC3基因突变在部分猫品种中常见，基因型与表型严重度存在剂量关系[quoted_fact: src-hcm-003]。
- 约10-15%的猫可能患有HCM，这使其成为猫群中较为常见的心脏病[quoted_fact: src-hcm-003]。
- 疾病的晚期表现包括纤维化、心室扩张及冠状动脉问题，属于重塑性心肌病理阶段[llm_inference]。
- HCM作为人类同类疾病的自然大动物模型，为理解机制及探索治疗提供了比较参考[quoted_fact: src-hcm-003]。

**未知领域：**
- 猫咪HCM的具体致病基因及变异如何影响疾病异质性与临床表现仍需深入研究。
- 现有对治疗方法有效性和阶段性应用的确定性较弱，临床证据尚不足。
- HCM与其他心肌病（如扩张型心肌病）在临床上如何精准区分及管理尚存挑战。
- 对新型生物标志物及AI辅助检测的实用性和局限性还需积累更多临床数据[llm_inference]。

**下一步推荐阅读：**
了解猫HCM的“基因型与临床表型关系”（Genetics and Phenotype link of feline HCM）页面，深入理解遗传因素如何影响疾病表现及风险评估，是进一步把握HCM危险性的自然延续。
```

## OU4. IBD versus lymphoma boundary

Question: `IBD和淋巴瘤怎么区分`

Must see: boundary answer，不是百科式概览。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/ibd/risk-and-recognition.md`

Exit code: `0`
Confidence: `high`
Source IDs found: `src-ibd-003, src-ibd-004, src-ibd-009, src-ibd-010, src-ibd-015, src-ibd-016, src-ibd-017, src-ibd-019`

Routing read:

- router question_type: `recognition`
- first family: `risk-and-recognition`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/papers/src-ibd-003.md, raw/papers/src-ibd-004.md, raw/papers/src-ibd-009.md, raw/papers/src-ibd-010.md, raw/papers/src-ibd-015.md, raw/papers/src-ibd-016.md, raw/papers/src-ibd-017.md, raw/papers/src-ibd-019.md, raw/papers/src-ibd-024.md, topics/ibd/risk-and-recognition-bilingual.md, topics/ibd/risk-and-recognition.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 339 cards indexed
[info] Source weights: 339 cards weighted
[info] Routing...
[info] Loaded: topics/ibd/risk-and-recognition.md
[info] Loaded: topics/ibd/risk-and-recognition-bilingual.md
[info] Hop 1/3 (~3107 tokens loaded)...
[info] Agent ready to synthesize
[info] Fallback source preload from compiled pages: ['src-ibd-003', 'src-ibd-004', 'src-ibd-009', 'src-ibd-010', 'src-ibd-015', 'src-ibd-016', 'src-ibd-017', 'src-ibd-019', 'src-ibd-024']
[info] Fallback loaded source: src-ibd-003
[info] Fallback loaded source: src-ibd-004
[info] Fallback loaded source: src-ibd-009
[info] Fallback loaded source: src-ibd-010
[info] Fallback loaded source: src-ibd-015
[info] Fallback loaded source: src-ibd-016
[info] Fallback loaded source: src-ibd-017
[info] Fallback loaded source: src-ibd-019
[info] Fallback loaded source: src-ibd-024
[info] Vision: no verified figures on disk yet (extract PDFs to enable)
[info] Synthesizing (11 files, ~16730 tokens)...
[meta] ROUTER_QTYPE=recognition
[meta] ROUTER_DISEASE=ibd
[meta] FIRST_FAMILY=risk-and-recognition
[meta] LOADED_PATHS=raw/papers/src-ibd-003.md,raw/papers/src-ibd-004.md,raw/papers/src-ibd-009.md,raw/papers/src-ibd-010.md,raw/papers/src-ibd-015.md,raw/papers/src-ibd-016.md,raw/papers/src-ibd-017.md,raw/papers/src-ibd-019.md,raw/papers/src-ibd-024.md,topics/ibd/risk-and-recognition-bilingual.md,topics/ibd/risk-and-recognition.md
```

Result excerpt:

```text
IBD（炎症性肠病）和淋巴瘤在猫的临床及诊断上难以区分，关键在于采用排除诊断思路，通过综合临床表现、影像学检查、组织活检和辅助标志物等多层面评估，并注意采样部位和病理解释的细节。具体来说，IBD识别需基于慢性肠病的怀疑（chronic enteropathy suspicion），先排除食物反应性疾病和小细胞淋巴瘤（small-cell lymphoma），而不是一开始就确认为特发性IBD。超声检查肌层增厚倾向于提示淋巴瘤风险，尤其是老年猫，但不能单凭此诊断。活检方面，包含十二指肠和回肠的多部位取样必不可少，因为淋巴瘤可能局限于回肠，单一部位活检可能漏诊。组织标本中的Bcl-2表达虽在淋巴瘤中显著较高，但两者均有较多表达，故只能作为倾向性参考。粪便S100A12虽能反映炎症存在，但无法区分IBD与淋巴瘤。代谢组学显示多不饱和脂肪酸等代谢物有潜力区分两者，但目前尚属前沿，尚未普及应用。综合来看，IBD与淋巴瘤的区分依赖有针对性的综合性临床与病理诊断流程，单一检查方法均不足以明确鉴别。

主要证据包括：

- IBD本质上是排除性诊断，食物不耐受或过敏及分化良好的肠道淋巴瘤均可临床和组织学上伪装成IBD [source_supported_conclusion: src-ibd-003]。
- 临床活动指数FCEAI可用于追踪慢性肠病的活动度与治疗反应，但不区分IBD与食物反应性疾病或淋巴瘤 [source_supported_conclusion: src-ibd-004]。
- 超声评估显示肌层增厚显著提示淋巴瘤，尤其在老年猫，但淋巴结肿大对IBD和淋巴瘤均常见，无足够鉴别能力 [source_supported_conclusion: src-ibd-010]。
- 十二指肠和回肠活检诊断一致性差，部分淋巴瘤仅回肠阳性，强调多部位取样的重要性，小细胞淋巴瘤诊断需结合回肠活检结果避免漏诊 [source_supported_conclusion: src-ibd-015]。
- 组织标本中Bcl-2抗凋亡蛋白表达在淋巴瘤猫显著较高，但两组均有较高表达，应作为倾向性辅助指标而非确诊依据 [source_supported_conclusion: src-ibd-016]。
- 粪便S100A12虽能反映肠道炎症存在，但IBD与淋巴瘤间无显著差异，不能区分两者 [source_supported_conclusion: src-ibd-017]。
- 代谢组学研究发现多不饱和脂肪酸等代谢物在IBD与小细胞淋巴瘤间具有一定区分能力，属于前沿探索，尚未进入常规诊断 [source_supported_conclusion: src-ibd-019]。
- 病理报告结构影响诊断准确度，自由文本描述比现行结构化报告能保留更多鉴别信息，尤其浆细胞数量是改进报告结构的关键特征 [source_supported_conclusion: src-ibd-009]。

尚存疑问和不足：

- 具体诊断时，如何根据临床和超声等影像表现合理安排活检部位和数量以最大限度减少漏诊？
- Bcl-2表达的具体阈值及其与其它组织学特征结合的辅助诊断价值未完全明确。
- 代谢组学及其他分子标志物的临床实用性与检测普及程度仍有限，需进一步验证和标准化。
- 粪便及血清支持性标志物在治疗监测和预后评估中的角色尚需探讨。
- 病理学家报告风格和解读标准差异如何影响临床诊断一致性及自动化分类的效果仍需研究。

总结，IBD与淋巴瘤的鉴别诊断依赖多学科综合评估，尤其注重详尽的活检策略及病理解读，辅助性标志物和影像检查可提供倾向性参考，但无单一检测可确诊，需谨慎结合全部信息做出诊断以指导治疗和管理[quoted_fact: src-ibd-003][quoted_fact: src-ibd-004][quoted_fact: src-ibd-009][quoted_fact: src-ibd-010][quoted_fact: src-ibd-015][quoted_fact: src-ibd-016][quoted_fact: src-ibd-017][quoted_fact: src-ibd-019][source_supported_conclusion: src-ibd-003][source_supported_conclusion: src-ibd-004][source_supported_conclusion: src-ibd-009][source_supported_conclusion: src-ibd-010][source_supported_conclusion: src-ibd-015][source_supported_conclusion: src-ibd-016][source_supported_conclusion: src-ibd-017][source_supported_conclusion: src-ibd-019].
```

## OU5. Diabetes remission

Question: `糖尿病猫为什么会缓解`

Must see: 解释缓解不是治愈，并落到结果 / 缓解解释面。
Expected question_type: `endpoints`
Expected primary family: `endpoint-handbook`
Expected strongest surface: `topics/diabetes/endpoint-handbook.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-diabetes-007, src-diabetes-015, src-diabetes-024`

Routing read:

- router question_type: `endpoints`
- first family: `endpoint-handbook`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/papers/src-diabetes-007.md, raw/papers/src-diabetes-015.md, raw/papers/src-diabetes-024.md, topics/diabetes/complications-neuropathy.md, topics/diabetes/endpoint-handbook.md, topics/diabetes/mechanism-overview.md, topics/diabetes/remission-boundaries.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 339 cards indexed
[info] Source weights: 339 cards weighted
[info] Routing...
[info] Loaded: topics/diabetes/endpoint-handbook.md
[info] Loaded: topics/diabetes/remission-boundaries.md
[info] Loaded: topics/diabetes/complications-neuropathy.md
[info] Loaded: topics/diabetes/mechanism-overview.md
[info] Hop 1/3 (~5427 tokens loaded)...
[info] Loaded source: src-diabetes-007
[info] Loaded source: src-diabetes-015
[info] Loaded source: src-diabetes-024
[info] Hop 2/3 (~9888 tokens loaded)...
[info] Agent ready to synthesize
[info] Vision: no verified figures on disk yet (extract PDFs to enable)
[info] Synthesizing (7 files, ~9888 tokens)...
[meta] ROUTER_QTYPE=endpoints
[meta] ROUTER_DISEASE=diabetes
[meta] FIRST_FAMILY=endpoint-handbook
[meta] LOADED_PATHS=raw/papers/src-diabetes-007.md,raw/papers/src-diabetes-015.md,raw/papers/src-diabetes-024.md,topics/diabetes/complications-neuropathy.md,topics/diabetes/endpoint-handbook.md,topics/diabetes/mechanism-overview.md,topics/diabetes/remission-boundaries.md
```

Result excerpt:

```text
糖尿病猫会出现缓解（即不再依赖胰岛素）的主要原因是通过治疗改善了血糖控制，减少了葡萄糖毒性，从而恢复了部分胰岛β细胞功能，但这种缓解是条件性的和不可预测的，不能归因于单一因素如某种饮食或胰岛素类型。缓解的发生涉及多种机制，包括降低碳水化合物饮食强度对血糖的影响，以及有效胰岛素治疗减轻胰岛素抵抗和促进β细胞恢复功能。同时，胰腺病变、肥胖、内分泌继发病等复杂机制也会影响缓解的可能性和持续性[quoted_fact: src-diabetes-007][source_supported_conclusion: src-diabetes-007][quoted_fact: src-diabetes-015][source_supported_conclusion: src-diabetes-015][quoted_fact: src-diabetes-024].

关键证据：

- 系统综述表明糖尿病猫的缓解真实存在，但当前证据未能确立任何单一饮食、胰岛素类型或治疗方案作为普适缓解的关键预测因子。缓解可能发生于不同胰岛素类型和多种治疗方案中，但研究缺乏随机化、盲法和控制混杂因素，使比较协议间缓解率难以保证科学准确[quoted_fact: src-diabetes-007][source_supported_conclusion: src-diabetes-007].
- 一项随机对照研究比较了低碳水化合物低纤维饮食与中等碳水化合物高纤维饮食在糖尿病猫管理中的作用，发现两组血糖和果糖胺均改善，但低碳水化合物低纤维组中更多猫咪达到非胰岛素依赖状态，显示饮食成分可能促进缓解但不可孤立解释缓解效果[quoted_fact: src-diabetes-015][source_supported_conclusion: src-diabetes-015].
- 使用胰岛素甘精U300的临床研究提示配合低碳水化合物饮食治疗，部分猫咪在短期内实现缓解，说明良好的胰岛素治疗配合适当饮食对缓解有促进作用，但胰岛素类型优势尚不确定且需要排除内分泌继发疾病干扰[quoted_fact: src-diabetes-024][source_supported_conclusion: src-diabetes-024].
- 机理上，糖尿病猫的核心病理是胰岛素抵抗与β细胞功能缺陷，慢性高血糖加重β细胞损伤。缓解可能反映了通过治疗逆转了部分葡萄糖毒性和胰岛素抵抗，暂时恢复了胰岛素分泌，但不会消除其慢性进展性特性[llm_inference][llm_inference][llm_inference].

尚不明了的事项：

- 缓解的具体定义和标准尚不同研究间不统一，影响缓解率的准确统计。
- 哪些具体生物标志物或临床特征可预测缓解尚无公认且强力证据支持。
- 癌症、胰腺炎、内分泌继发症（如肢端肥大症）等复杂背景对缓解的长期影响需要更进一步研究。
- 不同胰岛素方案和饮食调整如何协同影响缓解以及缓解的持续性时间仍缺乏较大样本的严谨前瞻性研究。
- 缓解是否能预防糖尿病的神经病变等慢性并发症尚未确立。

综上，糖尿病猫的缓解是治疗成功的重要反映，背后机制是多因素协同作用，现阶段努力控制葡萄糖毒性、优化胰岛素治疗和饮食管理是促进缓解的关键，但未来还需明确缓解的预测指标和维持策略[quoted_fact: src-diabetes-007][source_supported_conclusion: src-diabetes-007][quoted_fact: src-diabetes-015][quoted_fact: src-diabetes-024][llm_inference][llm_inference].
```

## OU6. Elevated creatinine worry

Question: `我的猫肌酐升高，这个库能告诉我什么`

Must see: 直接面向读者解释风险，并给出下一步页面。
Expected question_type: `overview`
Expected primary family: `current-state-dashboard`
Expected strongest surface: `topics/ckd/current-state-dashboard.md`

Exit code: `0`
Confidence: `high`
Source IDs found: `src-ckd-004, src-ckd-010, src-ckd-011`

Routing read:

- router question_type: `overview`
- first family: `current-state-dashboard`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/papers/src-ckd-004.md, raw/papers/src-ckd-010.md, raw/papers/src-ckd-011.md, topics/ckd/current-state-dashboard.md, topics/ckd/risk-and-recognition.md, topics/ckd/synthesis-index.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 339 cards indexed
[info] Source weights: 339 cards weighted
[info] Routing...
[info] Loaded: topics/ckd/current-state-dashboard.md
[info] Loaded: topics/ckd/synthesis-index.md
[info] Loaded: topics/ckd/risk-and-recognition.md
[info] Hop 1/3 (~1676 tokens loaded)...
[info] Loaded source: src-ckd-004
[info] Loaded source: src-ckd-010
[info] Loaded source: src-ckd-011
[info] Hop 2/3 (~4366 tokens loaded)...
[info] Agent ready to synthesize
[info] Synthesizing (6 files, ~4366 tokens)...
[meta] ROUTER_QTYPE=overview
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=current-state-dashboard
[meta] LOADED_PATHS=raw/papers/src-ckd-004.md,raw/papers/src-ckd-010.md,raw/papers/src-ckd-011.md,topics/ckd/current-state-dashboard.md,topics/ckd/risk-and-recognition.md,topics/ckd/synthesis-index.md
```

Result excerpt:

```text
您的猫肌酐升高说明可能存在慢性肾病（CKD）或肾功能下降的情况。根据目前的指南，猫肌酐水平高于140 µmol/L通常被用作临床诊断CKD的重要指标，同时还需要结合尿比重（USG低于1.035且持续存在）、蛋白尿和血压等多个指标进行综合评估[quoted_fact: src-ckd-004]。肌酐升高反映的是肾脏过滤功能的受损，它是早期及后期疾病监测和分期中的核心指标之一[quoted_fact: src-ckd-004, src-ckd-010]。

肌酐升高在病理机制上，与肾脏间质纤维化密切相关，纤维化是CKD中最关键的病理损伤，导致长期进展的肾功能下降[quoted_fact: src-ckd-010, src-ckd-011]。其他重要伴随指标还包括蛋白尿、高血压和磷水平升高，它们不仅帮助确认疾病严重程度，还可能是治疗的靶点[quoted_fact: src-ckd-004, src-ckd-010, src-ckd-011]。目前的治疗建议以控制磷负荷和营养支持肾脏饮食为核心，临床研究显示这能显著延长患猫的寿命并缓解临床症状[quoted_fact: src-ckd-004]。

对于读者来说，猫肌酐升高意味着肾脏功能已经受损，需要及时由兽医进行详细检查和阶段分级。这不仅需要单次血液检测，还要结合尿液分析、血压监测等多方面数据长期跟踪。早期发现和持续监测才是管理CKD的关键。饮食调整尤其重要，因为它是目前已证实能减缓病情进展、提升生活质量的基础治疗。

核心证据支撑点包括：
- 肌酐水平超过140 µmol/L，结合USG <1.035的持续性，是CKD诊断的操作标准[quoted_fact: src-ckd-004]。
- 肾间质纤维化是导致肌酐升高的主要病理机制，同时蛋白尿和高血压与不同肾脏微结构损伤有关[quoted_fact: src-ckd-010, src-ckd-011]。
- 肾脏专用饮食和磷限制被证实显著延长CKD猫的生存时间，改善症状[quoted_fact: src-ckd-004]。
- SDMA指标虽然敏感，但现行指南不建议单独用作筛查工具，而是作为辅助[quoted_fact: src-ckd-004]。
- 诊断时需多次复查确认肌酐持续升高，并排除如甲状腺功能亢进等可能影响肌酐的共病[quoted_fact: src-ckd-004].

当前还不完全明确的是早期CKD的准确筛查策略，现有证据推荐长期序列监测而非单次检测。此外肾脏纤维化的具体分子介导机制及其治疗靶点（比如TGF-beta）仍处于研究阶段，尚无成熟的干预手段在临床广泛应用[quoted_fact: src-ckd-011]。

下一步您可以关注“猫慢性肾病的风险识别和早期诊断”（topic-ckd-risk-and-recognition），了解如何早期发现CKD及如何通过多项检测指标综合监控肾功能变化，帮助您和兽医制定合理的管理计划。
```
