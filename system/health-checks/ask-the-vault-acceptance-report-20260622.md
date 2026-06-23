---
id: system-ask-the-vault-acceptance-report-20260622
type: health-check
topic: operating-system
question_type: acceptance
language: zh
last_compiled_at: 2026-06-22
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: pass
---

# Ask The Vault Acceptance Report, 2026-06-22

Suite: research
Execution mode: executed
Backend: openrouter
Write-back: off
Acceptance status: pass

Pass rule reminder:

1. 8 个核心问题里至少 6 个答案可接受
2. 0 个答案出现伪造 source id
3. 0 个答案把明显推断伪装成 `quoted_fact`
4. 至少 4 个答案能把用户直接带到最短答案面
5. `--write-back` 产物 frontmatter 完整且文件名稳定
6. 至少 1 个 cross-disease 问题被明确降级处理，而不是乱猜

## Scoreboard

| ID | Topic | Exit | QType | First Family | Strongest Surface | Clear Miss | Failure Type | Next Fix Layer | Source IDs | Confidence | Initial Read |
|---|---|---:|---|---|---|---|---|---|---:|---|---|
| Q1 | CKD mechanism spine | 0 | mechanism | mechanism-overview | yes | no | answer-compression-miss | answer-compression | 6 | low | pass-leaning |
| Q2 | CKD endpoint selection | 0 | endpoints | endpoint-handbook | yes | no | no-clear-failure | none | 6 | medium | pass-leaning |
| Q3 | CKD claim verification | 0 | claim_verification | verify-a-claim | yes | no | no-clear-failure | none | 3 | medium | pass-leaning |
| Q4 | FIP diagnostic workup | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 9 | medium | pass-leaning |
| Q5 | HCM recognition versus endpoint | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 7 | medium | pass-leaning |
| Q6 | IBD versus lymphoma boundary | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 9 | high | pass-leaning |
| Q7 | Cross-disease question | 0 | synthesis | disease-module-maturity-ladder | yes | no | answer-compression-miss | answer-compression | 2 | low | pass-leaning |
| Q8 | Regulatory question | 0 | regulatory | regulatory-brief | yes | no | no-clear-failure | none | 9 | medium | pass-leaning |

Acceptance summary: 6/8 automated pass-leaning answers; 0 execution failures; 0 provenance misses; 0 route misses. Status: pass.

## Detailed Runs

## Q1. CKD mechanism spine

Question: `CKD 的核心机制主线是什么？`

Must see: 至少落到 CKD mechanism 强答案面，且至少 2 个真实 source ids。
Expected question_type: `mechanism`
Expected primary family: `mechanism-overview`
Expected strongest surface: `topics/ckd/mechanism-overview.md`

Exit code: `0`
Confidence: `low`
Source IDs found: `src-ckd-001, src-ckd-010, src-ckd-011, src-ckd-015, src-ckd-016, src-ckd-021`

Routing read:

- router question_type: `mechanism`
- first family: `mechanism-overview`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `answer-compression-miss`
- next fix layer: `answer-compression`
- loaded paths: `raw/papers/src-ckd-001.md, raw/papers/src-ckd-002.md, raw/papers/src-ckd-004.md, raw/papers/src-ckd-006.md, raw/papers/src-ckd-009.md, raw/papers/src-ckd-010.md, raw/papers/src-ckd-011.md, raw/papers/src-ckd-015.md, raw/papers/src-ckd-016.md, raw/papers/src-ckd-021.md, topics/ckd/mechanism-overview.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 系统解析猫慢性肾脏病（CKD）的核心发病机制及其主要病理过程。
[info] Loaded: topics/ckd/mechanism-overview.md
[info] Hop 1/3 (~7528 tokens loaded)...
[info] Agent ready to synthesize
[info] Fallback source preload from compiled pages: ['src-ckd-001', 'src-ckd-002', 'src-ckd-004', 'src-ckd-006', 'src-ckd-009', 'src-ckd-010', 'src-ckd-011', 'src-ckd-015', 'src-ckd-016', 'src-ckd-021']
[info] Fallback loaded source: src-ckd-001
[info] Fallback loaded source: src-ckd-002
[info] Fallback loaded source: src-ckd-004
[info] Fallback loaded source: src-ckd-006
[info] Fallback loaded source: src-ckd-009
[info] Fallback loaded source: src-ckd-010
[info] Fallback loaded source: src-ckd-011
[info] Fallback loaded source: src-ckd-015
[info] Fallback loaded source: src-ckd-016
[info] Fallback loaded source: src-ckd-021
[info] Vision: 2 verified figure(s) available from ['src-ckd-001']
[info] Synthesizing (11 files, ~27398 tokens)...
[meta] ROUTER_QTYPE=mechanism
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=mechanism-overview
[meta] LOADED_PATHS=raw/papers/src-ckd-001.md,raw/papers/src-ckd-002.md,raw/papers/src-ckd-004.md,raw/papers/src-ckd-006.md,raw/papers/src-ckd-009.md,raw/papers/src-ckd-010.md,raw/papers/src-ckd-011.md,raw/papers/src-ckd-015.md,raw/papers/src-ckd-016.md,raw/papers/src-ckd-021.md,topics/ckd/mechanism-overview.md
```

Result excerpt:

```text
猫慢性肾病（CKD）的核心机制主线是肾小管间质纤维化，这一病理改变是猫CKD中最常报告且与肾功能关联度最高的病变，代表肾脏疾病的共同最终通路（final common pathway）。该纤维化主干作为病理结构上的核心锚点，贯穿老年猫特异性的慢性肾脏退行性病程，同时维系机制与临床指标如肌酐、蛋白尿、血磷和血压之间的桥梁。猫CKD病程多发生于12岁以上的老年猫，原发肾小球病极为罕见，因而以特发性、纤维化为中心的小管间质损伤为主要病理特征。蛋白尿、血磷及收缩压不仅是临床分期指标，更反映了不同的肾脏微结构损伤模式，支持CKD机制的多轴解读。此外，矿物质代谢紊乱（CKD-MBD）形成独立的分支，涉及钙失调、甲状旁腺素及FGF-23的动态调控，其中FGF-23的升高早于血磷异常，提示其为更早期的生物标记物。纤维化介质层面，转化生长因子β（TGF-beta）被确认是促纤维化的重要驱动因子，虽主要基于体外原代成纤维细胞研究，尚缺乏临床验证。老年猫的细胞衰老和端粒缩短被视为机制补充分支，可能参与疾病进展。新兴上游机制还包括肠道－肾脏轴中尿毒症毒素（如硫酸吲哚酚、硫酸对甲酚、TMAO）蓄积，以及猫副粘病毒（FeMV）感染导致的肾小管上皮细胞凋亡。遗传性疾病中，波斯猫常见的常染色体显性多囊肾病（ADPKD）由PKD1基因c.10063C>A突变引发，代表明确的病因学分支[quoted_fact: src-ckd-001][quoted_fact: src-ckd-011][quoted_fact: src-ckd-016][quoted_fact: src-ckd-010][quoted_fact: src-ckd-015][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference].

核心证据要点包括：

- 肾小管间质纤维化是与肌酐升高、贫血、高磷血症等功能指标相关度最高的组织学病变（80只猫队列尸检研究）[quoted_fact: src-ckd-010]。
- 蛋白尿与肾小管间质纤维化及肾小球肥大相关，收缩压与肾小球硬化和小动脉硬化相关，显示多指标对应不同微结构损伤模式[quoted_fact: src-ckd-010]。
- 以衰老为背景，老年猫中早期即有肾小管间质纤维化和炎症，原发肾小球病极罕见，老年衰老、缺血、低氧被视为促成因子但未获充分因果证据[quoted_fact: src-ckd-016][llm_inference][llm_inference]。
- FGF-23在各CKD阶段升高且早于高磷血症，有潜力作为早期诊断的生物标记物，且血清磷水平不完全反映早期磷潴留[llm_inference][quoted_fact: src-ckd-015]。
- TGF-beta是纤维化促成的核心介质，原代猫肾皮质成纤维细胞对其驱动有明确响应，但缺乏体内临床验证[llm_inference][quoted_fact: src-ckd-011]。
- 肠道源性尿毒症毒素的蓄积揭示肠道微生物与肾脏功能减退的联系，尚处于探索阶段[llm_inference]。
- FeMV感染与淋巴浆细胞性肾小管间质性炎症及caspase-3依赖的肾小管细胞凋亡密切相关，病毒载量与凋亡指标高度相关，提示病毒感染为CKD的一种可能病因[llm_inference][llm_inference]。
- 波斯猫ADPKD的遗传机制已明确为PKD1基因杂合突变，表现为肾囊肿形成，是遗传性CKD的一个明确分支[llm_inference][llm_inference]。

尚未解决的空白包括：

- 初始诱发因素（衰老、缺血、低氧、病毒感染与遗传）相对纤维化机制的主导地位尚未明确，缺乏充分体内因果证明。
- TGF-beta及其他介质通路虽体外证据明确，但其在猫自然CKD中的具体作用及治疗靶点价值待临床验证。
- FGF-23作为早期生物标记物的临床应用界限与诊断阈值尚未确立。
- 肠道微生物－肾脏轴的具体机制及调控手段仍处于早期探索阶段，缺乏实证干预数据。
- FeMV感染的普遍性及其在不同猫群CKD中的贡献度尚无定论，不能简单视为所有CKD的主因。
- ADPKD遗传变异谱尚未完全清晰，针对非典型突变的诊断与预后评估需要深入研究。

---

## 研究者视角

猫CKD最好被理解为一种以肾小管间质纤维化为核心，衰老为背景的复杂慢性疾病，其机制层级从明确的纤维化病变向多条介质通路扩展，包括转化生长因子β调控的促纤维化基因程序、矿物质代谢失衡、及RAAS系统中醛固酮/盐皮质激素受体（MR）的参与。临床上，蛋白尿、血磷和血压作为结构损伤桥梁变量，映射不同的病理轴，避免了单一严重度评分的不足。CKD-MBD分支凸显了FGF-23和PTH的复杂调节作用，提示矿物质代谢紊乱远超单纯磷代谢异常。衰老及肾缺血低氧作为上游促成因素为机制提供自然病史基础，其与体外TGF-beta介导的促纤维化机制、肠道尿毒素蓄积、FeMV病毒感染及遗传性PKD1突变协同构成了当前多元化的研究和临床视角。尽管存在不确定性，纤维化这一最终病理收敛为猫CKD机制研究提供了核心稳定点和潜在靶点框架[quoted_fact: src-ckd-001][quoted_fact: src-ckd-011][quoted_fact: src-ckd-016][llm_inference][quoted_fact: src-ckd-015][quoted_fact: src-ckd-021][llm_inference][llm_inference][llm_inference]。

## 不能说过头的地方

现有证据尚不足以确立任何单一的起始病因作为猫CKD的主导因素。转录介质如TGF-beta的体外证据不应直接外推为临床治疗靶点。血磷指标不应被简单视作矿物质代谢异常的全部表现，FGF-23尽管升高早期显著，也未被完全验证为独立诊断阈值。肠道尿毒症毒素虽然累积明确，但临床治疗路径尚未明朗。FeMV感染作为一种病因分支不应用于所有CKD猫的诊断筛查或治疗决策。遗传性PKD1突变筛查应限制于高风险品种如波斯猫。以上结论均不构成专业兽医诊断或治疗建议，临床实践需结合具体病历和专业判断[quoted_fact: src-ckd-011][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference]。

## 下一步

未来研究应聚焦于明确早期促纤维化信号的体内作用，开展基于TGF-beta及醛固酮/MR通路的临床试验验证其治疗潜力；纵向队列研究应评估FGF-23与其他矿物质代谢指标在CKD进展中的预后价值及诊断阈值；肠道微生物－肾脏轴相关代谢组学研究需向益生菌、益生元等非药物管理策略转化验证；病毒学研究应进一步界定FeMV感染对肾脏结构与功能的确切贡献度；遗传学领域需扩展PKD1变异谱鉴定，完善临床遗传诊断及预后模型。整体而言，整合老年猫自然病史模型与多维病理机制网络，将为猫CKD的早期识别、分型和个体化管理提供坚实理论基础[llm_inference]。
```

## Q2. CKD endpoint selection

Question: `What endpoints are most usable for feline CKD efficacy evaluation, and why?`

Must see: 有 endpoint shortlist 和 why，不只是罗列。
Expected question_type: `endpoints`
Expected primary family: `endpoint-handbook`
Expected strongest surface: `topics/ckd/endpoint-handbook.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-ckd-001, src-ckd-003, src-ckd-004, src-ckd-006, src-ckd-010, src-ckd-013`

Routing read:

- router question_type: `endpoints`
- first family: `endpoint-handbook`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/papers/src-ckd-001.md, raw/papers/src-ckd-002.md, raw/papers/src-ckd-003.md, raw/papers/src-ckd-004.md, raw/papers/src-ckd-006.md, raw/papers/src-ckd-007.md, raw/papers/src-ckd-010.md, raw/papers/src-ckd-013.md, raw/papers/src-ckd-015.md, raw/papers/src-ckd-017.md, topics/ckd/endpoint-handbook.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 猫慢性肾脏疾病（CKD）疗效评估中最适用的终点评估指标及其选择理由研究
[info] Loaded: topics/ckd/endpoint-handbook.md
[info] Hop 1/3 (~3577 tokens loaded)...
[info] Agent ready to synthesize
[info] Fallback source preload from compiled pages: ['src-ckd-001', 'src-ckd-002', 'src-ckd-003', 'src-ckd-004', 'src-ckd-006', 'src-ckd-007', 'src-ckd-010', 'src-ckd-013', 'src-ckd-015', 'src-ckd-017']
[info] Fallback loaded source: src-ckd-001
[info] Fallback loaded source: src-ckd-002
[info] Fallback loaded source: src-ckd-003
[info] Fallback loaded source: src-ckd-004
[info] Fallback loaded source: src-ckd-006
[info] Fallback loaded source: src-ckd-007
[info] Fallback loaded source: src-ckd-010
[info] Fallback loaded source: src-ckd-013
[info] Fallback loaded source: src-ckd-015
[info] Fallback loaded source: src-ckd-017
[info] Vision: 1 verified figure(s) available from ['src-ckd-017']
[info] Synthesizing (11 files, ~23872 tokens)...
[meta] ROUTER_QTYPE=endpoints
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=endpoint-handbook
[meta] LOADED_PATHS=raw/papers/src-ckd-001.md,raw/papers/src-ckd-002.md,raw/papers/src-ckd-003.md,raw/papers/src-ckd-004.md,raw/papers/src-ckd-006.md,raw/papers/src-ckd-007.md,raw/papers/src-ckd-010.md,raw/papers/src-ckd-013.md,raw/papers/src-ckd-015.md,raw/papers/src-ckd-017.md,topics/ckd/endpoint-handbook.md
```

Result excerpt:

```text
用于猫慢性肾脏病（CKD）疗效评价的最实用终点指标主要包括核心层的肌酐、尿比重（USG）、尿蛋白肌酐比值（UPCR）、收缩压和血清磷。这些指标不仅贯穿诊断、临床分期和病程进展，还能有效反映不同的结构损伤模式，从而支持多维度疗效评估和预后判断。诊断终点指明疾病存在及分期，强调如肌酐持续升高（>140 µmol/L且>15%基线增高）、尿比重异常（<1.035）的持续性异常，以及证实蛋白尿和高血压（多次平均收缩压>170 mmHg）等辅助判定，而疗效评估终点则侧重于动态变化和治疗响应，尤其关注磷、蛋白尿及血压的波动。这些核心终点在一线临床实践中基于ISFM专家共识指南（src-ckd-004）和一系列回顾性及前瞻性研究均有明确支持，体现猫独特的疾病表现和检测现实；例如，组织形态学研究显示肌酐、磷和贫血指标主要关联肾小管间质纤维化，而蛋白尿和收缩压则对应肾小球及血管病变，为不同终点提供了结构基础（src-ckd-010）。早期检测层面，SDMA作为辅助性早期标记物敏感度高且受肌肉量影响少，但目前尚不具备单独筛查资格，宜作为诊断和分期的辅助指标，而非替代核（src-ckd-004, src-ckd-024）。治疗评估则特别强调磷的控制及蛋白尿的治疗靶点作用，伴随收缩压的管理是减缓病程和保护靶器官的重要方向（src-ckd-003, src-ckd-006），且疗效评价应结合临床症状和健康相关生活质量参数，确保综合疗效观测（src-ckd-013）。总体而言，终点指标的使用需严谨区分诊断目标与疗效判断，合理划分主要（如肌酐、UPCR、收缩压、磷的趋势和水平）与次要终点（SDMA、PTH等背景解读指标），并应结合猫特异性证据和持续动态监测，以科学反映病情变化与治疗效果[quoted_fact: src-ckd-004][source_supported_conclusion: src-ckd-010][source_supported_conclusion: src-ckd-006][source_supported_conclusion: src-ckd-013][llm_inference][quoted_fact: src-ckd-003][quoted_fact: src-ckd-001].

尚未解决的空白主要体现在：(1)早期诊断尤其是非氮质血症阶段的敏感监测工具实用性仍有待验证，GFR虽为理论金标准，但因操作复杂难以常规使用；(2)蛋白尿的病理分区解释尚需更细致的亚型临床数据支持，特别是在不同蛋白尿形态与疗效反应间的关系厘清中（src-ckd-017）；(3)CKD矿物质骨代谢紊乱中，钙及相关生物标记物如FGF23、α-Klotho的临床应用及干预效果尚无充分猫特异性前瞻性研究（src-ckd-015）；(4)不同治疗方法及药物类别对终点指标的权重及优先级尚需更多实证指导，尤其是在试验设计和临床实践的有效衔接（src-ckd-013）。

---

## 研究者视角

猫CKD的核心机制以肾小管间质纤维化为共同结构终点，尽管上游病因复杂多变。临床上，肌酐、尿比重、UPCR、收缩压和磷水平构成结构损伤的多轴反映，这些指标在不同损伤路径（如纤维化vs肾小球-血管损伤）中扮演关键角色。持续的生理动态监测及趋势判断是诊断和疗效判定的基石。蛋白尿不仅是进展标志，还涵盖不同的病理分区（如免疫复合物肾小球病变与继发性CKD），需要结合病理学细分解读。磷的代谢与PTH补偿机制交织，需综合评估以指导控制治疗。辅助标记物SDMA虽敏感，对早期发现有帮助却不能替代核心指标。临床试验端应纳入更广泛结局集，包括生活质量、生存期等多维评估，以强化研究的转化价值。

## 不能说过头的地方

现有证据主要局限于晚期或中期CKD的诊断与监测，早期检测的实用性和敏感性仍不足，未能完全由猫特异性数据支持。SDMA作为辅助检测工具不能被误用为独立筛查标准。蛋白尿的解读应尊重不同病理背景，不宜简单以数值大小直接评估病情或疗效。影像学诊断及背景矿物质指标（PTH、FGF23等）目前更多用于辅助解释及管理，非一线疗效终点。所有结论严格依赖文献证据，不构成具体临床干预建议，临床应用前应结合综合诊断及兽医专家指导。

## 下一步

未来应聚焦开展：(1)早期检测敏感标记物（如SDMA、GFR变异体）的临床实用性和预测价值前瞻性研究；(2)蛋白尿不同病理亚型的临床特征和预后差异分析，以完善分层治疗策略；(3)矿物质骨代谢相关生物标记物（FGF23、α-Klotho）在猫CKD中的作用及对临床结局的预测价值前瞻验证；(4)基于多维终点指标系统的干预疗效综合评估研究，提升临床试验和实际管理的转化性与精准度。这些步骤将促进猫CKD疗效终点选择的科学性与临床指导价值的提升。
```

## Q3. CKD claim verification

Question: `Verify whether SDMA should already be treated as a core early-detection anchor in this vault.`

Must see: 必须是 verification 风格，同时呈现支持与保留条件。
Expected question_type: `claim_verification`
Expected primary family: `verify-a-claim`
Expected strongest surface: `system/indexes/verify-a-claim.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-ckd-001, src-ckd-002, src-ckd-004`

Routing read:

- router question_type: `claim_verification`
- first family: `verify-a-claim`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/papers/src-ckd-001.md, raw/papers/src-ckd-002.md, raw/papers/src-ckd-003.md, raw/papers/src-ckd-004.md, raw/papers/src-ckd-005.md, raw/papers/src-ckd-006.md, raw/papers/src-ckd-007.md, raw/papers/src-ckd-008.md, raw/papers/src-ckd-009.md, raw/papers/src-ckd-010.md, system/indexes/verify-a-claim.md, topics/ckd/current-state-dashboard.md, topics/ckd/endpoint-handbook.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 验证SDMA作为猫慢性肾病早期检测核心生物标志物的适用性及其临床价值。
[info] Loaded: system/indexes/verify-a-claim.md
[info] Loaded: topics/ckd/current-state-dashboard.md
[info] Loaded: topics/ckd/endpoint-handbook.md
[info] Hop 1/3 (~10203 tokens loaded)...
[info] Agent ready to synthesize
[info] Fallback source preload from compiled pages: ['src-ckd-001', 'src-ckd-002', 'src-ckd-003', 'src-ckd-004', 'src-ckd-005', 'src-ckd-006', 'src-ckd-007', 'src-ckd-008', 'src-ckd-009', 'src-ckd-010']
[info] Fallback loaded source: src-ckd-001
[info] Fallback loaded source: src-ckd-002
[info] Fallback loaded source: src-ckd-003
[info] Fallback loaded source: src-ckd-004
[info] Fallback loaded source: src-ckd-005
[info] Fallback loaded source: src-ckd-006
[info] Fallback loaded source: src-ckd-007
[info] Fallback loaded source: src-ckd-008
[info] Fallback loaded source: src-ckd-009
[info] Fallback loaded source: src-ckd-010
[info] Vision: 2 verified figure(s) available from ['src-ckd-001']
[info] Synthesizing (13 files, ~30337 tokens)...
[meta] ROUTER_QTYPE=claim_verification
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=verify-a-claim
[meta] LOADED_PATHS=raw/papers/src-ckd-001.md,raw/papers/src-ckd-002.md,raw/papers/src-ckd-003.md,raw/papers/src-ckd-004.md,raw/papers/src-ckd-005.md,raw/papers/src-ckd-006.md,raw/papers/src-ckd-007.md,raw/papers/src-ckd-008.md,raw/papers/src-ckd-009.md,raw/papers/src-ckd-010.md,system/indexes/verify-a-claim.md,topics/ckd/current-state-dashboard.md,topics/ckd/endpoint-handbook.md
```

Result excerpt:

```text
SDMA目前应被视为猫CKD早期检测的辅助标记物，而非核心早期检测锚点或独立筛查指标。它对早期肾功能减退的敏感性优于肌酐，且几乎不受肌肉量变化影响，具有明显的辅助诊断和监测价值，但指南和综述均明确指出，SDMA尚不建议作为单独筛查工具使用。猫CKD的诊断和分期仍以血清肌酐、尿比重（USG）、尿蛋白肌酐比（UPCR）、收缩压及血磷为核心终点指标，SDMA作为辅助的早期标记物纳入综合判断体系，辅助提升对非氮质血症早期阶段的识别而非取代传统方法[quoted_fact: src-ckd-004, src-ckd-002][source_supported_conclusion: src-ckd-004, src-ckd-002]。

核心支持证据包括ISFM共识指南（src-ckd-004）明确指出SDMA灵敏性高于肌酐，常用于早期检测支持，且该指南拒绝将SDMA作为单一筛查手段；诊断核心仍以肌酐和尿比重联合持久异常判定为主，SDMA为附属辅助指标。多篇综述（src-ckd-002、src-ckd-024）和生物标记物综述证实这一定位，强调早期检测问题复杂，单用SDMA检测尚不成熟。此外，现有文献指出猫CKD早期检测实务依赖多指标连续监测与趋势分析，而非单次指标判定，SDMA的辅助价值体现在整合入连续追踪流程中。临床实践中，SDMA不可取代现有诊断确认框架，同时也面临早期检测技术操作限制[quoted_fact: src-ckd-004, src-ckd-002][source_supported_conclusion: src-ckd-004, src-ckd-002]。

尚未解决的空白主要是：SDMA的临床操作方案尚未完全标准化，例如其最佳阈值设定、单独与多指标联合使用的早期检测敏感性和特异性比较；SDMA在不同CKD阶段的动态变化模式及与其他早期标记物（如GFR测定、代谢组学筛查）的关联；以及SDMA辅助干预决策的临床效果是否能够实质改善预后和延缓病程，仍缺乏高质量干预研究支持。这些空白表明目前SDMA仍处于“辅助性早期检测支持”层级，而非核心早期诊断锚点[quoted_fact: src-ckd-004][llm_inference][llm_inference]。

---

## 研究者视角

基于猫CKD已深提炼的文献，疾病机制以肾小管间质纤维化为稳定核心，终点指标层级分明：核心层包含肌酐、尿比重、UPCR、收缩压、血磷等直接关联诊断和预后，辅助层以SDMA和肾小球滤过率（GFR）为早期功能减退指示，背景层则包括PTH、钙、FGF23等矿物质代谢指标。SDMA作为辅助早期检测标记在多个高权重文献（如ISFM指南）中定位明确，灵敏度优于肌酐，且因受肌肉量影响小而具有理论优势，但指南一致强调其不可作为独立筛查标准，故其临床使用场景主要是连续监测的辅助手段，与传统诊断终点指标形成互补。研究背景显示，猫CKD诊断困境在于症状多晚期出现且缺乏足够早期钝感标记物，故早期检测战略注重多指标综合与高风险筛查人群识别，SDMA是这一结构中重要但尚非唯一依赖的环节，未来研究需加强其操作化方案与预后改善验证[quoted_fact: src-ckd-004, src-ckd-002, src-ckd-001][source_supported_conclusion: src-ckd-004][llm_inference]。

## 不能说过头的地方

当前文献明确区分了诊断核心与辅助检测标记层级，SDMA不能取代肌酐及尿比重等诊断指标，且尚无单项指标能独立完成早期CKD筛查的支持证据。物种差异和操作复杂性限制了人类CKD研究直接外推至猫。SDMA的临床使用应保持科学、循证的严谨态度，避免将其宣传为万能早筛工具。该知识库内容基于现有高权重文献与指南，不构成专业兽医临床诊断或治疗建议，具体诊疗方案应结合临床实际和专业判断。

## 下一步

推荐继续开展高质量的前瞻性临床研究，明确SDMA与其他早期指标（如GFR、代谢组学等）联合早期识别效果及阈值设定；开发规范化的多指标早期检测工作流，验证其对病程延缓和预后改善的贡献；加强SDMA在不同CKD病理阶段的动态变化监控与临床干预指导价值的研究；并在临床指南中持续更新SDMA的操作建议，确保其合理纳入综合早期筛查和监测战略。与此同时，应保持现有诊断及管理流程稳健运行，避免SDMA被误用为独立检测或治疗决策基石。[llm_inference]
```

## Q4. FIP diagnostic workup

Question: `What is the current diagnostic workup architecture for feline FIP?`

Must see: 不能把 diagnosis 简化成单一 assay。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/fip/risk-and-recognition.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-fip-003, src-fip-005, src-fip-006, src-fip-007, src-fip-008, src-fip-012, src-fip-015, src-fip-020, src-fip-023`

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
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 当前猫传染性腹膜炎（FIP）的诊断流程及其架构的系统性分析与评估
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
[info] Synthesizing (10 files, ~15067 tokens)...
[meta] ROUTER_QTYPE=recognition
[meta] ROUTER_DISEASE=fip
[meta] FIRST_FAMILY=risk-and-recognition
[meta] LOADED_PATHS=raw/papers/src-fip-003.md,raw/papers/src-fip-005.md,raw/papers/src-fip-006.md,raw/papers/src-fip-007.md,raw/papers/src-fip-008.md,raw/papers/src-fip-012.md,raw/papers/src-fip-015.md,raw/papers/src-fip-020.md,raw/papers/src-fip-023.md,topics/fip/risk-and-recognition.md
```

Result excerpt:

```text
目前猫传染性腹膜炎（FIP）的诊断工作流程架构强调多层次综合识别体系，以风险背景提示潜在疑虑，由临床病理学与疾病形式引导初步怀疑，再辅以分支特色的实验室检测和分子支持，尤其在神经或眼部表现时调整诊断方向，脑脊液（CSF）检测成为专门支持手段，而非普适首选。该流程遵循风险因素先行（如年轻年龄、特定品种雄性猫群、密集多猫环境等），但不构成诊断依据，随后以临床病理表现（湿性、非湿性及其分期）主导识别疑端，之后辅以病毒变异筛查和特异性辅助检测（包括CSF的RT-PCR），神经或眼部症状时预先转入专属分支，治疗反应均处于诊断流程之后，不影响初诊判定[quoted_fact: src-fip-003][quoted_fact: src-fip-005][quoted_fact: src-fip-006][quoted_fact: src-fip-015][quoted_fact: src-fip-023][llm_inference].

核心证据包括：首先，从风险层面，研究显示年轻猫、特定品种（英短、德文卷毛、阿比西尼亚），雄性过度代表，还有多猫环境中肠冠状病毒的流行风险，能显著提高FIP怀疑度但本身非诊断证据[quoted_fact: src-fip-005][quoted_fact: src-fip-008][quoted_fact: src-fip-012][quoted_fact: src-fip-020]。其次，临床病理学是识别的核心，多个病例系列通过分析湿性与非湿性临床特征及病程分期，建立了层次化识别架构，有助于系统地将不同病例分类与怀疑度层级区分开[quoted_fact: src-fip-006][quoted_fact: src-fip-015]。再次，带有神经或眼科症状的病例，诊断流程需改变路径，将脑脊液病毒检测作为高特异性诊断支持，虽灵敏度有限但阳性高度确认，体现了分支式诊断的必要[quoted_fact: src-fip-023]。此外，湿性FIP涉及独特的免疫生理机制，提示湿性与非湿性疾病的免疫病理差异，进一步支持形式识别的重要性[quoted_fact: src-fip-007]。综上，FIP的诊断工作流是一个结构严谨的逐层推进流程，诊断依赖于综合风险、临床与实验室证据的体系支持，而非单一试验结果。

目前仍存在的空白和挑战包括：具体的临床病理变量在不同病例和地理背景间的普适排序尚不明确，现有分期体系的标准化和推广力度不足，诊断的临床敏感性与特异性需在现代抗病毒时代背景下重新验证，风险影响因子在非澳大利亚和非特定群体中外推的有效性仍待证实，脑脊液RT-PCR对非神经及非眼部病例的诊断价值有限且阴性结果不足以排除FIP，需开发更精确的辅助生物标志物群以提升早期与非典型病例的诊断准确度[quoted_fact: src-fip-003][quoted_fact: src-fip-006][quoted_fact: src-fip-023][quoted_fact: src-fip-005][quoted_fact: src-fip-015].

## 研究者视角

FIP的诊断认识架构是一套多层次识别体系，涵盖宿主信号（年龄、品种、性别）、环境风险（多猫共同环境中的模型冠状病毒感染压力）、具体临床表现（湿性/非湿性病形及分期）和分子诊断支持（病毒RNA检测及变异筛查）等维度。其病理特征涵盖多种病程表现形式，湿性FIP伴强烈免疫介导的液体渗出，非湿性FIP则涉及多器官肉芽肿形成，神经和眼部表现则要求CSF检测辅助确认。生物标志物群尚未形成明确单一金标准，因病毒变异较大和宿主反应多样，故诊断依赖于风险背景、临床病理学模式识别以及结合特异实验室和分子测试的综合推断。此外，学科研究仍聚焦于优化识别的分子方法和风险模型，防止单一试验误导诊断，推动分期体系标准化和临床适用性验证。

## 不能说过头的地方

当前诊断流程是风险提示与临床病理学模式识别主导的复合式判断体系，不应将风险因素、种群统计或单一检测结果视为确诊依据，尤其动物品种或年龄分布在不同地区可能存在差异，外推时需谨慎。CSF RT-PCR阳性虽高度特异，但阴性不能排除神经型FIP，无症状猫或非神经表现病例使用该检测结果的局限性较大。诊断仍无简单快速的“金标准”替代方法，任何诊断建议应结合临床全貌和实验室验证，且不应用作兽医诊断替代。对于患者治疗反应的观察也不能回溯调整初步诊断疑虑层级。

## 下一步

后续研究应重点验证和标准化FIP疾病形态的分期系统，明确关键临床病理指标的诊断敏感性与特异性，整合并评估分子检测试剂盒在不同临床表现层面的性能表现，特别是针对非神经、非湿性病例的检测策略。进一步开展多地区、多种族的流行病学调查，细化风险因素模型，避免单一风险过分解读。同时，兴建多中心前瞻性队列研究以验证诊断工作流程的实际临床效用，并探索联合生物标志物组与影像学的复合诊断路径。此外，重视神经型FIP特异检测指标的开展与优化，及早发现和区分临床亚型，促进诊断精准化与个体化管理。
```

## Q5. HCM recognition versus endpoint

Question: `For feline HCM, what should be separated between recognition and endpoints?`

Must see: 承认 recognition 和 endpoint 是两层。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/hcm/risk-and-recognition.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-hcm-001, src-hcm-009, src-hcm-010, src-hcm-012, src-hcm-013, src-hcm-023, src-hcm-024`

Routing read:

- router question_type: `recognition`
- first family: `risk-and-recognition`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/papers/src-hcm-001.md, raw/papers/src-hcm-002.md, raw/papers/src-hcm-008.md, raw/papers/src-hcm-009.md, raw/papers/src-hcm-010.md, raw/papers/src-hcm-012.md, raw/papers/src-hcm-013.md, raw/papers/src-hcm-021.md, raw/papers/src-hcm-023.md, raw/papers/src-hcm-024.md, topics/hcm/endpoint-handbook.md, topics/hcm/risk-and-recognition.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 猫肥厚型心肌病（HCM）研究中，识别标准与终点指标应如何明确区分和定义？
[info] Loaded: topics/hcm/risk-and-recognition.md
[info] Loaded: topics/hcm/endpoint-handbook.md
[info] Hop 1/3 (~3445 tokens loaded)...
[info] Agent ready to synthesize
[info] Fallback source preload from compiled pages: ['src-hcm-001', 'src-hcm-002', 'src-hcm-008', 'src-hcm-009', 'src-hcm-010', 'src-hcm-012', 'src-hcm-013', 'src-hcm-021', 'src-hcm-023', 'src-hcm-024']
[info] Fallback loaded source: src-hcm-001
[info] Fallback loaded source: src-hcm-002
[info] Fallback loaded source: src-hcm-008
[info] Fallback loaded source: src-hcm-009
[info] Fallback loaded source: src-hcm-010
[info] Fallback loaded source: src-hcm-012
[info] Fallback loaded source: src-hcm-013
[info] Fallback loaded source: src-hcm-021
[info] Fallback loaded source: src-hcm-023
[info] Fallback loaded source: src-hcm-024
[info] Vision: no verified figures on disk yet (extract PDFs to enable)
[info] Synthesizing (12 files, ~18875 tokens)...
[meta] ROUTER_QTYPE=recognition
[meta] ROUTER_DISEASE=hcm
[meta] FIRST_FAMILY=risk-and-recognition
[meta] LOADED_PATHS=raw/papers/src-hcm-001.md,raw/papers/src-hcm-002.md,raw/papers/src-hcm-008.md,raw/papers/src-hcm-009.md,raw/papers/src-hcm-010.md,raw/papers/src-hcm-012.md,raw/papers/src-hcm-013.md,raw/papers/src-hcm-021.md,raw/papers/src-hcm-023.md,raw/papers/src-hcm-024.md,topics/hcm/endpoint-handbook.md,topics/hcm/risk-and-recognition.md
```

Result excerpt:

```text
针对猫的肥厚型心肌病（HCM），识别（recognition）与终点指标（endpoints）之间应当保持明确分离，尤其是在结构型表型确认（echocardiographic phenotype and gross morphometry）与生物标志物、人工智能辅助或基因型解释之间的层级关系上。识别过程应以超声心动图为核心的结构表型为第一位，作为HCM表型的金标准，辅助以宏观形态测量以提高区分度，尤其是严重病例较易直观确认，而轻中度肥厚仍需排除其他病因，以免误诊[quoted_fact: src-hcm-001][quoted_fact: src-hcm-009][quoted_fact: src-hcm-013][source_supported_conclusion: src-hcm-001][source_supported_conclusion: src-hcm-009][source_supported_conclusion: src-hcm-013]。生物标志物如NT-proBNP适合用于扫描和标记重度疾病，但不适合用作轻度及中度HCM的筛查工具或结构确认，其信号更多是疾病负担或严重程度的反映[quoted_fact: src-hcm-010][source_supported_conclusion: src-hcm-010]；而肌钙蛋白I更适合作为心肌损伤和负担的指示器，而非结构表型的定义指标[llm_inference][llm_inference]。人工智能诊断目前更多是辅助和筛查工具，提供折衷的计算机辅助诊断支持，尚未达到替代超声心动图的核心确认地位[quoted_fact: src-hcm-023][source_supported_conclusion: src-hcm-023]。此外，基因型和年龄应作为风险修饰因素和解释修正层面参与，但基因突变阳性状态不等同于当前结构表型的确诊，基因剂量和年龄相关渗透率均影响临床表现，应分层考虑而非简单替代结构表型确认[quoted_fact: src-hcm-012][source_supported_conclusion: src-hcm-012]。终点指标层面应构建分层体系，首先为基于结构确认的表型定义，其次为NT-proBNP等的重度疾病筛查辅助，随后为肌钙蛋白的组织损伤与疾病负担指示，最后是新兴生物标志物、AI辅助以及右心室参与和解剖病理学分期所揭示的晚期重塑表型。这种分层结构防止了终点指标的扁平化，将不同指标的临床意义和适用范畴清晰分割[quoted_fact: src-hcm-009][quoted_fact: src-hcm-010][llm_inference][llm_inference][llm_inference][quoted_fact: src-hcm-024][source_supported_conclusion: src-hcm-009][source_supported_conclusion: src-hcm-010][llm_inference][llm_inference][llm_inference][source_supported_conclusion: src-hcm-024]。

**核心证据**：

- 识别应结构优先，超声心动图及宏观形态确认占据主导，轻中度肥厚需排除其他病因，避免过度诊断[quoted_fact: src-hcm-001][quoted_fact: src-hcm-009][quoted_fact: src-hcm-013]。
- NT-proBNP显著升高提示严重HCM，但对轻中度病例无显著筛查价值，不宜单独用作诊断工具[quoted_fact: src-hcm-010]。
- 肌钙蛋白I标志心肌损伤及疾病负担，使用时应区别于结构表型确认角色[llm_inference]。
- AI辅助诊断主要作为筛查及放射科支持，尚未形成替代结构型诊断的权威层级[quoted_fact: src-hcm-023]。
- MYBPC3基因突变剂量及年龄渗透率影响HCM严重程度和临床表现，基因型为修饰参数，不等同表型确认[quoted_fact: src-hcm-012]。
- 终末期HCM表型表现为纤维化沉积、心腔扩大及冠脉动脉硬化等多维结构重塑，与早期肥厚表现明显不同，提示终点评价需层级分割，避免混淆识别与严重度终点[quoted_fact: src-hcm-024]。

**尚未解决的空白**：

- 生物标志物及AI辅助工具在多品种、多疾病混合临床样本中的广泛适用性和真伪阳性/阴性界限尚需前瞻性验证。
- 轻中度HCM的排除诊断具体标准和客观量化阈值仍缺乏一致共识。
- 终末期病理分期的临床可视化早期识别及预后相关性判定不足，阻碍该端点应用于临床工作流首诊或监测。
- AI模型基于单一影像模式，难以区分多种心脏疾病病因，缺乏多模态临床信息融合应用研究。
- 基因突变多样性及组合效应对识别和终点定义的综合影响需要更大样本和多基因层面研究进一步明晰。

---

## 研究者视角

猫HCM的识别体系应基于结构表型的分层确认，其核心是超声心动图结合宏观心脏形态计量，优先定义肥厚的结构表型，避免过早依赖生物标志物和基因型数据。结构表型本身表现为高度异质性，包括弥漫性和节段性肥厚，伴随心腔容积缩小，确认复杂且受排除性诊断限制。生物标志物如NT-proBNP和肌钙蛋白I反映疾病负担和严重程度，但其作用属于终点评估和筛查辅助，非初诊结构确认。AI诊断作为放射学支持的新兴工具，必须保持在辅助层级，其临床替代能力有待验证。基因型信息（尤其MYBPC3 p.A31P剂量效应）为风险修饰因子，需结合年龄相关渗透率解读，反映疾病发展的时间动态。晚期结构重塑通过纤维化沉积、心腔扩张和血管重构表型得以识别，为严重度分级提供了形态学深度，使识别与终点明确区分，保障临床工作流的严谨与效率。

## 不能说过头的地方

现有证据明确指向超声心动图为猫HCM结构确认的核心，但超声评估仍对轻中度肥厚具有诊断上的不确定性，生物标志物和AI辅助不应被误用为单独诊断工具。基因型作为风险修饰不能等同结构性病变确认，年龄相关外显率进一步限制了早期直接确诊。AI模型依赖数据量和图像视角限制，未完成临床广泛验证，不能贸然上升为首诊权威。病理分期提供深层次严重度视角，但其临床应用受限，无法成为一线诊断或识别标准。所有上述结论均基于当前文献，尚不构成具体临床诊断建议，实际病例管理仍需专科兽医综合判断。

## 下一步

- 开展多中心、大样本的前瞻性研究，验证NT-proBNP、肌钙蛋白和AI辅助诊断在不同临床环境及各品种猫的筛查及诊断性能。
- 制定和细化轻中度HCM的排除性诊断标准，明确超声心动图和宏观形态计量阈值，减少误诊风险。
- 探索多模态AI诊断模型融合临床数据和多视角影像，提高其鉴别不同心肌病和心脏疾病的能力，并设计前瞻试验检验临床可行性。
- 加强长期随访队列，研究基因剂量效应及年龄因素对HCM发病机制、表型演变及预后的影响，推动精准风险分层。
- 聚焦晚期HCM的病理重塑机制，发展非侵入性早期识别方法，将病理分期指标临床化，用以优化治疗决策和预后监测。
```

## Q6. IBD versus lymphoma boundary

Question: `Where is the current IBD versus small-cell lymphoma boundary in this vault?`

Must see: 应该像 boundary answer，不应像 generic disease summary。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/ibd/risk-and-recognition.md`

Exit code: `0`
Confidence: `high`
Source IDs found: `src-ibd-003, src-ibd-004, src-ibd-009, src-ibd-010, src-ibd-015, src-ibd-016, src-ibd-017, src-ibd-019, src-ibd-024`

Routing read:

- router question_type: `recognition`
- first family: `risk-and-recognition`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/papers/src-ibd-003.md, raw/papers/src-ibd-004.md, raw/papers/src-ibd-009.md, raw/papers/src-ibd-010.md, raw/papers/src-ibd-015.md, raw/papers/src-ibd-016.md, raw/papers/src-ibd-017.md, raw/papers/src-ibd-019.md, raw/papers/src-ibd-024.md, system/indexes/ibd-lymphoma-boundary-memo.md, topics/ibd/risk-and-recognition-bilingual.md, topics/ibd/risk-and-recognition.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 明确并界定炎症性肠病（IBD）与猫小细胞淋巴瘤在本数据库中的鉴别标准及边界。
[info] Loaded: topics/ibd/risk-and-recognition.md
[info] Loaded: topics/ibd/risk-and-recognition-bilingual.md
[info] Hop 1/3 (~3107 tokens loaded)...
[info] Loaded: system/indexes/ibd-lymphoma-boundary-memo.md
[info] Hop 2/3 (~4226 tokens loaded)...
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
[info] Synthesizing (12 files, ~18935 tokens)...
[meta] ROUTER_QTYPE=recognition
[meta] ROUTER_DISEASE=ibd
[meta] FIRST_FAMILY=risk-and-recognition
[meta] LOADED_PATHS=raw/papers/src-ibd-003.md,raw/papers/src-ibd-004.md,raw/papers/src-ibd-009.md,raw/papers/src-ibd-010.md,raw/papers/src-ibd-015.md,raw/papers/src-ibd-016.md,raw/papers/src-ibd-017.md,raw/papers/src-ibd-019.md,raw/papers/src-ibd-024.md,system/indexes/ibd-lymphoma-boundary-memo.md,topics/ibd/risk-and-recognition-bilingual.md,topics/ibd/risk-and-recognition.md
```

Result excerpt:

```text
炎症性肠病（IBD）与小细胞淋巴瘤（small-cell lymphoma）在本知识库中的边界目前被定义为一个多模式、多层面的诊断排除过程，而非单一检测即可确立。其核心界限架构以“排除性诊断”为首要原则，强调从疑似慢性肠病（chronic enteropathy）开始，结合临床活动度、成像表现、组织活检位置、病理学报告结构和支持性生物标记物，逐层加权形成对小细胞淋巴瘤的怀疑与排除。具体如下：[source_supported_conclusion: src-ibd-003][source_supported_conclusion: src-ibd-004][source_supported_conclusion: src-ibd-015][source_supported_conclusion: src-ibd-010][source_supported_conclusion: src-ibd-009][source_supported_conclusion: src-ibd-016][source_supported_conclusion: src-ibd-017][source_supported_conclusion: src-ibd-019][source_supported_conclusion: src-ibd-024]

**核心证据**：

1. **诊断框架：**  
   猫IBD是排除性诊断，临床和组织学上，饮食性肠病和分化良好的肠道小细胞淋巴瘤均可模拟IBD表现，因此边界必须始于慢性肠病的临床怀疑，并积极排除模拟疾病。[source_supported_conclusion: src-ibd-003]

2. **临床活动指数（FCEAI）：**  
   FCEAI指数用于慢性肠病的活动度评估和治疗反应追踪，适用于IBD及食物反应性肠病，但不能区分IBD与淋巴瘤。[source_supported_conclusion: src-ibd-004]

3. **成像压力：**  
   超声肌层增厚明显倾向于淋巴瘤，尤其在老年猫，但并非确诊标志；淋巴结肿大虽异常但非特异，见于两者均可。[source_supported_conclusion: src-ibd-010]

4. **活检部位策略：**  
   十二指肠和回肠活检结果差异显著，小细胞淋巴瘤可能仅限于回肠或者十二指肠，全面评估两部位是确保排除淋巴瘤的关键步骤。[source_supported_conclusion: src-ibd-015]

5. **病理报告结构与解读：**  
   常规WSAVA结构化显微镜特征可能遗漏自由文本描述中的判别信息，特别是浆细胞数量是提高判别力的关键特征。病理报告的标准化应作为辅助而非替代采样和诊断。[source_supported_conclusion: src-ibd-009]

6. **组织标记物辅助：**  
   Bcl-2免疫标记在淋巴瘤中表达显著高于IBD，但两者均有高表达，故仅是淋巴瘤倾向性标记而非单一诊断依据。[source_supported_conclusion: src-ibd-016]

7. **非侵入性支持标记物：**  
   粪便S100A12可区分健康与病态，但不能区分IBD与淋巴瘤，是炎症的非特异支持指标。[source_supported_conclusion: src-ibd-017]

8. **代谢组前沿研究：**  
   粪便代谢组学显示多不饱和脂肪酸等代谢物对IBD与淋巴瘤的差异有较好分类能力，提示代谢物层面可能实现疾病分型，但尚不适合常规临床使用。[source_supported_conclusion: src-ibd-019]

9. **实践框架：**  
   IBD识别应嵌入更广泛的慢性肠病框架中，避免狭义“特发性IBD”标签，强调多层线索的排除诊断流程。[source_supported_conclusion: src-ibd-024]

**尚未解决的空白**：

- 目前尚无一项单独的检测或标志物能够实现IBD与小细胞淋巴瘤的确切鉴别，生物标记物（如Bcl-2、S100A12及代谢组学）均存在重叠和信号不确定性。  
- 活检采样策略虽已显著提高诊断准确性，但是否所有病例必须全面回肠活检仍需结合临床疑似情况，缺乏精准操作规程。  
- 代谢组学等前沿技术需要更大队列和纵向验证，确认其临床适用性及对病理诊断的增值效能。  
- 影像学指标主要为怀疑提示，缺乏明确的定量阈值及临床决策指导标准。  
- 病理报告文本标准化虽能提升诊断一致性，但对跨病理医生的可重复性和实际病例分类改进程度尚不足够明晰。

---

## 研究者视角

猫的IBD与小细胞淋巴瘤边界是一个复杂的多模态诊断问题，其核心在于排除模拟疾病和利用多层次证据提高鉴别力。病理组织活检仍为金标准，其中活检部位的选择极为关键，单一部位活检存在诊断遗漏风险。超声影像中肌层增厚是最有力的淋巴瘤提示信号，但需结合临床信息和病理证据确认。组织标记物如Bcl-2提供了微观水平的肿瘤指示，但表达重叠限制了其单独的诊断值。非侵入性标志物如粪便S100A12虽指示肠道炎症存在，但无法分辨IBD与淋巴瘤。代谢组学为未来的疾病分类与分型提供了前沿生物标志物，反映了病理生理机制的不同层面。整体框架强调“慢性肠病”这一广义操作容器，IBD定位为排除诊断后得出，避免过早贴标签。多学科结合的流程设计是实现准确鉴别的关键。

## 不能说过头的地方

现阶段不能将临床活动指数、肌层厚度超声表现或单一组织标记物作为IBD与小细胞淋巴瘤的确定性诊断依据；单一部位活检阴性不代表排除淋巴瘤；自由文本病理描述与结构化报告存在差异，不能单凭机器学习模型结果替代临床诊断；非侵入性生物标志物尤其需警惕过度解读，当前证据不支持常规独立诊断应用；代谢组学虽有研究价值，但尚未纳入标准诊断流程。临床应坚持综合多模态评估和排除性原则，避免科学炒作引导误诊误治。本回答不构成任何专业兽医个案诊断建议，临床具体判断仍需结合个体病史和全面诊断手段。

## 下一步

- 针对代谢组学和其他生物标志物扩展大规模、多中心前瞻性队列验证，以评估其诊断准确性和临床转化价值。  
- 制定和推广基于影像学与临床风险分层的内镜活检采样规范，明确何种临床场景必须伴随回肠活检。  
- 开展多病理专家盲审对比研究及文本报告标准化项目，提高病理诊断的一致性和信息利用率。  
- 发展基于多模态数据融合的诊断算法，尝试将临床、影像、病理及分子标记多层信号整合，为IBD和小细胞淋巴瘤鉴别提供决策支持。  
- 开展临床应用导向的长期随访研究，明确不同诊断类别的预后模式和治疗响应，优化整体慢性肠病管理框架。
```

## Q7. Cross-disease question

Question: `Compare CKD and HCM on the maturity of their endpoint architecture.`

Must see: 要么稳妥回答，要么诚实降级，不能假精确。
Expected question_type: `synthesis`
Expected primary family: `disease-module-maturity-ladder`
Expected strongest surface: `system/indexes/disease-module-maturity-ladder.md`

Exit code: `0`
Confidence: `low`
Source IDs found: `src-ckd-004, src-ckd-013`

Routing read:

- router question_type: `synthesis`
- first family: `disease-module-maturity-ladder`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `answer-compression-miss`
- next fix layer: `answer-compression`
- loaded paths: `raw/papers/src-ckd-001.md, raw/papers/src-ckd-002.md, raw/papers/src-ckd-003.md, raw/papers/src-ckd-004.md, raw/papers/src-ckd-006.md, raw/papers/src-ckd-007.md, raw/papers/src-ckd-010.md, raw/papers/src-ckd-013.md, raw/papers/src-ckd-015.md, raw/papers/src-ckd-017.md, system/indexes/cross-disease-second-wave-narrow-owner-audit.md, system/indexes/disease-module-maturity-ladder.md, topics/ckd/endpoint-handbook.md, topics/hcm/endpoint-handbook.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 比较猫慢性肾脏病（CKD）与肥厚型心肌病（HCM）终点结构成熟度的差异及其临床意义。
[info] Loaded: system/indexes/disease-module-maturity-ladder.md
[info] Loaded: system/indexes/cross-disease-second-wave-narrow-owner-audit.md
[info] Loaded: topics/ckd/endpoint-handbook.md
[info] Loaded: topics/hcm/endpoint-handbook.md
[info] Hop 1/3 (~8288 tokens loaded)...
[info] Agent ready to synthesize
[info] Fallback source preload from compiled pages: ['src-ckd-001', 'src-ckd-002', 'src-ckd-003', 'src-ckd-004', 'src-ckd-006', 'src-ckd-007', 'src-ckd-010', 'src-ckd-013', 'src-ckd-015', 'src-ckd-017']
[info] Fallback loaded source: src-ckd-001
[info] Fallback loaded source: src-ckd-002
[info] Fallback loaded source: src-ckd-003
[info] Fallback loaded source: src-ckd-004
[info] Fallback loaded source: src-ckd-006
[info] Fallback loaded source: src-ckd-007
[info] Fallback loaded source: src-ckd-010
[info] Fallback loaded source: src-ckd-013
[info] Fallback loaded source: src-ckd-015
[info] Fallback loaded source: src-ckd-017
[info] Vision: 4 verified figure(s) available from ['src-ckd-001', 'src-ckd-017']
[info] Synthesizing (14 files, ~28582 tokens)...
[meta] ROUTER_QTYPE=synthesis
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=disease-module-maturity-ladder
[meta] LOADED_PATHS=raw/papers/src-ckd-001.md,raw/papers/src-ckd-002.md,raw/papers/src-ckd-003.md,raw/papers/src-ckd-004.md,raw/papers/src-ckd-006.md,raw/papers/src-ckd-007.md,raw/papers/src-ckd-010.md,raw/papers/src-ckd-013.md,raw/papers/src-ckd-015.md,raw/papers/src-ckd-017.md,system/indexes/cross-disease-second-wave-narrow-owner-audit.md,system/indexes/disease-module-maturity-ladder.md,topics/ckd/endpoint-handbook.md,topics/hcm/endpoint-handbook.md
```

Result excerpt:

```text
慢性肾脏病（CKD）和肥厚型心肌病（HCM）在终点指标架构的成熟度上均已达到较高水平，但CKD已达最高控制层级（Level 7）且显示出第二层窄owner信号，反映其终点架构高度完善和细化；而HCM处于晚期Level 6.5向Level 7过渡阶段，同样出现了第二层边界信号，显示出接近最高成熟度但仍略逊于CKD的架构完善度[llm_inference][llm_inference]。

CKD的终点架构已全面涵盖了核心操作终点（肌酐、尿比重、UPCR、收缩压、磷）、辅助早期检测标记物（SDMA）、背景解释指标（PTH、钙、FGF23、贫血指标、影像学评估）及多轴结构病变映射，支持连续追踪和多维病理结构分层解读。其终点指标不仅涵盖诊断与分期，也含括预后判断和治疗效果评估，且配合详实的临床试验核心结局集，体现了深厚的研究和实践基础[llm_inference][quoted_fact: src-ckd-004][quoted_fact: src-ckd-013]。该架构具备完整的输出层（briefing、dossier、slides），双语编译层和完善的控制层，包含审计、回写和优先级路线等管理要素，且已开展第二波细化，如基于肾脏病理特征的优先memo评估、分支内部边界判定等[llm_inference][llm_inference]。

相比之下，HCM侧重结构性确认（超声表型、形态计量学）作为主导终点，并将严重病变筛查增效（如NT-proBNP）与损伤和负荷信号（心肌肌钙蛋白I）区分开。前沿标记物和AI技术作为辅助增强层次加入，同时右心室参与和病理分期拓展了疾病表型和进展解释。这种端点架构保留结构确认的第一权威，避免将多种指标简单并列，体现了分层而非扁平的成熟设计，且已有工作备有工作版输出文件、双语编译并开始向跨语言控制层推进。HCM当前介于Level 6.5和7之间，控制层尚不及CKD厚实，边界和分支细化刚起步，已有AI增强边界等第二层控制信号反映持续发展状态[llm_inference][llm_inference][llm_inference]。

在终点架构的系统性完备和临床工作流输出成熟度方面，CKD以其丰富的指标类别、多轴病变相关性和成熟的多语种控制层领先，HCM虽已具备显著层级架构和部分边界细化，但在整体管理宽度和深度上稍逊一筹，反映不同疾病领域终点架构建设的进化状态。

## 研究者视角

猫CKD的终点架构整合了生物标志物（肌酐、SDMA、UPCR等）、病理结构对应（肾小管间质纤维化、肾小球硬化、血管病变）及临床监测指标（收缩压、磷、PTH等）形成多层次、多维度的终点体系，强调连续监测与病理背景interpretation。这种多轴解读避免了简单坍缩评分，促进精准分期和治疗指南制定。CKD终点体系兼顾临床实际与科研需求，覆盖诊断确认、病程预后和治疗干预评估，且实现了全流程双语编译和控制机制，支持系统审计及优先级调度。

HCM终点体系则以结构性心肌肥厚超声标志为核心，辅以血清心肌损伤标志物和严重疾病筛查工具，整合前沿生物标记物和AI技术提升精细度和预测能力。同时通过右心室病变和病理分期增强表型深度，形成层级分明、功能清晰的终点架构。二者均已过基础阶段，进入层级控制和边界细化的高阶拓展区，显示临床决策和研究应用上的成熟度提升趋势。

## 不能说过头的地方

CKD的终点体系虽高度成熟，但部分标志物（如SDMA、影像学、PTH等）依旧作为辅助或背景指标，不能替代核心诊断指标。临床定期监测和疾病进展评估力求连续采样，不能仅凭单点数据。HCM终点虽分层清晰，但AI和新兴标记仍处于辅助验证阶段，未完全确立常规诊断权威。两病种的研究多依赖回顾性和部分外推人类研究数据，跨物种外推应保持谨慎。模块成熟度虽显示架构完备，但具体临床应用仍需专业兽医依据个体情况综合判断，不构成直接诊断或治疗建议。

## 下一步

为进一步提升CKD终点架构，应着重推动具体治疗类别和病理特征的终点映射，强化临床试验与常规诊疗终点的区分，开展更多早期钙磷代谢及PTH、FGF23等标志物的前瞻性研究以完善背景层。HCM方面，需加强AI和前沿生物标记物的验证，深化右心室参与和组织病理学分期指标与临床终点的功能关联，同时完善第二层窄owner边界判定以实现更精细的路径管理与个体化风险分层。跨疾病的第二波窄owner开发策略应被优先实施，针对各分支的边界、门槛和优先级进行更硬的结构梳理，使终点架构既稳固又灵活支持临床和研究需求。
```

## Q8. Regulatory question

Question: `What is the current regulatory path surface for feline CKD programs across China, FDA, and VMD?`

Must see: 至少承认 jurisdiction split。
Expected question_type: `regulatory`
Expected primary family: `regulatory-brief`
Expected strongest surface: `topics/ckd/regulatory-brief.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-reg-001, src-reg-002, src-reg-003, src-reg-004, src-reg-005, src-reg-006, src-reg-007, src-reg-008, src-reg-009`

Routing read:

- router question_type: `regulatory`
- first family: `regulatory-brief`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/regulations/src-reg-001-cn-vet-registration.md, raw/regulations/src-reg-002-cn-approval-number.md, raw/regulations/src-reg-003-cn-import.md, raw/regulations/src-reg-004-fda-animal-drugs.md, raw/regulations/src-reg-005-fda-conditional.md, raw/regulations/src-reg-006-fda-active-controls.md, raw/regulations/src-reg-007-ema-limited-market.md, raw/regulations/src-reg-008-vmd-marketing-authorisation.md, raw/regulations/src-reg-009-vmd-annex2.md, topics/ckd/regulatory-brief.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 研究中国、美国FDA和英国VMD对猫慢性肾病（CKD）治疗项目的当前监管路径和要求。
[info] Loaded: topics/ckd/regulatory-brief.md
[info] Hop 1/3 (~4704 tokens loaded)...
[info] Agent ready to synthesize
[info] Fallback source preload from compiled pages: ['src-reg-001', 'src-reg-002', 'src-reg-003', 'src-reg-004', 'src-reg-005', 'src-reg-006', 'src-reg-007', 'src-reg-008', 'src-reg-009']
[info] Fallback loaded source: src-reg-001
[info] Fallback loaded source: src-reg-002
[info] Fallback loaded source: src-reg-003
[info] Fallback loaded source: src-reg-004
[info] Fallback loaded source: src-reg-005
[info] Fallback loaded source: src-reg-006
[info] Fallback loaded source: src-reg-007
[info] Fallback loaded source: src-reg-008
[info] Fallback loaded source: src-reg-009
[info] Vision: no verified figures on disk yet (extract PDFs to enable)
[info] Synthesizing (10 files, ~10659 tokens)...
[meta] ROUTER_QTYPE=regulatory
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=regulatory-brief
[meta] LOADED_PATHS=raw/regulations/src-reg-001-cn-vet-registration.md,raw/regulations/src-reg-002-cn-approval-number.md,raw/regulations/src-reg-003-cn-import.md,raw/regulations/src-reg-004-fda-animal-drugs.md,raw/regulations/src-reg-005-fda-conditional.md,raw/regulations/src-reg-006-fda-active-controls.md,raw/regulations/src-reg-007-ema-limited-market.md,raw/regulations/src-reg-008-vmd-marketing-authorisation.md,raw/regulations/src-reg-009-vmd-annex2.md,topics/ckd/regulatory-brief.md
```

Result excerpt:

```text
当前，猫慢性肾脏病（CKD）在中国、美国FDA及英国VMD的监管路径存在显著差异，反映了各管辖区法规结构和证据要求的特点。中国的监管路径应视为一条正式的兽药注册路径，包含新兽药注册、产品批准文号管理及进口管理三级执行层级，且需要产品完成临床试验后提交注册申请，同时进口产品还须满足海关通关及标签等进口行政要求，这条路径并无快捷“人药转宠物药”方案[quoted_fact: src-reg-001, src-reg-002, src-reg-003][source_supported_conclusion: src-reg-001, src-reg-002, src-reg-003]。美国FDA则将监管路径分为完全批准（需实质性疗效证据）和有条件批准（基于合理疗效预期，且猫被归为主要物种，且有条件批准适用需满足复杂性疾病或研究困难的法定条件），强调早期试验设计的重要性，尤其活性对照设计在伴侣动物适应症中的适用性，且不能默认猫CKD产品自动符合有条件批准资格[quoted_fact: src-reg-004, src-reg-005, src-reg-006][source_supported_conclusion: src-reg-004, src-reg-005, src-reg-006]。英国VMD要求申请者选择多种上市许可途径中的一种，并且在卷宗文件提交时必须满足现行附录及科学指南的要求，监管路径强调途径选择和卷宗结构的复杂性，不应被简化为单一路径[quoted_fact: src-reg-008, src-reg-009][source_supported_conclusion: src-reg-008, src-reg-009]。欧盟EMA提供了基于《欧盟条例2019/6》第23条的有限市场路线指南，这可为部分非免疫兽药产品提供减轻数据负担的路径，但猫CKD具体是否符合该有限市场资格尚需明确评估，因此需要尽早测试适用性，尤其对产品策略影响重大[quoted_fact: src-reg-007][source_supported_conclusion: src-reg-007]。

综上所述，中国路径呈现为严格、层级分明的注册和生产合规体系，美国FDA路径则需在完全批准与有条件批准之间做具体适用资格判断，英国VMD强调多样化授权路径并对卷宗结构提出严格要求，而欧盟EMA的有限市场逻辑则为某些情况下的数据需求减免提供战略机会，但全部辖区尚未形成针对猫CKD伴侣动物肾脏病适应症特异性的疗效或试验设计官方指南。当前无任何官方法规支持跨辖区的“人药转宠物药”简化路径，需慎重对待该战略设想[quoted_fact: src-reg-001, src-reg-003, src-reg-004, src-reg-008][source_supported_conclusion: src-reg-001, src-reg-004, src-reg-008][llm_inference].

核心证据包括：中国农业农村部对兽药注册（含进口兽药）的正式法规规定，要求产品完成临床试验并取得批准文号方可上市生产[quoted_fact: src-reg-001, src-reg-002, src-reg-003]；美国FDA将动物药品批准划分为完全批准与有条件批准两条路径，对于条件批准的适用性需结合疾病严重性及研发难度评估，伴侣动物的临床试验设计指南提供活性对照设计应用建议[quoted_fact: src-reg-004, src-reg-005, src-reg-006]；欧洲药品管理局通过2024年起实施的有限市场法规指南，为特定非免疫类兽药提供数据要求减轻的合规路径，但适用范围需明确[quoted_fact: src-reg-007]；英国VMD要求针对兽药上市许可实行多条路径体系，卷宗结构遵循严格科学指导要求[quoted_fact: src-reg-008, src-reg-009]。

尚未解决的空白主要有：缺乏面向猫CKD适应症的专门疗效终点官方指南，特别是FDA、EMA和VMD均未公开具体的伴侣动物肾脏病试验设计及疗效证据包规范；中国尚无公开的详细伴侣动物申报材料技术要求文档，进口与国产路径的决策树尚不完善；欧盟有限市场资格及FDA有条件批准资格针对猫CKD的具体适用性仍未明确；“人药转宠物药”跨辖区简化路径仍属内部策略设想，缺乏官方支持文献；各辖区间的监管路径尚停留在框架或路径级别，缺少针对不同产品原型的细化实施方案。

---

## 研究者视角

猫CKD监管路径的核心机制体现在不同监管体系对兽药注册、批准及上市的分层管理。中国着眼于新兽药注册、产品批准文号及进口管理三个行政层面，体现了严谨的合规与分权执行。美国FDA严格区分完全批准与有条件批准，要求实质疗效证据或合理疗效预期，并依据疾病复杂性和研究难度对条件批准设限，强调临床试验设计的科学性，尤其活性对照方案的重要性。欧盟EMA基于有限市场法规为特定小众兽药提供减负通道，从而减少研发负担，考虑到猫CKD的市场范围相对有限，该条款可能成为关键策略。英国VMD则从多路径授权及伴随卷宗要求的角度，反映出较为灵活但严格规范的市场准入环境。现有的生物标志物及试验终点因缺乏跨辖区一致标准而制约了统一监管路径的形成，亟需针对猫CKD的领域特异性研发路径和数据标准。

## 不能说过头的地方

本回答基于路径及政策框架层面证据，缺乏针对猫CKD适应症的具体疗效数据和试验设计指南，因此不宜对某一监管辖区路径的疗效证明要求做出定论。跨辖区的“人药转宠物药”快捷路径仍是内部讨论主题，当前无官方足够证据支持，临床选药及注册决策应以具体产品实际数据和法规要求为准。因此，本文不构成任何专业兽医诊断建议，而仅供研发及合规战略规划参考。

## 下一步

1. 收集并系统化猫CKD及伴侣动物肾脏病的具体疗效终点指导及临床试验设计资料，尤其针对FDA CVM、EMA及VMD的官方技术文件。
2. 深入了解中国兽药注册的材料和数据要求，尤其进口与国产兽药路径的分支决策树，完善国内路径的实施细节。
3. 评估欧盟有限市场申请资格及美国有条件批准的适用条件，结合猫CKD的疾病负担及市场特点，明确最具战略价值的管辖区路径。
4. 建立针对产品原型（如小分子、再定位资产、营养类干预等）与证据包（多研究证据包、特殊路径逻辑包）之间的匹配体系，辅助临床工作流设计和监管决策。
5. 推动多辖区监管对话，促进形成共享的猫CKD适应症研发终点标准及监管共识，降低跨境注册壁垒，提高产品上市效率。
```
