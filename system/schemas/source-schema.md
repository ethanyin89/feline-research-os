# Source Schema

Use this frontmatter for every ingested source card.

Important:

- `source_kind` is a file/source-family label, not an authority ranking.
- `evidence_level` is a study/guidance type label, not a substitute for claim-fit judgment.
- Every new source should also be classified using [source hierarchy and claim-fit policy](../indexes/source-hierarchy-and-claim-fit-policy.md).

```yaml
---
id: src-ckd-001
type: source
title: ""
source_kind: paper # paper | regulation | guidance | dataset | image | web
species: feline
diseases: []
models: []
endpoints: []
jurisdictions: []
evidence_level: "" # review | guideline | original-study | case-series | regulation | commentary
year: 2026
status: ingested # inbox | ingested | reviewed | superseded
verification_status: source_checked # title_only | abstract_weighted | source_checked | deep_extracted | audited
decision_grade: no # no | provisional | yes
language_qa_status: not_applicable # unchecked | light_checked | bilingual_checked | not_applicable
tags: []
links:
  doi: ""
  url: ""
  local_assets: []
evidence_policy:
  quoted_fact: []
  source_supported_conclusion: []
  llm_inference: []
---
```

`links.local_assets` should point to files under `raw/images/` when the source has
high-value figures, panels, or image-only tables that matter for later retrieval.

During ingest, do not stop at `source_kind` + `evidence_level`.

The source card body should make clear:

1. what source family this really belongs to
2. what this source most safely controls
3. what this source must not control

If images are not downloaded yet, keep `local_assets: []` and add an `Image Asset TODO`
section in the source card body.

## Required Sections

1. One-line summary
2. Why it matters for CKD
3. Key findings
4. Limits / caveats
5. Open follow-up questions
6. Linked entities
