# Full-history security scan runbook

Status: operational runbook; non-canonical

This runbook describes the evidence needed for the P0 secret-scan gate. It deliberately does not include live credential values.

## Preparation

- Use a trusted workstation with sufficient disk space.
- Create a mirror clone so all branches, tags and reachable refs are available.
- Record the source repository, reviewed head commit and scan date.
- Update the selected scanner and record its version.
- Keep findings in a private location because scanner output may contain secrets.

## Scan layers

1. Scan the current working tree.
2. Scan all Git history and refs.
3. Inspect high-entropy findings and known credential formats.
4. Review binary, archive, build and IDE artifacts separately.
5. Search deployment repositories, Drive exports, backup locations and cloud configuration where authorized.
6. Compare discovered public keys or identifiers with accounts and hosts that may trust them.

## Representative commands

Choose a maintained tool and verify its current documentation before execution. A local scan may use tools such as Gitleaks or TruffleHog, but the exact command and configuration must be recorded with the result rather than copied blindly from this document.

Never paste scanner findings into a public issue or CI log. Configure CI to redact and fail safely.

## Finding classification

For each finding record privately:

- finding identifier and detector;
- path and commit, without the secret value;
- credential type and issuing system;
- whether it appears live, test, placeholder or false positive;
- exposure scope;
- revocation or rotation action;
- duplicate locations;
- history-cleanup decision;
- verification that replacement access works.

## Completion evidence

The P0 gate is complete only when:

- current tree and history were scanned;
- binaries and high-risk legacy paths received manual review;
- confirmed credentials were revoked or rotated;
- false positives were justified without publishing values;
- residual copies and trust paths were assessed;
- a sanitized audit record names the reviewed commit, tools, versions and remaining limitations.

## Repetition

Repeat the scan before a tagged preview or release, after importing legacy material and after any credential incident.
