---
id: ckd-output-language-matrix
type: index
topic: ckd
question_type: output-governance
language: bilingual
last_compiled_at: 2026-04-09
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: active
---

# CKD Output Language Matrix

Use this page when you need the fastest answer to:

- which CKD output files are working-English
- which files are derived English outputs
- which files are Chinese-facing outputs
- which pages are bilingual compiled pages

## Current Rule

**EN**
- raw material stays in its original language
- working files can stay English if the source workflow is still English-dominant
- non-raw pages must state language in frontmatter
- filename, frontmatter, and actual page language must align

**ZH**
- raw 素材保持原始语言
- 如果当前工作流仍以英文为主，工作文件可以继续是英文
- 非 raw 页面必须在 frontmatter 中明确语言
- 文件名、frontmatter、页面实际语言必须对齐

## Output Matrix

| Layer | Current File Pattern | Current Language | What It Is For | Can It Be Reused Externally |
|---|---|---|---|---|
| Working output | `*-working-en.md` | English | internal drafting and working synthesis | no |
| Derived English output | `*-en.md` | English | cleaner English-facing derivative output | limited, still `decision_grade: no` |
| Bilingual compiled page | `*-bilingual.md` or explicit bilingual topic pages | Bilingual | cross-language navigation and cross-checking | limited |
| Chinese-facing output | `*-zh.md` | Chinese | Chinese-facing briefings, dossiers, and slides | limited, still `decision_grade: no` |

## Current CKD Output Files

### Working-English Outputs

- [briefing working en](../../outputs/briefings/out-ckd-briefing-20260408-round1-working-en.md)
- [dossier working en](../../outputs/dossiers/out-ckd-dossier-20260408-v1-working-en.md)
- [slides working en](../../outputs/slides/out-ckd-slides-20260408-v1-working-en.md)

### Derived English Outputs

- [briefing en](../../outputs/briefings/out-ckd-briefing-20260408-round1-en.md)
- [dossier en](../../outputs/dossiers/out-ckd-dossier-20260408-v1-en.md)
- [slides en](../../outputs/slides/out-ckd-slides-20260408-v1-en.md)

### Bilingual Compiled Pages

- [current state dashboard bilingual](../../topics/ckd/current-state-dashboard-bilingual.md)
- [synthesis index bilingual](../../topics/ckd/synthesis-index-bilingual.md)
- [core paper synthesis memo bilingual](core-paper-synthesis-memo-ckd-round1-bilingual.md)

### Chinese-Facing Outputs

- [briefing zh](../../outputs/briefings/out-ckd-briefing-20260408-round1-zh.md)
- [dossier zh](../../outputs/dossiers/out-ckd-dossier-20260408-v1-zh.md)
- [slides zh](../../outputs/slides/out-ckd-slides-20260408-v1-zh.md)

**EN**
- the first clean `*-zh.md` output layer now exists
- the absence of a suffix still must not be read as Chinese
- working-English files and Chinese-facing files are now separate layers

**ZH**
- 第一批干净的 `*-zh.md` 输出层现在已经存在
- 没有语言后缀，仍然不等于中文
- working-English 文件和中文输出文件现在已经分层

## Reuse Guidance

### Safe Reading Order

1. read the working-English file if you want the closest working layer
2. read the `-en` derivative if you want a cleaner English-facing output
3. read bilingual compiled pages if you need cross-language orientation
4. use the `-zh` file only when you explicitly need a Chinese-facing output

### Trust Boundary

**EN**
- all current output files remain compiled outputs, not raw-source substitutes
- no file in this matrix should be treated as submission-grade or decision-grade
- bilingual pages are navigation and synthesis aids, not stronger evidence layers
- Chinese-facing outputs are language-facing derivatives, not stronger evidence layers

**ZH**
- 当前这张矩阵里的所有输出文件都仍然是编译结果，不是原始来源替代物
- 这里没有任何文件可以被当成 submission-grade 或 decision-grade
- 双语页面是导航和综合辅助层，不是更强证据层
- 中文输出是面向语言的派生层，不是更强证据层

## One-Sentence State

**EN**
The CKD vault now has a clean working-English layer, a derived English layer, a Chinese-facing output layer, and a bilingual compiled layer.

**ZH**
这个 CKD vault 现在已经有了清楚的 working-English 层、派生英文层、中文输出层和双语编译层。
