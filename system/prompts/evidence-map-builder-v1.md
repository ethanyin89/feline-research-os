# Evidence Map Builder Prompt V1

## 定位

Pipeline 第三步：将多篇 Paper Cards 聚类，生成结构化证据地图。

输入：一组已处理的 Paper Cards（JSON 或 Markdown）
输出：主题聚类 + 证据矩阵 + 跨文献洞察

**核心原则**：不读原始文献，只读已处理的 Paper Cards。

---

## 输入格式

```yaml
research_question: "研究问题"
topic_id: "diabetes_model_endpoints"
paper_cards:
  - source_id: "src-diabetes-025"
    file_path: "raw/deep-extractions/ext-src-diabetes-025.md"
  - source_id: "src-diabetes-026"
    file_path: "raw/deep-extractions/ext-src-diabetes-026.md"
  # ... 更多 Paper Cards
```

---

## 输出结构

### 1. 元信息

```yaml
---
topic_id: diabetes_model_endpoints
research_question: "猫糖尿病模型关键评价指标"
build_date: 2026-06-23
paper_count: 8
themes_identified: 6
---
```

### 2. 主题聚类

按内容自然聚类，不套用固定模板。典型结构：

```markdown
# 证据地图：猫糖尿病模型关键评价指标

## 主题一：表型与临床指标

### 核心证据
- **血糖/果糖胺**：src-diabetes-025 明确指出...
- **体重/BCS**：src-diabetes-027 发现...

### 跨文献共识
所有 8 篇文献均认可血糖和果糖胺作为基础指标，但 src-diabetes-025 和 src-diabetes-028 强调其局限性...

### 证据张力
src-diabetes-025 主张机制指标优于表型指标，与 src-diabetes-030（临床导向）存在视角差异。

---

## 主题二：外周胰岛素信号

### 核心证据
- **胰岛素受体/IRS/PI3K/AKT 通路**：src-diabetes-025 提供了系统框架...
- **GLUT4 表达**：src-diabetes-029 发现肥胖猫 GLUT4 早期下降...

### 跨文献共识
3/8 篇文献支持将外周胰岛素信号纳入模型评价。

### 证据张力
仅 src-diabetes-025 提供组织样本数据，其他文献为间接推断。

---

## 主题三：...
```

### 3. 证据矩阵

```markdown
## 证据矩阵

| 主题 | 直接证据 | 支持证据 | 推断证据 | 证据强度 |
|------|---------|---------|---------|---------|
| 表型指标 | 025, 027, 030 | 026, 028 | - | ★★★★☆ |
| 外周信号 | 025 | 029 | 031 | ★★★☆☆ |
| 肝脏代谢 | 025 | 032 | 026 | ★★☆☆☆ |
| ... | ... | ... | ... | ... |
```

### 4. 跨文献洞察

```markdown
## 跨文献洞察

### 共识发现
1. **血糖/果糖胺是必要但不充分指标**：8/8 篇认可其基础地位，但 3/8 篇明确指出局限性
2. **外周胰岛素抵抗是核心机制**：5/8 篇涉及，但仅 1 篇提供组织层面证据

### 证据缺口
1. **纵向研究缺失**：所有纳入文献均为横断面或回顾性设计
2. **治疗前后对比缺失**：仅 src-diabetes-025 区分 untreated vs treated
3. **样本量普遍较小**：中位样本量 42 只猫

### 方法学异质性
- 胰岛素敏感性测量：FSIVGTT vs HOMA-IR vs 其他
- 糖尿病定义标准不一致
- 肥胖分类标准（BCS vs BW% vs DEXA）不统一
```

### 5. 主题-文献索引

```markdown
## 主题-文献索引

### 表型与临床指标
- src-diabetes-025: 血糖、果糖胺局限性
- src-diabetes-027: 体重管理与血糖关系
- src-diabetes-030: 临床监测指标体系

### 外周胰岛素信号
- src-diabetes-025: 完整 IRS/PI3K/AKT/GLUT4 通路
- src-diabetes-029: GLUT4 早期下降

### ...
```

---

## 聚类规则

### 主题命名
- 使用具体名词，不用"其他"或"杂项"
- 如果一篇文献跨多个主题，在每个相关主题下引用
- 主题数量通常 4-8 个，过多则合并，过少则拆分

### 证据强度评级

| 星级 | 含义 |
|------|------|
| ★★★★★ | ≥3 篇直接证据，无冲突 |
| ★★★★☆ | 2 篇直接证据 + 支持证据 |
| ★★★☆☆ | 1 篇直接证据 + 多篇支持 |
| ★★☆☆☆ | 仅支持证据或推断 |
| ★☆☆☆☆ | 单一来源或存在明显冲突 |

### 证据类型区分

| 类型 | 定义 |
|------|------|
| 直接证据 | 原始数据直接支持结论（引用论文表/图/统计结果）|
| 支持证据 | 间接支持或部分支持（相关但非直接）|
| 推断证据 | 基于多来源综合推理 |

---

## 质量检查

构建完成后自检：

1. [ ] 每个主题至少引用 2 篇文献（单一来源标注为"弱证据"）
2. [ ] 所有输入 Paper Cards 都被引用至少一次
3. [ ] 证据矩阵覆盖所有识别的主题
4. [ ] 跨文献洞察包含：共识、缺口、异质性
5. [ ] 没有直接引用原文（只引用 Paper Card 内容）
6. [ ] 物种边界清晰（未将犬/人证据与猫证据混淆）

---

## 输出路径

```
outputs/evidence_maps/
└── {topic_id}/
    ├── evidence_map.md          # 主文档
    ├── evidence_matrix.json     # 结构化矩阵
    └── theme_index.json         # 主题-文献索引
```

---

## 与下游的接口

Evidence Map 传递给：
- Prompt 4 (Research Workspace Synthesizer)：作为生成研究输出的依据
- Prompt 5 (Verifier)：作为验证材料

关键约束：
- Synthesizer 不应引用 Evidence Map 未覆盖的文献
- Verifier 检查 Synthesizer 输出是否超出 Evidence Map 范围
