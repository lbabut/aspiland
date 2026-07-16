# Encrypted offsite backup upload — 2026-07-16

Status: upload confirmed; integrity verification pending  
Scope: encrypted Git bundle created on Android and uploaded to a private Google Drive folder

## Evidence

The repository owner created the backup using the documented Android/Termux procedure and uploaded both required files:

- `aspiland-20260716T182905Z.bundle.age`;
- `aspiland-20260716T182905Z.bundle.age.sha256`.

Connected Drive metadata confirmed:

- the encrypted bundle exists and is approximately 559 MB;
- the companion checksum file exists;
- both files are in the same private backup folder;
- the encrypted bundle is not shared and the only visible permission is the owner permission.

No passphrase, checksum value, private folder URL or recovery secret is recorded here.

## Verification boundary

The connected Drive interface could retrieve the small checksum file but rejected download of the encrypted bundle because its size exceeded the connector limit. The upload is therefore confirmed, but end-to-end integrity is not yet independently verified by this review.

The blocker is complete only after a copy downloaded from the offsite location returns `OK` from:

```bash
sha256sum -c aspiland-20260716T182905Z.bundle.age.sha256
```

## Current decision

- Offsite creation: complete.
- Private upload: complete.
- Independent downloaded-copy checksum: pending owner confirmation.
- Passphrase separation: required and not inspected.

This is sanitized operational evidence, not publication of the backup location or credentials.
