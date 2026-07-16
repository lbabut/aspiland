#!/data/data/com.termux/files/usr/bin/bash

set -euo pipefail

REPO_URL="${1:-https://github.com/lbabut/aspiland.git}"
DEST_DIR="${2:-$HOME/storage/shared/Download/AspilandBackup}"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
WORK_DIR="$(mktemp -d "${TMPDIR:-$HOME}/aspiland-backup.XXXXXX")"
MIRROR_DIR="$WORK_DIR/aspiland.git"
BUNDLE_PATH="$WORK_DIR/aspiland-$STAMP.bundle"
ENCRYPTED_PATH="$DEST_DIR/aspiland-$STAMP.bundle.age"
CHECKSUM_PATH="$ENCRYPTED_PATH.sha256"

cleanup() {
  rm -rf "$WORK_DIR"
}
trap cleanup EXIT

for command in git age sha256sum; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "Missing command: $command" >&2
    echo "In Termux run: pkg update && pkg install git age coreutils" >&2
    exit 1
  fi
done

mkdir -p "$DEST_DIR"

echo "Cloning a complete mirror..."
git clone --mirror "$REPO_URL" "$MIRROR_DIR"

echo "Creating and verifying Git bundle..."
git -C "$MIRROR_DIR" bundle create "$BUNDLE_PATH" --all
git -C "$MIRROR_DIR" bundle verify "$BUNDLE_PATH"

echo "Encrypting backup. Enter a strong passphrase when prompted."
age -p -o "$ENCRYPTED_PATH" "$BUNDLE_PATH"

(
  cd "$DEST_DIR"
  sha256sum "$(basename "$ENCRYPTED_PATH")" > "$(basename "$CHECKSUM_PATH")"
)

chmod 600 "$ENCRYPTED_PATH" "$CHECKSUM_PATH" 2>/dev/null || true

echo
echo "Encrypted backup created:"
echo "  $ENCRYPTED_PATH"
echo "Checksum:"
echo "  $CHECKSUM_PATH"
echo
echo "Upload both files to a private offsite location, then verify the checksum after download."
