---
id: system-ask-the-vault-day-1-runbook-20260416
type: system
topic: operating-system
question_type: runbook
language: zh
last_compiled_at: 2026-04-16
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Ask The Vault Day-1 Runbook, 2026-04-16

这页只回答一个实际问题：

`OpenRouter key 到手后，第一天应该怎么跑 ask-the-vault acceptance，而不是边跑边想？`

## 类型判断

这件事属于：

`检查执行 runbook`

不是新方案，也不是排查。

## 最短结论

第一天不要做 3 件事：

- 不要一上来测 UI
- 不要一上来打开 `--write-back`
- 不要一失败就去补内容

先跑 CLI acceptance，再按 fault tree 修主因。

## Preconditions

先确认这 5 件事：

1. 已安装 `openai`
2. 已安装 `streamlit`
3. 已设置 `OPENROUTER_API_KEY`
4. OpenRouter 网页里的 daily/project budget 已设为 `$1/day`
5. 已设置 `OPENROUTER_DAILY_BUDGET_USD=1.00` 和 `OPENROUTER_MODEL`

推荐最小安装：

```bash
pip3 install openai streamlit
export OPENROUTER_API_KEY=你的key
export OPENROUTER_DAILY_BUDGET_USD=1.00
export OPENROUTER_MODEL=openai/gpt-4.1-mini
```

如果普通用户页已经进入真实 OpenRouter 路径，但报 runtime 错，不要再翻旧 handoff，直接看：

- [Ask The Vault OpenRouter runtime playbook](ask-the-vault-openrouter-runtime-playbook-20260424.md)

如果你不想手敲整套 CLI 流程，也可以直接跑：

```bash
bash scripts/run_day1_acceptance.sh
```

## Day-1 Order

严格按这个顺序：

1. 跑纯本地测试
2. 跑 2 个 smoke questions
3. 跑完整 acceptance runner
4. 读报告，不要立刻改代码
5. 先修单一主因
6. 回跑同一题
7. 只有 CLI 稳了，才开 UI

## Step 1: Local Sanity

先跑：

```bash
python3 scripts/test_query.py
python3 -m py_compile scripts/query.py scripts/run_acceptance_checklist.py scripts/app.py
```

如果这里不过，不要进 API 验收。

## Step 2: Smoke Questions

先只跑两题：

```bash
python3 scripts/query.py "CKD 的核心机制主线是什么？" --backend openrouter
python3 scripts/query.py "Compare CKD and HCM on the maturity of their endpoint architecture." --backend openrouter
```

先看 stderr metadata：

- `ROUTER_QTYPE`
- `FIRST_FAMILY`
- `LOADED_PATHS`

只要这两题明显走歪，就先别跑 8 题全套。

## Step 3: Full Acceptance

先生成空模板：

```bash
python3 scripts/run_acceptance_checklist.py --template-only
```

再跑完整验收：

```bash
python3 scripts/run_acceptance_checklist.py --backend openrouter
```

或直接让脚本串起来跑完前 3 步：

```bash
bash scripts/run_day1_acceptance.sh
```

报告位置：

- [ask-the-vault-acceptance-report-20260416.md](../health-checks/ask-the-vault-acceptance-report-20260416.md)

## Step 4: How To Read The Report

先看这 6 列，不要先读长答案：

1. `QType`
2. `First Family`
3. `Strongest Surface`
4. `Clear Miss`
5. `Failure Type`
6. `Next Fix Layer`

判读规则：

- `qtype-miss`：先修 router 题型
- `family-miss`：先修 family 选择
- `strongest-surface-miss`：family 可能对了，但最强页没进来
- `answer-compression-miss`：页进来了，但回答没压出最短结论
- `provenance-miss`：先修 tags 和 source id discipline
- `execution-miss`：先修依赖或运行时

## Step 5: Fix Discipline

第一轮只允许一种修法：

`一轮只修一个主因`

不要一次同时改：

- router
- answer scaffold
- page 内容
- UI

否则你看不出哪一层真的生效。

## Step 6: Fix Order

严格按这个顺序修：

1. `qtype-miss`
2. `family-miss`
3. `strongest-surface-miss`
4. `answer-compression-miss`
5. `provenance-miss`
6. `content-miss`
7. `write-back-miss`

详细说明看：

- [ask-the-vault acceptance fault tree](ask-the-vault-acceptance-fault-tree-20260416.md)

## Step 7: UI Check

只有 CLI 基本稳定后，才跑：

```bash
python3 -m streamlit run scripts/app.py
```

UI 侧只检查这几件事：

- backend 能选 `OpenRouter (API)`
- 回答里 badge 正常
- sidebar files loaded 正常
- confidence 正常显示

不要在 CLI 还没稳的时候，把失败归咎给 UI。

## Step 8: Write-Back Check

第一天默认：

`不要开 --write-back`

只有当 8 题里大部分已经稳定，并且 provenance 没失真，才单独验证：

```bash
python3 scripts/run_acceptance_checklist.py --backend openrouter --write-back
```

然后再看：

- frontmatter 是否完整
- slug 是否稳定
- 文件名是否污染已有高价值产物

## Fast Triage By Question

如果是：

- `Q1/Q2`：先看 strongest surface 有没有中
- `Q3`：先看 verification 风格和 uncertainty 有没有保留
- `Q4/Q5/Q6`：先看有没有误当 generic disease summary
- `Q7`：先看是不是被错当单病种 endpoint 题
- `Q8`：先看是不是把 jurisdiction split 压没了

## Day-1 Exit Criteria

第一天不追求“全部修完”。

第一天只要达到下面 3 条，就算成功：

1. acceptance 能稳定跑出报告
2. 失败能被清楚归类，不再混成一团
3. 已经知道第一优先修复层是什么

## One-Line Summary

这页的作用不是教你怎么写更复杂的 ask-the-vault。

它只是确保 OpenRouter 一接上之后，第一轮验收按固定顺序执行，而不是边跑边猜。
