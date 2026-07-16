# Formal repository launch GO decision

Status: effective; non-canonical operational decision  
Date: 2026-07-16  
Decision-maker: repository owner  
Launch mode: formal public repository launch

## Decision

Aspiland is approved for formal public repository go-live.

This decision replaces the earlier repository-launch **NO-GO** record. The approved release is:

- release name: **Aspiland Repository Launch — 2026-07-16**;
- tag: `repository-launch-2026-07-16`;
- reviewed artifact: the merged commit containing this decision and the associated launch-status updates.

## What is launched

The launch presents Aspiland as a public experimental repository and historical archive. People may inspect the repository and website, read current and historical material, open issues and propose bounded contributions.

## What is not launched

This decision does not launch or certify:

- a sovereign state, legal jurisdiction or citizenship system;
- an operating community or governance system;
- production services or trusted infrastructure;
- processing of participant identity, health, contact or other private data;
- financial, medical or legal services;
- universal safety or support for historical code, binaries or experiments;
- a blanket open-source or reuse license.

Repository visibility does not grant permission beyond rights already held or separately granted.

## Completed controls

The launch decision relies on the completed repository-launch controls recorded in `docs/go-live-checklist.md`, including:

- current-tree and Git-history secret review;
- current-tree privacy and unsafe-public-material remediation;
- invalidation of the known historical credential candidate;
- connected-Google-Drive credential review;
- explicit acceptance of bounded external-store uncertainty;
- protected `main`, review rules and automated repository checks;
- secret checks for new changes and scheduled full-history review;
- documented security reporting and exposed-secret response;
- successful clean-runner recovery rehearsal;
- a private encrypted offsite backup verified after download;
- unfamiliar-reader onboarding review and static-site integrity checks;
- documented operational authority, recovery and rollback paths.

## Accepted residual risks

The owner accepts the following residual risks for repository launch:

- external stores outside the connected Drive scope were not exhaustively searched;
- legacy material may still be incomplete, outdated, unsupported or of uncertain provenance;
- the repository intentionally has no project-wide license during this phase;
- public visibility may attract mistaken claims about authority, readiness or reuse rights;
- security and privacy controls reduce risk but do not constitute exhaustive legal, forensic or production certification.

The external-store acceptance is recorded separately in `docs/decisions/2026-07-16-external-store-risk-acceptance.md`.

## Communication plan

Public communication may state that:

- the Aspiland repository has formally launched;
- the project remains an experiment and historical archive;
- contributions are welcome through documented repository paths;
- community or governance launch remains a separate future milestone;
- public access does not create a blanket reuse license.

## Rollback or unpublish triggers

Repository promotion or Pages publication must be reconsidered when there is credible evidence of:

- an active secret or privileged credential exposure;
- harmful personal-data exposure;
- materially misleading public claims about sovereignty, authority, safety or production readiness;
- repository compromise or loss of required security controls;
- a legal or rights claim requiring immediate containment;
- a failure that makes the published onboarding or security guidance materially unsafe.

Response follows `SECURITY.md`, `docs/recovery-checklist.md` and the rollback procedures in the previous go/no-go record.

## Ongoing obligations

After launch:

1. keep automated repository and secret checks active;
2. preserve the verified recovery path and refresh the offsite backup after consequential changes;
3. record security and privacy incidents without publishing sensitive values;
4. maintain clear separation between current material, proposals, experiments and archives;
5. require a separate decision before any community, governance, production-service or participant-data launch.

## Next review

Review this launch decision by 2026-08-16, or earlier when a rollback trigger or material scope change occurs.

## Outcome

**GO — formal public repository launch approved.**

Community or governance launch remains **NO-GO** until its separate controls and decision process are complete.