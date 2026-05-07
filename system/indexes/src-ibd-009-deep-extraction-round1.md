# src-ibd-009 Deep Extraction Round 1

## Verification Note

This worksheet is no longer title-level only. On 2026-04-23, the source was upgraded using the DOI article metadata and the matching Virginia Tech dissertation chapter that contains the same study text and tables. The journal DOI and PMC pages were not directly downloadable in that shell, so the source remains non-decision-grade even though the source card is now marked `verification_status: deep_extracted`.

## Core Takeaway

`histopathology-report classification belongs to pathology workflow architecture, and plasma-cell capture is the clearest recovered structured-report feature`

## What This Source Most Strongly Adds

- a concrete pathology-language and report-structure branch adjacent to diagnostic workup
- evidence that the current WSAVA microscopic feature set may lose discriminating information present in free-text pathology descriptions
- a candidate feature for structured report improvement: lamina propria plasma-cell quantity
- a useful LLM-wiki lesson: pathology reports need entity/feature normalization, not only citation storage

## Hard Details Recovered

- Dataset: 60 client-owned cats.
- Groups: 20 normal, 20 IBD, and 20 small-cell alimentary lymphoma cases.
- Setting: Virginia Tech Veterinary Teaching Hospital, 2008-2015.
- Tissue basis: upper GI endoscopic duodenal biopsy reports.
- Structured-report creation: original hematoxylin-and-eosin duodenal biopsy slides were retrieved, randomized, and rescored under WSAVA guidelines by one board-certified pathologist blinded to diagnosis.
- Structured features: nine WSAVA microscopic variables including epithelial injury, crypt distension, lacteal dilation, mucosal fibrosis, intraepithelial lymphocytes, lamina propria lymphocytes/plasma cells, eosinophils, and neutrophils.
- Free-text transformation: report descriptions were converted to word-occurrence vectors using WEKA text-processing tools.
- Algorithms: naive Bayes, C4.5 decision tree, and artificial neural networks.

## Quantitative Details Recovered

- Free-text average classification performance:
  - naive Bayes: 0.898
  - C4.5 decision tree: 0.755
  - artificial neural networks: 0.883
- Structured WSAVA average classification performance:
  - naive Bayes: 0.735
  - C4.5 decision tree: 0.717
  - artificial neural networks: 0.717
- Structured WSAVA plus plasma-cell feature:
  - naive Bayes: 0.792
  - C4.5 decision tree: 0.770
  - artificial neural networks: 0.782
- Plasma-word frequency in free-text descriptions:
  - IBD: 18/20 cases
  - normal: 5/20 cases
  - alimentary lymphoma: 7/20 cases

## Source-Supported Conclusions

- This source belongs in pathology-workflow architecture rather than frontline disease mechanism or treatment framing.
- Histopathology reporting structure can affect how much diagnostic signal survives into downstream classification.
- Free-text pathology reports may contain useful discriminating information that is not fully represented by current WSAVA structured microscopic variables.
- Plasma-cell quantity is a concrete candidate feature for improving structured report capture.
- The source can strengthen diagnostic-workup pages by separating tissue sampling, pathology interpretation, report structure, and automated classification.

## What It Does Not Prove

- It does not prove that machine learning can replace pathologist diagnosis.
- It does not prove that automated classification is ready for clinical decision-making.
- It does not replace biopsy-site strategy, imaging pressure, or integrated pathology review.
- It does not resolve the IBD-versus-lymphoma boundary in broad clinical populations.
- It does not support decision-grade or regulatory claims by itself.

## Best Write-Back Targets

- [ibd-diagnostic-workup-memo](ibd-diagnostic-workup-memo.md)
- [ibd-lymphoma-boundary-memo](ibd-lymphoma-boundary-memo.md)
- [ibd-source-depth-map](ibd-source-depth-map.md)

## Open Follow-up Questions

- Does the final journal article differ materially from the dissertation chapter version?
- Can plasma-cell quantification be standardized without overfitting to one institution's reporting style?
- Would performance hold if broader differentials were included?
- Should the IBD module get a small `pathology-report normalization` entity page later?
