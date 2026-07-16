# External-store residual-risk acceptance

Status: accepted for repository launch only; non-canonical  
Date: 2026-07-16  
Decision-maker: repository owner

## Decision

The repository owner explicitly accepts the residual risk created by not completing a forensic review of every external copy or store that may contain historical Aspiland material.

This acceptance closes the external-store review gate for a **formal repository launch**. It does not assert that every external location has been searched or that no historical credential, personal data or unsafe artifact exists outside the reviewed repository and connected Google Drive.

## Accepted uncertainty

The unreviewed or incompletely reviewed scope may include:

- Azure DevOps repositories, pipelines, variable groups, secure files and deployment exports;
- local phones, computers, removable media and offline archives;
- disconnected accounts, shared drives and independent backup systems;
- files stored under unrelated names or in binary formats that are not searchable through the available connectors;
- historical copies created before the current repository controls were introduced.

No active exposure in those locations is currently known. The residual risk is uncertainty caused by incomplete visibility, not evidence that those stores are clean.

## Basis for acceptance

The owner accepts this risk in light of the controls already completed:

- comprehensive current-tree and Git-history secret review;
- removal or invalidation of the known historical credential candidate;
- targeted connected-Google-Drive credential search;
- current-tree personal-data and unsafe-material remediation;
- automated secret checks for new changes and scheduled full-history review;
- private security-reporting and exposed-secret response procedures;
- protected `main`, review controls and rollback documentation;
- verified encrypted offsite repository backup.

## Boundaries

This acceptance applies only to presenting the repository as a public experimental body of work.

It does not authorize or certify:

- a community or governance launch;
- production services or trusted integrations using historical credentials;
- processing participant identity, health, contact or other private data;
- claims of exhaustive security, privacy, legal or forensic clearance;
- reuse of material whose copyright, license or provenance remains uncertain.

## Mandatory response to later discoveries

Discovery of a credible secret, private-data exposure or unsafe external copy requires:

1. immediate containment without publishing the sensitive value;
2. revocation or rotation of any affected credential;
3. assessment of whether repository promotion or Pages publication should be paused;
4. a sanitized incident record and remediation evidence;
5. reconsideration of this risk acceptance when the discovery materially changes the launch assessment.

## Review triggers

This acceptance must be reviewed before:

- connecting Aspiland to a production or privileged system;
- collecting or processing participant data;
- launching an operating community or governance system;
- relying on an old deployment, archive or credential container;
- any material evidence that an external copy contains an active secret or harmful personal data.

## Outcome

The external-store uncertainty is now an **accepted residual risk**, not an open repository-launch blocker. A separate, dated **GO**, **CONDITIONAL GO** or **NO-GO** decision is still required before formally announcing repository go-live.
