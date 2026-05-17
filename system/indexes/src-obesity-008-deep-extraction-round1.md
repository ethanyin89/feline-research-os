---
id: src-obesity-008-deep-extraction-round1
type: system
topic: obesity
question_type: deep-extraction
source_ids: [src-obesity-008]
language: en
last_compiled_at: 2026-05-17
verification_status: deep_extracted
decision_grade: no
owner: codex
status: active
---

# src-obesity-008 Deep Extraction, Round 1

## Source

- Source card: [src-obesity-008](../../raw/papers/src-obesity-008.md)
- Title: `Insulin Sensitivity Decreases with Obesity, and Lean Cats with Low Insulin Sensitivity are at Greatest Risk of Glucose Intolerance with Weight Gain`
- Official page checked: Sage DOI page, 2026-05-17
- DOI: `10.1053/jfms.2001.0138`

## Evidence Boundary

This round uses the official article page and abstract/body text available through the Sage DOI page. It is enough to promote this source from branch-placement-only to a bounded mechanism anchor, but it is still not a treatment or screening protocol.

## Study Object

The paper tests how marked weight gain changes glucose and insulin metabolism in cats.

The study used 16 research cats. Baseline glucose tolerance and insulin sensitivity were measured before weight gain. Cats were then fed high-energy diets ad libitum for about 10 months, gained substantial weight, and underwent repeated glucose tolerance, insulin sensitivity, and meal-response testing.

## Reusable Facts

### quoted_fact

- The official abstract reports 16 cats and an average weight increase of 44.2% over 10 months.
- The official abstract reports that feline obesity was accompanied by a 52% decrease in tissue sensitivity to insulin and reduced glucose effectiveness.
- The official abstract reports that glucose intolerance and abnormal insulin response occurred in some cats.
- The article reports that cats with lower lean-state insulin sensitivity and glucose effectiveness were at increased risk of impaired glucose tolerance after weight gain.
- The article reports that male cats gained more weight than females and discusses this as one possible contributor to male diabetes risk.

### source_supported_conclusion

- This is now a real obesity-diabetes bridge anchor, not just a title-level signal.
- The safest promotion is mechanism and endpoint placement: weight gain and obesity can reduce insulin sensitivity and glucose effectiveness in cats.
- The source supports keeping obesity upstream of insulin resistance and glucose intolerance inside diabetes-adjacent reasoning.
- The source supports individual-susceptibility framing: obesity does not imply that all obese cats become glucose intolerant.
- The source should strengthen the obesity module's first-owner choice toward `obesity-and-diabetes-bridge`, while still leaving public obesity guidance blocked until more obesity sources are extracted.

### llm_inference

- This source can be used to connect obesity with insulin-resistance burden in feline diabetes pages, provided it is not turned into screening rules or owner-facing weight-loss advice.
- The study's research-cat, induced-weight-gain design should remain visible when reusing its conclusions.
- The male-risk discussion is hypothesis-supporting, not sufficient for a standalone sex-risk rule.

## What To Promote

Promote branch placement and mechanism language:

- obesity has a feline-source mechanism bridge to insulin sensitivity, glucose effectiveness, and glucose tolerance
- the bridge is relevant to diabetes recognition and endpoint planning
- predisposition matters; obesity interacts with baseline metabolic vulnerability

## What Not To Promote

- no exact screening threshold
- no weight-loss prescription
- no universal diabetes-progression claim
- no owner-facing prevention program
- no claim that this single induced-weight-gain study defines the whole obesity module

## Best Write-Back Targets

- [src-obesity-008](../../raw/papers/src-obesity-008.md)
- [obesity source depth map](obesity-source-depth-map.md)
- [obesity current state dashboard](../../topics/obesity/current-state-dashboard.md)
- later, after more extraction: a narrow `obesity-and-diabetes-bridge` topic page

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for mechanism and branch placement; no, for clinical guidance`
- smallest durable home: `source card + depth map + dashboard note`

### Decision

Partial promote.

This source can now carry the first obesity mechanism anchor. The obesity module still should not become a public answer surface until at least the risk/review or prevention anchors are also extracted.
