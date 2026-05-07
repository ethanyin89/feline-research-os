---
id: system-ibd-round1-writeback-state-sync-20260418
type: index
topic: ibd
disease: IBD
question_type: writeback
language: en
last_compiled_at: 2026-04-18
owner: codex
status: promoted
promoted_at: 2026-04-21
promoted_to: [topics/ibd/current-state-dashboard.md, topics/ibd/synthesis-index.md, system/indexes/unresolved-questions.md]
---

# IBD Round-1 Write-Back State Sync

## Promotion Status

Promoted on `2026-04-21`.

The durable state now lives in:

- [IBD current state dashboard](../../topics/ibd/current-state-dashboard.md)
- [IBD synthesis index](../../topics/ibd/synthesis-index.md)
- [unresolved questions](unresolved-questions.md)

This file is retained as the state-sync audit record.

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes`
- smallest durable home: `topic update + synthesis update + unresolved sync`

### Reason

- what is repeating:
  the IBD round-1 worksheets keep pushing the same message upward: the module's hardest problem is boundary-aware workup sequence, not treatment-first flattening.
- what becomes clearer:
  the IBD module now has a stable ordering for biopsy-site strategy, imaging support, tissue markers, support markers, frontier markers, fibrosis, and extension branches.
- what is still too thin, if anything:
  jurisdiction-specific regulatory interpretation, later treatment ranking, and the exact incremental value of noninvasive and frontier markers still remain thinner than the core diagnostic spine.

### Decision

- promote

## Batch Rules To Write Back

1. `all 24` IBD seed sources now have round-1 deep-extraction worksheets, so the remaining job is compiled compression and state sync.
2. The boundary problem should now be read as a sequencing problem:
   `clinical suspicion -> imaging pressure -> biopsy-site choice -> histology / integrated pathology -> bounded marker support`
3. Muscularis thickening is lymphoma-leaning but not decisive, and ileal sampling can change the diagnosis; the boundary is not only a pathology-reading problem.
4. Vitamin D and fecal S100A12 belong in shared support-marker territory; metabolomics is the strongest current frontier-separation signal, but still not routine-ready.
5. Diet-first management remains the cleanest practical treatment anchor, but it still lives inside a mixed chronic-enteropathy and food-response frame rather than pure idiopathic-IBD certainty.
6. Fibrosis and eosinophilic remodeling deepen chronicity and extension logic without being allowed to flatten into the core idiopathic IBD branch.

## Unresolved Questions To Carry Up

- How should muscularis thickening, biopsy-site selection, and tissue-marker signals combine in a practical IBD-versus-lymphoma workup sequence?
- Which noninvasive or frontier markers add enough incremental value beyond histology, clonality, and sampling strategy to justify later densification?
- How cleanly can diet-responsive chronic enteropathy be separated from idiopathic IBD in the current treatment anchor?
- How should fibrosis and extension-branch remodeling be integrated with long-term outcome framing without flattening the core disease spine?
