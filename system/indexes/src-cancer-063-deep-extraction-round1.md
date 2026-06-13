---
id: src-cancer-063-deep-extraction-round1
type: system
topic: content-pipeline
last_compiled_at: 2026-06-09
verification_status: compiled
decision_grade: no
status: active
---

# Deep Extraction: src-cancer-063

## Source Metadata

| Field | Value |
|-------|-------|
| ID | src-cancer-063 |
| Title | Feline Alimentary Lymphomas: Established Concepts and an Underexplored Molecular Landscape |
| Authors | Szafron LA, Parys M, Parys M, Szafron LM |
| Year | 2026 |
| Journal | Current Issues in Molecular Biology |
| DOI | 10.3390/cimb48020218 |
| PMID | 41751480 |
| PMC | PMC12939859 |
| Evidence Level | Review |
| Citations in Vault | 8 |

## Extraction Summary

**Extraction method:** Europe PMC XML full-text retrieval
**Extraction date:** 2026-06-09
**Previous status:** abstract_weighted
**New status:** deep_extracted

## Key Quantitative Findings

### Survival Data

| Subtype | Median Survival | Range |
|---------|-----------------|-------|
| LGAL (SCL) | 800-1300 days | 19-29 months |
| HGAL | 1.5 months | Weeks to months |
| LGLL | 17 days | Days to weeks |
| EATL II equivalent | 2.4 years | — |

### Treatment Response

| Treatment | Response Rate | Tolerability |
|-----------|---------------|--------------|
| Chlorambucil + glucocorticoids | 69-96% | Well tolerated |
| CHOP protocol | Lower | Variable |

### Phenotype Distribution

- T-cell: 51 mentions (predominant)
- B-cell: 21 mentions
- T-cell represents ~84% of cases in some studies

### Risk Factors

| Factor | Association |
|--------|-------------|
| FeLV | 80-90% of thymic lymphoma |
| FIV | Positive correlation with AL |
| Helicobacter spp. | Chronic inflammation |
| Tobacco smoke | Environmental risk |

## Molecular Pathway Summary

| Pathway | Mentions | Relevance |
|---------|----------|-----------|
| JAK/STAT | 1 | Key oncogenic pathway |
| STAT5 | 11 | Dysregulated in AL |
| BCL family | 20 | Apoptosis regulation |
| TP53 | 3 | Tumor suppressor |
| NF-κB | 1 | Inflammatory pathway |

## Evidence Policy Additions

### New quoted_fact entries

1. "Median survival for LGAL (EATL II) is 19-29 months"
2. "Median survival for LGLL (EATL I subtype) is 17 days"
3. "Median survival times for SCL range from about 800 to 1300 days"
4. "Current standard of LGAL (SCL) care involves combination therapy with glucocorticoids and chlorambucil"
5. "Various dosing regimens yield response rates between 69% and 96%"
6. "80-90% of thymic lymphoma cats were positive for the FeLV antigen"
7. "The presence of FIV correlates positively with the development of AL"

### New source_supported_conclusion entries

1. "LGAL has dramatically better prognosis than HGAL: 19-29 months vs 17 days-1.5 months"
2. "Standard LGAL treatment (chlorambucil + glucocorticoids) yields 69-96% response rates"
3. "Comparative oncology: feline AL mirrors human EATL with shared pathway involvement"

## Comparative Oncology Matrix

| Feature | Feline AL | Human EATL |
|---------|-----------|------------|
| Low-grade type | LGAL/SCL | EATL II (MEITL) |
| High-grade type | HGAL | EATL I |
| T-cell predominant | Yes | Yes |
| JAK/STAT involvement | Yes | Yes |
| Enteropathy association | Yes | Yes (celiac) |

## Topic Page Impact

This source controls lymphoma.md section on alimentary lymphoma with:
- LGAL vs HGAL classification
- Survival statistics
- Treatment protocols
- Molecular pathway context
- IBD-lymphoma continuum discussion

## Follow-Up Actions

- [ ] Update topics/cancer/lymphoma.md with deep-extracted findings
- [ ] Consider adding IBD-lymphoma differential diagnosis section
- [ ] Link to JAK/STAT mechanism page if created
- [ ] Cross-reference with other lymphoma sources for consistency
