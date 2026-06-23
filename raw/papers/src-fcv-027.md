---
id: src-fcv-027
type: source
title: "Feline Calicivirus Virulent Systemic Disease: Clinical Epidemiology, Analysis of Viral Isolates and In Vitro Efficacy of Novel Antivirals in Australian Outbreaks"
source_kind: paper
species: feline
diseases: [FCV]
models: [outbreak-investigation, in-vitro-antiviral]
endpoints: [mortality, antiviral-EC50, viral-phylogenetics]
jurisdictions: [Australia]
evidence_level: original-study
year: 2021
status: deep_extracted
extraction_depth: partial
verification_status: abstract_weighted
pmid: "34696470"
doi: "10.3390/v13102040"
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, VS-FCV, virulent-systemic, antivirals, nitazoxanide, 2CMC, NITD-008, outbreak, phylogenetics, recombination, Australia]
links:
  doi: "10.3390/v13102040"
  url: "https://doi.org/10.3390/v13102040"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Overall mortality among 23 cases of FCV-VSD was 39%."
    - "Five genetically distinct FCV lineages within the three outbreaks, all seemingly evolving in situ in Australia."
    - "No mutations that clearly distinguished FCV-URTD from FCV-VSD phenotypes were identified."
    - "Dose-response inhibition of FCV-VSD at low micromolar concentrations."
    - "Investigation of these antivirals for the treatment of FCV-VSD is warranted."
  source_supported_conclusion:
    - "VS-FCV mortality is 39% (n=23 across 3 Australian outbreaks)."
    - "Five distinct viral lineages evolved locally in Australia; no universal VS-FCV mutation signature."
    - "Three antivirals show in vitro efficacy: Nitazoxanide (EC50 0.4-0.6 µM, TI=21), 2CMC (EC50 2.7-5.3 µM, TI>18), NITD-008 (EC50 0.5-0.9 µM, TI>111)."
    - "NITD-008 has highest therapeutic index (>111) but is experimental."
    - "Recombination contributes to FCV genetic diversity."
  llm_inference:
    - "Nitazoxanide is the most clinically accessible compound (already approved for other indications)."
    - "Lack of distinguishing VS-FCV mutations complicates diagnostic prediction of virulence."
    - "In vitro efficacy warrants clinical trials but does not constitute treatment recommendation."
  # V2 enhanced fields
  study_design: "前瞻性病例系列研究，23例澳大利亚FCV-VSD病例，结合病毒基因组测序和细胞培养中抗病毒药物体外活性检测"
  core_argument: "澳大利亚VC-FCV病例中发现5条局地进化的病毒谱系，未鉴定出统一的致病毒变异，且三种新型抗病毒药物在低微摩尔浓度显示有效抑制作用，提示其治疗潜力。"
  implicit_premise: "病毒致病性主要由多基因或环境因素决定，单一基因突变不足以解释致病性差异，体外抗病毒活性可部分反映潜在临床疗效。"
  title_gap: "标题强调病毒系统性疾病及临床流行病学，但实际揭示的是病毒多源局部进化及缺乏统一致病变异，同时首次验证了多种新抗病毒的体外抑制效果——为治疗提供新方向。"
  evidence_boundary: "未明确验证三种抗病毒药物的临床疗效及安全性，未探讨病毒致病机制的具体分子基础，也未涉及不同猫群体或免疫状态下的疾病表现差异。"
  unexpected_finding: "尽管高致病性，FCV-VSD病毒未显示任何统一的致病性相关突变，说明致病性可能由复杂因素共同作用产生。"
---

# FCV Virulent Systemic Disease: Clinical Epidemiology + Antivirals (Australia)

## Evidence-Depth Caveat

**Deep-extracted from PubMed abstract (PMID 34696470).** 2021 Viruses study of 3 Australian VS-FCV outbreaks (n=23 cases, 39% mortality). Five distinct viral lineages; no universal VS-FCV mutation. Three antivirals tested: Nitazoxanide (EC50 0.4-0.6 µM), 2CMC (EC50 2.7-5.3 µM), NITD-008 (EC50 0.5-0.9 µM). Evidence level: original study with in vitro antiviral data.

## Source Check, 2026-06-17

PubMed abstract extracted.

- PMID: 34696470
- DOI: 10.3390/v13102040
- Journal: Viruses (MDPI)
- Year: 2021
- Open access: yes

## Clinical Epidemiology

| Metric | Value |
|--------|-------|
| Outbreaks analyzed | 3 |
| Total cases | 23 |
| Overall mortality | **39%** |
| Location | Australia |
| Viral lineages | 5 distinct |

## Viral Characterization

**Quoted:** "Five genetically distinct FCV lineages within the three outbreaks, all seemingly evolving in situ in Australia."

**Key finding:** "No mutations that clearly distinguished FCV-URTD from FCV-VSD phenotypes were identified."

- Recombination identified in one URTD strain
- Local evolution pattern (not imported)
- No universal virulence marker

## Antiviral Efficacy (In Vitro)

| Compound | EC50 (µM) | Therapeutic Index | Status |
|----------|-----------|-------------------|--------|
| Nitazoxanide (NTZ) | 0.4-0.6 | 21 | Approved (other indications) |
| 2'-C-methylcytidine (2CMC) | 2.7-5.3 | >18 | Experimental |
| NITD-008 | 0.5-0.9 | **>111** | Experimental |

**Quoted:** "Dose-response inhibition of FCV-VSD at low micromolar concentrations."

**Quoted:** "Investigation of these antivirals for the treatment of FCV-VSD is warranted."

## One-Line Summary

Australian VS-FCV study (n=23, 39% mortality): 5 distinct lineages, no universal virulence mutation; 3 antivirals show in vitro efficacy (Nitazoxanide, 2CMC, NITD-008).

## Claim-Fit Judgment

**Strongest safe use:**
- VS-FCV mortality estimate (39%, n=23)
- Viral lineage diversity and local evolution
- In vitro antiviral EC50 values
- Lack of diagnostic virulence mutations

**May control:**
- FCV index page VS-FCV section
- Treatment overview experimental antivirals
- Mechanism overview viral diversity

**Should use with caveats:**
- Antiviral recommendations (in vitro only, no clinical trials)
- Mortality rates (limited sample size)

**Must not control:**
- Clinical treatment protocols
- Drug dosing recommendations
- Universal VS-FCV mutation claims

## Deep Extraction Metadata

- **Extraction date:** 2026-06-17
- **Source:** PubMed abstract (PMID 34696470)
- **Full text verified:** Abstract-level
- **Citations in vault topic pages:** 12 (high-priority branch-controlling)

## Linked Entities

- diseases: FCV, VS-FCV (virulent systemic disease)
- antivirals: Nitazoxanide, 2CMC, NITD-008
- endpoints: mortality, EC50, therapeutic index
- mechanisms: viral replication inhibition, recombination
- regulations: none (experimental therapeutics)
