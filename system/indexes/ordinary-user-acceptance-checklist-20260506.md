---
id: system-ordinary-user-acceptance-checklist-20260506
type: system
topic: operating-system
question_type: checklist
language: zh
last_compiled_at: 2026-05-06
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Ordinary-User Acceptance Checklist, 2026-05-06

这页只回答一个窄问题：

`普通用户第一次打开 Ask the vault 时，什么样的回答算真的够用？`

## 类型判断

这件事属于：

`检查`

不是新方案，也不是故障排查。

## 最短结论

先不要继续往内容里加更多页面。

先用一组固定的普通用户问题，验证 5 件事：

1. 能不能稳定命中普通用户答案面
2. 能不能给出足够长，但仍可扫读的解释
3. 能不能清楚区分证据、支持性结论、推断
4. 能不能把 next step 说出来
5. 能不能把 reader-facing value 和 Wikipedia 区分开

## 这组样本为什么存在

这组问题不是为了测“有没有答案”。

它是为了测：

- 普通用户会不会一进来就得到可读的解释
- answer surface 会不会比文件树导航更像产品
- trust block 有没有真的帮助理解，而不是只做装饰

## 样本集

### Q1. CKD overview

问题：

`解释CKD`

必须看到：

- `overview` 路由
- `current-state-dashboard` 或同层级最强总览面
- 至少 2 个真实 source ids
- 读者能看懂的 plain-language answer

### Q2. FIP recognition

问题：

`FIP怎么识别`

必须看到：

- `recognition` 路由
- 识别 / workup 逻辑，而不是 generic disease summary
- 明确的 boundary 或 lead/support distinction

### Q3. HCM overview

问题：

`HCM是什么，为什么危险`

必须看到：

- `overview` 路由
- 解释为什么危险，而不是只给病名定义
- 读者能直接理解的风险解释

### Q4. IBD versus lymphoma boundary

问题：

`IBD和淋巴瘤怎么区分`

必须看到：

- `recognition` 路由
- boundary answer，而不是百科式概览
- 至少一个清晰的“还不能直接下结论”的点

### Q5. Diabetes remission

问题：

`糖尿病猫为什么会缓解`

必须看到：

- `endpoints` 或等价的结果/缓解解释路由
- 能解释“缓解”不是“治愈”
- 读者不会被带到太抽象的机制墙里

### Q6. User worry

问题：

`我的猫肌酐升高，这个库能告诉我什么`

必须看到：

- 直接面向读者的风险解释
- 能告诉用户下一步该看什么页面
- 不要只给纯学术总结

## Pass Rule

这 6 题里，至少 5 题要达到下面标准才算通过：

1. 路由正确
2. 主回答可读
3. 证据可见
4. trust block 有解释
5. next step 清楚

## Manual Run Rule

先手动跑 3 到 10 个真实样本。

只要这类样本将来还会反复做，先人工验证，再考虑把它做成脚本、skill，或者 cron。

## One-Line Summary

普通用户验收不是看系统能不能答题，而是看它能不能把问题变成一个像样的答案面。
