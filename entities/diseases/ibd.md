---
id: disease-ibd
type: disease
name: Feline Inflammatory Bowel Disease
species: feline
aliases: [IBD, feline IBD, idiopathic inflammatory bowel disease]
priority: high
related_models: []
related_endpoints: [fceai, intestinal-fibrosis]
related_regulations: []
status: active
---

# Feline IBD

## Why It Matters

Feline IBD matters because it is the first disease module in this vault where exclusion-first workup, lymphoma-boundary handling, marker hierarchy, and diet-first treatment all have to be modeled at the same time.

## Current Notes

- Feline IBD currently sits inside a wider `chronic enteropathy` frame rather than as a perfectly isolated disease object.
- The strongest current compiled framing is `diagnosis of exclusion plus multimodal boundary work`.
- The most important nearby branch is low-grade or small-cell alimentary lymphoma, not a generic inflammation-only differential set.
- Current treatment logic is real, but it remains subordinate to workup and pathology architecture.

## Linked Topic Pages

- [topic index](../../topics/ibd/index.md)
- [current state dashboard](../../topics/ibd/current-state-dashboard.md)
- [synthesis index](../../topics/ibd/synthesis-index.md)

## Open Questions

- how much of the current chronic-enteropathy frame will ultimately stay inside the IBD module
- how sharply idiopathic IBD can be separated from food-responsive disease and small-cell lymphoma in later compiled outputs
