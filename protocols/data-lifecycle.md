# Data Lifecycle Protocol

Status: Draft — proposed by RFC 0006; not yet operational

## Purpose

Define how Aspiland classifies, collects, stores, publishes, changes, exports, archives and deletes data. This protocol applies only after explicit acceptance through the change-control process.

## Principles

1. Collect the minimum data needed for a defined purpose.
2. Do not infer consent from repository participation or technical access.
3. Keep public, private, operational, generated and archival data distinguishable.
4. Grant access by documented need and least privilege.
5. Set retention and deletion conditions when data is created, not after it becomes a problem.
6. Preserve history without treating indefinite public exposure as mandatory.
7. Make consequential automated decisions explainable and reviewable.
8. Do not require medical or identity disclosure when a functional preference is sufficient.

## Data classes

### Public

Reviewed for unrestricted publication. Publication purpose, provenance and reuse status should be clear.

Examples: public documentation, accepted public governance text, intentionally released research output.

### Participant-private

Information shared for a specific project or interaction and not intended for general publication.

Examples: contact details, private reports, accommodation preferences, access requests.

### Restricted operational

Information needed to operate systems securely or reliably.

Examples: access-control records, private infrastructure details, incident evidence and non-public logs.

Secrets are not ordinary operational records. They belong in an approved secret store and must not be committed to the repository.

### Generated runtime data

Caches, model output, temporary state, telemetry, build artifacts and logs created by software. Generated data requires an owner, purpose, retention limit and deletion path before persistent use.

### Archival

Historical material retained for provenance, research or accountability. Archival status does not automatically justify unrestricted public access.

### Prohibited

Data that Aspiland has no justified purpose or safe authority to collect, including copied credentials, unnecessary medical details, private communications published without authorization and data acquired through unauthorized access.

## Dataset record

Every persistent dataset or store should document:

- name and owner;
- purpose and lawful or consensual basis where relevant;
- data classes and fields;
- source and collection method;
- access roles;
- storage location and encryption expectations;
- external processors or services;
- retention period or review trigger;
- backup treatment;
- export, correction and deletion procedure;
- incident contact;
- shutdown or succession plan.

## Collection

- State the purpose before collection.
- Prefer anonymous, pseudonymous or synthetic data where identity is unnecessary.
- Separate mandatory fields from optional ones.
- Do not use deceptive consent or make essential access conditional on unrelated data collection.
- For sensory or communication accommodations, collect the requested boundary or format rather than a diagnosis unless the diagnosis is genuinely necessary and voluntarily provided.

## Access

- Access is granted to named roles for defined tasks.
- Administrative access is logged where practical and periodically reviewed.
- Shared accounts should be avoided.
- Departing, inactive or reassigned maintainers lose unnecessary access promptly.
- Emergency access is time-limited, recorded and reviewed afterward.

## Publication

Before moving information into `public/` or another unrestricted channel, review:

- personal and confidential information;
- credentials and infrastructure details;
- copyright, licensing and contributor permission;
- accuracy, context and status;
- whether redaction would be sufficient;
- whether publication creates avoidable safety or dignity risks.

Public availability elsewhere does not automatically authorize republication.

## Retention and deletion

Each store must use either a defined retention period or a documented review event. `Keep forever` requires a specific archival justification and periodic review.

Deletion should cover active stores, indexes, derived copies and scheduled backup expiry where practical. The response must not promise immediate erasure from systems that cannot technically provide it; limitations should be explained honestly.

## Participant requests

A participant should have a practical method to request applicable:

- access to their data;
- correction;
- export;
- restriction of processing;
- deletion;
- explanation of a consequential automated outcome.

Identity verification must be proportionate and should not collect more data than the request itself warrants.

## Incidents

Potential leaks, unauthorized access, mistaken publication or credential exposure are reported privately under `SECURITY.md`.

Containment takes priority over public documentation. A later sanitized record may describe scope, impact, remediation and prevention without reproducing the exposed material.

## Backups and archives

Backups must have an owner, restore test, access controls and retention policy. Removing a record from the active repository does not guarantee immediate disappearance from Git history, clones, forks or backups.

History rewriting requires a documented decision considering sensitivity, harm, coordination cost and residual copies.

## Automated systems

Automated systems may classify, flag or recommend data actions, but deletion, publication, identity linkage and access restrictions require appropriate human review unless a narrowly defined reversible rule was previously accepted.

## Review

Review this protocol at least annually and after a serious incident, new data category, new external processor or major change in project scope.

## Rollback

Before operational adoption, rollback means withdrawing or superseding the draft. After adoption, any replacement must preserve active retention, deletion and incident obligations until migration is complete.
