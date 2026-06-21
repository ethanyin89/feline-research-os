---
id: src-ckd-002
type: source
title: "Feline CKD: Diagnosis, staging and screening – what is recommended?"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: [creatinine, sdma]
jurisdictions: []
evidence_level: review
year: 2014
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, diagnosis, staging, screening]
links:
  doi: "10.1177/1098612X13495235"
  url: "https://journals.sagepub.com/doi/10.1177/1098612X13495235"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Feline CKD diagnosis is based on compatible clinical signs and renal azotaemia, making urinalysis, especially urine specific gravity, mandatory for diagnostic confirmation."
    - "Advanced CKD and its complications are usually easier to diagnose with complete blood and urine examination than early CKD."
    - "Routine blood and urine tests have important limitations for detecting early CKD."
    - "Glomerular filtration rate would be ideal for identifying early kidney dysfunction, but practical limitations reduce its routine clinical use."
    - "CKD is typically a disease of aged cats, although it can occur at any age."
    - "The review covers the IRIS classification system and techniques for early detection."
  source_supported_conclusion:
    - This review is a high-value diagnostic anchor because it cleanly separates routine CKD confirmation from the harder problem of earlier or non-azotaemic detection.
    - USG should remain inside the operational diagnostic core because the paper gives urinalysis explicit authority rather than treating it as optional context.
    - GFR should continue to be framed as the conceptual gold standard for early dysfunction detection, but not as a routine first-line tool in current feline workflows.
    - Staging and screening should stay linked but not collapsed together, because the review preserves their different operational jobs.
  llm_inference:
    - Endpoint and early-detection pages should continue to describe a two-layer logic: practical diagnosis first, earlier recognition second.
    - Any one-test screening narrative would overstate what this source supports.
  # V2 enhanced fields
  study_design: "综述，涵盖猫 CKD 的诊断、分期和筛查"
  core_argument: "猫 CKD 诊断基于临床症状和肾性氮质血症，尿检（特别是尿比重）是诊断确认的必要条件——但早期或非氮质血症期 CKD 检测难度显著高于晚期"
  implicit_premise: "假设常规血尿检测的局限性是系统性的而非仅限于特定检测方法；假设 GFR 在理论上是早期检测的金标准"
  unexpected_finding: "尽管 GFR 是理想的早期检测指标，实际操作限制使其不适合常规临床使用——这提示「概念金标准」与「实用工作流」需要分开讨论"
  title_gap: "标题说诊断、分期和筛查，但真正挑战是早期检测的实用性落差：GFR 是概念金标准但不可常规使用——早期 CKD 检测与晚期诊断是不同的问题"
  evidence_boundary: "综述层面无法为每个升级检测排序；早期检测技术讨论的临床可操作性仍待验证"
---

# Feline CKD: Diagnosis, staging and screening – what is recommended?

## One-Line Summary

This review argues that timely diagnosis and staging improve prognosis, but emphasizes that early or non-azotaemic CKD is substantially harder to detect than advanced disease.

## Why It Matters For CKD

This likely anchors the endpoint layer and screening logic for CKD topic pages.

## Key Findings

### quoted_fact

- Feline CKD diagnosis is based on compatible clinical signs and renal azotaemia, making urinalysis, especially urine specific gravity, mandatory for diagnostic confirmation.
- Advanced CKD and its complications are usually easier to diagnose with complete blood and urine examination than early CKD.
- Routine blood and urine tests have important limitations for detecting early CKD.
- Glomerular filtration rate would be ideal for identifying early kidney dysfunction, but practical limitations reduce its routine clinical use.
- CKD is typically a disease of aged cats, although it can occur at any age.
- The review covers the IRIS classification system and techniques for early detection.
- The paper treats early or non-azotaemic CKD as a distinct recognition problem rather than simply a milder version of advanced disease.

### source_supported_conclusion

- The endpoint handbook should explicitly separate routine clinical diagnosis endpoints from ideal but impractical early-detection measures.
- USG remains a core practical endpoint, even though it is not sufficient on its own for early detection.
- Early CKD detection should be treated as a distinct subproblem in the endpoint page rather than folded into routine staging.
- This review is useful because it gives the vault a stable diagnostic hierarchy without overclaiming what current routine testing can do for the earliest disease states.
- The paper also helps keep IRIS staging visible while preventing staging logic from being mistaken for a solved screening workflow.

### llm_inference

- GFR-related thinking may matter more as a conceptual benchmark than as a practical V1 endpoint, unless later sources show a realistic feline workflow.
- The safest compiled diagnostic story remains composite and persistence-based, not biomarker-monist.

## Why This Review Matters

This review matters because it forces a clean distinction that the vault can easily blur if left unchecked.

Routine CKD diagnosis and early CKD detection are not the same job. The review makes ordinary diagnostic confirmation look comparatively straightforward once compatible signs, renal azotaemia, and urine-concentration context are available. But it treats early or non-azotaemic disease as much harder to capture with routine testing alone.

That distinction improves compilation quality in two ways.

First, it protects USG from being underplayed. Urinalysis is not merely supporting context here. It is part of diagnostic authority.

Second, it keeps ideal concepts like GFR in the right place. GFR is still the best conceptual measure of early dysfunction, but this source directly supports keeping it below the routine first-line workflow because operational limitations matter.

## Practical Diagnostic Hierarchy

The safest hierarchy supported by this paper is:

- routine clinical diagnosis uses composite clinical and laboratory interpretation
- urinalysis and USG retain first-wave authority
- early detection remains materially harder than advanced-disease recognition
- GFR is ideal in theory, but weak operationally
- staging and screening overlap, but should not be collapsed into one undifferentiated paragraph

That makes this review more than a generic diagnosis summary. It is a boundary-setting source for endpoint architecture.

## Limits / Caveats

- Current extraction is still abstract-heavy.
- More detail is needed on proteinuria and additional diagnostic testing sections.
- The source is stronger for diagnostic architecture and screening boundaries than for fine-grained ranking of every escalation test.

## Open Follow-Up Questions

- Which tests are part of the minimum recommended workup versus escalation workup?
- How does this review frame proteinuria in relation to diagnosis versus prognosis?
- Which parts of early-detection technique discussion remain clinically usable versus mostly conceptual?
- Does the paper give enough detail to refine how IRIS staging should be separated from screening language in compiled pages?

## Linked Entities

- diseases: CKD
- models:
- endpoints: creatinine, SDMA, USG, GFR, proteinuria
- mechanisms:
- regulations:
