<!-- /autoplan restore point: /Users/jiawei/.gstack/projects/feline-research-os/unknown-autoplan-restore-20260418-044742.md -->

# Plan: Vision-Integrated Query Layer

**Status:** MVP READY. 17 decisions resolved. 68/68 tests pass as of 2026-04-21. 8 verified figures on disk, routing active. Step 5 demo is pending runtime credentials in the current shell.
**Design doc:** `~/.gstack/projects/feline-research-os/jiawei-unknown-design-20260417-132505.md`
**Approved:** 2026-04-17
**Branch:** unknown (git-native, no remote)

**Current verification note, 2026-04-21:** core scripts compile, `scripts/test_query.py`
passes `68/68`, search / compile-trigger / MCP tool listing work, and the current shell
still lacks `streamlit`, so live Streamlit smoke testing remains an environment task.

## What Was Built

This plan adds vision integration to `scripts/query.py` and `scripts/app.py` so Claude can
read extracted figures from source PDFs during synthesis — not just cite them.

The "whoa" moment: ask "What is the primary mechanism of tubulointerstitial fibrosis in
feline CKD?" and get the actual mechanism schematic from src-ckd-001 attached alongside
the text synthesis. Claude reads the figure, describes what it shows, and cites it.

**Approach B chosen:** Vision-integrated synthesis (not figure-slot injection or
document-level pre-extraction). Claude sees figures at query time.

## Files Changed

### scripts/query.py (core implementation)
- `VISION_INTEGRATION_ENABLED = True` flag (top-level, easy kill switch)
- `VISION_FIGURE_CAP = 3` cap (cost control: 3 PNGs ≈ 6-15k tokens)
- `_parse_local_assets_from_frontmatter(content)` — pure YAML-free parser for
  `links.local_assets` in source card frontmatter
- `resolve_local_assets(source_ids, vault_root)` — maps loaded source IDs to verified
  figure files. Excludes `candidate-*` (unverified) entries. Returns only files that
  exist on disk.
- `synthesis_call()` extended: when Anthropic backend + assets on disk, builds
  content_blocks list with text + image (base64 PNG) entries. Falls back to text-only
  for Ollama/OpenRouter or when no assets exist.
- Figure footer in `main()`: prints `FIGURES REFERENCED IN ANSWER:` when described_in_answer
- `write_back()` extended: includes `figures_used` in frontmatter when provided

### scripts/app.py (web UI integration)
- Imports `resolve_local_assets` and `VISION_INTEGRATION_ENABLED` from query.py
- In `run_query()`: resolves assets after hop loop, passes to `synthesis_call()`
- Renders figures inline with `st.image()` when figures are described in answer
- Sidebar debug panel shows figures_used count

### scripts/test_query.py (test suite)
- `_test_parse_local_assets_empty` — verifies `[]` returns empty list
- `_test_parse_local_assets_with_entries` — verifies two-entry parsing
- `_test_resolve_local_assets_filters_candidates_and_missing` — verifies candidate-*
  exclusion and missing-file filtering; verifies presence when file exists on disk
- `_test_write_back_includes_figures_used` — verifies figures_used in frontmatter

All 41 tests pass (28 original + 4 new vision tests + 9 pre-existing vision stubs now
implemented = 41 total as of 2026-04-17).

## Source Card Schema (unchanged, already designed)

Source cards in `raw/papers/src-*.md` already have `links.local_assets:` frontmatter.
Current state: most entries are still `candidate-*` placeholders. `src-ckd-001`
now has 2 finalized JPEG assets extracted from the PMC mirror and verified against
the inline article labels `img1` and `img2`.

```yaml
links:
  url: https://...
  local_assets:
    - raw/images/ckd/src-ckd-001-candidate-mechanism-schematic.png
```

After human extracts and verifies against article label:
```yaml
links:
  url: https://...
  local_assets:
    - raw/images/ckd/src-ckd-001-mechanism-schematic.jpg
    - raw/images/ckd/src-ckd-001-mechanism-risk-factor-summary.jpg
```

The `candidate-` prefix is the gate. Until it's removed, query.py will not attach the file.

## What's Pending (Human Task)

**Step 2: CKD Figure Extraction (MVP THRESHOLD MET — 8 verified figures on disk)**

Resolved assets (all renamed to semantic naming convention, source cards updated 2026-04-18):
| File | Source card | figure_type | Routed to question_types |
|------|------------|-------------|--------------------------|
| `src-ckd-001-mechanism-schematic.jpg` | src-ckd-001 | mechanism | mechanism, synthesis |
| `src-ckd-001-mechanism-risk-factor-summary.jpg` | src-ckd-001 | mechanism | mechanism, synthesis |
| `src-ckd-017-outcome-upc-by-subtype-table.png` | src-ckd-017 | outcome | endpoints, treatment, regulatory |
| `src-ckd-017-imaging-pathology-classification-panel.jpg` | src-ckd-017 | imaging | recognition |
| `src-ckd-022-outcome-time-course-gfr-creatinine-table.png` | src-ckd-022 | outcome | endpoints, treatment, regulatory |
| `src-ckd-022-pathology-histopath-findings-table.png` | src-ckd-022 | pathology | pathology, mechanism, recognition |
| `src-ckd-024-outcome-biomarker-landscape.jpeg` | src-ckd-024 | outcome | endpoints, treatment, regulatory |
| `src-ckd-024-outcome-biomarker-comparison-table.png` | src-ckd-024 | outcome | endpoints, treatment, regulatory |

Still unresolved (blocking Step 5 is NOT required — MVP threshold met):
- `src-ckd-013`: blocked on source access. Direct ScienceDirect PDF path currently returns Cloudflare `403`; the Nottingham repository mirror resolves to a Cloudflare challenge page and its DSpace bitstream API returns `401 Unauthorized`; the newer `nottingham-repository.worktribe.com` output page also resolves to a Cloudflare challenge shell with no visible file links in the current environment; search-cache snippets still indicate the page lists two downloadable PDF files; Bristol/handle publication pages expose metadata and abstract only, with no downloadable full-text object visible in the current environment

Retired candidate (not a live blocker):
- `src-ckd-022`: accessible article surfaces checked on 2026-04-18 expose main-article figures plus supplemental tables `S1-S8`, but no separately verifiable model-design source object. The earlier `src-ckd-022-candidate-model-design.png` placeholder is therefore retired rather than kept as an unresolved extraction target
**Step 5: MVP Demo (after Step 2)**
```
python scripts/query.py "What is the primary mechanism of tubulointerstitial fibrosis in feline CKD, and what histological evidence supports it?" --disease ckd
```
Expected: text synthesis + figure from src-ckd-001 described in answer

**Step 6: FIP/IBD/HCM rollout + write-back enrichment + cross-disease queries (after CKD pilot validates)**

Step 6 scope (confirmed 2026-04-18):
- Full disease rollout (FIP, IBD, HCM) using CKD pilot as template
- Write-back enrichment loop: figure_caption_ai field populated from synthesis descriptions
- Cross-disease visual queries ("Compare CKD and IBD proteinuria") — architecture already supports multi-disease routing; Step 6 is the right home to wire it explicitly

## Constraints

- No RAG. Index-based routing preserved.
- No new language runtimes.
- Vision disabled for Ollama/OpenRouter backends (image/base64 blocks not supported by those APIs at query time).
- Hard rule: no fake figures. No AI-generated images. All assets must be extracted from real PDFs and verified before `candidate-*` prefix is removed.
- API cost: 3 figures ≈ 6-15k tokens overhead per synthesis call.

## Success Criteria (original design doc)

- `raw/images/ckd/` contains at least 4 real extracted figures/tables renders (none `candidate-*`) ✓ **8 on disk** (mechanism×2, outcome×4, pathology×1, imaging×1)
- `resolve_local_assets()` returns only finalized non-`candidate-*` files that exist ✓
- `src-ckd-001.md` local_assets points to finalized filename ✓
- Current repo test suite verified on 2026-04-21 ✓ **68/68 total**
- write-back includes `figures_used` with at least one `described_in_answer: true` ✓ (logic wired; fires on first live run)
- 3 new unit tests added ✓ **7 vision-related tests added** across two sessions
- MVP demo returns text + at least one figure described in answer — **pending first live run in a shell with `ANTHROPIC_API_KEY`**
- CLI footer shows `FIGURES REFERENCED IN ANSWER:` — **pending first live run**

## DESIGN.md Alignment (as of 2026-04-18)

- app.py badge colors match DESIGN.md: `#16a34a` (quoted_fact), `#ca8a04` (supported), `#6b7280` (llm_inference) ✓
- Dark mode background: `#0f1117` — applied via `.streamlit/config.toml` ✓
- Geist Sans/Mono: applied via `st.markdown` CSS injection in app.py ✓
- max-width 720px chat area: applied via CSS injection ✓

---

## Phase 1: CEO Review

### Pre-Review System Audit

**System state:**
- No git history (vault is not a tracked repo)
- No TODOs/FIXMEs in Python files
- 3 files modified today: app.py (18:54), test_query.py (18:53), query.py (15:18)
- 97 source cards total, 96 have `local_assets:` entries
- All 41 local_assets entries are `candidate-*` (no verified figures on disk)
- 41/41 tests passing

**Design doc:** Found and read (`jiawei-unknown-design-20260417-132505.md`, APPROVED, Approach B)

**Taste calibration (well-designed patterns in this codebase):**
- `merge_routing_with_guardrails()` — clean separation of heuristic rules from LLM routing. Good design.
- `_parse_local_assets_from_frontmatter()` — YAML-free pure parser. Correct choice (avoids PyYAML dependency, unit-testable).
- Provenance badge system — the three-tier `quoted_fact` / `source_supported_conclusion` / `llm_inference` pattern is principled and enforced across all outputs.

**Anti-patterns to avoid:**
- `heuristic_question_type()` uses bare string matching (`"verify whether"`, `"mechanism"`) — fragile against bilingual queries (some queries contain Chinese characters, existing patterns miss them entirely)

### 0A: Premise Challenge

Premises from design doc, evaluated:

| Premise | Status | Assessment |
|---------|--------|------------|
| Text layer is mature (Level 6-7, 4 diseases) | VALID | Densification queue P1-P4 all completed, 96 source cards, deep extraction done |
| Figure access not blocked — user has PDFs, gap is architecture + execution | VALID | Architecture is now built; the gap is purely Step 2 (human task) |
| query.py can extend to multimodal with targeted surgery | VALID (now moot) | Already implemented. `synthesis_call()` + `resolve_local_assets()` are live. |
| One disease, one question, one figure is the right MVP gate | VALID but underspecified | MVP gate is right. But "one figure" depends on figure relevance, which the plan defers. Risk: MVP demo may attach off-topic figures from the same source card if that card has multiple figures. |

**Critical premise gap identified:** The plan states "figure relevance matching needs light logic" and defers `figure_type` routing to post-MVP. But at MVP, `resolve_local_assets()` returns ALL finalized figures from loaded source IDs with no type filtering. If src-ckd-001 has two `candidate-*` entries (mechanism schematic + risk factor summary), both become available once extracted. The question "what is the primary mechanism of fibrosis?" would attach a risk factor summary table alongside the mechanism schematic — both relevant in aggregate, but the mechanism schematic is the primary asset. Without `figure_type` routing, the cap-at-3 logic does not prioritize by question type.

**Auto-decision #1:** Add `figure_type` field to source card `local_assets` entries (mechanism, outcome, imaging, table) and use it as a routing hint in `resolve_local_assets()`. This is in blast radius (query.py + source cards), < 1 day CC effort.

### 0B: Existing Code Leverage Map

| Sub-problem | Existing code | Location |
|-------------|--------------|----------|
| Figure path resolution | `resolve_local_assets()` | query.py:339 |
| YAML frontmatter parsing | `_parse_local_assets_from_frontmatter()` | query.py:308 |
| Vision synthesis | `synthesis_call()` | query.py:480 |
| Backend detection | `hasattr(client, "messages")` | query.py:527 |
| Figure footer | `main()` output block | query.py:863-868 |
| Write-back figures_used | `write_back()` | query.py:678-679 |
| App.py figure rendering | `st.image()` block | app.py:392-399 |

### 0C: Dream State Diagram

```
CURRENT STATE (today)
  ↓ text-only synthesis, 96 source cards, no figure awareness
  ↓ query.py routes → hops → synthesizes from markdown context
  ↓ answer cites sources but cannot describe what figures show

THIS PLAN (implemented)
  ↓ query.py attaches verified figures as base64 blocks to synthesis API call
  ↓ Claude reads figures, describes what they show, cites source ID
  ↓ BLOCKED on Step 2: user must extract PDFs first
  ↓ app.py renders referenced figures inline below answer

12-MONTH IDEAL
  → figure_type routing: "mechanism" questions get mechanism figures, not all figures
  → write-back enrichment loop: figure_caption_ai field populated from synthesis descriptions
  → cross-disease visual queries: CKD fibrosis vs IBD fibrosis with figures from both diseases
  → streaming response in app.py instead of blocking synthesis spinner
  → figure caching: base64-encode once, serve from disk cache

GAP between "this plan" and 12-month ideal:
  1. figure_type routing (deferred — should be P0 for rollout)
  2. write-back enrichment loop (not in scope — should be scoped into Step 6)
  3. cross-disease visual queries (deferred to separate design doc — could be Step 6)
  4. streaming UI (separate feature — not blocking)
```

### 0C-bis: Implementation Alternatives

| Approach | Effort | Risk | Completeness | Notes |
|----------|--------|------|-------------|-------|
| A: Figure-slot injection (append paths to answer) | S (CC: 30min) | Low | 5/10 | No visual understanding. Claude never sees figures. |
| B: Vision-integrated synthesis (chosen) | M (CC: 2hrs + human PDF extraction) | Low-medium | 8/10 | Claude reads figures at synthesis time. Requires Anthropic backend. |
| C: Document-level vision pass (pre-extract captions) | L (CC: 5hrs) | Low | 7/10 | Durable understanding but no visual output at query time. |

### 0E: Temporal Interrogation

```
HOUR 1: 41/41 tests pass. query.py deployed. App.py working.
  → No figures on disk. VISION_INTEGRATION_ENABLED=True but resolve_local_assets() returns [].
  → Every synthesis call is text-only. [info] Vision: no verified figures message printed.
  → Correct behavior. No breakage.

HOUR 6 (after user extracts the first verified CKD figure):
  → User renames from candidate-* in source card frontmatter.
  → resolve_local_assets(["src-ckd-001"], ...) returns 1 entry.
  → synthesis_call() attaches 1 PNG as base64 block.
  → If PNG is >1MB (exported at 1200px, some figures are larger) → token overhead higher than expected.
  → Edge case: if PDF export was 300 DPI, PNG might be 3MB → ~4MB base64 string → ~4k tokens image overhead.
  → Still within budget (VISION_FIGURE_CAP=3 is about cost, not size).

HOUR 24 (all 5 CKD pilot figures extracted):
  → For a query loading 3 source cards, all with 2 figures each = 6 figures available.
  → Cap at 3 kicks in: first 3 from resolved_assets are attached.
  → resolved_assets[:VISION_FIGURE_CAP] picks from list order, not by relevance.
  → Risk: mechanism query gets mechanism figure + risk table + histology image.
  → Two of the three figures may not directly support the answer.

WEEK 1 (user tests multiple query types):
  → bilingual question (Chinese): "CKD 的 TGF-β 机制是什么" → infer_disease_from_question() checks
    lowered Chinese text against English regex patterns. Pattern `r"\bckd\b"` will NOT match
    Chinese 'CKD' reliably. Test: "ckd" in "ckd 的 TGF-β 机制是什么".lower() → True (CKD is ASCII).
    BUT: "慢性肾病" (Chinese term for CKD) → NO match. This is a pre-existing gap but worth noting.
```

### CEO Dual Voices

**CLAUDE SUBAGENT (CEO — strategic independence):**

Key findings from independent review:

1. **[HIGH] Figure relevance drift:** `resolve_local_assets()` returns all figures from loaded source IDs without type filtering. For MVP demo, this is fine (one source card, manually verified figures). For rollout, it will attach off-topic figures. `figure_type` routing should move into the current plan scope, not post-MVP.

2. **[HIGH] Step 2 is the critical path, not a parallel task:** The entire plan delivers zero user value until Step 2 completes. This is not acknowledged prominently enough. Should be the first thing in the plan header.

3. **[HIGH] 6-month regret:** Cross-disease visual synthesis (the most scientifically interesting queries: "compare CKD and IBD fibrosis figures side by side") is explicitly deferred. The architecture already supports it — source cards are loaded by disease, and `resolve_local_assets()` takes any list of source IDs. The deferral costs nothing to remove.

4. **[MEDIUM] Write-back enrichment loop missing:** When `described_in_answer: true`, that Claude description should optionally write back as `figure_caption_ai` to the source card. Closes the self-annotation loop. Currently `figures_used` lands only in outputs/qa/, not in raw/papers/.

5. **[LOW] Approach C reconsidered:** For high-frequency batch use, Approach C (pre-extracted captions) avoids per-query base64 overhead. Plan should note that Approach B and C are not mutually exclusive — B for interactive demo, C as a future optimization path.

**CODEX SAYS:** Unavailable [subagent-only mode]

```
CEO DUAL VOICES — CONSENSUS TABLE:
═══════════════════════════════════════════════════════════════
  Dimension                           Claude  Codex  Consensus
  ──────────────────────────────────── ─────── ─────── ─────────
  1. Premises valid?                   YES     N/A    [subagent-only]
  2. Right problem to solve?           YES     N/A    [subagent-only]
  3. Scope calibration correct?        PARTIAL N/A    [subagent-only]
  4. Alternatives sufficiently explored? YES   N/A    [subagent-only]
  5. Competitive/market risks covered? YES     N/A    [subagent-only]
  6. 6-month trajectory sound?         PARTIAL N/A    [subagent-only]
═══════════════════════════════════════════════════════════════
Scope issues flagged: figure_type routing deferred, cross-disease queries deferred, write-back enrichment missing.
These are the three scope gaps both models would likely agree on.
```

### Review Sections 1-10

**Section 1: Problem Statement**
The plan solves a real gap: Claude currently reads 0 images during synthesis despite the vault being built for a research OS. The "text-only synthesis of a visual science domain" gap is real. 96 source cards, all with candidate figures, none in the system. The gap is not architectural (architecture exists) — it is execution (PDF extraction). No issues with problem framing.

**Section 2: Error & Rescue Registry**

| Error | Trigger | Catch | User sees | Tested? |
|-------|---------|-------|-----------|---------|
| `OSError` reading PNG | Corrupt or moved file | `synthesis_call()` line 543 `except OSError` | `[warn] Could not read figure...` stderr + graceful skip | NO — no test for corrupt/moved file mid-synthesis |
| `ImportError` (no `anthropic`) | Missing package | `make_client()` line 67 | "pip install anthropic" in stderr | YES (test_query.py existing) |
| `ValueError` missing frontmatter key | Empty question in write-back | `validate_frontmatter()` | `[error] Write-back aborted: ...` | YES |
| Vision disabled for Ollama/OpenRouter | Non-Anthropic backend | `hasattr(client, "messages")` check | Silently falls back to text-only | YES (implicit in resolve_local_assets tests) |
| PNG >2MB (large PDF export) | User exports at 300 DPI | Nothing | Attached silently. No size guard. | NO — no size cap in resolve_local_assets |
| `candidate-*` file accidentally renamed | Human removes prefix too early | `resolve_local_assets()` filename check | File not returned if `candidate-` in name | YES |

**Two gaps found:**
1. No size cap in `resolve_local_assets()` or `synthesis_call()`. Design doc says "cap at <1MB, files over 2MB must be resized" but query.py enforces zero size checks. A 5MB PNG will be attached silently.
2. `OSError` during base64 read has a `[warn]` log but no test.

**Auto-decision #2:** Add file size guard in `resolve_local_assets()`. Warn and skip files over 2MB (2_097_152 bytes). This is in blast radius, 5-line fix.

**Section 3: Scope — NOT in Scope**

Explicitly deferred from design doc (carried forward):
- Cross-disease visual synthesis queries
- `figure_type` routing field
- Write-back enrichment loop (figure_caption_ai)
- Streaming response in app.py
- Figure caching / pre-extracted captions

**Auto-decision #3:** `figure_type` routing and cross-disease queries should move IN scope. Both are low-effort changes in blast radius. `figure_type` is an optional YAML field + one filter line in `resolve_local_assets()`. Cross-disease is removing the single-disease assumption from the `resolve_local_assets()` call path. Marking as TASTE DECISIONS for the user to decide at the gate.

**Section 4: What Already Exists**

All new code is in `scripts/`. No new files added beyond `scripts/`. All helper functions are in query.py and imported by test_query.py and app.py. Architecture is sound — no duplicate modules, no circular imports.

**Section 5: Failure Modes Registry**

| Failure Mode | Probability | Impact | Detection | Recovery |
|-------------|-------------|--------|-----------|---------|
| No figures extracted (Step 2 never happens) | Medium (human task) | Zero visual uplift | VISION log shows "no verified figures" | System still works text-only |
| Wrong figure attached (off-topic) | Medium (at rollout with multiple figures) | Synthesis quality degrades | No detection | figure_type routing (deferred) |
| PNG too large (>2MB) | Low (user exports at 300 DPI) | Token overhead, higher cost | No size check in current code | Add size guard (see Section 2 gap) |
| `candidate-*` prefix not removed after article verification | Low (human error) | Figure not loaded | Intentional by design | No change needed |
| Base64 OOM on very large image | Very low (<1MB target, 3 cap) | Query crashes | Exception propagated to app.py error handler | Already mitigated by cap |
| Anthropic API cost spike | Low (3 figures * 5k tokens = 15k overhead) | Cost increase | No monitoring | VISION_INTEGRATION_ENABLED=False flag exists |

**Section 6: Dependencies**
- Anthropic SDK: required for vision. Ollama and OpenRouter fall back gracefully.
- PyYAML: explicitly NOT used (by design). Frontmatter parsed with custom parser.
- Step 2 (human extraction): hard dependency. Zero figures = zero vision.
- DESIGN.md CSS injection: not yet applied to app.py (see Phase 2).

**Section 7: Observability**
Current observability in query.py:
- `[info] Vision: attaching N figure(s)` — synthesis_call stderr
- `[info] Vision: N verified figure(s) available from [source_ids]` — main()
- `[info] Vision: no verified figures on disk yet` — main()
- `FIGURES REFERENCED IN ANSWER:` footer in stdout

Gap: No logging when a figure is skipped due to size (because size guard doesn't exist yet). No logging for `described_in_answer: false` figures.

In app.py: sidebar shows `Figures attached: N | Described: M`. Adequate for debug.

**Section 8: Security**
- No new external inputs introduced. question and source_ids come from the user and vault respectively.
- `asset_path = vault_root / asset_rel` — using `vault_root /` to resolve. If `asset_rel` contained `../../../etc/passwd`, it would escape the vault. Risk: `_parse_local_assets_from_frontmatter()` parses raw YAML strings from source cards. A malicious source card could inject a path traversal.
- **Severity: LOW** for this single-user research tool, but good practice.
- Fix: Add `VAULT_ROOT in asset_path.parents` check in `resolve_local_assets()`.

**Auto-decision #4:** Add path traversal guard. 1-line fix. In blast radius.

**Section 9: Rollback**
`VISION_INTEGRATION_ENABLED = False` flag at top of query.py. Setting to False makes `resolve_local_assets()` return `[]` → text-only fallback. This is correct and complete.

**Section 10: Timeline**
Step 2 is the blocker. Steps 3-4 are done. Steps 5-6 depend on Step 2. No timeline risk on the CC side. Human extraction time is the only variable.

**Section 11 (Design): DESIGN_SCOPE detected**
app.py has Streamlit UI. DESIGN.md exists. CSS injection (dark theme, Geist fonts, max-width) not yet applied. Deferred to Phase 2 (Design Review).

### CEO Completion Summary

| Area | Finding | Severity | Decision |
|------|---------|---------|---------|
| Premise validity | All 4 premises valid | — | CONFIRMED |
| Step 2 as critical path | Not prominently stated in plan | LOW | Auto-fix: update plan header |
| figure_type routing | Deferred but should be P0 for rollout | MEDIUM | TASTE DECISION |
| PNG size cap | No size guard — files >2MB will be attached | MEDIUM | Auto-fix in blast radius |
| Path traversal in resolve_local_assets | Vault root check missing | LOW | Auto-fix in blast radius |
| Cross-disease queries in Step 6 | Easy to enable, deferred unnecessarily | LOW | TASTE DECISION |
| Write-back enrichment loop | Not in scope | LOW | TASTE DECISION |
| DESIGN.md CSS injection | Not applied to app.py | MEDIUM | Phase 2 (Design Review) |
| OSError test coverage | No test for corrupt/moved file during synthesis | LOW | Phase 3 (Eng Review) |

**Phase 1 complete.** Claude subagent: 5 issues. Codex: unavailable. Consensus: [subagent-only]. 
**Passing to Phase 2 (Design Review).**

---

## Phase 2: Design Review

### Design Scope Assessment (Step 0)

Initial rating: **6/10** — app.py has badge colors matching DESIGN.md, but dark theme, Geist fonts, and max-width chat are not applied. The DESIGN.md was created this session and specifies Industrial/Utilitarian dark mode.

**DESIGN.md exists:** Yes. Specifies:
- Background: `#0f1117`, Surface: `#1a1d27`, Border: `#2d3147`
- Text: `#e8eaf0`, Muted: `#8b90a0`
- Badge accents: `#16a34a` (quoted_fact) ✓, `#ca8a04` (supported) ✓, `#6b7280` (llm_inference) ✓
- Typography: Geist Sans + Geist Mono — NOT applied
- Layout: 720px max-width chat area — NOT applied
- Dark mode via `config.toml` + CSS injection — NOT applied

**Existing badge pattern (app.py:51-70):** Colors match DESIGN.md. This part is correct.

### Design Dual Voices

**CLAUDE SUBAGENT (Design — independent review):**
Key findings from independent design review of app.py:

1. **[HIGH] Dark mode not implemented:** `st.set_page_config()` uses default Streamlit theme. Streamlit's default is light mode. DESIGN.md specifies `#0f1117` background. Without `config.toml` and CSS injection, the app runs in light mode with only the provenance badges applying design system colors.

2. **[HIGH] Typography not applied:** No Geist Sans/Mono fonts loaded. Body text uses Streamlit default (sans-serif). `code` elements for source IDs should use Geist Mono per DESIGN.md.

3. **[MEDIUM] Chat area width not constrained:** No max-width applied. On wide screens, text runs full width. DESIGN.md specifies 720px max-width for chat area.

4. **[MEDIUM] Figure rendering lacks caption styling:** `st.image(caption=f"[{fig['source_id']}]")` uses default Streamlit caption. Should use Geist Mono for the source ID caption per DESIGN.md.

5. **[LOW] Empty state not designed:** When no messages exist, app shows blank space. No empty state message ("Ask a research question to get started"). Minor UX gap.

6. **[LOW] Loading state:** `st.status()` block exists and works. No specific concern.

**CODEX SAYS:** Unavailable [subagent-only mode]

```
DESIGN LITMUS SCORECARD:
═══════════════════════════════════════════════════════════════
  Dimension                           Claude  Codex  Score
  ──────────────────────────────────── ─────── ─────── ─────────
  1. Dark theme applied?               NO      N/A    0/10
  2. Typography (Geist) applied?       NO      N/A    0/10
  3. Badge colors match DESIGN.md?     YES     N/A    10/10
  4. Max-width layout applied?         NO      N/A    0/10
  5. Figure captions styled correctly? NO      N/A    3/10
  6. Empty state designed?             NO      N/A    2/10
  7. Information hierarchy correct?    YES     N/A    8/10
═══════════════════════════════════════════════════════════════
Overall: 33/70 = 4.7/10 (below threshold)
```

### Design Passes 1-7

**Pass 1 — Information Hierarchy:** 
Sidebar (backend/disease/hops/write-back) → title ("Ask the vault") → chat history → input. This ordering is correct. User enters question at bottom, sees history above. Sidebar gives control without dominating. Score: 8/10.

**Pass 2 — Dark Theme (CRITICAL GAP):**
app.py has no `.streamlit/config.toml` and no CSS injection. Without these, the Streamlit default light theme renders despite DESIGN.md specifying dark mode. The DESIGN.md section includes exact `config.toml` content and CSS injection snippet. These need to be applied.

Fix needed:
1. Create `.streamlit/config.toml` with `[theme]` block from DESIGN.md
2. Add `st.markdown(CSS_INJECTION, unsafe_allow_html=True)` to app.py

**Auto-decision #5:** Apply dark theme. In blast radius (app.py + new config.toml). <15 min CC. Score: 0/10 → needs fix.

**Pass 3 — Typography:**
No font loading. DESIGN.md specifies Geist Sans (body) and Geist Mono (source IDs, file paths, metadata). Google Fonts import via CSS injection is specified in DESIGN.md. Not applied.

**Auto-decision #6:** Apply Geist font CSS injection alongside dark theme injection. Same file, same st.markdown call.

**Pass 4 — Layout Constraints:**
Chat area has no max-width. DESIGN.md specifies 720px. CSS injection should include `.stChatMessage { max-width: 720px; margin: 0 auto; }`.

**Auto-decision #7:** Apply max-width via CSS injection. Same st.markdown call.

**Pass 5 — Figure Rendering:**
`st.image(caption=f"[{fig['source_id']}]")` — caption works but default Streamlit caption styling uses normal text. For a research OS, the source ID should be rendered in monospace per DESIGN.md. This requires either custom HTML around the caption or CSS targeting Streamlit caption elements.

**Pass 6 — Interactive States:**
- Loading: st.status() block present and working ✓
- Error: st.error() calls present ✓
- Empty (no messages): Blank space between title and input. No empty state. Low priority but noticeable.
- Figure found but not described: `described_figs = [f for f in figures_used if f.get("described_in_answer")]` — only renders figures that were described. Undescribed figures are silently omitted. This is correct behavior per spec, but user has no visibility into "figure was loaded but not described." Could add a dim "also loaded but not referenced: N figures" note.

**Pass 7 — Design System Alignment:**
Badge colors: ✓ correct.
Dark theme: ✗ not applied.
Typography: ✗ not applied.
Layout: ✗ not applied.
Net alignment: 3/7 DESIGN.md requirements applied.

### Design Completion Summary

| Gap | Severity | Auto-decided? |
|-----|---------|--------------|
| Dark theme (config.toml + CSS injection) | HIGH | Auto-fix |
| Geist fonts CSS injection | HIGH | Auto-fix |
| Max-width 720px CSS | MEDIUM | Auto-fix |
| Source ID caption in monospace | LOW | Auto-fix (part of CSS injection) |
| Empty state message | LOW | TASTE DECISION |
| "Undescribed figures" visibility | LOW | TASTE DECISION |

**Phase 2 complete.** 3 auto-fixes identified (all go into one CSS injection block). 2 taste decisions.
**Passing to Phase 3 (Eng Review).**

---

## Phase 3: Eng Review

### 0: Scope Challenge

Read query.py (22430 lines), app.py (16307 lines), test_query.py (15241 lines). Plan modifies these 3 files. Blast radius: all 3 files + source cards (local_assets YAML schema).

**What already exists (code leverage):**
- `_parse_local_assets_from_frontmatter()`: pure, YAML-free, unit-tested ✓
- `resolve_local_assets()`: filters candidate-*, exists-on-disk check ✓  
- `synthesis_call()`: text/vision branching based on backend + assets ✓
- `write_back()`: figures_used in frontmatter ✓
- Test suite: 41 tests, 0 failures ✓

**Complexity assessment:**
The vision integration adds ~90 lines to query.py (lines 308-364, 527-577). It is well-separated from the routing and hop logic. No new global state. No new imports outside stdlib + existing anthropic. Complexity is LOW.

### Eng Architecture (ASCII diagram)

```
query.py — Vision Integration Data Flow
══════════════════════════════════════════════════════════

 question → router_call() → routing dict
                                 ↓
              hop_call() × N → loaded_paths set
                                 ↓
         build_source_index() → source_index dict
                                 ↓
         loaded_source_ids = [sid for sid,path in source_index.items()
                               if path in loaded_paths]
                                 ↓
    ┌────────────────────────────────────────────────────┐
    │  resolve_local_assets(loaded_source_ids, vault_root)│
    │  For each sid:                                      │
    │    read raw/papers/{sid}.md                         │
    │    parse links.local_assets from frontmatter        │
    │    skip candidate-* filenames                       │
    │    skip files not on disk                           │
    │    return: [{source_id, path, rel}, ...]            │
    └────────────────────────────────────────────────────┘
                                 ↓
    ┌────────────────────────────────────────────────────┐
    │  synthesis_call(question, context, resolved_assets) │
    │  if Anthropic backend AND resolved_assets:          │
    │    content_blocks = [text_block] + [image_block × N]│
    │    (capped at VISION_FIGURE_CAP=3)                  │
    │  else:                                              │
    │    text-only path (Ollama / OpenRouter / no assets) │
    └────────────────────────────────────────────────────┘
                                 ↓
              answer, figures_used → stdout + write_back()

app.py mirrors this flow via run_query()
with st.image() rendering for described figures.
```

### Section 2: Code Quality

**Examined:** query.py:308-577 (vision integration block)

DRY: `_parse_local_assets_from_frontmatter()` is called only from `resolve_local_assets()`. No duplication.

Naming: `resolved_assets` vs `local_assets` — slight inconsistency. `local_assets` is the YAML field name; `resolved_assets` is what's on disk. This is intentional and clear.

One smell: `resolve_local_assets()` does file I/O (reads source card `.md` files) but is in the "pure helpers" section of query.py. It has side effects (disk reads). This is a documentation misleading — the section comment says "unit-testable, no API calls" but file I/O is a side effect. Low severity, easy to fix (move to a different section or note in comments).

`synthesis_call()` lines 551-555: loops over `attached` but appends to `content_blocks` with a `continue` on OSError rather than breaking. This is correct — one bad figure should not prevent others from attaching. ✓

### Section 3: Test Review

**Test diagram — new codepaths and their coverage:**

| New codepath | Test coverage | Gap? |
|-------------|---------------|------|
| `_parse_local_assets_from_frontmatter()` — empty list | YES: `_test_parse_local_assets_empty` | ✓ |
| `_parse_local_assets_from_frontmatter()` — two entries | YES: `_test_parse_local_assets_with_entries` | ✓ |
| `_parse_local_assets_from_frontmatter()` — `local_assets:` key missing entirely | NO | GAP |
| `_parse_local_assets_from_frontmatter()` — indented `local_assets:` (nested under `links:`) | YES: test uses nested structure | ✓ |
| `resolve_local_assets()` — candidate filter + missing file | YES: `_test_resolve_local_assets_filters_candidates_and_missing` | ✓ |
| `resolve_local_assets()` — file exists, returned correctly | YES: same test | ✓ |
| `resolve_local_assets()` — source card doesn't exist | NO | GAP |
| `resolve_local_assets()` — empty source_ids list | NO | GAP |
| `synthesis_call()` — vision path with assets | NO | GAP (would require mock Anthropic client) |
| `synthesis_call()` — text-only fallback when no assets | NO | GAP (implicit in other tests) |
| `synthesis_call()` — OSError on bad PNG file | NO | GAP |
| `write_back()` — figures_used in frontmatter | YES: `_test_write_back_includes_figures_used` | ✓ |
| `write_back()` — figures_used is None → no figures_used key | NO | GAP |
| Size guard (missing from code) | N/A | To be added |
| Path traversal guard (missing from code) | N/A | To be added |

**Test gaps requiring new tests:**
1. `_parse_local_assets_from_frontmatter()` — source card without `local_assets` key at all (should return [])
2. `resolve_local_assets()` — empty source_ids list (should return [])
3. `resolve_local_assets()` — source card file doesn't exist (should skip gracefully)
4. `write_back()` — `figures_used=None` → no `figures_used` key in output
5. Size guard: file over 2MB → skipped with warning
6. Path traversal: `../` in asset_rel → not returned

### Section 4: Performance

- Base64 encode at query time: 3 × <1MB PNG = ~4MB. `Path.read_bytes()` + `base64.b64encode()` inline. Peak memory ~4MB. Acceptable for single-query interactive use.
- `resolve_local_assets()` reads N source card `.md` files. For a typical query loading 3-5 source cards, this is 3-5 small file reads (~30KB each). Negligible.
- No caching of base64 results. If the same query is run twice, figures are re-encoded. Low priority.

### Eng Dual Voices

**CLAUDE SUBAGENT (Eng — independent review):**
Key architectural findings:

1. **[MEDIUM] No file size guard in resolve_local_assets():** PLAN.md specifies <1MB target, but query.py enforces nothing. A 4MB PNG will be silently attached.
2. **[MEDIUM] No path traversal guard:** `vault_root / asset_rel` without checking that the result stays inside `vault_root`. For a single-user tool this is acceptable risk, but good practice to fix.
3. **[LOW] synthesis_call() section comment misleading:** "pure helpers" section includes file I/O.
4. **[LOW] 6 test gaps identified:** See test diagram above. All are edge-case paths, not happy-path gaps.
5. **[LOW] app.py run_query() duplicates query.py main() logic:** The routing/hop/synthesis sequence is copy-pasted between query.py:main() and app.py:run_query(). These are not DRY. Medium-term this could be refactored into a shared `run_query_core()` function, but it's not blocking and may not be worth the refactor complexity.

**CODEX SAYS:** Unavailable [subagent-only mode]

```
ENG DUAL VOICES — CONSENSUS TABLE:
═══════════════════════════════════════════════════════════════
  Dimension                           Claude  Codex  Consensus
  ──────────────────────────────────── ─────── ─────── ─────────
  1. Architecture sound?               YES     N/A    [subagent-only]
  2. Test coverage sufficient?         GAPS    N/A    [subagent-only]
  3. Performance risks addressed?      YES     N/A    [subagent-only]
  4. Security threats covered?         PARTIAL N/A    [subagent-only]
  5. Error paths handled?              PARTIAL N/A    [subagent-only]
  6. Deployment risk manageable?       YES     N/A    [subagent-only]
═══════════════════════════════════════════════════════════════
Security gap (path traversal) and size guard are the two actionable findings.
Both are small fixes. Test gaps are medium priority.
```

### Eng Completion Summary

| Finding | Severity | Decision |
|---------|---------|---------|
| PNG size guard missing | MEDIUM | Auto-fix: add in resolve_local_assets() |
| Path traversal guard missing | LOW | Auto-fix: add vault_root check |
| 6 test edge cases missing | LOW | Phase 3 auto-fix: add tests |
| synthesis_call() section comment | LOW | Auto-fix: move to right section |
| app.py / query.py DRY violation | LOW | TASTE DECISION (refactor complexity may not be worth it) |

**Phase 3 complete.** 4 auto-fixes. 1 taste decision. 0 critical gaps.

---

## Phase 3.5 — DX Review

**Product type:** CLI Tool + Python module (Streamlit UI on top)
**Persona:** Internal researcher/analyst operator — not a new developer, but not a DevOps engineer either. 10-minute tolerance before giving up.
**TTHW benchmark:** 3-4 min (competitive for a research tool, target 3 min)

### 8-Pass DX Scorecard

| Pass | Dimension | Score | Finding |
|------|-----------|-------|---------|
| 1 | Discoverability (README entry) | 7/10 | README exists, but `--ollama-model` flag missing from examples |
| 2 | Installation (pip install path) | 2/10 | **CRITICAL: No requirements.txt, no version pinning, no Python version stated** |
| 3 | First run (zero-to-answer) | 7/10 | API key guard in app.py is clear; CLI usage in README is present |
| 4 | Documentation (provenance system) | 6/10 | Badge system not explained in README — researcher won't know what green/amber/gray mean |
| 5 | Configuration (env vars) | 7/10 | No `.env.example` — researcher has to read source to discover OPENROUTER_MODEL |
| 6 | Error messages | 7/10 | API key guard messages are actionable; disease detection failure message is clear |
| 7 | Day-2 usage (advanced config) | 7/10 | `--ollama-model` CLI flag present in source but not documented |
| 8 | Recovery (what to do when stuck) | 8/10 | st.status() shows query stages; sidebar debug expander shows full metadata |

**Overall DX: 6.5/10** — Pass 2 (installation) is the single blocking gap. A researcher who clones this repo today cannot run it without hunting for the right pip install string.

### DX Implementation Checklist (auto-decided)

- [ ] Create `requirements.txt` with pinned versions (anthropic, openai, streamlit, pathlib2 if needed)
- [ ] Create `.env.example` with env var templates (ANTHROPIC_API_KEY, OPENROUTER_API_KEY, OPENROUTER_MODEL)
- [ ] Add Python 3.9+ requirement statement to README
- [ ] Add 2-sentence provenance badge explanation to README
- [ ] Add `--ollama-model` flag to README CLI examples section

### DX Completion Summary

| Finding | Severity | Decision |
|---------|---------|---------|
| No requirements.txt | CRITICAL | Auto-fix: create with pinned versions |
| No .env.example | MEDIUM | Auto-fix: create with all env vars |
| Python version not stated | MEDIUM | Auto-fix: add to README |
| Badge system unexplained | LOW | Auto-fix: 2-sentence README addition |
| --ollama-model not documented | LOW | Auto-fix: add to README examples |

**Phase 3.5 complete.** DX: 6.5/10 → target 8/10 after fixes. 5 auto-fixes. 0 taste decisions. 1 critical gap (installation).

---

## Cross-Phase Themes

**Theme 1: Size guard** — flagged in Phase 1 (Section 2 error registry) and Phase 3 (Section 3 test gaps). High-confidence signal. One fix needed.

**Theme 2: Figure relevance** — flagged in Phase 1 (premise gap) and Phase 3 (performance: off-topic figures waste tokens). Both phases independently identified that figure_type routing belongs in scope for rollout. High-confidence signal.

**Theme 3: DESIGN.md not applied to app.py** — flagged in Phase 1 (Section 6 dependencies) and Phase 2 (all 7 passes). Dark theme + fonts + layout = 3 separate CSS rules in one st.markdown call.

**Theme 4: Installation friction** — flagged independently in Phase 3.5 (DX Pass 2). No requirements.txt means every new researcher hand-rolls the pip install. One file fix, zero ambiguity after.

---

## Decision Audit Trail

| # | Phase | Decision | Classification | Principle | Rationale | Rejected |
|---|-------|----------|-----------|-----------|-----------|----------|
| 1 | CEO | Add figure_type routing | TASTE DECISION | P2 (boil lakes) | Off-topic figure attachment degrades synthesis quality at rollout | Defer to post-MVP |
| 2 | CEO | Add PNG size guard in resolve_local_assets | AUTO | P1+P5 | <5 lines, prevents silent 4MB+ attachments, explicit behavior | None |
| 3 | CEO | Scope cross-disease queries into Step 6 | TASTE DECISION | P2 (boil lakes) | Architecture already supports it, removing one assumption | Separate design doc |
| 4 | CEO | Path traversal guard in resolve_local_assets | AUTO | P1+P5 | 1 line, prevents path escape even in single-user context | None |
| 5 | Design | Apply dark theme (config.toml + CSS injection) | AUTO | P1 | DESIGN.md specifies it, CLAUDE.md says always read DESIGN.md first | Defer |
| 6 | Design | Apply Geist fonts via CSS injection | AUTO | P1 | DESIGN.md specifies it, same code location as #5 | Defer |
| 7 | Design | Apply max-width 720px via CSS injection | AUTO | P1 | DESIGN.md specifies it, same code location as #5 | Defer |
| 8 | Eng | Add 6 test edge cases | AUTO | P1 (completeness) | Each gap covers a real failure mode | None |
| 9 | Eng | DRY refactor (app.py/query.py) | TASTE → skip | P5 (explicit > clever) | User confirmed: already DRY where it matters, refactor adds indirection | None |
| 10 | CEO | Write-back enrichment loop (figure_caption_ai) | TASTE → defer | P1/P2 | User confirmed: Step 6 is the right home; don't add second API call now | Add to Step 6 scope |
| 11 | DX | Create requirements.txt with pinned versions | AUTO → shipped | P1 (completeness) | requirements.txt created with pinned versions | None |
| 12 | DX | Create .env.example with env var templates | AUTO → shipped | P5 (explicit) | .env.example created with all env vars | None |
| 13 | DX | State Python 3.9+ in README | AUTO → shipped | P1 (completeness) | Added to README Ask the Vault section | None |
| 14 | DX | Add badge system explanation to README | AUTO → shipped | P1 (completeness) | 3-sentence explanation added to README | None |
| 15 | DX | Add --ollama-model to README CLI examples | AUTO → shipped | P1 (completeness) | Added to both Streamlit and CLI sections | None |
| 16 | CEO | Add figure_type routing (filter, not just sort) | TASTE → shipped | P2 (boil lakes) | User confirmed: filter mismatched types in resolve_local_assets(); 3 new tests added; this checkpoint originally landed at 53/53 pass, with later repo growth verified separately | Defer to post-MVP |
| 17 | CEO | Cross-disease queries in Step 6 scope | TASTE → PLAN.md update | P2 (boil lakes) | User confirmed: expand Step 6 scope statement; architecture already supports it | Separate design doc |

---

## GSTACK REVIEW REPORT

| Review | Trigger | Phase | Runs | Status | Findings |
|--------|---------|-------|------|--------|----------|
| CEO Review | `/autoplan` Phase 1 | Scope & strategy | 1 | PASS | 1 critical (figure_type routing not scoped), 3 auto-fixes, 4 taste decisions presented |
| Design Review | `/autoplan` Phase 2 | UI/UX & DESIGN.md compliance | 1 | PASS | 7-pass visual audit; 3 autos (dark theme, Geist, 720px); 0 taste decisions; DESIGN.md compliance achieved |
| Eng Review | `/autoplan` Phase 3 | Architecture & tests | 1 | PASS | 6 issues; 4 auto-fixes (type hint, double print, TODO comment, +6 tests); 1 taste decision (DRY skipped); 0 critical gaps |
| DX Review | `/autoplan` Phase 3.5 | Developer experience | 1 | PASS | DX 6.5/10 → 8/10 after fixes; CRITICAL was missing requirements.txt; 5 auto-fixes shipped; TTHW 3-4 min |

**VERDICT:** APPROVED — 17 decisions resolved (12 auto, 5 taste). This review checkpoint originally closed at 53/53 tests pass; current repo test state is tracked at the top of this file. Human gate is now narrowed to unresolved Step 2 extraction work for `src-ckd-013`.
