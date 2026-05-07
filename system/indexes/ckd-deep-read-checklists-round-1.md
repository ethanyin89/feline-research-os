# CKD Deep Read Checklists — Round 1

Use this when reading the Tier A papers.

Rule:

- do not try to summarize everything
- extract only material that can be promoted into topic pages or entity cards
- separate direct facts from your interpretation

## Shared Output Format

For each paper, capture:

1. `one_sentence_summary`
2. `quoted_fact`
3. `source_supported_conclusion`
4. `uncertainty_or_limit`
5. `candidate_entities`
6. `write_back_targets`

---

## src-ckd-004

**Title:** ISFM Consensus Guidelines on the Diagnosis and Management of Feline Chronic Kidney Disease

### Must Extract

- exact disease definition or framing language
- diagnostic workflow steps
- staging system names and criteria
- monitoring recommendations
- management recommendations by stage if present
- markers named as clinically important
- places where the guideline says something is consensus vs evidence-backed

### Nice To Have

- tables worth recreating in markdown
- explicit frequency recommendations for monitoring
- mention of owner communication / prognosis framing

### Can Skip For Round 1

- long background narrative
- detailed rationale for every minor recommendation

### Candidate `quoted_fact`

- “X is recommended for diagnosis/staging”
- “Y should be monitored at Z interval”
- “IRIS stage / guideline staging uses ...” if explicitly stated

### Candidate `source_supported_conclusion`

- which endpoints are core enough to promote into the endpoint handbook
- which management steps are baseline standard-of-care

### Write-Back Targets

- `topics/ckd/index.md`
- `topics/ckd/endpoint-handbook.md`
- `raw/papers/src-ckd-004.md`

---

## src-ckd-001

**Title:** Feline CKD: Pathophysiology and risk factors — what do we know?

### Must Extract

- named mechanisms of CKD injury/progression
- strongest risk factors listed
- whether the paper distinguishes initiation vs progression
- any feline-specific framing vs generic mammalian CKD framing
- any mechanistic gaps the authors explicitly call out

### Nice To Have

- diagrams you may want to reconstruct later
- cross-links between mechanisms and measurable endpoints

### Can Skip For Round 1

- broad literature-history narrative
- mechanisms discussed only in passing without relevance to feline CKD

### Candidate `quoted_fact`

- “Risk factors include ...”
- “Mechanisms implicated include ...”
- “Current evidence does not establish ...” if stated explicitly

### Candidate `source_supported_conclusion`

- which 3-5 mechanisms deserve first-class entity cards
- whether risk factor framing belongs in `mechanism-overview` or a later dedicated page

### Write-Back Targets

- `topics/ckd/mechanism-overview.md`
- `entities/mechanisms/aim.md`
- `entities/mechanisms/ugt1a6.md` only if truly relevant after reading
- `raw/papers/src-ckd-001.md`

---

## src-ckd-002

**Title:** Feline CKD: Diagnosis, staging and screening – what is recommended?

### Must Extract

- diagnostic criteria named explicitly
- screening candidates or risk-based screening logic
- primary biomarkers / markers
- staging approach
- how the paper frames early detection
- which endpoints are for diagnosis vs follow-up vs severity

### Nice To Have

- comparison between markers
- comments on sensitivity, specificity, limitations

### Can Skip For Round 1

- repeated background already covered in the guideline
- minor test descriptions with no downstream effect

### Candidate `quoted_fact`

- named biomarkers
- diagnostic thresholds if present
- screening recommendations if explicit

### Candidate `source_supported_conclusion`

- first version of the CKD endpoint shortlist
- separation of “core endpoints” vs “context endpoints”

### Write-Back Targets

- `topics/ckd/endpoint-handbook.md`
- `entities/endpoints/creatinine.md`
- `entities/endpoints/sdma.md`
- add new endpoint cards only if used repeatedly
- `raw/papers/src-ckd-002.md`

---

## src-ckd-003

**Title:** Feline CKD: Current therapies – what is achievable?

### Must Extract

- major therapy categories
- what outcomes therapies are trying to improve
- what the paper treats as realistic treatment goals
- where evidence is strong vs weak
- what is supportive care vs disease-modifying intent

### Nice To Have

- therapy-by-therapy evidence ranking
- explicit link between therapy and endpoint choice

### Can Skip For Round 1

- exhaustive detail on every minor intervention
- pharmacology detail that does not change planning

### Candidate `quoted_fact`

- “Current therapies include ...”
- “Goal of treatment is ...”
- “Evidence for X is limited / stronger” if stated clearly

### Candidate `source_supported_conclusion`

- first baseline treatment map for CKD translation layer
- early distinction between symptom control and progression control

### Write-Back Targets

- `topics/ckd/index.md`
- `topics/ckd/endpoint-handbook.md`
- `raw/papers/src-ckd-003.md`

---

## src-ckd-010

**Title:** Histomorphometry of Feline Chronic Kidney Disease and Correlation With Markers of Renal Dysfunction

### Must Extract

- study population / sample source
- pathology features measured
- renal dysfunction markers measured
- exact relationship between pathology and markers
- strongest and weakest correlations
- any statements on what markers fail to capture

### Nice To Have

- quantitative values worth keeping
- figure or table references worth translating into markdown

### Can Skip For Round 1

- methods detail that does not alter interpretation
- pathology sub-measures with no connection to the endpoint layer

### Candidate `quoted_fact`

- sample size and design
- named pathology variables
- named biochemical or functional markers
- explicit correlations

### Candidate `source_supported_conclusion`

- which measurable markers most plausibly reflect actual structural injury
- which endpoints may be over-trusted or under-trusted

### Write-Back Targets

- `topics/ckd/mechanism-overview.md`
- `topics/ckd/endpoint-handbook.md`
- `raw/papers/src-ckd-010.md`

---

## Round 1 Promotion Rules

Promote to topic pages only if one of these is true:

- the statement is directly quoted or paraphrased from a high-confidence source
- the statement is supported by at least 2 independent sources
- the statement is a clearly labeled `llm_inference`

Do not promote:

- vague “seems important” claims
- mechanistic speculation with no direct support in the paper
- endpoint importance claims based only on familiarity or convention
