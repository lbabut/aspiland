# RFC 0006 — Data lifecycle and privacy baseline

Status: Proposed  
Proposed: 2026-07-12

## Purpose

Adopt a repository-wide baseline for classifying, collecting, storing, publishing, retaining, exporting and deleting data without treating permanent public exposure as the default.

## Proposed change

Accept `protocols/data-lifecycle.md` as the operational data lifecycle protocol after review and an explicit effective date.

The protocol introduces:

- public, participant-private, restricted operational, generated runtime, archival and prohibited data classes;
- a required record for persistent datasets and stores;
- data minimization and purpose definition;
- least-privilege access and periodic review;
- publication review for privacy, credentials, licensing and context;
- retention periods or explicit review triggers;
- access, correction, export, restriction and deletion request paths;
- private incident reporting and sanitized follow-up;
- backup, history and automated-system safeguards.

## Affected people and systems

- repository contributors and maintainers;
- participants whose information may be processed;
- active and legacy software projects;
- public documentation and archives;
- backups, logs, exports and external processors;
- automated systems assisting with classification, publication or deletion.

## Immediate motivating findings

The pre-launch audit found a public legacy JSON record indexed for contact-data fields in a directory explicitly marked for deletion. The repository also contains historical user areas, chat material, generated artifacts and operational experiments whose purpose and retention have not been consistently documented.

## Risks

- classification may be applied inconsistently;
- deletion promises may exceed technical capability in Git, forks or backups;
- excessive process may obstruct small experiments;
- archival interests may conflict with privacy and dignity;
- automated classification may produce false positives or miss sensitive context.

## Safeguards

- proportional requirements based on data sensitivity and persistence;
- honest documentation of technical deletion limits;
- human review for consequential publication, deletion and identity linkage;
- private handling of incident evidence;
- periodic review and explicit dataset ownership;
- no diagnostic disclosure requirement when a functional preference is sufficient.

## Migration

If accepted:

1. inventory persistent datasets and stores using the protocol's dataset record;
2. prioritize `users/`, `PublicChat.txt`, `Embassies/`, `SharedAssets/`, runtime outputs and build artifacts;
3. classify active project data and identify owners;
4. establish retention, access, backup and deletion procedures;
5. move reviewed public material to `public/` where helpful;
6. record unresolved historical-data decisions without reproducing sensitive content;
7. re-evaluate go-live readiness.

## Rollback

Supersede or suspend the protocol through change control. Existing incident-containment, deletion and confidentiality commitments remain in effect until data is safely migrated or disposed of.

## Decision record

No decision yet. Merging this RFC or the draft protocol does not activate it. Acceptance requires explicit approval and an effective date.
