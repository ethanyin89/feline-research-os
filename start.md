---
id: start
type: index
topic: system
question_type: navigation
language: bilingual
last_compiled_at: 2026-04-22
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Ask First

> **Ask the vault:** What do you want to know about feline CKD, FIP, HCM, IBD, or Diabetes?

The best first move is a bounded question, not a tour of the folder tree.

Examples:

- `CKD 里 phosphorus control 的证据强度如何？`
- `Compare CKD and HCM on endpoint maturity.`
- `FIP 的诊断证据里，哪些 marker 最容易误导？`
- `IBD 和 Diabetes 哪些结论仍然偏 abstract-weighted？`
- `Which disease module is weakest for decision-grade use today?`

Why use this instead of Wikipedia:

- you get a source-aware answer surface, not just a general summary
- you can see which claims are quotes, supported conclusions, or inference
- you can jump from the answer into the next best disease page or claim check

Use the chat UI when an API key is available:

```bash
OPENROUTER_API_KEY=<key> OPENROUTER_MODEL=openai/gpt-4.1-mini python -m streamlit run scripts/app.py
```

Use the CLI when you are already in this folder:

```bash
python3 scripts/query.py "Compare CKD and HCM on endpoint maturity." --backend openrouter
```

Every answer should keep provenance visible:

- `[quoted_fact]` means a direct source-card quote.
- `[source_supported_conclusion]` means a synthesis supported by loaded evidence.
- `[llm_inference]` means reasoning beyond the loaded source surface.

Do not treat `candidate-*` image references as evidence. Verified images are linked from source-card `local_assets`; candidate targets stay in manifests or TODOs until the original article figure/table label is checked.

<details>
<summary>If you want to browse instead of ask</summary>

- [Ask the vault](system/indexes/ask-the-vault.md)
- [Reader start here](system/indexes/reader-start-here.md)
- [ordinary user usage guide](system/indexes/ordinary-user-usage-guide-bilingual.md)
- [compiled pages vs original papers](system/indexes/compiled-vs-source-reading.md)
- [best answer surfaces](system/indexes/best-answer-surfaces.md)

</details>

<details>
<summary>Disease dashboards</summary>

- CKD: [current-state-dashboard](topics/ckd/current-state-dashboard.md)
- CKD bilingual: [current-state-dashboard-bilingual](topics/ckd/current-state-dashboard-bilingual.md)
- FIP: [current-state-dashboard](topics/fip/current-state-dashboard.md)
- HCM: [current-state-dashboard](topics/hcm/current-state-dashboard.md)
- IBD: [current-state-dashboard](topics/ibd/current-state-dashboard.md)
- IBD bilingual: [current-state-dashboard-bilingual](topics/ibd/current-state-dashboard-bilingual.md)
- Diabetes: [current-state-dashboard](topics/diabetes/current-state-dashboard.md)

</details>

<details>
<summary>Maintainer checks</summary>

- Run health: `python3 scripts/health.py`
- Run query tests: `python3 scripts/test_query.py`
- Run acceptance: `python3 scripts/run_acceptance_checklist.py --backend openrouter`
- Latest handoff: [HANDOFF-NEXT-2026-04-22](HANDOFF-NEXT-2026-04-22.md)

</details>
