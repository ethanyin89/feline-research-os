# Handoff: II-Commons-Skills Research OS Direction

**Date:** 2026-06-06  
**Status:** Conceptual review completed; this model lane stopped at its usage limit while the project continued through another model

## Why This Handoff Exists

This document restores the missing June 6 timeline represented by
[the archived June 6 source](system/handoffs/source-materials/2026-06-06-raw-2.md).

The June 6 discussion was not primarily a CKD content-processing session. It
examined II-Commons-Skills and related Intelligent Internet materials to clarify
how `feline-research-os` could evolve from a Streamlit question-answering surface
into a durable, evidence-grounded Research OS.

The existing
[HANDOFF-2026-06-06-CKD-MATERIAL-COMPLETION.md](HANDOFF-2026-06-06-CKD-MATERIAL-COMPLETION.md)
remains valid for the separate CKD material work completed on the same date.

## Source Readability Audit

The June 6 II / II-Commons analysis is still directly readable as original
source material, not only through a later summary.

| Check | Result |
|---|---|
| Original path | `/Users/jiawei/Desktop/raw-2.md` |
| Original creation time | `2026-06-06 15:15:10 +0800` |
| Original modification time | `2026-06-06 15:15:10 +0800` |
| Length | 1,448 lines; 92,833 bytes |
| SHA-256 | `c2723f0d8a38d4c68a9bb59f161d3ec69eb3a594d7acb7b3ed0c1862df181ed8` |
| Repository archive | [system/handoffs/source-materials/2026-06-06-raw-2.md](system/handoffs/source-materials/2026-06-06-raw-2.md) |
| Archive verification | Byte-for-byte identical to the Desktop source on 2026-06-11 |

Future agents should read the repository archive first. The Desktop file is the
provenance source, but it is outside version control and may be moved or deleted.

### Recovery Boundary

A second file, `260606-handoff(1).md`, is named in the June 8/9 continuation
record as a 534-line handoff provided on June 6. That original file was not found
on the Desktop or in this repository during the 2026-06-11 audit.

Its ideas are partially recoverable from:

- [HANDOFF-2026-06-08-CKD-EVIDENCE-GAP-REVIEW.md](HANDOFF-2026-06-08-CKD-EVIDENCE-GAP-REVIEW.md),
  which records its product positioning, six-layer architecture, schemas, and
  P0/P1/P2 priorities;
- [ARCHITECTURE.md](ARCHITECTURE.md);
- [PLAN-chatacademia-research-workbench.md](PLAN-chatacademia-research-workbench.md).

Do not describe `260606-handoff(1).md` as fully recovered unless the original
534-line file is found and archived. The full `raw-2.md` source is verified;
the companion handoff is currently recoverable only through later derived
artifacts.

## June 6 Discussion

### 1. II-Commons-Skills as the Retrieval Reference

II-Commons-Skills was treated as a reference for deterministic agent retrieval,
not as a chatbot or a model to copy wholesale.

The useful product ideas were:

- search authoritative corpora before synthesis;
- expose the retrieval scope and cutoff;
- preserve canonical identifiers such as PMID, PMCID, and DOI;
- package repeatable research actions as skills;
- return ranked evidence cards, a quick domain map, and concrete next research
  moves instead of an unstructured answer.

The direct mapping proposed for this repository was a family of feline research
skills such as literature review, disease-model review, PK design, protocol
writing, and regulatory-gap assessment.

### 2. Research Record as the Durable Unit

The CommonGround Kernel material shifted the design target from saving final
answers to preserving the public facts of research work.

The minimum proposed record included:

- original request;
- retrieval scope and sources searched;
- included and excluded evidence;
- reasons for evidence selection;
- decisions and uncertainties;
- generated output;
- next moves;
- handoff summary for the next person or agent.

This became the conceptual basis for `Research Record` and `Evidence Card`.

### 3. Retrieval Must Be Cheap and Repeated

The `psql_bm25s` discussion reinforced that long-running research work is limited
by retrieval of accumulated state, not only by model context length.

The June 6 recommendation was deliberately conservative:

- keep the existing file-first system initially;
- use structured Markdown/JSON records and lightweight search;
- separate stable knowledge from active, unverified additions;
- defer PostgreSQL-native BM25, a vector store, and other infrastructure until
  scale or concurrency demonstrates the need.

### 4. Add a Harness, Not Just More Prompts

RALPH and Zenith were used to identify premature completion as a central failure
mode for veterinary research tasks.

The proposed Feline-RALPH loop was:

```text
draft -> gap check -> revision -> independent verification -> final -> save record
```

The verifier was expected to check at least:

- feline species boundaries and unmarked cross-species extrapolation;
- evidence support and citation coverage;
- endpoint-type distinctions;
- protocol completeness;
- unresolved uncertainty and stopping conditions.

### 5. Six-Layer Research OS Direction

By the end of the discussion, the proposed architecture had converged on:

1. Human-in-the-loop Research Workspace
2. Professional Team Mode
3. Research Pipeline
4. Research Record
5. Retrieval Memory
6. Data Quality and Verification

The intended product was a feline research thinking environment where the user
could inspect, correct, resume, and reuse research work, not an autonomous system
that silently made scientific or commercial decisions.

## Autoplan Decision Record

| Decision | Classification | Reason |
|---|---|---|
| Record this as a June 6 historical handoff | Mechanical | `raw-2.md` and later handoffs identify June 6 as the source session |
| Keep the CKD handoff separate | Mechanical | The two June 6 workstreams had different scope and completion states |
| Treat II-Commons-Skills as a design reference, not a completed integration | Mechanical | No June 6 implementation or verified live integration is documented |
| Prefer file-first Research Records before new retrieval infrastructure | Mechanical | Matches the repository architecture and avoids premature infrastructure |
| Require human review and independent verification | Product boundary | Research outputs can affect scientific and business decisions |
| Do not attribute June 9 implementation to June 6 | Timeline correction | Architecture and harness code were created during the later continuation |

## Usage-Limit Handoff Point

The June 6 session ended after the conceptual synthesis and proposed architecture.
Codex usage was insufficient for that model to continue its assigned lane.
This did not pause the project. The operating model was to preserve the current
lane, hand off its exact state, and let a new model continue a different or
complementary part of the project.

At that point:

- the II-Commons-Skills and related materials had been mapped to the project;
- the Research Record, Evidence Card, retrieval-memory, and harness-loop concepts
  had been proposed;
- no completed II-Commons-Skills integration should be claimed;
- no June 9 code or benchmark result existed yet in this timeline;
- the stopped lane needed to remain recoverable without blocking other project
  work;
- the next model could continue another workstream, provided it recorded its own
  scope and did not overwrite unresolved decisions from this lane.

### Project Continuity Rule

`Usage exhausted` means `one model lane stops`, not `the project stops`.

Every usage-limit handoff must preserve:

1. the original inputs and source files;
2. what that model actually read;
3. completed outputs and verification performed;
4. the exact unfinished boundary;
5. files changed and files intentionally left untouched;
6. the next safe action for the same lane;
7. parallel work that another model may perform;
8. the future merge or reconciliation point.

New models should take a bounded, non-conflicting workstream when possible. They
must not infer that all project work is suspended merely because one model ran
out of usage.

## Later Continuation, Not June 6 Work

On 2026-06-09, another model continued this direction and converted it into
repository artifacts, including:

- [ARCHITECTURE.md](ARCHITECTURE.md);
- [PLAN-chatacademia-research-workbench.md](PLAN-chatacademia-research-workbench.md);
- Research Record and Evidence Card schemas;
- the harness-loop, verifier, UI, and benchmark work described in
  [HANDOFF-2026-06-09-CHATACADEMIA-CONTENT.md](HANDOFF-2026-06-09-CHATACADEMIA-CONTENT.md).

Those files are implementation follow-through from the June 6 discussion by a
later model lane. They must not be represented as completed on June 6, but they
also demonstrate that the project continued while the original Codex lane was
unavailable.

## Resume Instructions

For historical or product-direction work:

1. Read this handoff.
2. Read
   [system/handoffs/source-materials/2026-06-06-raw-2.md](system/handoffs/source-materials/2026-06-06-raw-2.md)
   for the full, byte-verified source discussion.
3. Read [PLAN-business-critical-feline-research-os.md](PLAN-business-critical-feline-research-os.md)
   for the June 6 authority-boundary review.
4. Read the June 9 architecture and handoff for the later implementation.
5. Check [HANDOFF.md](HANDOFF.md) and the newest authoritative worktree handoff
   before editing code; later repository reality supersedes historical completion
   claims.

## Guardrails

- Do not describe external II projects as installed project dependencies unless
  the live repository proves that integration.
- Do not replace the existing evidence vault with a new platform merely because
  an external architecture is attractive.
- Do not let generated readiness labels become scientific, clinical, investment,
  or commercial decisions.
- Preserve source identifiers, exclusions, uncertainty, counterevidence, and
  human review in any continuation.
