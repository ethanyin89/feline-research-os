---
id: system-ask-the-vault-acceptance-report-20260613
type: health-check
topic: operating-system
question_type: acceptance
language: zh
last_compiled_at: 2026-06-13
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: pass
---

# Ask The Vault Acceptance Report, 2026-06-13

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
| Q1 | CKD mechanism spine | 0 | mechanism | mechanism-overview | yes | no | no-clear-failure | none | 10 | medium | pass-leaning |
| Q2 | CKD endpoint selection | 0 | endpoints | endpoint-handbook | yes | no | no-clear-failure | none | 2 | medium | pass-leaning |
| Q3 | CKD claim verification | 0 | claim_verification | verify-a-claim | yes | no | no-clear-failure | none | 3 | medium | pass-leaning |
| Q4 | FIP diagnostic workup | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 9 | high | pass-leaning |
| Q5 | HCM recognition versus endpoint | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 9 | high | pass-leaning |
| Q6 | IBD versus lymphoma boundary | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 9 | high | pass-leaning |
| Q7 | Cross-disease question | 0 | synthesis | disease-module-maturity-ladder | yes | no | answer-compression-miss | answer-compression | 3 | low | pass-leaning |
| Q8 | Regulatory question | 0 | regulatory | regulatory-brief | yes | no | no-clear-failure | none | 7 | medium | pass-leaning |

Acceptance summary: 7/8 automated pass-leaning answers; 0 execution failures; 0 provenance misses; 0 route misses. Status: pass.

## Detailed Runs

## Q1. CKD mechanism spine

Question: `CKD 的核心机制主线是什么？`

Must see: 至少落到 CKD mechanism 强答案面，且至少 2 个真实 source ids。
Expected question_type: `mechanism`
Expected primary family: `mechanism-overview`
Expected strongest surface: `topics/ckd/mechanism-overview.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-ckd-001, src-ckd-002, src-ckd-004, src-ckd-006, src-ckd-009, src-ckd-010, src-ckd-011, src-ckd-015, src-ckd-016, src-ckd-021`

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
[info] Source index: 1418 cards indexed
[info] Source weights: 1418 cards weighted
[info] Routing...
[info] Loaded: topics/ckd/mechanism-overview.md
[info] Hop 1/3 (~4856 tokens loaded)...
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
[info] Synthesizing (11 files, ~23320 tokens)...
[meta] ROUTER_QTYPE=mechanism
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=mechanism-overview
[meta] LOADED_PATHS=raw/papers/src-ckd-001.md,raw/papers/src-ckd-002.md,raw/papers/src-ckd-004.md,raw/papers/src-ckd-006.md,raw/papers/src-ckd-009.md,raw/papers/src-ckd-010.md,raw/papers/src-ckd-011.md,raw/papers/src-ckd-015.md,raw/papers/src-ckd-016.md,raw/papers/src-ckd-021.md,topics/ckd/mechanism-overview.md
```

Result excerpt:

```text
猫慢性肾脏病（CKD）的核心机制主线是肾小管间质纤维化（tubulointerstitial fibrosis），这是一种最常见且与肾功能衰竭最密切相关的病理病变。大多数发病猫为老年猫，CKD以肾小管间质纤维化为病理标志，起始原因多不明确，属于多因素引起的不可逆性进行性损伤。多种辅助机制如蛋白尿、高磷血症、血压升高等表现与纤维化病变密切相关，推动病情进展。此外，矿物质代谢紊乱（包括磷、钙、甲状旁腺素及FGF23的调控异常）、促纤维化因子（如TGF-β），以及肾素-血管紧张素-醛固酮系统（RAAS）活化造成的炎症、氧化应激和血管损伤等也参与疾病发展。肠道来源的尿毒素堆积、猫类副黏病毒感染（FeMV）及遗传因素（如PKD1基因突变）则为新兴的发病机制分支。目前证据主要强调纤维化的终末病理地位，将其确立为机制研究和临床识别的核心基石。

关键证据如下：

- 多项高质量综述和组织病理学研究显示，肾小管间质纤维化为猫CKD最稳定、最频繁的病变，且与肾功能(如肌酐、尿比重降低)密切相关，是重要的病理学机制骨架[quoted_fact: src-ckd-001, src-ckd-011, src-ckd-010, src-ckd-016]。
- 病理组织学研究进一步揭示，纤维化与高血肌酐、高磷血症和贫血等临床表现具有最好的一致性，蛋白尿和高收缩压更侧重于反映肾小球和血管病变[quoted_fact: src-ckd-010]。
- 绝大多数受影响猫龄大于12岁，CKD为老龄猫疾病，起始因素可能涉及衰老、肾缺血和低氧，但尚未确定主导病因[quoted_fact: src-ckd-016]。
- 磷代谢紊乱是促病机制重要通路，伴随甲状旁腺素（PTH）和成纤维细胞生长因子23（FGF23）调节，FGF23在早期升高比高磷血症更早见，强调CKD相关矿物骨代谢病（CKD-MBD）为广义矿物代谢紊乱[quoted_fact: src-ckd-015, src-ckd-006]。
- 促纤维化信号传导主要有转化生长因子β（TGF-β）介导，体外实验显示猫肾皮质成纤维细胞对其具有明显转录增殖反应，具备成为治疗靶点潜力[quoted_fact: src-ckd-011]。
- RAAS系统特别是醛固酮及矿物皮质激素受体（MR）激活被认为加重肾脏损伤及纤维化，动物实验及人类研究证据丰富，猫自然发病的直接证据有限，MR拮抗剂为潜在继发治疗方向[quoted_fact: src-ckd-021]。
- 肠道-肾轴的尿毒素（吲哚硫酸盐、对甲酚硫酸盐、三甲胺氧化物）在猫CKD中积累，提示肠道菌群失调参与病理机制，虽尚无明确干预证据[llm_inference]。
- 猫副黏病毒（FeMV）感染与淋巴浆细胞性肾间质炎和Caspase-3介导的肾小管细胞凋亡显著相关，是CKD的潜在感染性病因分支[llm_inference]。
- 遗传性多囊肾病（ADPKD）由PKD1基因突变引起，虽为少数病例但提供具体遗传机制示范[llm_inference]。

我们尚不清楚的方面：

- 多数CKD起始因素目前仍为推测，缺少统一确定的主导起始机制，尤其是老龄化、缺血、免疫及病毒感染等的具体病理贡献仍需进一步证实[quoted_fact: src-ckd-016]。
- TGF-β等促纤维化信号的体内作用机制、临床治疗效果及安全性尚无充分的猫特异性研究证明[quoted_fact: src-ckd-011]。
- 肠道菌群相关尿毒素的具体代谢路径、干预潜力和临床应用仍处于初步发现阶段[llm_inference]。
- 现有血压和蛋白尿介导机制与纤维化等结构损伤的整合内在机制尚未完全阐明，临床监测和治疗的优化方案仍待研究[quoted_fact: src-ckd-009, src-ckd-010]。
- FeMV感染的流行病学及其与CKD的因果关系，是否普遍存在或仅为部分猫群特异性，还需进一步流行病及机制研究[llm_inference]。

---

## 研究者视角

猫CKD机制研究的核心是透过形态学和临床指标确认肾小管间质纤维化为泛化的病理终末通路，连接老龄化及多种病因的损伤累积。纤维化作为关键病理特征，关联肌酐升高、磷代谢异常和贫血，成为病情分期和干预靶点。蛋白尿和血压变化提示肾小球及血管性损伤，支持临床端点的多维解释框架。生物标志物如FGF23的升高揭示矿物骨代谢紊乱的早期亚临床阶段。TGF-β信号通路和RAAS（特别是醛固酮/MR）提供了分子层面解释纤维化进展的路径。肠道菌群功能失调引发的尿毒素蓄积预示着全身代谢和免疫环境的复杂交互。FeMV感染和PKD1基因突变则代表病因学领域的前沿，拓宽了从疾病发病基础到可能精准防治的研究维度。总体而言，支撑机制主线的是病理学的纤维化证据，其它机制被纳入辅助或次级机制分支，以呈现多元致病网络。

## 不能说过头的地方

尽管纤维化是肯定的病理中心，但目前尚无明确猫特异性主病因或广泛公认的启动机制。各因子作用的优先级和临床干预效果还未完全明晰，尤其如TGF-β抑制和MR拮抗剂在猫CkD中的安全性和功效未达临床验证标准。肠道尿毒素和FeMV的直接致病机制如何融入整体发病图谱仍有待完成大样本、多中心研究。血压与蛋白尿机制联动尚未成为治疗设计核心，需避免简单将这些指标机械解读为病程进展线性变量。本文信息不构成专业兽医诊疗建议，临床应用请结合具体病例和专业指导。

## 下一步

- 开展针对纤维化机制中关键分子（如TGF-β及其受体）的猫体内干预试验，验证其治疗潜力及安全性。
- 加强老龄猫群中CKD早期病理变化的纵向研究，明确起始因素与进展因子分界。
- 深入研究矿物代谢扰动路径中FGF23、PTH及钙磷平衡的分子机制及其调控靶点。
- 进一步利用代谢组学和微生物组学方法探索肠道-肾轴尿毒素产生与清除的病理学角色。
- 扩大FeMV流行病学调查，结合组织学和分子病理学，明确其在CKD中的具体致病机制和流行特征。
- 推动临床多中心数据库建设，整合血压、蛋白尿及结构性病理标志物，优化CKD进展和治疗反应的多维预测模型。

以上内容基于丰富高质量综述和关键原始研究综合，确保科学性和专业性。[quoted_fact: src-ckd-001, src-ckd-002, src-ckd-004, src-ckd-006, src-ckd-009, src-ckd-010, src-ckd-011, src-ckd-015, src-ckd-016, src-ckd-021]

---

## 研究者视角

猫慢性肾病的核心机制围绕肾小管间质纤维化这一终末病理通路展开。纤维化带来肾结构功能衰退，是各种起始损伤的共同汇聚点。纤维化进展与蛋白尿、血磷升高及贫血紧密相关，提示了多维临床指标的结构性病理反映，同时这也揭示了老龄猫自然发病的进展轨迹。矿物代谢异常（CKD-MBD）不仅限于高磷，还包括钙代谢异常、甲状旁腺素及内分泌因子FGF23的调控失衡。转化生长因子β（TGF-β）和醛固酮/矿物皮质激素受体等信号传导轴成为识别和干预的焦点。肠道菌群相关尿毒素和猫副黏病毒感染拓宽本病的机制网络，提示环境与遗传因素共同作用。总体机制框架强调纤维化作为稳定且关键的病理中心，辅助机制则支持多因子、网络化的病理进展理解。

## 不能说过头的地方

目前尚无确定单一主导起始因子，所有涉及机制均未达到完全可靠的治疗干预指标。TGF-β及MR拮抗剂等介导路径虽有一定体外和动物模型证据，但缺乏充分的猫临床试验数据。尿毒素和FeMV等新兴机制仍属探索阶段，未形成广泛共识。血压和蛋白尿等指标应谨慎解读，避免过度简化。本文内容非专业兽医诊断治疗建议，临床应用应咨询专业人士。

## 下一步

- 着重进行纤维化相关分子机制的猫体内验证研究，尤其围绕TGF-β与RAAS信号通路。
- 结合分子标志物探索早期CKD检测手段，提升疾病早期识别能力。
- 推进矿物代谢调控网络，特别是FGF23和PTH相互作用机制的深入研究。
- 利用代谢组和微生物组联合技术，研究肠道菌群和尿毒素对CKD的影响机制與干预潜力。
- 加大FeMV相关CKD病理机制与流行病学调查力度， clarifying viral pathogenic role in feline CKD.
- 建立多中心纵向队列，整合临床、病理及分子数据，优化CKD综合管理策略。
```

## Q2. CKD endpoint selection

Question: `What endpoints are most usable for feline CKD efficacy evaluation, and why?`

Must see: 有 endpoint shortlist 和 why，不只是罗列。
Expected question_type: `endpoints`
Expected primary family: `endpoint-handbook`
Expected strongest surface: `topics/ckd/endpoint-handbook.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-ckd-004, src-ckd-010`

Routing read:

- router question_type: `endpoints`
- first family: `endpoint-handbook`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/papers/src-ckd-004.md, raw/papers/src-ckd-010.md, topics/ckd/endpoint-handbook.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1418 cards indexed
[info] Source weights: 1418 cards weighted
[info] Routing...
[info] Loaded: topics/ckd/endpoint-handbook.md
[info] Hop 1/3 (~2785 tokens loaded)...
[info] Loaded source: src-ckd-004
[info] Loaded source: src-ckd-010
[info] Hop 2/3 (~7253 tokens loaded)...
[info] Agent ready to synthesize
[info] Vision: no verified figures on disk yet (extract PDFs to enable)
[info] Synthesizing (3 files, ~7253 tokens)...
[meta] ROUTER_QTYPE=endpoints
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=endpoint-handbook
[meta] LOADED_PATHS=raw/papers/src-ckd-004.md,raw/papers/src-ckd-010.md,topics/ckd/endpoint-handbook.md
```

Result excerpt:

```text
The most usable endpoints for efficacy evaluation in feline chronic kidney disease (CKD) include serum creatinine (with serial trend monitoring), urine specific gravity (USG), urine protein-to-creatinine ratio (UPCR), systolic blood pressure (SBP), and serum phosphorus. These form the core operational tier of endpoints because they robustly bridge diagnosis, staging, longitudinal monitoring, and prognosis in feline CKD [source_supported_conclusion: src-ckd-004, src-ckd-010]. Creatinine elevation and its trend over time provide a primary measure of reduced renal function, while USG aids diagnostic confirmation alongside creatinine. UPCR is critical for prognosis, substaging, and treatment targeting due to its association with interstitial fibrosis and glomerular hypertrophy. SBP informs risk management and progression context because persistent hypertension promotes glomerulosclerosis and vascular injury. Phosphorus is essential for monitoring progression and treatment effects related to mineral burden and CKD-mineral bone disorder (CKD-MBD), with elevated phosphorus correlating with increased mortality and fibrosis severity. Early-detection markers like SDMA serve as adjunctive tools but are not recommended as standalone efficacy endpoints [quoted_fact: src-ckd-004].

### Endpoint Selection Considerations

- **Diagnosis vs Efficacy:** Creatinine, USG, and creatinine trend primarily serve both diagnostic and longitudinal monitoring functions, with serial measurements necessary for confirming disease presence and tracking progression [quoted_fact: src-ckd-004]. For efficacy evaluation, endpoints must reflect treatment impact on disease progression; therefore, phosphorus, UPCR, SBP, and creatinine trends provide actionable targets linking to pathological burden and prognosis [source_supported_conclusion: src-ckd-010].
  
- **Primary vs Secondary Endpoints:** The core operational endpoints—creatinine, USG, UPCR, SBP, and phosphorus—constitute primary efficacy evaluation endpoints due to their established clinical relevance and structural lesion mapping [quoted_fact: src-ckd-004]. Secondary/contextual endpoints like PTH, calcium, FGF23, anaemia, and imaging provide additional mechanistic insight and disease context but are not first-line endpoints for routine efficacy monitoring [llm_inference].
  
- **Feline Species Evidence:** Evidence supporting these endpoints derives predominantly from feline-specific studies and consensus guidelines. The ISFM guideline for feline CKD diagnosis and management explicitly defines creatinine, USG, UPCR, and SBP as core clinical decision variables validated in cats [quoted_fact: src-ckd-004]. Histomorphometry studies link these endpoint levels directly to feline renal lesions, distinguishing pathways associated with fibrosis versus vascular injury in naturally occurring feline CKD [quoted_fact: src-ckd-010].
  
- **Literature Support:** The ISFM consensus guideline (high-weight source, src-ckd-004) anchors the diagnostic and monitoring framework, endorsing serial creatinine and USG for diagnosis, and emphasizing UPCR, SBP, and phosphorus for prognosis and treatment monitoring. The histomorphometry study (medium-weight, src-ckd-010) provides pathological correlation for endpoint selection by linking specific markers to structural damage, supporting a multi-axis endpoint interpretation. Biomarker review and CKD-MBD-focused papers further refine the roles of adjunct and context markers like SDMA and PTH [quoted_fact: src-ckd-004, src-ckd-010].

### What We Don't Know Yet

There remain gaps regarding the optimal weighting or ranking of endpoints across diverse feline CKD phenotypes and intervention classes. How endpoints should be integrated or prioritized when multiple abnormalities coexist (e.g., hypertension with proteinuria and hyperphosphatemia) is unclear. The specific responsiveness and sensitivity of certain secondary markers (PTH, FGF23, anaemia) for efficacy evaluation await further validation. Also, SDMA's definitive role as an efficacy endpoint requires more prospective evidence despite its promising early-detection profile. The currently available histomorphometry evidence reflects late-stage disease and may not fully extrapolate to early or treatment-responder stages. Thus, a trial- or product-specific endpoint prioritization framework remains to be conclusively established [source_supported_conclusion: src-ckd-004, src-ckd-010].

---

## 研究者视角

Feline CKD endpoints correlate with distinct pathological mechanisms. Serum creatinine, phosphorus, and anaemia align tightly with interstitial fibrosis severity, representing core fibrosis-linked burden markers. Proteinuria links to both fibrosis and glomerular hypertrophy, bridging structural damage and prognosis. Systolic blood pressure correlates with glomerulosclerosis and vascular lesions, reflecting a glomerulo-vascular injury axis. Biomarkers such as SDMA provide early detection sensitivity less influenced by muscle mass but currently serve adjunctive roles. Secondary endpoints including PTH and FGF23 elucidate CKD-MBD impact but are less established for routine efficacy assessment. Multi-axis interpretation recognizes that no single marker encompasses CKD progression fully; thus, serial surveillance combining these endpoints is essential for nuanced assessment in clinical and research contexts [source_supported_conclusion: src-ckd-010, src-ckd-004].

## 不能说过头的地方

The evidence supports distinguishing operational, support, and context tiers of endpoints to avoid inappropriate interchangeability. SDMA is an adjunct not a standalone screening or efficacy marker. Phosphorus should never be interpreted without PTH status due to compensatory dynamics. Imaging remains an important workup context but does not substitute efficacy endpoints. Histomorphometry results stem from late-stage necropsy specimens, limiting direct extrapolation to early-stage or intervention efficacy evaluations. This synthesis does n
```

## Q3. CKD claim verification

Question: `Verify whether SDMA should already be treated as a core early-detection anchor in this vault.`

Must see: 必须是 verification 风格，同时呈现支持与保留条件。
Expected question_type: `claim_verification`
Expected primary family: `verify-a-claim`
Expected strongest surface: `system/indexes/verify-a-claim.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-ckd-002, src-ckd-004, src-ckd-010`

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
[info] Source index: 1418 cards indexed
[info] Source weights: 1418 cards weighted
[info] Routing...
[info] Loaded: system/indexes/verify-a-claim.md
[info] Loaded: topics/ckd/current-state-dashboard.md
[info] Loaded: topics/ckd/endpoint-handbook.md
[info] Hop 1/3 (~7664 tokens loaded)...
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
[info] Synthesizing (13 files, ~26643 tokens)...
[meta] ROUTER_QTYPE=claim_verification
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=verify-a-claim
[meta] LOADED_PATHS=raw/papers/src-ckd-001.md,raw/papers/src-ckd-002.md,raw/papers/src-ckd-003.md,raw/papers/src-ckd-004.md,raw/papers/src-ckd-005.md,raw/papers/src-ckd-006.md,raw/papers/src-ckd-007.md,raw/papers/src-ckd-008.md,raw/papers/src-ckd-009.md,raw/papers/src-ckd-010.md,system/indexes/verify-a-claim.md,topics/ckd/current-state-dashboard.md,topics/ckd/endpoint-handbook.md
```

Result excerpt:

```text
SDMA is currently positioned as a supportive early-detection biomarker in feline CKD but should not yet be treated as a core standalone early-detection anchor in clinical workflows. The consensus guidelines and synthesized evidence emphasize SDMA’s greater sensitivity than creatinine for detecting early CKD and its relative independence from muscle mass; however, SDMA cannot replace core diagnostic endpoints such as creatinine, urine specific gravity (USG), and proteinuria. It is recommended as an adjunct test, useful for supporting early detection and staging but not as a single screening replacement. Thus, SDMA belongs in an adjunctive support tier in the endpoint hierarchy rather than the operational diagnostic core.

Key evidence:

- The ISFM Consensus Guidelines (2016) explicitly state that SDMA appears more sensitive than creatinine for early CKD detection and less affected by muscle mass but cannot currently be recommended as a single screening test for CKD [quoted_fact: src-ckd-004].

- The endpoint handbook classifies SDMA as an adjunct early-detection aid, not as a standalone screening replacement, positioning it separately from the core operational endpoints (creatinine, USG, UPCR, systolic blood pressure, phosphorus) [source_supported_conclusion: src-ckd-004].

- The 2014 diagnostic review highlights the distinction between routine clinical diagnosis endpoints and ideal but impractical early detection measures, reinforcing that early CKD detection is harder and that biomarkers like SDMA should be adjunctive rather than primary [source_supported_conclusion: src-ckd-002].

- A biomarker review and other sources confirm SDMA’s promise but emphasize lack of sufficient evidence for it to serve as a single diagnostic or screening marker [llm_inference].

- GFR remains the conceptual gold standard for early renal dysfunction but is impractical routinely; SDMA is useful but fulfills a different, supplementary role [source_supported_conclusion: src-ckd-002, src-ckd-004].

What we don't know yet:

- Precise operational algorithms integrating SDMA with core diagnostic tests for early detection remain under development.

- The clinical impact of SDMA-guided interventions on outcomes is not fully established in prospective studies.

- The limits of SDMA sensitivity and specificity in different CKD stages and comorbid contexts in cats require further validation.

- How SDMA quantification can best support risk stratification or progression monitoring beyond adjunctive detection is still being researched.

## 研究者视角

From a research perspective, feline CKD diagnosis and early recognition rely on a tiered endpoint architecture. Core operational endpoints include serum creatinine, urine specific gravity, proteinuria (UPCR), systolic blood pressure, and serum phosphorus, which are directly linked to disease staging, prognosis, and management. SDMA emerges as a sensitive early-detection biomarker, less confounded by muscle mass than creatinine, but functions as an adjunctive marker rather than a standalone diagnostic anchor. Mechanistically, SDMA reflects reduced glomerular filtration but does not replace structural or functional endpoint layers. This reflects a cautious integration of novel biomarkers, balancing clinical practicality, and rigorous validation. The field situates SDMA beneath the gold standard GFR conceptually but values it for supplementing routine surveillance, supporting earlier suspicion especially during serial monitoring. This layered biomarker grouping fits within a broader framework associating different markers with distinct renal lesion patterns (e.g., fibrosis-linked vs glomerulo-vascular injury) and clinical implications [source_supported_conclusion: src-ckd-004, src-ckd-010].

## 不能说过头的地方

Although SDMA shows promise as an early-detection aid, it currently should not be treated as a core standalone screening test, as this overstates the available evidence. The operational diagnostic core remains creatinine, USG, UPCR, and blood pressure, with SDMA as adjunct support. Recommendations based on current evidence caution against using SDMA in isolation without corroborative clinical and laboratory context. This synthesis does not constitute professional veterinary advice and should not replace clinical judgment or established diagnostic protocols. Applying SDMA as a primary diagnostic anchor ahead of further validation would exceed current guideline support.

## 下一步

1. Conduct prospective studies validating SDMA’s sensitivity, specificity, and influence on early diagnosis workflows and clinical outcomes in feline CKD.

2. Develop and test clinical algorithms that integrate SDMA with core endpoints (creatinine, USG, UPCR) for serial surveillance to improve early recognition.

3. Quantify the additive predictive value of SDMA across CKD stages and in common comorbidities (hypertension, proteinuria).

4. Refine endpoint and treatment outcome frameworks to incorporate biomarker dynamics including SDMA trends over time.

5. Continue building species-specific evidence to distinguish feline SDMA utility from data extrapolated from other species.

In summary, SDMA is a valuable adjunct early-detection biomarker in feline CKD with growing evidence support; however, it should currently be treated as a support marker rather than a core early-detection anchor in clinical practice [source_supported_conclusion: src-ckd-004, src-ckd-002].

# Short Reference for key source cards:  
- ISFM Guideline, 2016 [source_supported_conclusion: src-ckd-004]  
- Diagnostic review, 2014 [source_supported_conclusion: src-ckd-002]  
- Biomarker review [src-ckd-024]  
- Histopathology correlations [source_supported_conclusion: src-ckd-010]
```

## Q4. FIP diagnostic workup

Question: `What is the current diagnostic workup architecture for feline FIP?`

Must see: 不能把 diagnosis 简化成单一 assay。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/fip/risk-and-recognition.md`

Exit code: `0`
Confidence: `high`
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
[info] Source index: 1418 cards indexed
[info] Source weights: 1418 cards weighted
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
The current diagnostic workup architecture for feline infectious peritonitis (FIP) is a structured, multi-layered process that begins with recognizing risk context but relies primarily on clinicopathology and disease form to build suspicion, followed by laboratory and molecular support tailored to the disease form, and specialized neurologic or ocular workup branches when relevant. Risk factors such as young age, specific breeds, male sex, and multi-cat endemic coronavirus exposure serve to raise suspicion but do not diagnose FIP. Clinicopathology, especially distinguishing effusive ("wet") and non-effusive ("dry") forms, remains the operational core for suspicion-building. After suspicion is established, bounded molecular diagnostics—including mutation analyses and CSF real-time RT-PCR for neurologic cases—provide supportive evidence, but no single test, including molecular assays, is definitive alone. Neurologic or ocular signs prompt a diagnostic branch shift, where CSF analysis gains importance but remains a confirmatory rather than primary diagnostic tool. Treatment response is considered only downstream and does not alter initial recognition.[source_supported_conclusion: src-fip-003, src-fip-005, src-fip-006, src-fip-008, src-fip-012, src-fip-015, src-fip-023]

Key evidence supporting this architecture includes:

- **Risk context raises suspicion but is nondiagnostic**: Young age, breeds such as British Shorthair, Devon Rex, Abyssinian, male sex, and exposure in multi-cat environments with endemic feline enteric coronavirus increase pretest probability but cannot confirm disease [source_supported_conclusion: src-fip-005, src-fip-008, src-fip-012, src-fip-020].

- **Clinicopathology and disease form lead suspicion-building**: Clinical and laboratory patterns from retrospective case series (42 cases in Sydney and 51 cases in Taiwan) provide structured staging and differentiation between effusive and non-effusive presentations, shaping the early diagnostic approach [source_supported_conclusion: src-fip-006, src-fip-015].

- **Effusive form linked to immune phenomena**: Immunopathologic understanding of the effusive form adds biological context, preventing oversimplification of diagnosis based solely on physical effusions [source_supported_conclusion: src-fip-007].

- **Molecular and specialized tests provide bounded support**: Mutation detection and CSF RT-PCR tests, particularly in neurologic or ocular FIP, have high specificity but limited general sensitivity, and thus strengthen but do not lead diagnosis [source_supported_conclusion: src-fip-003, src-fip-023].

- **Neurologic/ocular branch shift**: Presence of neurologic or ocular signs changes the diagnostic pathway, making CSF analysis central for these cases, but a negative CSF RT-PCR does not exclude FIP [source_supported_conclusion: src-fip-015, src-fip-023].

What remains uncertain or less defined includes the exact weighting of risk factors across different geographic and population contexts, optimal staging criteria standardization, the detailed ranking of laboratory variables in clinicopathologic suspicion, and the full integration of newer molecular tests without overreliance on single assays. Further, the boundaries limiting when and how to apply CSF RT-PCR and mutation testing require more precise clinical workflow confirmation. Treatment response remains a downstream factor and lacks clarity on how it could inform reclassification of initial suspicion.[source_supported_conclusion: src-fip-005, src-fip-006, src-fip-015, src-fip-023]

## 研究者视角

From a research perspective, FIP diagnosis is a complex, multi-step composite process integrating epidemiologic risk, clinicopathological patterns, and molecular diagnostics. The pathological characteristics encompass effusive and non-effusive forms with distinct immunologic underpinnings, as effusive FIP involves immune complex and inflammatory phenomena documented since historical immunopathology studies. Biomarker groups include routine laboratory abnormalities (e.g., altered protein levels, effusions), mutation analysis of viral RNA, and detection of viral RNA in cerebrospinal fluid for neurologic manifestations. The research context distinguishes exposure to feline enteric coronavirus (non-pathogenic background) from emergence of the mutated FIP virus responsible for clinical disease. The diagnostic workflow architecture therefore respects this layered biology and epidemiology, applying non-specific clinical findings as the primary suspicion layer, then complementing with specialized molecular tools post-suspicion. The recognition framework prevents collapsing diagnosis into single-test decisions, emphasizing staged, form-specific, and context-aware approaches consistent with veterinary academic findings and diagnostic challenges.

## 不能说过头的地方

The evidence does not support diagnosing FIP based solely on breed, age, sex, household, or referral population factors; these remain risk enhancers, not diagnostic criteria. Similarly, effusion presence, while highly suspicious, does not definitively prove FIP. Cerebrospinal fluid RT-PCR has high specificity but limited sensitivity and should not be used as a universal screening test; a negative result does not exclude FIP, especially outside neurologic or ocular cases. Treatment response, although clinically useful, should not be used to retrospectively alter the initial diagnostic suspicion tier. This synthesis strictly separates recognition layers and caution against overreliance on any single molecular or laboratory assay in solitude. These points underline that current understanding is based on retrospective case series, epidemiologic associations, and diagnostic performance metrics primarily from referral populations, limiting broad universal extrapolation and underscoring that this summary is not a substitute for clinical veterinary judgment.

## 下一步

Next steps involve detailed extraction and verification of clinicopathology s
```

## Q5. HCM recognition versus endpoint

Question: `For feline HCM, what should be separated between recognition and endpoints?`

Must see: 承认 recognition 和 endpoint 是两层。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/hcm/risk-and-recognition.md`

Exit code: `0`
Confidence: `high`
Source IDs found: `src-hcm-001, src-hcm-008, src-hcm-009, src-hcm-010, src-hcm-012, src-hcm-013, src-hcm-021, src-hcm-023, src-hcm-024`

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
[info] Source index: 1418 cards indexed
[info] Source weights: 1418 cards weighted
[info] Routing...
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
For feline hypertrophic cardiomyopathy (HCM), recognition and endpoints must be clearly separated in a hierarchical framework where structural phenotype confirmation—primarily through echocardiographic assessment and gross morphometry—forms the foundation of both recognition and endpoint determination, while biomarkers, artificial intelligence (AI), and genotype interpretation serve only as bounded augmentation or modifiers rather than replacements. Recognition should start from suspicion based on broader cardiomyopathy awareness, proceed through structure-first confirmation, and then be augmented by biomarkers (e.g., NT-proBNP for severe disease flagging), AI-based screening support, and genotype/age context. Endpoints similarly follow a hierarchy: structural confirmation leads, supported by severe-disease screening markers (like NT-proBNP), injury/burden indicators (troponin I), frontier biomarkers/AI augmentation, and finally deeper phenotype and end-stage pathology staging. This separation ensures phenotype-based diagnosis maintains diagnostic and prognostic priority, avoids biomarker or AI overreach, and supports nuanced interpretation of mild-to-moderate cases and advanced disease stages [source_supported_conclusion: src-hcm-001, src-hcm-009, src-hcm-010, src-hcm-013, src-hcm-023, src-hcm-024].

Key evidence:

- **Recognition hierarchy:**
  - Echocardiographic phenotype and gross morphometry dominate phenotype confirmation; mild-to-moderate hypertrophy remains diagnosis of exclusion.
  - Biomarkers like NT-proBNP and AI facilitate screening augmentation but cannot replace structural confirmation.
  - Genotype information modulates risk and interpretation but does not confirm current phenotype.
  - HCM recognition needs to remain inside a broader cardiomyopathy framework to avoid diagnostic tunnel vision [source_supported_conclusion: src-hcm-001, src-hcm-008, src-hcm-009, src-hcm-010, src-hcm-012, src-hcm-021, src-hcm-023].

- **Endpoint hierarchy:**
  - Structural confirmation is the leading endpoint, reflecting the disease phenotype heterogeneity.
  - NT-proBNP is useful to flag severe disease but unreliable for mild-to-moderate HCM screening.
  - Troponin I indicates myocardial injury/burden rather than phenotype definition.
  - Novel biomarkers and AI widen endpoint assessment but remain frontline confirmatory steps inferior.
  - Anatomopathological staging and right-ventricle involvement enhance depth of phenotype and severity understanding, especially in remodeled end stages [source_supported_conclusion: src-hcm-009, src-hcm-010, src-hcm-013, src-hcm-023, src-hcm-024].

- **Complementary evidence:**
  - Gross morphometry distinguishes HCM from normal hearts better than histologic cell-level analysis for recognition.
  - Severe phenotypes as defined by morphology/echo correlate with clinical outcomes; mild/moderate forms require cautious interpretation and exclusion of other causes.
  - AI-based radiographic screening shows promising accuracy but must be viewed as assistance, subordinated to echocardiographic confirmation [source_supported_conclusion: src-hcm-009, src-hcm-013, src-hcm-023].

What we don't know yet:

- How specifically boundaries should be operationalized in diverse clinical settings, especially for milder or equivocal cases.
- The extent to which biomarker and AI augmentation can be prospectively validated across populations and breeds beyond research colonies.
- Detailed integration of genotype dosage effects with phenotype staging for tailored prognosis.
- Optimal use and timing of pathology staging in living patients to inform management decisions.
- Validation of morphometric thresholds and their relation to echo findings in routine practice [source_supported_conclusion: src-hcm-010, src-hcm-012, src-hcm-024].

---

## 研究者视角

Feline HCM recognition and endpoints rest on a fundamental pathological mechanism of left ventricular hypertrophy with variable, often asymmetric patterns detected primarily by echocardiography and gross morphometry. These structural phenotypes define the core diagnosis, distinguishing HCM from other myocardial diseases. Biomarkers (NT-proBNP, Troponin I) serve as quantitative signals of severe disease burden or myocardial injury but do not replace phenotype diagnosis. AI methodologies represent a frontier augmentation for screening and diagnostic assistance but remain below structure-first authority. Molecular genetics, notably MYBPC3 mutation dosage and age-dependent penetrance, modify severity risk and timing but cannot stand alone as phenotype confirmers. End-stage HCM is characterized by fibrotic remodeling, chamber dilation, and vascular changes, deepening severity architecture beyond initial hypertrophy. This multilayered framework maintains a disciplined clinical workflow separating phenotype recognition from endpoint stratification, ensuring clear biomarker and AI use cases while embedding HCM within the broader myocardial disease context [source_supported_conclusion: src-hcm-001, src-hcm-009, src-hcm-012, src-hcm-013, src-hcm-021, src-hcm-023, src-hcm-024].

## 不能说过头的地方

Current evidence mandates maintaining structural phenotype confirmation as the primary node for both recognition and endpoint assessment in feline HCM. Biomarkers like NT-proBNP and Troponin I should not be used standalone for mild-to-moderate disease diagnosis or screening, nor should AI or genotype information supplant imaging-based confirmation. The boundary rules established from research colony cohorts and experimental studies may not yet generalize fully to all clinical populations and breeds. End-stage pathology findings enrich severity understanding but are not practical frontline diagnostic tools. Thus, existing knowledge should be applied cautiously, avoiding overreliance on biomarkers or AI without structural confirmation and recognizing that these insights do not constitute direct professional veterinary advice but rather guide structured diagnost
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
- loaded paths: `raw/papers/src-ibd-003.md, raw/papers/src-ibd-004.md, raw/papers/src-ibd-009.md, raw/papers/src-ibd-010.md, raw/papers/src-ibd-015.md, raw/papers/src-ibd-016.md, raw/papers/src-ibd-017.md, raw/papers/src-ibd-019.md, raw/papers/src-ibd-024.md, topics/ibd/risk-and-recognition-bilingual.md, topics/ibd/risk-and-recognition.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1418 cards indexed
[info] Source weights: 1418 cards weighted
[info] Routing...
[info] Loaded: topics/ibd/risk-and-recognition.md
[info] Loaded: topics/ibd/risk-and-recognition-bilingual.md
[info] Hop 1/3 (~3107 tokens loaded)...
[info] Loaded source: src-ibd-003
[info] Loaded source: src-ibd-004
[info] Loaded source: src-ibd-009
[info] Loaded source: src-ibd-010
[info] Loaded source: src-ibd-015
[info] Loaded source: src-ibd-016
[info] Loaded source: src-ibd-017
[info] Loaded source: src-ibd-019
[info] Loaded source: src-ibd-024
[info] Hop 2/3 (~16730 tokens loaded)...
[info] Agent ready to synthesize
[info] Vision: no verified figures on disk yet (extract PDFs to enable)
[info] Synthesizing (11 files, ~16730 tokens)...
[meta] ROUTER_QTYPE=recognition
[meta] ROUTER_DISEASE=ibd
[meta] FIRST_FAMILY=risk-and-recognition
[meta] LOADED_PATHS=raw/papers/src-ibd-003.md,raw/papers/src-ibd-004.md,raw/papers/src-ibd-009.md,raw/papers/src-ibd-010.md,raw/papers/src-ibd-015.md,raw/papers/src-ibd-016.md,raw/papers/src-ibd-017.md,raw/papers/src-ibd-019.md,raw/papers/src-ibd-024.md,topics/ibd/risk-and-recognition-bilingual.md,topics/ibd/risk-and-recognition.md
```

Result excerpt:

```text
The current IBD versus small-cell lymphoma boundary in this vault is framed as a complex, multistep, and exclusion-first diagnostic process that integrates clinical suspicion of chronic enteropathy, targeted biopsy strategies including duodenal and ileal sampling, ultrasound imaging cues (notably muscularis propria thickening), detailed histopathologic interpretation, and supportive tissue and noninvasive biomarkers. No single marker or modality definitively separates IBD from small-cell lymphoma; rather, the boundary is an operational and interpretive workflow that balances suspicion, sampling completeness, and integrated pathology along with adjunct markers and emerging frontier tools like metabolomics.

Key evidence supporting this includes:

- Feline IBD is defined as a diagnosis of exclusion starting from chronic gastrointestinal enteropathy suspicion, recognizing that dietary disease and well-differentiated alimentary lymphoma can mimic IBD clinically and histologically. This excludes premature assignment of idiopathic IBD before lymphoma or food-responsive disease are ruled out [source_supported_conclusion: src-ibd-003, src-ibd-024].

- The Feline Chronic Enteropathy Activity Index (FCEAI) provides a practical measure for staging disease burden and tracking treatment response but cannot discriminate IBD from food-responsive enteropathy or small-cell lymphoma [source_supported_conclusion: src-ibd-004].

- Ultrasound findings, specifically thickening of the muscularis propria, raise suspicion for lymphoma over IBD, especially in older cats; however, lymphadenopathy is non-specific and appears in both conditions [source_supported_conclusion: src-ibd-010].

- Endoscopic biopsy should include both duodenal and ileal samples because biopsy-site findings often disagree, and small-cell lymphoma can be detected exclusively at the ileum in a significant subset of cats. This demonstrates the criticality of site selection in achieving diagnostic completeness for lymphoma exclusion [source_supported_conclusion: src-ibd-015].

- Histopathology report structure influences classification accuracy; free-text descriptions capture discriminative features better than standardized WSAVA structured features, with plasma-cell quantification emerging as a reproducible feature potentially helpful in differentiating IBD and lymphoma [source_supported_conclusion: src-ibd-009].

- Tissue markers such as Bcl-2 immunolabeling tend to be higher in lymphoma than IBD but show overlap and cannot serve as standalone discriminators. Their role is to add lymphoma-leaning pressure within a multi-layer diagnostic context [source_supported_conclusion: src-ibd-016].

- Noninvasive fecal markers like S100A12 can distinguish abnormal chronic enteropathy from health but do not differentiate IBD from lymphoma, emphasizing their supportive but non-decisive role in the boundary workup [source_supported_conclusion: src-ibd-017].

- Frontier tools like untargeted fecal metabolomics indicate metabolic differences between IBD and small-cell lymphoma, particularly involving polyunsaturated fatty acids and associated pathways, representing promising but as yet non-routine stratification tools [source_supported_conclusion: src-ibd-019].

What we don't know yet includes:

- Precise operational algorithms integrating imaging, biopsy-site strategy, histopathology, and biomarkers for routine clinical discrimination.

- Validation and thresholding of molecular or metabolomic markers for definitive diagnosis and their additive value beyond biopsy and imaging.

- How well plasma-cell quantification or Bcl-2 staining independently improve lymphoma detection in live clinical practice.

- The optimal clinical criteria triggering ileal biopsy in routine workflows.

- Stability, repeatability, and treatment-response dynamics of fecal S100A12 and metabolomics in chronic enteropathy subtypes.

---

## 研究者视角

The IBD versus small-cell lymphoma boundary in feline chronic enteropathy diagnosis involves understanding pathological features, multimodal biomarker integration, and clinical context. The pathological hallmark difference is histologic differentiation of inflammatory infiltrate characteristic of idiopathic IBD versus neoplastic lymphoid proliferation in lymphoma, supported by immunohistochemical markers such as Bcl-2 that tend to overexpress in lymphoma. Morphological assessment requires site-aware biopsy sampling, notably including ileal tissue, given its frequent lymphoma-only involvement.

Imaging biomarkers like muscularis propria thickening reflect lymphoma-associated structural changes but are insufficient for standalone diagnosis. Noninvasive inflammatory markers such as fecal S100A12 support disease presence but not class distinction, while advanced metabolomics show class-stratifying potential through metabolite profiles related to lipid and oxidative pathways. Diagnostic algorithms must prioritize exclusion of mimics using chronic enteropathy suspicion, comprehensive tissue sampling, and multilayer pathology including both traditional histology and adjunct markers. Novel tools like free-text pathology informatics and metabolomic profiling represent active research frontiers to refine this boundary.

## 不能说过头的地方

Current evidence clearly supports that no single marker or test conclusively distinguishes feline IBD from small-cell lymphoma. Ultrasound, biopsy, histopathology, and biomarkers provide supportive signals but must not replace comprehensive diagnostic exclusion protocols. Chronic enteropathy suspicion is not synonymous with idiopathic IBD confirmation, and FCEAI scores should be confined to activity tracking rather than etiologic diagnosis.

One-site biopsies, especially duodenal-only, cannot reliably exclude lymphoma presence; ileal biopsies are critical. Bcl-2 and S100A12 markers, while informative, overlap between diseases and cannot be used as diagnostic endpoints alone. Metabolomics remain investigational and not routin
```

## Q7. Cross-disease question

Question: `Compare CKD and HCM on the maturity of their endpoint architecture.`

Must see: 要么稳妥回答，要么诚实降级，不能假精确。
Expected question_type: `synthesis`
Expected primary family: `disease-module-maturity-ladder`
Expected strongest surface: `system/indexes/disease-module-maturity-ladder.md`

Exit code: `0`
Confidence: `low`
Source IDs found: `src-ckd-004, src-ckd-006, src-ckd-007`

Routing read:

- router question_type: `synthesis`
- first family: `disease-module-maturity-ladder`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `answer-compression-miss`
- next fix layer: `answer-compression`
- loaded paths: `raw/papers/src-ckd-001.md, raw/papers/src-ckd-002.md, raw/papers/src-ckd-003.md, raw/papers/src-ckd-004.md, raw/papers/src-ckd-006.md, raw/papers/src-ckd-007.md, raw/papers/src-ckd-010.md, raw/papers/src-ckd-013.md, raw/papers/src-ckd-015.md, raw/papers/src-ckd-017.md, system/indexes/cross-disease-second-wave-narrow-owner-audit.md, system/indexes/disease-module-maturity-ladder.md, topics/ckd/endpoint-handbook.md, topics/hcm/endpoint-handbook.md, ../../topics/ckd/endpoint-handbook.md, ../../topics/hcm/endpoint-handbook.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1418 cards indexed
[info] Source weights: 1418 cards weighted
[info] Routing...
[info] Loaded: system/indexes/disease-module-maturity-ladder.md
[info] Loaded: system/indexes/cross-disease-second-wave-narrow-owner-audit.md
[info] Loaded: ../../topics/ckd/endpoint-handbook.md
[info] Loaded: ../../topics/hcm/endpoint-handbook.md
[info] Hop 1/3 (~7495 tokens loaded)...
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
[info] Synthesizing (14 files, ~26379 tokens)...
[meta] ROUTER_QTYPE=synthesis
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=disease-module-maturity-ladder
[meta] LOADED_PATHS=raw/papers/src-ckd-001.md,raw/papers/src-ckd-002.md,raw/papers/src-ckd-003.md,raw/papers/src-ckd-004.md,raw/papers/src-ckd-006.md,raw/papers/src-ckd-007.md,raw/papers/src-ckd-010.md,raw/papers/src-ckd-013.md,raw/papers/src-ckd-015.md,raw/papers/src-ckd-017.md,system/indexes/cross-disease-second-wave-narrow-owner-audit.md,system/indexes/disease-module-maturity-ladder.md,topics/ckd/endpoint-handbook.md,topics/hcm/endpoint-handbook.md
```

Result excerpt:

```text
Feline CKD has a more mature and controlled endpoint architecture than feline HCM, reaching a full Level 7 maturity with active second-wave narrow-owner signals driving priority memos within its endpoint and control layers. In contrast, HCM is at a transitional late Level 6.5 moving into Level 7 status, showing extensive bilingual compiled pages and active second-wave boundary memos but with slightly less overall control-layer thickness and output matrix maturity than CKD. CKD’s endpoint framework is well-established with a multi-tiered, multi-axis operational hierarchy that integrates core diagnostic, progression, treatment, and context endpoints tied robustly to pathology and clinical guideline consensus. HCM’s endpoint hierarchy is structured but still evolving, emphasizing a structural confirmation-led approach supplemented by bounded biomarker, AI, and pathology-depth augmentation layers without flattening the endpoint importance into a single ranking.

Key evidence:

- CKD is at Level 7 maturity, fully integrated with a robust compiled spine, output layers (briefing, dossier, slides), bilingual compiles, audit, QA, and traceability, plus emerging second-wave priority signaling for route memos, indicating a self-compressing controlled module [llm_inference].

- HCM stands between late Level 6.5 and early Level 7, having compiled memos, extensive bilingual outputs, active biomarker and regulatory branch ownership, and newly appeared second-wave signals such as AI augmentation boundaries; yet its control layer and output matrix thickness remain slightly less mature than CKD [llm_inference].

- CKD endpoints are hierarchically categorized into core operational (creatinine, USG, UPCR, systolic blood pressure, phosphorus), early detection (SDMA, GFR), and context markers (PTH, calcium, FGF23, anaemia, imaging). This architecture is multi-axis, with endpoints mapping to different lesion patterns (e.g., fibrosis-linked vs glomerulo-vascular injury) [llm_inference].

- HCM endpoint hierarchy similarly follows a staged model: structural confirmation leads (echocardiography and gross morphology), followed by severe-disease screening markers (NT-proBNP), injury/burden signals (troponin I), and frontier biomarker/AI augmentation, plus phenotype-depth endpoints (right ventricular involvement and pathology staging). HCM endpoints maintain a hierarchy, avoiding flattening all markers into one ranking [llm_inference].

- CKD’s endpoint and treatment maturity are reflected in comprehensive guidelines (ISFM) and multiple high-value source extractions that frame serial surveillance, multi-parameter monitoring, and complex mineral-bone disorder interpretation. Treatment evidence hierarchy strongly supports renal diet and phosphorus control at the apex [quoted_fact: src-ckd-004, src-ckd-006, src-ckd-007].

- HCM endpoint architecture has begun to incorporate sophisticated secondary control notes (e.g., AI augmentation boundary) and phenotype-depth interpretations but lacks the same degree of control-layer densification and audit granularity present in CKD [llm_inference].

What we don’t know yet:

- The exact comparative impact of second-wave narrow-owner control layers on clinical workflow and trial endpoint refinement in HCM compared to CKD is unclear.

- The precise quantitative difference in output matrix thickness and control-layer maturity between CKD and HCM in operational clinical settings lacks granular measurement beyond the categorical level.

- How frontier biomarker integration and AI augmentation in HCM will influence endpoint validation and clinical adoption over time remains to be demonstrated.

---

## 研究者视角

CKD的终点架构体现为一套多层次、结构严谨的体系，将核心操作性指标（肌酐、尿比重、蛋白尿、收缩压、磷）置于首位，同时辅以早期检测标记（SDMA、GFR）和临床管理上下文指标（PTH、钙离子、FGF23、贫血、影像学），此分类反映不同病理结构如间质纤维化与肾小球血管病变的多轴关系，强调了终点与病变的直接关联。CKD模块在成熟度上达到系统控制层（Level 7），涵盖了完整的编译备忘录、多语言输出、数据审核和复核追踪，且已经开展第二层窄拥有人角色的深化管理，专注于分支内部边界、优先级和门控判定，使得该疾病模块进入了高度结构化、可审计和动态更新的控制范畴。相较而言，HCM的终点架构虽涵盖结构确认、严重疾病筛查（NT-proBNP）、损伤负担（肌钙蛋白I）及前沿生物标志物和AI增强层次，但整体控制层深度及输出矩阵厚度尚略逊于CKD，当前处于Level 6.5至7的过渡阶段，正逐步向完整控制层成熟转型。HCM中强调终点之间层级区分，避免生物标志物与结构终点混淆，并针对其病理深度和临床表型制定细致的分支边界管理。

## 不能说过头的地方

尽管具有广泛数据支持，CKD与HCM在终点架构成熟度上的比较依赖预设层级划分，缺乏绝对量化指标，且两者模块的输出密度与控制层稳健度存在一定主观评估成分。第二层窄拥有人信号目前主要基于内部审核复合指标，并非直接明证其临床效用，因而不宜过度透支其对临床工作流即时优化的意义。两病种的终点逻辑虽然结构化，但不构成具体临床诊疗建议，应在兽医专业判断范围内结合个案特征使用。当前知识仓库框架更适合用于评估和设计研究优先级及证据整合，而非直接指导临床干预。

## 下一步

未来研究应聚焦于：

- 定量比较CKD与HCM终点架构中控制层与输出矩阵的具体指标，推动多维度成熟度测评体系发展。

- 验证第二层窄拥有人信号在临床路径优化及研究效率提升中的实际作用，尤其在HCM中的应用效能。

- 深入评估HCM中AI和前沿生物标志物对终点确定与病理分型准确率的影响，促进其临床转化。

- 在CKD基础上，拓展矿物质骨代谢紊乱分支的功能性终点，强化其在疾病监测和治疗干预中的角色。

- 完善双方病种的终点与治疗效应关联模型，促进个性化疗法设计与证据支持。
```

## Q8. Regulatory question

Question: `What is the current regulatory path surface for feline CKD programs across China, FDA, and VMD?`

Must see: 至少承认 jurisdiction split。
Expected question_type: `regulatory`
Expected primary family: `regulatory-brief`
Expected strongest surface: `topics/ckd/regulatory-brief.md`

Exit code: `0`
Confidence: `medium`
Source IDs found: `src-reg-001, src-reg-002, src-reg-003, src-reg-004, src-reg-005, src-reg-008, src-reg-009`

Routing read:

- router question_type: `regulatory`
- first family: `regulatory-brief`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `raw/regulations/src-reg-001-cn-vet-registration.md, raw/regulations/src-reg-002-cn-approval-number.md, raw/regulations/src-reg-003-cn-import.md, raw/regulations/src-reg-004-fda-animal-drugs.md, raw/regulations/src-reg-005-fda-conditional.md, raw/regulations/src-reg-008-vmd-marketing-authorisation.md, raw/regulations/src-reg-009-vmd-annex2.md, topics/ckd/regulatory-brief.md`

stderr:

```text
[info] Backend: openrouter  model: openai/gpt-4.1-mini
[info] Source index: 1418 cards indexed
[info] Source weights: 1418 cards weighted
[info] Routing...
[info] Loaded: topics/ckd/regulatory-brief.md
[info] Hop 1/3 (~3549 tokens loaded)...
[info] Loaded source: src-reg-001
[info] Loaded source: src-reg-002
[info] Loaded source: src-reg-003
[info] Loaded source: src-reg-004
[info] Loaded source: src-reg-005
[info] Loaded source: src-reg-008
[info] Loaded source: src-reg-009
[info] Hop 2/3 (~8127 tokens loaded)...
[info] Agent ready to synthesize
[info] Vision: no verified figures on disk yet (extract PDFs to enable)
[info] Synthesizing (8 files, ~8127 tokens)...
[meta] ROUTER_QTYPE=regulatory
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=regulatory-brief
[meta] LOADED_PATHS=raw/regulations/src-reg-001-cn-vet-registration.md,raw/regulations/src-reg-002-cn-approval-number.md,raw/regulations/src-reg-003-cn-import.md,raw/regulations/src-reg-004-fda-animal-drugs.md,raw/regulations/src-reg-005-fda-conditional.md,raw/regulations/src-reg-008-vmd-marketing-authorisation.md,raw/regulations/src-reg-009-vmd-annex2.md,topics/ckd/regulatory-brief.md
```

Result excerpt:

```text
The current regulatory path landscape for feline chronic kidney disease (CKD) programs involves distinct, structured frameworks across China, the U.S. FDA, and the UK VMD, with the European Medicines Agency (EMA) adding a strategic limited-market consideration. China manages veterinary drug registration at the ministry level with separate formal registration, approval-number issuance, and import-administration pathways. The FDA pathway bifurcates into full approval—with substantial evidence of effectiveness required—and conditional approval, which requires a reasonable expectation of effectiveness and specific eligibility criteria beyond species designation. The UK VMD requires applicants to choose among multiple marketing authorisation routes, each with strict dossier structure mandates aligned with current scientific guidelines. EMA’s pathway includes a potentially significant limited-market route under Article 23 of Regulation (EU) 2019/6 that could affect data requirements if feline CKD products qualify. None of these jurisdictions currently support a simple “human drug to pet” shortcut, emphasizing the need for clear species- and indication-specific regulatory strategies.

**Key Evidence:**

- **China**:  
  - New veterinary drug and imported veterinary drug registration are regulated at the ministry level per 兽药注册办法, requiring clinical trials completion before submission.  
  - A veterinary product approval number issued by the ministry is mandatory for manufacturing each veterinary product, separating registration from manufacturing approval.  
  - Imported veterinary drugs require additional import customs clearance and product documentation, forming a distinct regulatory workflow.  
  [quoted_fact: src-reg-001, src-reg-002, src-reg-003]  
  [source_supported_conclusion: src-reg-001, src-reg-002, src-reg-003]

- **FDA (USA)**:  
  - Full approval requires substantial evidence of effectiveness; conditional approval allows earlier market access under the premise of reasonable expectation but is time-limited and requires renewal.  
  - Cats are classified as a major species, but conditional approval eligibility depends on the disease’s seriousness, unmet needs, and study complexity—not merely on feline status.  
  - FDA companion animal study guidance explicitly addresses active-control clinical trial design considerations for cats.  
  [quoted_fact: src-reg-004, src-reg-005]  
  [source_supported_conclusion: src-reg-004, src-reg-005]

- **EMA (EU)**:  
  - Article 23 under Regulation (EU) 2019/6 provides a limited-market route for non-immunological veterinary medicines, potentially altering efficacy and safety data requirements.  
  - Early testing of limited-market eligibility is strategically important before committing to a standard full dossier.  
  [llm_inference]  
  [llm_inference]

- **VMD (UK)**:  
  - Marketing authorisation applications must select from multiple available routes and comply with structured dossier documentation as per Veterinary Medicines Regulations Annex 2.  
  - Current guidance emphasizes route selection plus dossier discipline rather than a single uniform pathway.  
  - Efficacy and safety documentation must align with up-to-date veterinary medicinal knowledge and established guidelines.  
  [quoted_fact: src-reg-008, src-reg-009]  
  [source_supported_conclusion: src-reg-008, src-reg-009]

- **Cross-jurisdictional notes**:  
  - No official source yet supports a “human drug to pet” shortcut; this remains an internal strategic question.  
  - Regulatory planning should focus on product archetype, target indication claim, evidence package feasibility, and jurisdiction-specific pathway fit rather than on which country is “easiest.”  
  [source_supported_conclusion: src-reg-001, src-reg-003, src-reg-004, src-reg-008]

**What We Don’t Know Yet:**

- Disease- and indication-specific efficacy and safety evidence requirements for feline CKD products in any jurisdiction remain unidentified.  
- Detailed dossier requirements, especially in China, are not yet publicly available, limiting precise planning.  
- FDA’s acceptance criteria for CKD indications under conditional approval (for example, how complex studies must be to qualify) remain uncertain.  
- Whether EMA limited-market status will be available or beneficial for feline CKD products is currently unproven.  
- Import versus domestic product registration sequencing and timing in China are unknown.  
- Comprehensive guidance on which VMD marketing authorisation route is most appropriate for feline CKD in Great Britain has not been clarified.

---

## 研究者视角

The regulatory frameworks reflect a multi-layered approach to feline CKD therapeutic development. Mechanistically, candidate products must be accurately classified by archetype (e.g., small molecules, biologics, nutritional interventions) and be matched to intended claims (such as disease modification, progression slowing, or symptom control). China’s model delineates registration, approval-number issuance, and import management as operationally distinct checkpoints under the Ministry of Agriculture’s veterinary drug registration system (兽药注册办法). The FDA bifurcates approval into full and conditional pathways, requiring methodologically rigorous demonstration of effect or a justified reasonable expectation thereof, mindful of companion-animal-specific study design nuances including active-control trials. EMA’s Article 23 limited-market route introduces a potential shortcut but demands early screening for eligibility, influencing biomarker and endpoint requirements. The UK VMD enforces route-selection and dossier structure adherence aligned with the Veterinary Medicines Regulations Annex II, integrating scientific and regulatory best practices. This explains current regulatory complexity and highlights the absence of species- and indication-tailored guidance documents, underscoring an active research context focusing on CKD-specific clinical trial des
```
