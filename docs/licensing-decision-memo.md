# Aspiland licensing decision memo

Status: decision preparation; non-canonical; no license applied  
Prepared: 2026-07-16

This memo reduces the licensing decision to a small set of explicit choices. It is not legal advice and does not grant rights to any repository content.

## Current position

No root `LICENSE`, `LICENSE.md` or `LICENSE.txt` was identified during the repository review. Public visibility on GitHub allows viewing and forking under GitHub's platform terms, but without an explicit license default copyright rules otherwise apply. Publishing a repository is therefore not the same as granting broad permission to reuse, modify or redistribute its contents.

Aspiland is a mixed repository containing software, documentation, public communication, artwork or brand material, historical records, user-area material and possible third-party content. A single blanket license should not be applied until ownership and provenance are confirmed for the covered paths.

## Option A — staged split licensing

**Recommended working direction, subject to rights review.**

- Original software intentionally cleared for open-source release: **Apache License 2.0**.
- Original current documentation and public text intentionally cleared for reuse: **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
- Brand names, marks and logos: excluded from the content license except for ordinary attribution and descriptive reference.
- `archive/`, legacy directories, `users/`, historical chat, third-party assets and content with uncertain authorship: **not licensed by the new repository notice** until individually cleared.
- Generated binaries and runtime state: removed or classified rather than licensed as maintained source.

Why this may fit:

- Apache-2.0 provides an explicit patent grant and contribution terms for software.
- CC BY 4.0 is designed for shareable creative and documentary material with attribution.
- Explicit exclusions avoid pretending that the repository owner can license material whose rights or authorship are uncertain.

Costs:

- more files and notices to maintain;
- GitHub may not display one simple repository-wide license label;
- contributors need clear path-level guidance.

## Option B — simple permissive code license

Apply the **MIT License** only to a clearly enumerated set of original software paths and keep all other material excluded until reviewed.

Why this may fit:

- short and widely understood;
- permits use, modification, distribution and sublicensing while retaining copyright and license notices;
- easier administration than Apache-2.0.

Costs:

- no express patent grant comparable to Apache-2.0;
- still requires path-level exclusions for mixed historical and creative material;
- does not solve artwork, brand, archive or publication-rights questions.

## Option C — remain unlicensed during Repository Preview

Keep the current default-copyright position while provenance, privacy and contributor rights are reviewed.

Why this may fit:

- avoids granting rights the owner may not hold;
- safest for uncertain historical and user-contributed material;
- compatible with a read-only Repository Preview framing.

Costs:

- external contributors and users do not receive clear permission to reuse or redistribute the work;
- the repository should not be promoted as open source;
- contribution expectations remain ambiguous unless submissions include explicit terms.

## Recommended staged decision

1. Keep the repository as **Repository Preview / not yet generally licensed**.
2. Inventory authorship and third-party material by path.
3. Identify a narrow first set of files that the repository owner unquestionably controls.
4. Apply a software license only to cleared software paths.
5. Apply a content license only to cleared documentation and public materials.
6. Add explicit exclusions for archive, user areas, third-party assets, brands and uncertain works.
7. Add contributor terms before accepting substantial external contributions.
8. Revisit whether the project needs professional legal review before formal launch.

## Owner decision required later

The owner must eventually choose:

- **A:** staged Apache-2.0 + CC BY 4.0 with exclusions;
- **B:** staged MIT for cleared code, with other content reserved;
- **C:** no license until more provenance work is complete.

No option should be activated while the owner is impaired, under time pressure or unable to review the covered paths.

## Implementation checklist after a decision

- [ ] confirm the copyright holder name and year range;
- [ ] list exactly which paths are covered;
- [ ] list excluded legacy, user, brand and third-party paths;
- [ ] add the official license text without modifying it;
- [ ] add `NOTICE` or attribution files where required;
- [ ] update README and contribution guidance;
- [ ] document treatment of past and future contributions;
- [ ] verify dependency and asset licenses;
- [ ] record the owner decision and reviewed commit;
- [ ] obtain professional advice if ownership or contributor rights remain unclear.

## Primary references

- GitHub Docs, “Licensing a repository”: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
- Open Source Initiative, MIT License: https://opensource.org/license/mit
- Apache Software Foundation, Apache License 2.0: https://www.apache.org/licenses/LICENSE-2.0
- Creative Commons, CC BY 4.0: https://creativecommons.org/licenses/by/4.0/
