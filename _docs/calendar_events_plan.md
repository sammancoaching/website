# Plan: Replace addcal with self-hosted calendar events

## Goal

Stop depending on [addcal](https://addcal.co) for getting Samman Society events into people's calendars. Instead:

* Define the date and time of each event in **one place** in this repository.
* Generate an **event page** for each event that looks similar to the current addcal pages.
* Let people **download an `.ics` file**, **add the event to their calendar** (Google, Apple, Outlook, Outlook.com, Office 365, Yahoo, Other), or **subscribe** to a feed that follows date changes.

We start with the Open Space event, then migrate the other events.

## Current situation

* `_data/events.yml` holds, for each event, an addcal `ical_url` (`.ics` feed) and a `calendar_link` (the addcal event page).
* At build time the `jekyll-ical-tag` plugin downloads each addcal `.ics` feed. The events list (`society/events/index.md`), the home page (`index.md`), `society/events/next_open_space.md`, `next_ensemble.md`, `next_learning_hour.md`, `ai_coding_dojo.md`, `training/deliver_learning_hours.md` and `training/learning_hours_masterclass.md` all get their dates this way using `{% ical %}`.
* The real date only lives in addcal, and every build needs network access to addcal. If a download fails, `_plugins/ical_tag_patch.rb` swallows the error and the event silently disappears from the site.
* Most events happen once, but the ensemble repeats weekly (`RRULE:FREQ=WEEKLY;COUNT=24;INTERVAL=1;BYDAY=FR`).
* The open space routine (`routines.md`) includes manually updating the addcal link and triggering a rebuild of the site.

The next open space is currently in addcal as **Wednesday 9 December 2026, 16:00–17:00 Europe/Berlin**.

## Decisions

1. **Where events are defined:** front matter of the `_upcoming_events/*.md` files. `_data/events.yml` is removed once every event has been migrated.
2. **Subscribe button:** yes. Each event's `.ics` file always contains the next date under a fixed address, so people can subscribe to it with `webcal://` and their calendar follows date changes automatically.
3. **When the date has passed:** the event page shows "Next date to be announced" and hides the calendar buttons. The subscribe button stays visible.
4. **Scope:** start with the Open Space only. Each of the other events is migrated in a later phase (see below).

## Design

### 1. Event definition (front matter)

Each `_upcoming_events/<key>.md` gets calendar fields alongside the existing listing fields:

```yaml
---
layout: calendar_event
title: Online Open Space Event
event_key: open_space
calendar_title: Samman Society Open Space
start: 2026-12-09 16:00
duration_minutes: 60
timezone: Europe/Berlin
# rrule: FREQ=WEEKLY;COUNT=24;BYDAY=FR   # optional, only for repeating events
location: Online (Zoom link emailed to sign-ups)
calendar_description: |
  If you have signed up on our website, we will email you a zoom link before the meeting starts.

  We also put the zoom link in the #general channel of our Discord server.
audience: Open to All
show_on_homepage: true
description: Bring your questions and exchange experiences with other technical coaches. We'll collaboratively create an agenda and hold discussions in breakout rooms.
details_link: society/events/next_open_space.md
---
```

* `start` is a local time in `timezone`, so daylight saving is handled by the plugin, not by whoever edits the date.
* Note `_config.yml` sets the site `timezone: Europe/Stockholm`. Front matter dates must be read as wall-clock times in the event's `timezone`, not converted by Jekyll. The plugin should parse `start` as a string to avoid YAML/Jekyll turning it into a `Time` in the site timezone. Quote it if needed: `start: "2026-12-09 16:00"`.
* The collection already outputs pages at `/society/events/:name`, so the open space event page becomes `/society/events/open_space.html`.

To move an event to a new date: change `start:` and push to `main`. The deploy GitHub Action rebuilds the site on every push.

### 2. Plugin: `_plugins/calendar_events.rb`

A Jekyll generator that, for each document in `site.upcoming_events` that has a `start` field:

* **Works out the next date** that hasn't ended yet, using `tzinfo` and `ice_cube` (for `rrule`). Both gems are already installed as dependencies of `jekyll-ical-tag`. If `jekyll-ical-tag` is removed, add `icalendar`, `ice_cube` and `tzinfo` to the `Gemfile` directly.
* **Exposes data to Liquid** on the document, e.g.:
  * `next_start`, `next_end` (local `Time` in the event timezone)
  * `next_start_utc`, `next_end_utc`
  * `has_upcoming_date` (false when the date has passed → "to be announced")
  * `ics_url` (`/society/events/<key>.ics`), `webcal_url` (`webcal://sammancoaching.org/society/events/<key>.ics`)
  * `calendar_links` with `google`, `outlook_com`, `office365`, `yahoo`
* **Writes a static file** `/society/events/<key>.ics` using the `icalendar` gem:
  * `VTIMEZONE` for the event timezone (`icalendar` has a `tzinfo` helper for this)
  * fixed `UID` per event, e.g. `open_space@sammancoaching.org`, so re-importing updates rather than duplicates
  * `DTSTAMP` at build time; `SEQUENCE` derived from the start time (e.g. its epoch seconds), so it goes up whenever the date moves later
  * `DTSTART`/`DTEND` with `TZID`, `SUMMARY`, `DESCRIPTION`, `LOCATION`, `URL` (the event page), optional `RRULE`
  * a `VALARM` reminder 30 minutes before, as addcal does
  * `X-WR-CALNAME` / `REFRESH-INTERVAL;VALUE=DURATION:PT12H` / `X-PUBLISHED-TTL:PT12H` so subscribed calendars refresh regularly
  * when there is no upcoming date: an empty `VCALENDAR` (still valid, so subscribers' feeds don't break)
* **Builds the "add to calendar" links** (all values URL-encoded):
  * Google: `https://calendar.google.com/calendar/render?action=TEMPLATE&text=…&dates=YYYYMMDDTHHMMSSZ/YYYYMMDDTHHMMSSZ&details=…&location=…&recur=RRULE:…`
  * Outlook.com: `https://outlook.live.com/calendar/0/deeplink/compose?path=/calendar/action/compose&rru=addevent&subject=…&startdt=…&enddt=…&body=…&location=…`
  * Office 365: the same on `https://outlook.office.com/calendar/0/deeplink/compose?...`
  * Yahoo: `https://calendar.yahoo.com/?v=60&title=…&st=…&et=…&desc=…&in_loc=…`
  * Apple, Outlook (desktop) and Other: the `.ics` download
  * The Outlook.com, Office 365 and Yahoo links can't carry a repeat rule. For repeating events those buttons fall back to the `.ics` download.

Check that the deploy workflow (`jekyll/builder` container running `bundle exec jekyll build --future`) loads `_plugins/` and that the gems are available there. Custom plugins already work there (`timezone_filter.rb`, `connects_index_generator.rb`).

Consider also making `--future` irrelevant: the plugin computes upcoming dates itself, so it doesn't rely on Jekyll's future-post handling.

### 3. Layout: `_layouts/calendar_event.html`

Modelled on the addcal event page:

* Event title (`calendar_title`)
* Date and time, e.g. "Wed, Dec 9, 2026, 4:00 PM – 5:00 PM", with a "Time shown in Europe/Berlin" line
* A short piece of inline JavaScript uses `Intl.DateTimeFormat` to show the time in the visitor's own time zone (rendering from `next_start_utc` in a `data-` attribute). Without JavaScript the page shows the event timezone.
* For repeating events, a line describing the repeat (e.g. "Every Friday")
* `calendar_description`
* "Add to Calendar" buttons: Google, Apple, Outlook (desktop), Outlook.com, Office 365, Yahoo, Other
* A "Subscribe" button (`webcal_url`), with a short explanation that the calendar will follow date changes, and a copyable `https://` feed URL for calendars that don't handle `webcal://` links
* A link to the event's details page (`details_link`)
* When `has_upcoming_date` is false: "Next date to be announced", no add-to-calendar buttons, subscribe button still shown

Styling goes in `_sass`, reusing the existing `.add-calendar-btn` / `.event-links` styles where possible.

### 4. Shared include for pages that show the next date

Add an include, e.g. `_includes/next_event_date.html`, that takes an event key and renders the next date (or "to be announced"). Pages use this instead of `{% ical %}`, which keeps the date formatting consistent.

## Implementation steps

### Phase 1: Open Space

1. Write `_plugins/calendar_events.rb` (next-date calculation, Liquid data, `.ics` generation, calendar links).
2. Write `_layouts/calendar_event.html` and its styles.
3. Add the calendar fields to `_upcoming_events/open_space.md` with `start: 2026-12-09 16:00`, `timezone: Europe/Berlin`, `duration_minutes: 60`, and switch its layout to `calendar_event`.
4. Update the pages that show the open space date so they use the plugin data for events with a `start` field and fall back to `{% ical %}` for events not yet migrated:
   * `society/events/next_open_space.md`: date line and "Add to Calendar" button point at the new event page; add a "Subscribe" link.
   * `society/events/index.md` and `index.md`: in the event loops, use the plugin data when `event_item.start` is set, otherwise keep the existing `{% ical %}` code.
5. Remove `open_space` from `_data/events.yml`.
6. Tests (Python, in `tests/`, run by `./build_and_test`):
   * `_site/society/events/open_space.ics` exists, parses, and has `DTSTART;TZID=Europe/Berlin:20261209T160000`, `DTEND …T170000`, and a stable `UID`.
   * The event page contains all calendar buttons and a subscribe link, and its `.ics` link resolves.
   * The Google link's `dates=` is `20261209T150000Z/20261209T160000Z` (UTC conversion correct).
   * A unit-level test, or a test fixture event, for a date in summer time, to check daylight saving (e.g. 16:00 Berlin in June = 14:00Z).
   * A test fixture event in the past renders "Next date to be announced" and no add-to-calendar buttons.
   * Update `tests/test_upcoming_events.py`, which currently compares dates against a fixed `2026-04-17`; use today's date instead.
7. Manually check the generated `.ics` and buttons in Google Calendar, Apple Calendar and Outlook, and subscribe to the feed in at least one of them, then move the date in front matter and confirm the subscribed calendar updates.
8. Update `routines.md`:
   * Step 4 becomes: "Update `start:` in `_upcoming_events/open_space.md` with the next date and push to `main`".
   * Step 5 (trigger the GitHub action) is no longer needed, since pushing to `main` deploys.
9. Update the open space event in addcal (or its description) to point people to the new event page, so old links still lead somewhere useful.

### Phase 2: Ensemble (repeating event)

1. Add calendar fields to `_upcoming_events/ensemble.md` with `start: 2026-11-13 15:00`, `duration_minutes: 60`, `timezone: Europe/Berlin` and `rrule: FREQ=WEEKLY;COUNT=24;INTERVAL=1;BYDAY=FR` (copy the current values from addcal at the time of migration).
2. Check the plugin's next-occurrence logic for the repeating rule and the repeat description on the event page.
3. Check that the Outlook.com, Office 365 and Yahoo buttons fall back to `.ics` for repeating events.
4. Update `society/events/next_ensemble.md` to use the new event page and include.
5. Remove `ensemble` from `_data/events.yml`; add tests for the `RRULE` in the `.ics` file and the Google `recur=` parameter.

### Phase 3: Learning Hour and AI Coding Dojo

1. Add calendar fields to `_upcoming_events/learning_hour.md` and `_upcoming_events/ai_coding_dojo.md` (copy the current dates from addcal).
2. Update `society/events/next_learning_hour.md` and `society/events/ai_coding_dojo.md`.
3. Remove both from `_data/events.yml`; extend tests.

### Phase 4: Training courses

1. Add calendar fields to `_upcoming_events/deliver_learning_hours.md` and `_upcoming_events/learning_hours_masterclass_training.md`.
   * The masterclass runs over two half-days. Decide whether to model it as two dates (e.g. a list of `dates:` in front matter, generating one `VEVENT` each) or as a single entry for the first session.
2. Update `training/deliver_learning_hours.md` and `training/learning_hours_masterclass.md` to use the include.
3. Remove both from `_data/events.yml`; extend tests.

### Phase 5: Clean up

1. Delete `_data/events.yml`.
2. Remove the `{% ical %}` fallback code from `society/events/index.md` and `index.md`.
3. Remove `jekyll-ical-tag` from the `Gemfile` and `_config.yml` plugins list, delete `_plugins/ical_tag_patch.rb`, and add `icalendar`, `ice_cube` and `tzinfo` to the `Gemfile` directly if the plugin still needs them. Run `bundle install` and update `Gemfile.lock`.
4. Search the site for remaining `addcal` references and update any routines or docs that mention it.
5. Close down the addcal events once their old links are no longer in circulation.
