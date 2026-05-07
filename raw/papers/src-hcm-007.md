---
id: src-hcm-007
type: source
title: "The Feline Cardiomyopathies: 1. General concepts"
source_kind: paper
species: feline
diseases: [HCM, cardiomyopathy]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 2021
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [cardiomyopathy, review, framing]
links:
  doi: "10.1177/1098612X211021819"
  url: "https://journals.sagepub.com/doi/10.1177/1098612X211021819"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The source covers general concepts in feline cardiomyopathies."
    - "The abstract states that feline cardiomyopathies are the most prevalent heart disease type in adult domestic cats and that HCM is the most common form."
    - "The abstract states that echocardiography is the definitive clinical confirmatory test, while biomarkers and imaging can assist recognition."
    - "The source card captures abstract-level framing that feline cardiomyopathies are often clinically indistinguishable."
    - "The abstract states that prognosis is often guarded or poor once overt clinical manifestations appear."
  source_supported_conclusion:
    - This is a high-value framing source for placing HCM inside a broader myocardial-disease map.
    - The review supports keeping cardiomyopathy classification visible around HCM, instead of collapsing myocardial disease into one phenotype story.
    - The paper is useful because it keeps suspicion separate from confirmation, which helps prevent the endpoint layer from flattening supportive signals and definitive structural diagnosis into one list.
    - This review also supports keeping overt-clinical-disease prognosis distinct from earlier subclinical phenotype recognition.
  llm_inference:
    - This is one of the best first deep-extraction targets for the HCM shell.
    - The HCM module should keep an outer cardiomyopathy frame so extension branches do not have to be recreated ad hoc later.
---

# One-line Summary

General cardiomyopathy framing source that should anchor the outer frame of the HCM module and keep HCM inside the wider myocardial-disease map.

## Why It Matters For HCM

- keeps HCM connected to broader myocardial-disease classification
- likely helps recognition and extension logic
- now gives the HCM shell a safer outer rule that cardiomyopathy recognition is broader than one phenotype

## Key Findings

- broad feline cardiomyopathy concepts source
- abstract states that cardiomyopathies are often clinically indistinguishable
- abstract states that echocardiography is the confirmatory test, while biomarkers and thoracic imaging can aid suspicion
- abstract states that prognosis is often guarded or poor once overt clinical manifestations appear

## Why This Review Matters

This review matters because it stops the HCM module from over-isolating itself.

HCM may be the most common feline cardiomyopathy, but the paper starts one level higher, at the cardiomyopathy family. That is useful because it keeps HCM connected to a broader myocardial-disease classification problem instead of pretending every thickened ventricle already sits inside one clean phenotype bucket.

It also improves diagnostic architecture. The paper keeps suspicion and confirmation separate. Biomarkers and other imaging tools may help raise concern, but echocardiography remains the definitive confirmatory branch. That is exactly the kind of hierarchy a compiled endpoint page needs if it wants to avoid biomarker overcompression.

Finally, the review helps preserve stage structure. If prognosis becomes guarded or poor once overt manifestations appear, then overt disease cannot be allowed to define the whole module. Silent structural disease, recognition-stage disease, and overt decompensation have to stay distinct.

## Outer-Frame Signal

The safest promotion from this source is:

- HCM should stay inside a broader cardiomyopathy frame
- suspicion-support tools and confirmatory tools should be separated
- clinically indistinguishable phenotypes make symptoms alone inadequate
- overt prognosis should not erase subclinical recognition architecture

That makes this review a framing anchor, not just background context.

It also strengthens one specific anti-overclaim rule for the module: broad cardiomyopathy framing should remain visible even when HCM is the operational focus. That prevents downstream pages from treating every feline myocardial presentation as though the classification work has already been finished before echocardiographic confirmation.

## Limits / Caveats

- current card is abstract-weighted, not full-text reviewed
- The source is strongest for outer-frame classification and recognition architecture, not for a detailed phenotype-by-phenotype prognostic hierarchy.

## Open Follow-up Questions

- how does it classify HCM against other phenotypes?
- does it change which branches need to appear in the HCM shell?
- how much does the general framing alter recognition logic versus prognosis framing?
- which ancillary imaging tools does it treat as practically useful before echocardiographic confirmation?
- how sharply does it distinguish cardiomyopathy classification from symptom-based clinical presentation?

## Linked Entities

- HCM
- cardiomyopathy
- echocardiography
