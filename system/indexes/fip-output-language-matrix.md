---
id: fip-output-language-matrix
type: index
topic: fip
question_type: output-governance
language: bilingual
last_compiled_at: 2026-04-10
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: active
---

# FIP Output Language Matrix

Use this page when you need the fastest answer to:

- which FIP output files are working-English
- which files are derived English outputs
- which files are Chinese-facing outputs
- which output layers still do not exist

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
| Chinese-facing output | `*-zh.md` | Chinese | Chinese-facing briefings, dossiers, and slides | limited, still `decision_grade: no` |
| Bilingual compiled page | `*-bilingual.md` or explicit bilingual topic pages | bilingual | cross-language navigation and cross-checking | started, still narrow |

## Current FIP Output Files

### Working-English Outputs

- [briefing working en](../../outputs/briefings/out-fip-briefing-20260410-round1-working-en.md)
- [dossier working en](../../outputs/dossiers/out-fip-dossier-20260410-v1-working-en.md)
- [slides working en](../../outputs/slides/out-fip-slides-20260410-v1-working-en.md)

### Derived English Outputs

- [briefing en](../../outputs/briefings/out-fip-briefing-20260410-round1-en.md)
- [dossier en](../../outputs/dossiers/out-fip-dossier-20260410-v1-en.md)
- [slides en](../../outputs/slides/out-fip-slides-20260410-v1-en.md)

### Chinese-Facing Outputs

- [briefing zh](../../outputs/briefings/out-fip-briefing-20260410-round1-zh.md)
- [dossier zh](../../outputs/dossiers/out-fip-dossier-20260410-v1-zh.md)
- [slides zh](../../outputs/slides/out-fip-slides-20260410-v1-zh.md)

### Bilingual Compiled Pages

- [current state dashboard bilingual](../../topics/fip/current-state-dashboard-bilingual.md)
- [synthesis index bilingual](../../topics/fip/synthesis-index-bilingual.md)
- [mechanism overview bilingual](../../topics/fip/mechanism-overview-bilingual.md)
- [risk and recognition bilingual](../../topics/fip/risk-and-recognition-bilingual.md)
- [translation brief bilingual](../../topics/fip/translation-brief-bilingual.md)
- [endpoint handbook bilingual](../../topics/fip/endpoint-handbook-bilingual.md)
- [regulatory brief bilingual](../../topics/fip/regulatory-brief-bilingual.md)

## What Does Not Exist Yet

- no broad bilingual FIP page family yet beyond the current compiled core stack
- no FIP output layer has passed a separate language-QA round beyond initial creation

## Current State

- the first clean `working-en` FIP layer now exists
- the first clean derived `-en` layer now exists
- the first clean `-zh` output layer now exists
- FIP now has briefing, dossier, and slides output families
- the first bilingual compiled FIP topic layer now exists
- the first bilingual recognition, translation, and endpoint pages now also exist
- the first bilingual mechanism and regulatory pages now also exist
- bilingual coverage is still intentionally narrow

## Trust Boundary

- all current FIP output files remain compiled outputs, not raw-source substitutes
- no file in this matrix should be treated as submission-grade or decision-grade
- the treatment branch may be practically strong, but the output layer is still bounded by diagnosis ambiguity and regulatory thinness

## One-Sentence State

FIP now has a real working-English layer, a derived English layer, a Chinese-facing output layer, and a first bilingual compiled core stack, but broader bilingual coverage is still intentionally narrow.
