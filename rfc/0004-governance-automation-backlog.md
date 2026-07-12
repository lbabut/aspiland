# RFC 0004 — Recover the governance automation backlog

Status: Proposed  
Proposed: 2026-07-12  
Source: sanitized review of historical Google Drive material

## Purpose

Recover the strongest unfinished ideas from Aspiland's early governance notes without restoring obsolete rules, importing private data or treating historical drafts as automatically binding.

This RFC creates a reviewable backlog. It does not itself make any item canonical and does not authorize automated systems to decide rights, sanctions, membership or ownership.

## Proposed backlog

### 1. Change notice and activation window

Define a standard review window for consequential changes. Each proposal should state:

- who is affected;
- how notice will be delivered;
- the earliest activation date;
- whether an objection pauses activation;
- the rollback or supersession path.

Emergency changes remain narrow, temporary and subject to later confirmation under `protocols/change-control.md`.

### 2. Machine-assisted consistency checks

Create a non-authoritative checker for governance documents and RFCs. It should flag, at minimum:

- conflicting definitions;
- incompatible permissions or responsibilities;
- missing status, decision or effective-date fields;
- unresolved links and references;
- rules without an identified review or rollback path;
- language variants that have drifted from the identified source text.

A human review record remains required for acceptance.

### 3. Continuity and succession protocol

Document how maintainers recover access and transfer responsibilities when a role holder is unavailable. The protocol should use:

- at least two maintainers for consequential infrastructure where practical;
- least-privilege access;
- documented recovery procedures;
- inactivity thresholds with notice;
- time-limited emergency authority;
- explicit review of every succession event.

No role may appoint its own permanent successor without an independent review path.

### 4. Translation workflow

Allow governance material to be read and proposed in multiple languages while preventing silent divergence. Every translated governance document should identify:

- its source document and version;
- whether it is informative or authoritative;
- the translator or translation method;
- the last comparison date;
- known ambiguities requiring review.

### 5. Sensory accessibility profile

Design a voluntary way for participants to communicate relevant boundaries around noise, light, smell, proximity, interruption and communication cadence. The implementation must minimize personal data, avoid diagnosis requirements and distinguish preferences from urgent safety needs.

### 6. Transparent decisions and appeal

Create a reusable decision-record format containing:

- the decision and its scope;
- the criteria applied;
- the supporting evidence;
- the affected people or systems;
- the reviewer or decision process;
- the review date and appeal route.

Automated recommendations must be labeled as such and remain challengeable.

### 7. Data lifecycle and reliable access

Define a data-handling protocol covering classification, purpose, access, retention, backup, recovery and deletion. Public, private, operational and generated material must remain clearly separated. Reliable access should not be achieved by publishing sensitive material or retaining it indefinitely.

### 8. Accessible onboarding and handover

Create plain-language templates for project participation, role requests, informed consent where needed, and operational handover. Templates should be translatable and must state that participation is voluntary, scoped and revocable.

### 9. Needs-first review gate

Before adopting a policy or system, reviewers should ask whether it creates barriers for people whose immediate safety, accessibility or essential needs are unresolved. This is a design check, not a mechanism for ranking people's worth or eligibility.

### 10. Economy sandbox

Any token, budget, recurring distribution or tax concept should be implemented only as an opt-in experiment under `projects/`. Economic state must not automatically determine identity, membership, essential access or ownership.

## Affected users and systems

This proposal affects future governance tooling, maintainers, translators, project participants and any system that processes governance documents or participant preferences.

## Non-goals

This RFC does not:

- import the original Drive spreadsheets or documents;
- declare historical drafts canonical;
- create government authority or legal jurisdiction;
- permit autonomous governance decisions;
- require disclosure of health information or private identity data;
- revive superseded sanctions, property rules or administrator privileges.

## Risks

- Automation may create false confidence or encode ambiguous assumptions.
- Translation may conceal meaningful differences between versions.
- Continuity procedures may centralize access if least privilege is ignored.
- Accessibility profiles may become sensitive personal data.
- A token experiment may be mistaken for real financial value or entitlement.

Each implementation therefore requires its own threat model, data-minimization review and rollback plan.

## Migration plan

1. Preserve the sanitized historical summary in `archive/drive/2022-governance-notes.md`.
2. Review and prioritize the backlog as separate RFCs, issues or projects.
3. Prototype tools using non-sensitive test data.
4. Require explicit acceptance before moving any governance text into `canon/`.
5. Record rejected or superseded items rather than silently deleting their decision history.

## Rollback plan

Revert the commit or pull request that introduces this RFC. Any implementation produced from the backlog must define its own independent rollback and data-deletion procedure.

## Decision record

Pending review. Merging this file records the proposal but does not accept it or make it effective.
