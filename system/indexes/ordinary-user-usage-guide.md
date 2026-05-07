---
id: ordinary-user-usage-guide
type: index
topic: system
question_type: usage
language: zh
last_compiled_at: 2026-04-09
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# 普通用户怎么使用这个项目

这页不是给维护者看的。

如果你不想先理解说明文档，直接先看：

- [Reader start here](reader-start-here.md)
- [compiled pages vs original papers](compiled-vs-source-reading.md)

这页回答的是：

`如果我是普通用户，我现在怎么用这个 vault？`

## 先说最短答案

普通用户不需要理解整套编译流程。

最简单的用法只有 3 步：

1. 先选病种
2. 再进这个病种的 `navigation` 或 `current-state-dashboard`
3. 按你的目的选页面，不要一上来就读 raw papers

## 普通用户最常见的 4 种用法

### 1. 你只想快速知道“现在能说到哪一步了”

先看 disease dashboard。

推荐入口：

- [CKD current state dashboard](../../topics/ckd/current-state-dashboard.md)
- [FIP current state dashboard](../../topics/fip/current-state-dashboard.md)
- [IBD current state dashboard](../../topics/ibd/current-state-dashboard.md)

如果你更习惯中英对照，优先看带 `bilingual` 的 dashboard。

这类页面回答的是：

- 现在已经做完什么
- 哪些结论比较稳
- 哪些地方还薄
- 下一步最值得补什么

### 2. 你想快速读一个病种，而不是研究系统本身

先看对应病种的 `navigation`。

推荐入口：

- [CKD navigation](../../topics/ckd/navigation.md)
- [FIP navigation](../../topics/fip/navigation.md)
- [IBD navigation](../../topics/ibd/navigation.md)

这些页的作用是：

- 告诉你从哪一页开始最省时间
- 把 mechanism、recognition、endpoint、translation、regulatory 分开
- 把 working output、中文页、双语页都挂好

如果你不知道从哪开始，永远先读 `navigation`。

### 3. 你想拿一份“能直接读”的总结

先读 output 层，不要先读 source card。

推荐入口：

- `briefing`
- `dossier`
- `slides`

现在 IBD 和 CKD 已经有比较完整的：

- `working-en`
- `en`
- `zh`
- 部分 `bilingual compiled` 页

这类页面适合：

- 快速内部同步
- 做讨论材料
- 先形成大图，再决定要不要下钻

但它们不适合被当成最终 submission-grade 结论。

## 4. 你想查某个具体问题

按问题类型走，不要按文件夹乱找。

### 机制问题

去：

- `mechanism-overview`

### 识别 / 诊断流程问题

去：

- `risk-and-recognition`
- `diagnostic-workup memo`

### marker / endpoint 问题

去：

- `endpoint-handbook`

### 治疗 / 转化问题

去：

- `translation-brief`
- `treatment-evidence memo`

### 监管 / 路径问题

去：

- `regulatory-brief`

### 想看结构化综合结论

去：

- `synthesis-index`

## 普通用户最稳的阅读顺序

如果你第一次接触一个病种，推荐按这个顺序读：

1. `current-state-dashboard`
2. `navigation`
3. `briefing` 或 `briefing-zh`
4. `synthesis-index`
5. 再按需要进入：
   `mechanism-overview`
   `risk-and-recognition`
   `endpoint-handbook`
   `translation-brief`
   `regulatory-brief`

也就是说：

`先看状态 -> 再看入口 -> 再看可读输出 -> 最后按问题深挖`

而不是：

`先读 raw paper -> 再自己拼`

## 普通用户要怎么理解不同页面的可信边界

这个项目里，不同层不是同一强度。

### 最底层

- `raw/papers/`
- `raw/regulations/`

这是原始材料层。

### 中间层

- `source card`
- `deep extraction worksheet`
- `topic page`
- `entity card`

这是编译层。

### 上层

- `synthesis`
- `briefing`
- `dossier`
- `slides`
- `bilingual compiled page`

这是为了阅读和复用而压缩过的派生层。

普通用户最需要记住的一句是：

`越往上越好读，但不代表越往上证据越强。`

## 如果你会一边看 compiled，一边看原文，这是正常的

这不是冲突，而是更合理的用法。

最稳的组合是：

1. 先用 compiled page 建立结构
2. 再回原文核对关键 claim
3. 然后再回 compiled 看这个 claim 在整条 disease branch 里放在哪

如果你只想搞清楚这两层到底分别干什么，直接看：

- [compiled pages vs original papers](compiled-vs-source-reading.md)

## 普通用户最该避免的 5 个误用

1. 不要把 `working-en` 当成最终对外版本
2. 不要把 `bilingual` 页当成比底层 source 更强的证据
3. 不要把 dashboard 上的“usable”理解成“已经定论”
4. 不要把 translation / regulatory 页当成 submission-grade advice
5. 不要只看一个 marker 或一个 treatment signal 就跳过 diagnosis / boundary 页面

## 如果你只会问一句话，应该怎么问

最有效的问法不是：

- “讲讲 IBD”

而是：

- “IBD 现在最稳的 recognition 结论是什么？”
- “FIP 现在 treatment branch 最能 defend 的结论是什么？”
- “CKD 哪些 endpoint 是 operational，哪些只是 context？”
- “IBD 的 treatment 现在能说多强，不能说多强？”

也就是：

`病种 + 问题类型 + 你想要的边界`

这样得到的答案会比“大而空的问题”稳定很多。

## 如果你想最快上手，直接走这条

### 中文用户

1. 先读对应病种的 `dashboard-bilingual` 或 `zh briefing`
2. 再读 `navigation`
3. 再进入具体问题页

### 英文用户

1. 先读 `dashboard` 或 `briefing working-en / en`
2. 再读 `navigation`
3. 再进入具体问题页

## 一句话总结

普通用户使用这个项目，最好的方法不是自己从论文层往上拼，而是：

`先从 dashboard / navigation 进入，再用 briefing / synthesis 建立大图，最后按问题类型进入 topic 或 memo。`
