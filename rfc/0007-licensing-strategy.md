# RFC 0007 — Licensing strategy for mixed historical material

Status: Proposed  
Proposed: 2026-07-12

## Purpose

Define a lawful and understandable licensing strategy before Aspiland announces reuse rights for a repository containing software, governance documents, research notes, artwork, conversations, generated artifacts and historical contributions.

## Decision required from the repository owner

Licensing changes legal permissions and cannot be inferred from public visibility, repository ownership or operational stewardship. This RFC therefore presents a proposed structure but does not select or apply licenses without explicit owner approval and confirmation of rights.

## Proposed classification

### New original software

Use a clearly identified open-source software license selected by the owner after considering attribution, patent terms, compatibility and desired commercial reuse.

Candidate families for explicit decision:

- permissive, such as MIT or Apache-2.0;
- reciprocal, such as GPL-family licenses;
- project-specific closed or source-available terms when open-source reuse is not intended.

No candidate is adopted by this RFC.

### New documentation and governance text

Use a documentation or content license selected independently from the software license. A Creative Commons license may be considered, with an explicit decision about attribution, commercial reuse and derivative works.

No Creative Commons license should be applied to software code.

### Research data and generated outputs

Document dataset provenance, upstream terms, privacy constraints and whether the output is copyrightable or redistributable. Do not assume that generated output is free of third-party rights or confidentiality restrictions.

### Artwork, logos, fictional material and merchandise designs

Keep all rights reserved unless the owner or verified creator explicitly chooses a reuse license. Trademark-like identifiers and branding may require separate rules from copyright licensing.

### Historical contributions and conversations

Do not retroactively license another person's identifiable contribution without evidence of permission or a valid contribution agreement. Public availability is not the same as permission for unrestricted reuse.

Historical material with unclear rights should be labeled `rights unclear — no additional permission granted` until reviewed.

### Third-party material

Retain only when redistribution is authorized. Record source, author, applicable license, required attribution and modifications. Links are preferable to copied material when redistribution rights are unclear.

## Proposed repository files

After explicit decisions and rights review, add:

- root `LICENSE` only when one license accurately covers the defined default scope;
- `LICENSES/` for multiple license texts where necessary;
- `REUSE.toml`, SPDX headers or an equivalent machine-readable mapping if practical;
- `NOTICE` for attribution and third-party notices;
- `docs/licensing.md` explaining path-level exceptions and historical material;
- contributor terms appropriate to the selected licenses.

## Default before acceptance

Until licenses are explicitly applied, repository publication grants only rights provided by applicable law and GitHub platform terms. It must not be described as open source merely because the repository is public.

## Migration

1. Inventory files by creator, date, content type and known source.
2. Separate generated artifacts and copied third-party content.
3. Identify material created solely by the repository owner.
4. Contact other contributors where necessary and proportionate.
5. Choose licenses for new code, documentation and artwork separately.
6. Add machine-readable path mappings and attribution.
7. Label unresolved historical material conservatively.
8. Recheck the public launch note and contribution process.

## Risks

- applying an overbroad root license to material the owner cannot license;
- incompatible terms between code and dependencies;
- accidental licensing of personal communications or private data;
- ambiguity about logos, names and commercial merchandise;
- discouraging contribution through unclear or excessively complex terms.

## Rollback

Licenses already granted may not always be revocable for existing recipients. For that reason, implementation requires deliberate owner approval and a rights inventory before publication. Corrections should narrow future distribution honestly without claiming that past grants disappeared.

## Decision record

No licensing decision yet. Explicit owner approval is required before adding license texts or announcing reuse permissions.
