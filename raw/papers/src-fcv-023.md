---
id: src-fcv-023
type: source
title: "Nucleotide sequence of UK and Australian isolates of feline calicivirus (FCV) and phylogenetic analysis of FCVs"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [phylogeny, genome diversity]
jurisdictions: [UK, Australia]
evidence_level: original-study
year: 1999
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, phylogeny, genome, diversity, uk, australia]
links:
  doi: "10.1016/S0378-1135(99)00043-7"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S0378113599000437?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - Phylogenetic analysis suggested FCV isolates in the dataset fell into one diverse genogroup.
    - There was an overall lack of geographic or temporal clustering in the analysed isolates.
  source_supported_conclusion:
    - This is a foundational FCV sequence-diversity and phylogeny paper.
    - The paper supports caution against simple geography-or-time clustering assumptions.
  llm_inference:
    - This source should help anchor the molecular-diversity branch beneath broader reviews.
  # V2 enhanced fields
  study_design: "分子遗传学研究，采集英国和澳大利亚多株猫杯状病毒（FCV）分离株，采用核苷酸测序和系统发育分析"
  core_argument: "猫杯状病毒的不同地理来源分离株在基因组上存在广泛多样性，但不表现出明显的地域性或时间性聚类"
  implicit_premise: "系统发育和序列分析能够准确反映病毒的遗传关系及其地理和时间分布特征"
  title_gap: "标题强调了序列测定及系统发育分析，但真正的发现是这些FCV株虽遗传多样，却没有预期中的地域或时间聚类——这挑战了基于地理或时间推断病毒传播路径的传统假设"
  evidence_boundary: "未探讨FCV的临床表现、致病机制或疫苗效果，也未涵盖亚洲或其他大陆的病毒株遗传情况"
  unexpected_finding: "尽管采样涵盖不同国家和时间，系统发育树未见分明显的地域或时间相关性，违背了通常病毒群体在地理和时间上的分层预期"
---

# Nucleotide sequence of UK and Australian isolates of feline calicivirus (FCV) and phylogenetic analysis of FCVs

## One-Line Summary

Foundational FCV sequencing paper showing broad genomic diversity but limited clean geographic or temporal clustering among analysed isolates.

## Why It Matters For FCV

- gives the module a sequence-era anchor under later vaccine and epidemiology claims
- helps explain why FCV strain selection and vaccine design are persistently hard

## Key Findings

### quoted_fact

- Phylogenetic analysis suggested FCV isolates in the dataset fell into one diverse genogroup.
- There was an overall lack of geographic or temporal clustering in the analysed isolates.

### source_supported_conclusion

- Complete genome and capsid comparisons showed broad but structured FCV diversity.
- ORF1 and ORF2 variation was substantial, while ORF3 behaved differently.
- Analysed FCVs formed one diverse genogroup without simple geography/time clustering.
- The source supports caution against assuming clean geography-based or time-based FCV clustering.

### llm_inference

- This source should anchor the older molecular-diversity branch beneath broad review and vaccine-fit discussions.
- Its safest role is `foundational phylogeny and diversity`, not `current surveillance map`.

## Deep Extraction Notes

### Unit 1: FCV diversity is broad but not easily partitioned

- core_claim: the analysed isolates fell into one diverse genogroup rather than cleanly separable groups.
- hard_details: the card preserves one diverse genogroup and lack of geographic or temporal clustering.
- implication: vaccine and epidemiology pages should avoid simple country-era lineage stories unless newer data support them.
- boundary: this is older sequence-era evidence and should not be treated as current circulation mapping.

### Unit 2: Genome-region variation matters

- core_claim: ORF-level behaviour differs across the genome.
- hard_details: ORF1 and ORF2 variation was substantial, while ORF3 behaved differently.
- implication: molecular pages should avoid generic `the genome varies` statements and preserve region-specific nuance.
- boundary: the card does not by itself identify which changes drive clinical phenotype.

### Unit 3: Foundational molecular evidence supports vaccine-fit caution

- core_claim: older phylogeny already shows why FCV strain fit is difficult.
- hard_details: broad diversity and poor geography/time clustering are preserved.
- implication: this card can support the background rationale for cross-neutralisation and geography-specific vaccine papers.
- boundary: use newer vaccine studies for neutralisation percentages or platform claims.

## Claim-Evidence Structure

| Claim | Evidence in this card | Safe downstream use | Do not use for |
|---|---|---|---|
| Analysed FCVs were diverse | one diverse genogroup | molecular-diversity background | current strain prevalence |
| Clustering was not simple | lack of geographic or temporal clustering | anti-simplistic geography/time caveat | universal absence of clustering |
| Genome regions differ | ORF1/ORF2 variation, ORF3 difference | mechanism and phylogeny nuance | phenotype assignment |
| Vaccine fit is difficult | diversity and clustering limits | background to vaccine-breadth branch | vaccine-performance claims |

## Write-Back Implications

- [mechanism overview](../../topics/fcv/mechanism-overview.md) should use this for foundational genomic-diversity language.
- [endpoint handbook](../../topics/fcv/endpoint-handbook.md) can cite this only as background for vaccine-fit difficulty.
- [current state dashboard](../../topics/fcv/current-state-dashboard.md) should pair this older source with newer regional epidemiology before making any current-state claim.

## Limits / Caveats

- older sequencing era and dataset size constrain what it can say about current FCV circulation
- should not be promoted into a modern surveillance answer by itself

## Open Follow-Up Questions

- how do the older phylogenetic conclusions compare with newer prevalent-strain studies?
- which genomic regions matter most for vaccine breadth versus pathotype shift?

## Linked Entities

- diseases: FCV
- models:
- endpoints: phylogeny, genome diversity
- mechanisms: ORF variation, capsid diversity
- regulations:
