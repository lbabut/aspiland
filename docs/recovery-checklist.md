# Repository recovery checklist

Status: working operational checklist; non-canonical

Use this checklist to ensure Aspiland can be recovered without depending on one device, one credential or undocumented memory.

## Ownership and access

- [ ] Confirm the repository owner's primary email and recovery methods are current.
- [ ] Enable strong multi-factor authentication and securely store recovery codes outside the primary device.
- [ ] Inventory GitHub SSH keys, personal access tokens, installed apps and deploy keys.
- [ ] Remove unknown, unused or unscoped credentials.
- [ ] Identify an emergency recovery contact or documented succession mechanism.
- [ ] Record which actions require the legal principal rather than an operational maintainer.

Do not commit account identifiers, recovery codes, private keys or token values to this repository.

## Backup

- [ ] Create a mirror clone containing all refs.
- [ ] Record the backup date, source commit and tool versions.
- [ ] Store at least one encrypted copy outside GitHub.
- [ ] Include Git LFS objects, releases, issue or wiki exports where applicable.
- [ ] Define retention and replacement intervals.
- [ ] Verify that backup access does not depend solely on the account being recovered.

## Restore test

- [ ] Restore the mirror into a disposable private test repository or local bare repository.
- [ ] Verify branches, tags and default-branch history.
- [ ] Verify representative text and binary files.
- [ ] Verify Git LFS and release artifacts where used.
- [ ] Check that documentation links and essential project entry points remain understandable.
- [ ] Record the result without publishing private infrastructure details.

## Operational continuity

- [ ] List active maintainers and their scopes.
- [ ] Document how to suspend compromised automation or credentials.
- [ ] Document release, rollback and incident communication paths.
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
