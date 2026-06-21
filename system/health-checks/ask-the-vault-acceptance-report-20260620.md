---
id: system-ask-the-vault-acceptance-report-20260620
type: health-check
topic: operating-system
question_type: acceptance
language: zh
last_compiled_at: 2026-06-20
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: needs_review
---

# Ask The Vault Acceptance Report, 2026-06-20

Suite: research
Execution mode: executed
Backend: openrouter
Write-back: off
Acceptance status: needs_review

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
| Q1 | CKD mechanism spine | 0 | mechanism | mechanism-overview | yes | no | no-clear-failure | none | 6 | medium | pass-leaning |
| Q2 | CKD endpoint selection | 0 | mechanism | mechanism-overview | yes | qtype-miss | qtype-miss | qtype | 1 | medium | pass-leaning |
| Q3 | CKD claim verification | 0 | claim_verification | verify-a-claim | yes | no | no-clear-failure | none | 2 | medium | pass-leaning |
| Q4 | FIP diagnostic workup | 0 | recognition | risk-and-recognition | yes | no | answer-compression-miss | answer-compression | 1 | low | pass-leaning |
| Q5 | HCM recognition versus endpoint | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 7 | medium | pass-leaning |
| Q6 | IBD versus lymphoma boundary | 0 | recognition | risk-and-recognition | yes | no | provenance-miss | provenance | 0 | low | needs-review |
| Q7 | Cross-disease question | 0 | endpoints | endpoint-handbook | no | qtype-miss | qtype-miss | qtype | 2 | low | pass-leaning |
| Q8 | Regulatory question | 0 | regulatory | regulatory-brief | yes | no | no-clear-failure | none | 9 | high | pass-leaning |

Acceptance summary: 4/8 automated pass-leaning answers; 0 execution failures; 1 provenance misses; 2 route misses. Status: needs_review.

## Detailed Runs

## Q1. CKD mechanism spine

Question: `CKD 的核心机制主线是什么？`

Must see: 至少落到 CKD mechanism 强答案面，且至少 2 个真实 source ids。
Expected question_type: `mechanism`
Expected primary family: `mechanism-overview`
Expected strongest surface: `topics/ckd/mechanism-overview.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-ckd-001, src-ckd-010, src-ckd-011, src-ckd-015, src-ckd-016, src-ckd-021`

Routing read:

- router question_type: `mechanism`
- first family: `mechanism-overview`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/papers/src-ckd-001.md, raw/papers/src-ckd-002.md, raw/papers/src-ckd-004.md, raw/papers/src-ckd-006.md, raw/papers/src-ckd-009.md, raw/papers/src-ckd-010.md, raw/papers/src-ckd-011.md, raw/papers/src-ckd-015.md, raw/papers/src-ckd-016.md, raw/papers/src-ckd-021.md, topics/ckd/mechanism-overview.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 研究猫慢性肾脏病（CKD）的核心病理机制及其主要病理生理通路。
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
[info] Synthesizing (11 files, ~26072 tokens)...
[meta] ROUTER_QTYPE=mechanism
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=mechanism-overview
[meta] LOADED_PATHS=raw/papers/src-ckd-001.md,raw/papers/src-ckd-002.md,raw/papers/src-ckd-004.md,raw/papers/src-ckd-006.md,raw/papers/src-ckd-009.md,raw/papers/src-ckd-010.md,raw/papers/src-ckd-011.md,raw/papers/src-ckd-015.md,raw/papers/src-ckd-016.md,raw/papers/src-ckd-021.md,topics/ckd/mechanism-overview.md
```

Result excerpt:

```text
猫慢性肾脏病（CKD）的核心机制主线是肾小管间质纤维化，这一病理学改变被认为是猫CKD中最常见且与肾功能下降相关性最强的共同最终病变。CKD主要发生于老年猫（通常大于12岁），表现为以肾小管间质炎症、肾小管萎缩、纤维化和继发肾小球硬化为特征的退行性疾病，原发性肾小球病则极为罕见。多种临床终点指标，如蛋白尿、血磷和收缩压，分别对应不同的肾脏结构病变（如纤维化、肾小球肥大及血管损伤），提示CKD的病理进展是多维的、多机制并存而非单一维度。矿物质代谢紊乱（CKD-MBD）在CKD机制中占据独立分支，其包括血磷、钙、甲状旁腺激素（PTH）及成纤维细胞生长因子-23（FGF-23）等多种代谢异常，FGF-23的升高往往早于血磷升高，具有潜在的早期生物标志物价值。促纤维化介质如TGF-beta通路在病理进展中发挥重要作用，且猫肾皮质成纤维细胞表现出对TGF-beta1的响应。此外，衰老、肾缺血及缺氧等因素被列为上游促成因素，虽未被确证为主导病因，但丰富了CKD的发病机制。肠道源性尿毒症毒素的蓄积揭示了肠肾轴可能在机理中发挥作用。新兴的感染性与遗传性病因包括猫副粘病毒（FeMV）感染导致的淋巴浆细胞性肾小管间质性炎症及caspase-3介导的凋亡，以及波斯猫中PKD1基因突变引起的常染色体显性多囊肾病（ADPKD）[source_supported_conclusion: src-ckd-001][source_supported_conclusion: src-ckd-010][source_supported_conclusion: src-ckd-011][source_supported_conclusion: src-ckd-015][source_supported_conclusion: src-ckd-016][source_supported_conclusion: src-ckd-021][llm_inference][llm_inference][llm_inference][llm_inference].

**核心证据：**

1. **肾小管间质纤维化为机制主干**：多项关键文献阐明纤维化是猫CKD的最终共同路径，也是最与肾功能指标（肌酐、磷、贫血）高度相关的病理病变（src-ckd-001, src-ckd-010, src-ckd-011, src-ckd-016）。肾小管间质纤维化及其与蛋白尿和肾小球肥大相关的表现，成为结构病变和临床终点的桥梁。

2. **老年猫为主要患病群体，原发肾小球病罕见**：CKD绝大多数发生于老年猫，且病理以肾间质炎症、肾小管萎缩和继发硬化为主，强调衰老为疾病进展的重要内生因素（src-ckd-016）。

3. **蛋白尿、磷、血压反映不同病理损伤模式**：蛋白尿与纤维化和肾小球肥大相关；高磷血症及FGF-23升高关联矿物质代谢异常；血压升高则与肾小球硬化及小动脉硬化相关，三者构成多维度的病理指标体系（src-ckd-010, src-ckd-009, src-ckd-015, src-ckd-026）。

4. **CKD矿物质和骨代谢异常（CKD-MBD）多层面机制**：除磷之外，还涉及钙及调控因子如PTH和FGF-23，FGF-23升高早于血磷异常，是更早期的潜在生物标志物；同时，过分磷限制饮食可能诱发高钙血症（src-ckd-015, src-ckd-026, src-ckd-029）。

5. **纤维化促成介质及通路**：体外实验显示原代肾皮质成纤维细胞对TGF-beta1有明确的促纤维化转录反应，TGF-beta信号为可追踪的机制桥梁且为潜在治疗靶点（src-ckd-011, src-ckd-050）。醛固酮/盐皮质激素受体（MR）介导通路因其在其他物种肾脏损伤中的重要作用，被定位为未来的研究重点（src-ckd-021）。

6. **上游促成因素**：衰老、缺血、缺氧虽被认为是诱发因素但目前证据不足以确认主导地位（src-ckd-016, src-ckd-022, src-ckd-023）。

7. **肠肾轴及肠道源尿毒症毒素蓄积**：代谢组学研究揭示硫酸吲哚酚、硫酸对甲酚和TMAO等毒素在CKD猫体内积累，提供肠道微生物-肾脏相互作用的新兴机制视角（src-ckd-027）。

8. **感染性与遗传性新兴分支**：猫副粘病毒（FeMV）感染与肾小管间质性炎症及caspase-3介导的细胞凋亡相关，病毒载量与凋亡水平显著相关；波斯猫及相关品种的ADPKD由PKD1基因c.10063C>A杂合突变引发，导致多囊肾病变（src-ckd-037, src-ckd-087, src-ckd-121, src-ckd-162, src-ckd-038, src-ckd-058, src-ckd-061, src-ckd-101）。

**尚未解决的空白：**

- 猫CKD的具体初始病因尚不明确，多数渠道为老年退行性机制叠加，尚无确证主导的单一起因，纤维化被视为终末病理通路。
- 促纤维化的分子介质（如TGF-beta及MR信号）在猫体内的确切机制、时序和干预价值仍未充分确立，当前多基于体外或间接推断。
- 肠肾轴中肠道微生物群的具体作用机制尚属探索阶段，益生菌或益生元等干预策略证据不足。
- FeMV感染的流行病学与发病机制仍未达成临床普适应用共识，病毒在CKD整体发病中的比重和筛查指征尚需进一步研究。
- ADPKD存在部分猫咪中PKD1基因其他变异未明，基因型与临床表现的对应及遗传多样性尚需深入阐明。

---

## 研究者视角

猫CKD机制的核心在于肾小管间质纤维化，这是一条病理学和功能衰退的共同最终路径，强烈联系临床指标如肌酐、磷和贫血等。老年猫作为发病主要群体，其肾脏组织早期即表现纤维化、肾小管萎缩和间质炎症，提示衰老、慢性损伤与缺血缺氧可能作为上游背景因子。多维度临床指标（三大经典终点蛋白尿、血磷、血压）分别对应不同的结构路径，更精细地揭示病理演进的异质性。CKD-MBD复杂矿物质代谢异常包含钙、PTH、FGF-23等关键调控因子，FGF-23在临床上被证明为早期预警标志物。促纤维化介质层面，TGF-beta驱动的成纤维细胞活化和醛固酮/盐皮质激素受体介导的炎症及纤维化被视为关键环节，尽管实验性证据多见于体外及人类研究。肠道源性尿毒症毒素的代谢积累提出肠肾轴参与CKD通路的新视角。新兴的感染（FeMV）和遗传（PKD1突变导致ADPKD）因素则为CKD复杂发病机制补充了特异性病因候选。

---

## 不能说过头的地方

尽管纤维化是当前最清晰的机制锚点，但尚不能将任何单一初始病因为CKD主导。临床标志物不应简单合并为单一严重度评分，而应根据其对应病理特点多维度解读。TGF-beta及醛固酮/MR介入机制虽有坚实实验支持，但仍未发展为临床验证的治疗靶点。FGF-23生物标志物虽有潜力，但尚缺绝对定量的临床诊断阈值。肠道菌群调节和FeMV感染的作用仍处于探讨初期，不能视为所有CKD猫的普遍因素。ADPKD遗传筛查不适用于非典型品种且无囊肿表现的猫。此回答不构成具体诊断或治疗建议，临床决策应综合完整病史、物种特异性特征及专业兽医意见。

---

## 下一步

1. 开展更多体内层面纤维化相关介质（TGF-beta、MR等）及其信号通路的猫特异性机制研究，验证其干预潜力和安全性。
2. 深化对肠肾轴功能和肠道微生物群在CKD中的病理贡献，组织随机对照干预试验评估益生菌及益生元的疗效。
3. 持续大规模猫群体流行病学研究，明确FeMV感染的发病机制、病理学关联及防治策略，并制定针对高危群体的筛查方案。
4. 扩展PKD1和其他可能遗传变异的分子遗传学研究，完善多囊肾病的遗传诊断体系，尤其是在非波斯猫属及杂交种中的表现和遗传多样性。
5. 优化临床多标志物（蛋白尿、FGF-23、血压等）组合模型，用于早期筛查、疾病分期和预后评估，提高临床管理的个性化和精准化水平。
```

## Q2. CKD endpoint selection

Question: `What endpoints are most usable for feline CKD efficacy evaluation, and why?`

Must see: 有 endpoint shortlist 和 why，不只是罗列。
Expected question_type: `endpoints`
Expected primary family: `endpoint-handbook`
Expected strongest surface: `topics/ckd/endpoint-handbook.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-ckd-024`

Routing read:

- router question_type: `mechanism`
- first family: `mechanism-overview`
- strongest surface hit: `yes`
- clear miss: `qtype-miss`
- failure type: `qtype-miss`
- next fix layer: `qtype`
- loaded paths: `raw/papers/src-cancer-014.md, raw/papers/src-cancer-091.md, raw/papers/src-ckd-024.md, raw/papers/src-ckd-107.md, raw/papers/src-hcm-001.md, topics/ckd/endpoint-handbook.md, topics/ckd/mechanism-overview.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 评估猫慢性肾脏病（CKD）疗效时，最适用的终点指标有哪些及其作用机制解析
[info] Loaded: topics/ckd/mechanism-overview.md
[info] Loaded: topics/ckd/endpoint-handbook.md
[info] Search pre-loaded: src-ckd-024 (16 matches)
[info] Search pre-loaded: src-cancer-014 (15 matches)
[info] Search pre-loaded: src-ckd-107 (9 matches)
[info] Search pre-loaded: src-hcm-001 (8 matches)
[info] Search pre-loaded: src-cancer-091 (6 matches)
[info] Hop 1/3 (~18842 tokens loaded)...
[info] Agent ready to synthesize
[info] Vision: no verified figures on disk yet (extract PDFs to enable)
[info] Synthesizing (7 files, ~18842 tokens)...
[meta] ROUTER_QTYPE=mechanism
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=mechanism-overview
[meta] LOADED_PATHS=raw/papers/src-cancer-014.md,raw/papers/src-cancer-091.md,raw/papers/src-ckd-024.md,raw/papers/src-ckd-107.md,raw/papers/src-hcm-001.md,topics/ckd/endpoint-handbook.md,topics/ckd/mechanism-overview.md
```

Result excerpt:

```text
猫慢性肾脏病（CKD）评价中最实用的终点指标是肌酐、尿比重（USG）、尿蛋白肌酐比值（UPCR）、收缩压和血磷，原因在于这些指标分别映射不同的肾脏结构损伤模式且临床易测，能够构成全面且分层的诊断和疗效评价框架。肌酐作为经典的诊断和分期指标，虽受肌肉量影响且升高较晚，但仍是诊断和病程长期监控的核心；尿比重辅助确诊尿液浓缩功能的减退，强化肌酐的诊断价值；UPCR关联肾小管间质纤维化与肾小球肥大，是病程进展与预后重要指标；收缩压与肾小球硬化及增生性小动脉硬化相关，提示血流动力学损伤程度；而血磷反映矿物质代谢异常，与肾小管间质纤维化密切关联，且每升高一个单位血磷显著提高死亡风险[llm_inference]。此外，SDMA作为辅助性早期检测标记物，灵敏度优于肌酐，但特异性和独立筛查价值有限，应配合上述核心指标综合应用[quoted_fact: src-ckd-024]。不同终点指标通过多维度结构病理映射，支持疾病解读不应坍缩为单一评分，而是结合纤维化为主的肾小管间质损伤及肾小球-血管损伤两大病理通路分层解释[llm_inference]。连续的动态追踪（特别是肌酐趋势及收缩压重复测量）是终点指标逻辑的必要组成部分，避免单次读数误判[llm_inference]。

核心证据涵盖了国际兽医学指南基于临床最小数据库制定的诊断和分期标准（src-ckd-004），组织形态学研究中对标临床指标与微观肾结构损伤的多维映射（src-ckd-010），血磷对预后的回顾性研究（src-ckd-006）以及矿物质代谢紊乱综合综述，详细阐述了FGF-23作为比血磷更早期的生物标记物潜力同时说明血磷监测的重要性（src-ckd-015），还有最新的关于SDMA性能和局限性的综述强化了其辅助而非替代角色（src-ckd-024）。综合来看，这些指标的选择基于其机制承载性强、临床易测和跨层级病程反映作用，为猫CKD临床诊疗和药效评价提供了合理且实用的框架。

尚未解决的空白包括：SDMA的临床特异性数据仍有限且未能完全明确其在不同临床工作流中的权重和地位；成像指标虽然是结构性评估的重要补充，但其与临床试验终点指标的衔接度和标准化应用需要进一步验证；血磷及矿物质代谢指标如PTH和FGF-23的绝对诊断阈值尚无统一共识，临床如何根据这些指标精准调整治疗仍待深入研究；此外，一些新兴的生物标记物和尿液中的蛋白质标志物等，尚处探索阶段，缺乏广泛临床验证，未来有望成为补充性终点[quoted_fact: src-ckd-024]。

---

## 研究者视角

猫CKD终点指标体系基于多层机制与临床指标的耦合，以肾小管间质纤维化为病理主干，关联肌酐、血磷、贫血等指标反映肾功能损害。蛋白尿和收缩压则桥接了肾小球与血管损伤病理，体现病程进展及血流动力学压力。肾脏矿物质和骨代谢紊乱（CKD-MBD）概念包含了钙、PTH和FGF-23网络，超越传统单一血磷监控。SDMA作为肾小球滤过率（GFR）的较新生物标记，虽具有敏感性优势，但特异性不完全，不能脱离临床背景单独使用。连续监测和多标志物集成评估是目前诊断、管理与疗效评估的最佳实践。此体系支持多轴终点评估与个体化管理，体现CKD复杂的异质性与进展多样性。

## 不能说过头的地方

当前仍无法将所有终点指标等同视作疾病严重程度的单一标尺，亦不可将SDMA吹捧为普适独立筛查工具。血磷的解读必须结合PTH水平，不能孤立判读。影像学结构评估为辅助而非主导终点。新兴尿液和损伤生物标记物尚处研究阶段，不宜纳入常规终点评价。对此框架的总结不构成具体的兽医临床诊断建议，所有临床实践应基于综合专业判断。

## 下一步

建议开展前瞻性临床研究，量化SDMA与传统肌酐等指标在不同病程阶段的联合预测价值，明确其临床特异性与早期诊断优势。进一步验证FGF-23及PTH等矿物质代谢指标与临床预后的相关性，建立猫特异性标志物阈值。加强多模态（血液、生化、尿液、影像）联合终点指标的动态监测体系，构筑多层级、多维度的整合诊疗工作流。期望通过临床试验纳入这些多维终点开发精准药效评价指标体系，推动猫CKD干预策略的精细化和个性化进展。

---

[quoted_fact: src-ckd-024]  
[source_supported_conclusion: src-ckd-024]
```

## Q3. CKD claim verification

Question: `Verify whether SDMA should already be treated as a core early-detection anchor in this vault.`

Must see: 必须是 verification 风格，同时呈现支持与保留条件。
Expected question_type: `claim_verification`
Expected primary family: `verify-a-claim`
Expected strongest surface: `system/indexes/verify-a-claim.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-ckd-018, src-ckd-024`

Routing read:

- router question_type: `claim_verification`
- first family: `verify-a-claim`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/papers/src-ckd-018.md, raw/papers/src-ckd-024.md, raw/papers/src-ckd-128.md, raw/papers/src-diabetes-035.md, raw/papers/src-hcm-194.md, system/indexes/verify-a-claim.md, topics/ckd/current-state-dashboard.md, topics/ckd/endpoint-handbook.md, topics/ckd/risk-and-recognition.md, ../../topics/ckd/endpoint-handbook.md, ../../topics/ckd/risk-and-recognition.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 验证血清对称二甲基精氨酸(SDMA)是否应作为猫肾脏疾病早期检测的核心指标。
[info] Loaded: system/indexes/verify-a-claim.md
[info] Loaded: topics/ckd/current-state-dashboard.md
[info] Loaded: ../../topics/ckd/endpoint-handbook.md
[info] Loaded: ../../topics/ckd/risk-and-recognition.md
[info] Search pre-loaded: src-ckd-024 (40 matches)
[info] Search pre-loaded: src-ckd-128 (36 matches)
[info] Search pre-loaded: src-ckd-018 (31 matches)
[info] Search pre-loaded: src-diabetes-035 (29 matches)
[info] Search pre-loaded: src-hcm-194 (29 matches)
[info] Hop 1/3 (~21731 tokens loaded)...
[info] Hop 2/3 (~21731 tokens loaded)...
[info] Agent ready to synthesize
[info] Vision: 2 verified figure(s) available from ['src-ckd-024']
[info] Synthesizing (9 files, ~21731 tokens)...
[meta] ROUTER_QTYPE=claim_verification
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=verify-a-claim
[meta] LOADED_PATHS=raw/papers/src-ckd-018.md,raw/papers/src-ckd-024.md,raw/papers/src-ckd-128.md,raw/papers/src-diabetes-035.md,raw/papers/src-hcm-194.md,system/indexes/verify-a-claim.md,topics/ckd/current-state-dashboard.md,topics/ckd/endpoint-handbook.md,topics/ckd/risk-and-recognition.md
```

Result excerpt:

```text
SDMA（对称二甲基精氨酸）当前应被视为猫慢性肾脏病（CKD）早期检测的重要辅助生物标志物，但尚不能作为核心独立的早期检测锚点单独使用。SDMA比传统肌酐对早期CKD检测更敏感且不受肌肉量影响，但其特异性数据仍有限，目前不推荐将SDMA作为单一筛查测试，而应配合肌酐、尿比重（USG）等多指标的连续监测体系应用。此外，代谢组学和机器学习等新兴方法显示出更优的早期检测潜力，但尚处于研究阶段，未能替代现有的序贯监测框架[quoted_fact: src-ckd-024][quoted_fact: src-ckd-018][source_supported_conclusion: src-ckd-024][source_supported_conclusion: src-ckd-018]。

【核心证据】
1. 2022年高权重生物标志物综述明确指出，SDMA作为新型肾小球滤过率（GFR）相关指标在早期检测CKD中表现出敏感性优势，但缺乏充分特异性数据，且不能单独用于筛查，依然需要结合肌酐和尿比重的序贯监测[quoted_fact: src-ckd-024][source_supported_conclusion: src-ckd-024]。
2. 2025年基于代谢组学和机器学习的研究显示，3-羟基犬尿喹啉（3-hydroxykynurenine）在极早期（约传统CKD2诊断前6个月）显示出更强的早期识别力，且多标记物模型的效果优于单一标记物（如SDMA），这提示未来可能通过代谢物组合模型辅助或增强早期识别[quoted_fact: src-ckd-018][source_supported_conclusion: src-ckd-018]。
3. 现有证据体系中，将SDMA置于辅助早期检测标记物层（support tier），而非核心操作性终点指标层，强调SDMA应作为序贯监测与多指标组合中的一个补充，而非替代方案[quoted_fact: src-ckd-024][source_supported_conclusion: src-ckd-024]。

【尚未解决的空白】
- SDMA特异性及其在各种共病（如甲状腺功能亢进）环境下表现的确切性能尚不完全明确，限制了其作为独立筛查工具的应用范围。
- 代谢组学中最佳早期标记物（如3-羟基犬尿喹啉）虽显示出较高预测力，但现阶段仍缺乏大规模、多中心临床验证及早期CKD阶段（CKD1）的系统检测数据。
- 如何将多标记物组合方案有效整合入临床工作流以实现高效成本比的实际早期筛查仍待进一步研究。

## 研究者视角
基于目前完全深提炼的猫CKD文献卡片层，SDMA属于辅助早期检测的生物标记物类别，与传统肌酐、尿比重等指标联合使用，能够补充诊断灵敏度，尤其是在肌肉量减少对肌酐干扰较大时。其本质是一种反映肾小球滤过率变化的GFR替代指标，但因特异性不足，不宜单独作为筛查锚点。结合代谢组学发展的最新成果，未来多标记物综合模型有望提升早期认知，但尚未成熟。SDMA定位于辅助层，肌酐、尿比重、蛋白尿、收缩压及磷等指标仍为临床核心操作层终点。早期检测架构需要纳入序贯监测的连续性逻辑，而非依赖单一时间点单一标志物[quoted_fact: src-ckd-024, src-ckd-018][source_supported_conclusion: src-ckd-024, src-ckd-018]。

## 不能说过头的地方
SDMA不是万能的独立早期筛查捷径，不能被误认为是取代肌酐或唯一筛查工具。当前数据表明其特异性不足且不能直接转化为临床诊断决策标准。代谢组学等新兴技术虽极具潜力，但仍处于研究层面，外推至临床普遍应用需更严谨的验证。将SDMA定位为辅助、非核心标志物符合现有循证证据，避免夸大其单独诊断价值。上述论断不构成具体的兽医临床诊断建议，实际诊疗需结合完整病史及多项指标综合判断[quoted_fact: src-ckd-024, src-ckd-018][source_supported_conclusion: src-ckd-024, src-ckd-018]。

## 下一步
1. 在临床研究中加强SDMA与传统指标（肌酐、USG等）联合序贯监测的实证研究，评估其在不同共病下的特异性表现。
2. 推动3-羟基犬尿喹啉及相关代谢组学多标志物模型的多中心大规模研究，验证其早期CKD（尤其是CKD1期）的检测效能与实用性。
3. 开发并优化临床可用的组合标志物检测策略和工作流，形成标准化、成本效益高且操作简便的早期CKD筛查方案。
4. 重视兽医临床诊疗实践中使用SDMA的规范化指导，避免其被误用为独立筛查或诊断替代品。

综上，SDMA应维持为辅助早期检测标志物的中坚，不能脱离肌酐等核心指标序列单独作为早期检测锚点。未来生物标志物的集成创新有潜力提升敏感度和特异性，但需要更完善的临床证据和工作流整合支持[quoted_fact: src-ckd-024, src-ckd-018][source_supported_conclusion: src-ckd-024, src-ckd-018][llm_inference]。
```

## Q4. FIP diagnostic workup

Question: `What is the current diagnostic workup architecture for feline FIP?`

Must see: 不能把 diagnosis 简化成单一 assay。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/fip/risk-and-recognition.md`

Exit code: `0`
Confidence: `low`
Source IDs found: `src-fip-131`

Routing read:

- router question_type: `recognition`
- first family: `risk-and-recognition`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `answer-compression-miss`
- next fix layer: `answer-compression`
- loaded paths: `raw/papers/src-fip-131.md, topics/fip/risk-and-recognition.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 系统性评估当前猫传染性腹膜炎（FIP）的诊断流程及其构建体系。
[info] Loaded: topics/fip/risk-and-recognition.md
[info] Search pre-loaded: src-fip-131 (4 matches)
[info] Hop 1/3 (~2805 tokens loaded)...
[info] Agent ready to synthesize
[info] Vision: no verified figures on disk yet (extract PDFs to enable)
[info] Synthesizing (2 files, ~2805 tokens)...
[meta] ROUTER_QTYPE=recognition
[meta] ROUTER_DISEASE=fip
[meta] FIRST_FAMILY=risk-and-recognition
[meta] LOADED_PATHS=raw/papers/src-fip-131.md,topics/fip/risk-and-recognition.md
```

Result excerpt:

```text
猫传染性腹膜炎（FIP）诊断工作流目前以风险评估、临床病理学和疾病类型判定为核心架构，随后辅以分支特异的实验室和分子检测支持。具体流程首先结合猫咪的年龄、品种、性别及多猫环境等风险背景，以提升对FIP的关注指数，但这仅作为风险筛查层面，而非诊断依据。接下来，依据临床表现（例如干型或湿型FIP）和实验室检测（如血液学变化、腹水特征），将风险转化为明确的疑诊状态。随后，结合有限的实验室数据和分子检测结果强化诊断信心，但这些支持测试的作用依赖于前期疑诊的确立，且不同病理形态（如神经型或眼部表现）要求切换至专门工作线程，进行脑脊液（CSF）检测等专门化分析。整个诊断流程强调的是“顺序识别”和“复合证据支持”，避免单一检测结果被过度依赖或提前主导诊断。治疗反应评估属于诊断后的辅助环节，不影响初步的诊断识别架构[llm_inference][llm_inference][llm_inference][llm_inference][llm_inference]。

核心证据包括澳大利亚多猫环境中的流行病学特征和品种风险（风险背景确定），悉尼和台湾对临床病理学及FIP分期的系统分析明确了湿型与干型FIP的识别要素，脑脊液检测则被确认是神经型FIP诊断分支的重要支持工具，且存在CSF检测阴性不能排除FIP的原则。多项深度综述及病例系列强调诊断架构的层级与顺序，认知框架从风险起点，经病理转换，到分子和分支测试的逐步支持，避免诊断流程中出现检测主导的混乱[llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference]。

尚未解决的空白主要在于针对不同FIP亚型的诊断试剂灵敏度和特异性的精准评估，尤其是分子检测方法和新兴AI算法辅助诊断系统（如CatBoost算法模型）的临床验证仍属探索阶段，目前缺乏充分公开的、细化的临床路径数据以支持机器学习在FIP诊断中的广泛应用和标准化。此外，不同地区和环境下FIP诊断的普适性和文化差异尚需进一步多中心前瞻性研究补充[quoted_fact: src-fip-131][llm_inference]。

---

## 研究者视角

FIP的诊断机制涉及家猫冠状病毒变异为致病型FIP病毒这一根本病理机制，临床表现因免疫反应差异而分为湿性（伴腹腔或胸腔积液）和干性（非渗出性肉芽肿性炎症）两大主要类型，部分病例表现为神经或眼部症状，形成专门的诊断分支。生物标志物包括伴随的炎症指标和病毒抗体反应，脑脊液内的病毒核酸检测提供了对神经型FIP的辅助支持。当前诊断是多层次的识别框架，强调临床病理学和病情分型作为疑诊核心，分子检测及CSF支持为辅助，风险因素提供背景增益。该架构防止单一检测结果导致误诊，确保综合多因子证据后进行临床判断，体现了复杂传染病异质性诊断的现代思路[llm_inference][llm_inference][llm_inference][llm_inference][llm_inference].

## 不能说过头的地方

目前的FIP诊断流程并不将风险因素视为独立诊断依据，且不能单凭腹水存在确认FIP，也不能依赖CSF的RT-PCR检测作为普遍适用的首选诊断手段。诊断需结合临床表现和综合多方位实验室支持；同时，治疗反应不应重新定义诊断顺序。新兴机器学习辅助诊断模型尚处开发初期，临床推广和外推至多地、多样品种环境的安全性与准确性未充分验证。所有诊断推断需基于专业兽医综合临床判断，不能替代临床兽医专业诊断建议[llm_inference][llm_inference][llm_inference][quoted_fact: src-fip-131].

## 下一步

未来研究应重点进行大规模、多中心的前瞻性临床验证，评估分子检测与传统临床病理指标在不同FIP亚型诊断中的敏感性和特异性；尤其是新算法模型如CatBoost在临床实践中的诊断准确性及实用性。此外，应加强对神经型和眼部FIP的专门检测方法的标准化研究。最终目标是形成一套既科学严谨又操作便捷的诊断工作流，兼顾不同专家及养猫环境的需求和条件，推动FIP的早期、准确诊断和分型，更有效指导临床治疗方案制定[quoted_fact: src-fip-131][llm_inference].
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
[info] Refined query: 关于猫肥厚型心肌病（HCM），应如何区分疾病的识别标准与研究终点指标？
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
[info] Synthesizing (12 files, ~17780 tokens)...
[meta] ROUTER_QTYPE=recognition
[meta] ROUTER_DISEASE=hcm
[meta] FIRST_FAMILY=risk-and-recognition
[meta] LOADED_PATHS=raw/papers/src-hcm-001.md,raw/papers/src-hcm-002.md,raw/papers/src-hcm-008.md,raw/papers/src-hcm-009.md,raw/papers/src-hcm-010.md,raw/papers/src-hcm-012.md,raw/papers/src-hcm-013.md,raw/papers/src-hcm-021.md,raw/papers/src-hcm-023.md,raw/papers/src-hcm-024.md,topics/hcm/endpoint-handbook.md,topics/hcm/risk-and-recognition.md
```

Result excerpt:

```text
对于猫HCM（肥厚型心肌病），识别（recognition）和终点（endpoints）之间应明确分离：识别应以结构表型为核心，重点依赖超声心动图表型和心脏宏观形态测量进行确认，避免单纯依赖生物标志物（如NT-proBNP）或人工智能（AI）诊断来定义表型；而终点指标层级则应由结构确认引领，随后是筛查辅助（例如NT-proBNP用于严重疾病的信号提示）、损伤和疾病负荷指标（如肌钙蛋白I）及病理学分期等深度表型解读，确保生物标志物和AI技术仅作为结构确认之下的辅助手段，二者在逻辑和应用层面实现清晰分工[quoted_fact: src-hcm-001][quoted_fact: src-hcm-009][quoted_fact: src-hcm-010][quoted_fact: src-hcm-013][quoted_fact: src-hcm-023][quoted_fact: src-hcm-024][source_supported_conclusion: src-hcm-001][source_supported_conclusion: src-hcm-009][source_supported_conclusion: src-hcm-010][source_supported_conclusion: src-hcm-023][source_supported_conclusion: src-hcm-024]。

核心证据包括：（1）识别方面，猫HCM的确诊依赖超声心动图评估心肌厚度与心脏形态变化，且轻中度增厚常需排除其他病因，不应单凭生物标志物或AI判定（如NT-proBNP对轻中度HCM筛查价值有限，AI诊断多为辅助而非替代工具）；（2）终点方面，结构表型确认是一线，之后生物标志物如肌钙蛋白I反映心肌损伤和疾病负荷，NT-proBNP主要用作严重病情的筛查和辅助标志，而AI及新型生物标志物则拓宽终点框架但仍居于结构确认之下；（3）病理学分期提供末期HCM的纤维化、腔室扩张等重构信息，深化终点层次但不改变结构表型作为首要识别方法的地位[quoted_fact: src-hcm-001][quoted_fact: src-hcm-009][quoted_fact: src-hcm-010][llm_inference][llm_inference][llm_inference][quoted_fact: src-hcm-024][source_supported_conclusion: src-hcm-001][source_supported_conclusion: src-hcm-009][source_supported_conclusion: src-hcm-010][source_supported_conclusion: src-hcm-023][source_supported_conclusion: src-hcm-024]。

尚未解决的空白包括生物标志物（如NT-proBNP和肌钙蛋白I）在不同猫种、早期HCM鉴别诊断和自然疾病进展中的性能边界，以及AI辅助诊断的标准化验证和跨机构推广可行性。此外，终点指标与临床预后、治疗响应以及分期系统的实时运用关系仍需深入验证，以保证非结构性终点工具的合理整合并避免过度依赖辅助检测[quoted_fact: src-hcm-010][quoted_fact: src-hcm-023][quoted_fact: src-hcm-024][llm_inference]。

## 研究者视角

猫HCM识别基于形态学结构表型，该表型富含异质性，包括节段性和弥漫性心肌肥厚，超声心动图和宏观心脏形态测量是确认诊断的金标准。生物标志物如NT-proBNP和肌钙蛋白I以及AI技术属于辅助识别和终点评估手段，前者在重度疾病筛查中表现优于轻度疾病，后者应当作为计算辅助工具存在，由基因型（如MYBPC3 p.A31P突变剂量）和年龄调节识别风险与严重程度的解析。终点层级框架强调结构确认优先，其次为生物标志物辅助，再后为心肌损伤指标与病理学分期，整体架构明确区分识别与严重度评估，保证临床决策有据且分层合理[quoted_fact: src-hcm-001][quoted_fact: src-hcm-009][quoted_fact: src-hcm-010][llm_inference][quoted_fact: src-hcm-012][quoted_fact: src-hcm-013][quoted_fact: src-hcm-023][quoted_fact: src-hcm-024]。

## 不能说过头的地方

现有证据尚未支持将生物标志物或AI诊断作为猫HCM的首选诊断标准，且多项生物标志物的筛查灵敏度和特异度因种群及疾病阶段不同存在明显限制。不同猫品种和遗传背景对生物标志物表达及AI算法表现的影响仍需谨慎外推。临床实践中应避免跳过结构性表型确认而直接采用辅助生物标志物做出诊断决定，当前证据亦不足以支持AI替代传统影像诊断。此外，治疗建议应谨慎界定为疾病管理和症状控制而非疾病逆转，不构成专业兽医诊断或治疗指南[quoted_fact: src-hcm-001][quoted_fact: src-hcm-010][quoted_fact: src-hcm-023][llm_inference]。

## 下一步

建议进一步开展大规模、多中心、异种群的前瞻性研究以评估NT-proBNP和肌钙蛋白I在不同早期HCM谱系中的筛查和监测性能，并结合影像学特征递进明确生物标志物阈值。AI辅助诊断算法应接受跨机构验证、标准化操作流程制定及临床工作流的整合测试。需加强结构型终点与临床预后和治疗反应的相关性研究，完善病理分期系统与实时临床指标的对应关系，促进识别层级与终点层级的动态联动和精准风险分层，最终实现多模态联合诊断和管理策略的科学评估和优化[quoted_fact: src-hcm-010][quoted_fact: src-hcm-023][quoted_fact: src-hcm-024][llm_inference]。
```

## Q6. IBD versus lymphoma boundary

Question: `Where is the current IBD versus small-cell lymphoma boundary in this vault?`

Must see: 应该像 boundary answer，不应像 generic disease summary。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/ibd/risk-and-recognition.md`

Exit code: `0`
Confidence: `low`
Source IDs found: `none`

Routing read:

- router question_type: `recognition`
- first family: `risk-and-recognition`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `provenance-miss`
- next fix layer: `provenance`
- loaded paths: `raw/papers/src-ckd-015.md, raw/papers/src-ckd-016.md, raw/papers/src-diabetes-001.md, raw/papers/src-hcm-194.md, raw/papers/src-hcm-205.md, system/indexes/ibd-lymphoma-boundary-memo.md, topics/ibd/risk-and-recognition-bilingual.md, topics/ibd/risk-and-recognition.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 明确炎症性肠病(IBD)与猫小细胞淋巴瘤在本数据库中的鉴别界限及诊断标准。
[info] Loaded: topics/ibd/risk-and-recognition.md
[info] Loaded: topics/ibd/risk-and-recognition-bilingual.md
[info] Search pre-loaded: src-hcm-194 (33 matches)
[info] Search pre-loaded: src-ckd-015 (32 matches)
[info] Search pre-loaded: src-ckd-016 (32 matches)
[info] Search pre-loaded: src-hcm-205 (32 matches)
[info] Search pre-loaded: src-diabetes-001 (31 matches)
[info] Hop 1/3 (~12415 tokens loaded)...
[info] Loaded: system/indexes/ibd-lymphoma-boundary-memo.md
[info] Hop 2/3 (~13534 tokens loaded)...
[info] Agent ready to synthesize
[info] Vision: no verified figures on disk yet (extract PDFs to enable)
[info] Synthesizing (8 files, ~13534 tokens)...
[meta] ROUTER_QTYPE=recognition
[meta] ROUTER_DISEASE=ibd
[meta] FIRST_FAMILY=risk-and-recognition
[meta] LOADED_PATHS=raw/papers/src-ckd-015.md,raw/papers/src-ckd-016.md,raw/papers/src-diabetes-001.md,raw/papers/src-hcm-194.md,raw/papers/src-hcm-205.md,system/indexes/ibd-lymphoma-boundary-memo.md,topics/ibd/risk-and-recognition-bilingual.md,topics/ibd/risk-and-recognition.md
```

Result excerpt:

```text
目前在这个知识库中，炎症性肠病（IBD）与小细胞淋巴瘤（small-cell lymphoma）的鉴别边界应被理解为一个复杂的多模式综合识别问题，而非依赖单一检测手段即可断定。最核心的框架是以“排除法诊断”为基础，起始点为慢性肠病（chronic enteropathy）怀疑，而非一开始即认定为特发性IBD。临床活动度指标（如FCEAI评分）用于病情负担和治疗反应的追踪，但不能明确区分IBD与淋巴瘤。影像学检查中，尤其是超声下肌层增厚（muscularis thickening）应提升淋巴瘤的疑虑，但其本身并不确诊淋巴瘤；淋巴结肿大则缺乏特异性。活检组织的取样策略极为关键，因十二指肠和回肠的病理表现可能不同，小细胞淋巴瘤常限于回肠，仅依赖十二指肠活检可能漏诊。组织学病理报告的结构化语言有助于统一诊断流程，但一处非淋巴瘤病理结果不足以排除淋巴瘤可能。组织标志物如Bcl-2虽倾向淋巴瘤，但存在重叠，无法单独诊断；粪便S100A12支持炎症存在，但无法区分IBD与淋巴瘤；代谢组学是当前最具前景的分型工具，但尚未成熟为常规诊断方法。因此，IBD与小细胞淋巴瘤的鉴别距离仍由循序渐进的排他性工作流和多层支持工具共同构成，尚无单一“边界点”可供简化界定[llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference].

核心支持证据包括：(1) 总结性大型文献强调IBD识别起点应为慢性肠病的排除性诊断，避免误将所有慢性胃肠症状直接归为特发性IBD；(2) FCEAI评分虽有利于病情活动及治疗反应监控，但未具备单独区分疾病类别能力；(3) 超声检测肌层增厚更倾向淋巴瘤风险，特别在老年猫表现明显，而淋巴结肿大缺乏特异性；(4) 十二指肠与回肠活检结果存在差异，回肠采样对于检测小细胞淋巴瘤至关重要，单一活检点结果不宜作为最终排除标准；(5) 病理报告语言规范可促进诊断解释一致性；(6) Bcl-2等组织标志物、粪便S100A12及代谢组学提供辅助支持，但均不足以替代全面组织学诊断流程[llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference].

目前尚未解决的知识空白包括：如何整合分子及微生物组学标志物使其在常规临床中实用化，具体阐明肌层增厚与淋巴瘤病理变化的定量关联程度，回肠活检的最佳采样策略及活检负面结果的评估标准，代谢组学等前沿工具实现疾病分类的标准化流程，以及淋巴瘤亚型之间的内部分层识别。这些限制使得目前诊断仍需依赖多层评估，无法仅凭某一临床、影像或分子指标精确划界[llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference][llm_inference].

## 研究者视角

猫的IBD与小细胞淋巴瘤的识别是一项复杂多因素的系统工程，涉及临床症状、活动指标、生物影像、组织活检多点采样、组织学语言规范及生物标志物多层次的集成分析。机制层面，慢性肠道炎症反应和肠道淋巴细胞恶变存在一定程度的交叉表现，导致单一标志物难以确立明确边界。活检部位的选择（特别是回肠活检）对检测小细胞淋巴瘤有决定意义。整合支持层如组织Bcl-2表达、粪便S100A12和肠道代谢组学能够从不同角度补充病变识别，尽管目前还属于前沿探索范畴。精准理解和管理该边界需强调从慢性肠道疾病排除开始，再结合影像和病理综合判断，体现出诊断流程的动态和多维特色。

## 不能说过头的地方

现有证据明确提示无单一标志物或检测能独立完成IBD与小细胞淋巴瘤的区分，临床应谨防过度简化诊断流程，避免将临床慢性肠病表现直接定性为IBD，或将影像学肌层增厚症状误认为淋巴瘤确诊。标志物虽有辅助价值，但均存在交叉表达，不能作为单独诊断依据。单点活检阴性不能保证无淋巴瘤存在，影像和标志物应纳入综合判断。研究和临床应用也必须顾及物种间外推的限制，避免简单类比人类淋巴瘤诊断标准。整体来看，所有判断都需置于排除法框架内，并结合多模态信息，才能逐步缩窄IBD与淋巴瘤间的鉴别边界，且这不构成具体诊疗建议。

## 下一步

建议未来研究继续深化多部位肠道活检的采样策略标准化，评估十二指肠与回肠病理差异及其对诊断的影响；推广并验证以Bcl-2、S100A12及代谢组学等分子标志物为基础的辅助诊断模型，探索其在常规临床中的实用性和敏感性；持续跟踪影像学肌层厚度变化与病理结果的相关性，开发量化指标以提升超声在鉴别中的参考价值；加强肠道微生物组及免疫信号通路差异的机制研究，为边界生物学理解提供数据支撑。同时应设计前瞻性临床研究，评估综合多模态识别策略对IBD与小细胞淋巴瘤早期诊断率及预后的改善效果。

---

## 研究者视角

猫IBD与小细胞淋巴瘤边界识别基于慢性肠道疾病的排除诊断框架，结合临床活动评分、超声肌层增厚影像学线索、多部位（十二指肠和回肠）活检策略及标准化病理语言解释。组织层面，Bcl-2等 lymphoma-倾向标记物与粪便S100A12等炎症标志物提供多层支持，代谢组学则是当前最有前景的未来分层工具。整体识别流程强调多模式、多层次集成，体现生物机械通路与诊断实践的交叉。

## 不能说过头的地方

目前尚无单项检验或标志物能够确诊IBD或小细胞淋巴瘤，肌层增厚是淋巴瘤风险提醒非确诊依据，单处活检阴性不排除疾病，组织标志物存在交叉表达。临床上避免将慢性肠病误诊为IBD，谨慎利用多模态诊断数据，不可因影像或单一检测而下结论，同时必需注意跨物种诊断标准的差异。所有判定均应以排除法为主，单项证据不足以替代全面诊断。

## 下一步

推动多部位活检规范及其在淋巴瘤发现率中的作用评估；深化多标志物（Bcl-2、S100A12、代谢组学）的临床实用验证；开发量化影像指标连接肌层厚度与淋巴瘤风险；扩展肠道微生物组与免疫分子机制研究；设计前瞻性研究评估多模态综合诊断对疾病早期识别与预后改善的影响。
```

## Q7. Cross-disease question

Question: `Compare CKD and HCM on the maturity of their endpoint architecture.`

Must see: 要么稳妥回答，要么诚实降级，不能假精确。
Expected question_type: `synthesis`
Expected primary family: `disease-module-maturity-ladder`
Expected strongest surface: `system/indexes/disease-module-maturity-ladder.md`

Exit code: `0`
Confidence: `low`
Source IDs found: `src-ckd-009, src-ckd-010`

Routing read:

- router question_type: `endpoints`
- first family: `endpoint-handbook`
- strongest surface hit: `no`
- clear miss: `qtype-miss`
- failure type: `qtype-miss`
- next fix layer: `qtype`
- loaded paths: `raw/papers/src-ckd-009.md, raw/papers/src-ckd-010.md, raw/papers/src-ckd-105.md, raw/papers/src-ckd-128.md, raw/papers/src-hcm-032.md, topics/ckd/endpoint-handbook.md, topics/hcm/endpoint-handbook.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1428 cards indexed
[info] Source weights: 1428 cards weighted
[info] Routing...
[info] Refined query: 系统比较慢性肾病（CKD）与肥厚型心肌病（HCM）在其终点架构成熟度方面的差异。
[warn] Not found, skipping: topics/ckd,hcm/endpoint-handbook.md
[info] Loaded: topics/ckd/endpoint-handbook.md
[info] Loaded: topics/hcm/endpoint-handbook.md
[info] Search pre-loaded: src-ckd-128 (9 matches)
[info] Search pre-loaded: src-ckd-105 (8 matches)
[info] Search pre-loaded: src-hcm-032 (8 matches)
[info] Search pre-loaded: src-ckd-009 (6 matches)
[info] Search pre-loaded: src-ckd-010 (5 matches)
[info] Hop 1/3 (~12395 tokens loaded)...
[info] Agent ready to synthesize
[info] Vision: no verified figures on disk yet (extract PDFs to enable)
[info] Synthesizing (7 files, ~12395 tokens)...
[meta] ROUTER_QTYPE=endpoints
[meta] ROUTER_DISEASE=ckd,hcm
[meta] FIRST_FAMILY=endpoint-handbook
[meta] LOADED_PATHS=raw/papers/src-ckd-009.md,raw/papers/src-ckd-010.md,raw/papers/src-ckd-105.md,raw/papers/src-ckd-128.md,raw/papers/src-hcm-032.md,topics/ckd/endpoint-handbook.md,topics/hcm/endpoint-handbook.md
```

Result excerpt:

```text
慢性肾病（CKD）和肥厚型心肌病（HCM）在终点指标架构的成熟度上存在显著差异，主要体现为CKD的终点指标架构更加系统分层且多维度，而HCM则遵循以结构确认为核心的等级体系。具体来说，CKD的终点指标体系明确划分为核心操作层（如肌酐、尿比重、蛋白尿、收缩压、磷）、辅助早期检测层（如SDMA）和背景解释管理层（如PTH、钙、FGF23、贫血和影像学），并结合多轴病理结构映射，将不同指标与肾脏不同病理损伤模式相对应，且连续追踪和趋势分析是诊断与管理的必备逻辑，用于区别诊断、病情进展及疗效评估，体现了细致的多层次和功能区分[quoted_fact: src-ckd-010][source_supported_conclusion: src-ckd-010, src-ckd-009]。相比之下，HCM的终点指标架构则是一种层级递进体系，首要以超声心动图形态学和肉眼形态测量为结构确认的主要层级，界定表型基础；其次是基于NT-proBNP的重症筛查增强层，其信号主要指示重症病变而非轻中度筛查；第三层为肌钙蛋白I等生物标志物用于反映心肌损伤负担和疾病严重度；第四层为新兴的边缘生物标志物和人工智能辅助工具，作为辅助和前沿延展手段；第五层则为右心室病变及病理分期，丰富表型和终末阶段理解，但不取代前线结构确认[llm_inference][llm_inference]。HCM架构强调核心以结构确认为首，辅以筛查和严重度解读，且注重区分不同类型的终点功能和定位，而非进行指标的简单等效比较。

终点指标的诊断与疗效评估功能在CKD中明确分层：例如肌酐和尿比重主要用于诊断和分期，蛋白尿、收缩压和磷既是预后指标也是疗效和管理目标；而SDMA作为辅助早期标志，不能独立完成筛查。HCM终点则通过结构形态确认作为诊断核心，NT-proBNP用于强化筛查，肌钙蛋白I反映损伤负担，且前沿生物标志物和AI尚处于辅助和研究层面。主要终点通常为CKD中的肌酐、蛋白尿和收缩压，HCM中的形态学指标和NT-proBNP，次要终点包括CKD中的PTH、钙、贫血和影像学，HCM中的肌钙蛋白I和AI辅助等，这反映两者架构中的功能与层级区分。两者均有基于猫特异性大量深挖文献支持，如CKD重度依赖ISFM指南及多篇组织学和临床研究（`src-ckd-004`, `src-ckd-010`, `src-ckd-013`），而HCM终点依托多篇猫种表型及生物标志物研究（`src-hcm-009`, `src-hcm-006`, `src-hcm-010`, `src-hcm-024`）[llm_inference]。

需要强调的是，CKD终点架构已非常成熟且全面，强调不同终点在机制和解读上的多维度分工，并结合连续动态评估；而HCM架构虽然系统分层，但仍处于基于形态确认为核心的稳固阶段，许多生物标志物和AI等新兴终点尚未成为常规结构确认或诊断的替代，更多作为辅助和补充，显示其体系的边界和发展空间[llm_inference][llm_inference]。此外，两者均强调切勿将所有终点等统一认定为同质的严重程度指标，且避免将辅助标志物误用作一线诊断。

尚待解决的研究空白包括：CKD中怎样更好地将不同病理结构损伤映射整合进终点选择，以及不同治疗干预如何针对各个层级终点指标产生差异化影响；HCM领域则需进一步验证新生物标志物和AI辅助终点的临床效能边界，及其与传统结构确认终点的准确度和使用场景分界[llm_inference].

---

## 研究者视角

猫CKD的终点指标架构基于大量机制与临床证据，区分了与肾间质纤维化相关的肌酐、磷、贫血指标，与肾小球-血管病变相关的蛋白尿和收缩压，强调疾病多维度病理异质性。连续多时间点的指标趋势分析是诊断与疗效评估的核心流程。生物标志物如SDMA、FGF23、甲状旁腺激素（PTH）等辅助解读矿物质代谢及病程进展。HCM终点则层级分明，首由心脏结构形态确认定义疾病表型，辅以血浆标志物对病情严重度和损伤的补充衡量，且引入AI和前沿生物标志物以支持表型深度和自动化判读，但结构确认仍是诊断和疗效评估的核心。这反映两病不同的病理机制和临床管理需求，造就了各自的终点架构成熟度差异。

## 不能说过头的地方

当前CKD终点指标体系在诊断与管理工作流中已十分成熟，但仍未解决如何将多维病理结构和终点动态整合至精准干预决策；HCM方面虽有丰富表型和标志物研究，但生物标志物和AI尚未上位为常规定义终点，且不能简单替代影像学和形态学诊断标准。两者终点皆不可视为简单的疾病严重度量化数值，应谨慎避免跨物种外推和一刀切应用。此外，本回答不构成具体的临床诊断或治疗建议。

## 下一步

针对CKD，应开展多中心、前瞻性研究验证不同终点指标组合与特定治疗反应的关联，尤其探讨基于结构病理的个体化终点优先级。HCM领域应继续开展生物标志物和AI辅助诊断工具的临床验证，明确其在早期筛查、疗效评估及疾病分期中的具体作用和局限，推动形成更协调和分层的终点评估体系。同时，两病均需引入更细致的临床工作流示范，将多层级终点指标合理嵌入诊疗路径，促进证据转化为临床实践。
```

## Q8. Regulatory question

Question: `What is the current regulatory path surface for feline CKD programs across China, FDA, and VMD?`

Must see: 至少承认 jurisdiction split。
Expected question_type: `regulatory`
Expected primary family: `regulatory-brief`
Expected strongest surface: `topics/ckd/regulatory-brief.md`

Exit code: `0`
Confidence: `high`
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
[info] Refined query: 研究中国、美国FDA及英国VMD监管机构对猫慢性肾病（CKD）药物开发及审批路径的现状与差异
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
当前针对猫慢性肾脏病（CKD）产品的监管路径，中国、美国FDA和英国VMD各自形成了较为系统但结构不同的监管框架，且均未形成针对猫CKD适应症的特异性审批标准。中国应被视为一条涵盖兽药注册、批准文号管理与进口审批的多层次正式兽药监管路径；FDA路径则明显分叉为需要提供实质有效性证据的完全批准和基于合理疗效预期的有条件批准两条主线，且有条件批准需评估是否符合严重性、未满足医疗需求及研究难度等特定条件；英国VMD侧重于多种上市许可途径的选择及其对应卷宗规范，需严格满足附录和科学指南要求，不能简单视为单一路径。此外，欧盟EMA对于符合有限市场条件的产品提供了较轻数据要求的路径选择，但该有限市场资格需及早验证并非默认适用。整体而言，这些监管路径均未支持所谓“人药转宠物药”的简化跳过路径，且缺乏专门针对猫CKD的疗效终点或证据包具体指南[quoted_fact: src-reg-001][quoted_fact: src-reg-002][quoted_fact: src-reg-003][quoted_fact: src-reg-004][quoted_fact: src-reg-005][quoted_fact: src-reg-006][quoted_fact: src-reg-007][quoted_fact: src-reg-008][quoted_fact: src-reg-009][source_supported_conclusion: src-reg-001][source_supported_conclusion: src-reg-002][source_supported_conclusion: src-reg-003][source_supported_conclusion: src-reg-004][source_supported_conclusion: src-reg-005][source_supported_conclusion: src-reg-006][source_supported_conclusion: src-reg-007][source_supported_conclusion: src-reg-008].

核心证据包括：  
1. 中国依据《兽药注册办法》建立了新兽药及进口兽药的分步注册体系，生产前还需获得产品批准文号，进口药品还涉及专门的通关及资料要求，说明其监管路径明确且分层管理[quoted_fact: src-reg-001][quoted_fact: src-reg-002][quoted_fact: src-reg-003]。  
2. FDA规定完全批准要求充分的有效性证据，有条件批准允许基于合理期望获批但需符合严重性及未满足需求的条件，且为期有限，Cats被归类为主要物种同时有针对伴侣动物的活性对照设计指南，强调临床试验设计在路径规划中的重要性[quoted_fact: src-reg-004][quoted_fact: src-reg-005][quoted_fact: src-reg-006]。  
3. EMA为了有限市场产品提供符合第23条的简化有效性和安全性数据标准，但必须及早确认有限市场资格，否则数据期望会较高[quoted_fact: src-reg-007]。  
4. 英国VMD强调多条上市许可路线与严格的卷宗结构要求，视路径规划为路线选择与文档管理问题，建议初期集中在大不列颠地区的方案较为简便[quoted_fact: src-reg-008][quoted_fact: src-reg-009]。

尚未解决的空白主要包括：  
- 缺乏针对猫CKD适应症的具体疗效终点及试验设计官方指导文件，尤其三大司法辖区均无明确针对肾脏病的伴侣动物疗效指南。  
- 中国进口兽药的路径细节和内外国产品路径的决策树仍待完善。  
- “人药转宠物药”的监管可行性及捷径尚无官方支撑，仍需谨慎对待。  
- 路径与产品原型、证据打包的具体匹配策略尚未达到决策级别，需补充更细致数据和指导。  
- EMA和VMD尚无针对CKD适应症的试验方案细化资料。

---

## 研究者视角

从学术机制与监管实践结合的角度看，当前宠物猫CKD研发面临多司法辖区复杂且不统一的监管环境。中国法规定义明确，兼顾国产与进口兽药差异，要求完成临床试验且获得注册及生产批准文号，强调程序的正规完整；美国FDA基于动物药法规的逻辑，设立了完全批准与条件批准两条审批路径，后者适用于研究难度大、临床未满足医疗需求的情况，活性对照试验设计指南体现了对伴侣动物临床试验方法论的关注；EMA则通过欧盟第23条对特别限定市场提供简化路径潜力，提示研究者早期判断产品市场定位对监管路径策略至关重要；英国VMD的多路径选择反映了其监管的灵活性和对科学指南的一体化要求。生物标志物和终点尚无充分书面指南支持，为临床证据收集带来挑战，形成了监管路径既具结构性又存在执行细节不确定的现状[quoted_fact: src-reg-001][quoted_fact: src-reg-004][quoted_fact: src-reg-007][quoted_fact: src-reg-008].

## 不能说过头的地方

目前公开的官方监管文件均仅为框架级规定，缺少针对猫CKD适应症的细节疗效和安全性终点指导，且覆盖的证据包要求偏宏观，因而不宜过度从人药经验推断宠物药路径。不同司法辖区的路径结构复杂，存在分支与多路径交互，猫作为主要物种虽可适用部分条件批准，但并无自动权利保证。中国进口药物的管理依然独立于注册流程，简单“人药转宠物药”说法今无监管支持。上述限制意味着当前信息不足以指导具体产品申报策略，且任何药物使用建议必须基于专业兽医判断，不能以此页面内容替代临床诊断建议[quoted_fact: src-reg-005][quoted_fact: src-reg-006][quoted_fact: src-reg-009].

## 下一步

为提升猫CKD监管路径的决策效率，应重点开展以下工作：  
1. 搜集并完善中国兽药注册申报材料及技术要求文件，细化国产和进口路径的决策树结构。  
2. 深入挖掘FDA、EMA及VMD公开或内部指南，特别是针对伴侣动物CKD的疗效终点和临床试验设计标准。  
3. 评估目标产品在EMA有限市场路径和美国有条件批准路径下的资格和证据准备要求，通过早期对比分析确定最优发展策略。  
4. 构建细化的路径-产品原型匹配系统，涵盖多种CKD干预模式（如蛋白尿指导保护、磷控制等），提升内部路径清晰度和方案可操作性。  
5. 保持对“人药转宠物药”策略的监管动态监控，谨慎解读权威更新，避免策略过早落实。  

通过这些步骤，可逐步从路径级框架过渡到具体产品临床试验设计和申报策略制订，促进猫CKD药物开发和监管的科学化、系统化推进。
```
