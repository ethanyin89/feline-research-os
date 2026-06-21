---
id: src-fip-023
type: source
title: "Detection of feline coronavirus in cerebrospinal fluid for diagnosis of feline infectious peritonitis in cats with and without neurological signs"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2015
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, diagnosis, neurologic, csf]
links:
  doi: ""
  url: "https://journals.sagepub.com/doi/10.1177/1098612X15574757"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source explicitly studies detection of feline coronavirus in cerebrospinal fluid for diagnosis of FIP in cats with and without neurological signs.
    - The abstract reports a specificity of 100%, sensitivity of 42.1%, PPV of 100%, and NPV of 57.7% for CSF real-time RT-PCR in diagnosing FIP.
    - The abstract reports sensitivity of 85.7% in cats with neurological and/or ocular signs.
  source_supported_conclusion:
    - This source belongs in the neurologic diagnostic-extension branch of the FIP workup.
    - This source supports CSF viral detection as a high-specificity specialized tool rather than a general FIP workup leader.
  llm_inference:
    - This paper is likely one of the most important supports for treating neurologic FIP workup as a separate layer rather than a minor variation.
    - The paper is strongest when used to justify branch shift into CNS-aware workup, not one-test certainty.
  # V2 enhanced fields
  study_design: "原始研究，检测脑脊液中猫冠状病毒用于有无神经系统症状猫的 FIP 诊断"
  core_argument: "CSF 实时 RT-PCR 是高特异性专业化工具（特异性 100%，PPV 100%）但敏感性有限（42.1%）——在有神经和/或眼部症状猫中敏感性升至 85.7%"
  implicit_premise: "假设诊断工具性能因呈现亚组而异；假设 CSF 检测属于神经/眼科专业化分支而非通用 FIP 筛查"
  unexpected_finding: "同一检测可以作为广泛排除工具较弱而作为专业化支持工具较强——这表明诊断性能必须按亚组呈现"
  title_gap: "标题说 CSF 检测用于 FIP 诊断，但真正发现是情境依赖性能：总体敏感性仅 42.1%（不能广泛排除），但神经/眼部猫中升至 85.7%——同一检测在不同亚组中有不同价值"
  evidence_boundary: "总体 NPV 仅 57.7%，阴性 CSF 结果不能广泛排除 FIP；85.7% 敏感性仅限于神经和/或眼部情境"
---

# One-line Summary

CSF-detection paper that anchors the neurologic diagnostic-extension branch in FIP.

## Why It Matters For FIP

- gives the module a CNS-specific diagnostic branch
- supports keeping neurologic workup separate from general FIP suspicion logic
- now serves as the first deep-extracted CSF diagnostic anchor in the FIP module

## Key Findings

- abstract reports specificity of 100% and PPV of 100%
- abstract reports overall sensitivity of 42.1% and NPV of 57.7%
- abstract reports sensitivity of 85.7% in cats with neurological and/or ocular signs
- best interpreted as a subgroup-sensitive support test rather than a generic FIP diagnostic shortcut

## Neurologic-Diagnostic Role

This paper anchors the CNS-aware diagnostic extension branch in FIP. It should not be treated as an ordinary workup-leader paper just because the specificity and PPV are strong. Its real contribution is branch-sensitive interpretation: the usefulness of CSF real-time RT-PCR changes depending on whether neurologic or ocular disease is part of the presentation.

The abstract-level metrics make the placement clear. Overall specificity and PPV were reported as 100%, which means a positive result can strongly support FIP in the right clinical context. But overall sensitivity was 42.1% and NPV was 57.7%, so a negative CSF result cannot broadly rule out FIP. In cats with neurological and/or ocular signs, sensitivity rose to 85.7%, which is why this paper belongs in a specialized neurologic/ocular branch rather than in a generic FIP diagnostic shortcut.

For wiki reuse, this source should sit below clinicopathology-led suspicion and beside mutation-testing support. It is not competing with risk context or routine clinicopathology. It becomes important after the case has shifted toward CNS or ocular involvement. That branch shift should be explicit in the endpoint handbook because readers can easily misread high specificity as universal readiness.

The paper also provides a model for how to write all FIP diagnostic sources: do not summarize a test with one global adjective. Preserve specificity, sensitivity, PPV, NPV, subgroup context, and placement in the diagnostic sequence. `src-fip-023` is a high-value source precisely because it shows that the same assay can be weak as a broad rule-out tool and strong as a specialized support tool.

The candidate image assets should remain high priority. A performance table and a neurologic-versus-general workup branch figure would make the subgroup-sensitive logic much harder to overread. Until those visuals are verified, the prose card should keep the numbers attached to their context every time.

## Limits / Caveats

- current card is deep-extracted at worksheet level, but still not full-text reviewed
- overall sensitivity remains too limited for broad rule-out or first-line leadership
- subgroup strength should not be generalized into ordinary FIP workup
- do not treat a negative CSF result as a broad exclusion of FIP
- do not detach the 85.7% sensitivity figure from neurologic and/or ocular context

## Image Asset TODO

- figures to capture:
  - CSF RT-PCR performance table
  - subgroup diagnostic-yield figure for neurologic and/or ocular presentations
  - any workup branch diagram that shows where CSF testing sits
- why these matter:
  - this source is central to the neurologic diagnostic-extension branch and should preserve its subgroup-sensitive logic clearly
  - performance metrics are easier to misread when collapsed into prose
  - if a branch figure exists, it would help keep CSF testing in the specialized layer instead of letting it drift into generic workup language

## Open Follow-up Questions

- how should CSF RT-PCR be placed relative to clinicopathologic suspicion and mutation-based support?
- how often does neurologic or ocular subgroup framing change actual diagnostic yield in practice?

## Deep Extraction

- [src-fip-023 deep extraction round 1](../../system/indexes/src-fip-023-deep-extraction-round1.md)

## Linked Entities

- cerebrospinal fluid
- neurologic FIP
- diagnosis
