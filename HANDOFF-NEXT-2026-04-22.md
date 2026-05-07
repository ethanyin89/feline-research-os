---
title: Handoff — Karpathy Alignment + Ordinary-User Surface, 2026-04-22
date: 2026-04-22
type: handoff
audience: next-model
read-before-acting: true
---

# Handoff — Karpathy Alignment + Ordinary-User Surface

This handoff is written to be self-contained. A new model can read this single file
and know exactly what is true, what is missing, and what to do next, without first
reading 10 prior handoffs.

It does NOT replace `HANDOFF.md`. It is a focused successor that adds:

- a clean diff between the current vault and Karpathy's LLM-wiki blueprint
- a content audit of the five disease × 24-source modules
- a presentation audit through the eyes of a non-maintainer reader
- a prioritized, executable next-move queue

If anything in this document conflicts with `HANDOFF.md`, prefer this file for the
gap diagnosis and prefer `HANDOFF.md` for the operating-plan rules and constraints.

---

## 1. 30-Second Reality

- Architecture is at `7/7` Karpathy layers. No new system to invent.
- Content base = `120` paper source cards (`5 diseases × 24`) + `14` regulation cards.
  All `120` are explicit `extraction_depth: full`. **No fake data.**
- Verified images on disk = `12`: CKD has `8`; FIP/HCM/IBD/Diabetes each has
  one verified first-pass asset. Source-card `local_assets` contain no
  unverified `candidate-*` paths.
- Streamlit ordinary-user front door is functional, API-first, and the
  acceptance runner now preflights missing keys correctly. `live acceptance`
  remains blocked only because no real API key is present in this shell.
- Tests: `68/68 pass` as of 2026-04-21 baseline.
- Real remaining gaps are **execution + presentation**, not architecture.

## 2. What Karpathy Asked For vs What We Have

Karpathy's blueprint (six layers + future):

```
ingest → compile → IDE → Q&A → output → linting → (future: finetune)
```

| Layer | Status | Visible Gap |
|------|--------|-------------|
| Ingest — text | ✅ 120 paper cards across 5 diseases + 14 regulation cards | Web Clipper / batch ingest is still manual; no automated pull from PMC/PubMed |
| Ingest — image | ⚠️ Pipeline complete, CKD has 8 verified assets; FIP/HCM/IBD/Diabetes each has one first-pass verified asset | Candidate targets remain in manifests/TODOs; depth expansion is still needed outside CKD |
| Compile | ✅ 93 topic pages + `compile_trigger.py` | Trigger exists but is not wired to a git hook, cron, or Obsidian command. Manual recompile habit |
| IDE | ✅ Obsidian | — |
| Q&A | ✅ `query.py` + routing + hops + vision + provenance + `search.py` pre-heat | Live runtime not validated because no API key is present; acceptance runner now records blocked-missing-key instead of template-only |
| Output — text | ✅ briefings / dossiers / Marp slides exist for all 5 diseases | Promotion habit (output → topic) is not yet routine |
| Output — figures | ✅ `charts.py` (radar / coverage / maturity) | Only 3 chart types; cross-disease comparison missing |
| Linting | ⚠️ `linting-schedule.md` defines policy; scripts exist | No cron / CI / Obsidian alert; not yet a daily immune system |
| Future — finetune | ❌ Not started | Long-term, intentionally deferred |

### Where Karpathy's Spirit Is Still Underdelivered

These are the qualitative misses, not table cells:

1. **"Wiki is being lived in"** — Karpathy's loop adds up across days. Our
   `inbox/` + `--save-to-inbox` exists but is not yet on a routine rhythm.
   Outputs accumulate; they do not yet *compound* back into the wiki.
2. **"Self-healing knowledge base"** — `scripts/health.py` now aggregates link
   checks, query tests, source-id uniqueness, candidate-image gate status,
   inbox backlog, acceptance status, compile-trigger status, and API-key
   presence into `system/health-checks/health-report-YYYYMMDD.md`. The remaining
   gap is cadence: it is a command now, not yet cron / CI / Obsidian alert.
3. **"Naive search engine that the LLM also uses"** — `search.py` exists and is
   wired into `query.py` pre-heat, but it is not exposed as a first-class
   reader UI surface (the Streamlit sidebar search exists, but is not the
   primary interaction).
4. **"You ask it like a person"** — Root `start.md` now gives an ask-first
   landing surface, but the full product proof still depends on a live
   Streamlit/API acceptance run with real keys.

## 3. Content Audit — 5 × 24 Source Cards

### 3.1 Hard Numbers (verified 2026-04-21 / 22)

| Disease | Source cards | Round-1 worksheets | Explicit `full` | Topic pages | Bilingual coverage | Verified images |
|---------|--------------|--------------------|-----------------|-------------|-------------------|-----------------|
| CKD | 24 | 24 | 24 | 19 | partial | 8 |
| FIP | 24 | 24 | 24 | 17 | strong | 1 |
| HCM | 24 | 24 | 24 | 20 | strong | 1 |
| IBD | 24 | 24 | 24 | 18 | strong | 1 |
| Diabetes | 24 | 24 | 24 | 19 | none | 1 |

### 3.2 Where Real Risk Still Lives

- **`verification_status: abstract_weighted`** appears in non-CKD source
  cards (e.g. `src-diabetes-001`). This means the extraction was anchored on
  an abstract, not the full text. It is not "fake data," but it is a
  *thinner* truth claim than full-text extraction. The current source-depth
  map and disease dashboards now expose this overlay, so a reader can tell
  `extraction_depth: full` apart from `verification_status: abstract_weighted`.
  CKD's pre-standard source cards have now been backfilled to
  `verification_status: deep_extracted`; the remaining gap is enforcing
  decision-grade claim checks against this field.
- **Diabetes is no longer thin at the topic-count layer, but it is still
  thinner at the evidence-depth / language layer.** It now has 19 topic
  pages, matching the other mature modules numerically. The remaining gap is
  that its compiled layer is memo-derived and all 24 paper cards remain
  `verification_status: abstract_weighted`, with no bilingual compiled layer.
- **Image asymmetry is now a depth gap, not a proof-of-pipeline gap.** CKD has
  8 verified assets; FIP / HCM / IBD / Diabetes each has one verified
  first-pass asset. The Karpathy promise of "markdown + images" needs depth
  expansion outside CKD, not another pipeline proof.
- **`src-ckd-013` is the one durable source-access blocker.** ScienceDirect
  403, Nottingham repository Cloudflare challenge, Bristol metadata-only.
  Document is reachable from search-cache snippets only.
- **Conflict register covers CKD only (13 tensions, 19 cards).** FIP / IBD
  audits found no source-to-source conflict but no equivalent register has
  been built for HCM / Diabetes — meaning we have not even *looked*.

### 3.3 What is *Not* a Gap (do not redo)

- Generic source-card thickening for any of the 5 diseases. All are full.
- Round-1 worksheets. All 120 done.
- CKD bootstrapping. CKD is the mature template — copy from it, do not rebuild it.

## 4. Presentation Audit — Ordinary-User View

Method: walk the surface as if I had no prior context, no maintainer
knowledge, and one question to ask.

### 4.1 What Already Works

- README has a clear "Start Here" section pointing to a single reader entry.
- Streamlit empty state has example chips, provenance guide, "How this
  works", sidebar search, copy-markdown, save-as-markdown.
- Provenance badges are color-coded and consistent with DESIGN.md.
- Maintainer material is now collapsed under `<details>For Maintainers</details>`.

### 4.2 Where the Ordinary-User Lens Still Catches Friction

1. **Two-tier front door has a first-pass fix.**
   Root `start.md` now opens with an ask prompt and hides secondary browsing
   paths under `<details>`. The remaining check is whether the live Streamlit
   surface passes acceptance once a real API key is available.

2. **"Ask the vault" still needs live runtime proof.**
   The markdown landing layer now points to the ask-first path, but the
   Streamlit synthesis path has not been validated in this shell because no
   API key is present.

3. **Disease asymmetry now leaks mostly through depth and language.**
   A reader landing on Diabetes now sees 19 topic pages, but no bilingual
   layer and no full-text-mature paper cards. HCM/IBD still feel stronger
   because their compiled layers are more mature, not because Diabetes lacks
   a topic spine.

4. **The provenance promise is not legible without reading the audit.**
   Badges show after an answer, but a first-time user does not know that
   `[quoted_fact]` means a verbatim quote from a source card and that
   `candidate-*` images are intentionally hidden. This is a *strength* that
   currently reads as opacity.

5. **No "answered before?" trail.**
   Karpathy's wiki accumulates: previously answered questions become wiki
   pages. Our `--save-to-inbox` writes to disk, but the Streamlit UI does
   not yet show *"3 readers asked this before — here are the answers we
   kept."*

6. **Mobile / non-Obsidian read path is implicit.**
   The README assumes Obsidian. A reader on a phone clicking a GitHub link
   sees raw markdown without backlinks, without the Streamlit chat, and
   without the bilingual toggle.

## 5. Prioritized Next Moves (Executable)

The list is ordered so a new model can pick the highest item that matches
its tools and shell capabilities. **Do not block on lower items.**

### P0 — Make the Q&A surface real

1. **Live acceptance run** — get `ANTHROPIC_API_KEY` or `OPENROUTER_API_KEY`
   into a shell that has `streamlit` installed. Run:
   ```bash
   python3 scripts/run_acceptance_checklist.py --backend openrouter
   ```
   Without the key, the runner now writes `Execution mode:
   blocked-missing-key:OPENROUTER_API_KEY` instead of pretending the checklist
   executed.
   Goal: at least 6 of 8 core questions return acceptable answer surfaces
   with 0 fake source ids. Promote the chosen backend to README default.

2. **One ask-native landing page** — first pass complete. Root `start.md`
   now opens with an ask prompt, gives a few bounded example questions, and
   pushes browsing routes, disease dashboards, and maintainer checks under
   `<details>`. Keep improving it through live acceptance feedback rather
   than adding more index pages.

### P1 — Close the visible content asymmetry

3. **Diabetes compile layer parity** — first pass complete. Diabetes now has
   19 topic pages after promoting the memo layer into reader-facing branches:
   diagnostic/workup, diet, remission, treatment map, obesity/body-condition,
   endocrine-secondary disease, pancreatitis, neuropathy/complications,
   epidemiology/breed risk, and SGLT2 label control. Remaining Diabetes gaps:
   full-text maturity and bilingual compiled coverage.

4. **One verified image per non-CKD disease** — now complete for the first
   pass: FIP `src-fip-003` Figure-2, HCM `src-hcm-011` Fig 3, IBD
   `src-ibd-019` Figure 1, and Diabetes `src-diabetes-023` Figure-4 are
   verified against article/PDF labels and linked from source-card
   `local_assets`. Unverified `candidate-*` paths have also been removed from
   source-card `local_assets` and left in manifests/TODOs only. Next image work
   should expand depth, not prove the pipeline again.

5. **Enforce `verification_status`** — the source-depth maps and disease
   dashboards now show `verification_status`, and CKD's pre-standard source
   cards have been backfilled. `scripts/health.py` now hard-checks required
   source-card trust fields and blocks source cards whose `decision_grade`
   outruns their `verification_status`.

### P2 — Make the wiki self-heal

6. **Health cadence** — `scripts/health.py` now exists and writes
   `system/health-checks/health-report-YYYYMMDD.md`. Next step is wiring it to
   a routine trigger: manual end-of-session checklist first, then git hook,
   launchd, cron, or CI.

7. **Wire `compile_trigger.py` to a git hook** — once any source card is
   edited, the operator sees the recompile queue in their next commit.

### P3 — Make the wiki feel lived-in

8. **"Previously answered" panel in Streamlit** — read `inbox/<disease>/`
   and `outputs/qa/`, show the last 5 answered questions with their
   provenance badges. Karpathy's compounding loop only works if past
   answers stay visible.

9. **Conflict register for HCM / Diabetes** — currently only CKD has a
   real register (and FIP / IBD have a confirmed-no-conflicts pass). HCM
   and Diabetes have not even been audited for tensions.

10. **MCP `vault_query` tool** — `mcp_server.py` exposes search /
    compile / source list. Adding the full route + hop + synthesize as a
    fourth tool turns the vault into something a remote agent (Claude
    Desktop, Codex) can talk to without running the Streamlit UI.

### Defer

- Cloudflare / remote-inference backend until OpenRouter acceptance lands.
- Synthetic data + finetuning. Karpathy himself flagged this as future.
- Mobile read path. Investigate only after P0 + P1 close.

## 6. Constraints to Re-State to Every New Model

```
1. No RAG / no vector retrieval. Veterinary vocabulary breaks cosine similarity.
   Architectural decision is locked.
2. Routing path: query.py → question-router.md → topic pages + source cards.
3. Three-tier provenance must be preserved:
   [quoted_fact] / [source_supported_conclusion] / [llm_inference]
4. Filename grammar: src-{disease}-{id}-{figure_type}-{description}.ext
5. The `candidate-*` prefix is the gate. Never strip it without opening the
   original article and verifying the figure / table label. No AI-generated
   images. No guessed figure numbers.
6. Test baseline: python3 scripts/test_query.py (68/68 pass = 2026-04-21)
7. AI-written wiki pages stage in inbox/, promote only after human review.
8. Streamlit runtime is API-first. Ollama is hidden unless ENABLE_OLLAMA=true.
9. No fake data. If a fact is not in a source card, it does not get cited.
   `abstract_weighted` is allowed but must remain visible as such.
10. Two-track owner split: content side owns truth; frontend side owns
    presentation. Frontend may not silently rewrite truth claims.
```

## 7. Verify In 5 Commands

```bash
python3 scripts/test_query.py                                          # 68/68 baseline
find raw/images -type f \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' \) ! -name 'candidate-*' | wc -l   # expect 8
python3 scripts/search.py "phosphorus" --scope raw --limit 3           # search works
python3 scripts/compile_trigger.py --since 1 --json | head -20         # recompile queue
python3 - <<'PY'
from pathlib import Path
import re
root = Path('raw/papers')
for d in ['ckd','fip','hcm','ibd','diabetes']:
    cards = sorted(root.glob(f'src-{d}-*.md'))
    depths = {}
    for p in cards:
        m = re.search(r'^extraction_depth:\s*(\S+)', p.read_text(encoding='utf-8'), re.M)
        k = m.group(1) if m else 'missing'
        depths[k] = depths.get(k, 0) + 1
    print(d, len(cards), depths)
PY
```

Expected output for the last command:
```
ckd 24 {'full': 24}
fip 24 {'full': 24}
hcm 24 {'full': 24}
ibd 24 {'full': 24}
diabetes 24 {'full': 24}
```

## 8. Files To Read Before Touching Anything

In strict order. Stop reading once you have enough to act.

1. This file (you are here).
2. `HANDOFF.md` — operating-plan rules, two-track owner split.
3. `system/indexes/karpathy-gap-analysis.md` — full layer-by-layer gap matrix.
4. `system/indexes/two-track-operating-plan-20260418.md` — content vs frontend owner split.
5. `system/indexes/ordinary-user-llm-wiki-usability-audit-20260410.md` — reader-side audit.
6. `system/indexes/source-depth-map.md` — current depth reality.
7. `scripts/query.py` and `scripts/app.py` — the runtime.

If you are continuing a specific track:

- Content: add `system/indexes/source-processing-ledger-120-20260421.md` + the per-disease depth maps.
- Frontend: add `system/indexes/ux-improvement-handoff-20260418.md` + `scripts/app.py`.

## 9. Do Not Regress To

- "Continue only the CKD image gate."
- Treating presentation polish as the content-side default.
- Reopening locked architecture decisions (RAG / routing / provenance tiers).
- Re-asking the user to confirm repeated source-card processing steps.
- Bilingual-everything for the sake of symmetry. Bilingual lives in compiled
  layers, not raw.
- Strip `candidate-*` prefixes without checking the article figure label.

## 10. One-Line Close

Architecture is done. The remaining work is the difference between
"a vault that *can* answer" and "a wiki that *feels* like an LLM living in it."
That difference is mostly **live acceptance + Diabetes full-text / bilingual
depth**. The first-pass ask-native landing page, Diabetes topic parity, and
non-CKD image pipeline proof are done; image work from here is depth expansion,
not pipeline proof.
