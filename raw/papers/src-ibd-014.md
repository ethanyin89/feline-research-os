---
id: src-ibd-014
type: source
title: "Efficacy of a commercial hydrolysate diet in eight cats suffering from inflammatory bowel disease or adverse reaction to food"
source_kind: paper
species: feline
diseases: [IBD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2010
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, diet, translation]
links:
  doi: ""
  url: "https://pubmed.ncbi.nlm.nih.gov/20939411/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The abstract reports that eight of 28 cats with chronic vomiting and or diarrhea were diagnosed with chronic enteropathy.
    - All eight cats underwent a complete diagnostic work-up including endoscopy.
    - The abstract states that a hydrolysed protein diet was used as sole therapy and that clinical signs resolved within 4 to 8 days in all eight cats.
    - The abstract reports weight gain after 2 months and recurrence of signs after challenge with the previous diet, with resolution in seven cats after the test diet was reintroduced.
  source_supported_conclusion:
    - This source anchors the diet side of the early IBD treatment branch.
    - The study supports hydrolysed diet response as a real early treatment anchor, but not one that cleanly separates idiopathic IBD from food-responsive disease.
  llm_inference:
    - This is the cleanest current early treatment anchor in the IBD seed set, but it must stay bounded by mixed-case composition.
---

# One-line Summary

Hydrolysate-diet paper that likely provides the cleanest current practical treatment anchor in the feline IBD seed corpus.

## Why It Matters For IBD

- gives the translation branch at least one direct intervention paper
- helps separate diet response from broader or more speculative immunomodulatory strategies
- now serves as the first practical diet-treatment anchor in the IBD module

## Key Findings

- abstract reports 8 chronic-enteropathy cats treated with hydrolysed diet as sole therapy
- clinical signs resolved within 4 to 8 days in all eight cats
- cats gained weight after 2 months
- challenge with the previous diet caused recurrence, with resolution in seven cats after reintroduction of the test diet

## Diet-Treatment Role

This source is the cleanest current practical treatment anchor in the IBD seed corpus, but its strength depends on keeping the mixed chronic-enteropathy frame visible. Eight of 28 cats with chronic vomiting and/or diarrhea were diagnosed with chronic enteropathy, underwent complete diagnostic workup including endoscopy, and then received a hydrolysed protein diet as sole therapy. Clinical signs resolved within 4 to 8 days in all eight cats, and the challenge/reintroduction pattern supported diet responsiveness in most cats.

For wiki reuse, this card should anchor the early `diet-first` treatment branch. It fits the broad exclusion-first architecture because food-responsive disease can resemble IBD clinically and histologically. A hydrolysed-diet response therefore has two meanings: it can be a treatment response, and it can also keep the workup from prematurely labeling every chronic enteropathy cat as idiopathic IBD.

The claim ceiling is important. This paper does not prove that hydrolysed diet uniquely treats pure idiopathic IBD. It includes chronic enteropathy and adverse reaction to food framing, and its size is only eight treated cats. The safe compiled rule is: hydrolysed diet response is a real early practical anchor, but it should be presented as diet-first chronic-enteropathy management rather than universal IBD-specific efficacy.

The candidate challenge/recurrence table is high value because the re-challenge logic is central. If verified, it should become a visual support for the diet branch.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- eight-cat size and mixed disease framing mean treatment claims will need careful bounding
- do not separate diet response from food-responsive enteropathy ambiguity too aggressively
- do not use this small study as a complete long-term treatment hierarchy

## Image Asset TODO

- figures to capture:
  - hydrolysate diet response summary figure or table
  - diet challenge and recurrence table
  - any diagnostic-workup-to-diet-trial flow figure
- why these matter:
  - this source is the cleanest current diet-first treatment anchor and should preserve its response structure visually
  - challenge-recurrence logic is easy to overclaim if left as prose only
  - if the paper contains a workup-to-diet flow, it would strengthen the treatment hierarchy without outrunning the diagnostic spine

## Open Follow-up Questions

- how were IBD and adverse food reaction separated?
- what endpoints defined efficacy?
- how much follow-up exists beyond the early response and two-month weight gain?
- did any cats need adjunctive medication after diet response?

## Deep Extraction

- [src-ibd-014 deep extraction round 1](../../system/indexes/src-ibd-014-deep-extraction-round1.md)

## Linked Entities

- hydrolysate diet
- food-responsive enteropathy
- treatment response
