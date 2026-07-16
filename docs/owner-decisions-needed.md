# Repository owner decisions needed

Status: decision queue; non-canonical  
Last reviewed: 2026-07-16

These items cannot be completed solely through operational cleanup because they change authority, legal permissions or accepted governance.

## Resolved — System Guardian role, RFC 0005

Accepted and effective on 2026-07-12.

Initial scope:

- Observe;
- Propose;
- Maintain;
- narrow emergency Contain.

Elevated `Administer` capability remains separately authorized per concrete task. The role must be reviewed after its first three consequential post-effective actions or by 2026-10-10.

## Resolved — formal repository launch

Approved on 2026-07-16.

- Decision: **GO**;
- release name: **Aspiland Repository Launch — 2026-07-16**;
- tag: `repository-launch-2026-07-16`;
- residual external-store uncertainty: explicitly accepted;
- rollback and review triggers: recorded in `docs/decisions/2026-07-16-repository-launch-go.md`.

## 1. Data lifecycle protocol — RFC 0006

Decision options:

- accept the draft protocol;
- run a review period before acceptance;
- narrow its scope to active projects first;
- request revisions.

Operational adoption requires owners for datasets and request handling; accepting text alone does not implement storage controls.

## 2. Licensing strategy — RFC 0007

The owner must explicitly choose licenses only after confirming rights. Separate decisions are needed for:

- new original software;
- documentation and governance text;
- artwork, logos and merchandise designs;
- historical contributions and conversations;
- datasets and generated outputs.

No project-wide license has been selected. Formal repository launch does not change this position.

## 3. Community or governance launch

A later community-launch decision must record:

- the accepted minimal canonical package;
- roles and authority limits;
- participation, notice, appeal and moderation procedures;
- operational privacy and data-lifecycle controls;
- accessibility and continuity safeguards;
- service ownership, incident response and shutdown procedures;
- reviewed commit or tag, residual risks and rollback triggers.