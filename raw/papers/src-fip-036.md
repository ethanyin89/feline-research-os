---
id: src-fip-036
type: source
title: "Rapid Clinical Resolution and Differential Diagnosis of a Neurological Case of Feline Infectious Peritonitis (FIP) Using GS-441524"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: [neurological-resolution, seizure-control, viral-clearance]
jurisdictions: [USA]
evidence_level: case-report
year: 2025
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
pmid: "40430745"
doi: "10.3390/pathogens14050424"
tags: [fip, neurological-fip, gs-441524, tetraparesis, ataxia, seizures, nanopore-sequencing, FCoV, case-report, 84-day-protocol]
links:
  doi: "10.3390/pathogens14050424"
  url: "https://doi.org/10.3390/pathogens14050424"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Progressive history of tetraparesis, ataxia, and inappetence over 4 days."
    - "Non-ambulatory tetraparetic and developed seizures while in hospital."
    - "MRI revealed multifocal meningeal contrast enhancement in the brainstem and cervical spine."
    - "Targeted Nanopore-based sequencing identified FCoV-1 RNA in spinal fluid and anal swab, but not in urine."
    - "Neurologic signs did not improve on an antibiotic alone but improved significantly after two subcutaneous injections of GS-441524."
    - "At follow-up exceeding 12 months post-diagnosis, the cat remains ambulatory and seizure-free without recurrence of neurologic signs and no detectable viral shedding in feces."
  source_supported_conclusion:
    - "Neurological FIP can present with tetraparesis, ataxia, seizures, and meningeal enhancement on MRI."
    - "Nanopore sequencing of CSF can confirm FIP diagnosis when other tests are inconclusive."
    - "GS-441524 produces rapid neurological improvement where antibiotics fail."
    - "84-day GS-441524 treatment achieves sustained remission (>12 months) with viral clearance."
    - "Differential diagnosis should exclude toxoplasmosis and cryptococcosis."
  llm_inference:
    - "Nanopore sequencing represents emerging diagnostic modality for neurological FIP."
    - "Subcutaneous GS-441524 effective for CNS disease (suggests adequate penetration)."
    - "Single case limits generalizability but demonstrates proof of concept."
  # V2 enhanced fields
  study_design: "病例报告，2 岁 DSH 神经性 FIP（四肢瘫痪、癫痫发作、脑膜增强）使用 GS-441524 皮下注射 84 天治疗"
  core_argument: "神经性 FIP 可通过纳米孔测序在 CSF 中确诊 FCoV-1——GS-441524 产生快速神经学改善（抗生素单独无效），>12 个月缓解且病毒清除"
  implicit_premise: "假设纳米孔测序代表神经性 FIP 的新兴诊断方式；假设皮下 GS-441524 对 CNS 疾病有足够穿透"
  unexpected_finding: "仅两次皮下注射 GS-441524 后神经症状即显著改善——比预期更快的反应"
  title_gap: "标题说神经性 FIP 的快速临床缓解和鉴别诊断，但真正发现是诊断方法学：纳米孔测序在 CSF 中确诊 FCoV-1——代表神经性 FIP 的新兴诊断方式，仅两次皮下注射即显著改善"
  evidence_boundary: "单例报告（n=1）限制推广性；鉴别诊断应排除弓形虫病和隐球菌病"
---

# Rapid Clinical Resolution and Differential Diagnosis of a Neurological Case of Feline Infectious Peritonitis (FIP) Using GS-441524

## Evidence-Depth Caveat

**Deep-extracted from PubMed abstract (PMID 40430745).** 2025 Pathogens case report: 2-year-old DSH with neurological FIP (tetraparesis, seizures, meningeal enhancement). Nanopore sequencing confirmed FCoV-1 in CSF. GS-441524 SC produced rapid improvement; >12 month remission, seizure-free, viral clearance. Evidence level: case report.

## Source Check, 2026-06-17

PubMed abstract extracted.

- PMID: 40430745
- DOI: 10.3390/pathogens14050424
- Journal: Pathogens (MDPI)
- Year: 2025
- Open access: yes

## Case Presentation

| Feature | Value |
|---------|-------|
| Patient | 2-year-old male DSH |
| Duration of signs | 4 days progressive |
| Initial signs | Tetraparesis, ataxia, inappetence |
| Hospital progression | Non-ambulatory tetraparesis, seizures |
| Other signs | Mucopurulent nasal discharge, stertor |

## Neuroimaging

**Quoted:** "MRI revealed multifocal meningeal contrast enhancement in the brainstem and cervical spine."

## Diagnostic Workup

| Test | Result |
|------|--------|
| Toxoplasmosis | Excluded |
| Cryptococcosis | Excluded |
| **Nanopore sequencing** | FCoV-1 RNA in CSF and anal swab |
| Urine | FCoV-1 negative |

**Quoted:** "Targeted Nanopore-based sequencing identified FCoV-1 RNA in spinal fluid and anal swab, but not in urine."

## Treatment Response

**Quoted:** "Neurologic signs did not improve on an antibiotic alone but improved significantly after two subcutaneous injections of GS-441524."

| Treatment | Response |
|-----------|----------|
| Antibiotics alone | No improvement |
| GS-441524 (SC) | **Significant improvement** |
| Anticonvulsants | Phenobarbital, levetiracetam |
| Duration | 84 days |

## Long-Term Outcome

**Quoted:** "At follow-up exceeding 12 months post-diagnosis, the cat remains ambulatory and seizure-free without recurrence of neurologic signs and no detectable viral shedding in feces."

| Outcome | Status |
|---------|--------|
| Follow-up | >12 months |
| Ambulation | Restored |
| Seizures | None |
| Neurological signs | No recurrence |
| Viral shedding | Undetectable |

## One-Line Summary

2025 case report: neurological FIP (tetraparesis, seizures, meningeal MRI enhancement) confirmed by Nanopore CSF sequencing; GS-441524 SC achieved rapid improvement and sustained >12 month remission with viral clearance.

## Claim-Fit Judgment

**Strongest safe use:**
- Neurological FIP presentation (tetraparesis, seizures, MRI findings)
- Nanopore sequencing as diagnostic tool
- GS-441524 efficacy in neurological FIP
- Differential diagnosis approach

**May control:**
- FIP mechanism-overview.md neurological section
- Diagnosis approach for neuro FIP
- Treatment-overview.md CNS disease response

**Should use with caveats:**
- Single case report (n=1)
- Specific sequencing technology

**Must not control:**
- Universal treatment protocols
- Prognosis predictions for neuro FIP

## Deep Extraction Metadata

- **Extraction date:** 2026-06-17
- **Source:** PubMed abstract (PMID 40430745)
- **Full text verified:** Abstract-level
- **Citations in vault topic pages:** 6 (branch-controlling)

## Linked Entities

- diseases: FIP, neurological FIP
- drugs: GS-441524, phenobarbital, levetiracetam
- diagnostics: Nanopore sequencing, MRI, CSF analysis
- signs: tetraparesis, ataxia, seizures, meningeal enhancement
- outcomes: remission, viral clearance
