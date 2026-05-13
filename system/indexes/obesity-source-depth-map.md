---
id: obesity-source-depth-map
type: index
topic: obesity
question_type: navigation
language: bilingual
last_compiled_at: 2026-05-13
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Source Depth Map — Obesity

## Use

Use this map to decide which obesity source cards need deep extraction before any obesity topic page becomes an answer surface.

## Depth Definitions

- `partial`: first-pass card exists, but article facts are not fully extracted.
- `title_only`: only title / DOI / bibliographic role has been verified.
- `abstract_weighted`: at least some accessible abstract text has been used, but not full-text extraction.
- `deep_extracted`: structured source worksheet and reusable card facts exist.

## Coverage Summary

| Disease | Source Cards | partial | full | title_only | abstract_weighted | deep_extracted |
|---|---:|---:|---:|---:|---:|---:|
| Obesity | 8 | 8 | 0 | 6 | 2 | 0 |

## Tier 1 — Bootstrap Anchors

| Source ID | Title Short | Current Role | Depth | Verification | Priority | Key Gap |
|---|---|---|---|---|---|---|
| src-obesity-001 | Feline obesity broad review | shell / assessment | partial | title_only | HIGH | needs abstract/full-text extraction before prevalence or assessment claims |
| src-obesity-004 | Domestic cat overweight/obesity risk and pathologies | risk / associated pathologies | partial | title_only | HIGH | needs extraction before risk-factor and pathology ranking |
| src-obesity-005 | Target population and prevention | prevention | partial | abstract_weighted | HIGH | needs full abstract/full-text extraction before prevention claims |
| src-obesity-008 | Insulin sensitivity decreases with obesity | mechanism / diabetes bridge | partial | abstract_weighted | HIGH | needs methods/results extraction before numeric or predictive claims |

## Tier 2 — Management Context

| Source ID | Title Short | Current Role | Depth | Verification | Priority | Key Gap |
|---|---|---|---|---|---|---|
| src-obesity-002 | Canine/feline obesity review | broad management context | partial | title_only | MEDIUM | split canine vs feline claims |
| src-obesity-003 | Canine/Feline obesity management | management | partial | title_only | MEDIUM | split species and evidence strength |
| src-obesity-006 | Management of obesity in cats | feline management | partial | title_only | MEDIUM | extract currentness and evidence basis |
| src-obesity-007 | Environment and behavior modification | behavior / environment branch | partial | title_only | MEDIUM | verify species scope and recommendation basis |

## Immediate Queue

Do not write obesity mechanism, risk, endpoint, translation, or management pages yet.

First deep-extract:

1. `src-obesity-001`
2. `src-obesity-004`
3. `src-obesity-005`
4. `src-obesity-008`

Then decide whether the first compiled obesity page should be:

- risk-and-recognition
- mechanism-overview
- obesity-and-diabetes-bridge
- management-boundary memo

## Maintenance

Update this map after every obesity source-card ingest or deep extraction.
