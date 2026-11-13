# Plan: rolling out the Samman design system

How to bring [design_system.html](design_system.html) into the site, ending with light and dark mode.

## Status (13 November 2026)

| Phase | Status |
|---|---|
| 1. Tokens and base styles | Done |
| 2. Migrate the components | Done |
| 3. Enforce the rules and clean up | Done |
| 4. Turn on dark mode | Started |
| 5. Keep the design system doc honest | Not started |

Done for Phase 3: `_colors.scss`, `$primary-color`, the `.banner` rules and `_sass/_site/` are gone. `tests/test_no_hard_coded_colours.py` fails on any hex, `rgb()`/`hsl()` or named colour, or old `$brand` variable, in `_sass` outside `_tokens.scss`.

Already in place for Phase 4: the light/dark switch in the nav (`assets/js/theme_toggle.js`), and the HubSpot forms follow the theme (`assets/js/hubspot_form_theme.js`, checked by `tests/test_hubspot_form_theme.py`). Still to do:

1. Set `$dark-mode-follows-os: true` in `_tokens.scss`. It is `false`, so only the switch turns dark mode on.
2. Add the `color-scheme` meta and per-scheme `theme-color` metas to `head.html`. `theme-color` is still a single `#ffffff`.
3. Check content images on navy, click through the key page types in both themes, and run `style_audit.py --dark` (see Phase 4 below).

Answered open questions: 2 (there is a visible switch) and 6 (dark-mode links use light blue).

Not in the phases yet: the Home tab sits against the left edge of the nav bar, because the nav is `text-align: justify` with no side padding. About 10px of side padding on the desktop nav would fix it.

## What I found

- **There is one base layout.** Every layout chains to `_layouts/default.html`, so the `.site` wrapper, the theme hook on `<html>` and the dark-mode meta tags each go in one place.
- **Colours are hard-coded throughout the Sass.** About 970 lines use `$coral`/`$dark-blue` and literals such as `#f6f8fa`, `#6a737d` and `white`. The migration map in the design system already covers most of them.
- **The old class names are used in 23 files.** The biggest are `_layouts/member.html`, `_layouts/coaching_offer.html`, `index.md`, `society/offers/index.md` and `society/events/*.md`.
- **JS and tests depend on the old class names:**
  - `copy_code.js` and `copy_markdown.js` toggle `copied`/`error`.
  - `_includes/search.html` toggles `active`.
  - `test_copy_markdown_button.py` and `test_upcoming_events.py` match exact class markup with regexes.
  - `test_search_bar.py` uses the ids, which we keep.
- **The tooling is fine.** Jekyll uses dart-sass (`sass-embedded`), so `@use`, CSS custom properties and `color-mix()` all work.

### What the running site actually renders

`_tools/style_audit/style_audit.py` loads 22 representative pages in headless Chrome and tallies the computed styles. The site is already fairly consistent:

- **Colours:** 4 text colours (navy, off-white, coral, and black in the search box) and 6 backgrounds. Three of the backgrounds appear on one or two pages only: the 45% white overlay on the offers cards, light blue on the date badge, and `#f6f8fa` on code blocks.
- **Fonts:** Inter and Neulis Sans, plus Arial at 13.3px in the search box and the code copy button. Those are browser defaults for form controls, which don't inherit the page font.
- **Sizes:** 16, 24 and 32px cover almost all text. One-offs are 12, 13.6, 14.4, 15.2, 18.4 and 18.72px. `h3` is 18.4px in event cards and on the offers page and 18.72px elsewhere.
- **Radii:** 5, 6, 10, 4 and 8px.
- **Contrast:** the only failing text is the nav, at 2.2:1 (off-white on coral, and coral on off-white for the current tab).
- **Page hygiene:** almost no inline styles (one each on newsletter and contact). `404.html` has its own `<style>` block and no `<title>`.
- **Mobile:** nothing overflows at 390px wide.
- **Dark mode today:** the site ignores `prefers-color-scheme`, has no `color-scheme` meta, and has `theme-color` set to `#ffffff`.

These gaps aren't covered by the design system draft yet:

1. Form controls (search input, copy button) need an explicit `font: inherit` and colour tokens, or they stay black-on-white in dark mode.
2. The footer divider is the browser-default `<hr>` (1px inset grey) on most pages. It needs a border token.
3. The offers cards' `rgba(255,255,255,.45)` overlay will look like a grey wash on navy. It should be a surface token, not transparency.
4. The light-blue button border is 1.8:1 against white. Non-text UI should reach 3:1.
5. The code background `#f6f8fa` is the only cool grey on a warm palette. It's fine to keep, but it's a one-token change if wanted.
6. Coral on navy is only 4.2:1, so coral can't be the dark-mode link colour as it is.

## Phases

Each step leaves the site working, and `./build_and_test` runs after each one. Each step is its own commit, using Risk-Aware commit notation.

Run the style audit before starting and after each step, and compare the reports. In Phase 1 the light-mode report should not change at all. From Phase 2 on, the number of distinct values should only go down.

### Phase 1: Tokens and base styles (light mode looks the same)

1. **Add `_sass/_tokens.scss`.** It holds the brand palette, type, spacing, radius and motion tokens, plus the light semantic tokens, all as CSS custom properties. The dark tokens go in a Sass mixin that is included twice, under `@media (prefers-color-scheme: dark) :root:not([data-theme=light])` and under `:root[data-theme=dark]`. That way the "keep both blocks identical" rule can't drift. For now only the `data-theme="dark"` selector is switched on, so dark mode can be tested by hand without visitors seeing it.
2. **Add `_sass/_base.scss`.** It takes over the element defaults from section 2 of the design system and replaces the `body`, `a` and `h*` rules in `main.scss` and the prose rules in `_code.scss`. The focus mixins switch to `var(--color-focus)`. The `:focus` fallback can go, since every browser now supports `:focus-visible`.
3. **Add `_sass/_layout.scss`.** It holds `.site`, `.wrapper`, `.stack`, `.cluster`, `.split` and `.grid-cards`. In `default.html`, the content gets wrapped in `<div class="site">` and the `max-width` comes off `<body>`.

### Phase 2: Migrate the components

One component per step, changing the Sass, the markup, the JS and the tests together:

| Step | Sass | Markup / JS / tests |
|---|---|---|
| a. Buttons (`.btn`, `--sm`, `--icon`, `--overlay`, `is-success`/`is-error`) | `_mixins.scss` (drop `pill-button`), `_code.scss`, `_copy_markdown.scss` | `copy_code.js` (plus `currentColor` SVGs), `copy_markdown.js`, `copy_markdown_button.html`, `test_copy_markdown_button.py` |
| b. Panels and cards | `_card.scss` | `society/offers/index.md`, `coaching_offer.html`, `test_offers.py` |
| c. Events and date badge | `_events.scss` | `index.md`, `society/events/*.md`, `test_upcoming_events.py` regex |
| d. People (avatar, person-row, profile-hero) | `_member.scss` | `member.html`, `coaching_offer.html` |
| e. Site chrome (header, nav with `.is-current`, search with `.is-active`, footer, licence box) | `main.scss`, `_navigation.scss`, `_print.scss` | `navigation.html`, `search.html`, `header.html`, `footer.html`, `society_footer.html` |
| f. Images | `.book-cover`, `.centered-image` | `society/contributors/emilybache.md` (`{: .book-cover}`) |
| g. Forms and rules (`font: inherit` on inputs and buttons, `hr` border token) | `_base.scss` | none |
| h. 404 page (move its `<style>` into the Sass, add a title) | `_layout.scss` | `404.html` |

Step a covers the copy button font and step e covers the search input font. Step b replaces the offers card overlay with a surface token.

The visual changes listed under "Deliberate visual changes" in the design system land here.

### Phase 3: Enforce the rules and clean up

- Delete `_colors.scss` as a shared import (the brand values live only in `_tokens.scss`), plus `$primary-color`, the unused `.banner` rules and the untracked `_sass/_site/` leftovers.
- Add a small pytest that fails if any `_sass` file other than `_tokens.scss` contains a colour literal or a `$brand` variable. This enforces principle 5 automatically.

### Phase 4: Turn on dark mode

- Switch on the `prefers-color-scheme` block.
- Add `<meta name="color-scheme" content="light dark">` and per-scheme `theme-color` metas to `head.html`.
- Check content images on navy, such as diagrams with transparent backgrounds and `rose_pattern_handout.svg`. This is the main risk; see question 3.
- Click through the key page types in both themes: home, offers, member, events, kata, learning hour, code smell and search.
- Run `style_audit.py --dark`. The low-contrast list should be empty, or contain only the pairs we've accepted (see question 4).

### Phase 5: Keep the design system doc honest

Change `_docs/design_system.html` to link to the built `/assets/css/styles.css` and keep only its `ds-*` styles. Then the reference page always shows the real CSS instead of a copy that can drift.

## Open questions

1. **Rollout:** should dark mode go live only at Phase 4, after everything is migrated (recommended)? The alternative is switching it on as soon as the tokens land, accepting some half-migrated pages for a while.
2. **Theme toggle:** should the site just follow the OS setting, or have a visible Auto/Light/Dark switch in the header? The `data-theme` hook already supports one. It would need a small script in `<head>` so the page doesn't flash the wrong theme while loading.
3. **Content images in dark mode:** should all images in page content get a light backing (an off-white background with padding and radius) in dark mode? It's a simple, safe default. The alternative is checking images one by one and only fixing the ones that look bad.
4. **The two open contrast decisions in the design system:**
   - Should nav links become dark blue on coral? That's 4.2:1, and it needs bigger nav text to fully pass.
   - Should link hover keep coral and add a thicker underline?

   Both stay as they are unless decided otherwise.
5. **Publishing the reference page:** should the design system page stay private in `_docs/`, or be published at something like `/design-system/`?
6. **Accent colour on navy:** coral on navy is 4.2:1. In dark mode, should links use a lightened coral (about 5:1 or better), or off-white with a coral underline? This is needed before Phase 4.
7. **Light-blue button border:** it is 1.8:1 against white, below the 3:1 that non-text UI needs. Should we darken the border, or accept it because the label carries the meaning?
