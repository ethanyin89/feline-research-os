# Feline Research OS

Internal Obsidian-based research operating system for:

- feline mechanism research
- disease models
- translational evaluation
- regulatory path analysis

Current scope:

- diseases: `CKD`, `FIP`, `HCM`, `IBD`, `Diabetes`
- workflow: ingest -> compile -> ask -> write-back -> health check
- output formats: briefing, dossier, slides
- evidence rule: no fake data; unverified image references stay behind the `candidate-*` gate

## Quick Start (日常操作)

打开 terminal 后：

```bash
cd /Users/jiawei/Desktop/insclaude/feline-research-os
source .venv/bin/activate
OPENROUTER_API_KEY='your-key' scripts/run_test_page.sh
```

更多日常操作路径见 [memory/project/GBRAIN_STATUS.md](memory/project/GBRAIN_STATUS.md)

---

## Ask the Vault (Chat UI)

**Requires:** Python 3.9+

The fastest way in. Type a question, get a sourced answer with provenance tags.

Cost rule: ordinary coding, content work, documentation, and review should use
Claude/ChatGPT subscription products. Do not connect real paid APIs unless you are
running the real Streamlit page or live acceptance path. For OpenRouter live runs,
set the OpenRouter dashboard limit to `$1/day` and set
`OPENROUTER_DAILY_BUDGET_USD=1.00` or lower in this project environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env  # then fill in your API key
```

**Option A — Anthropic API**
```bash
ANTHROPIC_API_KEY=<key> python -m streamlit run scripts/app.py
```

**Option B — OpenRouter**
```bash
OPENROUTER_API_KEY=<key> scripts/run_test_page.sh
```

Preflight the OpenRouter config without making an API call:

```bash
OPENROUTER_API_KEY=<key> OPENROUTER_DAILY_BUDGET_USD=1.00 python scripts/check_openrouter_budget_guard.py
```

For Streamlit Cloud or any hosted Streamlit deploy, put the same keys in
Streamlit secrets instead of relying on shell environment variables:

```toml
OPENROUTER_API_KEY = "sk-or-..."
OPENROUTER_DAILY_BUDGET_USD = "1.00"
OPENROUTER_MODEL = "openai/gpt-4.1-mini"
```

The app mirrors these secrets into the process environment at startup so the
same OpenRouter budget guard is enforced locally and in hosted Streamlit.

**Option C — Ollama (local, hidden by default)**
```bash
brew install ollama
ollama pull qwen2.5:14b   # one-time, ~9 GB
ollama serve &
ENABLE_OLLAMA=true python -m streamlit run scripts/app.py
# sidebar → switch to "Ollama (local)"
# optional: --ollama-model llama3.3 to override the default model
```

All three open `localhost:8501`. The Streamlit UI defaults to **Vault Search (free)**, which searches local source cards and topic pages without calling an API. Switch to Anthropic, OpenRouter, or Ollama only when you need generated cross-source synthesis. Ollama remains hidden in the UI unless `ENABLE_OLLAMA=true` is set.

When a paid API engine is selected, the app requires the sidebar checkbox **Allow paid API synthesis for this session** before it will send a question. This prevents stale browser state such as `?backend=openrouter` from silently spending tokens.

Answers include provenance badges: green `[quoted_fact]` marks direct quotes from source cards, amber `[source_supported_conclusion]` marks inferences the loaded evidence supports, and gray `[llm_inference]` marks reasoning beyond the loaded sources. The sidebar shows which files were loaded and the confidence level.

Each answer also exposes a collapsed Research trace showing how the vault interpreted the question, which local surfaces it searched, which source cards it loaded, and what evidence was excluded or only used as context. Treat the trace as an audit trail, not as additional evidence. In free local-search mode the trace should show `api_calls=0`.

Do not treat `candidate-*` image references as evidence. The query layer filters them out until a human has checked the article figure/table label and placed a real non-candidate file on disk.

CLI alternative (no browser):
```bash
python3 scripts/query.py "CKD 的 TGF-β 机制是什么" --backend ollama
python3 scripts/query.py "CKD 的 TGF-β 机制是什么" --backend ollama --ollama-model llama3.3
python3 scripts/query.py "What endpoints are most usable for CKD?" --backend anthropic
python3 scripts/query.py "Compare CKD and HCM on endpoint maturity." --backend openrouter
python3 scripts/query.py "phosphorus control evidence" --save-to-inbox  # saves to inbox/ for review
python3 scripts/run_acceptance_checklist.py --template-only
python3 scripts/run_acceptance_checklist.py --backend openrouter
bash scripts/run_day1_acceptance.sh
```

`run_acceptance_checklist.py` preflights remote backends. If the required key is
missing, it writes a blocked report instead of marking the checklist executed.

## Search the Vault

Full-text search across all .md files. Works standalone or as a pre-filter inside query.py.

```bash
python3 scripts/search.py "phosphorus binder"                    # search everything
python3 scripts/search.py "proteinuria.*treatment" --scope raw   # regex, raw/ only
python3 scripts/search.py "SDMA" --scope topics --limit 5        # top 5 in topics/
python3 scripts/search.py "fibrosis" --llm-format                # compact output for LLM context
```

When `query.py` runs, it automatically uses `search.py` as a pre-heat step: after routing the question, it searches for relevant source cards and loads the top matches into the synthesis context.

## Health Check

Run the aggregate health command before handoff or after a content batch:

```bash
python3 scripts/health.py
```

It runs markdown link checks, query tests, source-id inventory, source-card depth and `verification_status` counts, required source-card field checks, source state consistency checks, source DOI/URL proof, machine-readable source `evidence_policy` checks, source `quoted_fact` discipline checks, reader `quoted_fact` discipline checks, recursive topic/output `source_ids` validation, thin-source usage reporting for `abstract_weighted` / `title_only` sources, thin-source evidence-depth caveat checks, title-only caveat checks, key-claim traceability checks, quantified-claim traceability checks, high-visibility language QA checks, decision-grade gating, candidate-image gate status, inbox backlog, acceptance-report status, compile-trigger status, and API-key presence. The report is written to `system/health-checks/health-report-YYYYMMDD.md`.

## Read Without Chat

If you want to browse the vault like a normal reader instead of starting in the chat UI:

1. Open this folder in Obsidian
2. Start with [Ask first](start.md)
3. Open [Reader start here](system/indexes/reader-start-here.md) only if you want a folder-style route

## Start Here

If you are opening this vault as a fresh ordinary reader, start with exactly one page:

- [Ask first](start.md)

<details>
<summary>Secondary reader paths</summary>

- [Reader start here](system/indexes/reader-start-here.md)
- [ordinary user usage guide](system/indexes/ordinary-user-usage-guide-bilingual.md)
- [Ask the vault](system/indexes/ask-the-vault.md)
- [compiled pages vs original papers](system/indexes/compiled-vs-source-reading.md)

</details>

<details>
<summary>For Maintainers</summary>

- Handoff stack for model takeover:
  - [Root handoff](HANDOFF.md)
  - [Usage-limit emergency handoff, 2026-04-17](system/indexes/usage-limit-emergency-handoff-20260417.md)
  - [Model continuity handoff, 2026-04-17](system/indexes/model-continuity-handoff-20260417.md)
  - [Final integrator closeout checklist, 2026-04-18](system/indexes/final-integrator-closeout-checklist-20260418.md)
  - [Vision-integrated query layer handoff, 2026-04-18](system/indexes/vision-query-layer-handoff-20260418.md)
- [Multi-disease LLM wiki status audit, 2026-04-10](system/indexes/multi-disease-llm-wiki-status-audit-20260410.md)
- [Disease module maturity ladder](system/indexes/disease-module-maturity-ladder.md)
- [Ask the vault acceptance checklist, 2026-04-16](system/indexes/ask-the-vault-acceptance-checklist-20260416.md)
- [Ask the vault priority answer surfaces, 2026-04-16](system/indexes/ask-the-vault-priority-answer-surfaces-20260416.md)
- [Ask the vault router hit map, 2026-04-16](system/indexes/ask-the-vault-router-hit-map-20260416.md)
- [Ask the vault acceptance fault tree, 2026-04-16](system/indexes/ask-the-vault-acceptance-fault-tree-20260416.md)
- [Ask the vault day-1 runbook, 2026-04-16](system/indexes/ask-the-vault-day-1-runbook-20260416.md)
- [Image ingest protocol, 2026-04-16](system/indexes/image-ingest-protocol-20260416.md)
- [Cross-disease densification queue](system/indexes/cross-disease-densification-queue.md)

</details>

## Working Rules

1. `raw/` stores original material only.
2. Every ingested source must get a source card before it is cited in a topic page.
3. Topic pages summarize evidence, they do not replace evidence.
4. Every output must distinguish:
   - `quoted_fact`
   - `source_supported_conclusion`
   - `llm_inference`
5. High-value outputs may be promoted back into topic pages only after review.
6. V1 structure should be maintained by one primary operator.

## How Bilingual Works

This vault supports bilingual compiled content, but it does not bilingualize the raw layer.

- `raw/` keeps original language only
- English source stays English
- Chinese source stays Chinese
- source cards are not translated by default just to make the vault look uniform
- bilingual support belongs mainly in compiled pages and outputs

Current high-value bilingual assets include:

- [CKD current state dashboard bilingual](topics/ckd/current-state-dashboard-bilingual.md)
- [CKD synthesis index bilingual](topics/ckd/synthesis-index-bilingual.md)
- [core paper synthesis memo bilingual](system/indexes/core-paper-synthesis-memo-ckd-round1-bilingual.md)
- [briefing en](outputs/briefings/out-ckd-briefing-20260408-round1-en.md)
- [dossier en](outputs/dossiers/out-ckd-dossier-20260408-v1-en.md)

Detailed policy:

- [bilingual content policy](system/prompts/bilingual-content-policy.md)

## Directory Guide

```text
inbox/                 temporary drop zone
raw/                   original files and clipped material
entities/              stable knowledge objects
topics/                compiled topical views
outputs/               generated briefings, dossiers, slides, figures
system/schemas/        frontmatter contracts
system/templates/      markdown templates
system/prompts/        reusable prompts
system/indexes/        summary indexes
system/health-checks/  integrity checks and reports
```

Current entity families include diseases, endpoints, mechanisms, regulations, and lightweight symptom cards when recognition logic needs explicit anchors.
