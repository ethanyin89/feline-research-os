# /topic-recompile — Topic Page Recompilation Skill

将 topic page 从 "routing page" 升级为 "handbook" 状态。

## 触发条件

当用户要求：
- 重编译某个 topic page
- 检查 topic page 状态
- 升级 topic page 到 handbook

## 前置检查

在开始前，运行这个脚本检测需要重编译的页面：

```bash
cd /Users/jiawei/Desktop/insclaude/feline-research-os
for disease in ckd fip hcm ibd diabetes fcv; do
  echo "=== $disease ==="
  for page in mechanism-overview risk-and-recognition endpoint-handbook; do
    f="topics/$disease/$page.md"
    if [ -f "$f" ]; then
      date=$(grep "last_compiled_at:" "$f" | head -1 | sed 's/.*: *//')
      has_key_claim=$(grep -c "## Key-Claim Traceability" "$f" 2>/dev/null || echo 0)
      has_layer=$(grep -c "### Layer" "$f" 2>/dev/null || echo 0)
      if [ "$has_key_claim" = "0" ]; then
        echo "  NEEDS RECOMPILE: $page (compiled=$date)"
      else
        echo "  OK: $page (handbook, compiled=$date)"
      fi
    fi
  done
done
```

## Handbook 结构标准

重编译后的 handbook 页面必须包含以下结构：

### 1. Frontmatter 更新

```yaml
last_compiled_at: YYYY-MM-DD  # 今天日期
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
```

### 2. Key-Claim Traceability 表格

```markdown
## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| {PREFIX}1 | {核心声明} | B | src-xxx-NNN, src-xxx-NNN | {边界说明} |
| {PREFIX}2 | {核心声明} | B | src-xxx-NNN | {边界说明} |
```

- ID 前缀规则: `FM` (mechanism), `FR` (recognition), `FE` (endpoint)
- Level: `B` = 源卡支持的声明, `C` = 扩展分支声明
- Source ids: 直接支持该声明的源卡列表
- Boundary: 该声明的适用边界（不是什么）

### 3. Evidence-Depth Caveat

```markdown
## Evidence-Depth Caveat

This page sits on a fully deep-extracted {DISEASE} source-card layer ({N}/{N} papers).
Key anchors: {列出关键锚点源卡和角色}. This is now a {type} handbook rather than a routing page.
```

### 4. Core Takeaway

一段话总结该页面的核心洞察。

### 5. Hierarchy / Architecture 层级

**对于 mechanism-overview:**
```markdown
## Mechanism Hierarchy

### Layer 1: {顶层机制}
{描述}
**Lead sources:** `src-xxx-NNN`, `src-xxx-NNN`
**Current safe read:**
- {安全声明 1}
- {安全声明 2}

### Layer 2: {次层机制}
...
```

**对于 risk-and-recognition:**
```markdown
## Recognition Architecture

### Core Recognition Frame
{核心识别框架}
**Lead sources:** `src-xxx-NNN`

### Diagnostic Testing
...

### Carrier State / Differential
...
```

**对于 endpoint-handbook:**
```markdown
## Endpoint Hierarchy

### Endpoint 1: {端点名称}
{描述}
**Key boundary:** {边界}
**Lead sources:** `src-xxx-NNN`

### Endpoint 2: ...
```

### 6. Source-Layer Reality 表格

```markdown
## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-xxx-NNN | {该源在本页的角色} | deep_extracted |
```

### 7. Current Owner Memo 链接

```markdown
## Current Owner Memo

- `{DISEASE} {type} memo`: `../../system/indexes/{disease}-{type}-memo.md`
```

### 8. Guardrail

```markdown
## Guardrail

{说明这个页面不应该做什么，防止过度声明}
```

### 9. What The Module Can Say Safely / Cannot Say Yet

```markdown
## What The Module Can Say Safely

- {安全声明 1}
- {安全声明 2}

## What The Module Should Not Say Yet

- do not {限制 1}
- do not {限制 2}
```

### 10. Current Role

```markdown
## Current Role

Use this page as the {DISEASE} {type} handbook. The source-card layer is complete at {N}/{N}
deep-extracted papers. Next gains come from {下一步方向}.
```

## 执行流程

### Step 1: 读取源卡

```bash
# 列出该疾病的所有源卡
ls /Users/jiawei/Desktop/insclaude/feline-research-os/raw/papers/src-{disease}-*.md
```

读取所有相关源卡的 frontmatter 和 Key Findings 部分。

### Step 2: 读取现有 topic page

读取需要重编译的 topic page 当前内容。

### Step 3: 读取相关 owner memo

检查 `system/indexes/{disease}-*-memo.md` 是否存在相关 memo。

### Step 4: 重编译

按照上述 Handbook 结构标准重写页面。

关键规则：
- Key-Claim 必须有明确的源卡追溯
- 不要创造新的声明，只整合源卡中已有的内容
- Guardrail 必须明确说明边界
- Layer/Endpoint 数量根据源卡支持程度决定

### Step 5: 验证

重编译完成后验证：

```bash
# 检查新页面结构
f="topics/{disease}/{page}.md"
echo "Key-Claim Traceability: $(grep -c '## Key-Claim Traceability' $f)"
echo "Layers: $(grep -c '### Layer' $f)"
echo "Source-Layer Reality: $(grep -c '## Source-Layer Reality' $f)"
echo "Guardrail: $(grep -c '## Guardrail' $f)"
```

### Step 6: 更新 dashboard

更新 `topics/{disease}/current-state-dashboard.md`:
- 标记该页面已重编译
- 更新 confidence 状态

## 批量执行

当需要批量重编译时，按以下顺序：

1. **同一疾病内优先顺序**: mechanism-overview → risk-and-recognition → endpoint-handbook
2. **疾病优先顺序**: 用户指定 > 最旧的编译日期优先

## 样本参考

FCV 重编译（2026-04-30）是当前最佳样本：
- `topics/fcv/mechanism-overview.md` — 4 层机制层级
- `topics/fcv/risk-and-recognition.md` — 识别架构 + 5 个 Key-Claim
- `topics/fcv/endpoint-handbook.md` — 8 个端点层级 + 4 个 Key-Claim

## 不做的事情

- 不翻译源卡
- 不创造新声明
- 不修改源卡内容
- 不运行健康检查（那是另一个技能）
- 不创建 handoff 文档（那是另一个技能）
