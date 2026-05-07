---
id: src-ibd-022
type: source
title: "Characterization of intestinal fibrosis in cats with chronic inflammatory enteropathy"
source_kind: paper
species: feline
diseases: [IBD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2023
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, fibrosis, chronic-enteropathy]
links:
  doi: "10.1111/jvim.16688"
  url: "https://academic.oup.com/jvim/article/37/3/936/8447850"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The abstract states that intestinal fibrosis is commonly identified on histopathology of intestinal biopsy specimens from cats with chronic inflammatory enteropathy and that its clinical relevance is unknown.
    - The study included 65 client-owned cats diagnosed with chronic inflammatory enteropathy.
    - The abstract reports that histologic and immunohistochemical evidence of intestinal fibrosis was found in 38.5% to 100% of duodenal biopsy specimens and 65.2% to 100% of colonic biopsy specimens depending on the detection method.
    - The abstract reports that cats with intestinal fibrosis had significantly lower body weight and serum albumin concentration than cats without intestinal fibrosis.
  source_supported_conclusion:
    - This source anchors the fibrosis and chronicity branch of the IBD module.
    - The study supports intestinal fibrosis as a real burden-associated chronicity layer, not as a minor incidental pathology note.
  llm_inference:
    - This was the correct next deep extraction because it gives the module a structural chronicity branch above single-marker stories.
---

# One-line Summary

Fibrosis paper that likely upgrades chronicity and remodeling from a side note into a real branch of the feline IBD module.

## Why It Matters For IBD

- gives the module a chronicity and tissue-remodeling axis
- may help connect pathology burden with long-term disease architecture
- now serves as the first fibrosis / chronicity anchor in the IBD module

## Key Findings

- abstract includes 65 cats with chronic inflammatory enteropathy
- abstract reports high prevalence of intestinal fibrosis depending on whether histology, Masson's trichrome, vimentin, or collagen I labeling was used
- abstract reports lower body weight and lower serum albumin in cats with intestinal fibrosis
- abstract conclusion states that intestinal fibrosis should be considered an important part of histopathologic assessment in feline chronic inflammatory enteropathy

## Fibrosis / Chronicity Role

This paper upgrades fibrosis from a side observation into a named chronicity-and-burden branch. The study included 65 client-owned cats diagnosed with chronic inflammatory enteropathy, and the abstract reports intestinal fibrosis in a large proportion of biopsy specimens depending on detection method. That method dependence is itself important: fibrosis visibility changes when ordinary histology is compared with Masson's trichrome, vimentin, or collagen I labeling.

The burden signal makes the source more than a pathology description. Cats with intestinal fibrosis had significantly lower body weight and lower serum albumin concentration than cats without fibrosis. The wiki should therefore place fibrosis beside chronic disease burden and tissue remodeling, not merely in a microscopic-features footnote.

This source should connect mechanism, pathology, and endpoint thinking. FCEAI tracks disease activity; biopsy-site sources address lymphoma exclusion; this fibrosis paper asks whether chronic inflammatory enteropathy is also leaving structural tissue consequences. That distinction matters because activity, diagnosis, and remodeling may move together but are not identical.

The claim ceiling is treatment readiness. The paper supports fibrosis as an important histopathologic assessment layer, but it does not establish a feline antifibrotic intervention, a clean prognostic score, or a simple subtype separator. The correct compiled statement is that fibrosis deserves explicit modeling inside chronic enteropathy architecture and may correlate with burden markers such as albumin and body weight.

Image recovery is high value here. A detection-method table or histology/immunohistochemistry panel would prevent the wiki from flattening a method-sensitive finding into one prevalence number.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- fibrosis presence is not automatically the same thing as intervention target readiness
- method-dependent detection means one simple prevalence number may be misleading
- do not treat fibrosis as a proven disease-class separator without stronger evidence

## Image Asset TODO

- figures to capture:
  - fibrosis detection-method comparison table
  - fibrosis burden versus body weight or albumin figure
  - any histology or immunohistochemistry panel showing remodeling
- why these matter:
  - this paper upgrades chronicity from a background note into a real branch and should preserve that visually
  - method-dependent fibrosis detection is exactly the kind of structure that gets lost in text compression
  - a histology or immunohistochemistry panel would give the fibrosis memo a non-prose anchor

## Open Follow-up Questions

- how common and how severe is fibrosis in these cats?
- does fibrosis help separate chronic enteropathy subtypes or mainly indicate burden?
- how do detection methods change the apparent fibrosis burden?
- should fibrosis become a separate histopathology subsection in the endpoint handbook?

## Deep Extraction

- [src-ibd-022 deep extraction round 1](../../system/indexes/src-ibd-022-deep-extraction-round1.md)

## Linked Entities

- intestinal fibrosis
- chronic inflammatory enteropathy
- tissue remodeling
