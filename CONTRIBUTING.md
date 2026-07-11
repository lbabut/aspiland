# Contributing to Aspiland

Aspiland contains governance documents, historical records and experimental software. Changes should make the repository easier to understand without rewriting its history.

## Choose the correct area

- Binding governance belongs in `canon/` only after acceptance.
- Proposed governance changes begin in `rfc/`.
- Procedures belong in `protocols/`.
- Software and research belong in `projects/` or an identified legacy project area.
- Superseded material belongs in `archive/`.
- Material intended for unrestricted distribution belongs in `public/`.

## Change rules

1. Keep changes small and explain their purpose.
2. Do not commit passwords, API keys, private infrastructure details or unnecessary personal data.
3. Do not commit generated build output, caches, virtual environments or runtime state.
4. Preserve historical material before moving or replacing it.
5. Distinguish factual claims from fiction, satire, hypotheses and experiments.
6. Include a rollback path for consequential governance or structural changes.

## Software changes

- Add dependency instructions close to the project.
- Prefer reproducible source over generated executables.
- Keep generated files out of Git.
- Document external network access and persistent local data.
- Never deserialize untrusted pickle files.

## Governance changes

Create a numbered RFC containing:

- status,
- purpose,
- proposed change,
- affected users or systems,
- risks,
- migration plan,
- rollback plan,
- decision record.

A merged proposal does not become canonical unless its acceptance and effective date are explicitly recorded.
