# GBrain & GStack 日常操作路径

**更新日期:** 2026-04-28
**适用环境:** `/Users/jiawei/Desktop/insclaude/feline-research-os`

---

## 快速重启 Checklist

打开 terminal 后，按顺序执行：

```bash
cd /Users/jiawei/Desktop/insclaude/feline-research-os
source .venv/bin/activate
```

---

## 1. 启动 Streamlit App

### OpenRouter 后端 (推荐)

```bash
OPENROUTER_API_KEY='your-key' \
OPENROUTER_DAILY_BUDGET_USD=1.00 \
OPENROUTER_MODEL='openai/gpt-4.1-mini' \
python -m streamlit run scripts/app.py
```

浏览器打开 http://localhost:8501

### Anthropic 后端

```bash
ANTHROPIC_API_KEY='your-key' python -m streamlit run scripts/app.py
```

---

## 2. GStack 技能调用

### QA 测试 (headless)

```bash
# 在 Claude Code 中直接输入
/qa
# 或带参数
/qa http://localhost:8501
```

### 启动可视化浏览器

```bash
# 在 Claude Code 中直接输入
/open-gstack-browser
```

启动后可以用 `/qa` 看着浏览器执行测试。

### 常用技能列表

| 技能 | 用途 |
|------|------|
| `/qa` | QA 测试网站 |
| `/qa-only` | 只报告不修复 |
| `/open-gstack-browser` | 启动可视化浏览器 |
| `/learn` | 查看项目学习记录 |
| `/ship` | 提交代码 |
| `/review` | 代码审查 |
| `/investigate` | 调查 bug |

---

## 3. GBrain 记忆操作

### 存储记忆

```bash
~/Desktop/insclaude/bin/gbrain-remember <slug> "<memory>"
```

示例：
```bash
~/Desktop/insclaude/bin/gbrain-remember streamlit-startup "启动命令: source .venv/bin/activate && python -m streamlit run scripts/app.py"
```

### 检索记忆

```bash
~/Desktop/insclaude/bin/gbrain-recall "<query>"
```

示例：
```bash
~/Desktop/insclaude/bin/gbrain-recall "streamlit 怎么启动"
~/Desktop/insclaude/bin/gbrain-recall "QA 测试"
```

### 记忆规则

**应该存储的:**
- 系统配置 (Hermes, gbrain, OpenRouter, skills, scripts)
- 错误和修复配对
- 稳定的用户偏好
- 项目决策
- 可复用的工作流
- 常见错误及解决方案

**不应存储的:**
- 临时聊天内容
- API keys, 密码, tokens
- 一次性命令输出
- 未验证的假设

---

## 4. 项目健康检查

```bash
python3 scripts/health.py
python3 scripts/test_query.py
python3 scripts/check_markdown_links.py
```

---

## 5. QA 报告位置

QA 测试报告保存在：
```
.gstack/qa-reports/qa-report-localhost-YYYY-MM-DD.md
```

---

## 6. 已确认的项目学习 (Learnings)

| Key | Type | Insight |
|-----|------|---------|
| `research-lite-output-mode` | pattern | 研究笔记输出模式 |
| `karpathy-gap-order` | pattern | Karpathy 构想差距排序 |
| `geist-font-google-import` | pitfall | Geist 字体需要 Google Fonts 导入 |
| `image-ingest-gate` | operational | 图片入库 gate 流程 |

查看完整列表：
```bash
# 在 Claude Code 中
/learn
```

---

## 7. 注意事项

1. **这个 repo 不是 git 仓库** — `git` 命令会失败
2. **API 成本控制** — OpenRouter 需要设置 `$1/day` 预算
3. **虚拟环境** — 必须先 `source .venv/bin/activate`
4. **WaveSurfer 错误** — console 中的 WaveSurfer 错误是 Streamlit 框架问题，不影响功能

---

*最后更新: 2026-04-28 QA session 后*
