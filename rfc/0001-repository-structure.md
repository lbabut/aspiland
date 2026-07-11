# RFC 0001 — Preserve the dream, separate the law from the scratchpad

Status: Accepted  
Accepted: 2026-07-11  
Decision record: PR #1  
Effective: 2026-07-11

## Purpose

Aspiland already contains law, identity, experiments, public communication and software. This RFC introduces a structure that preserves the entire history while making it clear which documents are binding, proposed, experimental, archival or safe for public distribution.

## Accepted top-level structure

- `/canon` — currently binding constitutional and governance documents.
- `/rfc` — proposed changes and decision records.
- `/projects` — experiments, software and research projects.
- `/archive` — preserved legacy material and superseded documents.
- `/protocols` — procedures for consent, voting, amendment, rollback, backups and verification.
- `/public` — material intentionally prepared for unrestricted public distribution.

## Migration principles

1. Nothing from the existing repository is deleted during the first phase.
2. Existing documents remain historical evidence even when replaced.
3. A document becomes canonical only through an explicit review and acceptance process.
4. Satire, fiction, experiments and binding rules must be clearly distinguishable.
5. Personal data must not be made eternal merely because it was committed.
6. Every future structural migration must be reversible.

## First project under the new structure

`UNIVERSE / MERCY` is the first project organized under `/projects`. It explores safe governance for hypothetical technologies capable of highly consequential interventions in complex systems.

## Decision

Accepted through merged PR #1. This decision accepts the directory model and migration principles; it does not automatically declare any legacy document canonical.
