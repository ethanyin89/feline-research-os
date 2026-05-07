---
id: system-ask-the-vault-openrouter-runtime-playbook-20260424
type: system
topic: ask-the-vault
question_type: runbook
language: zh
last_compiled_at: 2026-04-24
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Ask The Vault OpenRouter Runtime Playbook, 2026-04-24

这页回答的是一个很具体的问题：

`普通用户页面在真实 OpenRouter 路径报错时，下一次应该怎么判断、怎么修、怎么避免回到同一个坑？`

## 类型判断

这件事属于：

`方案 owner + 运行时复用资产`

不是临时 handoff，也不是一次性排查记录。

## 最短结论

这次真实链路跑下来，已经可以把 OpenRouter 普通用户页的问题固定成 5 个 owner：

1. `环境问题`
2. `预算守卫问题`
3. `OpenRouter 返回空内容`
4. `默认模型不适合当前 chat-completions 路径`
5. `页面必须把错误保留下来，而不是 rerun 清掉`

## Current Stable Read

当前普通用户路径里，OpenRouter 的稳定默认值应读成：

`OpenRouter + OPENROUTER_DAILY_BUDGET_USD=1.00 + openai/gpt-4.1-mini + .venv streamlit`

## What Was Actually Learned

### 1. 没有 key 时，页面应直接阻止查询

这不是 bug。

正确行为是：

- sidebar 显示 `OPENROUTER_API_KEY not set`
- answer 区显示 `OpenRouter is selected, but OPENROUTER_API_KEY is not set in this shell.`

### 2. 预算守卫必须和 key 一样当成前置条件

这也不是可选优化。

当前项目已经明确要求：

- OpenRouter dashboard daily budget cap = `$1/day`
- project env `OPENROUTER_DAILY_BUDGET_USD=1.00`

少任意一个，都应该在页面层直接阻断。

### 3. `message.content=None` 不是理论问题，是真实返回形状

这次真实 API 调用已经证实：

- OpenRouter 可能返回 `resp.choices[0].message.content = None`
- 旧实现会把 `None` 继续喂给 regex / parser
- 现在已经改成先在 `_chat()` 截住，并输出可读错误

所以以后再看到：

- `content_type=NoneType`

不要再怀疑是不是 UI 假错，先按 runtime shape 读。

### 4. `finish_reason='length' + content_type=NoneType` 指向模型路径不合适

这次最关键的新事实不是“OpenRouter 不行”，而是：

`openai/gpt-5-mini` 在当前 JSON-first router/hop chat-completions 路径上，会耗尽 completion budget 但不给 usable text`

所以这个问题的 owner 不是：

- 内容问题
- routing prompt 本身
- 页面渲染层

而是：

- `default OpenRouter model selection`

当前默认值已改成：

- `openai/gpt-4.1-mini`

## Runtime Fault Tree

如果普通用户页再次失败，按这个顺序读：

### Case 1: `OPENROUTER_API_KEY not set`

主因：

- Streamlit 进程没拿到 key

动作：

- 先停旧进程
- 在同一个 shell 里 export key
- 再重启 Streamlit

### Case 2: `OPENROUTER_DAILY_BUDGET_USD not set` 或超 cap

主因：

- project guard 缺失或设置错误

动作：

- 先修 env
- 再确认 dashboard 也设成 `$1/day`

### Case 3: `OpenAI-compatible backend returned unsupported message content: NoneType`

主因：

- 后端返回空内容

动作：

- 先看 error details 里的 shape summary
- 重点看：
  - `finish_reason`
  - `content_type`
  - `refusal_present`
  - `tool_calls`

### Case 4: `finish_reason='length' + content_type=NoneType`

主因：

- 当前模型不适合这条普通用户路径

动作：

- 切到 `OPENROUTER_MODEL=openai/gpt-4.1-mini`
- 重启 Streamlit
- 不要继续用旧进程复测

### Case 5: 页面一失败就回空白

主因：

- query failure 被 `st.rerun()` 清掉

动作：

- 先查 `run_query(question) -> bool` 语义有没有被破坏
- 页面应保留 failure block，而不是刷新后看不到错误

## Recommended Start Command

```bash
cd ~/Desktop/insclaude/feline-research-os
source .venv/bin/activate
export OPENROUTER_API_KEY='your-key'
export OPENROUTER_DAILY_BUDGET_USD=1.00
export OPENROUTER_MODEL='openai/gpt-4.1-mini'
python -m streamlit run scripts/app.py
```

## What This Should Become

以后这类普通用户页 runtime 问题，默认应该先看这几个 surface：

- [README](../../README.md)
- [start](../../start.md)
- [ordinary user usage guide bilingual](ordinary-user-usage-guide-bilingual.md)
- [ask-the-vault day-1 runbook](ask-the-vault-day-1-runbook-20260416.md)
- 本页

而不是每次先翻 handoff。

## Why This Is Not A Skill

这次沉淀更适合做 repo 内 owner asset，而不是 gstack skill。

原因：

- 它强依赖当前仓库的 `scripts/app.py` / `scripts/query.py`
- 它强依赖当前 OpenRouter budget policy
- 它强依赖当前普通用户页的 Streamlit surface

所以它是：

`repo runtime playbook`

不是：

`cross-project reusable skill`

## Best Reuse Targets

- [ordinary user usage guide bilingual](ordinary-user-usage-guide-bilingual.md)
- [ask-the-vault day-1 runbook](ask-the-vault-day-1-runbook-20260416.md)
- future ask-the-vault acceptance / runtime handoff pages
