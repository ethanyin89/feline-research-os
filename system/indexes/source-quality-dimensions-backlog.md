---
id: source-quality-dimensions-backlog
type: system
topic: meta
status: backlog
created_at: 2026-06-05
owner: claude
---

# Source Quality Dimensions — Backlog

Not on main workflow. Parking for future consideration.

## Altmetric Attention Score

Noticed during cancer extraction work. Altmetric measures online attention to research:
- Social media mentions
- News coverage
- Blog citations
- Policy documents
- Wikipedia citations

Potential use: complement citation count with attention/impact score for prioritizing high-value sources.

Reference: https://www.altmetric.com/

## Source Type Taxonomy (Previously Discussed)

Dimensions for classifying reference materials:

| Type | Description | Evidence Weight |
|------|-------------|-----------------|
| Review | Synthesis of existing literature | Secondary |
| Original Study | Primary research with data | Primary |
| Guideline | Consensus recommendations | High (for practice) |
| Product Spec | Manufacturer documentation | Commercial context |
| Marketing | Promotional materials | Low (bias) |
| Regulatory | Government/agency documents | High (for compliance) |
| Internal Doc | Unpublished working documents | Context only |

## Future Integration Ideas

1. Add `altmetric_score` field to source card frontmatter
2. Use Altmetric API to auto-populate scores
3. Weight extraction priority by citation + altmetric combo
4. Distinguish evidence types in Key-Claim Traceability tables

## Status

Parked. Revisit when:
- Cancer module reaches 80%+ deep extraction
- Need to prioritize among many equal-quality sources
- Building automated intake pipeline
