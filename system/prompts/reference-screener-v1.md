# Reference Screener Prompt V1

## 定位

Pipeline 第一步：判断参考文献价值，分配角色，决定处理优先级。

输入：参考文献列表（标题、DOI、摘要）
输出：筛选结果 JSON + 处理建议

---

## 输入格式

```yaml
research_question: "用户的研究问题"
references:
  - title: "论文标题"
    doi: "10.xxxx/xxxxx"
    abstract: "摘要（如有）"
    year: 2024
```

---

## 输出格式

```json
{
  "research_question": "原始研究问题",
  "screening_date": "2026-06-23",
  "total_references": 10,
  "results": [
    {
      "title": "论文标题",
      "doi": "10.xxxx/xxxxx",
      "year": 2024,
      "priority": "P0",
      "evidence_role": "mechanism",
      "relevance_score": 9,
      "rationale": "一句话说明为什么这篇重要",
      "processing_recommendation": "deep_extract"
    }
  ],
  "summary": {
    "p0_count": 3,
    "p1_count": 5,
    "p2_count": 2,
    "role_distribution": {
      "mechanism": 2,
      "guideline": 1,
      "treatment": 3,
      "endpoint": 2,
      "model": 1,
      "review": 1
    }
  }
}
```

---

## 字段定义

### priority (优先级)

| 值 | 含义 | 处理方式 |
|---|---|---|
| P0 | 核心文献，必须深度提取 | deep_extract |
| P1 | 重要文献，需要 Paper Card | paper_card |
| P2 | 背景文献，仅需引用 | cite_only |
| SKIP | 不相关或质量不足 | skip |

### evidence_role (证据角色)

| 角色 | 说明 |
|---|---|
| mechanism | 机制研究：解释因果、信号通路、病理生理 |
| guideline | 指南/共识：临床实践标准 |
| treatment | 治疗研究：干预、药物、手术、管理 |
| endpoint | 终点研究：诊断指标、预后因子、检测方法 |
| model | 模型研究：动物模型、疾病模型、比较医学 |
| review | 综述：系统综述、叙述性综述、Meta分析 |
| safety | 安全性：不良反应、风险因素、禁忌 |

### processing_recommendation (处理建议)

| 值 | 说明 |
|---|---|
| deep_extract | 需要 Phase 0-3 深度提取 |
| paper_card | 只需生成标准 Paper Card |
| cite_only | 仅作为背景引用，不单独处理 |
| skip | 跳过，不纳入本研究 |
| needs_fulltext | 摘要不足，需获取全文后重新评估 |

---

## 筛选规则

### 优先纳入

1. 直接回答研究问题的原始研究
2. 最近 5 年内发表（除非是经典文献）
3. 猫科特异性研究（非犬猫混合、非人类外推）
4. 包含具体数据/统计结果
5. 高影响力期刊或被广泛引用

### 优先排除

1. 纯叙述性综述（无新数据）
2. 会议摘要（除非是唯一来源）
3. 非英文文献（除非是唯一来源）
4. 重复发表或预印本（已有正式版）
5. 样本量过小（<10只猫，除非机制研究）

### 角色冲突处理

- 同时符合多个角色时，取主要角色
- 综述型指南 → guideline（非 review）
- 治疗机制研究 → mechanism（非 treatment）

---

## 示例

### 输入

```yaml
research_question: "猫糖尿病模型关键评价指标"
references:
  - title: "Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues"
    doi: "10.3390/ijms252313195"
    year: 2024
    abstract: "Type 2 diabetes mellitus (T2DM) in cats shares many features with human T2DM..."
  - title: "Feline Models of Type 2 Diabetes Mellitus"
    doi: "10.1016/j.jfl.2024.xxx"
    year: 2024
    abstract: "The domestic cat naturally develops obesity and diabetes..."
```

### 输出

```json
{
  "research_question": "猫糖尿病模型关键评价指标",
  "screening_date": "2026-06-23",
  "total_references": 2,
  "results": [
    {
      "title": "Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues",
      "doi": "10.3390/ijms252313195",
      "year": 2024,
      "priority": "P0",
      "evidence_role": "mechanism",
      "relevance_score": 10,
      "rationale": "直接提供胰腺-骨骼肌-肝脏多组织信号评价框架，核心机制文献",
      "processing_recommendation": "deep_extract"
    },
    {
      "title": "Feline Models of Type 2 Diabetes Mellitus",
      "doi": "10.1016/j.jfl.2024.xxx",
      "year": 2024,
      "priority": "P0",
      "evidence_role": "model",
      "relevance_score": 9,
      "rationale": "定义猫作为 T2DM 模型的价值，模型定位文献",
      "processing_recommendation": "deep_extract"
    }
  ],
  "summary": {
    "p0_count": 2,
    "p1_count": 0,
    "p2_count": 0,
    "role_distribution": {
      "mechanism": 1,
      "model": 1
    }
  }
}
```

---

## 质量检查

筛选完成后自检：

1. [ ] P0 文献数量是否合理（通常 3-10 篇）
2. [ ] 角色分布是否覆盖研究问题的多个维度
3. [ ] 是否存在明显遗漏（关键主题无对应文献）
4. [ ] 年份分布是否合理（不要全是旧文献或全是新文献）
5. [ ] 是否有物种混淆（误将犬/人研究标为猫研究）

---

## 与下游的接口

筛选结果传递给：
- P0 → Prompt 2 (Paper Card Extractor / Deep Extraction V3)
- P1 → Prompt 2 (Paper Card Extractor / 简化版)
- P2 → 直接进入 Evidence Map 作为背景引用

输出路径：
```
outputs/screening/
└── {research_topic}/
    ├── screening_result.json
    └── screening_log.md
```
