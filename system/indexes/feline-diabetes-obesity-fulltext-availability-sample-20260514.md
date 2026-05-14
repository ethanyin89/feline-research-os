---
id: feline-diabetes-obesity-fulltext-availability-sample-20260514
type: system
topic: content-pipeline
question_type: fulltext-availability-check
language: zh
last_compiled_at: 2026-05-14
verification_status: generated
decision_grade: no
owner: codex
status: active
---

# Feline Full-Text Availability Check, 2026-05-14

Source set: `diabetes obesity deep-extraction candidate availability sample 2026-05-14`

## Rule

This report checks full-text availability signals before deep extraction. It does not download articles, create clinical claims, or promote source-card status.

## Summary

- Cards checked: `10`
- Crossref metadata found: `10`
- With Crossref full-text/TDM links: `10`
- With license metadata: `9`
- With reachable HEAD probes: `5`
- With Crossref abstracts: `8`

## Availability Table

| Source | Status | DOI | Abstract | Links | License | Reachable Probe | Recommendation |
|---|---|---|---|---:|---:|---:|---|
| `src-diabetes-035` | `abstract_weighted` | `10.2460/javma.24.03.0174` | `yes` | 3 | 1 | 1 | full-text/TDM link present; verify access before deep extraction |
| `src-diabetes-046` | `title_only` | `10.1016/j.cvsm.2023.02.001` | `no` | 2 | 7 | 1 | full-text/TDM link present; verify access before deep extraction |
| `src-diabetes-050` | `abstract_weighted` | `10.1177/1098612x15571880` | `yes` | 3 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |
| `src-diabetes-087` | `abstract_weighted` | `10.5326/jaaha-ms-6822` | `yes` | 4 | 1 | 1 | full-text/TDM link present; verify access before deep extraction |
| `src-diabetes-091` | `abstract_weighted` | `10.1111/jvim.16625` | `yes` | 4 | 2 | 0 | full-text/TDM link present; verify access before deep extraction |
| `src-obesity-001` | `title_only` | `10.17221/145/2015-vetmed` | `no` | 1 | 1 | 1 | full-text/TDM link present; verify access before deep extraction |
| `src-obesity-004` | `abstract_weighted` | `10.1177/1098612x241285519` | `yes` | 3 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |
| `src-obesity-005` | `abstract_weighted` | `10.1177/1098612x241228042` | `yes` | 3 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |
| `src-obesity-008` | `abstract_weighted` | `10.1053/jfms.2001.0138` | `yes` | 3 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |
| `src-obesity-080` | `abstract_weighted` | `10.2460/ajvr.79.2.181` | `yes` | 3 | 0 | 1 | full-text/TDM link present; verify access before deep extraction |

## Link Detail

### `src-diabetes-035`

- Title: Velagliflozin, a once-daily, liquid, oral SGLT2 inhibitor, is effective as a stand-alone therapy for feline diabetes mellitus: the SENSATION study
- Container/year: Journal of the American Veterinary Medical Association / 2024
- DOI landing: https://doi.org/10.2460/javma.24.03.0174
- Primary URL: https://avmajournals.avma.org/view/journals/javma/262/10/javma.24.03.0174.xml
- Full-text/TDM links: https://avmajournals.avma.org/view/journals/javma/262/10/javma.24.03.0174.xml (text/html,...; https://avmajournals.avma.org/downloadpdf/journals/javma/262/10/javma.24.03.0174.xml (tex...; +1 more
- License URLs: http://creativecommons.org/licenses/by-nc/4.0/
- HEAD probes: https://avmajournals.avma.org/view/journals/javma/262/10/javma.24.03.0174.xml -> HTTP 403; https://avmajournals.avma.org/downloadpdf/journals/javma/262/10/javma.24.03.0174.xml -> 2...
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-diabetes-046`

- Title: Pathophysiology of Prediabetes, Diabetes, and Diabetic Remission in Cats
- Container/year: Veterinary Clinics of North America: Small Animal Practice / 2023
- DOI landing: https://doi.org/10.1016/j.cvsm.2023.02.001
- Primary URL: https://linkinghub.elsevier.com/retrieve/pii/S0195561623000207
- Full-text/TDM links: https://api.elsevier.com/content/article/PII:S0195561623000207?httpAccept=text/xml (text/...; https://api.elsevier.com/content/article/PII:S0195561623000207?httpAccept=text/plain (tex...
- License URLs: https://www.elsevier.com/tdm/userlicense/1.0/; https://www.elsevier.com/legal/tdmrep-license; +5 more
- HEAD probes: https://api.elsevier.com/content/article/PII:S0195561623000207?httpAccept=text/xml -> 200...; https://api.elsevier.com/content/article/PII:S0195561623000207?httpAccept=text/plain -> H...
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-diabetes-050`

- Title: ISFM Consensus Guidelines on the Practical Management of Diabetes Mellitus in Cats
- Container/year: Journal of Feline Medicine and Surgery / 2015
- DOI landing: https://doi.org/10.1177/1098612x15571880
- Primary URL: https://journals.sagepub.com/doi/10.1177/1098612X15571880
- Full-text/TDM links: https://journals.sagepub.com/doi/pdf/10.1177/1098612X15571880 (application/pdf, text-mini...; https://journals.sagepub.com/doi/full-xml/10.1177/1098612X15571880 (application/xml, text...; +1 more
- License URLs: https://journals.sagepub.com/page/policies/text-and-data-mining-license
- HEAD probes: https://journals.sagepub.com/doi/pdf/10.1177/1098612X15571880 -> HTTP 403; https://journals.sagepub.com/doi/full-xml/10.1177/1098612X15571880 -> HTTP 403
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-diabetes-087`

- Title: 2018 AAHA Diabetes Management Guidelines for Dogs and Cats*
- Container/year: Journal of the American Animal Hospital Association / 2018
- DOI landing: https://doi.org/10.5326/jaaha-ms-6822
- Primary URL: https://jaaha.kglmeridian.com/view/journals/aaha/54/1/article-p1.xml
- Full-text/TDM links: https://jaaha.kglmeridian.com/view/journals/aaha/54/1/article-p1.xml (text/html, text-min...; http://meridian.allenpress.com/jaaha/article-pdf/54/1/1/1329462/jaaha-ms-6822.pdf (applic...; +2 more
- License URLs: https://creativecommons.org/licenses/by-nc-nd/4.0/
- HEAD probes: https://jaaha.kglmeridian.com/view/journals/aaha/54/1/article-p1.xml -> 200 (text/html, l...; http://meridian.allenpress.com/jaaha/article-pdf/54/1/1/1329462/jaaha-ms-6822.pdf -> HTTP...
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-diabetes-091`

- Title: Survival, remission, and quality of life in diabetic cats
- Container/year: Journal of Veterinary Internal Medicine / 2023
- DOI landing: https://doi.org/10.1111/jvim.16625
- Primary URL: https://academic.oup.com/jvim/article/37/1/58/8448017
- Full-text/TDM links: https://onlinelibrary.wiley.com/doi/pdf/10.1111/jvim.16625 (application/pdf, text-mining); https://onlinelibrary.wiley.com/doi/full-xml/10.1111/jvim.16625 (application/xml, text-mi...; +2 more
- License URLs: https://creativecommons.org/licenses/by-nc-nd/4.0/; http://creativecommons.org/licenses/by/4.0/
- HEAD probes: https://onlinelibrary.wiley.com/doi/pdf/10.1111/jvim.16625 -> HTTP 403; https://onlinelibrary.wiley.com/doi/full-xml/10.1111/jvim.16625 -> HTTP 403
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-obesity-001`

- Title: Feline obesity - prevalence, risk factors, pathogenesis, associated conditions and assessment: a review
- Container/year: Veterinární medicína / 2016
- DOI landing: https://doi.org/10.17221/145/2015-vetmed
- Primary URL: http://vetmed.agriculturejournals.cz/doi/10.17221/145/2015-VETMED.html
- Full-text/TDM links: http://vetmed.agriculturejournals.cz/doi/10.17221/145/2015-VETMED.pdf (unspecified, simil...
- License URLs: https://creativecommons.org/licenses/by-nc/4.0/
- HEAD probes: http://vetmed.agriculturejournals.cz/doi/10.17221/145/2015-VETMED.pdf -> 200 (application...
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-obesity-004`

- Title: Overweight and obesity in domestic cats: epidemiological risk factors and associated pathologies
- Container/year: Journal of Feline Medicine and Surgery / 2024
- DOI landing: https://doi.org/10.1177/1098612x241285519
- Primary URL: https://journals.sagepub.com/doi/10.1177/1098612X241285519
- Full-text/TDM links: https://journals.sagepub.com/doi/pdf/10.1177/1098612X241285519 (application/pdf, text-min...; https://journals.sagepub.com/doi/full-xml/10.1177/1098612X241285519 (application/xml, tex...; +1 more
- License URLs: https://creativecommons.org/licenses/by-nc/4.0/
- HEAD probes: https://journals.sagepub.com/doi/pdf/10.1177/1098612X241285519 -> HTTP 403; https://journals.sagepub.com/doi/full-xml/10.1177/1098612X241285519 -> URLError: <urlopen...
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-obesity-005`

- Title: Identifying the target population and preventive strategies to combat feline obesity
- Container/year: Journal of Feline Medicine and Surgery / 2024
- DOI landing: https://doi.org/10.1177/1098612x241228042
- Primary URL: https://journals.sagepub.com/doi/10.1177/1098612X241228042
- Full-text/TDM links: https://journals.sagepub.com/doi/pdf/10.1177/1098612X241228042 (application/pdf, text-min...; https://journals.sagepub.com/doi/full-xml/10.1177/1098612X241228042 (application/xml, tex...; +1 more
- License URLs: https://creativecommons.org/licenses/by/4.0/
- HEAD probes: https://journals.sagepub.com/doi/pdf/10.1177/1098612X241228042 -> HTTP 403; https://journals.sagepub.com/doi/full-xml/10.1177/1098612X241228042 -> HTTP 403
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-obesity-008`

- Title: Insulin Sensitivity Decreases with Obesity, and Lean Cats with Low Insulin Sensitivity are at Greatest Risk of Glucose Intolerance with Weight Gain
- Container/year: Journal of Feline Medicine and Surgery / 2001
- DOI landing: https://doi.org/10.1053/jfms.2001.0138
- Primary URL: https://journals.sagepub.com/doi/10.1053/jfms.2001.0138
- Full-text/TDM links: https://journals.sagepub.com/doi/pdf/10.1053/jfms.2001.0138 (application/pdf, text-mining); https://journals.sagepub.com/doi/full-xml/10.1053/jfms.2001.0138 (application/xml, text-m...; +1 more
- License URLs: https://journals.sagepub.com/page/policies/text-and-data-mining-license
- HEAD probes: https://journals.sagepub.com/doi/pdf/10.1053/jfms.2001.0138 -> HTTP 403; https://journals.sagepub.com/doi/full-xml/10.1053/jfms.2001.0138 -> HTTP 403
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-obesity-080`

- Title: Effects of weight loss with a moderate-protein, high-fiber diet on body composition, voluntary physical activity, and fecal microbiota of obese cats
- Container/year: American Journal of Veterinary Research / 2018
- DOI landing: https://doi.org/10.2460/ajvr.79.2.181
- Primary URL: https://avmajournals.avma.org/view/journals/ajvr/79/2/ajvr.79.2.181.xml
- Full-text/TDM links: https://avmajournals.avma.org/view/journals/ajvr/79/2/ajvr.79.2.181.xml (text/html, text-...; https://avmajournals.avma.org/downloadpdf/journals/ajvr/79/2/ajvr.79.2.181.xml (text/html...; +1 more
- License URLs: none in Crossref metadata
- HEAD probes: https://avmajournals.avma.org/view/journals/ajvr/79/2/ajvr.79.2.181.xml -> HTTP 403; https://avmajournals.avma.org/downloadpdf/journals/ajvr/79/2/ajvr.79.2.181.xml -> 200 (ap...
- Next action: full-text/TDM link present; verify access before deep extraction
