---
id: topic-fip-synthesis-index
type: topic
topic: fip
species: feline
disease: FIP
question_type: synthesis
source_ids: [src-fip-001, src-fip-002, src-fip-003, src-fip-004, src-fip-005, src-fip-006, src-fip-007, src-fip-008, src-fip-009, src-fip-010, src-fip-011, src-fip-012, src-fip-013, src-fip-014, src-fip-015, src-fip-016, src-fip-017, src-fip-018, src-fip-019, src-fip-020, src-fip-021, src-fip-022, src-fip-023, src-fip-024, src-fip-025, src-fip-026, src-fip-027, src-fip-028, src-fip-029, src-fip-030, src-fip-031, src-fip-032, src-fip-033, src-fip-034, src-fip-035, src-fip-036, src-fip-037, src-fip-038, src-fip-039, src-fip-040, src-fip-041, src-fip-042, src-fip-043, src-fip-044, src-fip-045, src-fip-046, src-fip-047, src-fip-048, src-fip-049, src-reg-004, src-reg-005, src-reg-006, src-reg-014]
last_compiled_at: 2026-06-11
confidence: high
verification_status: compiled
decision_grade: yes
language_qa_status: light_checked
language_qa_notes: "2026-06-11 expanded source set includes 49/49 FIP cards (100% intake complete). Synthesis now encompasses treatment transformation (GS-441524/remdesivir era) + diagnosis/biomarkers + pathogenesis (recombinant emergence). Updated confidence from medium→high due to comprehensive source coverage."
owner: codex
status: active
---

# Feline FIP Synthesis Index

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FS1 | FIP synthesis is organized around mechanism, recognition, diagnostic limits, and antiviral treatment transformation | B | src-fip-001, src-fip-003, src-fip-004, src-fip-005, src-fip-006, src-fip-013, src-fip-016, src-fip-017, src-fip-019, src-fip-024 | compiled branch map |
| FS2 | Modern treatment transformation does not remove diagnostic ambiguity | B | src-fip-003, src-fip-010, src-fip-022, src-fip-023 | no one-test diagnostic claim |
| FS3 | Antiviral evidence should stay branch-separated across experimental foundation, baseline efficacy, package logic, neurologic rescue, and durability | B | src-fip-013, src-fip-016, src-fip-017, src-fip-019, src-fip-024 | no universal efficacy claim |
| FS4 | Regulatory framing exists but product-archetype route selection remains unresolved | C | src-reg-001, src-reg-014 | not decision-grade |

## Quick Helpers

- if you want to trace a claim back down:
  [verify a claim](../../system/indexes/verify-a-claim.md)
- if you want to see real `promote / hold / partial promotion` examples:
  [promotion examples index](../../system/indexes/promotion-examples-index.md)

## One-Sentence Summary

The FIP map is now organizing around four stable branches: `pathobiogenesis and mutation logic`, `risk and clinicopathologic recognition`, `diagnostic limits`, and `antiviral treatment transformation`.

## Current Best Map

- mechanism backbone: systemic-disease emergence from feline coronavirus background
- mechanism branch now also has recombinant-outbreak and direct-transmission pressure, so classical mutation-origin can no longer be treated as the exclusive emergence model
- risk branch: multi-cat / endemic-exposure / population-structure literature
- recognition branch: clinicopathology, effusive versus non-effusive form, neurologic extension
- mutation branch now needs to be read as `origin / systemic-spread correlate / bounded utility / diagnostic limitation`, not as one flat assay story
- diagnostic caution branch: mutation detection is informative but not automatically definitive
- endpoint / diagnostic support now has one concrete numeric boundary: CSF RT-PCR has strong positive support after neurologic/ocular branch shift, but limited overall sensitivity and NPV prevent broad rule-out use
- treatment branch: GS-441524 and remdesivir-era evidence changes the translational landscape, but with a real lower experimental-foundation layer
- regulatory branch now has a first jurisdiction-aware split across China / USA / EU / UK, but still does not support final jurisdiction recommendation or product-archetype route advice
- product-archetype route boundary is now clearer: baseline GS-441524 is the cleanest first stress-test object, while remdesivir package logic and neurologic rescue should stay separate
- U.S. conditional-approval eligibility for baseline GS-441524 is now a live `plausible-to-test` branch, but not an eligibility conclusion or preferred-route recommendation
- U.S. active-control design for baseline GS-441524 is now mapped as a live planning branch, but comparator identity remains unresolved
- U.S. comparator boundary for baseline GS-441524 is now clearer: compounded GS access, remdesivir package logic, neurologic evidence, and historical fatality are not equivalent active comparators
- the antiviral layer is now also clearer as a branch-comparison problem: `experimental foundation`, `baseline efficacy`, `package logic`, `neurologic rescue`, and `durability` are adjacent but not equivalent
- remission durability is now a real post-treatment layer rather than a generic success-story add-on
- broad architectural anchor: diagnosis remains supportive and composite even as treatment has become dramatically more actionable
- risk branch now needs to be read as signalment risk + ecology-aware exposure risk + referral-population enrichment, not one flat epidemiology bucket
- all 24 FIP seed source cards are now explicit full-depth cards; the next source work is precision, not generic thickening

## New Anchor

- [src-fip-003 deep extraction round 1](../../system/indexes/src-fip-003-deep-extraction-round1.md)
- [src-fip-004 deep extraction round 1](../../system/indexes/src-fip-004-deep-extraction-round1.md)
- [src-fip-005 deep extraction round 1](../../system/indexes/src-fip-005-deep-extraction-round1.md)
- [src-fip-006 deep extraction round 1](../../system/indexes/src-fip-006-deep-extraction-round1.md)
- [src-fip-013 deep extraction round 1](../../system/indexes/src-fip-013-deep-extraction-round1.md)
- [src-fip-014 deep extraction round 1](../../system/indexes/src-fip-014-deep-extraction-round1.md)
- [src-fip-017 deep extraction round 1](../../system/indexes/src-fip-017-deep-extraction-round1.md)
- [src-fip-016 deep extraction round 1](../../system/indexes/src-fip-016-deep-extraction-round1.md)
- [src-fip-022 deep extraction round 1](../../system/indexes/src-fip-022-deep-extraction-round1.md)
- [src-fip-023 deep extraction round 1](../../system/indexes/src-fip-023-deep-extraction-round1.md)

This worksheet now stabilizes one important rule for the whole module:

`modern treatment transformation does not remove diagnostic ambiguity`

The second worksheet now stabilizes a second rule:

`the baseline GS-441524 treatment anchor is real, but it is not universal across all FIP forms`

The third worksheet now stabilizes a third rule:

`mutation-origin belongs to mechanism first, not to diagnostic certainty first`

The fourth worksheet now stabilizes a fourth rule:

`single-drug baseline efficacy and real-world treatment-package logic are not the same layer`

The fifth worksheet now stabilizes a fifth rule:

`neurologic rescue is not just “more of the same treatment”`

The sixth worksheet now stabilizes a sixth rule:

`experimental antiviral foundation is not the same thing as natural-disease baseline efficacy`

The seventh worksheet now stabilizes a seventh rule:

`positive mutation utility must stay bounded by the wider diagnostic architecture`

The eighth worksheet now stabilizes an eighth rule:

`CSF viral detection is a neurologic-extension support test, not a general-workup leader`

The endpoint boundary sync now stabilizes a seventeenth rule:

`CSF performance numbers sharpen the neurologic branch, but they do not create a cross-assay leaderboard for FIP diagnosis`

The regulatory sync now stabilizes an eighteenth rule:

`jurisdiction-aware framing exists, but product-archetype route selection is still the next unresolved regulatory layer`

The product-archetype route memo now stabilizes a nineteenth rule:

`baseline GS-441524 is the first regulatory stress-test object, not the same object as remdesivir package logic or neurologic rescue`

The baseline GS U.S. eligibility memo now stabilizes a twentieth rule:

`plausible-to-test U.S. conditional approval is not the same thing as FDA eligibility or route preference`

The baseline GS U.S. active-control design memo now stabilizes a twenty-first rule:

`active-control design mapping is not the same thing as a chosen comparator or accepted protocol`

The baseline GS U.S. comparator boundary memo now stabilizes a twenty-second rule:

`compounded GS access is not the same thing as FDA-approved active-comparator status`

The ninth worksheet now stabilizes a ninth rule:

`post-treatment durability is not the same thing as whole-branch cure-rate proof`

The tenth worksheet now stabilizes a tenth rule:

`gut competence and systemic disease competence are not the same thing`

The eleventh worksheet now stabilizes an eleventh rule:

`recombinant outbreak logic prevents exclusive reliance on one emergence route`

The twelfth worksheet now stabilizes a twelfth rule:

`risk context should raise suspicion earlier, not settle diagnosis`

The thirteenth worksheet now stabilizes a thirteenth rule:

`clinicopathology should lead suspicion-pattern recognition before bounded molecular strengthening`

The compiled bridge memo now stabilizes a fourteenth rule:

`mechanism should constrain diagnostic interpretation, not create diagnostic certainty`

The new antiviral-branch comparison memo now stabilizes a fifteenth rule:

`experimental foundation, baseline efficacy, package logic, neurologic rescue, and durability should not be collapsed into one antiviral success sentence`

The new neurologic-rescue boundary memo now stabilizes a sixteenth rule:

`neurologic rescue should be read as treatment-category shift, not intensified ordinary baseline treatment`

## What This Module Most Needs Next

1. treat dashboard / synthesis / unresolved state-sync as promoted, and shift the next batch to full-text / official-source / image-table precision where branch order or output claims require it
2. keep endpoint/diagnostic architecture dense without collapsing it into one-test language or one cross-assay leaderboard
3. keep mechanism and diagnosis explicitly bridged without letting one collapse into the other
4. keep disease-form architecture explicit so wet, dry, and neurologic branches do not collapse into one severity story
5. sharpen product-archetype regulatory route logic without treating the first jurisdiction split, baseline GS stress-test status, U.S. plausible-to-test result, active-control design map, or comparator boundary memo as final route advice
6. keep bilingual rollout narrow and only expand it where cross-language reuse pressure is real

## Source-Card Depth State

- FIP source cards: `24/24` explicit `full`
- FIP round-1 worksheets: `24/24`
- card-level map: [FIP source depth map](../../system/indexes/fip-source-depth-map.md)
- remaining source-side work: non-CSF assay performance details, mutation sample-context specifics, staging/table verification, treatment label/dose precision, and official regulatory current-record checks
