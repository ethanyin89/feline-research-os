# /verify-research-output

验证 Research Workspace 输出：检查准确性、证据边界、物种外推。

## 触发方式

- `/verify-research-output` - 交互式选择
- `/verify-research-output --topic diabetes_model_endpoints` - 指定主题
- `/verify-research-output --level thorough` - 指定验证级别

## 验证级别

| 级别 | 检查范围 | 用时 |
|------|---------|------|
| quick | 完整性 + 物种边界 | ~2 分钟 |
| standard | 全部 8 个维度 | ~5 分钟 |
| thorough | 全部 + 逐句验证 + Gold Standard 对比 | ~15 分钟 |

## 工作流程

### Step 1: 加载输入

```bash
TOPIC="$1"
WS_FILE="outputs/research_workspace/${TOPIC}/research_workspace.md"
MAP_FILE="outputs/evidence_maps/${TOPIC}/evidence_map.md"

if [ ! -f "$WS_FILE" ]; then
  echo "Error: Research Workspace not found"
  exit 1
fi
```

### Step 2: 加载 Prompt

读取 `system/prompts/verifier-gap-checker-v1.md`

### Step 3: 执行 8 维验证

1. **事实准确性检查**
   - 逐条验证引用的具体数据
   - 与原始 Paper Card 对比

2. **证据标签一致性**
   - 检查 [直接证据]/[来源支持]/[分析推断] 使用是否准确

3. **物种边界检查**
   - 检测跨物种外推（人→猫、犬→猫）

4. **证据覆盖检查**
   - 验证是否超出 Evidence Map 范围
   - 检查未使用的文献

5. **逻辑一致性检查**
   - 检测内部矛盾

6. **完整性检查**
   - 确保 6 个 Tab 都存在且非空

7. **方法学审查**
   - 检查研究设计相关声明

8. **Gold Standard 对比**（thorough 级别）
   - 与已有 Gold Standard 评分对比

### Step 4: 输出报告

```bash
mkdir -p outputs/verification/${TOPIC}
```

生成：
- `verification_report.md` - 验证报告
- `issues.json` - 结构化问题列表
- `revision_checklist.md` - 修订清单

### Step 5: 判定结果

| 状态 | 条件 |
|------|------|
| pass | 总分 ≥ 80，无高严重度问题 |
| needs_revision | 总分 70-79 或存在高严重度问题 |
| fail | 总分 < 70 或多项严重问题 |

## 示例输出

```markdown
# 验证报告

## 综合评分

| 维度 | 评分 | 权重 | 加权分 |
|------|------|------|-------|
| 事实准确性 | 80% | 25% | 20.0 |
| 证据标签 | 70% | 15% | 10.5 |
| 物种边界 | 80% | 15% | 12.0 |
| 证据覆盖 | 90% | 15% | 13.5 |
| 逻辑一致性 | 85% | 10% | 8.5 |
| 完整性 | 83% | 10% | 8.3 |
| 方法学 | 70% | 10% | 7.0 |
| **总分** | | **100%** | **79.8** |

## 状态：needs_revision

## 必须修正的问题

1. **[高]** Tab 3：修正果糖胺时间窗口描述
2. **[高]** Tab 4：不能从横断面研究推断因果

## 修订清单

- [ ] 果糖胺时间窗口已修正
- [ ] 因果表述已修正
```

## 质量门控

### 必须通过

- [ ] 事实准确性 ≥ 80%
- [ ] 物种边界 ≥ 90%
- [ ] 完整性 100%
- [ ] 无高严重度方法学问题

### 触发重做

- 事实准确性 < 60%
- 多项 < 60%
- 不可修复的结构性问题

## 输出路径

```
outputs/verification/
└── {topic_id}/
    ├── verification_report.md
    ├── issues.json
    └── revision_checklist.md
```

## 修订循环

```
验证不通过
    ↓
生成修订清单
    ↓
返回 /synthesize-research-workspace 修订
    ↓
重新验证
    ↓
最多 3 轮，仍不通过 → needs_human_review
```

## 安全边界

- 只读取，不修改任何文件
- 不发明评分标准
- 诚实报告问题，不掩盖
