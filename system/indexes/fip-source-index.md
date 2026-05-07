# FIP Source Index

## Seed Corpus

| ID | Title | Primary Layer | Evidence Level | Status |
|---|---|---|---|---|
| src-fip-001 | Chapter 10 - Feline Infectious Peritonitis (Feline Coronavirus) | mechanism | review | deep-extracted; full source-card depth |
| src-fip-002 | Changes in some acute phase protein and immunoglobulin concentrations in cats affected by feline infectious peritonitis or exposed to feline coronavirus infection | endpoint | original-study | deep-extracted; full source-card depth |
| src-fip-003 | A review of feline infectious peritonitis virus infection | mechanism | review | deep-extracted; full source-card depth |
| src-fip-004 | Feline infectious peritonitis: insights into feline coronavirus pathobiogenesis and epidemiology based on genetic analysis of the viral 3c gene | mechanism | original-study | deep-extracted; full source-card depth |
| src-fip-005 | Risk factors for feline infectious peritonitis in Australian cats | recognition | original-study | deep-extracted; full source-card depth |
| src-fip-006 | Clinicopathological findings associated with feline infectious peritonitis in Sydney, Australia: 42 cases (1990–2002) | recognition | case-series | deep-extracted; full source-card depth |
| src-fip-007 | Immunologic phenomena in the effusive form of feline infectious peritonitis | mechanism | original-study | deep-extracted; full source-card depth |
| src-fip-008 | Risk factors for feline infectious peritonitis among cats in multiple-cat environments with endemic feline enteric coronavirus | recognition | original-study | deep-extracted; full source-card depth |
| src-fip-009 | Feline Infectious Peritonitis Viruses Arise by Mutation from Endemic Feline Enteric Coronaviruses | mechanism | original-study | deep-extracted; full source-card depth |
| src-fip-010 | Limitations of using feline coronavirus spike protein gene mutations to diagnose feline infectious peritonitis | endpoint | original-study | deep-extracted; full source-card depth |
| src-fip-011 | Serologic Studies of Naturally Occurring Feline Infectious Peritonitis | endpoint | original-study | deep-extracted; full source-card depth |
| src-fip-012 | Prevalence of feline infectious peritonitis in specific cat breeds | recognition | original-study | deep-extracted; full source-card depth |
| src-fip-013 | Long-term follow-up of cats in complete remission after treatment of feline infectious peritonitis with oral GS-441524 | translation | case-series | deep-extracted; full source-card depth |
| src-fip-014 | Feline infectious peritonitis epizootic caused by a recombinant coronavirus | mechanism | original-study | deep-extracted; full source-card depth |
| src-fip-015 | Clinicopathological findings and disease staging of feline infectious peritonitis: 51 cases from 2003 to 2009 in Taiwan | recognition | case-series | deep-extracted; full source-card depth |
| src-fip-016 | Efficacy and safety of the nucleoside analog GS-441524 for treatment of cats with naturally occurring feline infectious peritonitis | translation | original-study | deep-extracted; full source-card depth |
| src-fip-017 | The nucleoside analog GS-441524 strongly inhibits feline infectious peritonitis virus in tissue culture and experimental cat infection studies | translation | original-study | deep-extracted; full source-card depth |
| src-fip-018 | Amino acid changes in the spike protein of feline coronavirus correlate with systemic spread of virus from the intestine and not with feline infectious peritonitis | mechanism | original-study | deep-extracted; full source-card depth |
| src-fip-019 | Thirty-two cats with effusive or non-effusive feline infectious peritonitis treated with a combination of remdesivir and GS-441524 | translation | case-series | deep-extracted; full source-card depth |
| src-fip-020 | Epidemiology of feline infectious peritonitis among cats examined at veterinary medical teaching hospitals | recognition | original-study | deep-extracted; full source-card depth |
| src-fip-021 | Morphogenesis of a virus in cats with experimental feline infectious peritonitis | mechanism | original-study | deep-extracted; full source-card depth |
| src-fip-022 | Detection of feline coronavirus spike gene mutations as a tool to diagnose feline infectious peritonitis | endpoint | original-study | deep-extracted; full source-card depth |
| src-fip-023 | Detection of feline coronavirus in cerebrospinal fluid for diagnosis of feline infectious peritonitis in cats with and without neurological signs | endpoint | original-study | deep-extracted; full source-card depth |
| src-fip-024 | Antiviral treatment using the adenosine nucleoside analogue GS-441524 in cats with clinically diagnosed neurological feline infectious peritonitis | translation | original-study | deep-extracted; full source-card depth |

## First-Pass Reading Priorities

### Tier A

- `src-fip-003`
- `src-fip-009`
- `src-fip-016`
- `src-fip-019`
- `src-fip-024`
- `src-fip-004`

### Tier B

- `src-fip-005`
- `src-fip-006`
- `src-fip-010`
- `src-fip-015`
- `src-fip-018`
- `src-fip-022`
- `src-fip-008`
- `src-fip-017`
- `src-fip-023`
- `src-fip-013`

## Notes

- `ingested` means a first source card already exists in `raw/papers/`
- `deep-extracted` means a round-1 extraction worksheet now exists in `system/indexes/`

## Current Status Note

The FIP source-card layer is now complete across the current 24-source seed corpus, deep extraction covers the full seed set, and all 24 paper cards are explicit `extraction_depth: full`.

That means the next gains should come from:

- full-text / image-table precision where it changes branch order
- official-source regulatory checks where route status changes
- better endpoint, diagnostic, and treatment compression only where control-layer pressure remains real

For card-level depth detail, use:

- [FIP source depth map](fip-source-depth-map.md)
