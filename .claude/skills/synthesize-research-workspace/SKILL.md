# /synthesize-research-workspace

生成 Research Workspace 输出：基于 Evidence Map 生成可直接进入页面的结构化内容。

## 触发方式

- `/synthesize-research-workspace` - 交互式选择主题
- `/synthesize-research-workspace --topic diabetes_model_endpoints` - 指定主题
- `/synthesize-research-workspace --map outputs/evidence_maps/xxx/evidence_map.md` - 指定 Evidence Map

## 前置条件

- Evidence Map 已生成（通过 `/build-evidence-map`）
- 或有可用的 Paper Cards

## 工作流程

### Step 1: 加载 Evidence Map

```bash
TOPIC="$1"
MAP_FILE="outputs/evidence_maps/${TOPIC}/evidence_map.md"
if [ ! -f "$MAP_FILE" ]; then
  echo "Error: Evidence Map not found. Run /build-evidence-map first."
  exit 1
fi
```

### Step 2: 加载 Prompt

读取 `system/prompts/research-workspace-synthesizer-v1.md`

### Step 3: 生成 6 个 Tab

1. **任务摘要**
   - 研究问题
   - 任务理解
   - 检索范围
   - 核心结论（3-5 条）

2. **证据地图**
   - 按角色排序的文献表
   - 为什么选这些文献

3. **核心发现**
   - 每个发现标注证据标签：[直接证据] / [来源支持] / [分析推断]
   - 包含模型评价启示

4. **方法与终点**
   - 指标分层矩阵
   - 检测方法推荐

5. **模型与药效评价价值**
   - 对 NewPets 业务的转化价值
   - 可复用内容块

6. **缺口与下一步**
   - 证据缺口表
   - 下一步研究建议
   - 推荐的后续研究任务

### Step 4: 输出

```bash
mkdir -p outputs/research_workspace/${TOPIC}
```

生成：
- `research_workspace.md` - 完整输出
- `snippets.json` - 可调用内容块
- `metadata.json` - 元信息

### Step 5: 自动调用验证

生成后自动调用 `/verify-research-output` 进行质量检查。

## 示例

### 输入

```
主题：猫糖尿病模型关键评价指标
Evidence Map：outputs/evidence_maps/diabetes_model_endpoints/evidence_map.md
```

### 输出（摘要）

```markdown
# Research Workspace: 猫糖尿病模型关键评价指标

## 任务摘要

### 核心结论
1. 表型指标是必要但不充分
2. 外周胰岛素信号是机制评价核心
3. 分层因素必须控制
4. 肾功能指标应纳入
5. 酮体监测是安全性必需

## 证据地图
| 文献 | 角色 | 贡献 | 强度 |
...

## 核心发现

### 发现 1：糖尿病猫的外周胰岛素信号障碍是多组织现象
[直接证据]
Patra et al. (2024) 发现...

...

## 方法与终点

### 指标分层矩阵
| 指标类型 | 具体指标 | 适用场景 | 来源 |
...

## 模型与药效评价价值

### 可复用内容块
> 猫糖尿病模型评价不宜只看血糖、果糖胺...

## 缺口与下一步

### 证据缺口
| 缺口 | 影响 | 严重程度 |
...
```

## 证据标签规则

| 标签 | 含义 | 前端样式 |
|------|------|---------|
| [直接证据] | 文献原文或数据直接支持 | 绿色 |
| [来源支持] | 多篇文献共同支持 | 黄色 |
| [分析推断] | 合理推理，需人工复核 | 灰色 |

## 质量检查

生成后自动验证：
- [ ] 6 个 Tab 全部填写完整
- [ ] 每个核心发现都有证据标签
- [ ] 每个结论都引用了具体文献
- [ ] 没有超出 Evidence Map 的引用
- [ ] 转化价值具体到业务场景

## 输出路径

```
outputs/research_workspace/
└── {topic_id}/
    ├── research_workspace.md
    ├── snippets.json
    └── metadata.json
```

## 下游接口

生成后自动：
1. 调用 `/verify-research-output` 验证
2. 如果通过，标记为 `verified`
3. 如果不通过，显示修订清单

## 安全边界

- 不引用 Evidence Map 之外的文献
- 不发明数据或统计量
- 证据标签必须准确
- 物种边界必须清晰
