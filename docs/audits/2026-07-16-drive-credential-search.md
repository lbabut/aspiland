# Connected Drive credential search — 2026-07-16

Status: completed best-effort search of connected Google Drive; non-canonical  
Scope: Aspiland-related files discoverable through the connected Drive search interface

## Search method

The connected Google Drive was searched using narrow project and credential-related terms, including:

- `Aspiland`;
- `dev.azure.com/aspiland`;
- `aspiland azure`;
- `aspiland token`;
- `aspiland key`;
- `aspiland password`;
- `aspiland secret`;
- `aspiland api`;
- the historical candidate filename.

Search results were reviewed without copying any credential value into this repository or into public issue text.

## Result

- One old project document was found containing a link to the Aspiland Azure DevOps organization.
- No duplicate of the historical credential candidate was found by name.
- No Aspiland-related token, password, API-key or secret document was surfaced by the targeted connected-Drive searches.
- The repository owner separately confirmed that the historical pre-2023 candidate is invalid.

## Limits

This is a search-based review of the currently connected Google Drive, not a byte-for-byte forensic scan. It does not cover:

- Azure DevOps repositories, variable groups, pipelines or secure files;
- local phone or computer storage;
- disconnected Google accounts or shared drives outside the connector's visibility;
- old deployment exports, offline disks or independent backup systems;
- secrets stored under unrelated filenames or formats not indexed as searchable text.

## Decision

The connected-Google-Drive portion of the external-store review is complete. Other external stores remain outside the present connector scope and must be reviewed separately or explicitly accepted in a later launch decision.
