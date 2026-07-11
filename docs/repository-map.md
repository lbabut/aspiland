# Repository map

This map distinguishes current structure from legacy material. It is descriptive, not canonical law.

## Current structure

| Path | Purpose |
| --- | --- |
| `canon/` | Explicitly accepted governance documents |
| `rfc/` | Proposals and decision records |
| `protocols/` | Change, consent, review and rollback procedures |
| `projects/` | Active experiments and software projects |
| `archive/` | Preserved legacy and superseded material |
| `public/` | Material reviewed for unrestricted publication |
| `docs/` | Repository-wide explanatory documentation |

## Legacy structure under review

| Path | Current interpretation | Planned treatment |
| --- | --- | --- |
| `AspieLand_TheUnitedStatesOfMinds/` | Early constitutional experiment | Preserve; review through RFC before declaring anything canonical |
| `AspieLanguage/` | Language experiment | Preserve as a project or archive after inventory |
| `Embassies/` | Early organizational model | Preserve; classify records and remove private operational assumptions |
| `SharedAssets/` | Shared project material | Inventory by project and data sensitivity |
| `users/` | User areas and experimental software | Review carefully for personal data, generated output and active projects |
| `PublicChat.txt` | Historical public conversation log | Preserve as legacy material; do not treat as current project communication |
| `muminki_world/` | Artificial-life experiments | Consolidate under a documented project after code and data review |
| `.vs/` | Visual Studio-generated state | Remove from the current tree after file inventory; history remains in Git |

## Known hygiene work

- Stop tracking IDE metadata, Python caches, PyInstaller output and generated runtime state.
- Replace the historical root README with a current project overview.
- Document the Muminki runtime and dependencies.
- Review tracked build artifacts under `users/Muminki/build/` and `dist/` before removal.
- Review user directories for information that should not be permanently public.
- Avoid history rewriting unless a confirmed secret requires emergency removal.

## Rule for migration

Copy or document legacy material before moving it. Delete generated artifacts only after confirming that reproducible source and build instructions exist.
