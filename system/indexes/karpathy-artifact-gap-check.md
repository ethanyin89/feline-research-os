---
id: system-karpathy-artifact-gap-check
type: system
topic: system
question_type: audit
language: zh
last_compiled_at: 2026-04-09
confidence: medium
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Karpathy Artifact Gap Check

这页只回答一个问题：

`为什么当前执行出来的产物，和 Karpathy 分享里那种 LLM knowledge base 的感觉，还是差很多？`

## 类型判断

这件事属于：

`检查`

因为你现在不是在提新想法，也不是在排查某个坏掉的点。

你是在看：

- 当前系统已经产出了什么
- 这些产物的形态像不像 Karpathy 说的那个东西
- 差距主要落在“产品表面”还是“系统内核”

## 最短结论

当前 `feline-research-os` 的内核，已经明显在 Karpathy 那条路上。

但当前可见产物，还是更像：

`高纪律的研究文档系统`

而不是：

`一个可以直接 ask、直接得到活的 wiki 页面、并且查询会自然沉淀回系统的知识表面`

差距不小。而且是用户能立刻感受到的差距。

## 真正像的部分

当前系统和 Karpathy 分享真正对上的，不是表面，而是骨架：

1. 有 `raw -> compile -> output -> write-back -> health check`
2. 有 source card、topic、entity、synthesis、output 这些明确层级
3. 有“查询结果会沉淀回系统”的 write-back 逻辑
4. 有比普通 AI note 更硬的 trust / audit discipline

也就是说：

`底层编译纪律，你已经做得比很多“AI knowledge base”概念图更真。`

## 真正不像的部分

真正不像的地方，主要有 5 个。

### 1. 产物还是“导航文档优先”，不是“查询表面优先”

Karpathy 那种感觉最强的一点是：

- 人先问
- 系统先答
- 答案天然落在 wiki 结构里

而你现在普通用户看到的，还是：

- 先选 navigation
- 再选 dashboard
- 再选 synthesis / topic / output

这更像维护者友好的资料入口，不像 query-native surface。

### 2. 当前页面更像“整理好的说明页”，不像“活的研究对象”

Karpathy 分享里最迷人的部分，不是“有很多 markdown”。

而是那种感觉：

- 这个 wiki 本身正在被持续编译
- 你每次问，像是在碰一个活系统

而你现在的大部分产物，哪怕质量已经不低，看上去还是偏静态：

- dashboard
- navigation
- memo
- briefing

它们更像高质量文件，不像一个正在生长的知识界面。

### 3. ask layer 还不够可见

Karpathy 的分享里，`ask the wiki` 是前台动作。

你现在其实已经有不少可以被问的结构：

- topic
- synthesis
- entity
- output

但这些结构还主要是“给人手动点开”的。

还没有一个足够清晰的前台表面，让用户感觉：

`我是在问这套系统，不是在浏览一堆文件。`

### 4. write-back 是真的，但产品感还不够直接

现在 write-back 已经存在。

但它更像内部工作流：

- 先做 extraction
- 再写 memo
- 再回写 topic / synthesis

Karpathy 那种产品感更强的地方在于：

`用户会直接感觉到，这次探索让系统本身变厚了。`

而当前这件事更多只有维护者能感觉到。

### 5. 你现在更强的是“可信度控制”，不是“使用流畅度”

这是一个非常关键的现实。

当前系统最强的地方，其实不是 Karpathy 味最浓的地方。

最强的是：

- compile discipline
- verification boundary
- bilingual control
- auditability

这些东西非常值钱。

但它们偏后端控制层。

Karpathy 分享最打人的地方，反而偏前台体验层：

- 原始资料进来
- 很快长成 wiki
- 可以不断问
- 会不断沉淀

所以当前差距，不是“没有内核”。

而是：

`内核比表面更成熟。`

## 这意味着什么

这意味着当前项目不是走偏了。

而是走成了一个和 Karpathy 展示顺序相反的版本：

- 你先把纪律和可审计性打厚了
- 但 query-native、wiki-native、ask-native 的表面还没长出来

这不是坏事。

但如果不承认这个差距，后面会一直误判：

以为“我们已经很像了”。

其实没有。

`我们更像一个做对了底层的 research OS prototype，还不像一个已经把产品表面打穿的 LLM knowledge base。`

## 当前最该补的，不是更多页面

如果目标是更接近 Karpathy 分享的那个感觉，最该补的不是再多写几张 memo。

最该补的是更前台的 4 个东西：

1. `ask surface`
   不是再写一张 usage guide，而是让用户更自然地从问题进入系统。

2. `claim lookup surface`
   让用户可以直接问“这个结论从哪来”，而不是自己在 topic 和 source 之间跳。

3. `living page cues`
   明确告诉用户：哪些页是被持续刷新、持续回写、持续变厚的。

4. `query-to-writeback visibility`
   让用户看得见“这次问答如何改变了系统”，而不是只有维护者知道。

## 一句话判断

当前产物和 Karpathy 分享差得最多的，不是编译骨架。

差得最多的是：

`它还不像一个被提问驱动的活知识表面，而更像一个已经高度整理好的研究文档仓。`
