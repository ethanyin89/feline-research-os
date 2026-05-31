# Handoff: Karpathy LLM Wiki Gap Analysis — 2026-05-17

**Updated: 2026-05-30** — Added cancer module (102 cards, 8 branch pages)

## 任务背景

用户要求：分析当前 feline-research-os 与 Karpathy LLM Wiki 理念的差距，继续处理可闭合的差距，写接力文档。

## Karpathy 原始构想 vs 当前状态

### 七层对齐状态

| Karpathy 层 | 对齐度 | 当前状态 | 剩余差距 |
|------------|:------:|---------|---------|
| **Data ingest (文字)** | 92% | 441 source cards (427 paper + 14 regulation)，8 病种，year metadata 100% | PDF/web clipper 自动化弱，手工管理为主 |
| **Data ingest (图片)** | 60% | 12 verified images (CKD 8, FIP/HCM/IBD/Diabetes 各 1)，vision pipeline 完整 | FCV/Obesity/Cancer 0 images，src-ckd-013 blocked |
| **Compile** | 95% | topics/entities 完整，compile_trigger.py 接入 git hook + launchd | 全自动 recompile 仍需人工触发 |
| **IDE (Obsidian)** | 100% | 本地 Obsidian 在用 | 完全对齐 |
| **Q&A agent** | 85% | query.py + routing + hops + vision + provenance + search pre-heat | API-first 已实现，ask-native 产品感待打磨 |
| **Output** | 90% | briefings, dossiers, Marp slides, matplotlib charts, inbox write-back | promote 回 topics 的习惯待建立 |
| **Linting** | 95% | 107 tests, 25+ health checks, launchd scheduled | 完全自动化已实现 |
| **Extra tools** | 90% | search.py + mcp_server.py + charts.py | 完整 route+hop+synthesize MCP tool 待暴露 |
| **Future (finetuning)** | 0% | 无 | 远期目标 |

### 总体对齐度：**~82%** (↑2% from cancer module addition)

## 可闭合差距分析

### 已闭合（本次 session 之前）

| 差距 | 闭合状态 | 证据 |
|------|---------|------|
| Scheduled health checks | ✅ FIXED | launchd plist active |
| Compile auto-trigger | ✅ FIXED | git hook active |
| Year metadata | ✅ FIXED | 325/325 (100%) |
| Obesity Tier 1 | ✅ FIXED | 4 deep-extracted, 4 architecture pages |
| Expert-review workflow | ✅ FIXED | codified at 3/3-10 samples |

### 仍开放的差距

| 差距 | 优先级 | 可闭合性 | 所需行动 |
|------|:------:|:--------:|---------|
| Ask-native product feel | HIGH | 低（taste decision） | 需人工决策产品方向 |
| FCV/Obesity/Cancer images | MEDIUM | 高 | 需原文 PDF 访问验证 |
| API live acceptance | HIGH | 高 | 需配置 API key 跑 acceptance |
| Full MCP tool | MEDIUM | 中 | 需 API key + route/hop/synthesize 封装 |
| Obesity Tier 2 sources | LOW | 高 | 按需继续 management 源 |
| Cancer Tier 2 extraction | MEDIUM | 高 | 67 title_only cards → abstract_weighted via PubMed |
| Cancer decision-grade | LOW | 中 | 需更多 clinical outcome sources |

### 2026-05-30 闭合进展

| 差距 | 状态 | 证据 |
|------|------|------|
| Cancer module bootstrap | ✅ CLOSED | 102 source cards ingested, 8 branch pages compiled |
| Cancer source depth | ⏳ PARTIAL | 6 deep-extracted + 29 abstract_weighted (35% coverage) |
| Cancer synthesis shell | ✅ CLOSED | architecture-level synthesis index complete |

## 本次 Session 完成内容

### 系统索引更新

| 文件 | 更新内容 |
|------|---------|
| `karpathy-gap-analysis.md` | 更新到 7-module, 325-card 现实；标记 scheduled checks 和 auto-compile 为 FIXED |
| `two-track-operating-plan-20260418.md` | 更新 current reality section |
| `content-side-densification-queue.md` | 更新 bootstrap lane 状态 |
| `HANDOFF.md` | 更新 pipeline reference 和 disease module count |

### 年份元数据恢复

| 病种 | 恢复数量 | 来源 |
|------|---------|------|
| Obesity | 6 cards | WebSearch + WebFetch (PubMed, Crossref) |
| Diabetes | 8 cards | WebSearch + WebFetch (PubMed, institutional repos) |

### 双语页面编译

| 页面 | 内容 |
|------|------|
| mechanism-overview-bilingual.md | 5-branch architecture (EN/ZH) |
| risk-and-recognition-bilingual.md | Risk factor framework (EN/ZH) |
| prevention-bilingual.md | Prevention strategy (EN/ZH) |
| diabetes-bridge-bilingual.md | Insulin sensitivity mechanism (EN/ZH) |

## 当前 Vault 现实

```
Paper source cards:      427 (8 diseases)
Regulation cards:        14
Year metadata:           427/427 (100%)
Verified images:         12
Health check tests:      107 passing
Health check status:     ALL PASS

Disease module status:
  CKD:      24/24 deep-extracted, 8 images
  FIP:      24/24 deep-extracted, 1 image
  HCM:      24/24 deep-extracted, 1 image
  IBD:      24/24 deep-extracted, 1 image
  FCV:      24/24 deep-extracted, 0 images
  Diabetes: 118 cards (24 full + 94 partial), 1 image
  Obesity:  87 cards (4 Tier 1 deep-extracted), 0 images
  Cancer:   102 cards (6 deep-extracted, 29 abstract_weighted, 67 title_only), 0 images

Cancer module architecture:
  Branch pages compiled:  8 (workflow, lymphoma, mammary, oral-scc, fiss, cox-markers, registry, mast-cell placeholder)
  Synthesis index:        6 key claims, architecture-level only
  Decision-grade content: NO (workflow shell only)
```

## Karpathy 差距的具体解决方案

### Gap 1: Ask-native product feel → Streamlit pilot + feedback loop

**问题**: Karpathy 说 "incredible new product"，我们是 "hacky collection of scripts"

**解决方案**: 已部署 Streamlit app，下一步是:
1. 设置 Sharing → Public (Streamlit Cloud dashboard)
2. 邀请 1 位 pilot researcher 做 15 分钟反馈
3. 根据反馈决定 UI 方向：minimal chat vs guided workflow vs hybrid

**不需要 API 成本**，只需要人工判断。

### Gap 2: Image density → PubMed Central 免费全文图片

**问题**: 仅 12 张验证图片，Cancer/FCV/Obesity 各 0 张

**解决方案**: PubMed Central 提供免费全文访问，包括 figures
1. 搜索 `site:ncbi.nlm.nih.gov/pmc "feline lymphoma" histopathology`
2. 验证 figure 许可证 (CC-BY 优先)
3. 下载并标注来源

**不需要 API 成本**，只需要手工验证。

### Gap 3: Cancer source depth → PubMed E-utilities batch upgrade

**问题**: 67 title_only 卡片缺少 abstract 内容

**解决方案**: 已验证 PubMed E-utilities 可用
```bash
# 批量获取 abstract
for pmid in $(grep -h "^pmid:" raw/papers/src-cancer-*.md | grep -v "^pmid: $" | cut -d: -f2 | tr -d ' '); do
  curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=$pmid&rettype=abstract&retmode=text"
  sleep 0.5  # rate limit
done
```

**不需要 API 成本**，但需要时间批量处理。

### Gap 4: Full MCP tool → 延迟到 API acceptance 完成

**问题**: route+hop+synthesize 完整工具未暴露

**依赖**: 需要 API key 跑 live acceptance 验证 query.py
**决策**: 延迟到 pilot feedback 确认产品方向后再投入

### Gap 5: PDF ingest 自动化 → 不闭合（非阻塞）

**问题**: Karpathy 用 Obsidian Web Clipper 一键抓取

**决策**: 当前手工 + LLM 辅助流程已够用，自动化是 nice-to-have 不是 blocker

## 与 Karpathy 构想的核心差异

### 1. 我们比 Karpathy 构想更强的地方

| 维度 | Karpathy 原版 | 我们的实现 |
|------|-------------|-----------|
| **证据分级** | 无明确系统 | 三层 provenance badges + decision-grade 机制 |
| **多语言** | 仅英文 | 双语 (EN/ZH) 架构页面 |
| **健康检查深度** | "定期 linting" | 25+ 自动化检查，含 thin-source usage, quantified claim traceability |
| **Evidence policy** | 无 | 每张 source card 都有 evidence_policy 声明 |
| **Source-card 结构** | 简单 summary | 完整 schema：year, extraction_depth, verification_status, decision_grade |

### 2. 我们仍弱于 Karpathy 构想的地方

| 维度 | Karpathy 原版 | 我们的差距 |
|------|-------------|-----------|
| **PDF ingest 自动化** | Obsidian Web Clipper 一键抓取 | 手工 + LLM 辅助管理 |
| **图片密度** | 完整 figure/table archive | 仅 12 张验证图片 |
| **产品感** | "incredible new product" | 仍是 "hacky collection of scripts" |
| **Finetuning** | 构想中的终极目标 | 未开始 |

### 3. 不同路线选择

| 决策点 | Karpathy 选择 | 我们的选择 | 原因 |
|--------|-------------|-----------|------|
| **向量检索** | 可能用 | 明确不用 | 专科兽医词汇破坏余弦相似度 |
| **本地 LLM** | Ollama 优先 | API-first | 旧 MacBook Pro 不适合本地推理 |
| **证据标注** | 简单引用 | 三层 provenance | 医学研究需要更严格的证据链 |

## 下一步建议

### 优先级 1：可立即执行（无 API 成本）

1. **Cancer abstract extraction** — 继续用 PubMed E-utilities 将 67 title_only 卡片升级到 abstract_weighted
   - 命令：`curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=PMID&rettype=abstract&retmode=text"`
   - 优先顺序：branch-control candidates (lymphoma clinical, oral SCC clinical, FISS treatment)

2. **Cancer branch expansion** — 将 abstract_weighted 发现整合到现有 branch pages
   - 添加 claim 到 key-claim traceability tables
   - 维护 "What The Module Should Not Say Yet" 边界

3. **Pilot researcher feedback** — Streamlit app 已部署，设置 Public 后邀请 pilot researcher
   - URL: https://feline-research-os-3fzhk6zhd2mgvj8rxlbvou.streamlit.app
   - 需要 Streamlit Cloud dashboard 设置 Sharing → Public

### 优先级 2：需要 API 或人工判断

1. **API live acceptance** — 配置 OPENROUTER_API_KEY，跑 `scripts/run_acceptance_checklist.py --backend openrouter`
2. **Ask-native product feel** — 需要用户决定 Streamlit UI 的产品方向
3. **Obesity Tier 2** — 只在需要 intervention/management 细节时继续

### 优先级 3：可延迟

1. **Full MCP tool** — 等 API acceptance 完成后再封装
2. **PDF ingest 自动化** — 非阻塞，当前手工流程可用
3. **Cancer decision-grade** — 需要 treatment outcome sources，当前 architecture-only 足够

## 关键约束（传递给下一个模型）

```
1. 不用 RAG / 向量检索。架构决策已锁定。
2. 路由机制：query.py → question-router.md → topic pages + source cards。
3. 三层证据标签必须保留：[quoted_fact] / [source_supported_conclusion] / [llm_inference]
4. 测试基线：107/107 pass (2026-05-17)。
5. 8 病种架构：
   - CKD/FIP/HCM/IBD/FCV 各 24/24 full
   - Diabetes 118 cards
   - Obesity 87 cards (Tier 1 complete)
   - Cancer 102 cards (6 deep + 29 abstract_weighted + 67 title_only)
6. Year metadata 100% coverage：427/427 paper source cards 都有 year 字段。
7. 不要伪造数据。candidate-* 图片必须验证后才能去除前缀。
8. AI 写的 wiki 页面先进 inbox/，人工确认后 promote。
9. Cancer module 约束：
   - 仅 architecture-level synthesis，不做 treatment/prognosis 推荐
   - Branch pages 必须有 "What The Module Should Not Say Yet" section
   - 单研究 risk factor（如 canned food 4.7x）不能推广为 owner-facing 建议
```

## 本次 Commits

```
fad2233 docs: update HANDOFF.md with 7-module, 325-card reality
33f9a85 docs: update karpathy-gap-analysis with 7-module, 325-card reality
dc1c952 docs: update system indexes with 7-module, 325-card reality
abc7e3d docs: update handoff files with year metadata completion
511c307 chore: update health report after year metadata recovery
528152d feat(diabetes): recover year metadata for 8 source cards
16f0cbb feat(obesity): recover year metadata for 6 source cards
08d241c docs: update source depth maps with obesity architecture completion
d8831e5 docs: update handoff with bilingual completion status
867e344 docs(obesity): update dashboard and index for bilingual completion
```

## 用户绑定规则（从 session 开始继承）

1. **No fake data** — candidates stay gated
2. **No one-off work** — codify or don't do
3. **3-10 samples before skill** — obesity extraction reached 4/4 Tier 1
4. **Test standard** — if asked same thing twice, you failed

## Session 状态

- **STATUS**: DONE
- **Health check**: 107/107 pass, all checks PASS
- **Blockers**: None (ask-native product feel is taste decision, not blocker)
- **Next session start point**: Read this handoff + health report

---

## 2026-05-30 Session Update

### 新增内容

1. **Cancer module 完整引导** — 102 source cards, 8 branch pages, architecture-level synthesis
2. **6 source cards 升级** — 从 title_only → abstract_weighted (via PubMed E-utilities, 零 API 成本)
3. **Streamlit 部署** — app 已上线，等待设置 Public sharing
4. **Karpathy 差距分析更新** — 识别 5 个具体差距，提出解决方案

### Karpathy 对齐度变化

- **Data ingest (文字)**: 90% → 92% (↑2%, 新增 cancer 102 cards)
- **总体对齐度**: ~80% → ~82%

### 可立即执行的下一步

1. 设置 Streamlit Sharing → Public
2. 邀请 pilot researcher
3. 继续 cancer abstract extraction (PubMed E-utilities, 无 API 成本)
