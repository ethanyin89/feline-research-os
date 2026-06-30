# Public Test Debug 与第三批内容层接力文档

**日期**: 2026-06-26 15:23 CST
**当前分支**: `material-reading`
**最新相关提交**: `b555096 docs(content): add third obesity batch workspace review`
**本轮状态**: 公开测试入口已本地修复并验证；公网测试链接尚未创建。第三批 Obesity/Diabetes 深度材料已全部提供并完成复核记录，但最终 Evidence Map / Research Workspace 产物还未完整落盘。

---

## 1. 本轮任务判断

用户最新要求是：

1. `continue, debug, and show me the test link`
2. 随后改为：`写一下接力文档`

因此当前工作属于两条线：

| 线 | 类型 | 状态 |
|---|---|---|
| 公开测试页 / test link | 排查 + debug | 本地修复完成，公网 link 未开 |
| 第三批 deep extract 内容层 | 检查 + 内容产物接力 | 材料复核完成，最终产物待继续 |

---

## 2. 公开测试页 Debug 进展

### 已发现的问题

`scripts/public_test_app.py` 原本只能处理：

- `/health`
- `/`
- `POST /ask`

但 public-test-link 流程需要的普通用户测试入口没有完整支持：

- `/public-test-health.html`
- `/intake-parser.html`
- `/intake-parser.html?request=...&disease=...#decision-path`
- replay 页面上的 `#decision-path`
- 可见入口 `查看决策路径`
- 可复制路径按钮 `复制路径链接`
- `obesity` 疾病范围选项

另外，Obesity replay 页面虽然显示了本地命中，但 decision path 里的 `Loaded source count` 是 0，和实际证据命中不一致。

### 已修改文件

只修改了：

- `scripts/public_test_app.py`

主要改动：

1. 增加 `obesity` 到 disease dropdown 和 POST/GET allowlist。
2. 增加 `/public-test-health.html`，返回公开测试哨兵页：
   - `Ask the Vault public test sentinel`
   - `status: ok`
   - `product: Feline Research OS`
3. 增加 `/intake-parser.html`：
   - 无 query 时返回产品页，并显示 `Decision path ready`
   - 有 `request` query 时执行本地 replay
4. 增加 `render_decision_path(...)`：
   - 页面包含 `<section id="decision-path">`
   - 显示 `查看决策路径`
   - 提供 `复制路径链接` 按钮
5. 增加 `evidence_ids_for_answer(...)`：
   - 优先读取 `loaded_source_ids`
   - 若本地检索回答只有“本地命中”列表，则从 `- \`...\` —` 中提取 evidence id / path
   - 修正 Obesity replay 的 `Loaded source count: 0` 问题

### 已完成本地验证

当前使用新代码启动了本地测试服务：

```bash
OPENROUTER_DAILY_BUDGET_USD=1.00 OPENROUTER_MODEL=openai/gpt-4.1-mini python3 scripts/public_test_app.py --host 127.0.0.1 --port 8513
```

本地验证通过：

| URL | 结果 | 关键检查 |
|---|---|---|
| `http://127.0.0.1:8513/` | 200 | 根页可访问，包含 `Obesity` option |
| `http://127.0.0.1:8513/public-test-health.html` | 200 | health sentinel 正确 |
| `http://127.0.0.1:8513/intake-parser.html` | 200 | 产品页显示 `Decision path ready` |
| `...request=解释CKD&disease=ckd#decision-path` | 200 | `Loaded source count: 4` |
| `...request=FIP怎么识别&disease=fip#decision-path` | 200 | `Loaded source count: 3` |
| `...request=猫肥胖和糖尿病的证据关系&disease=obesity#decision-path` | 200 | `Loaded source count: 3` |

代码检查通过：

```bash
python3 -m py_compile scripts/public_test_app.py
git diff --check -- scripts/public_test_app.py
```

### 尚未完成

还没有创建公网临时测试链接。

下一步应执行：

```bash
npx --yes localtunnel --port 8513
```

拿到 `https://*.loca.lt` 后，用公开 URL 检查：

```bash
bash scripts/check_public_test_page.sh https://YOUR-TUNNEL.loca.lt
```

还应额外检查这些路径：

```text
/
/public-test-health.html
/intake-parser.html
/intake-parser.html?request=%E8%A7%A3%E9%87%8ACKD&disease=ckd#decision-path
/intake-parser.html?request=FIP%E6%80%8E%E4%B9%88%E8%AF%86%E5%88%AB&disease=fip#decision-path
/intake-parser.html?request=%E7%8C%AB%E8%82%A5%E8%83%96%E5%92%8C%E7%B3%96%E5%B0%BF%E7%97%85%E7%9A%84%E8%AF%81%E6%8D%AE%E5%85%B3%E7%B3%BB&disease=obesity#decision-path
```

如果公网链接检查通过，再只提交 `scripts/public_test_app.py`。

---

## 3. 当前 Git 状态

本轮 debug 改动：

- `M scripts/public_test_app.py`

工作树中已有的内容层未提交文件，不是本轮 debug 产生，不能误删或回滚：

- `M outputs/gold_standards/diabetes_model_endpoints/research_workspace_gold.md`
- `?? outputs/gold_standards/diabetes_model_endpoints/paper_cards/src-diabetes-025.json`
- `?? outputs/gold_standards/diabetes_model_endpoints/paper_cards/src-diabetes-025.md`
- `?? outputs/gold_standards/diabetes_model_endpoints/topic_task_card.yaml`
- `?? outputs/gold_standards/diabetes_treatment_remission/`
- `?? outputs/gold_standards/obesity_insulin_resistance/`
- `?? scratch/topic1_summary.txt`
- `?? scripts/extract_batch1.py`

注意：后续如果要提交公开测试修复，只 add/commit：

```bash
git add scripts/public_test_app.py
git commit -m "fix(test): add public replay health and decision path routes"
```

---

## 4. 第三批内容层状态

用户确认第三批 deep extract 材料已全部提供，共 10 篇：

1. Feline comorbidities: Pathophysiology and management of the obese diabetic cat
2. Comparative Aspects of Human, Canine, and Feline Obesity and Factors Predicting Progression to Diabetes
3. GLUT4 but not GLUT1 expression decreases early in the development of feline obesity
4. Insulin Sensitivity Decreases with Obesity, and Lean Cats with Low Insulin Sensitivity are at Greatest Risk of Glucose Intolerance with Weight Gain
5. Obesity-induced changes in gene expression in feline adipose and skeletal muscle tissue
6. The cat as a model for human obesity: insights into depot-specific inflammation associated with feline obesity
7. Metabolic Profiles of Feline Obesity Revealed by Untargeted and Targeted Mass Spectrometry-Based Metabolomics Approaches
8. Association between Gut Microbiota and Metabolic Health and Obesity Status in Cats
9. The effect of obesity and subsequent weight reduction on cardiac morphology and function in cats
10. Identifying the target population and preventive strategies to combat feline obesity

最近相关提交显示第三批复核已经推进：

```text
b555096 docs(content): add third obesity batch workspace review
ca449d4 fix(content): reconcile third obesity batch review state
b9530db feat(content): ingest obesity microbiota cardiac prevention extracts
4bc96a2 feat(content): ingest obesity metabolomics inflammation extracts
```

但当前文件状态显示：

- `outputs/gold_standards/obesity_insulin_resistance/topic_task_card.yaml` 已存在
- `outputs/gold_standards/obesity_insulin_resistance/` 目录尚未看到完整 `evidence_map.md` / `research_workspace_gold.md` 成品

因此下一阶段不要重新问用户材料列表，应直接继续做：

1. 检查 10 篇 deep extract 是否全部被转换成 paper card 或等价结构。
2. 构建 `outputs/gold_standards/obesity_insulin_resistance/evidence_map.md`。
3. 生成 `outputs/gold_standards/obesity_insulin_resistance/research_workspace_gold.md`。
4. 按用户提供的规则文档复核：
   - `/Users/jiawei/Desktop/给定 1 篇或多篇参考文献，如何稳定产出“像 Research Workspace 里那种有证据、有判断、有推荐理由、有转化价值的高质量结果”.md`
5. 重点检查每一个关键判断是否能回到具体原文段落，而不是只回到论文级别。

---

## 5. 内容层必须遵守的规则

从用户多次强调中继承的硬约束：

1. 不是摘要任务，而是 Research Workspace 级产物。
2. 每一个关键判断都必须能一键回到原文，并定位到支撑判断的具体段落。
3. 不能把“文献中出现过”写成“已经证明”。
4. 不能把 obesity、insulin resistance、diabetes progression 三者混成一个未经分层的因果链。
5. 猫内证据优先；任何人/犬/跨物种对照只能作为转化背景，不能替代 feline evidence。
6. Evidence label 必须区分：
   - 直接原文事实
   - 多文献来源支持
   - 分析推断
7. 对第三批特别要分清：
   - 肥胖作为风险状态
   - 胰岛素敏感性下降作为机制/中间状态
   - 糖耐量异常或糖尿病作为进展终点
   - 炎症、脂肪组织、骨骼肌 GLUT4、metabolomics、microbiota、cardiac morphology 这些只是机制层或伴随层，不应自动升级为临床终点

---

## 6. 推荐下一步顺序

### A. 先完成公开测试链接

1. 保持或重启 8513 本地服务。
2. 开 localtunnel。
3. 用公开 URL 跑：
   - `scripts/check_public_test_page.sh`
   - 三个 replay URL
4. 通过后提交 `scripts/public_test_app.py`。
5. 把公开 test link 发给用户。

### B. 再回到内容层

1. 不要重新从用户收材料。
2. 从现有 deep extract / gold standard 文件检查第三批 10 篇是否已入结构。
3. 若缺 paper cards，补齐到 `outputs/gold_standards/obesity_insulin_resistance/paper_cards/`。
4. 生成 evidence map 和 workspace gold。
5. 做逐条 claim traceability 复核。

---

## 7. 对下一位模型的提醒

- 当前请求已经从“给 test link”切到“写接力文档”，不要在用户没有重新要求前继续开公网隧道。
- 8513 本地服务可能还在运行，但不应假设公网 link 已存在。
- 不要回滚或清理未提交内容层文件，它们大概率是前面材料处理的中间产物。
- 若要提交 debug 修复，只提交 `scripts/public_test_app.py`。
- 若继续内容层，优先处理 `obesity_insulin_resistance`，不要回到第一批/第二批重新确认材料列表。
