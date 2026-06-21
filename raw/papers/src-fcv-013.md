---
id: src-fcv-013
type: source
title: "A novel replication-deficient FCV vaccine provides strong immune protection in cats"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [neutralising antibodies, challenge protection, vaccine platform]
jurisdictions: []
evidence_level: original-study
year: 2025
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, vaccine, replication-deficient, challenge, multivalent]
links:
  doi: "10.1128/jvi.00093-25"
  url: "https://journals.asm.org/doi/10.1128/jvi.00093-25"
  local_assets: []
evidence_policy:
  quoted_fact:
    - Immunisation with the replication-deficient vaccine generated high neutralising-antibody levels and reduced clinical outcomes after homologous virulent systemic FCV challenge.
    - Combining constructs with genetically distant VP1 genes generated broad neutralising antibodies against FCV strains in cats.
  source_supported_conclusion:
    - This is the newest FCV vaccine-platform paper in the seed set.
    - The paper supports treating multivalent or platform-vaccine design as an active modern branch.
  llm_inference:
    - This source should likely be deep-extracted in the first vaccine-focused FCV batch.
  # V2 enhanced fields
  study_design: "原始实验研究，使用家猫作为研究对象，采用复制缺陷性猫杯状病毒（FCV）疫苗构建体接种及同源高毒力系统性FCV挑战测试免疫效果"
  core_argument: "复制缺陷性FCV疫苗能够在猫中诱导高效的中和抗体水平并显著减轻同源毒株感染的临床症状，且通过结合异源VP1基因构建实现广谱中和抗体反应。"
  implicit_premise: "诱导的中和抗体水平是评估疫苗保护效果的关键指标，且异源VP1基因的组合不会削弱疫苗免疫原性。"
  title_gap: "标题强调复制缺陷性FCV疫苗的新颖性，但真正发现是利用异源VP1设计实现了对多种FCV株的广谱中和保护——这为多价和平台疫苗设计提供了实验依据。"
  evidence_boundary: "本研究未评估该疫苗对猫长期免疫记忆的维持效果，也未涵盖疫苗在野外复杂感染环境中的实际保护效果。"
  unexpected_finding: "结合遗传距离较远的VP1基因片段反而增强了中和抗体的广谱性，挑战了单一株疫苗设计的传统思路。"
---

# A novel replication-deficient FCV vaccine provides strong immune protection in cats

## One-Line Summary

Modern vaccine-platform paper showing a replication-deficient FCV construct can generate strong immune protection and broaden neutralising activity with heterologous VP1 design.

## Why It Matters For FCV

- gives the module a current vaccine-technology anchor beyond classic strain swapping
- helps connect vaccine breadth to platform design rather than only field-isolate screening

## Key Findings

### quoted_fact

- Immunisation with the replication-deficient vaccine generated high neutralising-antibody levels and reduced clinical outcomes after homologous virulent systemic FCV challenge.
- Combining constructs with genetically distant VP1 genes generated broad neutralising antibodies against FCV strains in cats.

### source_supported_conclusion

- The candidate reduced clinical severity after virulent systemic FCV challenge.
- Two combined constructs with distant VP1 genes broadened neutralising responses.
- The platform was framed as potentially useful for multivalent or vector-style vaccine development.
- The source supports treating modern FCV vaccine design as an active platform and breadth problem, not only strain replacement.

### llm_inference

- This source should be the current newest vaccine-platform anchor in the FCV module.
- Its safest role is `experimental platform and breadth signal`, not `field-ready product recommendation`.

## Deep Extraction Notes

### Unit 1: The paper adds a platform branch to FCV vaccination

- core_claim: replication-deficient FCV design is being evaluated as more than a conventional isolate-substitution strategy.
- hard_details: immunisation generated high neutralising-antibody levels and reduced clinical outcomes after homologous virulent systemic FCV challenge.
- implication: vaccine pages should include platform design as a modern branch.
- boundary: the preserved evidence is experimental and should not be translated into current clinical product preference.

### Unit 2: Breadth is pursued through genetically distant VP1 design

- core_claim: combining constructs with genetically distant VP1 genes can broaden neutralising antibody responses.
- hard_details: the source card preserves broad neutralising antibodies against FCV strains in cats after combining constructs.
- implication: FCV vaccine breadth should be framed as antigenic-design work, not just a yes/no vaccine question.
- boundary: breadth in a tested panel is not the same as complete circulating-strain coverage.

### Unit 3: Challenge protection and neutralisation are related but not identical

- core_claim: the paper has both immunogenicity and challenge-protection relevance.
- hard_details: high neutralising antibodies and reduced clinical outcomes are both preserved.
- implication: endpoint pages should separate neutralising antibody breadth from clinical challenge outcome.
- boundary: field effectiveness, carrier-state reduction, and outbreak control remain outside this card's strongest claim.

## Claim-Evidence Structure

| Claim | Evidence in this card | Safe downstream use | Do not use for |
|---|---|---|---|
| Replication-deficient vaccine design produced immune response | high neutralising-antibody levels | platform-vaccine branch | current-market recommendation |
| Homologous VS-FCV challenge outcomes improved | reduced clinical outcomes after challenge | challenge-protection discussion | field effectiveness |
| VP1 diversity can broaden response | distant VP1 constructs generated broader neutralising antibodies | vaccine-breadth design logic | universal strain coverage |
| Modern FCV vaccine work remains active | 2025 platform paper | current research landscape | regulatory approval status |

## Write-Back Implications

- [endpoint handbook](../../topics/fcv/endpoint-handbook.md) should treat this as the newest platform-vaccine source.
- [current state dashboard](../../topics/fcv/current-state-dashboard.md) should distinguish this experimental branch from licensed-product evidence.
- [translation brief](../../topics/fcv/translation-brief.md) can mention modern platform work only with an experimental caveat.
- [synthesis index](../../topics/fcv/synthesis-index.md) should pair this with older breadth and persistence sources to avoid overclaiming.

## Limits / Caveats

- challenge and immunogenicity findings do not automatically translate to field effectiveness
- this source should not be promoted into immediate product-level recommendation

## Open Follow-Up Questions

- how broad was the heterologous neutralisation panel in practice?
- what tradeoffs exist between safety, breadth, and manufacturability for this platform?

## Linked Entities

- diseases: FCV
- models:
- endpoints: neutralising antibodies, challenge protection, vaccine platform
- mechanisms: VP1 diversity, replication-deficient design
- regulations:
