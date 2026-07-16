# Encrypted offsite backup upload — 2026-07-16

Status: complete; downloaded-copy integrity confirmed  
Scope: encrypted Git bundle created on Android, uploaded to a private Google Drive folder and verified after download

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

## Downloaded-copy verification

The connected Drive interface could not download the encrypted bundle because its size exceeded the connector limit. The repository owner therefore downloaded the offsite copy to Android and ran:

```bash
sha256sum -c aspiland-20260716T182905Z.bundle.age.sha256
```

The command returned:

```text
aspiland-20260716T182905Z.bundle.age: OK
```

This confirms that the copy retrieved from the offsite location matches the checksum created with the encrypted backup.

## Current decision

- Offsite creation: complete.
- Private upload: complete.
- Downloaded-copy checksum: complete.
- Passphrase separation: intentionally private and not inspected by this review.

The durable encrypted offsite-backup gate is complete. This is sanitized operational evidence, not publication of the backup location, checksum or credentials.
