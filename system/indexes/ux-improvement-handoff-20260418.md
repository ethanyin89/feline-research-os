---
title: UX Improvement Handoff — Streamlit App
date: 2026-04-18
status: active
from: claude-opus-4-6 (session 3)
to: next model
---

# UX Improvement Handoff — Streamlit App

## 30 秒现状

DESIGN.md 里定义的 5 个 UX 交互规范已经在 `2026-04-18` 分两轮落地到 `scripts/app.py`，之前缺的普通用户前端尾巴这轮也补上了。

当前现实：

- empty state 已实现，包含 vault stats、example chips、provenance guide
- empty state 现在还有 `How this works` 折叠 onboarding，首次展开，之后默认折叠
- empty state 和主界面现在都有更明确的 `research instrument` chrome，不再只是默认 Streamlit 标题 + caption
- empty state 不再和主标题重复渲染；现在是空白页走 hero，非空对话走标准 header
- sidebar search 已实现，调用 `search.py` 的 `vault_search()`
- 搜索结果现在可点击，会在主面板打开 preview；若是 source card，也会作为下一次问题的 preferred context
- sidebar search 结果现在也用了 panel card 样式，不再是纯 markdown + caption 堆叠
- error states 已改成普通用户可读的结构化提示
- 如果 0 个 source card 命中，前端现在直接停下并提示重写问题，不再硬 synthesize
- assistant answers 已有 `Copy markdown` 按钮
- provenance badge 已从实心块改成 tinted pill，颜色和 DESIGN.md 的语义层次现在更接近 preview 稿
- chat bubble、sidebar、input、button、expander 现在都有统一 dark surface / border treatment，产品感比默认 Streamlit 明显更强
- backend 状态、search 空结果、low-confidence、query failure 现在也走统一 notice 语言，不再主要依赖原生 `st.warning()` / `st.error()` 盒子
- sidebar 底部 runtime 信息现在是单独 panel，不再是 3 行松散 caption
- search snippet 现在会高亮命中的 query，而不是只显示一块原始 code 文本
- `Files loaded / Last query debug` 现在也换成更普通用户语义的 `Readings used / Answer summary`
- sidebar 的主控制现在分成：
  - `Answer engine`
  - `Condition`
  - `Advanced settings`
  普通用户默认先看到常用控制，`Max hops / auto-save` 不再直接铺在第一层
- `Search vault` 也已换成更普通用户语义的 `Find by keyword`
- sidebar 底部 `Runtime` 已换成 `App status`
- `Auto-save answers to outputs/qa/` 已进一步压成 `Auto-save answers`
- `Answer summary` 里现在优先展示普通用户关心的 `Topic / Confidence / Sources / Figures / Save this answer`
- `Answer style / depth / estimated size` 已下沉到内层 `More details`
- 普通用户路径里残留的 `source cards / loaded evidence` 术语已继续压成 `sources / cited sources`
- selected search preview 现在也更 reader-first：`Selected search result` 改成 `Selected reading`，清除按钮改成 `Clear this selection`
- `No source cards matched your question` 这类报错也已改成普通用户语气，不再暴露内部对象名
- search 结果里的 `hits` 已改成更普通用户的 `matches`，按钮也从 `Open in main pane / Use in next answer` 改成 `Preview / Use for next answer`
- sidebar 的 `Context loaded / Last answer details / Technical details` 这组也继续收口为 `Readings used / Answer summary / More details`
- answer summary 首屏项里 `Focus disease` 也已压成更自然的 `Topic`
- sidebar 顶部控制里的 `Focus disease` 也继续压成了 `Condition`
- query failure 折叠项从 `Technical details` 改成 `Error details`
- `App status` 里 `model` 也已换成更普通用户的 `engine`
- provenance badge 可见词也继续去内部术语化：`quoted_fact / llm_inference` 已改成 `quote / inference`
- `More details` 里的 `Question type / Estimated tokens` 也已压成 `Answer style / Estimated size`
- sidebar 的 `Last query debug` 现在有单击 `Save as .md`
- README 的普通用户入口已简化
- `scripts/query.py` 现在认识 `preferred_source_ids` 和 `NoSourceCardsLoadedError`，CLI 与 Streamlit 行为一致
- live runtime 现已确认：本地 `8501 / 8502` 两个 Streamlit 实例都存活，`/_stcore/health` 均回 `200 ok`
- 当前环境里 `streamlit` 依赖未安装，所以 live smoke test 仍需在装好依赖的 shell 里补跑

## 验证命令（先跑这 3 条）

```bash
python3 scripts/test_query.py                                       # 68/68 pass as of 2026-04-21
python3 -m streamlit run scripts/app.py --server.headless true &     # Streamlit 启动
sleep 2 && curl -s http://localhost:8501 | head -5                   # 能访问
```

## 需要改的文件

| 文件 | 行数 | 改什么 |
|------|------|--------|
| `scripts/app.py` | 主要改动已完成 | 已加 empty state、search sidebar、search preview/context、error UX、copy/export |
| `scripts/search.py` | 216 行 | **不改**，只需 import `vault_search` |
| `scripts/query.py` | 1195+ 行 | 已小改：支持 preferred source preload + `NoSourceCardsLoadedError` |
| `DESIGN.md` | 443 行 | **不改**，规范已写好，读它就行 |

## 第三轮视觉收口（本次继续）

这轮不是重新设计，而是把 preview 里的 visual language 真正压进真实 Streamlit UI：

1. provenance badge 改成 tinted pill，而不是实心块
2. empty state 改成 hero + panel，而不是纯 caption 堆叠
3. sidebar header 改成 panel card，强调这是研究工具而不是默认 demo
4. chat / input / sidebar / expander 统一 dark chrome，减少 Streamlit 原生感
5. 修掉 empty-state 与主标题重复的真实 UI bug，并把 search/context 区块统一进同一套 card 语言
6. 把 status / error / low-confidence / runtime footer 统一成同一套 notice-and-panel 语气
7. 把 search snippet 和 sidebar panel 命名也压到更接近普通用户，而不是开发者术语
8. 把 sidebar 设置按常用 / 高级分层，降低第一屏工具感
9. 把回答详情里的调试项继续下沉，避免普通用户直接看到内部路径和 token/hops 术语

## 这一轮实际改了什么

改动都在 [scripts/app.py](../../scripts/app.py#L40)：

- `BADGE_PATTERNS` 现在输出带半透明底色和边框的 provenance badge
- 新增 `EMPTY_STATE_INTRO_HTML` 和 `HOW_IT_WORKS_HTML`
- CSS injection 现在覆盖：
  - app background / header / sidebar
  - chat bubble surface
  - button / input / expander / chat input chrome
  - `.vault-hero` / `.vault-panel` / `.prov-badge` 这些内部 UI primitive
- sidebar 标题区不再是 `st.title + st.caption`，而是一个固定 panel card
- 空白页与主界面现在分两套 header：
  - empty state 走 `vault-hero`
  - 有对话后走 `render_main_header()`
- 搜索结果与 selected search context 现在都使用同一套 `vault-search-card` / `vault-inline-note` 视觉原语
- 新增 `render_notice()`，统一处理：
  - backend availability
  - query failure
  - no source cards
  - no search results
  - low confidence
- sidebar footer 现在是 `vault-sidebar-meta` panel，而不是 caption 堆叠
- 新增 `highlight_search_snippet()` / `render_search_snippet()`，让 sidebar search 结果更可扫读
- sidebar expander 命名已改成：
  - `Context loaded`
  - `Last answer details`
- sidebar controls 已重新分层：
  - visible: `Answer engine`, `Focus disease`
  - collapsed: `Advanced settings`
- search section 已改名为 `Find by keyword`
- runtime footer 已改名为 `App status`
- auto-save 文案已去掉内部目录路径
- save CTA 已改成 `Save this answer`
- answer details 现在默认 reader-first，technical 项目被下沉到内层 expander

关键定位点：

- provenance badge HTML: [scripts/app.py](../../scripts/app.py#L40)
- empty-state hero: [scripts/app.py](../../scripts/app.py#L89)
- search card template: [scripts/app.py](../../scripts/app.py#L98)
- notice helper: [scripts/app.py](../../scripts/app.py#L250)
- search snippet highlight: [scripts/app.py](../../scripts/app.py#L258)
- main header split: [scripts/app.py](../../scripts/app.py#L303)
- visual CSS primitives: [scripts/app.py](../../scripts/app.py#L311)
- sidebar research card: [scripts/app.py](../../scripts/app.py#L601)
- sidebar control split: [scripts/app.py](../../scripts/app.py#L807)
- runtime footer panel: [scripts/app.py](../../scripts/app.py#L920)
- reader-first answer details: [scripts/app.py](../../scripts/app.py#L927)

## 5 个实现任务（状态）

### Task 1: Empty State（最高优先）

**状态：已完成**

**DESIGN.md 位置：** "## Empty State" section

**当前问题：** 用户打开 app 看到空白页 + "Ask the vault" 标题 + 空聊天框。不知道该问什么。

**要做的事：**

在 `app.py:284`（`st.title("Ask the vault")` 之后），检测 `st.session_state.messages` 是否为空，如果为空则渲染：

1. **Vault stats line**
   ```python
   source_index = get_source_index()
   topic_count = len(list((VAULT_ROOT / "topics").rglob("*.md")))
   st.caption(f"{len(source_index)} sources · {topic_count} topic pages · 5 diseases")
   ```

2. **Example question chips**（5 个，每个病种一个）
   ```python
   EXAMPLE_QUESTIONS = [
       "CKD 的 SDMA 作为早期 biomarker 的证据有多强？",
       "Compare FIP treatment options: GS-441524 vs molnupiravir",
       "IBD 的诊断排除流程是什么？",
       "What HCM screening endpoints are usable today?",
   ]
   ```
   - 用 `st.button()` 渲染，点击后触发 `run_query()`
   - Streamlit 的 button 点击需要配合 `st.session_state` 管理状态

3. **Provenance guide**（3 行，展示 badge 颜色含义）
   ```python
   st.markdown("""
   <div style="margin-top:24px;padding:16px;background:#1a1d27;border-radius:6px;border:1px solid #2d3147">
     <div style="font-size:13px;color:#8b90a0;margin-bottom:8px">Provenance guide:</div>
     <div><span style="background:#16a34a;color:#fff;padding:1px 6px;border-radius:3px;font-size:0.75em">quote</span> direct quote from source</div>
     <div style="margin-top:4px"><span style="background:#ca8a04;color:#fff;padding:1px 6px;border-radius:3px;font-size:0.75em">supported</span> supported by the cited sources</div>
     <div style="margin-top:4px"><span style="background:#6b7280;color:#fff;padding:1px 6px;border-radius:3px;font-size:0.75em">inference</span> goes beyond the cited sources</div>
   </div>
   """, unsafe_allow_html=True)
   ```

**关键约束：** 只在 `len(st.session_state.messages) == 0` 时显示。对话开始后消失。

---

### Task 2: Search UI（sidebar）

**状态：已完成**

**DESIGN.md 位置：** "## Search UI" section

**当前问题：** `search.py` 只有 CLI，Streamlit 里没有搜索功能。

**要做的事：**

在 `app.py` sidebar 的 `st.divider()` 之后（约 line 227），加一个搜索区：

```python
from search import vault_search

st.divider()
st.markdown("**Find by keyword**")
search_query = st.text_input("Keyword", placeholder="phosphorus, SDMA, fibrosis...", label_visibility="collapsed")
search_scope = st.radio("Scope", ["All", "Raw", "Topics"], horizontal=True, label_visibility="collapsed")

if search_query:
    scope_map = {"All": "all", "Raw": "raw", "Topics": "topics"}
    results = vault_search(search_query, VAULT_ROOT, scope=scope_map[search_scope], limit=5)
    if results:
        for r in results:
            id_tag = f"**{r['id']}**" if r["id"] else r["file"]
            title_tag = f" — {r['title']}" if r["title"] else ""
            st.markdown(f"{id_tag}{title_tag} ({r['matches']} hits)")
            if r["snippets"]:
                st.code(r["snippets"][0][:200], language=None)
    else:
        st.caption("No results")
```

**关键约束：**
- `search.py` 已经在 `sys.path` 里（`app.py:26` 已设置），直接 `from search import vault_search` 即可
- `vault_search()` 返回 `list[dict]`，每个 dict 有 `file`, `id`, `title`, `matches`, `snippets`
- 最多展示 5 条结果
- search 和 chat 是独立功能，搜索结果不自动变成 query context

---

### Task 3: Error States

**状态：已完成**

**DESIGN.md 位置：** "## Error & Edge States" section

**当前问题：** 错误信息对非开发者没用。`"Query failed: {e}"` 看不懂。

**要改的地方：**

1. **Disease detection failure** (`app.py:316-320`)
   - 当前：`st.warning("Could not detect disease...")`
   - 改为：更友好的措辞 + 重新展示 example question chips

2. **API failure** (`app.py:322-324`)
   - 当前：`st.error(f"Query failed: {e}")`
   - 改为：结构化错误信息（plain English 解释 + 建议步骤 + 折叠的技术详情）
   ```python
   st.error("Query failed")
   st.markdown("""
	   **What to try:**
	   - Check your API key is set correctly
	   - Try switching between Anthropic (API) and OpenRouter (API) in the sidebar
	   - If local Ollama is intentionally enabled, make sure it's running: `ollama serve`
   """)
   with st.expander("Error details"):
       st.code(str(e), language=None)
   ```

3. **Low confidence**（新增）
   - 在 `run_query()` 末尾，`compute_confidence()` 之后
   - 如果 `confidence == "low"`，在答案下方加低置信度提示，说明回答明显超出了 cited sources

---

### Task 4: Copy Markdown Button

**状态：已完成**

**DESIGN.md 位置：** "## Copy / Export Actions" section

**当前问题：** 用户拿到好答案，没法复制或分享。

**实现方式：**

Streamlit 没有原生 clipboard API。用 `st.components.v1.html()` 注入 JS：

```python
import streamlit.components.v1 as components

def copy_button(text: str, key: str):
    escaped = text.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")
    components.html(f"""
    <button onclick="navigator.clipboard.writeText(`{escaped}`).then(()=>{{this.textContent='Copied';this.style.color='#16a34a';setTimeout(()=>{{this.textContent='Copy markdown';this.style.color='#8b90a0'}},2000)}})"
    style="background:none;border:none;color:#8b90a0;cursor:pointer;font-family:Geist,system-ui;font-size:11px;padding:4px 0">
    Copy markdown</button>
    """, height=30)
```

在每条 assistant message 渲染后调用 `copy_button(msg["content"], key=f"copy-{i}")`。

**注意：** `st.components.v1.html()` 在 Streamlit 里是 iframe，复制按钮的高度需要设对（~30px），否则会有多余空白。

---

### Task 5: README 简化（可选）

**状态：已完成**

**当前问题：** `README.md` 第 92-131 行有 40+ 个 system index 链接，信息过载。

**建议：**
- "Start Here" section 只保留 `reader-start-here.md` 一个链接
- 维护者链接移到 `## For Maintainers` 折叠区
- 普通用户看到的 README 应该只有 3 件事：Chat UI 怎么启动、Obsidian 怎么打开、CLI 怎么搜索

---

## app.py 当前结构（改动参考）

```
scripts/app.py (400 行)
├── L1-11      docstring
├── L12-38     imports + query.py 函数导入
├── L44-63     BADGE_PATTERNS + render_provenance()
├── L76-85     cached resources (get_client, get_source_index)
├── L91-138    page config + CSS injection (Geist fonts)
├── L145-170   backend selection + API key guard
├── L176-268   sidebar (backend/disease/hops/write-back/debug)
├── L270-278   session state init
├── L280-291   chat history display          ← Task 1 在这之后
├── L297-388   run_query() 函数              ← Task 3 改错误处理
├── L395-400   chat input + trigger          
```

**import 需要新增：**
```python
from search import vault_search    # Task 2
```

**session_state 需要新增：**
```python
if "search_results" not in st.session_state:
    st.session_state.search_results = []
```

## 设计系统约束（必须遵守）

```
1. 读 DESIGN.md 再动手。所有颜色、字体、间距都定义在那里。
2. 只用 3 个 accent 颜色：#16a34a (green), #ca8a04 (amber), #6b7280 (gray)。不加新颜色。
3. 字体：Geist Sans (正文) + Geist Mono (代码/metadata)。CSS 已注入。
4. 暗色模式 only。背景 #0f1117，Surface #1a1d27。
5. provenance badges 是唯一的彩色元素。不要加蓝色/紫色/渐变。
6. 所有 metadata（source ID、文件路径、token 数）用 Geist Mono 11px #8b90a0。
```

## 测试验证

实现后需要检查：

```bash
# 1. 测试套件不能 break
python3 scripts/test_query.py   # 68/68 pass

# 2. Streamlit 能启动
python3 -m streamlit run scripts/app.py

# 3. 手动检查清单
- [ ] 打开 app，看到 empty state（example chips + vault stats + provenance guide）
- [ ] 点击 example chip，query 正常执行
- [ ] 对话开始后 empty state 消失
- [ ] sidebar 搜索框输入关键词，结果正确展示
- [ ] 故意输入无法识别病种的问题，看到友好错误信息
- [ ] 每条 assistant message 下方有 "Copy markdown" 按钮
- [ ] 点击 Copy，粘贴到其他地方，provenance tags 完整
```

## 不要重做

- `scripts/query.py`（1195+ 行，稳定，68/68 tests pass as of 2026-04-21）
- `scripts/search.py`（216 行，稳定）
- `scripts/test_query.py`（68 tests as of 2026-04-21）
- `DESIGN.md`（443 行，规范已完成）
- CSS injection（`app.py:97-138`，Geist 字体已正确配置）
- provenance badge rendering（`app.py:44-63`，工作正常）
- sidebar 现有控件（backend/disease/hops/write-back/debug）

## 关键文件速查

| 用途 | 文件 |
|------|------|
| UX 规范 | `DESIGN.md`（完整读一遍再动手） |
| 主要改动目标 | `scripts/app.py` |
| 搜索 API | `scripts/search.py`（`vault_search()` 函数签名见上方） |
| 查询引擎 | `scripts/query.py`（不改，只用已导出的函数） |
| 测试基线 | `scripts/test_query.py`（68/68 pass） |
| 项目约束 | `system/indexes/karpathy-alignment-handoff-20260418.md` |
