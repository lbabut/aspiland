# Current-tree go-live audit — 2026-07-12

Status: working security and privacy record; non-canonical

## Scope

This pass reviewed the indexed content of the current default branch for common credential markers, obvious contact-data fields and repository launch prerequisites. It also checked selected high-risk legacy paths identified by the repository map.

This was not a complete Git-history, binary, archive, backup, Drive or infrastructure scan. Absence from the findings below is not proof that no exposure exists.

## Actions completed

- Removed the obsolete Google Drive document containing an RSA private key.
- Confirmed that the removed Drive file was no longer retrievable through the connected Drive account.
- Searched the current repository index for common private-key markers and several credential patterns.
- Located a public `zzz_DeleteMe/user.json` record containing contact-data fields and scheduled it for removal from the current tree.
- Confirmed that no repository license file currently exists.
- Added `SECURITY.md`, contribution templates, a code of conduct, shared terminology and the go-live checklist.

## Current-tree findings

### P0 — public contact-data record

Path: `zzz_DeleteMe/user.json`

The file is indexed for at least `email` and `phone` fields. Its directory name also explicitly marks it for deletion. The current-tree copy should be removed without reproducing its contents.

Follow-up:

1. Remove it from the current branch.
2. Determine whose data it contains and whether the exposure warrants Git-history cleanup.
3. Search forks, releases, exported archives and backups where proportionate.
4. Record any necessary notification privately rather than in a public issue.

### P1 — legacy API configuration requires manual inspection

Path: `users/Muminki/muminki.py`

The file refers to `OPENAI_API_KEY` / `api_key`. Search did not identify common live-key prefixes, but code-search results alone cannot prove that no credential or unsafe fallback is embedded. Review the file locally or through a secret-scanning tool without publishing any discovered value.

### P1 — incomplete history and binary coverage

The repository is large and contains generated artifacts, IDE state, binaries and legacy user areas. Current indexed text search does not inspect all binary content or every historical revision.

High-priority areas remain:

- Git history and deleted paths;
- `.vs/`, `build/`, `dist/` and packaged executables;
- `users/`, `Embassies/`, `SharedAssets/` and historical chat or operational exports;
- deployment files, local environment files and backups;
- GitHub account keys, Azure resources and hosts that may trust the deleted RSA key.

### P0 — licensing is unresolved

No root `LICENSE` or `COPYING` file was found. A legal licensing decision is required before describing third-party reuse rights. Code, documentation, artwork and historical contributions may require different treatment.

## Searches performed

The indexed current tree was checked for representative markers including:

- RSA and OpenSSH private-key headers;
- `password`;
- `client_secret` and `client_secret.json`;
- `api_key` and `OPENAI_API_KEY`;
- common OpenAI key prefixes;
- `credentials.json` and `private_key_id`;
- common connection-string wording;
- several common personal email-domain markers;
- contact-data field combinations such as `email` and `phone`.

Most matches were policy documentation or variable names rather than confirmed secrets. Findings requiring manual inspection are recorded above.

## Required external scan

Before repository go-live, run a full clone-based scan with a maintained secret scanner against all refs and history, then manually inspect high-entropy and binary findings. The result should identify the scanner version, command or configuration, reviewed commit, findings, suppressions and remediation.

Do not paste discovered credentials into issues, pull requests, logs or this audit record.

## Privacy-history decision

Current-tree deletion is necessary but may not be sufficient. History rewriting should be reserved for confirmed serious exposure because it disrupts commit identifiers and requires coordinated cleanup of forks and clones. The decision should consider:

- sensitivity and identifiability of the data;
- whether the person consented to publication;
- exposure duration and repository reach;
- availability in forks, caches or releases;
- harm caused by preserving versus rewriting history.

## Remaining launch blockers

- comprehensive all-history secret scan;
- privacy review and decision for historical user data;
- credential trust-path review for the deleted RSA key;
- licensing decision;
- project-by-project runtime and dependency inventory;
- branch protection, recovery and release controls;
- formal go/no-go record.
