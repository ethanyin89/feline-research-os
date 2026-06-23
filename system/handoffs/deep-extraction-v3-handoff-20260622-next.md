# Handoff: Deep Extraction V3 & Vault Health Alignment (2026-06-22)

**日期**: 2026-06-22  
**状态**: 基础 UI 架构完成，待进行桌面 Draft 内容完整恢复与事实数据校准  
**目标分支**: `main`

---

## 1. 任务背景与核心要求
当前任务的目标是根据桌面（Desktop）上修改时间为 6 月 22 日 11:52 AM – 12:38 PM 的三个专家评审草稿（Draft），对当前 Feline Research OS 的**深度提炼（Deep Extraction）**进行数据和内容的对齐校准，解决其中的截断、事实错误和统计学不一致问题。

## 2. 待完成的工作与解决步骤

### 2.1. 恢复深度提炼文件的完整内容（解决截断问题）
工作区中的深度提炼文件（存储于 `raw/deep-extractions/`）相比桌面上的 Draft 缺失了重要章节（如“对宠物药/模型/药效评价的启发”、“局限与阅读时的边界”、“最终压缩版结论”以及详细的“Phase 3 自检”子章节）。
需要将以下桌面文件中的完整内容移植并合并回工作区中：
1. **HCM 205**:
   - 桌面文件: `/Users/jiawei/Desktop/Prevalence of Hypertrophic Cardiomyopathy and ALMS1 Variant in Sphynx Cats in New Zealand deep extract.md`
   - 工作区目标文件: `raw/deep-extractions/ext-src-hcm-205.md`
2. **HCM 076**:
   - 桌面文件: `/Users/jiawei/Desktop/*Left Atrioventricular Coupling Index in Feline Hypertrophic   Cardiomyopathy: Association with Disease Severity and Arterial   Thromboembolism.* 2026.  deep extract.md`
   - 工作区目标文件: `raw/deep-extractions/ext-src-hcm-076.md`
3. **Diabetes 025**:
   - 桌面文件: `/Users/jiawei/Desktop/Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues. 2024.deep extract.md`
   - 工作区目标文件: `raw/deep-extractions/ext-src-diabetes-025.md`

### 2.2. 修正 hcm-076 的 FATE 关联几率比 (OR) 事实错误
* **发现问题**: `ext-src-hcm-076.md` 中引用的 FATE（动脉血栓栓塞）的 Odds Ratio (OR) 错写为了 `OR = 6.8`。该数值错误地复制自 Draft 中提到的人类 MESA 队列研究。
* **正确数据**: 真实的猫 HCM 研究数据（参考 `raw/papers/src-hcm-076.md`）中的几率比为 `OR = 4.65` (95% CI: 1.405–29.215, p = 0.020)。
* **执行动作**: 修正 `raw/deep-extractions/ext-src-hcm-076.md` 中引用的 `OR = 6.8` 为 `OR = 4.65`，确保其与 source card 事实完全一致。

### 2.3. 修正 hcm-205 的流行病学统计数据不一致
* **发现问题**: source card `raw/papers/src-hcm-205.md` 标记了 `Prevalence of HCM: 40% (20/55 cats)`。然而，20/55 的计算结果是 36.4%，这在原论文摘要中是个排版/编辑错误。论文正文的病例构成和实际分析明确支持最终累计诊断为 **22/55只猫，即 40.0%**（代表 1.8 年随访后的累计发病率）。
* **执行动作**:
  1. 将 `raw/papers/src-hcm-205.md` 中的 `quoted_fact` 由 `40% (20/55 cats)` 修正为 `40.0% (22/55 cats)`，消除此统计学矛盾。
  2. 确保在 `raw/deep-extractions/ext-src-hcm-205.md` 中对此事实进行了正确的解释。

### 2.4. 同步索引与全局验证 (Index Sync & Health Gate)
内容和卡片更新后，必须执行以下验证命令：
```bash
# 1. 重新同步深度图索引
.venv/bin/python scripts/sync_indexes.py

# 2. 运行全局健康检查（必须通过且退出码为 0）
.venv/bin/python scripts/health.py

# 3. 运行查询测试套件（113 个测试必须全部 PASS）
.venv/bin/python scripts/test_query.py
```

---

## 3. 关键规则与约束

1. **绝对禁止伪造数据 (No Fake Data)**: 所有的修改、指标与数据提取必须基于原文及 Draft 中的真实描述，不可自行虚构。
2. **Streamlit 唯一 Widget Key 限制 (Duplicate Key Hazard)**: 
   - 任何在聊天日志渲染循环（如 `render_answer_block`、`render_source_card_v2`）中输出的 Streamlit Widget 必须传入 `key_prefix` 或动态 index。
   - 修改后运行 AST 检测工具进行合规性验证：
     ```bash
     .venv/bin/python .agents/skills/streamlit_key_guard/scripts/lint_streamlit_keys.py
     ```
3. **排版规范**:
   - 深度提炼页面的正文需保持 `Source Serif 4` 衬线体以符合学术阅读体验。

---

## 4. 相关文件速查
* **工作区深度提炼存盘**: `raw/deep-extractions/ext-*.md`
* **论文 Source Cards**: `raw/papers/src-*.md`
* **Streamlit 主程序**: `scripts/app.py`
* **提炼解析器**: `scripts/deep_extraction.py`
* **Research Mode 渲染**: `scripts/research_mode.py`
