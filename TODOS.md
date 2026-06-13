# TODOS

## Research Cases

### Add semantic claim entailment evaluation

**What:** Build and validate a semantic evaluator that distinguishes support,
contradiction, uncertainty, and irrelevance for atomic feline research claims.

**Why:** The current lexical matcher can return the same result for positive and
negated claims and cannot safely set reviewed evidence dispositions.

**Context:** Release 1 uses the matcher only to retrieve candidate evidence. Start
with a blinded golden set containing positive/negative claim pairs, species and
applicability boundaries, source-depth variation, and abstention cases. Promotion
to gate credit requires measured error thresholds and human review.

**Effort:** L
**Priority:** P2
**Depends on:** Research Case Evidence schema and a completed CKD pilot

### Add authenticated identity and reliable signing

**What:** Add authenticated users, role separation, immutable signed snapshots,
and explicit signature invalidation.

**Why:** Typed actor names in the local app are self-asserted and cannot support
independent review, nonrepudiation, or final decision signing.

**Context:** Release 1 labels reviewer actions as unverified attestations and does
not render Recommend or Sign. Revisit only when there is a real multi-user
deployment and a defined legal/compliance requirement.

**Effort:** XL
**Priority:** P2
**Depends on:** Persistent deployment, authentication architecture, Research Case revision model

### Reassess storage after measured scale

**What:** Benchmark the per-case JSON store and decide whether to migrate to
SQLite or a service database.

**Why:** A database adds operational complexity now, but file size, multi-user
contention, or remote deployment may eventually exceed the local store.

**Context:** Trigger reassessment if the performance budget fails at 100 cases,
1,000 revisions per case, or 10,000 evidence links, or when more than one trusted
user must write remotely. Preserve the schema and revision semantics during any
migration.

**Effort:** M
**Priority:** P3
**Depends on:** Release 1 performance measurements and adoption evidence

## Completed
