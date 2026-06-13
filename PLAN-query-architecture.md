# Query Architecture Plan

## 核心基础：Karpathy Wiki LLM Concept

**这是vault的真正价值所在，不能丢失：**

1. **结构化source cards** - 每篇论文都有深度提取
   - `quoted_fact` - 原文直接引用的事实
   - `source_supported_conclusion` - 基于source能推出的结论
   - `llm_inference` - LLM推理（明确标注，可追溯）

2. **Key-Claim Traceability** - 每个claim都能追溯
   - Claim ID → Source ID → 原文
   - Level (A/B/C) 标注证据强度
   - Boundary 说明claim的边界

3. **Deep Extraction Workflow** - 分层提取
   - Abstract level → Full-text deep extraction
   - 保留 limits/caveats
   - 标注 open follow-up questions

**这个底座的价值：**
- 比普通LLM回答更可靠（因为可核验）
- 比直接读论文更高效（因为已结构化）
- 支持研究者做严肃的知识工作

---

## 目标

### Goal 1: 知识类查询 — Wikipedia式详实内容，可核验
- 用户问"什么是FIP" → 获得清晰解释 + 引用来源
- 用户想核验 → 能追溯到source card甚至原文

### Goal 2: 研究/专业类查询 — 药效学评价等，可核验支持
- 用户问"FIP药效评价指标" → 获得结构化的endpoint hierarchy
- 用户问"GS-441524疗效证据" → 获得Key-Claim Traceability表格
- 每个claim都标注证据层级和来源

---

## 当前问题诊断

### app.py builder函数的问题
```
当前：返回预制套话，对普通用户太难懂，对研究者又不够结构化
应该：根据query类型，暴露vault中已有的结构化内容
```

### Query分类缺失
```
当前："解释FIP"和"FIP药效评价"用同一个函数处理
应该：区分query类型，路由到不同内容层
```

---

## 解决方案

### Query类型分类

| 类型 | 示例查询 | 应返回内容 | 目标页面 |
|------|----------|------------|----------|
| 简单解释 | "什么是FIP", "解释猫传腹" | 易懂的解释 + 基础来源 | what-is-*.md |
| 机制详情 | "FIP发病机制", "FIP是怎么发展的" | 机制层级 + 引用 | mechanism-overview.md |
| 诊断/评价 | "FIP怎么诊断", "FIP的评价指标" | Endpoint Hierarchy + Key-Claim表 | endpoint-handbook.md |
| 治疗/转化 | "FIP怎么治疗", "GS-441524疗效" | Treatment分支 + 引用 | translation-brief.md |
| 验证/核查 | "验证这个claim", "原文在哪" | Source card + 原文链接 | verify-a-claim.md |

### 实现步骤

#### Step 1: 优化query分类逻辑
修改 `scripts/app.py` 中的 query routing：
- 检测query关键词判断类型
- 简单解释类 → build_*_simple_explanation()
- 研究类 → build_*_research_answer()

#### Step 2: 创建研究类answer builder
对每个疾病，创建返回结构化内容的函数：
```python
def build_fip_endpoint_research_answer(chinese: bool) -> tuple[str, list[str]]:
    """返回FIP endpoint hierarchy的结构化内容"""
    # 直接从 topics/fip/endpoint-handbook.md 提取Key-Claim表格
    # 返回：
    # - Endpoint Hierarchy (1-6)
    # - Key-Claim Traceability表格
    # - 验证路径提示
```

#### Step 3: 添加验证路径
每个answer都包含：
- 来源标注 `[source: src-fip-016]`
- 证据层级 `[quoted_fact]` / `[source_supported_conclusion]` / `[llm_inference]`
- "如何验证"提示

---

## 具体文件修改清单

### 1. scripts/app.py

**修改query分类函数：**
```python
def classify_query(query: str) -> str:
    """将查询分类为不同类型"""
    simple_keywords_zh = ["什么是", "解释", "是什么", "简单介绍"]
    mechanism_keywords_zh = ["机制", "原理", "为什么会", "怎么发展"]
    endpoint_keywords_zh = ["诊断", "指标", "评价", "检测", "怎么判断"]
    treatment_keywords_zh = ["治疗", "药", "疗效", "怎么治"]
    verify_keywords_zh = ["验证", "核查", "原文", "引用"]

    for kw in simple_keywords_zh:
        if kw in query:
            return "simple"
    for kw in endpoint_keywords_zh:
        if kw in query:
            return "endpoint"
    for kw in treatment_keywords_zh:
        if kw in query:
            return "treatment"
    # ...
    return "general"
```

**添加研究类builder函数：**
为每个疾病添加：
- `build_*_endpoint_answer()` - 返回endpoint hierarchy
- `build_*_treatment_answer()` - 返回treatment evidence
- `build_*_mechanism_answer()` - 返回mechanism overview

### 2. 确保topic pages结构完整

每个疾病需要：
- [x] what-is-*.md - 简单解释（已创建FIP/CKD/obesity/cancer）
- [ ] endpoint-handbook.md - 需确认Key-Claim表格完整
- [ ] translation-brief.md - 需确认treatment分支完整
- [ ] mechanism-overview.md - 需确认机制层级完整

### 3. 添加验证流程支持

在answer末尾添加标准验证提示：
```markdown
---
## 如何验证
- 本回答基于 [src-fip-016, src-fip-019] 等source cards
- 查看详细引用：打开 `raw/papers/src-fip-016.md`
- 核查原文：[DOI链接]
```

---

## 验收标准

### 知识类查询测试
| 查询 | 期望结果 |
|------|----------|
| "什么是FIP" | 易懂解释 + 基础引用 |
| "猫慢性肾病是什么" | 易懂解释 + 基础引用 |

### 研究类查询测试
| 查询 | 期望结果 |
|------|----------|
| "FIP的诊断指标有哪些" | Endpoint Hierarchy表格 + Key-Claim引用 |
| "GS-441524的疗效证据" | Treatment分支 + 具体source引用 |
| "FIP药效学评价应该看什么" | Endpoint分层 + 证据边界说明 |

### 核验路径测试
- 每个claim都能追溯到source card
- 每个source card都有原文链接或DOI
- 证据层级清晰标注

---

## 实施优先级

1. **P0**: 修复app.py query分类逻辑
2. **P1**: 为FIP创建研究类answer builder（作为模板）
3. **P2**: 复制模板到其他疾病
4. **P3**: 添加验证流程支持

---

## 下一步行动

1. 修改 `scripts/app.py` 添加query分类函数
2. 为FIP创建 `build_fip_endpoint_research_answer()` 函数
3. 测试 "FIP药效评价指标" 查询
4. 如果可行，复制模式到其他疾病
