# Legacy privacy and unsafe-public-material review — 2026-07-16

Status: completed current-tree review for targeted legacy areas; non-canonical  
Scope: `users/`, `PublicChat.txt`, `Embassies/`, `SharedAssets/`, archive material, generated build output and binary archives present in the reviewed branch

## Method

The review combined:

- an automated current-tree scan for email addresses, international phone numbers, possible 11-digit personal identifiers and privacy or health markers;
- identification of binary, archive, IDE-database and generated build artifacts;
- encrypted review of exact file paths and flagged media;
- manual inspection of every remaining text hit and all flagged images;
- removal or redaction in the current tree without publishing matched values in the audit record.

Public workflow output contained only counts and broad directory groups. Exact paths and media used during review were encrypted to a one-time audit key and were not retained in the final repository changes.

## Initial result

The first scan considered 69 targeted files and produced 44 locations requiring review. The categories included:

- email and telephone contact details;
- possible personal-identifier patterns;
- one health-related keyword hit;
- legacy images and duplicated temporary media;
- a photo archive in a deletion-marked directory;
- local Visual Studio and Copilot databases;
- generated PyInstaller build output and an executable.

## Remediation

The current tree was changed as follows:

- removed personal email and emergency telephone details from two duplicated historical user-profile files;
- removed a personal contact address from the archived server-status block;
- removed the obsolete photo ZIP from the deletion-marked directory;
- removed local Visual Studio and Copilot index databases;
- privately reviewed the legacy image set and removed it from the current tree because it contained duplicated material, a photograph of a person, password-like text, a work-schedule screenshot and other material with uncertain provenance or publication rights;
- removed duplicated copies of that media from the user temporary area;
- removed generated Muminki PyInstaller build output, cache files, reports, package files and the compiled executable; some build metadata contained local development paths;
- preserved two text files after manual review established that their scanner hits were false positives: one ordinary reference to a public diagnostic test and one 11-digit sequence occurring inside a public legal-document URL.

No Git-history rewrite was performed. Historical retention and current-tree publication are treated separately.

## Final verification

The final automated pass considered 36 targeted text files and reported only the two manually reviewed false positives described above.

It reported:

- no email-address hits;
- no international-phone hits;
- no remaining flagged media, archives, IDE databases, build output or executables in the targeted scope;
- no unreadable files;
- two known text-pattern hits with non-personal context.

## Decision

The targeted **current-tree personal-data and unsafe-public-material review is complete** for Repository Preview.

The result does not assert that every item in historical Git commits is suitable for republication, and it is not a legal or forensic certification. New material remains subject to repository quality checks, secret scanning, review requirements and the security-reporting process.

## Limits

This review does not cover:

- personal data that may exist only in old Git history and is not present in the current tree;
- external Drive, DevOps, local-device or backup content except where covered by separate audits;
- metadata retained by external hosting or collaboration platforms;
- identity or rights claims that cannot be inferred from the files themselves.
