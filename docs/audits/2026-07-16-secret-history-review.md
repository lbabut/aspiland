# Secret history review — 2026-07-16

Status: completed automated history review with one unresolved historical candidate; non-canonical  
Scanner: Gitleaks v8.30.1  
Scope: complete fetched Git history and all fetched refs, segmented to avoid timeout

## Safety method

- The repository was checked out with complete Git history.
- Gitleaks output was fully redacted.
- Raw reports were deleted inside the runner.
- Public logs and retained summaries contained only period, status, suspected-finding count and rule identifiers.
- A one-time location report was encrypted to an ephemeral audit key, reviewed privately and removed from the proposed repository changes.
- No secret value, matching text or credential material was copied into this audit.

## Coverage

The review covered:

- history through 2022;
- calendar years 2023 and 2024;
- all quarters of 2025, with April and the second quarter subdivided when the patch-based scan exceeded practical runtime;
- both halves of 2026 through the review date;
- an additional commit-snapshot check for a date whose Git patch traversal was disproportionately expensive.

## Result

- **2023 through 2026:** no suspected secret findings in the covered periods.
- **Through 2022:** two scanner detections mapped to the same file, line and commit through different refs. They represent **one unique historical candidate** classified by Gitleaks as `generic-api-key`.
- The candidate file is absent from the current `main` tree.
- No active current-tree exposure was confirmed by this review.

## Risk assessment

The historical candidate cannot be assumed safe merely because it was removed from the current tree. A credential committed to public Git history must be treated as potentially compromised until the system that trusted it is identified and the credential is confirmed invalid, revoked or rotated.

The scanner classification is heuristic. This review did not use or test the candidate value against any external service, and therefore does not claim that it is a functioning credential.

## Decision

- Keep formal repository go-live blocked on credential disposition.
- Do not publish the candidate value, matching text or precise historical location in public audit records.
- Do not rewrite Git history automatically while the credential type, affected system and false-positive status remain unconfirmed.
- Track the candidate as a deferred security investigation requiring a sober, authorized account review.
- Prevent new secret candidates from entering pull requests or pushes to `main` through `.github/workflows/secret-change-guard.yml`.
- Retain `.github/workflows/secret-history-scan.yml` as a scheduled and manually callable full-history audit, separate from merge checks.

## Required follow-up

1. Inventory old administrator credentials, API integrations, cloud applications, bots, deployment systems and secret stores that may predate 2023.
2. Identify the likely issuing system without copying the candidate into issues, chat or documentation.
3. Revoke or rotate the credential if the issuing system can still recognize it.
4. Record only the credential class, affected system, disposition date and sanitized evidence.
5. Decide whether a coordinated history rewrite is still justified after revocation and provenance review.
6. If rewriting history, notify affected clones and integrations, preserve a recovery bundle and record the force-update plan before execution.

## Limits

This review does not cover duplicate credentials stored outside Git, including Drive, DevOps exports, deployment backups, local devices or external secret stores. It is a strong automated control, not a security certification or proof that every possible secret pattern is detectable.
