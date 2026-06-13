# Handoff: Phase 6 /autoplan Review Complete

**Date:** 2026-06-12
**Branch:** `idea-chatacademia-research-workbench`
**Status:** /autoplan review complete; awaiting user scope decision
**Plan:** [PLAN-page-rendering-improvements.md](PLAN-page-rendering-improvements.md)

## Context

User requested Phase 6: II-Commons detailed presentation + Research Record consolidation. The goal was to make research results more detailed like the II-Commons reference in `/Users/jiawei/Desktop/raw-2.md`, adding:

- Full source metadata (authors, journal, PMCID/PMID, categories)
- Research value judgments (one-sentence annotation per source)
- Retrieval scope declaration (what was searched, filters applied)
- Domain map / quick take (synthesis showing source relationships)
- Research Record save flow (consolidate useful research for future sessions)

## What Happened

Ran /autoplan with three review phases (CEO, Design, Eng). Codex was unavailable (auth failed), so all reviews were Claude subagent-only.

### Review Summary

| Phase | Findings | Critical | High | Recommendation |
|-------|----------|----------|------|----------------|
| CEO | 8 | 2 | 5 | Pause or scope down; system has zero completed research loops |
| Design | 18 | 4 | 7 | Critical hierarchy and state gaps; source card layout undefined |
| Eng | 18 | 4 | 6 | Schema incomplete; Research Record has no roundtrip test |

**Total: 44 findings, 10 critical**

### Cross-Phase Themes (High-Confidence Signals)

1. **Research Record has no adoption path** - CEO, Eng both flagged. Who decides when to save? How do saved records re-enter retrieval? What's the staleness policy?

2. **Research value judgment undefined** - Eng, Design both flagged. Is it LLM-generated? Template-based? Manual? What's the cost? What's the fallback?

3. **Domain map is aspirational** - Eng, Design both flagged. "Identify clusters, show convergence/divergence" requires clustering algorithm not specified.

### CEO Strategic Concerns

1. **Presentation polish on unused system** - Only one research case exists, stuck since 2026-06-06. Polishing presentation before proving the research loop works is premature.

2. **II-Commons is retrieval, not presentation** - The reference works because retrieval is good. Adding metadata fields without improving retrieval produces richer-looking empty cards.

3. **Claim Evidence Workbench was dismissed** - ChatAcademia analysis recommended narrow wedge first. Phase 6 generalizes presentation before proving the wedge.

4. **6-month regret scenario** - Beautiful source cards with zero users, Research Record feature with zero saved records, domain map disabled due to API cost.

## User Decision Required

Three paths forward:

**A) Scoped-down Phase 6** (recommended for momentum)
- Keep: Extended source cards (authors, journal, PMCID)
- Defer: Research Record, domain map, research value judgments
- Risk: Lower impact, but shippable

**B) Claim Evidence Workbench first** (CEO recommended)
- Pause Phase 6
- Ship the narrow wedge from ChatAcademia analysis
- Prove research loop works before generalizing
- Risk: Delays visible Ask the Vault improvements

**C) Full Phase 6 with blockers resolved**
- Address all 10 critical issues first
- Significant spec work before implementation
- Risk: Scope creep, long timeline

## Files Changed

- `PLAN-page-rendering-improvements.md` - Updated with Phase 6 spec and review findings
- Plan already has complete Phase 6 section (lines 463-601)
- Decision audit trail updated with decisions 24-25

## Verification

- /autoplan preamble passed
- Platform detected: GitHub, base branch: main
- Claude subagent reviews completed for CEO, Design, Eng
- Codex unavailable (auth failed) - all reviews subagent-only
- Plan file updated with Phase 6 /autoplan Review section

## What the Next Agent Needs

1. **Get user decision** on scope (A, B, or C above)
2. If A (scoped-down): Create implementation tasks for presentation-only changes
3. If B (Claim Evidence Workbench): Read `system/indexes/chatacademia-inspired-research-workbench-idea-20260601.md` for the original recommendation
4. If C (full Phase 6): Resolve the 10 critical issues before creating tasks

## Key Files for Reference

| File | Purpose |
|------|---------|
| `PLAN-page-rendering-improvements.md` | Full plan with Phase 6 spec and review findings |
| `/Users/jiawei/Desktop/raw-2.md` | II-Commons reference material (user provided) |
| `core/result_presentation.py` | Current presentation models and builders |
| `core/source_metadata.py` | Shared source metadata resolver |
| `system/indexes/chatacademia-inspired-research-workbench-idea-20260601.md` | ChatAcademia analysis recommending narrow wedge |

## API Cost Notes

No API costs incurred in this session. The /autoplan review was purely analytical using local files. Any implementation work requiring live Ask the Vault testing still needs:

1. OpenRouter dashboard daily limit set to $1/day
2. Environment: `OPENROUTER_DAILY_BUDGET_USD=1.00`
3. Feature flag: `USE_RESULT_PRESENTATION_V2=1`

## Open Questions

1. Should Research Record be a separate Phase 7, or dropped entirely?
2. Is research value judgment worth the LLM cost, or should we use templates?
3. Should we require 3-5 completed research cases before any presentation work?
4. Does the Claim Evidence Workbench still make sense as the narrow wedge?
