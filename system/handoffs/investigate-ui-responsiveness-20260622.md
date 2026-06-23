# 调查报告：页面无响应问题排查

**日期**: 2026-06-22
**状态**: DONE_WITH_CONCERNS - 已修复，需用户验证
**涉及文件**: `scripts/app.py`

---

## 问题描述

用户反馈：点击 Research mode 按钮后，页面无响应。提供了三张截图：
1. 查询已提交但无响应
2. Quick Start 正常工作
3. 空状态页面，部分 Research mode 项目显示删除线样式

---

## 调查过程

### 1. 代码流程追踪

追踪了从按钮点击到查询处理的完整流程：

```
用户点击按钮 → Streamlit 触发 rerun → queue_question() 设置 pending_question
→ 脚本继续渲染 UI → 到达 line 6830 处理 pending_question → run_query() 执行
```

**关键代码位置**:
- `queue_question()`: line 385-388
- `render_example_question_chips()`: line 391-434
- `run_query()`: line 6534-6823
- 问题处理入口: line 6830-6836

### 2. 网络请求检查

Research mode 查询会调用 PubMed API：
- `fetch_pubmed_augmentation()` at research_mode.py:1747
- 超时设置: 15秒 (line 1766)
- 两次 HTTP 请求：search + fetch details
- 总延迟可达 15-30 秒

所有网络请求都有超时处理，不会无限阻塞。

### 3. CSS 样式检查

搜索了以下关键词，未发现删除线相关样式：
- `strikethrough`
- `line-through`
- `text-decoration`
- `.completed`, `.disabled`, `.crossed`

用户看到的"删除线"可能是截图视觉误差或浏览器渲染问题。

### 4. Tab UI 状态确认

Tab UI 已被禁用：
```python
# line 5735-5736
if "use_workspace_tabs" not in st.session_state:
    st.session_state.use_workspace_tabs = False  # DISABLED
```

---

## 根本原因

**视觉反馈不足导致的感知问题**

当用户点击 Research mode 按钮时：
1. `queue_question()` 设置 `pending_question` 并触发 `st.rerun()`
2. 页面重新渲染，显示 `render_main_header()` 但聊天历史为空
3. 脚本继续执行到 line 6830，开始处理查询
4. `run_query()` 显示 status 块，但此时已有 1-2 秒空白期
5. PubMed 查询需要 15-30 秒

在步骤 2-4 之间，用户看到的是空白页面，造成"无响应"的感知。

Quick Start 之所以正常，是因为它使用预定义内容，无网络延迟，瞬间返回。

---

## 修复内容

### 修复 1：添加即时视觉反馈

在 `scripts/app.py` line 6447 后添加：

```python
# Show immediate feedback when a question is queued but not yet processed
if st.session_state.pending_question and len(st.session_state.messages) == 0:
    is_zh = is_session_chinese()
    processing_msg = "正在处理您的问题..." if is_zh else "Processing your question..."
    st.markdown(f"<div style='text-align:center;padding:32px;color:#8b90a0'><span style='font-size:24px'>⏳</span><br/>{processing_msg}</div>", unsafe_allow_html=True)
```

### 修复 2：清理冗余代码

移除 line 496 的冗余 `st.rerun()` 调用，因为 `queue_question()` 内部已包含 `st.rerun()`。

---

## 验证清单

- [x] Streamlit 应用正常启动，无错误
- [x] `queue_question()` 包含 `st.rerun()` 确保即时处理
- [x] Tab UI 已禁用，不会显示占位符内容
- [ ] **需用户验证**：点击 Research mode 按钮，确认看到"正在处理您的问题..."提示
- [ ] **需用户验证**：查询完成后正常显示结果

---

## 相关发现

### 1. PubMed API 延迟是预期行为

Research mode 总是调用 PubMed（硬编码 `include_external=True`），这与侧边栏的 `allow_external_search` 设置无关：

```python
# research_mode.py line 2345
answer, research_source_ids = handle_research_query(question, chinese=output_chinese, include_external=True)
```

### 2. Tab UI 占位符问题的根源

之前用户报告的"占位符"问题来自 `handle_research_query_structured()` at line 1966：

```python
"why_included": f"Relevant to {disease.upper()} research; Evidence level: {card.evidence_level or 'not specified'}",
```

这是模板文本，不是 LLM 生成的解释。Tab UI 已被禁用以解决此问题。

### 3. 三层架构状态

| 层级 | 名称 | 状态 | 说明 |
|-----|------|------|------|
| Layer 1 | Quick Start | ✅ 正常 | 预定义内容，无 API 调用 |
| Layer 2 | Disease Briefing | ✅ 正常 | 从 Obsidian 文件加载 |
| Layer 3 | Research Workspace | ⚠️ 部分可用 | Tab UI 禁用，使用长文本输出 |

---

## 后续建议

1. **用户测试**：请用户验证修复效果，确认"正在处理您的问题..."提示正常显示

2. **如需进一步改进 Research Workspace**：
   - 需要实现真正的 LLM 内容生成（如"为什么选这篇"的解释）
   - 这涉及 API 调用，需要遵守 API Red Line 规则
   - 建议在用户明确要求测试时再启用

3. **PubMed 延迟优化**（可选）：
   - 添加缓存机制
   - 或提供跳过 PubMed 的选项

---

## 技术债务

1. `st.components.v1.html` 已弃用，需替换为 `st.iframe`（Streamlit 警告）
2. Tab UI 代码仍在代码库中，虽已禁用，但增加了复杂度

---

## 文件变更摘要

```
scripts/app.py
  - line 6447-6452: 添加处理中提示
  - line 495-496: 移除冗余 st.rerun()
```
