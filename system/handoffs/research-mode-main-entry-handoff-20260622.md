# Handoff: Research Mode as Main Entry Layout Transition (2026-06-22)

**日期**: 2026-06-22  
**状态**: 需求界定完成，待实施页面架构与文案升级  
**目标分支**: `main`

---

## 1. 任务背景与核心诉求

根据桌面文件 `/Users/jiawei/Desktop/Research mode 做主入口.md`，Feline Research OS 的长期定位是一个**面向猫疾病模型、猫药物研发、药效评价、PK/PD 和方案设计的研究操作系统 (Research OS)**，而不是一个普通的“猫病百科问答网页”或面向大众宠物主的工具。

当前 Streamlit 首页（`scripts/app.py`）将 “Quick explanations” 与 “Research mode” 作为平级的主入口并列展示，这会模糊产品定位，稀释核心差异化特征。

为了强化 “Research OS” 的专业定位，需将 **Research Mode 升级为“研究工作台”，做为主入口**；将 **Quick Explanations 降级为 “Quick Start” 或“快速理解/示例问题/概念速查”**，作为低门槛的 Onboarding 入口，并能够引导用户深入进行证据研究。

---

## 2. 方案设计与升级要点

### 2.1. 命名与概念调整 (Renaming & Mapping)
通过更具专业调性的词汇替代现有的通用模式称呼：

| 现有名称 | 升级后名称 (中/英) | 角色定位 |
|---|---|---|
| **Quick explanations** | `Quick Start` / `快速理解` (或 `概念速查` / `疾病速览`) | 辅助入口、建议问题、快速 Demo，不作为平级 mode |
| **Research mode** | `Research Workspace` / `研究工作台` (或 `Evidence Research` / `证据研究`) | 系统的核心主入口与交付终点，提供多维度证据链 |

### 2.2. 页面布局重塑 (UI Layout Restructuring)
首页不再采用平级并列的双模式框，而是采用层次化的卡片/按钮布局：
1. **主输入框**: `st.chat_input("Ask a feline research question...")`。
2. **主行动点**: 突出展示 `Start Evidence Research` (开始深度研究)。
3. **Quick Start (辅助引导)**: 缩小原 Quick explanations 区域，缩小卡片高度，变为一行/两行紧凑的 suggested questions 按钮：
   - 解释 CKD
   - FIP 怎么识别
   - IBD 和淋巴瘤怎么区分
   - HCM 是什么，为什么危险
4. **Research Workspace (核心功能快捷方式)**:
   - 搜索最新文献 (Search latest papers)
   - 浏览证据卡片 (Review evidence cards)
   - 打开专题档案 (Open disease dossiers)
   - 生成研究简报 (Generate research briefings)
   - 比较方法与终点 (Compare methods and endpoints)

### 2.3. 任务型提示词替换 (Task-Oriented Prompts)
将现有的“搜索引擎式”关键词替换为更契合 Research OS 的“任务型”表达，以展现学术专业度：

| 现有指令/提示词 | 升级后的任务型表达 |
|---|---|
| 搜索 HCM 最新文献 | 构建 feline HCM 近三年证据地图 |
| search the latest papers about feline CKD... | 比较 CKD 诊断与分期指标的研究价值 |
| 查找 FIP 最新治疗研究 | 梳理 FIP 治疗研究的药效终点 |
| find recent diabetes papers with clinical relevance | 提炼猫糖尿病模型的关键评价指标 |

### 2.4. 连接深度研究流程 (Bridging from Quick Start)
当用户点击 Quick Start 链接快速获取概念解释后，输出内容下方需提供按钮或行动建议：
- “🔬 进入 [Disease] Research Workspace”
- “📖 查看 [Disease] Briefing/Dossier”
- “🔍 查看相关 Evidence Cards”

---

## 3. 待修改的系统文件

1. **`scripts/app.py`**:
   - 修改 `EXAMPLE_QUESTIONS_BASIC` 和 `EXAMPLE_QUESTIONS_RESEARCH` 常量，将提示词替换为任务型表达。
   - 调整 `render_example_question_chips` 中的排版层级，缩小 Quick Start 卡片，强化 Research Workspace 的概念。
   - 更改相关的 label 字符串（如将 `st.markdown("🔬 研究模式 / Research mode")` 改为 `st.markdown("🔬 研究工作台 / Research Workspace")`）。
2. **`scripts/research_mode.py`**:
   - 确保提示词与研究流程在后台支持更复杂的输出结构（包含检索范围、证据卡片、局限性等）。

---

## 4. 执行与验证步骤 (Execution & Verification)

修改完成后，必须运行以下三件套以及 AST lint 检查以确保系统健康度：
```bash
# 1. 重新同步深度图索引
.venv/bin/python scripts/sync_indexes.py

# 2. 运行全局健康检查（退出码必须为 0）
.venv/bin/python scripts/health.py

# 3. 运行查询测试套件（113 个测试全部通过）
.venv/bin/python scripts/test_query.py

# 4. 运行 Streamlit key 检查器
.venv/bin/python .agents/skills/streamlit_key_guard/scripts/lint_streamlit_keys.py
```

---
*本接力文档由 Antigravity 整理，专用于引导下一阶段 Research Mode 主入口 UI 的过渡实施。*
