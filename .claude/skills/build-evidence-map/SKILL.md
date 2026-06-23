# /build-evidence-map

构建证据地图：将多篇 Paper Cards 聚类，生成结构化证据地图。

## 触发方式

- `/build-evidence-map` - 交互式选择主题
- `/build-evidence-map --topic diabetes_model_endpoints` - 指定主题
- `/build-evidence-map --papers src-diabetes-025,src-diabetes-026` - 指定文献

## 前置条件

- 目标文献已完成深度提取（存在于 `raw/deep-extractions/`）
- 或存在 Paper Card 格式文件

## 工作流程

### Step 1: 收集 Paper Cards

```bash
# 检查可用的深度提取文件
TOPIC="$1"
echo "=== 查找相关深度提取 ==="
ls raw/deep-extractions/ext-src-${TOPIC}*.md 2>/dev/null || echo "无精确匹配"
ls raw/deep-extractions/ext-*.md 2>/dev/null | head -20
```

### Step 2: 加载 Prompt

读取 `system/prompts/evidence-map-builder-v1.md`

### Step 3: 读取 Paper Cards

对每篇指定的深度提取文件：
1. 读取 YAML 元信息
2. 提取 Phase 2（论点-论据）
3. 提取 Phase 3（自检发现）
4. 提取一句话总结

### Step 4: 主题聚类

按内容自然聚类，识别：
- 共同主题
- 跨文献共识
- 证据张力

### Step 5: 生成证据矩阵

```markdown
| 主题 | 直接证据 | 支持证据 | 推断证据 | 证据强度 |
|------|---------|---------|---------|---------|
```

### Step 6: 输出

```bash
mkdir -p outputs/evidence_maps/${TOPIC_ID}
```

生成：
- `evidence_map.md` - 主文档
- `evidence_matrix.json` - 结构化矩阵
- `theme_index.json` - 主题-文献索引

## 示例

### 输入

```
主题：猫糖尿病模型关键评价指标
Paper Cards：
- raw/deep-extractions/ext-src-diabetes-025.md
- raw/deep-extractions/ext-src-diabetes-026.md
- raw/deep-extractions/ext-src-diabetes-027.md
...
```

### 输出

```markdown
# 证据地图：猫糖尿病模型关键评价指标

## 元信息
- 文献数量：8
- 构建日期：2026-06-23
- 主题数量：6

## 主题一：表型与临床指标

### 核心证据
- src-diabetes-025: 血糖/果糖胺作为基础但有局限
- src-diabetes-030: 果糖胺诊断价值

### 跨文献共识
8/8 篇文献认可血糖和果糖胺作为基础指标...

## 主题二：外周胰岛素信号
...

## 证据矩阵
| 主题 | 直接 | 支持 | 推断 | 强度 |
|------|------|------|------|------|
| 表型指标 | 3 | 2 | - | ★★★★ |
...
```

## 质量检查

构建后自动验证：
- [ ] 每个主题至少引用 2 篇文献
- [ ] 所有输入 Paper Cards 都被引用
- [ ] 证据矩阵完整
- [ ] 包含跨文献洞察

## 输出路径

```
outputs/evidence_maps/
└── {topic_id}/
    ├── evidence_map.md
    ├── evidence_matrix.json
    └── theme_index.json
```

## 下游接口

Evidence Map 传递给：
- `/synthesize-research-workspace` - 生成研究任务输出
- `/verify-research-output` - 作为验证材料

## 安全边界

- 不读取原始 PDF/文献（只读 Paper Cards）
- 不引用 Evidence Map 之外的文献
- 不发明数据
