# Deep Extraction V3 二级页面架构 接力文档

**日期**: 2026-06-22
**状态**: 基础架构完成，待扩展内容
**优先级**: 高 — 提升 Research Mode 推荐质量

---

## 背景

Research Mode 的 "Why it matters" 和 "Takeaway" 字段过于模块化/模板化。用户希望：
1. **一级页面**：推荐卡片展示从 Phase 2/3 提炼的精华内容
2. **二级页面**：点击进入独立详情页，展示完整 Phase 2（论点-论据提炼）+ Phase 3（自检发现）+ 原文元信息 + 外链

---

## 已完成的工作

### 1. 架构设计

```
raw/deep-extractions/ext-{source-id}.md   # 深度提炼文档存储位置
```

**二级架构流程**：
- 一级页面：`has_deep_extraction=True` 的卡片显示提炼后的 Why/Takeaway + 详情链接
- 二级页面：通过 `?detail={source-id}` query param 路由到详情页

### 2. 新增文件

| 文件 | 用途 |
|------|------|
| `scripts/deep_extraction.py` | 解析和渲染深度提炼文档 |
| `system/prompts/deep-extraction-prompt-v3.md` | V3 深度提炼 prompt 模板 |
| `raw/deep-extractions/.gitkeep` | 目录占位 |

### 3. 已创建的深度提炼样本（3 篇）

| Source ID | 论文 | 状态 |
|-----------|------|------|
| `src-hcm-076` | Left Atrioventricular Coupling Index in Feline HCM | ✅ 完成 |
| `src-hcm-205` | ALMS1 Variant in Sphynx Cats (New Zealand) | ✅ 完成 |
| `src-diabetes-025` | Insulin Signaling Deficits in Feline Diabetes | ✅ 完成 |

### 4. 代码修改

**`scripts/deep_extraction.py`** (新建)
- `DeepExtraction` dataclass — 结构化存储提炼内容
- `has_deep_extraction(source_id)` — 检查是否存在深度提炼
- `parse_deep_extraction(source_id)` — 解析 YAML frontmatter + Phase 内容
- `render_detail_page_markdown(extraction)` — 渲染二级页面 markdown
- `get_distilled_why_it_matters(extraction)` — 从 Phase 2 提取论点
- `get_distilled_takeaway(extraction)` — 从 Phase 3 提取 takeaway

**`scripts/research_mode.py`** (修改)
- `SourceCard` 新增字段：`has_deep_extraction`, `deep_extraction_why`, `deep_extraction_takeaway`
- `enrich_with_deep_extraction(card)` — 用深度提炼内容增强卡片
- `_format_chinese_paper_entry()` — 使用深度提炼内容 + 添加详情链接

**`scripts/app.py`** (修改)
- 添加 `?detail={source-id}` 路由处理
- 二级页面渲染 + 返回按钮

---

## 深度提炼文档格式

```yaml
---
source_id: src-{disease}-{nnn}
title: "论文完整标题"
title_zh: "论文中文标题"
authors:
  - "First Author"
  - "Second Author"
journal: "Journal Name"
year: 2024
doi: "10.xxxx/xxxxx"
url: "https://doi.org/..."
extraction_date: 2026-06-22
extractor: human|llm
---

# Phase 0：逐段微观分析
[内部过程，不对外展示]

# Phase 1：主题重构
[内部过程，不对外展示]

# Phase 2：论点-论据提炼
[二级页面核心内容]

# Phase 3：自检发现
[二级页面核心内容]

# 一句话总结
[用于一级页面 Takeaway]
```

---

## 验证命令

```bash
# 检查深度提炼文件
ls -la raw/deep-extractions/

# 测试解析
python3 -c "
from scripts.deep_extraction import list_deep_extractions, parse_deep_extraction
sources = list_deep_extractions()
print(f'Found {len(sources)} deep extractions: {sources}')
for sid in sources:
    ext = parse_deep_extraction(sid)
    print(f'{sid}: Phase2={bool(ext.phase2_content)}, Phase3={bool(ext.phase3_content)}')
"

# 测试卡片增强
python3 -c "
from scripts.research_mode import load_disease_sources, enrich_with_deep_extraction
cards = load_disease_sources('hcm')
for card in cards:
    card = enrich_with_deep_extraction(card)
    if card.has_deep_extraction:
        print(f'{card.id}: {card.deep_extraction_why[:50]}...')
"

# 运行查询测试
python3 scripts/test_query.py
```

---

## 下一步建议

### 优先级 1: 扩展深度提炼内容
- 当前仅 3 篇论文有深度提炼
- 高价值目标：高证据等级论文（指南、系统综述、Meta 分析）
- 建议先完成 HCM 和 Diabetes 各 5-10 篇核心文献

### 优先级 2: 创建批量提炼技能
- 参考 `.claude/skills/import-deep-extraction/` 目录结构
- 输入：PDF 全文或摘要
- 输出：符合 V3 格式的 `ext-{source-id}.md`

### 优先级 3: 质量门控
深度提炼质量标准：
- Phase 2 论点必须是完整主张，非话题描述
- Phase 3 必须指出具体证据边界，非泛泛"需要更多研究"
- 一句话总结必须具体、有信息量，非重复标题

### 优先级 4: UI 优化
- 一级页面：为有深度提炼的卡片添加视觉标记（如 📖 图标）
- 二级页面：优化 Phase 2/3 的渲染样式

---

## 关键约束

1. **No Fake Data**: 深度提炼内容必须来自真实论文，禁止编造
2. **命名规范**: 深度提炼文件必须为 `ext-{source-id}.md` 格式
3. **Phase 2/3 必填**: 至少要有 Phase 2 或 Phase 3 内容，否则无意义
4. **外链必须**: 每篇深度提炼必须包含可访问的原文 DOI 或 URL

---

## 相关文件

| 文件 | 用途 |
|------|------|
| `scripts/deep_extraction.py` | 核心解析/渲染模块 |
| `scripts/research_mode.py` | 卡片增强逻辑 |
| `scripts/app.py` | 二级页面路由 |
| `system/prompts/deep-extraction-prompt-v3.md` | 提炼 prompt 模板 |
| `raw/deep-extractions/` | 深度提炼文档存储 |

---

## 接力检查清单

- [x] 3 个样本文件已创建并通过解析测试
- [x] `deep_extraction.py` 模块功能完整
- [x] `research_mode.py` 卡片增强逻辑可用
- [x] `app.py` 二级页面路由可用
- [ ] 运行 `python3 scripts/test_query.py` 确认测试通过
- [ ] 启动 Streamlit 验证二级页面渲染效果
- [ ] 选择下一批待深度提炼的论文
