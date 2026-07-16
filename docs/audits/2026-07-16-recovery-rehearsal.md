# Repository recovery rehearsal — 2026-07-16

Status: completed automated restore test; non-canonical  
Workflow: `.github/workflows/recovery-rehearsal.yml`  
Evidence: pull request #19, successful `restore-test` job

## Scope

This rehearsal tested whether the complete Git history fetched by a GitHub-hosted runner could be packaged into a restorable Git bundle and recovered without relying on the repository owner's local device.

The test did not create or retain a durable offsite backup. It did not export issues, releases, wiki data, Git LFS objects, account recovery material or external service configuration.

## Procedure

1. Check out the repository with full Git history.
2. Create a temporary `recovery-snapshot` branch at the reviewed commit.
3. Create a Git bundle containing all refs available in the checkout.
4. Verify the bundle using `git bundle verify`.
5. Clone the bundle into a clean temporary directory.
6. Confirm that the restored HEAD exactly matches the source commit.
7. Run `git fsck --full` on the restored repository.
8. Verify representative entry-point documents.
9. Delete the temporary bundle and restored clone without uploading them as artifacts.

## Result

**PASS.** The workflow completed successfully. The bundle was accepted by Git, restored into a clean clone, matched the source HEAD and passed object-integrity checks.

## What this establishes

- the documented Git-only recovery mechanism is executable on infrastructure independent of the owner's device;
- a bundle made from the fetched history can be restored into a usable clone;
- representative repository documentation survives the tested path;
- the procedure can be repeated manually or through the monthly workflow.

## What remains open

- create and retain at least one encrypted backup outside GitHub;
- define retention and replacement intervals;
- confirm recovery access does not depend solely on the GitHub account being recovered;
- include and verify Git LFS objects, releases, issues and wiki exports where applicable;
- explicitly compare every branch and tag in a future extended rehearsal;
- verify representative binary artifacts only after their safety and licensing status is known.

## Safety

No bundle, restored repository or secret-bearing report was uploaded or committed. The audit contains no private infrastructure location, credential or recovery-code information.
