# Research Case Schema

Schema version: `1`

## Authority Boundary

Research Cases organize evidence and human attestations. They do not issue
automatic recommendations or signatures.

Release 1 actor identity:

`identity_assurance: self_asserted`

## Durable Record

Each case is stored at:

`system/research-cases/<case-id>.json`

The record contains:

- current projection;
- monotonic revision;
- immutable revision snapshots and SHA-256 content hashes;
- append-only audit events;
- Frame, Criteria, Claims/Evidence, Challenges, blockers, gaps, assumptions,
  and legacy attachments.

## Stage State

Stage state is derived, never directly edited:

```text
progress  = not_started | in_progress | blocked | complete
freshness = current | stale
```

A stage can be both blocked and stale.

## Invalidation

- Semantic Frame changes stale Criteria, Evidence, and Challenge.
- Administrative Frame changes do not stale evidence.
- Frozen Criteria changes stale Evidence and Challenge.
- Evidence/claim changes stale Challenge.
- Challenge replacement clears Challenge staleness only.

## Write Protocol

Every write requires:

- expected revision;
- actor label;
- reason;
- idempotent operation ID.

The store acquires a per-case advisory lock, reloads the record, checks the
expected revision, writes a same-directory temporary file, flushes and fsyncs
it, replaces the case file atomically, then fsyncs the directory.

Corrupt and unsupported records fail closed.
