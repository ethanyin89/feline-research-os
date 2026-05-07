---
id: legacy-96-source-processing-ledger-20260421
type: system
topic: content-pipeline
question_type: status-ledger
language: bilingual
last_compiled_at: 2026-04-22
verification_status: compiled
decision_grade: provisional
owner: codex
status: active
---

# Legacy 96 Source Processing Ledger, 2026-04-21

This page fixes the working definition for the user-facing instruction:

`process the currently provided 96 links before asking for confirmation again`

## Classification

按 `$autoplan`，这件事当前属于：

`方案 + 内容处理`

不是单纯想法，也不是单纯排查。当前要做的是把已经给过的 source scope 压成稳定 truth layer，并把处理状态写回 owner pages。

## Scope

The legacy `96` means the first four 24-source disease modules:

| Disease | Source cards | Round-1 worksheets | Current source-card depth state | Read |
|---|---:|---:|---|---|
| CKD | 24/24 | 24/24 | 24 full / 0 partial | mature template; do not reopen bootstrap |
| FIP | 24/24 | 24/24 | 24 full / 0 partial | source-card layer is explicit full; remaining work is full-text/official-source/output-specific precision only |
| HCM | 24/24 | 24/24 | 24 full / 0 partial | source-card layer is explicit full; remaining work is full-text/output-specific precision only |
| IBD | 24/24 | 24/24 | 24 full / 0 partial | `src-ibd-009` is now deep-extracted workflow support with recovered methods/metrics; remaining work is full-text/image/regulatory/output-specific precision only |

Total legacy scope:

- source cards: `96/96`
- round-1 worksheets: `96/96`
- explicit full source cards: `96/96`
- explicit partial source cards: `0/96`

The newer full vault scope is `120` paper source cards after adding Diabetes. That is real repo state, but it is outside this legacy-96 instruction unless the user explicitly widens the scope.

## Processing Definition

For this instruction, `processed` means:

1. a source card exists in `raw/papers/`
2. a round-1 worksheet exists in `system/indexes/`
3. the disease dashboard/source index knows that the source is no longer an unprocessed link
4. remaining work is framed as selective densification, not raw link processing

`Full source-card depth` is a stricter bar. It requires enough source-backed detail in the source card body/frontmatter to support dense write-back without reading the worksheet first.

## Current Decision

The legacy 96 links are processed at the source-card + worksheet layer.

Do not keep treating FIP or IBD as unprocessed-link backlogs.

Their remaining work is now full-text / official-source / image-table / output-specific precision only, plus memo/topic/dashboard write-back and specific branch compression where repeated questions expose a real gap.

FIP, IBD, and HCM no longer have partial source cards after the 2026-04-22 promotion passes. Do not reopen generic FIP/IBD/HCM thickening unless a concrete full-text, official-source, image/table, or output-specific claim requires it.

## Next Content Moves Inside The Legacy 96

1. IBD: only refine full-text, image/table, regulatory/route-fit, or output-specific precision; avoid reopening generic source-card thickening.
2. FIP: only refine full-text, official-source/regulatory, image/table, or output-specific precision; avoid reopening generic source-card thickening.
3. HCM: only refine full-text/output-specific precision; avoid reopening generic source-card thickening.
4. CKD: only refine comparison or boundary memos; avoid reopening bootstrap extraction.

## Verification Links

- [source depth map](source-depth-map.md)
- [FIP source depth map](fip-source-depth-map.md)
- [IBD source depth map](ibd-source-depth-map.md)
- [HCM source depth map](hcm-source-depth-map.md)
- [FIP source index](fip-source-index.md)
- [IBD source index](ibd-source-index.md)
- [CKD source index](ckd-source-index.md)
