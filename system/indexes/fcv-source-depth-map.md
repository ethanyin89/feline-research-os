---
id: system-fcv-source-depth-map
type: index
topic: fcv
question_type: source-depth-map
language: en
last_compiled_at: 2026-04-30
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# FCV Source Depth Map

## Current Read

- FCV has `24/24` seed paper source cards.
- FCV now has `24/24` deep-extracted paper anchors.
- The module is no longer bottlenecked by partial source-card status; the remaining work is topic-page synthesis, image coverage, and downstream product/UI polish.

## Card-Depth Reality

| extraction_depth | Count | Read |
|---|---:|---|
| full | 24 | all FCV seed paper cards now have full extraction depth, including classic broad review, modern epidemiology/vaccine-locality, replication-deficient vaccine, JAM-A receptor distribution, context-only editorial, foundational phylogeny, and hypervariable-region vaccine-failure cards |
| partial | 0 | no FCV seed paper cards remain partial |

| verification_status | Count | Read |
|---|---:|---|
| deep_extracted | 24 | all FCV seed paper cards now support downstream boundary writing |
| source_checked | 0 | no FCV seed paper cards remain only source-checked |

## Tiering Read

### Tier 1

- review / guideline anchors: `src-fcv-001`, `src-fcv-002`, `src-fcv-004`, `src-fcv-007`, `src-fcv-009`, `src-fcv-015`

### Tier 2

- vaccine breadth / persistence / epidemiology anchors: `src-fcv-003`, `src-fcv-005`, `src-fcv-006`, `src-fcv-011`, `src-fcv-017`, `src-fcv-022`

### Tier 3

- therapy, extension, and molecular pressure-test papers: `src-fcv-008`, `src-fcv-010`, `src-fcv-012`, `src-fcv-013`, `src-fcv-014`, `src-fcv-016`, `src-fcv-018`, `src-fcv-019`, `src-fcv-020`, `src-fcv-021`, `src-fcv-023`, `src-fcv-024`

## Next Moves

- ✅ Core topic pages (mechanism-overview, risk-and-recognition, endpoint-handbook) recompiled to handbook status (2026-04-30)
- Continue tightening synthesis-index, translation-brief, and regulatory-brief against recompiled handbooks
- Keep FCV output claims below final vaccine ranking or treatment guidance until field-effectiveness, label/regulatory, and therapy branches are denser
- FCV image assets remain at 0/24 — next visual gains require PDF figure extraction
