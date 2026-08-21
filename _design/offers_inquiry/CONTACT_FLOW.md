# Handoff: Contact / Inquiry Flow (sammancoaching.org)

## Overview
Make it easy for interested visitors to take the next step: one **central inquiry** that reaches the whole society (via HubSpot), instead of hunting down individual coaches. Approved designs (see `Offers Page.dc.html`, top section of the canvas):

- **2a — Inquiry page** (`/society/offers/inquiry.html` or similar): "how it works" steps + the central form
- **2b — Offer detail pages get an inquiry CTA panel** above the coach list
- **2c — Thank-you page**: sets expectations, links for while-you-wait

The offers pages themselves (designs 1a/1c) are already implemented in the repo.

## About the design file
`Offers Page.dc.html` is a **design reference**, not production code. Open it in a browser (assets included in this folder). The top section is the contact flow (2a/2b/2c); the section below is the earlier, already-implemented offers redesign (1a/1b/1c). The form in 2a is interactive — click the chips to see the conditional behavior.

## The flow
Offers index → offer detail page → **"Start an inquiry"** (offer pre-selected) → thank-you page.
Entry points for the CTA: each offer detail page (2b panel), the offers index footer note, and optionally the contact page.

## Form fields (2a)
- Name, Work email
- **Company, Job title**
- Timezone (select: Europe / Americas / Asia-Pacific / Other)
- **Engagement type** (Samman Coaching / Personal Coaching / Train the Trainer) — pre-selected when arriving from an offer detail page (e.g. query param)
- **Size — adaptive label**: "Number of teams" (1 / 2–5 / 6+ teams) normally; "Number of people to coach" (1 / 2–5 / 6+ people) when Personal Coaching is selected
- **Coaching format** (Remote / In-person / Hybrid) — selecting In-person or Hybrid **reveals a Location field** (city, country)
- Coaching priority (Legacy code / AI adoption / Other)
- Free-text message (optional)

Microcopy next to submit: "Goes to the society, not a mailing list. We reply within a few days."

## Thank-you page (2c)
Checkmark, "Inquiry sent", expectation-setting ("a coach will reach out within a few days for a free intro call"), and a "While you wait" box linking to how Samman works, the coaches, and the newsletter.

## Backend
- Form submissions land in HubSpot CRM as contacts + trigger workflows.
- **Discord notification**: use a HubSpot workflow with a webhook action posting to a Discord channel webhook URL on each submission (webhook actions require Operations Hub; alternatively use Zapier/Make, or a tiny serverless function as the form's POST target that forwards to both HubSpot and Discord).

## HubSpot implementation — three options

### Option A (recommended): custom form + HubSpot Forms Submission API
Build the form exactly as designed in plain HTML/JS in the Jekyll page; POST to
`https://api.hsforms.com/submissions/v3/integration/submit/{portalId}/{formGuid}`.
- Only route that reproduces the design pixel-perfectly (chips, conditional Location field, adaptive size label).
- Create a matching form in HubSpot with the same field names (use custom contact properties for timezone, engagement, size, format, location, priority).
- Include `hutk` cookie value in the submission context for analytics attribution; add the HubSpot tracking code to the page.
- You own client-side validation and spam protection (add a honeypot; HubSpot also does server-side filtering).

### Option B: raw-HTML embed of a HubSpot form (Pro/Enterprise required)
New-style forms can be embedded as raw HTML (Developer code / Advanced tab) — no iframe, so the site's CSS styles the form directly (target `.hs-input`, `.hs-button`, etc. in `_sass/`).
- ~90% fidelity: chips become radio buttons/selects unless you add JS on top.
- Conditional fields (Location, adaptive size label) are configured as HubSpot dependent fields.
- HubSpot owns validation, spam, and field rendering — less code to maintain.

### Option C: standard JS embed + CSS overrides (free tier fallback)
`hbspt.forms.create({ ..., target: '.inquiry-form' })` with CSS overrides scoped to the wrapper. Fragile (HubSpot may override styles; new-editor iframe forms can't be styled externally). Only if A and B are unavailable.

**Decision guide**: dev capacity + want the exact design → A. Prefer HubSpot owning the form → B.

## Styling notes (matches existing site SCSS)
- Form card: 2px `#e8e8e8` border, 10px radius, `rgba(255,255,255,0.45)` bg, padding ~26px 28px, max-width 620px
- Inputs: white bg, 2px `#e8e8e8` border, 6px radius, padding 10px 12px, focus border `rgb(162,195,221)`, Inter 16px, dark-blue text
- Chips (radio-as-buttons): 2px border, 6px radius, padding 8px 14px; selected = dark-blue border + light-blue `rgb(162,195,221)` bg; hover = dark-blue border
- Primary CTA ("Send inquiry" / "Start an inquiry"): dark-blue `rgb(23,64,100)` bg, off-white text, 6px radius, hover `rgb(65,103,136)`
- CTA panel (2b): 2px `rgb(162,195,221)` border, `rgba(162,195,221,0.25)` bg, 10px radius
- Steps (2a): numbered 34px dark-blue circles, Neulis Sans headings
- Thank-you icon: 64px light-blue circle + dark-blue checkmark

## Cleanup (from earlier review)
The old `_offers/` collection, `_layouts/offer.html`, and the offers collection entry in `_config.yml` are dead code — nothing references them, but Jekyll still builds orphan pages from them. Remove.

## Suggested Claude Code prompt
> Read design_handoff_offers_page/CONTACT_FLOW.md and implement the inquiry flow: an inquiry page (design 2a) using Option A (custom form posting to the HubSpot Forms Submission API), an inquiry CTA panel on each coaching_offer page (design 2b), and a thank-you page (design 2c). Open "Offers Page.dc.html" for the visual reference — the top canvas section shows 2a/2b/2c. Reuse existing SCSS; match the styling notes. Also remove the dead _offers collection. Ask me for the HubSpot portal ID and form GUID.
