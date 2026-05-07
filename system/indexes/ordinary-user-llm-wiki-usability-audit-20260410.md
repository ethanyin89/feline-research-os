---
id: system-ordinary-user-llm-wiki-usability-audit-20260410
type: system
topic: operating-system
question_type: audit
language: zh
last_compiled_at: 2026-04-11
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Ordinary-User LLM Wiki Usability Audit, 2026-04-10

这页回答的是一个窄问题：

`对普通用户来说，这个 vault 现在是不是一个简单、便捷的 LLM wiki？`

## 类型判断

这件事属于：

`检查`

不是新方案，也不是故障排查。

## 最短结论

如果问：

`它现在像不像 LLM wiki？`

答案是：

`像。`

如果问：

`它对普通用户来说是不是已经足够简单、便捷？`

答案是：

`现在已经接近基本通过，但还没有到真正完成态。`

更准确地说：

`它已经是一个 ask-guided, auditable, write-back-native compiled wiki，而且普通用户前门已经明显收窄，但它还没有变成真正 ask-native 的 ordinary-user LLM wiki。`

## 这次检查用的标准

我只用普通用户视角看 4 件事：

1. 第一次进入时，是否只有一个明显入口
2. 进入后，是否能在很少跳转里拿到答案
3. 是否容易把读者入口和维护者入口混在一起
4. 是否真的更像“先问问题”，而不是“先学结构”

## 通过的地方

### 1. 它已经明显不是文件树优先

现在已经存在：

- [reader-start-here](reader-start-here.md)
- [ask-the-vault](ask-the-vault.md)
- [question-router](question-router.md)
- 各病种的 dashboard 和 top-question 入口

这说明系统已经不再要求普通用户先理解 vault 结构。

### 2. 它已经有真实的 query surface

`Ask the vault` 和 `question router` 已经把入口改成：

- 机制
- 识别 / workup
- endpoint / marker
- treatment / translation
- regulatory
- claim verification

这已经是 LLM wiki 的方向，而不是传统 wiki 的目录页。

### 3. 它已经有 claim verification 和 trust boundary

普通用户现在不只是能“看总结”，还可以继续走到：

- [compiled-vs-source-reading](compiled-vs-source-reading.md)
- [verify-a-claim](verify-a-claim.md)

这一点是很多假 “AI wiki” 没有的。

## 没通过的地方

### 1. 前门太多，不够单纯

`这条现在已经明显改善。`

当前普通用户可能同时看到：

- `Reader start here`
- `Ask the vault`
- `Question router`
- `ordinary-user usage guide`
- `ordinary-user usage guide bilingual`
- disease dashboard
- disease navigation

这一轮之后，`Reader start here` 已经被明确压成唯一主入口，而 `ask-the-vault` 和 `question-router` 也已经被压成二级入口。

所以这里现在不再是主问题。

更准确的说法变成：

`前门已经开始收窄，但二级入口之间仍然有一点重复。`

### 2. README 对普通用户仍然太重

[README](../../README.md) 这轮已经明显比之前更收束了。

它现在已经明确分开：

- ordinary reader
- question-shaped reader
- claim verification
- maintainer

所以这里也不再是最主要的问题。

但它仍然不是一个纯 reader README，因为 maintainer 入口仍然和 reader 入口共存在同一页里。

### 3. Disease navigation 仍然混入了太多维护者材料

例如各 disease `navigation` 页里，普通用户入口和下面这些层会混在一起：

- source index
- reading plan
- output matrix
- bootstrap workflow
- promotion examples
- health check
- system schemas / prompts

这条现在也已经部分改善。

最近几轮里，disease navigation 已经开始显式分层成：

- reader-facing section
- operator and build path

而且 CKD / FIP 的一部分 memo 列表已经被下沉。

所以这里的当前真实状态是：

`仍有维护者噪音，但已经不是首屏主导问题。`

现在它们更像：

`reader-first hybrid page`

而不是：

`reader-only page`

### 4. 它还是 query-guided navigation，不是真正的 ask-native surface

`这条仍然成立，而且现在是最主要剩余缺口。`

当前的 “ask” 实际上仍然是：

`先把问题映射成页面，再去点页面。`

这已经比文件树好很多，但它还不是更自然的：

`我问一句话，系统直接把最合适的结构和答案面拿出来。`

所以它已经有了 LLM wiki 的骨架，但前台产品感还没有完全跟上。

## 这次检查里最明确的 3 个问题

### 问题 1

`不是没有入口，而是二级入口之间还有一点重复。`

### 问题 2

`不是没有 query surface，而是 query surface 还没有赢过导航 surface。`

### 问题 3

`不是没有普通用户页，而是普通用户页和维护者页还没有完全分层。`

## 当前判断

如果硬要打一个非常粗的判断：

- 作为 `auditable compiled research wiki`：`通过`
- 作为 `ordinary-user simple and convenient LLM wiki`：`基本通过，但还不能算完成`

也就是：

`底层方法已经对，前门已经明显变窄，但 ask-native 产品感还不够。`

## 最值得做的，不是再加入口

下一步最该做的不是继续加新 front door。

而是做减法：

1. 继续压短 `reader-start-here`，避免二级入口与 disease entry 重复
2. 把 `ask-the-vault` 再往真正的问题面收，而不是页面路由面
3. 继续把 disease navigation 的 operator material 往下沉
4. 只在普通读者真的需要时，才让他们碰到 source / system / operator 页面

## 一句话收口

这个系统现在已经有了 LLM wiki 的真骨架，而且普通用户前门已经比上一轮明显更窄；但它还停在“导航更聪明”，还没进入“真正像在问一个活 wiki”的完成态。
