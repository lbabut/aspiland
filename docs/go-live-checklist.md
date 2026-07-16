# Aspiland go-live checklist

Status: working checklist; non-canonical  
Last reviewed: 2026-07-16

This checklist separates a public repository launch from a community or governance launch. The second mode carries materially greater privacy, security, accessibility and decision-making obligations.

## 1. Choose the launch mode

### Repository launch

The repository is publicly presented as an experimental body of work. People may read, open issues and propose contributions. This does not create citizenship, jurisdiction, shared services or binding community membership.

### Community or governance launch

People are invited to participate under shared rules, roles, decisions, services or data-processing arrangements. This requires all repository-launch controls plus an accepted canonical package and operational community protections.

Record the chosen mode before announcing go-live.

## 2. Critical gate for any launch

The following items are go-live blockers unless a written risk acceptance explains why they are deferred.

- [x] Run a comprehensive automated secret scan of the current tree and fetched Git history; see `docs/audits/2026-07-16-secret-history-review.md`.
- [x] Search the connected Google Drive for Aspiland-related duplicate credentials; see `docs/audits/2026-07-16-drive-credential-search.md`.
- [x] Review or explicitly accept the uncertainty in remaining external stores and exports outside the connector scope; the owner accepted the residual risk in `docs/decisions/2026-07-16-external-store-risk-acceptance.md`.
- [x] Dispose of the removed pre-2023 credential candidate; the repository owner confirmed it is invalid and issue #22 records the sanitized disposition.
- [x] Complete a current-tree personal-data and unsafe-public-material review of targeted legacy areas; see `docs/audits/2026-07-16-legacy-privacy-review.md`.
- [x] Decide and document the current licensing model: Repository Preview remains without an explicit project-wide license; see `docs/licensing-decision-memo.md`.
- [x] Publish a security-reporting and exposed-secret procedure in `SECURITY.md`.
- [x] Identify the primary maintainer, reserved owner decisions and a documented recovery or succession path in `docs/repository-operations.md` and `docs/recovery-checklist.md`.
- [x] Confirm that a restorable Git bundle can be created and restored on a clean runner without the owner's device; see `docs/audits/2026-07-16-recovery-rehearsal.md`.
- [x] Create, privately upload and verify a durable encrypted offsite backup; see `docs/audits/2026-07-16-offsite-backup-upload.md`.
- [x] Keep the experimental, non-sovereign and non-production disclaimer visible in the root README.
- [x] Record a go/no-go decision with known residual risks and a rollback or unpublish plan; the current decision is formal **NO-GO** in `docs/decisions/2026-07-16-repository-launch-go-no-go.md`.

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
- [x] Add a redacted secret guard for every pull request and push to `main` through `.github/workflows/secret-change-guard.yml`.
- [x] Add an independently callable and scheduled full-history secret audit through `.github/workflows/secret-history-scan.yml`.
- [x] Add automated checks for broken links, Markdown structure and accidental generated files through `.github/workflows/repository-quality.yml`.
- [x] Define who can merge, publish releases and change repository settings in `docs/repository-operations.md`.

### Release and communication

- [ ] Choose a release name and tag the reviewed launch commit after a later GO or CONDITIONAL GO decision.
- [x] Draft a concise launch note explaining what Aspiland is and is not in `public/repository-preview-launch-note.md`.
- [x] Link prominently to the glossary, security policy, contribution guide and current status.
- [x] State which indexed components are active, conceptual, historical, unsupported or unsafe to run through the launch note and active project inventory.
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

## 5. Current assessment

Based on the repository review updated on 2026-07-16:

- the structure, disclaimers, contribution rules, change control, archive separation, operational authority, active project inventory and RFC workflow are suitable foundations for a repository launch;
- the historical credential candidate has a completed invalidity disposition based on owner attestation;
- the connected Drive credential search found no Aspiland credential duplicate, while uncertainty in Azure DevOps, local devices, deployment exports and independent backups is explicitly accepted as a bounded residual risk for repository launch;
- the targeted current-tree privacy review is complete after contact-data redaction and removal of unreviewed media, local IDE databases, an obsolete photo archive and generated Muminki build output;
- Repository Preview intentionally remains without an explicit project-wide license;
- Git-only recovery has been rehearsed successfully, and a private encrypted offsite backup has been created, uploaded and verified after download;
- branch protection and platform security settings are recorded complete by owner attestation;
- the unfamiliar-reader onboarding path has been reviewed and repaired, including completion of the previously truncated public website source;
- future pull requests and pushes to `main` are covered by a redacted change-range secret guard, while full-history review remains separately scheduled and callable;
- a formal decision record currently sets the repository launch state to **NO-GO**, while allowing the clearly labelled Repository Preview to remain online without additional promotion;
- the remaining repository-launch action is a new dated **GO**, **CONDITIONAL GO** or **NO-GO** decision, followed by a release name and tag if the decision permits launch;
- a community or governance launch is not ready until a minimal canonical package and the additional controls in section 4 are explicitly accepted and operational.

This assessment is a repository review, not a legal, security-certification or production-readiness guarantee.

## 6. Go/no-go record template

```text
Launch mode:
Target date:
Reviewed commit or tag:
Decision: GO / CONDITIONAL GO / NO-GO
Decision-makers:
Completed critical controls:
Accepted residual risks:
Open blockers:
Communication plan:
Rollback or unpublish trigger:
Next review date:
```
