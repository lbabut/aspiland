# Encrypted offsite backup from Android

Status: operational procedure; non-canonical  
Prepared: 2026-07-16

A complete encrypted repository backup can be created on an Android phone using Termux. The procedure creates a full Git mirror, packages all refs into a verified bundle, encrypts the bundle with a passphrase and writes a checksum next to it.

## Requirements

- Termux installed from a trusted distribution source;
- sufficient free storage for a complete mirror plus a temporary bundle and encrypted copy;
- a strong passphrase that is not stored in the repository or next to the backup;
- a private offsite destination such as a restricted Drive folder or another independently controlled storage account.

## One-time setup

```bash
termux-setup-storage
pkg update
pkg install git age coreutils
```

Allow storage access when Android asks.

## Create the backup

From a checked-out Aspiland repository, download or open `scripts/create_android_backup.sh`, then run:

```bash
chmod +x scripts/create_android_backup.sh
./scripts/create_android_backup.sh
```

The default output directory is:

```text
~/storage/shared/Download/AspilandBackup
```

The script produces:

- `aspiland-<timestamp>.bundle.age` — encrypted complete Git bundle;
- `aspiland-<timestamp>.bundle.age.sha256` — checksum for later integrity verification.

The temporary unencrypted mirror and bundle are removed automatically when the script exits.

## Store offsite

Upload both generated files to a private location outside GitHub. Do not upload the passphrase. Keep the passphrase in a separate password manager or other independent recovery channel.

## Verify after upload

Download both files into the same directory and run:

```bash
sha256sum -c aspiland-*.bundle.age.sha256
```

A successful verification prints `OK`.

## Restore test

Decrypt to a temporary bundle:

```bash
age -d -o aspiland-restored.bundle aspiland-*.bundle.age
```

Then verify and clone it:

```bash
git bundle verify aspiland-restored.bundle
git clone aspiland-restored.bundle aspiland-restored
```

Delete the temporary decrypted bundle after the test:

```bash
rm -f aspiland-restored.bundle
```

## Completion evidence

The durable-offsite-backup blocker is complete only after:

1. the encrypted file is uploaded outside GitHub;
2. the downloaded copy passes its checksum;
3. the passphrase is recoverable from a separate channel;
4. a dated, sanitized completion note records the storage class and verification result without publishing the passphrase or private location.
