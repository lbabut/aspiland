# Roles and authority map

Status: descriptive baseline; non-canonical  
Last reviewed: 2026-07-12

This document distinguishes technical capability from governance authority. Holding platform permissions does not create unlimited authority over participants, canonical rules, property or data.

## Current operational roles

| Role | Current holder | Scope | Limits |
| --- | --- | --- | --- |
| Repository owner | `lbabut` GitHub account | Repository settings, access, merges and platform ownership | Legal and platform control does not make every repository statement canonical; consequential governance follows change control. |
| Contributor | Any person submitting work | Propose code, documentation, research or governance changes | Cannot publish secrets, unnecessary personal data or represent proposals as accepted. |
| Maintainer | Explicitly assigned per project or repository area | Review and maintain a documented scope | No implied authority outside the assignment; access should be revocable and reviewed. |
| Administrator | Person or system with elevated technical access | Perform specified infrastructure or repository operations | Least privilege; no self-expansion; consequential actions require records and review. |
| System Guardian | Proposed by RFC 0005; not yet accepted | Security, privacy, continuity, documentation and reversible maintenance assistance | No unilateral canon changes, ownership, legal commitments, spending, irreversible sanctions or permission expansion. |
| Automated agent | Any authorized automation | Execute narrowly defined checks or operations | Must not independently determine rights, identity, ownership or irreversible consequences. |

## Authority types

### Platform authority

Capabilities granted by GitHub, Drive, cloud infrastructure or another service. Platform authority is technical and can exceed the person's governance mandate; it must be used only for its documented purpose.

### Operational authority

Permission to maintain a project, respond to incidents, publish a release or manage a defined resource. Operational authority should identify scope, duration, escalation and succession.

### Governance authority

Permission to participate in accepting or superseding canonical rules. It exists only through the applicable accepted process, not merely through administrator access.

### Legal authority

Authority to enter contracts, transfer rights, spend money or represent another person or entity. It requires explicit authorization and must not be inferred from repository or automation roles.

## Approval baseline

| Action | Routine maintainer | Repository owner instruction | Accepted governance process |
| --- | ---: | ---: | ---: |
| Correct links, indexes and formatting | Yes | Not normally required | No |
| Draft RFCs, protocols and checklists | Yes | Not normally required | No |
| Remove generated artifacts after source verification | Yes | Recommended for large changes | No |
| Contain a publicly exposed secret or unnecessary personal-data record | Yes, narrowly and with a record | Notify promptly | Later review for consequential aftermath |
| Merge ordinary reversible maintenance | According to branch policy | Yes where owner is sole maintainer | No |
| Activate or change canonical rules | No | Owner instruction only where current accepted process permits | Yes |
| Choose and apply legal licenses | No | Explicit owner/legal-rights approval required | Governance review where community rights are affected |
| Spend money or accept contracts | No | Explicit legal principal approval required | As required by future accepted governance |
| Expand own permissions | No | Explicit scoped approval required | Required for durable governance authority |
| Impose irreversible sanctions or transfer property | No | No automatic owner shortcut | Heightened accepted process and applicable law |

## Required assignment record

A durable role assignment should state:

- holder or service identity;
- purpose and scope;
- systems and permissions;
- start date and review or expiry date;
- actions requiring separate approval;
- logging and notification expectations;
- conflict-of-interest and refusal rules;
- suspension, revocation and succession path.

## Current gaps

- project-level maintainers are not yet assigned for all legacy areas;
- repository recovery and succession are not tested;
- branch and settings authority is not yet documented as an operational procedure;
- RFC 0005 remains proposed and creates no current office by itself.
