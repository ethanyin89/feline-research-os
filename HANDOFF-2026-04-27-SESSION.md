# Handoff Document — 2026-04-27 Session

**Created by:** Claude Opus 4.5
**Timestamp:** 2026-04-27 Asia/Shanghai
**Purpose:** 给下一个模型一份自包含的项目状态读物

---

## Read This First

如果这份文档和旧笔记冲突，以文件系统和这些当前表面为准：

1. `PLAN.md` — 当前计划状态，MVP READY
2. `system/indexes/karpathy-artifact-gap-check.md` — Karpathy 构想差距分析
3. `system/indexes/disease-module-bootstrap-workflow.md` — 疾病模块启动标准流程
4. `topics/*/current-state-dashboard.md` — 各疾病当前状态
5. `HANDOFF-2026-04-24-SESSION.md` — 上次交接文档

这个 repo **不是 git 仓库**。`git` 命令在这里会失败。

---

## 项目定位

这是一个 **Feline Research OS** — 猫科疾病研究知识库系统。

目标是成为 Karpathy 描述的那种 "LLM knowledge base"：
- 原始资料进来 → 快速长成 wiki → 可以不断问 → 会不断沉淀

当前状态：**内核成熟，产品表面待长**

---

## 核心架构

```
raw/papers/src-*.md         # 原始文献 source cards
    ↓ compile
topics/<disease>/           # 疾病主题页 (mechanism, translation, regulatory...)
    ↓ synthesis
outputs/                    # 可交付产物 (briefings, dossiers...)
    ↓ write-back
raw/papers/                 # 沉淀回 source cards
    ↓ health check
system/health-checks/       # 健康报告
```

关键流程：
- `raw → compile → output → write-back → health check`
- Provenance 三级标签：`quoted_fact` / `supported` / `llm_inference`
- 可审计、可追溯

---

## 疾病模块状态

| Disease | Cards | extraction_depth | verification_status | Maturity |
|---------|------:|------------------|---------------------|----------|
| CKD | 24 | full: 24 | deep_extracted: 24 | 成熟 |
| FIP | 24 | full: 24 | deep_extracted: 24 | 成熟 |
| HCM | 24 | full: 24 | deep_extracted: 24 | 成熟 |
| IBD | 24 | full: 24 | deep_extracted: 24 | 成熟 |
| Diabetes | 24 | full: 24 | deep_extracted: 24 | 成熟 |
| FCV | 24 | full: 24 | deep_extracted: 24 | 成熟 |

---

## Ask the Vault 运行状态

### 代码位置
- `scripts/query.py` — CLI 核心
- `scripts/app.py` — Streamlit UI
- `scripts/test_query.py` — 测试套件

### 当前验证
- `68/68` 测试通过 (PLAN.md 记录) 或 `79/79` (HANDOFF-2026-04-24 记录)
- Vision integration 已实现，8 个已验证图片在磁盘上
- OpenRouter 后端可用，稳定配置：`openai/gpt-4.1-mini`

### 运行命令
```bash
cd /Users/jiawei/Desktop/insclaude/feline-research-os
source .venv/bin/activate
export OPENROUTER_API_KEY='your-key'
export OPENROUTER_DAILY_BUDGET_USD=1.00
export OPENROUTER_MODEL='openai/gpt-4.1-mini'
python -m streamlit run scripts/app.py
```

---

## Karpathy 构想差距

详见 `system/indexes/karpathy-artifact-gap-check.md`

### 已经对上的
- 编译骨架：`raw → compile → output → write-back → health`
- source card / topic / entity / synthesis / output 层级
- write-back 沉淀逻辑
- 比普通 AI note 更硬的 trust / audit discipline

### 还需要补的
1. **ask surface** — 让用户从问题进入，不是从导航进入
2. **claim lookup** — "这个结论从哪来"可以直接问
3. **living page cues** — 告诉用户哪些页在持续刷新
4. **query-to-writeback visibility** — 让用户看到问答如何改变系统

核心判断：**内核比表面更成熟**

---

## 关键操作规则

### 1. 疾病增补：按 workflow 静默执行

后续疾病增补**不需要每个疾病都重新确认**流程。

标准流程 (`disease-module-bootstrap-workflow.md`)：
1. Build Disease Shell
2. Build Source Index
3. First-Pass Ingest
4. First Topic Compile
5. Selective Deep Extraction
6. Compiled Compression
7. Post-Bootstrap State Sync

执行方式：
- 直接按 workflow 推进
- 只在遇到歧义/质量太弱/两种互斥组织/需要高成本判断时才问
- 完成后报告结果

### 2. API 成本控制

```
CLAUDE.md 规则：
- 默认使用订阅产品做普通编码/文档
- 只有 Streamlit Ask the vault 或验收需要真实 API
- OpenRouter 需要 $1/day 预算保护
- Anthropic API 需要用户明确批准
```

### 3. 信任文件系统

当旧笔记和当前文件冲突时，以文件系统为准。

---

## 待办优先级

### P0 — 最高价值下一步
1. **处理 downstream recompilation queue**
   - source-card layer 已全部闭合，下一步应同步主题页和输出页状态
2. **做 full-text / image-table / regulatory precision**
   - 仅在具体输出需要更强证据、图表或监管路线时推进

### P1 — 产品表面
3. **清理 ordinary-user output formatting**
   - 去掉原始 provenance tags
   - 内部 footer 语言改成用户友好
   - 答案格式从研究笔记风格改成产品级

### P2 — 系统健康
4. **解决 low-word paper cards** (health 报告标记为 FAIL)
5. **只在 API keys 刻意提供时跑 live acceptance**

---

## 重启路径

### 如果下一个请求是内容继续

从这些文件开始：
- `topics/fcv/current-state-dashboard.md`
- `system/indexes/fcv-source-index.md`
- `system/indexes/fcv-source-depth-map.md`

然后 deep-extract 下一个 FCV anchor，回写到：
- source card
- source depth map
- source index
- owner memo
- current-state-dashboard
- 相关分支页

### 如果下一个请求是运行时/产品

从这些文件开始：
- `system/indexes/ask-the-vault-openrouter-runtime-playbook-20260424.md`
- `scripts/query.py`
- `scripts/app.py`

---

## 验证命令

```bash
cd /Users/jiawei/Desktop/insclaude/feline-research-os
source .venv/bin/activate
python3 scripts/check_markdown_links.py
python3 scripts/test_query.py
python3 scripts/health.py
```

---

## Session Notes

### 本次 session 主要讨论

1. **Karpathy 构想差距分析** — 内核成熟，产品表面待长
2. **疾病增补流程优化** — 后续疾病按 workflow 静默执行，不需要每次确认
3. **接力文档** — 本文档

### 用户明确指出的

> 之前提供的疾病种类，应该是提取过后续增补疾病时候处理方式，并不是每一个疾病都需要重复第一个疾病的确认方式，重复的工作不需要我来反复确认

这意味着：
- 第一个疾病 (CKD) 建立了模式
- 后续疾病应该**静默按 workflow 执行**
- 只有真正需要决策的 edge case 才问用户

---

## 最终读物

项目不在坏掉的状态。它在一个**内核成熟、产品表面待长**的状态：

- 5 个核心疾病模块基本成熟
- FCV 是活跃开发中的第 6 个模块，有 10 个 deep anchors
- Ask the vault 后端路径已调通，产品表面需要后续打磨
- 后续疾病增补应该按 workflow 静默执行

*End of handoff. 下一个模型：先读这份文档，然后继续 Pending 工作或跟随最新用户请求。*
