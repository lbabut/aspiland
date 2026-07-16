# Repository launch decision — 2026-07-16

Status: formal operational decision record; non-canonical  
Launch mode reviewed: public repository launch  
Decision: **NO-GO for a formal repository launch declaration**  
Repository Preview: **may remain online without additional promotion**

## Decision authority

- Repository owner: Łukasz Babut.
- Operational recommendation and record preparation: System Guardian.
- Reviewed commit: `b8535bcda725d97c646569fc23cce35982dfcd1a`.

This record does not authorize a community or governance launch, create shared jurisdiction, activate services, or change canonical authority.

## Rationale

The repository has a suitable foundation for continued Repository Preview use, and several important controls are already operating. A formal launch declaration would nevertheless be premature because unresolved security, privacy, licensing and recovery matters remain.

The NO-GO decision is therefore a controlled pause, not a project cancellation.

## Completed controls considered

- repository purpose, disclaimers and archive boundaries are visible;
- contribution, review and repository-operation rules are documented;
- active projects have an operational inventory;
- repository quality checks run on pull requests;
- new pull requests and pushes to `main` are covered by a redacted secret change guard;
- fetched Git history received a segmented automated secret review;
- Git bundle creation and clean-runner restoration were rehearsed successfully;
- a security reporting procedure and Repository Preview launch note are published.

## Open blockers

Formal launch remains blocked until the following are resolved or explicitly accepted in a later decision record:

1. Identify the issuing or trusting system for the removed pre-2023 credential candidate and revoke, rotate or confirm it invalid.
2. Search relevant external stores and exports for duplicate credentials.
3. Complete the broader legacy personal-data and unsafe-public-material review.
4. Decide and document the licensing model for code, documentation, artwork, historical records and contributor-owned material.
5. Create and verify a durable encrypted backup outside GitHub.
6. Protect `main` from force-push and deletion and confirm available GitHub security-alert settings.
7. Complete an unfamiliar-reader or new-account onboarding test.

## Residual risks accepted for Repository Preview

The owner accepts only the limited residual risk of keeping the existing Repository Preview accessible while:

- it remains clearly labelled experimental, non-sovereign and non-production;
- no formal launch, release announcement or broad promotional campaign occurs;
- unresolved blockers remain visible in the go-live tracker;
- newly confirmed security, privacy or rights concerns trigger containment rather than promotion.

This acceptance does not classify the unresolved historical credential candidate as safe and does not waive the rights of third parties whose material may appear in legacy areas.

## Communication plan

- Continue using **Repository Preview** wording.
- Do not publish a formal launch announcement or launch release tag.
- Do not describe Aspiland as an operating governed community.
- Direct contributors and readers to the current-status, security, glossary and contribution documents.
- Revisit the decision only through a new dated GO / CONDITIONAL GO / NO-GO record.

## Rollback or unpublish triggers

Containment or unpublishing should be considered immediately when any of the following occurs:

- a credential in current or historical content is confirmed active or exploitable;
- private, sensitive or unlawfully published personal data is confirmed;
- a credible copyright, ownership or consent dispute affects publicly presented material;
- repository or site content becomes materially misleading about project status or authority;
- access control, maintainer control or repository integrity is lost;
- automated checks reveal a new high-severity exposure that cannot be corrected promptly.

## Rollback or unpublish plan

1. Stop announcements, promotion and release activity.
2. Record the incident in a sanitized security or operations issue.
3. Remove or restrict the affected current-tree material without copying sensitive values into public records.
4. Revoke or rotate affected credentials before treating deletion as remediation.
5. Disable public presentation mechanisms, including GitHub Pages, when continued publication would increase harm.
6. Use the verified Git bundle recovery process if repository integrity is affected.
7. Publish a brief, non-sensitive status notice and define the condition required for restoration.
8. Create a new dated decision record before resuming formal launch work.

## Next review

Review this decision after the critical blockers are resolved, or before any formal release tag, launch announcement or material expansion of public participation—whichever occurs first.
