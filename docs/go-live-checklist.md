# Aspiland go-live checklist

Status: repository launch complete; community launch pending  
Last reviewed: 2026-07-16

This checklist separates a public repository launch from a community or governance launch. The second mode carries materially greater privacy, security, accessibility and decision-making obligations.

## 1. Launch mode

### Repository launch

The repository is publicly presented as an experimental body of work. People may read, open issues and propose contributions. This does not create citizenship, jurisdiction, shared services or binding community membership.

**Decision: GO — 2026-07-16.**

### Community or governance launch

People are invited to participate under shared rules, roles, decisions, services or data-processing arrangements. This requires all repository-launch controls plus an accepted canonical package and operational community protections.

**Decision: not launched.**

## 2. Critical gate for repository launch

- [x] Run a comprehensive automated secret scan of the current tree and fetched Git history; see `docs/audits/2026-07-16-secret-history-review.md`.
- [x] Search the connected Google Drive for Aspiland-related duplicate credentials; see `docs/audits/2026-07-16-drive-credential-search.md`.
- [x] Review or explicitly accept the uncertainty in remaining external stores and exports; see `docs/decisions/2026-07-16-external-store-risk-acceptance.md`.
- [x] Dispose of the removed pre-2023 credential candidate; the repository owner confirmed it is invalid and issue #22 records the sanitized disposition.
- [x] Complete a current-tree personal-data and unsafe-public-material review; see `docs/audits/2026-07-16-legacy-privacy-review.md`.
- [x] Decide and document the current licensing model: the repository remains without an explicit project-wide license; see `docs/licensing-decision-memo.md`.
- [x] Publish security-reporting and exposed-secret procedures in `SECURITY.md`.
- [x] Identify the primary maintainer, reserved decisions and recovery or succession path in `docs/repository-operations.md` and `docs/recovery-checklist.md`.
- [x] Confirm that a restorable Git bundle can be created and restored on a clean runner; see `docs/audits/2026-07-16-recovery-rehearsal.md`.
- [x] Create, privately upload and verify a durable encrypted offsite backup; see `docs/audits/2026-07-16-offsite-backup-upload.md`.
- [x] Keep the experimental, non-sovereign and non-production disclaimer visible in the root README.
- [x] Record the final launch decision, residual risks and rollback triggers; see `docs/decisions/2026-07-16-repository-launch-go.md`.

## 3. Repository-launch readiness

### Navigation and meaning

- [x] Root README explains the project and major directories.
- [x] Repository map distinguishes current and legacy areas.
- [x] Glossary distinguishes current terms from historical metaphors.
- [x] Contribution guidance separates canon, RFCs, projects, archive and public material.
- [x] Add a code of conduct appropriate for a small experimental community.
- [x] Ensure every active project has an owner, status, dependencies and safe use or run instructions in `projects/README.md`.

### GitHub controls

- [x] Protect `main` from accidental force-push and deletion; completed by owner attestation in issue #15.
- [x] Require review or an explicit exception record for consequential changes through `docs/repository-operations.md`.
- [x] Add issue and pull-request templates that prompt for scope, risk, data handling and rollback.
- [x] Confirm GitHub platform secret scanning and dependency alerts where available; completed by owner attestation in issue #15.
- [x] Add a redacted secret guard for every pull request and push to `main`.
- [x] Add a scheduled and manually callable full-history secret audit.
- [x] Add automated checks for links, Markdown structure, generated files and static-site integrity.
- [x] Define who can merge, publish releases and change repository settings.

### Release and communication

- [x] Choose release name **Aspiland Repository Launch — 2026-07-16** and tag `repository-launch-2026-07-16`.
- [x] Publish the formal launch note in `public/repository-launch-note.md`.
- [x] Link prominently to the glossary, security policy, contribution guide and current status.
- [x] State which indexed components are active, conceptual, historical, unsupported or unsafe to run.
- [x] Test the onboarding path as an unfamiliar unauthenticated reader; see `docs/audits/2026-07-16-unfamiliar-reader-onboarding.md`.

## 4. Additional community or governance gate

Do not present Aspiland as an operating governed community until these items are complete.

### Canon and authority

- [ ] Accept a minimal canonical package through the documented RFC and change-control process.
- [ ] Define the scope and limits of every governance and administrative role.
- [ ] Define succession, inactivity, removal and emergency-access procedures.
- [ ] Ensure no person or automated system can unilaterally redefine everyone's rights.
- [ ] Publish a decision register with effective dates and supersession history.

### Participation and fair process

- [ ] Create plain-language onboarding explaining voluntary participation and exit.
- [ ] Define how affected participants receive notice and meaningful review time.
- [ ] Define transparent criteria, reasons, appeal and review for consequential decisions.
- [ ] Adopt proportionate, time-limited and reviewable moderation procedures.
- [ ] Define conflicts of interest and when a decision-maker must step aside.

### Privacy and data lifecycle

- [ ] Publish a data classification, purpose, retention, access, backup and deletion protocol.
- [ ] Separate public, private, operational and generated data in practice, not only in documentation.
- [ ] Define how a participant can inspect, correct, export or request deletion of applicable data.
- [ ] Avoid collecting identity, diagnosis or contact data unless a specific function requires it.
- [ ] Perform a threat model for every system processing participant preferences or private data.

### Accessibility and boundaries

- [ ] Provide an accessible way to communicate sensory and communication boundaries without requiring diagnosis disclosure.
- [ ] Check documents and interfaces for readable structure, language clarity and keyboard or assistive-technology access where applicable.
- [ ] Define a practical response when immediate safety or essential-access needs conflict with normal process.
- [ ] Test translations against an identified source version and label whether they are authoritative or informative.

### Services and economy

- [ ] Clearly distinguish simulations from real financial instruments, employment, benefits or entitlement.
- [ ] Keep experimental tokens and budgets opt-in and separate from identity, membership, ownership and essential access.
- [ ] Define service availability, support limits, incident handling and shutdown procedures before operating shared infrastructure.

## 5. Launch assessment

Based on the repository review updated on 2026-07-16:

- all repository-launch critical gates are complete or explicitly resolved;
- the external-store uncertainty is accepted as a bounded residual risk;
- the repository remains without a project-wide license;
- the recovery rehearsal and verified offsite backup are complete;
- onboarding and static-site integrity checks are active;
- future changes remain covered by repository-quality and secret controls;
- formal public repository launch is **GO**;
- community or governance launch remains a separate later milestone.

This assessment is a repository review, not a legal, security-certification or production-readiness guarantee.

## 6. Release record

```text
Launch mode: formal public repository launch
Launch date: 2026-07-16
Release name: Aspiland Repository Launch — 2026-07-16
Tag: repository-launch-2026-07-16
Decision: GO
Decision-maker: repository owner
Accepted residual risks: external-store uncertainty; no project-wide license; legacy provenance and support limitations
Open repository-launch blockers: none
Rollback triggers: documented in the GO decision and SECURITY.md
Next review date: 2026-08-16
```