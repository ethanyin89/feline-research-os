---
id: system-language-filename-alignment-standard
type: system
topic: ckd
last_compiled_at: 2026-04-08
owner: codex
status: active
language: zh
---

# Language Filename Alignment Standard

这页解决的是一个很具体的问题：

`文件名、frontmatter、页面实际语言，不能互相打架。`

## 一句话版本

语言归语言，文件名归文件名。

但只要两者不一致，就必须显式标出来，不能靠读者自己猜。

## 基本规则

### 1. 原始素材保持原始语言

- 英文就英文
- 中文就中文
- 不因为 vault 想看起来整齐，就提前改语言

### 2. 非原始层默认要有 `language`

对 `topic / output / memo / bilingual page`：

- frontmatter 应显式写 `language`
- 不应让读者靠文件名猜

### 3. 文件名后缀只在真的稳定时才表达语言

- `-en` 只表示该文件稳定是英文页
- `-bilingual` 只表示该文件稳定是双语页
- 没有语言后缀，不等于默认中文

### 4. 如果文件名和实际语言暂时不一致，必须做两件事

1. frontmatter 写真实 `language`
2. 页面正文或入口页明确提示，不要把文件名当语言保证

## 当前项目的推荐模式

### 原始层

- 不改语言

### 编译层

- 单页用一个主工作语言
- 高复用页再派生 `bilingual` 版本

### 输出层

- 如果有中文页，就显式 `language: zh`
- 如果有英文页，就显式 `language: en`
- 如果只是“默认文件”但正文仍是英文，也必须标 `language: en`

## 当前禁止项

1. 把无后缀文件默认当中文页
2. 在导航里把实际英文文件写成 `zh`
3. 用文件名替代 frontmatter 的语言声明
4. 因为页面叫 `-en`，就假设配对文件一定是中文

## 当前执行规则

1. 入口页标签必须服从页面真实语言
2. frontmatter 的 `language` 优先级高于文件名印象
3. 若语言仍在迁移中，入口说明必须写清楚
4. bilingual 页必须真的含中英文，不得只因为“以后想双语”就先挂标签

## 当前最重要的提醒

`文件名可以历史遗留，但语言标记不能含糊。`
