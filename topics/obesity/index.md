---
id: topic-obesity-index
type: topic
topic: obesity
species: feline
disease: obesity
question_type: overview
source_ids: [src-obesity-001, src-obesity-004, src-obesity-005, src-obesity-008, src-obesity-080, src-obesity-085, src-obesity-088, src-obesity-089, src-obesity-090, src-diabetes-005]
last_compiled_at: 2026-06-11
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
language_qa_notes: "2026-06-11 expanded with weight loss intervention evidence, cancer cachexia boundary, comorbidity links. 4 deep + 5 extracted sources in mechanism layer."
owner: codex
status: active
---

# Feline Obesity Topic Index

## Current Status

This obesity module now has 4 deep-extracted Tier 1 source cards anchoring the 5-branch architecture:
- **src-obesity-001**: broad shell (prevalence 11.5-63%, risk factors, associated conditions, assessment)
- **src-obesity-004**: risk-factor architecture (extrinsic vs intrinsic framework)
- **src-obesity-005**: prevention branch (target population: post-gonadectomy kittens 5-12mo)
- **src-obesity-008**: diabetes-bridge mechanism (insulin sensitivity decline)

The module can now support bounded architecture pages. Tier 2 management context sources remain partial.

## Topic Pages

- [what-is-obesity](./what-is-obesity.md) — plain-language explanation for "what is feline obesity?" queries (bilingual)
- [mechanism-overview](./mechanism-overview.md) — 5-branch architecture handbook
- [risk-and-recognition](./risk-and-recognition.md) — risk factor framework and recognition handbook
- [prevention](./prevention.md) — prevention-over-treatment strategy and target populations
- [diabetes-bridge](./diabetes-bridge.md) — insulin sensitivity mechanism linking obesity to T2D
- [weight-loss-energy-calibration](./weight-loss-energy-calibration.md) — energy requirements and metabolic adaptation
- [weight-loss-energy-calibration-bilingual](./weight-loss-energy-calibration-bilingual.md) — (bilingual)
- [navigation](./navigation.md)
- [current-state-dashboard](./current-state-dashboard.md)

## Source Owners

- [obesity bootstrap source queue](../../system/indexes/obesity-bootstrap-source-queue-20260513.md)
- [obesity source index](../../system/indexes/obesity-source-index.md)
- [obesity source depth map](../../system/indexes/obesity-source-depth-map.md)
- [feline diabetes / obesity intake manifest](../../system/indexes/feline-diabetes-obesity-intake-manifest-20260513.md)
- [feline literature sheet intake workflow](../../system/indexes/feline-literature-sheet-intake-workflow.md)

## Existing Shared Evidence

The obesity module starts with one existing bridge already present in the diabetes module:

- [src-diabetes-005](../../raw/papers/src-diabetes-005.md): obese diabetic cat pathophysiology and management

This source can support diabetes-obesity bridge questions, but it should not be stretched into a full obesity module by itself.

## Next Move

Four architecture pages complete (mechanism-overview, risk-and-recognition, prevention, diabetes-bridge). Next options:
1. Deep-extract Tier 2 management context sources (002, 003, 006, 007, 080)
2. Compile bilingual versions of architecture pages
3. Write assessment-methods page after full-text extraction of body condition methods
