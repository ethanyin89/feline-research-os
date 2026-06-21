# /deep-extract-batch

批量深度提取：将 `status: extracted` 的论文升级为 `deep_extracted` 并添加 V2 字段。

## 触发方式

- `/deep-extract-batch` - 处理所有待深度提取的论文
- `/deep-extract-batch --disease ckd` - 仅处理 CKD
- `/deep-extract-batch --limit 10` - 限制每次处理数量

## 工作流程

### Step 1: 识别目标

```bash
echo "=== 待深度提取 ===" && for disease in hcm ckd fip cancer ibd; do
  count=0
  for f in raw/papers/src-${disease}-*.md 2>/dev/null; do
    if grep -q "^status: extracted" "$f" && ! grep -q "verification_status: deep_extracted" "$f"; then
      count=$((count+1))
    fi
  done
  [ $count -gt 0 ] && echo "$disease: $count"
done
```

### Step 2: 逐篇处理

对每篇论文执行：

1. **读取现有内容**：获取 title、evidence_policy、existing findings

2. **生成 V2 字段**（中文）：
   - `study_design`: 研究类型，样本描述，主要方法
   - `core_argument`: 一句话核心论点（必须是主张，不是话题）
   - `implicit_premise`: 隐含前提假设
   - `title_gap`: 这篇论文比标题/摘要看起来更值得读的原因
   - `evidence_boundary`: 证据边界，这篇论文回答不了什么

3. **更新 YAML frontmatter**：
   - `status: extracted` → `status: deep_extracted`
   - `extraction_depth: *` → `extraction_depth: full`
   - `verification_status: *` → `verification_status: deep_extracted`
   - 在 `evidence_policy:` 下 `llm_inference:` 后添加 V2 字段

### Step 3: 质量门控

每篇处理后验证：
- [ ] `core_argument` > 50 字符
- [ ] `evidence_boundary` 非空
- [ ] 至少一个 `quoted_fact` 含具体数据

### Step 4: 批量验证

```bash
python3 scripts/check_research_mode_presentation.py
```

## V2 字段模板

```yaml
  # V2 enhanced fields
  study_design: "研究类型，样本描述，主要方法"
  core_argument: "论文核心论点——必须是具体主张"
  implicit_premise: "假设...；假设..."
  title_gap: "标题说 X，但真正价值是 Y——隐藏发现/标题矛盾/价值偏移"
  evidence_boundary: "不能回答的问题；设计局限"
```

## 示例

**输入**：`src-ckd-026.md` (status: extracted)

**输出**：
```yaml
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
evidence_policy:
  quoted_fact:
    - "FGF-23 was higher in cats in all CKD stages than in controls."
  source_supported_conclusion:
    - "FGF-23 elevates earlier than hyperphosphatemia across CKD stages."
  llm_inference:
    - "FGF-23 may serve as an earlier-stage biomarker than serum phosphorus."
  # V2 enhanced fields
  study_design: "横断面研究，304 只猫（196 只 CKD、108 只健康对照），ELISA 检测血清 FGF-23"
  core_argument: "FGF-23 在所有 CKD 分期均升高且早于高磷血症出现"
  implicit_premise: "假设横断面关联反映纵向时间顺序"
  title_gap: "标题说早期诊断，但真正价值是表 3 显示健康猫 FGF-23 与年龄无关（p=0.15）——这意味着升高确实反映疾病而非衰老"
  evidence_boundary: "横断面设计不能建立时间先后顺序；单中心研究"
```

## 安全边界

- 不修改 `quoted_fact`（只能从原文提取）
- 不发明数据或统计量
- 如果现有内容不足以生成 V2 字段，标记为 `needs_full_text_review`
- 每次最多处理 20 篇，避免上下文过载

## 进度追踪

处理完成后更新：
```bash
echo "$(date +%Y-%m-%d): deep-extracted N papers (CKD: X, FIP: Y)" >> system/logs/deep-extraction-log.md
```
