# Handoff: Result Presentation Contract - Phase 4 Complete

**Date:** 2026-06-12
**Branch:** `idea-chatacademia-research-workbench`
**Status:** Phase 4 complete, Phase 5 ready to start
**Plan file:** `PLAN-page-rendering-improvements.md`

---

## Summary

Implemented the `ResultPresentation` contract for consistent research result presentation. The work removes global confidence badges (high/medium/low) and replaces them with factual evidence profiles. Internal IDs and raw status values are now translated to user-facing Chinese labels.

---

## What Was Completed

### Phase 1: Manual Samples (Complete)
- Updated `system/indexes/presentation-logic-test-page.html` with 4 visual samples
- Updated `system/indexes/content-presentation-logic-samples-20260611.md`
- Removed confidence badges, added evidence profiles
- Translated all internal labels to user-facing vocabulary

### Phase 2: Skill Codification (Complete)
- Created `.claude/skills/render-result-page.md`
- Documents: surface types, contracts, vocabulary, state matrix, anti-patterns
- Contains 6 approved examples and validation checklist

### Phase 3: Presentation Helpers (Complete)
- Created `core/result_presentation.py` (~450 lines)
- Data models:
  - `ResultPresentation` - top-level presentation object
  - `SourceDisplay` - user-facing source card
  - `EvidenceProfile` - factual evidence summary
  - `InlineCitation`, `AnswerSection`, `NextAction`
- Label maps:
  - `EVIDENCE_DEPTH_LABELS` - `deep_extracted` → `已核查全文`
  - `PROVENANCE_LABELS` - `quoted_fact` → `直接来源`
  - `SOURCE_TYPE_LABELS` - `pubmed` → `PubMed`
- Builder functions:
  - `build_evidence_profile(sources, claims, authority_state)`
  - `build_source_displays(sources)`
  - `build_result_presentation(...)` - main entry point
  - `build_next_actions(topic, surface_type)`
- Helpers: `detect_presentation_state()`, `get_state_warning()`

### Phase 4: Ask the Vault Integration (Complete)
- Added feature flag: `USE_RESULT_PRESENTATION_V2` (env var)
- New functions in `scripts/app.py`:
  - `load_full_source_metadata()` - extracts DOI, PMID, verification_status
  - `render_evidence_profile_v2()` - factual profile display
  - `render_source_card_v2()` - single card with canonical link
  - `render_sources_section_v2()` - expandable sources list
  - `render_next_actions_v2()` - task-specific suggestions
  - `build_presentation_from_answer()` - bridges old format to new contract
  - `render_answer_block_v2()` - complete v2 renderer
- Updated both call sites (chat history + live query) to check feature flag
- Old renderer preserved at `render_answer_block()` for rollback

---

## Key Files

| File | Purpose |
|------|---------|
| `PLAN-page-rendering-improvements.md` | Master plan with decision audit trail |
| `core/result_presentation.py` | Pure presentation helpers (no UI) |
| `scripts/app.py` | Streamlit app with v2 renderers |
| `.claude/skills/render-result-page.md` | Design/content contract for any agent |
| `system/indexes/presentation-logic-test-page.html` | Visual prototype |
| `system/indexes/content-presentation-logic-samples-20260611.md` | Markdown samples |

---

## How to Test Phase 4

```bash
# Enable v2 rendering
USE_RESULT_PRESENTATION_V2=1 streamlit run scripts/app.py

# Or with full budget guard
USE_RESULT_PRESENTATION_V2=1 \
OPENROUTER_DAILY_BUDGET_USD=1.00 \
OPENROUTER_MODEL=openai/gpt-4.1-mini \
streamlit run scripts/app.py
```

**What to verify:**
1. Evidence profile shows "基于 N 篇来源 | X 篇已核查全文 | Y 篇基于摘要"
2. No confidence badges (高/中等/低) appear
3. Source cards show paper titles with DOI/PubMed links
4. Provenance breakdown uses Chinese labels (直接来源, 来源支持, 分析推断)
5. "下一步" section shows task-specific actions, not generic "还有其他问题吗"

---

## What Remains (Phase 5)

### Phase 5: Apply adapters to two static surfaces

1. **Migrate one What-Is page**
   - Candidate: `topics/ckd/what-is-ckd.md` (most complete)
   - Add frontmatter fields for ResultPresentation
   - Create rendering adapter for static pages

2. **Migrate one ranked treatment page**
   - Check if ranked treatment pages exist in `topics/*/`
   - May need to create sample if none exists

3. **Compare against approved samples**
   - Visual comparison with `presentation-logic-test-page.html`
   - Verify no internal IDs leak through
   - Check responsive behavior (320px, 768px, 1440px)

4. **Expand to other pages after acceptance**

### Acceptance Criteria for Phase 5
- [ ] Zero `src-*` identifiers in default view
- [ ] Zero raw verification statuses (`abstract_weighted`, `deep_extracted`)
- [ ] Zero raw provenance types (`quoted_fact`, `llm_inference`)
- [ ] All source cards have paper titles
- [ ] All linked sources have canonical URLs or "链接不可用"
- [ ] Title-only sources marked as discovery-only

---

## CEO Review Decision (Context)

Both reviewers (Claude + Codex) agreed:
- Remove global `high/medium/low` confidence badges in V1
- Use factual evidence profiles instead
- Center on claim-to-evidence boundaries, not answer-level trust signals

The `compute_confidence()` function measures only provenance tag proportions, which is insufficient for a defensible trust signal. V1 shows factual counts; V2+ may add claim-level confidence after schema work.

---

## Architecture Notes

```
User Query
    ↓
run_query_core() → answer + source_ids + confidence
    ↓
build_presentation_from_answer()
    ↓
ResultPresentation {
    evidence_profile: EvidenceProfile
    source_cards: [SourceDisplay]
    next_actions: [NextAction]
}
    ↓
render_answer_block_v2()
    ├── render_provenance() (unchanged)
    ├── render_evidence_profile_v2()
    ├── render_research_trace() (unchanged)
    ├── render_expert_review_loop() (unchanged)
    ├── render_sources_section_v2()
    └── render_next_actions_v2()
```

---

## Potential Issues

1. **DOI extraction** - Some sources have DOI in `links.doi`, others may not. `load_full_source_metadata()` handles both frontmatter and nested links block.

2. **Feature flag scope** - Currently only affects Ask the Vault. Static pages (What-Is, ranked) need separate adapters.

3. **Responsive testing** - v2 HTML uses inline styles; may need CSS class extraction for maintainability.

---

## Quick Commands

```bash
# Verify module imports
python3 -c "from core.result_presentation import *; print('OK')"

# Check app compiles
python3 -m py_compile scripts/app.py

# Run with v2 enabled
USE_RESULT_PRESENTATION_V2=1 streamlit run scripts/app.py
```

---

## Next Session Recommendation

1. Start with Phase 5 task 1: migrate `topics/ckd/what-is-ckd.md`
2. Create a static page adapter that reads frontmatter and renders using ResultPresentation
3. Test responsive behavior at 320px, 768px, 1440px
4. After acceptance, remove feature flag and old renderer
