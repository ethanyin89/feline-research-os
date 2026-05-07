# /design-qa — Design System Compliance Check

检查 Streamlit app 是否符合 DESIGN.md 规范。

## 触发条件

当用户要求：
- 检查 UI 是否符合设计系统
- 验证 DESIGN.md 实现状态
- 找出 UI 和 DESIGN.md 之间的差异

## 前置条件

1. 读取 DESIGN.md 获取规范
2. 读取 scripts/app.py 获取当前实现

## 检查清单

### 1. 颜色检查

从 DESIGN.md 提取颜色定义：
- Background: `#0f1117`
- Surface: `#1a1d27`
- Surface 2: `#222535`
- Border: `#2d3147`
- Primary text: `#e8eaf0`
- Muted text: `#8b90a0`
- Subtle text: `#4a4f64`

Provenance 颜色：
- quoted_fact: `#16a34a` (green)
- source_supported_conclusion: `#ca8a04` (amber)
- llm_inference: `#6b7280` (gray)

**检查方法：**
```bash
grep -E "#[0-9a-fA-F]{6}" /Users/jiawei/Desktop/insclaude/feline-research-os/scripts/app.py
```

验证所有硬编码颜色是否在 DESIGN.md 颜色表中。

### 2. 字体检查

从 DESIGN.md 提取字体规范：
- Display/Hero: Geist Sans 600
- Body: Geist Sans 400, 15px, line-height 1.7
- UI/Labels: Geist Sans 500, 13px
- Data/Metadata: Geist Mono 400/500, 11–12px

**检查方法：**
```bash
grep -E "font-size|font-family|line-height" /Users/jiawei/Desktop/insclaude/feline-research-os/scripts/app.py
```

验证字体大小是否符合规范。

### 3. Provenance Badge 检查

从 DESIGN.md 提取 badge 规范：
- font-size: 0.75em (≈11px)
- padding: 1px 6px 或 2px 8px
- border-radius: 3px 或 4px
- white-space: nowrap

**检查方法：**
在 app.py 中找到 `BADGE_PATTERNS` 定义，验证样式是否符合规范。

### 4. Empty State 检查

从 DESIGN.md 提取 Empty State 规范：
- 标题: "Ask the vault" (Geist 600, xl 24px)
- 统计行: `{n} source cards · {m} topic pages · 4 diseases`
- 示例问题: 4 个，每疾病一个，双语混合
- Provenance guide: 只在 empty state 显示

**检查方法：**
在 app.py 中找到 `EMPTY_STATE_INTRO_HTML` 和 `render_example_question_chips`。

### 5. Error Message 检查

从 DESIGN.md 提取错误消息规范：

**Disease Detection Failure:**
```
I couldn't figure out which disease you're asking about.
Try selecting CKD, FIP, HCM, or IBD in the sidebar, then ask again.
```

**API/Backend Failure:**
```
Query failed: [error type]

What happened: [1-sentence plain English explanation]
What to try:
  · Check your API key is set correctly
  · Try switching to Ollama (local) in the sidebar
  · If using Ollama, make sure it's running: ollama serve
```

**检查方法：**
```bash
grep -E "st\.(error|warning)" /Users/jiawei/Desktop/insclaude/feline-research-os/scripts/app.py
```

验证错误消息是否符合规范。

### 6. Search UI 检查

从 DESIGN.md 提取 Search UI 规范：
- 位置: Sidebar, 在 Backend/Disease/Max hops 控件下方
- 组件: text_input + button + radio (All/Raw/Topics)
- 结果卡片: source ID + paper title + snippet

**检查方法：**
在 app.py 中找到 search 相关代码。

### 7. Copy/Export 检查

从 DESIGN.md 提取 Copy 规范：
- 位置: 每个 assistant message 下方，右对齐
- 标签: "Copy markdown"
- 行为: 复制 raw markdown 到剪贴板

**检查方法：**
在 app.py 中搜索 clipboard 或 copy 相关代码。

## 执行流程

### Step 1: 读取规范

```python
# 读取 DESIGN.md
design_spec = open("DESIGN.md").read()

# 提取关键规范
colors = extract_colors(design_spec)
fonts = extract_fonts(design_spec)
badges = extract_badge_spec(design_spec)
```

### Step 2: 读取实现

```python
# 读取 app.py
app_code = open("scripts/app.py").read()

# 提取实现细节
implemented_colors = extract_colors_from_code(app_code)
implemented_fonts = extract_fonts_from_code(app_code)
```

### Step 3: 比对差异

生成差异报告：

```markdown
## Design QA Report

### Colors
| Spec | Implementation | Status |
|------|---------------|--------|
| Background #0f1117 | #0f1117 | ✓ |
| Surface #1a1d27 | #1a1d27 | ✓ |

### Fonts
| Element | Spec | Implementation | Status |
|---------|------|---------------|--------|
| Body | 15px/1.7 | 15px/1.7 | ✓ |

### Features
| Feature | Spec Status | Implementation | Status |
|---------|-------------|----------------|--------|
| Empty State | defined | implemented | ✓ |
| Search UI | defined | implemented | ✓ |
| Copy button | defined | not found | ✗ |
```

### Step 4: 生成修复建议

对于每个不符合规范的项目，生成具体的修复代码。

## 输出格式

```markdown
# Design QA Report — {date}

## Summary
- Total checks: {n}
- Passed: {passed}
- Failed: {failed}
- Missing: {missing}

## Detailed Findings

### ✓ Passed
{list of passed checks}

### ✗ Failed
{list of failed checks with fix suggestions}

### ⚠ Missing (defined in DESIGN.md but not implemented)
{list of missing features}

## Recommended Actions
1. {action 1}
2. {action 2}
```

## 不做的事情

- 不修改代码（只生成报告）
- 不运行 Streamlit app
- 不检查运行时行为（只检查静态代码）
- 不检查非 DESIGN.md 定义的内容

## 相关技能

- `/topic-recompile` — 内容层面重编译
- `/browse` — 如需实际验证 UI 渲染效果，使用 browse 技能
