# Handoff Document — 2026-04-30 Session

**Created by:** Claude Opus 4.5
**Timestamp:** 2026-04-30 Asia/Shanghai
**Purpose:** 给下一个模型一份自包含的项目状态读物

---

## Read This First

如果这份文档和旧笔记冲突，以文件系统和这些当前表面为准：

1. `PLAN.md` — 当前计划状态，MVP READY
2. `topics/fcv/current-state-dashboard.md` — FCV 当前状态（刚完成重编译）
3. `system/health-checks/health-report-20260430.md` — 今日健康报告
4. `HANDOFF-2026-04-27-SESSION.md` — 上次交接文档

这个 repo **不是 git 仓库**。`git` 命令在这里会失败。

---

## 项目定位

这是一个 **Feline Research OS** — 猫科疾病研究知识库系统。

目标是成为 Karpathy 描述的那种 "LLM knowledge base"：
- 原始资料进来 → 快速长成 wiki → 可以不断问 → 会不断沉淀

当前状态：**6 个疾病模块成熟，全部 24/24 deep-extracted**

---

## 本次 Session 完成的工作

### FCV 主题页重编译 (P0 工作)

将 FCV 核心主题页从 "routing page" 升级为 "handbook" 状态：

1. **mechanism-overview.md** — 完成
   - 添加 4 层机制层级结构 (diversity → receptor/tropism → persistence → pathotype)
   - 添加 source-layer reality 表格
   - confidence 从 low 提升到 medium

2. **risk-and-recognition.md** — 完成
   - 添加完整 recognition architecture 结构
   - 添加 PCR-best-but-bounded 诊断逻辑
   - 添加 carrier state, co-pathogen, regional strain 考量
   - confidence 从 low 提升到 medium

3. **endpoint-handbook.md** — 完成
   - 添加 8 个 endpoint 家族分层结构
   - 添加 therapy 分支 (src-fcv-008, src-fcv-014, src-fcv-018)
   - 添加 source-layer reality 表格
   - confidence 从 low 提升到 medium

4. **辅助更新**
   - current-state-dashboard.md — 标记重编译完成
   - synthesis-index.md — 更新编译日期和状态
   - translation-brief.md — 添加 src-fcv-001, 更新 current role
   - fcv-source-depth-map.md — 更新 next moves 标记已完成工作

### HCM 主题页重编译 (P0 工作续)

1. **mechanism-overview.md** — 完成
   - 添加 4 层机制层级结构 (genetics → phenotype → remodeling → end-stage)
   - 添加 Key-Claim Traceability 表格 (5 条)
   - 添加 source-layer reality 表格
   - 整合已有的 genotype-severity memo 和 phenotype-remodeling bridge memo
   - confidence 从 low 提升到 medium

2. **current-state-dashboard.md** — 更新
   - 标记 mechanism-overview 重编译完成
   - confidence 从 low 提升到 medium

### 系统状态验证

- 健康检查全部通过 (2026-04-30)
- 766 个 markdown 文件无链接问题
- 84/84 测试通过

---

## 六个疾病模块状态

| Disease | Cards | extraction_depth | verification_status | Topic Page Status |
|---------|------:|------------------|---------------------|-------------------|
| CKD | 24 | full: 24 | deep_extracted: 24 | 成熟 |
| FIP | 24 | full: 24 | deep_extracted: 24 | 成熟 |
| HCM | 24 | full: 24 | deep_extracted: 24 | 成熟 |
| IBD | 24 | full: 24 | deep_extracted: 24 | 成熟 |
| Diabetes | 24 | full: 24 | deep_extracted: 24 | 成熟 |
| FCV | 24 | full: 24 | deep_extracted: 24 | **本次重编译完成** |

---

## 图片资产状态

| Disease | Verified images | Candidate refs |
|---|---:|---:|
| CKD | 8 | 0 |
| FIP | 1 | 0 |
| HCM | 1 | 0 |
| IBD | 1 | 0 |
| Diabetes | 1 | 0 |
| FCV | 0 | 0 |

FCV 图片资产为 0 — 需要 PDF 图像提取工作。

---

## 待办优先级

### P0 — 刚完成
- ✅ FCV 核心主题页重编译 (mechanism, recognition, endpoint)

### P1 — 下一步内容工作
1. **其他疾病模块主题页核查** — 检查 CKD, FIP, HCM, IBD, Diabetes 的主题页是否需要类似重编译
2. **FCV translation-brief 和 regulatory-brief 更新** — 使其与重编译后的 handbook 页面保持一致

### P2 — 产品表面
1. **清理 ordinary-user output formatting**
   - 去掉原始 provenance tags
   - 内部 footer 语言改成用户友好
   - 答案格式从研究笔记风格改成产品级

### P3 — 系统健康
1. **图片资产扩展** — FCV 0/24, 其他疾病 1/24 或 8/24
2. **Ask the Vault 产品打磨**

---

## 关键操作规则

### 1. 疾病增补/维护：按 workflow 静默执行

后续工作**不需要每个任务都重新确认**流程。

标准流程：
1. 识别需要更新的页面
2. 读取相关源卡和 memo
3. 执行更新
4. 更新 dashboard 和 depth-map
5. 验证健康检查

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

## 重启路径

### 如果下一个请求是继续内容工作

从这些文件开始：
- `topics/fcv/current-state-dashboard.md` — FCV 最新状态
- `topics/ckd/current-state-dashboard.md` — 检查 CKD 是否需要类似更新
- `topics/fip/current-state-dashboard.md` — 检查 FIP 是否需要类似更新

### 如果下一个请求是产品/UI

从这些文件开始：
- `scripts/app.py` — Streamlit UI
- `scripts/query.py` — CLI 核心
- `DESIGN.md` — 设计系统

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

### 本次 session 主要工作

1. **FCV 主题页重编译** — 将 3 个核心页面从 routing page 升级为 handbook 状态
2. **系统状态验证** — 健康检查全部通过
3. **接力文档** — 本文档

### 关键观察

- 所有 6 个疾病模块的源卡层已完全闭合 (144 个 paper cards, 全部 deep_extracted)
- 主要工作已从源卡提取转向主题页整合和产品表面打磨
- FCV 主题页重编译是一个好的模板，其他疾病模块可以参考

---

## 最终读物

项目在一个**内核成熟、表面逐步完善**的状态：

- 6 个疾病模块全部 24/24 deep-extracted
- FCV 核心主题页本次完成重编译
- Ask the vault 后端路径已调通
- 下一步是继续主题页整合和产品表面打磨

*End of handoff. 下一个模型：先读这份文档，然后继续 Pending 工作或跟随最新用户请求。*
