# Aspiland project inventory

Status: descriptive working inventory; non-canonical  
Last reviewed: 2026-07-12

This inventory identifies active and legacy areas for go-live review. `Active` means intentionally maintained or presented as current; it does not imply production support.

## Current projects

| Project | Path | Status | Runtime | Network or persistent data | Go-live note |
| --- | --- | --- | --- | --- | --- |
| UNIVERSE / MERCY | `projects/universe-mercy/` | Conceptual ethical thought experiment | None documented | None documented | Suitable for repository publication with its explicit hypothetical boundary. |
| Sandbox Detection | `projects/sandbox-detection/` | Conceptual research project | Analysis implementation not yet present | Intended future datasets and analysis outputs | Research framing is clear; future implementations need data-source, dependency and reproducibility records. |

## Legacy areas requiring classification

| Area | Current interpretation | Priority review |
| --- | --- | --- |
| `muminki_world/` | Artificial-life experiments | Source, dependencies, serialized state, unsafe pickle handling, generated data and migration into a documented project. |
| `users/Muminki/` | User-scoped Muminki implementation and generated output | API configuration, dependencies, build artifacts, runtime state, external services and personal-data assumptions. |
| `users/` excluding Muminki | Historical user areas and private-project experiments | Personal data, authorship, publication consent, active source versus abandoned material. |
| `AspieLanguage/` | Language experiment | Authorship, scope, documentation and archive-versus-active status. |
| `Embassies/` | Historical organizational metaphor and records | Personal or operational details, legal-status ambiguity and rights to publish. |
| `SharedAssets/` | Mixed shared project material | Ownership, licensing, personal data, binaries and project attribution. |
| `AspieLand_TheUnitedStatesOfMinds/` | Early constitutional experiment | Canonical status is already separated; continue provenance, translation and supersession review. |
| `PublicChat.txt` | Short historical public-chat record | Preserve as legacy only after confirming publication rights and whether nicknames or statements need contextualization. |
| `.vs/`, `build/`, `dist/` | Generated IDE and packaging output | Inventory reproducible source, then remove generated current-tree artifacts. |

## Required project record

Before an area is called active, maintained or supported, record:

- project name, purpose and current status;
- maintainer and succession or archival trigger;
- entry points and supported environments;
- dependencies and build or execution instructions;
- external services and network access;
- persistent data, retention and deletion path;
- credentials and configuration mechanism;
- known security and privacy limitations;
- factual, hypothetical, fictional or artistic claim boundary;
- license and third-party attribution;
- validation and rollback or shutdown procedure.

## Current conclusion

Only the two projects under `projects/` have clear current status pages. Legacy software and user areas must not be described as supported or safe to run until individually reviewed. The repository can launch as an archive and experimental laboratory while clearly labeling these limitations.
