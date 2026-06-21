---
id: src-fip-011
type: source
title: "Serologic Studies of Naturally Occurring Feline Infectious Peritonitis"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 1976
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, serology, endpoint, diagnosis]
links:
  doi: "10.2460/ajvr.1976.37.12.1449"
  url: "https://doi.org/10.2460/ajvr.1976.37.12.1449"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source explicitly studies serology in naturally occurring FIP.
  source_supported_conclusion:
    - This source belongs in the older serologic-support branch rather than a modern definitive endpoint branch.
    - This paper is best used as historical laboratory-support context beneath current clinicopathology, acute-phase, mutation, and CSF support branches.
  llm_inference:
    - This paper may be useful mainly as historical context for why serology alone should not dominate the modern workup.
    - This source may help make the endpoint branch look less abruptly modern without changing current operational rank order.
  # V2 enhanced fields
  study_design: "原始研究，研究自然发生 FIP 的血清学（1976 年）"
  core_argument: "血清学是 FIP 实验室支持的历史方法——但冠状病毒暴露可产生血清学信号，而 FIP 疾病需要更特异的临床病理解释"
  implicit_premise: "假设历史文献有助于理解现代复合诊断的演变；假设单一标志物诊断是有风险的捷径"
  evidence_boundary: "历史血清学，现代操作价值有限；不能直接推断抗体滴度解释规则"
---

# One-line Summary

Older serology paper that likely serves as historical context for the laboratory-support branch in FIP.

## Why It Matters For FIP

- helps show that supportive laboratory approaches long predate current mutation-based workup
- may sharpen why modern diagnostic architecture stayed composite
- now has a round-1 deep extraction worksheet that keeps it in a bounded historical-serology lane

## Key Findings

- title directly frames serologic studies in natural disease
- likely relevant to endpoint history more than modern standalone certainty
- should now be treated as historical laboratory-support context rather than a lead endpoint anchor

## Historical-Serology Role

This source should be used as the historical serology anchor in the FIP endpoint branch. It matters because serology was part of FIP reasoning long before modern mutation assays, CSF viral detection, or GS-era treatment monitoring. The source is about naturally occurring FIP, which makes it more relevant than a purely experimental serology note, but its age and method context keep it below modern operational endpoints.

The main wiki lesson is not that serology should lead diagnosis. The lesson is that FIP has long created an exposure-versus-disease problem. Coronavirus exposure can produce serologic signals, but FIP disease requires a more specific clinical and pathobiologic interpretation. That is why the modern workup remains composite: risk context, clinicopathology, disease form, effusion or CSF support, mutation evidence, and treatment context all have to be held in relation.

In a Karpathy-style endpoint handbook, this card should appear in a `historical laboratory support` row. It can explain why older serologic approaches were attractive and why they did not become a simple certainty engine. The source should also help the reader understand why later papers on acute phase proteins, immunoglobulins, spike mutations, and CSF detection are not isolated inventions; they are attempts to solve a long-standing diagnostic ambiguity.

The claim boundary is strict. Without full-text extraction, this card should not provide performance claims, modern test ranking, or specific serologic interpretation rules. Its reusable value is architectural and historical: it keeps the endpoint map temporally honest while reinforcing that single-marker diagnosis is a risky shortcut in FIP.

This card should be cross-linked to `src-fip-002` because both belong to supportive laboratory reasoning, but they should remain distinct. Serology speaks to immune recognition or exposure history; acute phase and immunoglobulin patterns speak more broadly to inflammatory and immune-state context. Neither source should replace disease-form recognition, but both explain why a workup may include more than imaging, effusion analysis, and molecular testing.

The source is therefore useful for teaching epistemic humility. A natural-disease serology paper from 1976 can be historically important while having limited direct operational authority today. That distinction is exactly the kind of boundary a wiki needs to encode explicitly.

## Limits / Caveats

- current card is title-led ingest, not full-text reviewed
- older serologic methods may have limited direct modern operational value
- its best role is endpoint-history clarification, not current diagnostic leadership
- do not merge old serology with modern mutation testing as if both had the same diagnostic meaning
- do not infer antibody-titer interpretation rules until the full text is reviewed

## Open Follow-up Questions

- what role did serology actually play in distinguishing FIP from coronavirus exposure?
- does this source mostly matter as historical caution?
- which assays were used, and are they comparable to modern coronavirus antibody testing?
- should serology be represented as endpoint history, active support, or both?

## Linked Entities

- serology
- diagnosis
- laboratory support

## Deep Extraction

- [src-fip-011 deep extraction round 1](../../system/indexes/src-fip-011-deep-extraction-round1.md)
