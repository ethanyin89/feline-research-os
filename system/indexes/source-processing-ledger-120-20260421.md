---
id: source-processing-ledger-120-20260421
type: system
topic: content-pipeline
question_type: status-ledger
language: bilingual
last_compiled_at: 2026-04-23
verification_status: compiled
decision_grade: provisional
owner: codex
status: active
---

# 120 Source Processing Ledger, 2026-04-21

This page fixes the current user-facing scope:

`5 disease modules x 24 provided content links = 120 paper sources`

## Classification

按 `$autoplan`，这件事属于：

`方案 + 内容处理`

The architecture is already in place. The current job is execution: keep compressing the 120 source set into stable Karpathy-style LLM wiki layers without re-confirming repeated steps.

## Scope

| Disease | Source cards | Round-1 worksheets | Topic surface | Output surface | Current source-card depth state | Read |
|---|---:|---:|---|---|---|---|
| CKD | 24/24 | 24/24 | usable and mature | briefing / dossier / slides exist | 24 full / 0 partial | mature template; avoid reopening bootstrap |
| FIP | 24/24 | 24/24 | usable and improving | briefing / dossier / slides exist | 24 full / 0 partial | all source cards now explicit full depth; next FIP work is full-text/official-source/image precision and branch-control refinement |
| HCM | 24/24 | 24/24 | usable and improving | briefing / dossier / slides exist | 24 full / 0 partial | all source cards now explicit full depth; next HCM work is full-text/output-specific precision only |
| IBD | 24/24 | 24/24 | usable and bilingual-rich | briefing / dossier / slides exist | 24 full / 0 partial | `src-ibd-009` is now deep-extracted workflow support with recovered methods/metrics; next work is full-text/image/regulatory precision and output-specific workup compression only |
| Diabetes | 24/24 | 24/24 | usable starter Level 5 | first briefing / dossier / slides started on 2026-04-21 | 24 full / 0 partial | fifth module now has source, worksheet, topic, memo, regulatory, output starter layers, and all source cards at explicit full depth |

Total current scope:

- paper source cards: `120/120`
- round-1 worksheets: `120/120`
- explicit full source cards: `120/120`
- explicit partial source cards: `0/120`

Regulatory cards are additional control sources and are not counted inside the 120 paper-source scope.

## Processing Definition

For the current instruction, `processed` means:

1. a paper source card exists in `raw/papers/`
2. a round-1 worksheet exists in `system/indexes/`
3. the disease has topic-level landing pages that can answer mechanism / recognition / endpoint / translation / regulatory / synthesis questions
4. narrow owners exist where repeated branch-order or boundary questions already appeared
5. outward output surfaces exist, or the module has a documented reason to remain topic-only

`Full source-card depth` is a stricter quality bar. It requires reusable quoted facts and conclusions in the source card itself. It is not required for the link to count as processed, but it is the next densification layer.

## Current Decision

The 120 provided paper sources are processed at the source-card + round-1 worksheet layer.

The remaining content job is no longer raw link processing. It is:

- full-text / official-source / image-table precision for modules already at 24/24 full
- narrow-owner memo densification
- dashboard / synthesis / state write-back
- output-surface parity where a disease module has enough topic structure

Diabetes was the main parity gap because it had source cards, worksheets, topics, memos, and U.S. SGLT2 regulatory controls, but no outward output set. That parity gap is now closed at the starter output layer. FIP has reached 24/24 explicit full source-card depth after the 2026-04-22 thickening pass. IBD is now 24/24 full after the 2026-04-23 `src-ibd-009` source-check pass. Remaining work is full-text clinical/regulatory/image precision only where a stronger external output requires it.

## Default Continue Order

1. IBD: restrict the next pass to full-text, image/table, regulatory/route-fit, or output-specific workup compression; 24/24 source cards are already explicit full.
2. FIP: restrict the next pass to full-text, official-source/regulatory, image/table, or output-specific precision; 24/24 source cards are already explicit full.
3. HCM: restrict the next pass to full-text/output-specific precision; 24/24 source cards are already explicit full.
4. Diabetes: restrict the next pass to full-text clinical/regulatory deepening or output-specific corrections; 24/24 source cards are already explicit full.
5. CKD: restrict work to comparison, boundary, and maintenance updates.

## Verification Links

- [source depth map](source-depth-map.md)
- [FIP source depth map](fip-source-depth-map.md)
- [IBD source depth map](ibd-source-depth-map.md)
- [HCM source depth map](hcm-source-depth-map.md)
- [Diabetes source depth map](diabetes-source-depth-map.md)
- [content-side densification queue](content-side-densification-queue.md)
- [Karpathy alignment handoff](karpathy-alignment-handoff-20260418.md)
- [Diabetes current state dashboard](../../topics/diabetes/current-state-dashboard.md)
- [Diabetes source index](diabetes-source-index.md)
