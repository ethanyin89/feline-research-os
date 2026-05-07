---
id: system-ckd-completion-and-multi-disease-rollout-memo
type: system
topic: ckd
last_compiled_at: 2026-04-09
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
language: zh
---

# CKD 完成度与多病种 rollout memo

这页回答的是三个紧挨着的问题：

`当前提供的 CKD 文献是不是已经处理完毕？`

`现在能不能开始并行引入 FIP / IBD / HCM？`

`以后新病种是不是还要像 CKD 一样反复确认？`

## 先给最短结论

当前 CKD 文献处理状态，不应被表述为：

`已经彻底完成`

更准确的表述是：

`当前批次已经完成到可复用模板级，但 CKD 仍保持增量开放`

也就是说：

- 对你目前已经提供的 CKD 文献，系统层、source 层、compiled 层已经做到了可工作的第一阶段闭环
- CKD 已经足够成熟，可以作为 FIP / IBD / HCM 的默认处理模板
- 后续新病种默认不需要再按 CKD 早期那种节奏反复找你确认
- 但 CKD 本身不能被视为封箱项目，后续新增文献仍然可以持续注入

## 对“处理完毕”的准确拆分

### 1. 如果说的是 ingest 和结构化处理

这一层基本可以认为：

`当前已提供的 CKD 文献，已处理完第一阶段`

原因很直接：

- 当前 CKD source corpus 已经有 `24` 篇 ingested papers
- 已经有完整的 source-card 层
- 已经有 `15` 篇做过 deep extraction
- topic / entity / synthesis / outputs / control layer 都已经建立

所以：

不是“还有很多原始资料连系统都没进去”。

### 2. 如果说的是知识深度和最终完备性

这一层不能说：

`已经完全处理完毕`

因为 dashboard 自己已经明确暴露了剩余薄点：

- treatment primary-study density 仍然不均
- dense model taxonomy 仍然偏薄
- product-specific regulatory strategy 仍不是 decision-grade
- newer early-detection literature 后续还可能继续加厚

所以更准确的判断是：

`已完成第一阶段闭环，不等于已经达到最终完备状态`

## 当前 CKD 更适合被定义成什么

当前 CKD 最合适的系统定义不是：

- 结束项目

而是：

- `open canonical module`

也就是：

- 它已经是当前 vault 里第一套真正成型的病种模块
- 它可以作为后续病种的默认骨架
- 它仍然允许后续继续追加 source、deep extraction、entity densification 和 route refinement

这和软件里的 `stable but still maintained` 更像，而不是 `archived`

## 能不能开始注入 FIP / IBD / HCM

可以。

而且按当前状态，不只是“可以”，而是：

`现在开始是对的`

原因是：

### 1. CKD 已经把工作流打磨出来了

现在 CKD 已经验证过下面这些层都能跑通：

- raw ingest
- source card
- deep extraction
- topic / entity compile
- synthesis / outputs
- verification / traceability / language QA

所以继续只在 CKD 里打转，边际收益已经开始下降。

### 2. 新病种不会再从零发明方法

FIP / IBD / HCM 不需要重新探索：

- source 怎么写
- topic 怎么分
- entity 什么时候建
- bilingual / output 怎么处理
- claim 边界怎么管

这些现在都应该继承 CKD 的模式，而不是重新发明。

### 3. CKD 可以继续增补，不会阻塞多病种推进

这件事最重要。

CKD 后续有新文献，不意味着必须暂停其他病种。

更合理的系统状态应该是：

- CKD 保持开放
- 新病种按同一操作系统继续扩张

## 后续新病种是否还要反复找你确认

默认不需要。

从现在开始，默认 operating mode 应该升级为：

`autonomous within schema`

并且再补上一条：

`repeatable work must be codified, not just remembered`

意思是：

- 只要是你明确要纳入的病种
- 只要有原始文献被放进系统
- 就默认沿 CKD 的流程持续推进

不再需要每推进一小段就停下来问。

而这件事现在不该只靠隐含记忆。

新病种启动的默认 owner，应该明确归给：

- [disease-module-bootstrap-workflow.md](disease-module-bootstrap-workflow.md)

同时：

- 如果某类动作已经重复出现
- 且输出模式已经稳定
- 那它默认不该继续停留在“一次性处理”

而应该被固化成 protocol / workflow / prompt / schema / health check 之一。

## 新病种的默认处理顺序

后续 FIP / IBD / HCM，默认按下面顺序执行。

1. 建立病种目录和入口页  
   至少包括 `index / navigation / current-state-dashboard`

2. 建立 source index 并 ingest 当前资料  
   所有你给到的文献先进入 `raw/` 和 source layer

3. 做第一轮 topic / entity compile  
   先搭出机制、endpoint、recognition、translation、regulatory 这些骨架

4. 找高杠杆 source cluster  
   选最值得 deep extraction 的一批，不追求一上来全深提炼

5. 写第一轮 synthesis / output / control pages  
   至少要把 dashboard、synthesis、claim boundary、language status 建起来

6. 再做 densification  
   沿高价值薄点往下补，而不是一开始就铺满所有枝杈

## 什么情况下才需要重新找你确认

以后只在下面这些情况再停下来问你：

1. 病种范围本身有歧义  
   比如 IBD 是否同时纳入 chronic enteropathy 更宽定义

2. 资料包质量差异太大  
   比如只有二手文章，没有 primary / guideline anchor

3. 要做高成本方向选择  
   比如某病种是否提前进入 product / regulatory 线

4. 出现互斥的组织方式  
   比如按病理分支建模和按治疗分支建模，二者只能先选一个主骨架

除此之外，默认直接推进。

## 对 CKD 的后续处理规则

CKD 从现在开始，建议按下面规则处理：

### 默认状态

- `maintained`
- `appendable`
- `non-blocking`

### 具体含义

- 有新 CKD 文献，就继续 ingest
- 有高价值 source，就继续 deep extraction
- 有薄点被发现，就继续 densify
- 但这些动作不再阻塞 FIP / IBD / HCM 的启动

## 一个明确的执行判断

如果必须把这件事压成一句操作判断，那就是：

`CKD 已经不是 waiting-for-completion 状态，而是 ready-for-reuse 状态`

## 建议的下一步

从系统角度，最自然的顺序是：

1. 保持 CKD 为可继续增补的 canonical module
2. 直接开始新病种注入，优先建立 FIP / IBD / HCM 的 disease shell
3. 对新病种默认复用 CKD workflow
4. 只有遇到真正的 scope ambiguity 或 high-cost branching 才重新找你确认
