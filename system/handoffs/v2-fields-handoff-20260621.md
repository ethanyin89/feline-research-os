# V2 Enhanced Fields 接力文档

**日期**: 2026-06-21
**状态**: 进行中
**优先级**: 常规批量处理

---

## 背景

V2 enhanced fields 用于提升 Research Mode 的文献推荐质量。每张 source card 的 `evidence_policy` 下新增以下字段：

- `study_design`: 研究设计（中文）
- `core_argument`: 核心论点（中文）
- `implicit_premise`: 隐含前提（中文）
- `title_gap`: 标题之外的价值（中文）
- `evidence_boundary`: 证据边界（中文）
- `unexpected_finding`: 意外发现（可选，中文）

---

## 当前进度

| 病种 | 带 V2 | 总数 | 覆盖率 |
|------|-------|------|--------|
| Cancer | 111 | 111 | 100% |
| IBD | 26 | 126 | 21% |
| Diabetes | 25 | 121 | 21% |
| FCV | 58 | 296 | 20% |
| CKD | 38 | 197 | 19% |
| Obesity | 15 | 95 | 16% |
| HCM | 32 | 226 | 14% |
| FIP | 33 | 242 | 14% |
| **总计** | **338** | **1414** | **24%** |

**剩余**: 1076 张卡片

---

## 已固化的工具

### 批量处理脚本

```bash
# 处理指定病种的 N 张卡片
OPENROUTER_DAILY_BUDGET_USD=1.00 .venv/bin/python scripts/add_v2_fields.py --disease <disease> --limit <n>

# 干跑（不实际修改）
OPENROUTER_DAILY_BUDGET_USD=1.00 .venv/bin/python scripts/add_v2_fields.py --disease fcv --limit 5 --dry-run

# 处理单个文件
OPENROUTER_DAILY_BUDGET_USD=1.00 .venv/bin/python scripts/add_v2_fields.py --file raw/papers/src-hcm-042.md
```

### 技能文档

- `.agents/skills/content_deep_extractor/SKILL.md` - 完整的深度提取流程，含 V2 字段模板和质量门控
- `system/prompts/deep-extraction-prompt-v2.md` - LLM 提取 prompt

### 自动化

```bash
# 已安装每日健康检查 (9:00 AM)
launchctl list | grep feline

# 手动运行
.venv/bin/python scripts/health.py
```

---

## 下一步建议

### 优先级 1: 低覆盖率病种
- HCM (14%) 和 FIP (14%) 最低
- 每次处理 10-20 张，保持质量

### 优先级 2: 质量抽查
- 随机检查已生成的 V2 字段
- 验证 `core_argument` 是完整主张而非话题描述
- 验证 `evidence_boundary` 是具体边界而非泛泛"需要更多研究"

### 优先级 3: 误收录清理
- 6 张 cancer cards 已标记为人类研究
- src-cancer-098, 103, 104, 106, 110, 111
- 可保留作为术语背景或移除

---

## 关键约束

1. **API 成本**: 每次运行必须设置 `OPENROUTER_DAILY_BUDGET_USD=1.00`
2. **使用 venv**: 必须使用 `.venv/bin/python`
3. **质量门控**:
   - `core_argument` > 50 字符
   - `evidence_boundary` 必须非空且具体
   - 至少一个 `quoted_fact` 含具体数据

---

## 验证命令

```bash
# 检查覆盖率
for d in cancer hcm ckd fip fcv ibd diabetes obesity; do
  echo "$d: $(grep -l 'core_argument:' raw/papers/src-${d}-*.md 2>/dev/null | wc -l)"
done

# 测试解析
.venv/bin/python -c "
from scripts.research_mode import parse_source_card
from pathlib import Path
card = parse_source_card(Path('raw/papers/src-fcv-001.md'))
print('core_argument:', card.core_argument[:80] if card.core_argument else 'None')
"

# 运行测试
python3 scripts/test_query.py
```

---

## 相关文件

- `scripts/add_v2_fields.py` - 批量处理脚本
- `scripts/research_mode.py` - V2 字段解析和显示
- `.agents/AGENTS.md` - 自动化文档
- `system/indexes/karpathy-gap-analysis.md` - 已更新到 2026-06-21

---

## 接力检查清单

- [ ] 运行 `python3 scripts/test_query.py` 确认 113 tests pass
- [ ] 检查 `launchctl list | grep feline` 确认健康检查已安装
- [ ] 选择下一个处理的病种（建议 HCM 或 FIP）
- [ ] 设置 `OPENROUTER_DAILY_BUDGET_USD=1.00` 后运行脚本
