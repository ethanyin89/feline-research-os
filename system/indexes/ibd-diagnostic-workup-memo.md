# IBD Diagnostic Workup Memo

## Core Takeaway

`feline IBD workup should be modeled as exclusion plus site-aware tissue strategy, not as one flat inflammatory diagnosis`

## Current Workup Architecture

- start from `chronic enteropathy suspicion`, not from assumed idiopathic IBD
- use `clinical activity` to stage burden and response tracking, not to settle disease class
- treat `biopsy and histopathology` as central diagnostic layers
- keep `small-cell lymphoma exclusion` inside the core workup branch from the beginning
- treat `duodenal versus ileal sampling` as a real decision point, not a procedural footnote
- model `histopathology-report structure` as a workflow-normalization layer adjacent to tissue interpretation, not as disease biology

## Practical Sequence Compression

The current evidence supports this ordering:

1. **Clinical suspicion / burden:** use chronic-enteropathy signs and activity indexing to decide that workup and response tracking are needed, not to assign final disease identity.
2. **Imaging pressure:** use ultrasound as a suspicion-shaping layer. Muscularis thickening should move lymphoma higher in the differential; lymphadenopathy mainly confirms abnormal intestinal disease pressure.
3. **Biopsy-site strategy:** decide whether duodenal-only sampling is enough for the question being asked. If the real question is meaningful lymphoma exclusion, ileal sampling cannot be treated as background.
4. **Histology and report structure:** pathology interpretation is central, but report-language stabilization and structured classification are workflow support, not biologic certainty. `src-ibd-009` strengthens this as a pathology-language branch, not as a replacement for tissue review.
5. **Bounded marker support:** tissue markers and noninvasive markers can strengthen or stratify the branch, but they sit below imaging plus biopsy strategy plus integrated pathology.

## Strongest Current Anchors

- [src-ibd-003 deep extraction round 1](src-ibd-003-deep-extraction-round1.md)
- [src-ibd-004 deep extraction round 1](src-ibd-004-deep-extraction-round1.md)
- [src-ibd-015 deep extraction round 1](src-ibd-015-deep-extraction-round1.md)
- [src-ibd-009 deep extraction round 1](src-ibd-009-deep-extraction-round1.md)

## What The Module Can Already Say

- broad review-level framing already supports `diagnosis of exclusion`
- FCEAI gives the module a usable activity and response-tracking layer
- biopsy utility is real, but biopsy-site agreement is poor enough that site choice can change the final lymphoma call
- pathology-report structure now also appears as a real workflow layer adjacent to tissue interpretation
- automated classification of structured histopathology reports should be treated as report-language stabilization, not as proof that inflammatory-versus-neoplastic classification has been biologically solved
- muscularis thickening can raise lymphoma suspicion before tissue is obtained, but it does not replace tissue-centered workup
- Bcl-2 and metabolomics create marker depth, while fecal S100A12 mainly supports abnormal inflammatory disease burden rather than lymphoma separation

## Current Boundaries

- `clinical activity` is not the same thing as etiologic diagnosis
- `duodenal convenience` is not the same thing as diagnostic completeness
- `negative or nonlymphoma tissue from one site` is not the same thing as strong lymphoma exclusion
- pathology-report classification support is not the same thing as biologic certainty
- automated report classification is not the same thing as improved biopsy-site coverage or lymphoma exclusion
- `support marker` is not the same thing as `boundary discriminator`

## Immediate Next Densification Targets

- higher-detail live-animal pathology workflow material if the report-structure branch needs expansion beyond the deep-extracted, non-decision-grade `src-ibd-009` anchor
