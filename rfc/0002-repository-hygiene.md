# RFC 0002 — Repository hygiene baseline

Status: Proposed

## Purpose

Establish a safe baseline for maintaining a repository that contains governance, historical records, personal areas and experimental software.

## Proposed baseline

1. The root README describes the current repository rather than a historical server status.
2. Legacy root text is preserved in `archive/` before replacement.
3. Generated IDE metadata, build output, caches and runtime state are ignored.
4. Active software experiments include dependency and execution instructions.
5. Text encoding and line endings are normalized for future commits.
6. Existing generated artifacts are inventoried before deletion.
7. User directories are reviewed for personal or sensitive data before reclassification.
8. History is not rewritten unless a confirmed secret or serious privacy exposure requires it.

## Changes included with this proposal

- replace `Readme.md` with `README.md`;
- preserve the old root README in the archive;
- expand `.gitignore`;
- add `.editorconfig` and `.gitattributes`;
- add repository and contribution documentation;
- document Muminki and its dependencies;
- record RFC 0001 as accepted.

## Deferred cleanup

Tracked `.vs/`, PyInstaller `build/` and `dist/` output should be removed in a separate reviewed change after their complete paths are inventoried. Source files and build instructions must be confirmed first.

## Rollback

Revert the cleanup merge commit. The legacy README remains preserved in `archive/legacy-root-readme-2025.md`.

## Decision record

Pending review.
