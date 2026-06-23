# /screen-references

筛选参考文献：判断文献价值，分配角色，决定处理优先级。

## 触发方式

- `/screen-references` - 交互式筛选
- `/screen-references --topic "猫糖尿病模型"` - 指定主题
- `/screen-references --input refs.json` - 从文件读取

## 输入格式

### 交互式输入

直接粘贴参考文献列表（标题、DOI、摘要），系统自动解析。

### 文件输入

```json
{
  "research_question": "猫糖尿病模型关键评价指标",
  "references": [
    {
      "title": "论文标题",
      "doi": "10.xxxx/xxxxx",
      "year": 2024,
      "abstract": "摘要..."
    }
  ]
}
```

## 工作流程

### Step 1: 解析输入

```bash
# 如果是文件输入
if [ -f "$INPUT_FILE" ]; then
  cat "$INPUT_FILE" | jq -r '.references[] | .title'
fi
```

### Step 2: 加载 Prompt

读取 `system/prompts/reference-screener-v1.md`

### Step 3: 执行筛选

对每篇文献判断：
- `priority`: P0 / P1 / P2 / SKIP
- `evidence_role`: mechanism / guideline / treatment / endpoint / model / review / safety
- `relevance_score`: 1-10
- `processing_recommendation`: deep_extract / paper_card / cite_only / skip / needs_fulltext

### Step 4: 输出结果

```bash
mkdir -p outputs/screening/${TOPIC_ID}
```

生成：
- `screening_result.json` - 结构化结果
- `screening_log.md` - 可读报告

### Step 5: 交互确认

显示筛选结果摘要，询问用户：
- 是否同意 P0 列表
- 是否需要调整某些文献的优先级
- 是否继续进入 Paper Card 提取阶段

## 示例

### 输入

```
研究问题：猫糖尿病模型关键评价指标

文献列表：
1. Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues (DOI: 10.3390/ijms252313195, 2024)
2. Feline Models of Type 2 Diabetes Mellitus (2024)
3. The Cat as a Model for Human Obesity and Diabetes (2024)
...
```

### 输出

```
## 筛选结果摘要

- 总文献数：8
- P0（核心文献）：5
- P1（重要文献）：2
- P2（背景文献）：1
- SKIP：0

### P0 文献
| # | 标题 | 角色 | 建议 |
|---|------|------|------|
| 1 | Feline Diabetes Is Associated with... | mechanism | deep_extract |
| 2 | Feline Models of Type 2 Diabetes... | model | deep_extract |
...

是否继续处理 P0 文献？(Y/n)
```

## 质量检查

筛选后自动验证：
- [ ] P0 数量合理（3-10 篇）
- [ ] 角色分布覆盖多个维度
- [ ] 无明显遗漏
- [ ] 年份分布合理

## 输出路径

```
outputs/screening/
└── {topic_id}/
    ├── screening_result.json
    └── screening_log.md
```

## 下游接口

筛选结果传递给：
- P0 → `/deep-extract-batch` 或手工深度提取
- P1 → `/deep-extract-batch --mode paper_card`
- P2 → 直接进入 Evidence Map 作为背景引用

## 安全边界

- 不访问外部网络（DOI 解析需要全文时标记为 needs_fulltext）
- 不修改已有 Paper Cards
- 不自动开始提取（需用户确认）
