---
id: system-karpathy-gap-analysis
type: system
topic: operating-system
question_type: gap-map
language: bilingual
last_compiled_at: 2026-04-23
verification_status: human-reviewed
decision_grade: provisional
owner: jiawei
status: active
---

# Karpathy LLM Wiki Gap Analysis

这页只回答一个问题：

`当前 feline research OS 和 Karpathy 的 LLM wiki 构想，差距在哪里，已做什么，还剩什么？`

## Karpathy 原始构想（2026年原推文，逐段核实）

Karpathy 的完整构想分六层：

```
Data ingest  →  raw/ 收源文件（含图片）+ Obsidian Web Clipper 抓网页
Compile      →  LLM 把 raw/ 编译成 .md wiki（summaries + backlinks + concept articles）
IDE          →  Obsidian 作为前端 IDE；LLM 写维护，人不直接动 wiki
Q&A          →  LLM agent 对着 wiki 回答复杂问题；不用 RAG，靠 index files + summaries
Output       →  markdown + Marp slides + matplotlib 图片；输出"file back into wiki"
Linting      →  定期 health check：找不一致、补缺失、找新连接
Extra tools  →  自己 vibe coded 的 naive search engine；既有 web UI，又作为 LLM CLI tool
Future       →  synthetic data + finetuning，把知识从文件压进权重
```

Karpathy 收尾语：**"I think there is room here for an incredible new product instead of a hacky collection of scripts."**

---

## 差距矩阵（2026-04-22 更新）

| Karpathy 层 | 当前状态 | 差距 | 优先级 |
|------------|---------|------|--------|
| **Data ingest — 文字** | `raw/papers/`, `raw/regulations/` 在用；134 source cards（120 paper + 14 regulation），覆盖 5 病种 | 原始 PDF / web clipper 自动化仍弱，很多 source card 是手工/LLM 管理后的卡片，不是完整 source-file archive | **MEDIUM** |
| **Data ingest — 图片** | CKD 有 8 张已验证非 `candidate-*` 图片/表格资产，完整 figure_type 命名规范，vision pipeline 可用 | FIP/HCM/IBD/Diabetes 图片仍主要是 `candidate-*` reference；`src-ckd-013` 仍有 source-access blocker | **MEDIUM** |
| **Compile** | `topics/`, `entities/` 已有；93 topic pages；`scripts/compile_trigger.py` 可检测变更并输出 recompile queue | 触发器已建，但还不是 Obsidian / git hook / cron 的日常自动闭环 | **MEDIUM** |
| **Source card 密度** | 120 paper cards 都有 `extraction_depth`；CKD / FIP / HCM / IBD / Diabetes 各 24 full | 普通 source-card thickening 完成；下一步是 full-text / official-source / image-table precision，而不是补卡 | **MEDIUM** |
| **IDE — Obsidian** | 本地已在用 Obsidian | 对齐 | — |
| **Q&A — query loop** | `query.py` + routing + hops + vision + provenance badges + figure_type routing + search pre-heat；Streamlit UI 可用 | 真实在线使用依赖 API key；旧 Mac 不适合本地 Ollama，UI 已改为 API-first；Cloudflare/remote inference 尚未接入 | **HIGH** |
| **Q&A — search tool** | `scripts/search.py` 可独立 CLI 使用，也可被 query.py import 做 pre-filter | ✅ **刚完成（2026-04-18）** | — |
| **Q&A — LLM tool (MCP)** | `scripts/mcp_server.py` 暴露 vault_search / compile_check / source_list | 完整 route+hop+synthesize 还没作为稳定 MCP tool 暴露；需要 API key 和运行时验收 | **MEDIUM** |
| **Output — 文字/slides** | briefings、dossiers、Marp slides 已有 | 对齐，但输出 promote 回 topics 的人工习惯还没有稳定节奏 | **LOW** |
| **Output — matplotlib 图** | `scripts/charts.py` 生成 endpoint-radar / source-coverage / maturity-bar，输出 `outputs/figures/` | ✅ **刚完成（2026-04-18）** | — |
| **Output — write-back 闭合** | `--write-back` → `outputs/qa/`；`--save-to-inbox` → `inbox/{disease}/` 供人工 review | ✅ **inbox 流量刚接通（2026-04-18）** | **LOW**（需要建立 promote 习惯） |
| **Linting** | `linting-schedule.md` + `run_acceptance_checklist.py` + `check_markdown_links.py` | 定义完整但没有 cron / CI 执行 | **MEDIUM** |
| **Staging layer** | `inbox/` 目录完整；`--save-to-inbox` flag 可用 | 闸门已建，流程已通 | — |
| **Knowledge integrity** | `conflict-register.md`、`unresolved-questions.md`、source-depth map、link checker、provenance checks 都在用 | 缺少一键 health dashboard / scheduled checks；外部论文逐句复核仍是人工任务 | **HIGH** |
| **Future — finetuning** | 无 | 远期 | LOW |

## 2026-04-21 delta

- Source base now reflects 5 diseases: CKD, FIP, HCM, IBD, Diabetes.
- Source count is 134 cards: 120 papers + 14 regulations.
- Topic pages are 83, not the older 74-page snapshot.
- Source-depth maps and disease dashboards now expose `verification_status` separately from `extraction_depth`, so `abstract_weighted` cards are no longer hidden behind `full` source-card depth.
- Query UI is now API-first. Anthropic and OpenRouter are the normal user paths; local Ollama is hidden unless `ENABLE_OLLAMA=true`.
- This is the right call for a MacBook Pro 15-inch 2017 class machine: local LLM UX is likely to be the bottleneck, not the vault architecture.
- Cloudflare or another remote inference backend remains a real gap, not implemented yet.

---

## 2026-04-11 本次 session 完成内容

本次由 gstack `/office-hours` + `/plan-eng-review` 联合执行。以下文件为今天新建或更新：

### 新建文件

| 文件 | 作用 |
|------|------|
| `system/indexes/source-depth-map.md` | 120 张 paper source cards 跨病种深度地图；CKD / FIP / HCM / IBD / Diabetes 各 24 full；下一步转向 full-text / official-source / image-table precision |
| `system/protocols/ai-content-workflow.md` | inbox/ staging 流程；AI 草稿 → 人工确认 → promote 到 topics/ 或 entities/ |
| `system/health-checks/linting-schedule.md` | 两触发器：每批深挖后 + 每月一次；报告命名规范 |
| `system/indexes/karpathy-gap-analysis.md` | 本文件 |

### 更新文件

| 文件 | 更新内容 |
|------|---------|
| `system/indexes/question-router.md` | 新增 Section 9：路由到 source-depth-map / conflict-register（待建）/ unresolved-questions（待建）；28/28 测试通过 |

### 建立目录

```
inbox/ckd/
inbox/fip/
inbox/hcm/
inbox/ibd/
inbox/entities/
inbox/rejected/
```

---

## 2026-04-18 session 完成内容

### 新建文件

| 文件 | 作用 |
|------|------|
| `scripts/search.py` | 全文搜索工具；支持 regex、scope 过滤、LLM context 格式输出；填补 Karpathy "extra tools — naive search engine" |
| `requirements.txt` | Python 依赖声明 |
| `.env.example` | API key 模板 |

### 更新文件

| 文件 | 更新内容 |
|------|---------|
| `scripts/query.py` | +search pre-heat（routing 后自动搜索相关 source cards）、+`--save-to-inbox` flag（write-back → inbox 流量）、+figure_type filter/sort、+media_type from extension、+dead code cleanup |
| `scripts/test_query.py` | 54 → 63 tests；新增 search/inbox/figure_type/media_type 测试 |
| `README.md` | 安装说明、provenance badge 解释、search.py 用法 |
| 5 张 CKD 图片 | 重命名为语义 figure_type 命名规范 |
| 5 张 source cards | local_assets 同步更新 |
| `system/indexes/karpathy-gap-analysis.md` | 本次更新 |

### 关键进展

- **图片层** 从 0 → 8 张已验证图片，vision pipeline 完整可用
- **搜索层** 从无 → `search.py` 可独立使用也可被 query.py 自动调用
- **write-back 层** 从断开 → `--save-to-inbox` 接通 inbox 流量
- **测试** 从 28 → 63 tests，全部 pass
- **内容完整性** 40 张 source cards 审计完成，0 fake data

---

### 关键进展（第二轮，同日）

- **auto-compile trigger** → `scripts/compile_trigger.py`，检测 source card 变更后找到所有下游需要 recompile 的文件（支持 git diff / --since N / --sources 三种模式）
- **conflict-register** 从 5 → 13 条 tension，覆盖 19 张 source cards（全 24 张 deep-extraction files 审阅完成）
- **MCP server** → `scripts/mcp_server.py`，暴露 vault_search / compile_check / source_list 三个工具，MCP over stdio JSON-RPC
- **matplotlib 图表** → `scripts/charts.py`，三种图表：endpoint-radar / source-coverage / maturity-bar，输出到 `outputs/figures/`
- **测试** 67/67 pass

---

## 仍有差距的功能

| 项目 | 说明 | 优先级 |
|------|------|--------|
| API-first runtime | UI 已改为 Anthropic/OpenRouter 优先；Ollama 默认隐藏 | 需要完成 API key 配置、OpenRouter live acceptance、后续 Cloudflare/remote inference backend 选择 | HIGH |
| linting cron / CI | 定义完整，手动检查可跑 | 没有实际自动执行；health checks 还不是日常保护网 | HIGH |
| non-CKD source densification | 120 paper cards 都有 depth 字段，worksheet 层完整；FIP / HCM / IBD / Diabetes 都已达 24/24 explicit full and deep_extracted；`src-ibd-009` 现在是 deep-extracted workflow support 但非 decision-grade | 下一步是 full-text / official-source / image-table / output-specific precision，不是普通 source-card thickening | MEDIUM |
| FIP/HCM/IBD/Diabetes images | CKD 已有 8 个 verified assets | 其他病种仍主要停在 `candidate-*` references；不能进入 vision pipeline | MEDIUM |
| vault_query MCP tool | `mcp_server.py` 暴露 search / compile / source list | 完整 route+hop+synthesize 尚未作为稳定 MCP tool 暴露 | MEDIUM |
| auto-compile 自动执行 | `compile_trigger.py` 存在 | 需要 git hook / cron / Obsidian workflow 实际触发 | MEDIUM |

---

## 最高优先级：Current Gap Queue

来自 `system/indexes/source-depth-map.md` 的 2026-04-21 现实：

1. **API-first live acceptance**
   - 配置 `ANTHROPIC_API_KEY` 或 `OPENROUTER_API_KEY`
   - 跑 `scripts/run_acceptance_checklist.py --backend openrouter` 或 Anthropic 等价路径
   - 目标不是“能回答”，而是 8 个核心问题里至少 6 个 answer surface 可接受，0 fake source id

2. **Remote inference backend decision**
   - 旧 MacBook Pro 不适合把 Ollama 当普通用户路径
   - 当前 UI 已把 Ollama 默认隐藏，只保留 Anthropic / OpenRouter
   - 下一步可以评估 Cloudflare Workers AI 或其他 remote OpenAI-compatible backend，但这需要新 backend adapter 和 live acceptance

3. **Non-CKD densification**
   - CKD 不再是 bootstrap 队列
   - FIP / HCM / IBD / Diabetes：24/24 source cards 已 full；`src-ibd-009` 仍应作为 workflow support 使用，不应升级成 decision-grade diagnosis
   - 下一步只在 full-text / official-source / image-table / output pressure 改变判断时继续加厚

4. **Image verification beyond CKD**
   - 保留 `candidate-*` gate
   - 只在打开原文并核对 figure/table label 后去掉 `candidate-*`
   - 不允许 AI 生成图或猜 figure 编号

5. **Scheduled health checks**
   - 当前手动检查已经能跑：link check、query tests、provenance/source id audit
   - Karpathy 构想里的 linting 是持续机制，不是偶尔手工跑一次

---

## 主要差距体现在哪里 / How the Gaps Show Up

### 1. Runtime gap: 有 wiki，但还没有稳定的日常问答后端

**体现在哪里：**

- Streamlit UI 能打开，`query.py` 能跑，但真实问答依赖 `ANTHROPIC_API_KEY` / `OPENROUTER_API_KEY`
- 旧 MacBook Pro 不适合把 Ollama 当普通用户默认路径
- Cloudflare / Workers AI / 其他 remote inference backend 还没有接入
- `scripts/run_acceptance_checklist.py` 已有，并且现在会把缺 key 明确写成 `blocked-missing-key`；当前最新报告不是 template-only，而是等待真实 API key

**为什么重要：**

Karpathy 构想里，Q&A 是 wiki 变成产品的地方。现在知识层已经接近可用，根目录 `start.md` 也已经改成 ask-first 入口；剩下的最后一公里是用真实 API key 跑完 live acceptance。

**处理方式：**

1. 先选一个主后端，不要同时追 3 条路。当前建议：OpenRouter 作为低摩擦主路径，Anthropic 作为高质量路径。
2. 配好 key 后跑：
   ```bash
   python3 scripts/run_acceptance_checklist.py --backend openrouter
   ```
3. 只有 8 个核心问题达到 acceptance，再把该 backend 写成 README 的默认推荐。
4. Cloudflare 作为第二阶段：先写 adapter，再跑同一套 acceptance，不要先改 UI。

### 2. Compile gap: 有编译产物，但自动 recompile 还没有成为习惯

**体现在哪里：**

- `topics/` 已有 93 个 topic pages
- `scripts/compile_trigger.py` 能找 downstream recompile queue
- 但它没有接到 git hook、cron、Obsidian command 或日常 checklist
- source card 变动后，哪些 topic 必须刷新，仍依赖操作者记得跑脚本

**为什么重要：**

Karpathy 的 wiki 不是静态笔记。raw 变了，上层 wiki 应该被重新编译。现在系统能告诉你“该重编什么”，但还不会自动提醒。

**处理方式：**

1. 加一个非破坏性 health command，把 link check、test_query、compile trigger 统一成一个入口。
2. 每次 source card 改动后跑：
   ```bash
   python3 scripts/compile_trigger.py --since 1
   ```
3. 稳定后再接 git hook 或 launchd，不急着上 CI。

### 3. Evidence-depth gap: CKD 是成熟模板，其他病种还没有同等厚度

**体现在哪里：**

- CKD: 24/24 `extraction_depth: full`
- FIP: 24/24 `extraction_depth: full`
- HCM: 24/24 `extraction_depth: full`
- IBD: 24/24 `extraction_depth: full`; 24/24 `deep_extracted`; `src-ibd-009` is workflow support, not decision-grade diagnosis
- Diabetes: 24/24 `extraction_depth: full`
- 所有 120 个 paper source card 都已从 worksheet 层回写到 full source-card depth

**为什么重要：**

Q&A 的质量上限不是模型，而是可加载证据的厚度。现在 source-card 厚度这一层已经打平，下一层瓶颈变成 full-text、官方来源、图片/表格和输出特定精度。

**处理方式：**

1. 不要重做所有 worksheet。
2. 不要再做普通 source-card thickening。
3. 只在具体输出或 branch-order 需要时做 full-text / official-source / image-table precision。
4. 每次 precision pass 都要同步 source-depth map、dashboard、synthesis 和 health checks。

### 4. Image gap: 图片机制已通，但内容资产只完成 CKD pilot

**体现在哪里：**

- `raw/images/ckd/` 有 8 个 verified assets
- FIP / HCM / IBD / Diabetes 现在各至少有 1 个 verified asset，已从“只有 README / candidate refs”推进到跨病种 pipeline proof
- source-card `links.local_assets` 已清掉未验证 `candidate-*` 路径；候选目标保留在 image manifest / TODO，不进入 query / vision 可用资产层
- 剩余问题是图像资产深度还不均衡，不是 pipeline 不通

**为什么重要：**

Karpathy 特别强调 markdown + images。医学/兽医研究里，机制图、病理图、endpoint 表格经常比文字摘要更能决定理解质量。

**处理方式：**

1. 保持硬规则：没有核对 article figure/table label，就不去掉 `candidate-*`。
2. 下一轮每个非 CKD 病种再补 1 篇 source 的图片 pilot，不要一次做完全部。
3. 优先抓机制图、diagnostic/workup table、endpoint/outcome table。
4. 每次新增图片后跑 local asset audit 和 query tests。

### 5. Write-back gap: 输出已经会产生，但沉淀回 wiki 还靠人工节奏

**体现在哪里：**

- `outputs/` 有 briefing、dossier、slides、figures
- `--save-to-inbox` 已经接通
- 当前 `inbox/` 基本清空，只剩 `.gitkeep` 和一个 rejected nested-path audit note
- `ai-content-workflow.md` 定义了 promote/reject，但没有固定批处理节奏

**为什么重要：**

Karpathy 的关键不是“问答”，而是每次探索都 add up。现在能 add，但还没有形成稳定复利。

**处理方式：**

1. 每次 session 结束前看一次：
   ```bash
   find inbox -maxdepth 3 -type f | sort
   ```
2. inbox 文件只允许三种结局：promote、reject、keep with explicit blocker。
3. 高价值 Q&A 不直接写 topics，先进 inbox，spot-check 2-3 个 claims 后再 promote。

### 6. Health-check gap: 有检查脚本，但还不是“知识库免疫系统”

**体现在哪里：**

- `scripts/test_query.py` 68/68
- `scripts/check_markdown_links.py` 能查 616 个 markdown links
- provenance/source-id audit 可以手动跑
- `scripts/health.py` 现在已经把 link、query tests、source ids、source schema gate、decision-grade gate、candidate image gate、acceptance status、compile drift、inbox backlog、API key presence 汇总成单个 report
- 但还没有 cron / CI / Obsidian alert；health checks 仍需要人工主动运行

**为什么重要：**

知识库会腐烂。文件越多，越需要自动发现旧状态、坏链接、证据越权、未清 inbox。

**处理方式：**

1. 先用 `python3 scripts/health.py` 作为 end-of-session health command。
2. 它会输出 `system/health-checks/health-report-YYYYMMDD.md`。
3. 第一版已经只聚合现有检查，不写新智能：
   - markdown links
   - query tests
   - source id uniqueness
   - provenance tags
   - image refs / candidate leakage
   - inbox backlog
   - acceptance report status
4. 稳定后再接 launchd/cron。

---

## 图片 pipeline（独立任务，不依赖上面）

Karpathy 明确把图片作为 ingest 一级素材。当前 `raw/images/ckd/` 已有 8 个 verified assets；FIP/HCM/IBD/Diabetes 各有 1 个 first-pass verified asset。source-card `local_assets` 已不再保留未验证 `candidate-*` 路径；candidate 目标只应留在 manifests/TODOs。

操作方法：
1. 下次用 Obsidian Web Clipper 抓论文时，把图片一起存到 `raw/images/<disease>/`
2. 打开原文核对 figure/table label
3. 对应 source card 添加 frontmatter 字段，例如已验证文件：`local_assets: [raw/images/ckd/src-ckd-001-mechanism-schematic.jpg]`
4. 没有核对前保持 `candidate-*`

不需要新架构，只需要执行习惯改变。

---

## Write-Back 闭合（独立任务）

Karpathy 说 outputs "file back into the wiki"，不是堆在独立目录。

当前状态：`--write-back` 写到 `outputs/qa/`。

正确路径：
- 经过验证的 Q&A 结论 → `inbox/<disease>/` → 人工审查 → promote 到 `topics/`
- 现在 `ai-content-workflow.md` 已经定义了这个流程
- 执行层面：只需要形成习惯，不需要改代码

---

## 关键约束（每次交给新模型前必须传达）

```
1. 不用 RAG / 向量检索。专科兽医词汇会破坏余弦相似度，架构决策已锁定。
2. 路由机制：query.py → question-router.md → topic pages + source cards。
3. 三层证据标签必须保留：[quoted_fact] / [source_supported_conclusion] / [llm_inference]
4. Obsidian 是本地 IDE，所有文件在本地文件系统。
5. 测试套件：python3 scripts/test_query.py（68/68 pass 为 2026-04-21 基线）。
6. AI 写的 wiki 页面先进 inbox/，人工确认后 promote——见 system/protocols/ai-content-workflow.md
7. 普通用户 runtime 走 API-first。Ollama 只在 `ENABLE_OLLAMA=true` 时作为显式本地测试路径。
```
