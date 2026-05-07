---
title: Ordinary User Karpathy Gap Recovery Plan, 2026-05-06
status: active
owner: feline-research-os
updated: 2026-05-06
classification: plan
related:
  - system/indexes/karpathy-llm-kb-product-gap-memo.md
  - system/indexes/karpathy-framework-gap-roadmap.md
  - system/indexes/ordinary-user-llm-wiki-usability-audit-20260410.md
  - system/indexes/ask-the-vault-acceptance-checklist-20260416.md
  - system/indexes/ask-the-vault-priority-answer-surfaces-20260416.md
---

# Ordinary User Karpathy Gap Recovery Plan, 2026-05-06

## Classification

This is a **plan** problem.

It is not primarily an idea problem: the target shape is already clear enough from the Karpathy-style LLM wiki direction, the existing vault architecture, and the live Ask the vault test.

It is not primarily a check problem: the live page already exposed the user-facing failure mode.

It is not primarily a debugging problem: there is no single crash or broken file path to fix. The failure is that the content layer has been improved many times, but the ordinary-user answer surface still does not convert that work into a usable product.

## Current Evidence

The live Ask the vault test used a broad ordinary-user prompt: `解释CKD`.

Observed result:

- The app loaded a meaningful context set: one CKD topic page plus fallback source cards.
- The answer shown to the user was too short for a broad explanatory question.
- The page showed `Readings used (11)`, but the main answer did not make those readings visible enough as a trust surface.
- The answer was marked low confidence even though the system had loaded relevant context.
- The warning said the answer relied heavily on inference, but the UI did not explain which claims were supported and which were not.
- The user-facing result felt like a research chat prototype, not a usable LLM wiki entry point.

This means the main gap is no longer raw content volume. The gap is the **content serving layer**: routing, synthesis contract, evidence presentation, and ordinary-user acceptance.

## Updated Judgment

Earlier ordinary-user notes treated the vault as close to usable because the knowledge structure was becoming navigable. That judgment should be downgraded.

Current status:

> The vault is structurally rich but not yet ordinary-user usable.

The project has strong compiled pages, source cards, traceability sections, and health checks. However, a normal reader does not experience those assets as a coherent answer. The interface still asks the user to trust that the vault did the right thing, instead of showing the answer as a wiki-quality synthesis.

## Root Product Gap

The current pipeline optimizes for "can the system find material and synthesize something?".

The ordinary-user product needs to optimize for:

1. Can a broad question produce a useful starter explanation?
2. Can the user see why the answer is trustworthy?
3. Can the user distinguish source-backed claims from inference?
4. Can the answer point to the best next page or next question?
5. Can repeated tests produce stable, legible, source-aware answers?

Until those are true, more content promotion will have weak user-visible impact.

## P0: Define The Ordinary-User Answer Contract

Every broad or explanatory Ask the vault answer should render the same minimum shape:

1. **Direct answer**
   - 2-4 short paragraphs.
   - Lead with the practical explanation, not a caveat.
   - Avoid one-sentence answers for broad disease prompts.

2. **What this means for a reader**
   - Translate the research finding into a plain-language interpretation.
   - Keep it educational, not veterinary advice.

3. **Evidence ladder**
   - 3-5 bullets.
   - Each bullet must carry one of:
     - `[quoted_fact: src-...]`
     - `[source_supported_conclusion: src-...]`
     - `[llm_inference]`
   - If a bullet is `[llm_inference]`, it must say why the inference is being made.

4. **What we do not know yet**
   - Use this section for gaps, uncertainty, weak evidence, or disease heterogeneity.

5. **Useful next step**
   - Link or name the best next topic page.
   - For broad disease prompts, suggest one natural follow-up question.

The synthesis prompt in `scripts/query.py` currently asks for "Direct answer (one paragraph)". That contract is too small for the ordinary-user surface and should be replaced for broad, unknown, or explain-style prompts.

## P0: Route Broad Questions To Best Answer Surfaces

The current deterministic routing falls back to:

- `topics/{disease}/synthesis-index.md`
- `topics/{disease}/current-state-dashboard.md`
- `topics/{disease}/endpoint-handbook.md`

That is a good start, but broad prompts like `解释CKD` should force a richer starter bundle:

- `topics/{disease}/current-state-dashboard.md`
- `topics/{disease}/synthesis-index.md`
- `topics/{disease}/mechanism-overview.md`
- `topics/{disease}/risk-and-recognition.md`
- `topics/{disease}/endpoint-handbook.md`

The loaded source cards should then support the answer. They should not become invisible implementation details.

Acceptance rule:

> If the user asks a broad disease explanation, the answer must behave like a compact wiki entry, not like a narrow citation lookup.

## P0: Make Trust Visible In The Main Answer

The current low-confidence warning is technically honest but user-hostile. It says the answer is weak without explaining what happened.

Replace the generic warning with a trust block:

- **Confidence:** high / medium / low.
- **Why:** count sourced claims and inference claims.
- **Readings used:** show 3-6 readable source titles, with source IDs secondary.
- **Unsupported areas:** list any major answer parts tagged `[llm_inference]`.

The UI already has provenance badges and a source section concept. The issue is priority and explanation: the ordinary user needs trust cues inside the answer flow, not hidden in sidebars or collapsed panels.

## P0: Acceptance Prompt Set

The first ordinary-user acceptance set should use broad and natural prompts:

1. `解释CKD`
2. `FIP怎么识别`
3. `HCM是什么，为什么危险`
4. `IBD和淋巴瘤怎么区分`
5. `糖尿病猫为什么会缓解`
6. `我的猫肌酐升高，这个库能告诉我什么`

Each prompt passes only if:

- The answer has the ordinary-user answer contract sections.
- The answer is long enough to be useful but still scannable.
- At least three evidence bullets have valid source IDs when the vault has sources loaded.
- Low confidence is explained by claim coverage, not only by a generic warning.
- Source titles or source IDs are visible in the main answer area.
- The answer includes one useful next step or follow-up question.

The checklist for this sample set is now stored at:

- [ordinary-user-acceptance-checklist-20260506](ordinary-user-acceptance-checklist-20260506.md)

## P1: Preserve The Research Layer, But Stop Leading With It

The vault should keep:

- source cards
- traceability tables
- evidence-depth caveats
- health checks
- compiled disease modules
- source-weighting and verification metadata

But the ordinary user should not have to understand those systems before getting value. The app should translate the research layer into a guided answer.

## Stop Rules

Until P0 is done, do not treat these as the main path:

- adding more topic pages as the primary fix
- doing another broad content precision pass
- promoting more extracted facts without changing the answer contract
- writing more Karpathy-alignment memos without tying them to answer behavior
- accepting "loaded many readings" as proof that the user received a good answer

## Implementation Order

1. Add a broad-question answer mode in `scripts/query.py`.
2. Expand broad disease routing to load the compact wiki starter bundle.
3. Change confidence reporting from a generic warning to a visible trust explanation.
4. Ensure sources used are rendered in the main answer area with readable titles.
5. Run the six-prompt ordinary-user acceptance set through the Streamlit UI.
6. Update `DESIGN.md` after the new trust surface is implemented.

## 2026-05-06 Implementation Note

First recovery slice implemented:

- `scripts/query.py` now recognizes broad ordinary-reader prompts such as `解释CKD` and exact disease-name prompts as `overview`.
- `overview` routing now loads the disease starter bundle:
  - `current-state-dashboard.md`
  - `synthesis-index.md`
- The synthesis contract now has an overview answer mode with:
  - direct answer
  - reader meaning
  - key evidence
  - uncertainty
  - useful next step
- `scripts/app.py` now replaces the generic low-confidence warning with a visible trust block that explains claim-tag coverage and readings loaded.
- Source ID parsing now handles both comma-separated and semicolon-separated citation lists.
- The deprecated `st.components.v1.html()` copy button was removed in favor of a Streamlit markdown download action.
- A dedicated ordinary-user acceptance checklist now exists for the 6 broad-reader prompts.
- `scripts/run_acceptance_checklist.py --suite ordinary-user` now generates or executes the 6-prompt suite.
- `scripts/run_acceptance_checklist.py --suite ordinary-user --route-only` now verifies those prompts without an LLM.
- `scripts/health.py` now includes a durable `Ordinary-user acceptance` row so the route-only or live suite stays visible in normal health checks.
- `scripts/run_acceptance_checklist.py` now strips Markdown link syntax inside stored result excerpts, so model-emitted relative links do not create false broken links in `system/health-checks`.
- `scripts/query.py` now compacts topic-page context and source-card context for `overview` questions, and disables figure attachment for overview mode.
- `scripts/query.py` now sanitizes provenance after synthesis: invalid source IDs are removed or downgraded, informal Chinese source brackets containing real `src-*` IDs become machine-readable source tags, and loose `llm_inference` variants are normalized.
- The root `start.md` and `reader-start-here.md` pages now say why this vault is different from Wikipedia.

Live OpenRouter smoke test:

```text
Question: 解释CKD
ROUTER_QTYPE=overview
ROUTER_DISEASE=ckd
FIRST_FAMILY=current-state-dashboard
Loaded: 2 CKD starter pages + preheated source cards
```

Observed improvement:

- The answer changed from a one-sentence explanation to a compact wiki-style starter answer.
- It included direct explanation, reader meaning, key evidence, unknowns, and recommended next readings.
- It cited multiple CKD source IDs in the answer body.

Remaining P0 concern:

- The overview path is materially lighter. Manual live samples after compaction synthesized at about `4025` tokens for `解释CKD`, `2457` tokens for `HCM是什么，为什么危险`, and `3669` tokens for `我的猫肌酐升高，这个库能告诉我什么`.
- A previous full live ordinary-user suite passed on 2026-05-06 before the later compaction/sanitizer changes.
- A post-compaction full live suite on 2026-05-07 reached `5/6` pass-leaning; the single miss was OU4 provenance formatting. After adding sanitizer normalization for informal Chinese source brackets, a targeted OU4 live rerun was blocked by OpenRouter `401 User not found`.
- Therefore the latest durable ordinary-user report is route-only `route_pass`; the full live suite still needs to be rerun after OpenRouter auth is stable.
- `scripts/run_acceptance_checklist.py` now classifies runtime blockers (`backend-auth`, `network`, `rate-limit`) and stops early with `blocked-runtime:*`, so backend failures are not misread as answer-quality failures.

## Success Definition

The project is ordinary-user usable only when a fresh user can open Ask the vault, type a natural disease question, and receive a compact, source-aware wiki answer without needing to inspect markdown files, route maps, source IDs, or debug expanders.

Current validation level:

- query tests: `102 passed | 0 failed`
- markdown links: PASS
- ordinary-user route-only report: [ordinary-user-acceptance-report-20260507](../health-checks/ordinary-user-acceptance-report-20260507.md), status `route_pass`
- health report: [health-report-20260507](../health-checks/health-report-20260507.md), row `Ordinary-user acceptance | PASS`, report status `active`
