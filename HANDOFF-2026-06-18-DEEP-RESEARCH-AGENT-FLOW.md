# 2026-06-18 Deep Research Agent Flow Handoff

## 1. Task Classification

This task should be treated as a **方案评审 with an embedded 排查 result**, not as a normal feature implementation task.

The original trigger was an investigation: a test of `https://agent.ii.inc/` using the query:

> search the latest papers about feline HCM, prioritize high-impact journals, and summarize findings, methods, and clinical relevance

The investigation found a concrete failure: the delivered report claimed no 2026 feline HCM original papers were found through 2026-06-18, but multiple 2026 counterexamples were later identified. That part is 排查.

The current user direction has moved one layer up. The important question is now:

> What should a trustworthy deep research agent do, show, and record when it turns a short user request into a research deliverable?

That makes the current stage a product/process design review.

## 2. Current Stage

We are **not** currently re-researching feline HCM itself.

We are using the feline HCM test as a case study to design and evaluate a deep research workflow. The repo already has substantial research-mode and presentation-layer work. The next meaningful step is to encode the lessons from this case into the research agent's contract, progress model, evidence audit model, and acceptance checks.

The current stage can be summarized as:

> Move from "the agent looked like it worked hard" to "the research decisions and final claims are auditable."

## 3. User's New Observations To Preserve

The user noted several first-read insights from `/Users/jiawei/Desktop/深度研究的thought 路径.md`. These are important because they identify the real shape of the workflow, not just the final bug.

### 3.1 The Agent Did Not Search Immediately

The agent first decomposed one sentence into four concrete tasks:

1. determine research time range;
2. limit the disease object;
3. determine source priority;
4. design the final report form.

This is a positive signal. It shows the system is not merely doing keyword search; it is converting a vague user request into a research contract.

The product implication is that the UI should expose this contract briefly before or during execution:

- time range;
- disease/topic boundary;
- source hierarchy;
- deliverable type;
- promised output fields.

### 3.2 The Workflow Was Deliverable-Oriented From The Start

The agent planned a Typst/PDF report and CSV early. This helps control the output, but it also has a risk: report formatting and file engineering may interfere with research design too early.

The right guardrail is not to remove deliverable planning. The right guardrail is to split it into two stages:

- early deliverable sketch: useful for scoping;
- final deliverable freeze: only allowed after freshness, inclusion, and evidence audit checks pass.

### 3.3 "High-Impact Journals" Requires An Explicit Standard

The thought path noticed that feline HCM papers cluster in specialty veterinary journals. This matters because "high-impact" cannot be interpreted like a broad biomedical topic.

In a niche veterinary domain, these three goals can conflict:

- latest;
- highest journal impact;
- direct clinical relevance.

The agent's practical solution was to use themed representative selection: genetics, diagnosis, biomarkers, and treatment. That is more reasonable than sorting only by impact factor.

But the final system must make this explicit. If no JCR, Scimago, CiteScore, or Clarivate verification is performed, the agent should downgrade the wording from "high-impact" to something like:

> higher-visibility and clinically relevant journals within the feline HCM literature.

### 3.4 The Agent Weighted Papers Unequally

The agent did not give every paper equal attention. It planned deeper extraction for papers that were clinically relevant, methodologically complex, or important for negative results.

This is desirable. Good research synthesis is not an equal-length abstract generator.

The missing control is a record of why a paper received high, medium, or low attention. A later reviewer should be able to tell whether deeper treatment was justified by:

- sample size;
- clinical directness;
- method complexity;
- novelty;
- negative result importance;
- representativeness for a topic;
- contribution to a key claim in the report.

### 3.5 The Paper Set Changed Iteratively

The number and identity of papers changed across the thought path. This shows a recursive research process:

1. initial search;
2. tentative paper set;
3. evidence gap discovery;
4. revised query or inclusion rule;
5. adjusted report structure;
6. renewed evidence check.

This is closer to real research than a one-shot search-and-summary pipeline.

The risk is scope drift: "I saw this, so I included it." The system needs a scope-change ledger for every added or removed paper.

## 4. Main Product Judgment

The key product problem is not whether to show the 43-step thought path.

The key product problem is how to make a recursive research process trustworthy without exposing raw internal monologue as the main trust signal.

A better structure has three layers:

1. **Simple Progress Layer** for normal users.
   - Example: define scope, collect sources, synthesize evidence, produce report.

2. **Research Decision Layer** for expert users.
   - Shows search boundaries, inclusion/exclusion changes, paper weighting, source hierarchy, and unresolved gaps.

3. **Evidence Audit Layer** for verification.
   - Maps every final claim to source rows, extraction fields, dates, and freshness checks.

The current ii.inc example has layer 1 and a raw version of layer 2. It is missing the clean, structured layer 3.

## 5. Core Failure From The Case Study

The strongest verified failure remains freshness validation.

The report and CSV covered 2023-2025 papers but claimed coverage through 2026-06-18. Later validation found multiple 2026 feline HCM papers, including JVIM, Animals, Veterinary Sciences, and JFMS records.

This means the failure was not only a missed citation. It was a broken acceptance gate for the word "latest."

The system should never treat an internal corpus cutoff as proof of live database coverage. A claim like "no 2026 papers found" needs a separate current-year search, source date, query string, and ideally a second-source check.

## 6. Required Control Points

### 6.1 Research Contract

Every deep research run should start with a structured contract:

- user request;
- interpreted topic;
- time range;
- source hierarchy;
- definition of "latest";
- definition of "high-impact" or explicit downgrade;
- deliverable format;
- required extraction fields;
- current-date assumptions.

### 6.2 Standard Conversion Ledger

The system should record each conversion:

- user language requirement -> search boundary;
- search boundary -> inclusion/exclusion criteria;
- inclusion criteria -> extraction fields;
- extraction fields -> report sections;
- report sections -> acceptance checks.

This ledger is more useful than raw thought for later review.

### 6.3 Scope Drift Ledger

Every paper-set change should be recorded with a reason:

- new query found it;
- citation chaining found it;
- current-year freshness check found it;
- high clinical relevance;
- high methodological relevance;
- representative for a topic;
- negative result worth preserving;
- excluded for weak directness;
- excluded because review/non-original;
- excluded because not feline-specific.

### 6.4 Evidence Weighting Record

The agent should not analyze every paper equally, but unequal attention must be auditable.

Suggested weighting fields:

- clinical directness;
- journal/source credibility;
- sample/model relevance;
- method complexity;
- recency;
- claim centrality;
- limitation severity.

### 6.5 Freshness Gate

For any query containing "latest", "recent", "current", "new", "through today", or date-sensitive equivalents:

- run a current-year query separately;
- search by topic terms and likely synonyms;
- check PubMed plus official journal/source pages when possible;
- sort by publication date and electronic publication date;
- distinguish "not found in this source" from "does not exist";
- block final "no papers found" language unless the audit log supports it.

### 6.6 Deliverable Freeze Gate

Typst/PDF/CSV generation should not freeze the research set until:

- search scope is logged;
- inclusion/exclusion decisions are logged;
- current-year freshness gate passes;
- high-impact wording is either verified or downgraded;
- main claims have evidence rows;
- CSV, report text, and references are consistent.

## 7. Product UI Implications

The screenshots from ii.inc suggest that users trust the system more when the visible process is detailed and concrete. That is directionally right, but raw detail is not enough.

Better presentation:

- For ordinary users: show four concise milestones.
- For advanced users: allow expanding "why these papers" and "what changed during screening."
- For audit users: provide a table-backed evidence trail.

Do not make the full 43-step internal path the default trust artifact. It is too verbose and contains implementation noise. The trust artifact should be a structured research trace.

## 8. Engineering Implications

The implementation should move toward explicit data structures rather than free-form progress text.

Candidate schemas:

- `ResearchContract`
- `SearchRun`
- `CandidatePaper`
- `ScreeningDecision`
- `ScopeChange`
- `ExtractionField`
- `EvidenceClaim`
- `ClaimEvidenceRow`
- `DeliverableManifest`
- `AcceptanceCheck`

Minimum acceptance checks:

- date-sensitive requests require live freshness validation;
- "no result" claims require query/source/date proof;
- high-impact claims require metric/source proof or downgraded wording;
- each top takeaway maps to one or more evidence rows;
- CSV/report/reference list consistency check passes;
- negative results are preserved when they affect interpretation;
- final deliverable states what it did not verify.

## 9. Recommended Next Step

Do not rewrite the feline HCM report first.

The next best step is to create a reproducible audit dataset for the 2026 counterexample set and the original 2023-2025 selected set.

Suggested file:

`2026-feline-hcm-audit.csv`

Suggested fields:

- title
- authors
- journal
- publication_date
- online_first_date
- DOI
- PMID
- source_url
- study_type
- population_or_model
- sample_size
- HCM_directness
- topic
- key_result
- clinical_relevance
- limitations
- include_status
- exclusion_reason
- found_by_query
- verified_on

After that, decide between three follow-up tracks:

1. revise the original report;
2. write a product/method article about deep research agents;
3. implement the audit layer inside the research-mode workflow.

## 10. Current Working Conclusion

The agent.ii.inc example is strong at research orchestration and document production. It also shows a genuinely useful recursive research pattern: the agent adjusts searches, paper selection, extraction depth, and report structure as it learns more.

Its weak point is not lack of effort. Its weak point is that recursive decisions are not converted into an auditable evidence trail, and date-sensitive claims can pass into the final report without independent freshness validation.

The product direction should therefore be:

> preserve the recursive research behavior, but require structured contracts, scope-change logs, evidence weighting, and freshness gates before the final report can claim authority.

