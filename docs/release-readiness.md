# Release readiness summary

Status: working status page; non-canonical  
Last reviewed: 2026-07-12

## Recommended next milestone

**Repository Preview**, not community or governance go-live.

The preview may present Aspiland as a public experimental archive and laboratory while clearly labeling unsupported legacy software, proposed governance and unresolved licensing. It must not claim production support, sovereign status, active citizenship or a fully operating community.

## Completed foundations

- current root overview and repository map;
- separation of canon, RFCs, protocols, projects, archive and public material;
- accepted change-control and hygiene baselines;
- removal of obsolete coercive current rules;
- glossary and interpretation of historical terminology;
- security-reporting and exposed-secret procedure;
- code of conduct and contribution templates;
- go-live checklist and active project inventory;
- current-tree removal of one exposed contact-data record;
- draft data lifecycle protocol;
- bounded System Guardian and licensing proposals.

## P0 blockers

1. Complete a clone-based secret scan across all refs and history.
2. Review historical personal data and decide whether any history rewrite is justified.
3. Identify and revoke the trust path of the deleted RSA key where it still exists.
4. Make an explicit licensing and rights decision.
5. Test backup restoration and repository recovery.
6. Record the final preview go/no-go decision and reviewed commit.

## P1 quality work

- inventory and remove tracked generated artifacts after source verification;
- manually review the Muminki API configuration and runtime data;
- assign maintainers or archival status to legacy areas;
- document branch protections and release authority;
- add automated link, Markdown and secret checks;
- prepare a concise preview announcement and test it with a new reader;
- tag the reviewed preview commit.

## Community launch blockers

A community or governance launch additionally requires:

- explicit acceptance of a minimal canonical package;
- roles, succession, notice, appeal and moderation procedures;
- an operational data lifecycle and participant request path;
- accessibility and sensory-boundary handling;
- service ownership and incident response;
- separation of experimental economy from identity and essential access.

## Current recommendation

Do not announce formal go-live yet. Continue cleanup under the `Repository Preview` milestone and make the final launch decision only after the P0 blockers have evidence-backed closure or an explicit written risk acceptance.
