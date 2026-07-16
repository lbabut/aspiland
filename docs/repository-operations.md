# Repository operations and authority

Status: working operational policy; non-canonical  
Last reviewed: 2026-07-16

This document defines the operational baseline for maintaining and publishing the Aspiland repository. It does not create sovereignty, legal agency, binding community membership or authority to change canon outside the accepted process.

## Primary responsibility

- **Repository owner and legal principal:** `lbabut`.
- **Operational maintainer:** the authorized System Guardian acting within RFC 0005.
- **Recovery path:** follow `docs/recovery-checklist.md`; consequential account recovery, credential rotation, legal commitments, licensing and ownership changes remain with the repository owner or an explicitly authorized successor.

The owner retains platform and legal control. The operational maintainer may perform reversible maintenance, evidence gathering, drafting, triage and narrow emergency containment within the documented scope.

## Change classes

### Routine maintenance

Examples: link fixes, navigation, formatting, indexes, documentation clarity, generated-file cleanup after verification and non-canonical status updates.

Routine maintenance may be prepared, reviewed and merged by an authorized maintainer when:

- the change is reversible;
- no secret or unnecessary personal data is introduced;
- canon, ownership, licensing and legal commitments are unchanged;
- scope, validation and rollback are recorded in the pull request.

### Consequential repository changes

Examples: deleting meaningful historical material, changing security or privacy policy, publishing a formal release, changing repository settings, modifying automation permissions or making a public go-live declaration.

These changes require:

- a pull request or durable decision record;
- explicit risk and rollback notes;
- review by the repository owner, unless a later accepted process assigns that authority elsewhere;
- an exception record when normal review cannot be completed during narrow emergency containment.

### Reserved decisions

The following require explicit owner or other valid legal/governance authority and cannot be inferred from maintainer access:

- selecting or applying licenses;
- contracts, spending or legal representation;
- ownership transfer;
- credential disclosure or durable permission expansion;
- activation or supersession of canon;
- irreversible sanctions or deletion of participant rights or property.

## Merge and release authority

- The repository owner may merge pull requests and change repository settings.
- An operational maintainer may merge ordinary reversible maintenance within its assigned scope.
- Formal releases, launch tags and public go-live declarations require an explicit owner-approved go/no-go record.
- Release artifacts must identify the reviewed commit, known limitations, rollback path and support status.
- Direct force-pushes to `main` and deletion of `main` are prohibited operationally and should be blocked through GitHub branch protection when available.

## Review expectations

Every consequential pull request should state:

1. scope and purpose;
2. affected data and systems;
3. security, privacy and governance impact;
4. validation performed;
5. rollback or containment path;
6. authority used and any separate approval required.

The author must not approve their own consequential change as the only review. When the repository has only one human maintainer, an explicit owner exception record may substitute for a second reviewer for reversible repository work.

## Incident exception

During a confirmed public secret or unnecessary personal-data exposure, the System Guardian may perform narrow containment before ordinary review when delay increases harm. The action must:

- minimize scope;
- avoid copying the exposed value into issues or logs;
- preserve sanitized evidence;
- notify the owner promptly;
- document follow-up rotation, remediation and rollback.

Containment does not authorize unrelated cleanup, history rewriting or permission expansion.

## Continuity and succession

Operational knowledge must remain transferable through repository documents, issue records and pull requests rather than private memory.

A successor must be explicitly authorized and receive only the minimum required permissions. Before handover, record:

- maintained scope;
- active credentials and integrations by class, never secret value;
- open incidents and go-live blockers;
- backup and restore status;
- suspension and revocation procedure.

Until a successor is explicitly appointed, `lbabut` remains the recovery authority and legal principal.
