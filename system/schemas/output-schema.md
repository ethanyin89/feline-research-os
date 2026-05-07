# Output Schema

Use this frontmatter for briefings, dossiers, and slides source files.

```yaml
---
id: out-ckd-briefing-20260408
type: output
output_kind: briefing # briefing | dossier | slides | figure | qa
language: zh # zh | en | bilingual
topic: ckd
question: ""
source_ids: []
generated_at: 2026-04-08
verification_status: compiled # compiled | audited
decision_grade: no # no | provisional | yes
language_qa_status: unchecked # unchecked | light_checked | bilingual_checked | not_applicable
owner: ""
status: draft # draft | reviewed | archived
evidence_policy:
  quoted_fact: []
  source_supported_conclusion: []
  llm_inference: []
---
```

## Required Sections

1. User question
2. Executive answer
3. Evidence-backed points
4. Uncertainty / limits
5. Suggested write-back targets
6. Promotion judgment

Use this short template when filling section 6:

- [write-back promotion template](../indexes/writeback-promotion-template.md)
