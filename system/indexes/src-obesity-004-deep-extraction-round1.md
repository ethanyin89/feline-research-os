---
id: src-obesity-004-deep-extraction-round1
type: system
topic: obesity
question_type: deep-extraction
source_ids: [src-obesity-004]
language: en
last_compiled_at: 2026-05-17
verification_status: deep_extracted
decision_grade: no
owner: codex
status: active
---

# src-obesity-004 Deep Extraction, Round 1

## Source

- Source card: [src-obesity-004](../../raw/papers/src-obesity-004.md)
- Title: `Overweight and obesity in domestic cats: epidemiological risk factors and associated pathologies`
- Official source: Crossref API abstract extraction, 2026-05-17
- DOI: `10.1177/1098612X241285519`
- Journal: Journal of Feline Medicine and Surgery
- Volume: 26, Issue 11
- Year: 2024
- Authors: Claudia Saavedra, Consuelo Pérez, Carlos Oyarzún, Ángelo Torres-Arévalo

## Evidence Boundary

This round uses the full abstract from Crossref API. It is sufficient to promote this source from branch-placement-only to a bounded risk-factor and associated-pathology anchor, but it is not full-text extracted.

## Article Type

This is a **narrative review** analyzing epidemiological variables and diseases associated with overweight and obesity (O&O) in domestic cats. It cites 87 references.

## Reusable Facts

### quoted_fact

- "The domestic cat has evolved in various aspects in its journey from original domestication to the present day."
- "Many domestic cats today lead a sedentary indoor lifestyle with low environmental stimulation."
- "Cats have changed their eating habits, transitioning from being carnivorous hunters to animals that eat commercial processed foods."
- "Eating patterns have also changed since cats no longer need to hunt for food but instead have access to several portions throughout the day."
- "The prevalence of O&O has significantly increased in the global cat population, making them a growing clinical concern for companion animals."
- "O&O contribute to the onset of other pathologies by either increasing susceptibility or creating conditions that allow existing or incipient pathologies to manifest or worsen."

### source_supported_conclusion

- Risk factors divide into extrinsic (lifestyle, diet, feeding patterns) and intrinsic (genetics, sex, breed).
- Associated pathologies include: musculoskeletal tissue changes, insulin resistance, type 2 diabetes, skin disorders, kidney and urinary tract diseases.
- This is a narrative review, not a systematic review or meta-analysis.
- The prevalence statement is qualitative ("significantly increased") without specific numbers in the abstract.

### llm_inference

- This source can anchor the obesity risk-factor architecture page.
- It can anchor the associated-pathology branch linking obesity to diabetes, musculoskeletal, skin, and urinary conditions.
- Full-text access would provide specific prevalence estimates and effect sizes from the 87 cited references.

## Risk Factors Identified

### Extrinsic (Environmental/Lifestyle)

| Factor | Description |
|--------|-------------|
| Sedentary lifestyle | Indoor living with low physical activity |
| Low environmental stimulation | Reduced mental/physical enrichment |
| Commercial processed foods | Shift from hunting/raw to processed diets |
| Feeding pattern change | Multiple portions available vs hunting for food |

### Intrinsic (Animal-Specific)

| Factor | Description |
|--------|-------------|
| Genetics | Genetic predisposition to weight gain |
| Sex | Sex-related metabolic differences |
| Breed | Breed-specific risk profiles |

## Associated Pathologies

| Pathology | Relationship |
|-----------|--------------|
| Musculoskeletal changes | O&O contributes to onset/worsening |
| Insulin resistance | O&O increases susceptibility |
| Type 2 diabetes | O&O contributes to onset/worsening |
| Skin disorders | O&O increases susceptibility |
| Kidney diseases | O&O contributes to onset/worsening |
| Urinary tract diseases | O&O increases susceptibility |

## Use Boundaries

This source can now support:
- Risk-factor architecture (extrinsic vs intrinsic framework)
- Associated-pathology branch visibility
- Qualitative prevalence statements ("growing clinical concern")

This source must NOT yet support:
- Specific prevalence percentages
- Risk-factor ranking by effect size
- Causal claims without mechanistic evidence
- Treatment or management recommendations
- Owner-facing weight-loss protocols

## Open Questions

- What specific prevalence estimates are cited in the full text?
- How are the 87 references distributed across risk factors vs pathologies?
- Does the review evaluate evidence quality for each association?
- Are there breed-specific risk profiles detailed?
