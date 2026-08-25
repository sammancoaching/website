# Handoff: Offers Page Redesign (sammancoaching.org)

> **Superseded** — designs 1a/1c below are already implemented in this repo.
> The active handoff is [CONTACT_FLOW.md](CONTACT_FLOW.md) (inquiry flow, designs 2a/2b/2c).

## Overview
Replace the current offers page (a grid of individual, time-limited coach offers) with three **service categories** — Samman Coaching for Teams, 1:1 Personal Coaching, and Train the Trainer — each linking to a detail page listing the society members who offer that service. This implements the two related items in `NextSteps.md`.

Approved designs: **1a** (offers page as a 3-card grid) and **1c** (per-service coach-list detail page).

## About the Design Files
`Offers Page.dc.html` in this bundle is a **design reference created in HTML** — a prototype showing intended look and behavior, not production code to copy directly. The task is to **recreate designs 1a and 1c in the existing Jekyll codebase** (`sammancoaching/website`), using its established Liquid layouts, SCSS partials, and data files. Ignore mockups 1b and the mockup chrome (badges, canvas background).

## Fidelity
**High-fidelity.** The mockups reuse the site's real fonts, colors, header/footer chrome, and existing `.card` / `.button` styles. Recreate closely — most styling already exists in `_sass/`.

## Target codebase facts (verified against the repo)
- Jekyll site; offers page lives at `society/offers/index.md` (layout `default`).
- Individual offers are a collection in `_offers/` with layout `_layouts/offer.html` — **both become obsolete** (user decision: drop individual time-limited offers entirely).
- Coach data: `_data/contributors.yml` (keys like `emilybache`, with `title`, `url`, `affiliation`, `member`, optional `headline`, `photo`).
- Styles: `_sass/_card.scss` (`.card-grid`, `.card`, `.ribbon`, `.button`), `_sass/_colors.scss`, `_sass/_member.scss` (avatar/photo patterns), `_sass/_variables.scss`.
- Colors: coral `rgb(240,130,113)`, dark-blue `rgb(23,64,100)`, off-white `rgb(243,238,230)`, light-blue `rgb(162,195,221)`.
- Fonts: Inter (body), Neulis Sans SemiBold (headings) — already set up in `_sass/_fonts.scss`.

## Suggested implementation plan (for Claude Code)
1. **Tag coaches with services.** Add an `offers` list to entries in `_data/contributors.yml`, e.g.:
   ```yaml
   emilybache:
     title: Emily Bache
     ...
     offers: [teams, personal, train_the_trainer]
   ```
2. **Define the three services** in a new `_data/coaching_offers.yml`: key, title, description, slug. Copy below.
3. **Rewrite `society/offers/index.md`** (design 1a): h1 "Hire a Technical Coach", intro paragraph, `.card-grid` with one `.card` per service. Each card: uppercase h2 title, description, optional "N coaches offer this" (count contributors whose `offers` contains the key), and a `.button` "See the coaches" linking to the detail page. No ribbons.
4. **Add detail pages** (design 1c), e.g. `society/offers/teams.md` etc. sharing one new layout `_layouts/coaching_offer.html` that:
   - shows a back link "← All coaching offers", h1, intro;
   - loops `site.data.contributors`, filtering `member == 'yes'` and `offers contains page.offer_key`;
   - renders each coach as a row: 64px photo (if `photo` set, styled like `.member-hero__photo`) or an initials tile (light-blue bg, dark-blue Neulis initials), name, affiliation, optional `headline`, and a `.button` "Website" → contributor `url`;
   - cross-links the other two services at the bottom.
5. **Remove** the `_offers/` collection, `_layouts/offer.html`, and the offers collection config in `_config.yml`; redirect or update any links.
6. Keep navigation ("Society" is the current section) and footer untouched.

### `_data/coaching_offers.yml` (proposed content)
```yaml
teams:
  title: Samman Coaching for Teams
  slug: teams
  description: >-
    The classic format: a block of 10 Samman sessions for a dev team that
    works together, combining learning hours and ensemble working.
personal:
  title: "1:1 Personal Coaching"
  slug: personal
  description: >-
    For tech leads and architects with an ambition to become technical
    coaches. Regular coach-the-coach sessions alongside our training courses.
train_the_trainer:
  title: Train the Trainer
  slug: train_the_trainer
  description: >-
    For organisations that want to roll out technical coaching as a career
    path across whole departments. A programme that grows coaches in-house.
```

## Screens / Views

### 1a — Offers index (`/society/offers/`)
- h1 (2em, Neulis Sans 600): "Hire a Technical Coach"
- Intro paragraph (max-width ~620px): "Technical skills have to be acquired deliberately, and the best effect comes from lifting the entire team at the same time. Members of the Samman Technical Coaching Society offer three kinds of coaching."
- 3-column card grid (existing `.card-grid`, gap ~34–40px). Card: existing `.card` (2px `#e8e8e8` border, 10px radius, centered text, hover → dark-blue border + `0 4px 12px rgba(23,64,100,0.15)` shadow), plus a subtle `rgba(255,255,255,0.45)` background used in the mock.
- Card contents top→bottom: uppercase h2 (~1.1em), description, muted coach count (0.85em, 75% opacity), `.button` "See the coaches".
- Below grid: "Not sure which fits? Get in touch via our contact page." (0.9em, links to `contact.md`).

### 1c — Service detail (e.g. `/society/offers/teams.html`)
- Back link (0.9em): "← All coaching offers"
- h1: service title; intro paragraph ending "These society members offer team coaching:"
- Coach rows, vertical stack (gap 18px). Row: grid `64px 1fr auto`, gap 18px, align center, same card border/hover treatment, padding 16px 20px.
  - Avatar: photo 64×64, 6px radius, 2px dark-blue border; fallback initials tile 64×64, light-blue bg, dark-blue Neulis 22px.
  - Middle: name (Neulis 600, 1.15em), affiliation (0.85em, 75% opacity), optional headline (0.95em).
  - Right: `.button` "Website" → contributor url.
- Footer line: "Also on offer: [other service] and [other service]."

## Interactions & Behavior
- Card and row hover: border-color → dark-blue + shadow (existing `.card:hover` transition, 0.3s ease).
- Button hover: light-blue background, dark-blue text (existing `.button:hover`).
- All navigation is plain links; no JS required.
- Coach count and coach lists are computed from data at build time — no hardcoded names in templates.

## Design Tokens
All existing in `_sass/`: colors above; `.button` = 0.5rem 1rem padding, 6px radius, white bg, light-blue text + 2px light-blue border; card radius 10px; content width 750px.

## Placeholder data — needs real input
The mock's service-to-coach tagging is **invented**. Before shipping, confirm with members who actually offers what. Mock used: Teams → Bache, Ördög, Ytterbrink, Sudbery, Riegler, Avni; Personal → Bache, Ördög, Eckart; Train the Trainer → Bache, Sudbery.

## Assets
No new assets. Uses existing repo assets: `assets/images/samman_banner.png`, `assets/images/profiles/ivett.jpg`, `assets/images/Submark_dark_blue_small.png`, fonts in `assets/fonts/`.

## Files
- `Offers Page.dc.html` — the design reference (open in a browser; 1a and 1c are the approved mockups; asset paths resolve if placed at repo root, otherwise view the hosted preview).

## Suggested Claude Code prompt
> Read design_handoff_offers_page/README.md and implement designs 1a and 1c in this Jekyll site. Follow the implementation plan: tag contributors with offers in _data/contributors.yml, add _data/coaching_offers.yml, rewrite society/offers/index.md as the three-service card grid, add a coaching_offer layout + three detail pages, and remove the old _offers collection. Reuse existing SCSS; add only minimal new styles for the coach rows and initials tiles. Ask me for the real coach-to-service tagging before finalizing data.
