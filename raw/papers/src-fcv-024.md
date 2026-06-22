---
id: src-fcv-024
type: source
title: "The use of sequence analysis of a feline calicivirus (FCV) hypervariable region in the epidemiological investigation of FCV related disease and vaccine failures"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [sequence epidemiology, vaccine failure, outbreak relatedness]
jurisdictions: []
evidence_level: original-study
year: 1997
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, sequence-epidemiology, vaccine-failure, outbreak, hypervariable-region]
links:
  doi: "10.1016/S0264-410X(97)00059-5"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S0264410X97000595?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - Isolates from the same outbreak were closely related, whereas unrelated isolates were much more distant.
    - Some vaccine-failure isolates were sufficiently similar to vaccine sequences to suggest vaccine origin.
  source_supported_conclusion:
    - This is a key FCV sequence-epidemiology and vaccine-failure boundary paper.
    - The paper supports keeping vaccine-failure investigation below simplistic “new resistant strain” narratives.
  llm_inference:
    - This source should pair naturally with later phylogeny and vaccine-breadth papers.
  # V2 enhanced fields
  study_design: "病毒分离与基因测序研究，采集多起猫杯状病毒（FCV）感染病例病毒样本，应用高变区序列分析进行流行病学关联性调查"
  core_argument: "疫苗失效不能简单归因于新抗性毒株——猫杯状病毒高变区序列分析表明，失效病例中既有明显不同的野外株，也有与疫苗株高度相似的分离株"
  implicit_premise: "高变区序列的遗传差异能够反映病毒传播链条及疫苗相关性，且序列聚类结果与流行病学数据一致"
  title_gap: "标题强调高变区序列在流行病调查中的应用，但真正揭示的是疫苗失效株既可能来源于疫苗，也可能来自多样的野外株——疫苗失效不应简单归因于新耐药株"
  evidence_boundary: "短序列区域分析研究（1997年），不等同于现代全基因组流行病学；未量化各类疫苗失效机制的发生频率或临床意义"
  unexpected_finding: "部分疫苗失效病毒株序列与疫苗株高度相似，提示疫苗株本身可能参与流行过程，突破传统仅把疫苗失效归因于野外变异株的观念"
---

# The use of sequence analysis of a feline calicivirus (FCV) hypervariable region in the epidemiological investigation of FCV related disease and vaccine failures

## One-Line Summary

Hypervariable-region sequencing paper showing outbreak-linked FCV isolates cluster tightly while vaccine-failure cases can reflect both distinct field strains and possible vaccine-related sequences.

## Why It Matters For FCV

- gives the module a molecular epidemiology tool paper for outbreak and vaccine-failure interpretation
- helps stop vaccine-failure stories from collapsing into one explanation

## Key Findings

### quoted_fact

- Isolates from the same outbreak were closely related, whereas unrelated isolates were much more distant.
- Some vaccine-failure isolates were sufficiently similar to vaccine sequences to suggest vaccine origin.

### source_supported_conclusion

- Same-outbreak isolates were very closely related.
- Unrelated isolates showed much larger sequence distances.
- Vaccine-failure isolates split into clearly distinct strains and vaccine-like strains.
- The source supports using sequence analysis to separate outbreak relatedness, field-strain difference, and possible vaccine-origin explanations.

### llm_inference

- This source should anchor the older sequence-epidemiology and vaccine-failure boundary branch.
- Its safest role is `investigation tool and narrative guardrail`, not `universal vaccine-failure explanation`.

## Deep Extraction Notes

### Unit 1: Sequence analysis can resolve relatedness questions

- core_claim: hypervariable-region sequencing helped distinguish related outbreak isolates from unrelated isolates.
- hard_details: same-outbreak isolates were closely related, while unrelated isolates were much more distant.
- implication: outbreak pages should frame sequencing as a relatedness tool.
- boundary: short-region analysis is not equivalent to modern whole-genome epidemiology.

### Unit 2: Vaccine failure has more than one molecular story

- core_claim: vaccine-failure isolates were not all one kind of failure.
- hard_details: some isolates were clearly distinct strains, while some were vaccine-like.
- implication: user-facing and clinician-facing copy should avoid saying vaccine failure simply means a resistant new strain.
- boundary: this source cannot quantify how common each failure pathway is now.

### Unit 3: This card is a boundary source for interpretation

- core_claim: the paper's value is in forcing careful interpretation of molecular evidence.
- hard_details: outbreak relatedness and vaccine-like sequences are both preserved.
- implication: it should pair with phylogeny and vaccine-breadth papers to create a cautious vaccine-failure branch.
- boundary: do not promote it into current vaccine product ranking or policy guidance.

## Claim-Evidence Structure

| Claim | Evidence in this card | Safe downstream use | Do not use for |
|---|---|---|---|
| Outbreak isolates can cluster tightly | same-outbreak isolates closely related | outbreak relatedness explanation | modern WGS replacement |
| Unrelated isolates are more distant | unrelated isolates had larger distances | sequence-epidemiology teaching point | universal distance threshold |
| Some vaccine-failure isolates may be vaccine-like | similarity to vaccine sequences | vaccine-failure narrative caution | frequency estimate |
| Vaccine failure is not one explanation | distinct and vaccine-like strains both appear | boundary-setting in vaccine pages | product ranking |

## Write-Back Implications

- [endpoint handbook](../../topics/fcv/endpoint-handbook.md) should use this as a vaccine-failure interpretation source.
- [mechanism overview](../../topics/fcv/mechanism-overview.md) can cite it for sequence-epidemiology logic, not pathogenesis.
- [translation brief](../../topics/fcv/translation-brief.md) should preserve the message that apparent vaccine failure needs careful investigation.

## Limits / Caveats

- short-region sequence work is not a complete whole-genome explanation
- this paper should not be overpromoted into a universal vaccine-failure rule

## Open Follow-Up Questions

- how often were vaccine-like sequences clinically meaningful versus incidental?
- how should this paper be reconciled with later full-genome phylogeny?

## Linked Entities

- diseases: FCV
- models:
- endpoints: sequence epidemiology, vaccine failure, outbreak relatedness
- mechanisms: capsid hypervariable region, strain relatedness
- regulations:
