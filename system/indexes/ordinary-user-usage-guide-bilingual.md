---
id: ordinary-user-usage-guide-bilingual
type: index
topic: system
question_type: usage
language: bilingual
last_compiled_at: 2026-05-19
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: active
---

# How Ordinary Users Should Use This Vault, Bilingual

If you want the shortest possible entry page first, start here:

- [Reader start here](reader-start-here.md)
- [compiled pages vs original papers](compiled-vs-source-reading.md)

## What This Page Is / 这页是什么

**EN**  
This page is for ordinary readers, not maintainers. It explains how to enter the vault, which pages to read first, and how to avoid getting lost in the raw layer.

**ZH**  
这页是给普通读者看的，不是给维护者看的。它解释的是，应该从哪里进入 vault、先读哪些页面、以及怎样避免一上来就掉进 raw 层。

## Short Answer / 最短答案

**EN**
1. pick the disease
2. either ask the Streamlit chat UI or open that disease's `navigation` / `current-state-dashboard`
3. choose pages by question type, not by folder name
4. treat `candidate-*` images as unverified references, not evidence

Current disease choices: `CKD`, `FIP`, `HCM`, `IBD`, `Diabetes`, `FCV`, `Obesity`.

**ZH**
1. 先选病种
2. 可以先用 Streamlit 问答界面，也可以打开这个病种的 `navigation` 或 `current-state-dashboard`
3. 按问题类型选页面，不要按文件夹名乱找
4. 看到 `candidate-*` 图片时，把它当成未验证线索，不要当成证据

当前可选病种：`CKD`、`FIP`、`HCM`、`IBD`、`Diabetes`、`FCV`、`Obesity`。

## The 4 Most Common User Goals / 普通用户最常见的 4 个目标

### 0. You want to ask the vault directly / 你想直接问这个资料库

**EN**
- open the project folder in Terminal
- run `source .venv/bin/activate`
- run `python -m streamlit run scripts/app.py`
- open the local URL shown by Streamlit, usually `http://localhost:8501`
- choose a backend in the sidebar, then ask one narrow question
- if you use OpenRouter, prefer `OPENROUTER_MODEL=openai/gpt-4.1-mini` and keep `OPENROUTER_DAILY_BUDGET_USD=1.00`
- if a maintainer gives you a temporary public test link, open that link directly instead of starting the app yourself
- if the Streamlit public link is stuck loading, use the plain HTTP public test page instead

**ZH**
- 在终端打开项目目录
- 运行 `source .venv/bin/activate`
- 运行 `python -m streamlit run scripts/app.py`
- 打开 Streamlit 显示的本地网址，通常是 `http://localhost:8501`
- 在侧边栏选择模型后端，然后问一个具体问题
- 如果你用 OpenRouter，优先用 `OPENROUTER_MODEL=openai/gpt-4.1-mini`，并保持 `OPENROUTER_DAILY_BUDGET_USD=1.00`
- 如果维护者给了临时公开测试链接，直接打开那个链接，不需要自己启动 app
- 如果 Streamlit 公开链接一直加载不出来，改用普通 HTTP 公开测试页

如果普通用户页在真实 OpenRouter 路径报错，先看：

- [Ask The Vault OpenRouter runtime playbook](ask-the-vault-openrouter-runtime-playbook-20260424.md)

### 1. You want the fastest status read / 你只想最快知道现在做到哪了

**EN**
- start with the disease dashboard
- use bilingual dashboards if cross-language alignment matters
- dashboards answer: what exists, what is strong, what is thin, what should happen next

**ZH**
- 先看病种 dashboard
- 如果你在意中英对照，优先看 bilingual dashboard
- dashboard 主要回答：现在有什么、哪里比较稳、哪里还薄、下一步最该做什么

### 2. You want to read one disease quickly / 你想快速读懂一个病种

**EN**
- start with that disease's `navigation`
- navigation pages separate mechanism, recognition, endpoint, translation, and regulatory branches
- if you do not know where to begin, always start from `navigation`

**ZH**
- 先看对应病种的 `navigation`
- navigation 会把 mechanism、recognition、endpoint、translation、regulatory 分开
- 如果你不知道从哪开始，永远先从 `navigation` 进入

### 3. You want something readable right now / 你想先拿一份能直接读的材料

**EN**
- start with outputs, not source cards
- use `briefing`, `dossier`, or `slides`
- these are good for internal discussion, but not submission-grade conclusions

**ZH**
- 先看 output，不要先看 source card
- 直接用 `briefing`、`dossier` 或 `slides`
- 这些材料适合内部讨论，但不等于 submission-grade 结论

### 4. You want an answer to one specific question / 你想查某个具体问题

**EN**
- mechanism question → `mechanism-overview`
- recognition or workup question → `risk-and-recognition` or `diagnostic-workup memo`
- endpoint or marker question → `endpoint-handbook`
- treatment or translation question → `translation-brief` or `treatment-evidence`
- regulatory question → `regulatory-brief`
- structured overall answer → `synthesis-index`

**ZH**
- 机制问题 → `mechanism-overview`
- 识别或诊断流程问题 → `risk-and-recognition` 或 `diagnostic-workup memo`
- endpoint 或 marker 问题 → `endpoint-handbook`
- 治疗或转化问题 → `translation-brief` 或 `treatment-evidence`
- 监管问题 → `regulatory-brief`
- 想看结构化综合结论 → `synthesis-index`

## Best Reading Order For New Readers / 新读者最稳的阅读顺序

**EN**
1. `current-state-dashboard`
2. `navigation`
3. `briefing` or `briefing-zh`
4. `synthesis-index`
5. then drill into specific topic pages

**ZH**
1. `current-state-dashboard`
2. `navigation`
3. `briefing` 或 `briefing-zh`
4. `synthesis-index`
5. 然后再进入具体 topic page

## Trust Boundary / 可信边界

**EN**
- lower layers are closer to evidence
- higher layers are easier to read
- easier to read does not mean stronger evidence

**ZH**
- 越底层越接近证据
- 越上层越容易读
- 越容易读，不代表证据越强

## Using Both Together / 两层一起用

**EN**
This is normal, and often better:
1. start with a compiled page to orient yourself
2. go back to the original paper to verify a claim
3. return to the compiled page to place that claim back into the larger structure

**ZH**
这其实是正常而且更好的用法：
1. 先用 compiled page 定向
2. 再回原文核对某个 claim
3. 再回 compiled page，把这个 claim 放回整体结构

For the direct explanation, use:

- [compiled pages vs original papers](compiled-vs-source-reading.md)

## 5 Misuses To Avoid / 最该避免的 5 个误用

**EN**
1. do not treat `working-en` as a final external version
2. do not treat bilingual pages as stronger than their underlying sources
3. do not read `usable` on a dashboard as "already settled"
4. do not treat translation or regulatory pages as submission-grade advice
5. do not jump from one marker or treatment signal to a final conclusion without reading the boundary pages

**ZH**
1. 不要把 `working-en` 当成最终对外版本
2. 不要把 bilingual 页当成比底层 source 更强
3. 不要把 dashboard 上的 `usable` 理解成“已经定论”
4. 不要把 translation 或 regulatory 页当成 submission-grade advice
5. 不要只看一个 marker 或一个 treatment signal 就跳到最终结论

## Best Question Pattern / 最有效的提问方式

**EN**
Bad:
- "tell me about IBD"

Better:
- "what is the strongest recognition conclusion in IBD right now?"
- "which CKD endpoints are operational versus contextual?"
- "how strong is the current FIP treatment branch, and what can it not claim?"

**ZH**
不好的问法：
- “讲讲 IBD”

更好的问法：
- “IBD 现在最稳的 recognition 结论是什么？”
- “CKD 哪些 endpoint 是 operational，哪些只是 context？”
- “FIP 当前治疗分支能说多强，不能说多强？”

## One-Sentence Summary / 一句话总结

**EN**
The best way for an ordinary user to use this vault is: start from dashboard or navigation, build the big picture from briefing or synthesis, then drill down by question type.

**ZH**
普通用户使用这个 vault 最好的方法是：先从 dashboard 或 navigation 进入，用 briefing 或 synthesis 建立大图，再按问题类型下钻。
