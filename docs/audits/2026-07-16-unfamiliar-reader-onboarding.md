# Unfamiliar-reader onboarding review — 2026-07-16

Status: completed for Repository Preview; non-canonical  
Scope: public, unauthenticated entry path from the website and repository root to a bounded first contribution

## Method

The review followed the project as an unfamiliar reader without relying on repository-owner context:

1. open the public repository while signed out;
2. identify the project phase and safety boundaries from the root page;
3. follow the current-status and repository-map links;
4. identify whether material is current, proposed, canonical, experimental or historical;
5. locate participation rules and a small first-contribution path;
6. inspect the public static-site source for complete navigation, readable structure and mobile behavior;
7. verify that the launch status and remaining blockers are described consistently.

The walkthrough used the current `main` content and an external unauthenticated renderer. It did not use a separate human research participant or a newly created GitHub account.

## Findings before remediation

The walkthrough found three material onboarding defects:

1. an external anonymous renderer initially served a stale pre-cleanup repository snapshot, although the current `main` tree contained the correct `README.md` and no conflicting root `Readme.md`;
2. `site/index.html` ended after the participation section, leaving the `#status` navigation target absent and omitting closing document structure;
3. `site/styles.css` ended before the section, card, status, footer and responsive rules, so much of the page lacked its intended layout;
4. the root README and current-status document still described privacy and licensing work as generally open after the current-tree review and temporary no-license decision had been completed.

The stale external rendering is treated as cache lag rather than current repository content. The repository cannot force immediate invalidation of every third-party cache, so current commit-linked content remains the source of truth.

## Remediation

The onboarding path was repaired by:

- completing the static-site HTML with status, closing and footer sections;
- restoring the missing `#status` target;
- adding responsive, keyboard-focus and reduced-motion styles in a separate reviewed stylesheet;
- adding direct links to the First Commit Kit, current status and go-live checklist;
- updating bilingual status text to match the actual remaining gates;
- updating the root README and current-status document;
- recording the private offsite-backup upload without publishing its location, checksum or passphrase.

## Final reader path

A new reader can now follow this bounded sequence:

1. public website or repository root;
2. `README.md` for purpose, phase, layers and disclaimers;
3. `docs/current-status.md` for what is complete and what remains blocked;
4. `docs/glossary.md` and `docs/repository-map.md` for interpretation and navigation;
5. `public/onboarding/first-commit-kit.md` for a small reversible contribution;
6. `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` and `SECURITY.md` for submission and safety rules.

The path makes clear that:

- Repository Preview is not formal repository, community or governance go-live;
- public visibility does not create a blanket license;
- historical files are not automatically current policy;
- a contribution grants no citizenship, ownership or authority;
- secrets and personal data must not be submitted publicly.

## Result

The unfamiliar-reader onboarding gate is **complete for Repository Preview** after the documented fixes.

This result does not certify community onboarding, accessibility conformance, translation quality across every document or the experience of a real first-time contributor. Those remain separate future tests where applicable.
