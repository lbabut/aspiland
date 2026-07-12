# Public contact-data containment

Date: 2026-07-12  
Type: emergency privacy containment  
Status: current-tree action complete; historical review open

## Decision

Remove `zzz_DeleteMe/user.json` from the current default branch because it was publicly indexed for contact-data fields and its directory explicitly marked it for deletion.

## Authority and rationale

The repository owner authorized continued go-live cleanup. `SECURITY.md`, the accepted repository hygiene baseline and RFC 0003 support narrow removal of unnecessary public personal data. Continuing publication created avoidable privacy risk, while current-tree deletion was narrow and reversible from Git history if the classification proved mistaken.

## Data handling

The record's content is not reproduced here. The review used the path, field-level indicators and blob identifier only as needed to remove the current copy.

## Verification

A read of the path on `main` after deletion returned `Not Found`.

## Remaining risk

The record may remain in Git history, clones, forks, caches, backups or exports. Current-tree removal does not guarantee erasure from those locations.

## Follow-up decision required

Determine privately:

- whose information the record contained;
- sensitivity and publication consent;
- exposure duration and repository reach;
- whether Git-history rewriting is justified;
- whether any notification or additional deletion request is appropriate.

## Rollback

Restore the file only after confirming a valid purpose, authority to publish, data minimization, retention conditions and an explicit privacy review. Do not restore the previous raw record by default.
