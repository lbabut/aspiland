# Aspiland website

Status: formal repository-launch site source  
Last reviewed: 2026-07-16

This directory contains the dependency-free public landing page for Aspiland.

## Files

- `index.html` — page structure and public content;
- `styles.css` and `sections.css` — responsive visual system;
- `app.js` — English and Polish language switching.

## Design constraints

- no external fonts, analytics, trackers or third-party runtime assets;
- no build step or package installation;
- keyboard-accessible navigation and visible focus states;
- reduced-motion support;
- prominent experimental and non-sovereign disclaimer;
- accurate formal repository-launch status without a community-launch claim;
- repository sources linked directly for verification.

## Local preview

Open `index.html` directly or serve this directory with any static HTTP server.

Example:

```bash
python3 -m http.server 8080 --directory site
```

Then open `http://localhost:8080`.

## Deployment

`.github/workflows/pages.yml` packages this directory and deploys it through GitHub Pages after changes reach `main`.

Expected project-site address:

`https://lbabut.github.io/aspiland/`

A custom domain can be considered separately. Domain purchase and DNS changes are outside the scope of this source directory.

## Content governance

The website is public communication material, not canon. When claims or status change:

1. update the authoritative repository document first;
2. update the website copy and the review date;
3. confirm translations still describe the same source state;
4. retain the distinction between accepted, proposed, experimental and archived material;
5. do not remove the experimental disclaimer without a reviewed replacement.