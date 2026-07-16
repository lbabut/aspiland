# Repository recovery checklist

Status: working operational checklist; non-canonical

Use this checklist to ensure Aspiland can be recovered without depending on one device, one credential or undocumented memory.

## Ownership and access

- [ ] Confirm the repository owner's primary email and recovery methods are current.
- [ ] Enable strong multi-factor authentication and securely store recovery codes outside the primary device.
- [ ] Inventory GitHub SSH keys, personal access tokens, installed apps and deploy keys.
- [ ] Remove unknown, unused or unscoped credentials.
- [ ] Identify an emergency recovery contact or documented succession mechanism.
- [x] Record which actions require the legal principal rather than an operational maintainer in `docs/repository-operations.md`.

Do not commit account identifiers, recovery codes, private keys or token values to this repository.

## Backup

- [ ] Create and retain a mirror clone or all-ref bundle suitable for recovery.
- [ ] Record the retained backup date, source commit and tool versions.
- [ ] Store at least one encrypted copy outside GitHub.
- [ ] Include Git LFS objects, releases, issue or wiki exports where applicable.
- [ ] Define retention and replacement intervals.
- [ ] Verify that backup access does not depend solely on the account being recovered.

A temporary all-ref Git bundle was successfully created and restored during the 2026-07-16 rehearsal, but it was deliberately deleted after the test and is not a retained backup.

## Restore test

- [x] Restore an all-ref Git bundle into a disposable clean clone.
- [ ] Explicitly compare every branch, tag and default-branch history in the restored copy.
- [x] Verify representative text files and repository entry points.
- [ ] Verify representative binary files after their safety and licensing status is known.
- [ ] Verify Git LFS and release artifacts where used.
- [x] Check that essential documentation entry points remain available after restore.
- [x] Record the result without publishing private infrastructure details in `docs/audits/2026-07-16-recovery-rehearsal.md`.

## Operational continuity

- [x] List active repository maintainers and their scopes in `docs/repository-operations.md`.
- [x] Document narrow emergency containment and compromised-credential handling in `docs/repository-operations.md` and `SECURITY.md`.
- [x] Document release, rollback and incident communication paths in repository operations and go-live guidance.
- [ ] Ensure essential configuration can be recreated from safe templates and secret-store references.
- [ ] Review inactive projects and mark them archived rather than leaving ambiguous support expectations.

## Incident recovery

For credential or personal-data exposure:

1. contain the active exposure;
2. revoke or rotate trusted credentials;
3. preserve sanitized evidence;
4. identify affected systems and copies;
5. restore from a known-good state where necessary;
6. review permissions and logs;
7. document remediation and prevention;
8. test the recovered path.

## Completion record

Use `docs/audits/` for dated sanitized records. Do not publish private backup locations or access details.

```text
Date:
Reviewed commit:
Backup location class (not secret path):
Restore target:
Performed by:
Verified refs and artifacts:
Problems found:
Corrective actions:
Next test date:
```

Latest rehearsal: `docs/audits/2026-07-16-recovery-rehearsal.md`.
