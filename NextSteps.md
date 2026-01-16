# Next Steps: Add Dynamic Date/Time to Individual Event Pages

## Context

We've successfully implemented dynamic event fetching on the main events listing page (`society/events/upcoming_events.md`). Now we need to add the same dynamic date/time information to the individual event detail pages.

### Current State
- Main events page (`upcoming_events.md`) displays dynamic dates from ICS feeds ✓
- Individual event pages have static/TODO date information:
  - `next_ensemble.md` - has "TODO put date and time here"
  - `next_learning_hour.md` - no date/time shown
  - `next_open_space.md` - has hardcoded date "Wednesday 21st January 2026, 16:00"
- Each event has its own ICS feed URL:
  - Ensemble: `https://addcal.co/ce/PsrhxxrWjJ/ics`
  - Learning Hour: `https://addcal.co/ce/YSnGoV3KR4/ics`
  - Open Space: `https://addcal.co/ce/t0S6bmoy2u/ics`

### Target State
- Individual event pages display next event date/time dynamically from ICS feeds
- Date/time updates automatically on each Jekyll build
- Format matches the style of each page

## Implementation Plan

### Step 1: Update next_ensemble.md

**File:** `society/events/next_ensemble.md`

Replace the TODO line (line 10) with dynamic date/time using jekyll-ical-tag:

```liquid
{% ical url: https://addcal.co/ce/PsrhxxrWjJ/ics only_future: true limit: 1 %}
**Next event: {{ event.start_time | date: "%A %-d %B %Y, %H:%M" }} {{ event.start_time | date: "%Z" }}**
{% endical %}
```

**Action:** Use `edit` tool to replace line 10.

### Step 2: Update next_learning_hour.md

**File:** `society/events/next_learning_hour.md`

Add dynamic date/time information after the title (around line 8-10):

```liquid
{% ical url: https://addcal.co/ce/YSnGoV3KR4/ics only_future: true limit: 1 %}
**Next event: {{ event.start_time | date: "%A %-d %B %Y, %H:%M" }} {{ event.start_time | date: "%Z" }}**
{% endical %}
```

**Action:** Use `edit` tool to add after line 8.

### Step 3: Update next_open_space.md

**File:** `society/events/next_open_space.md`

Replace the hardcoded date line (line 8) with dynamic date/time:

```liquid
{% ical url: https://addcal.co/ce/t0S6bmoy2u/ics only_future: true limit: 1 %}
**{{ event.start_time | date: "%A %-d %B %Y, %H:%M" }} {{ event.start_time | date: "%Z" }}**
{% endical %}
```

**Action:** Use `edit` tool to replace line 8.

### Step 4: Test the Implementation

Run Jekyll build to verify all pages render correctly:

```bash
bundle exec jekyll build
```

**Action:** Use `run_command` tool to build and check for errors.

### Step 5: Verify Output

Start Jekyll server and check each page:
- `/society/events/next_ensemble.html`
- `/society/events/next_learning_hour.html`
- `/society/events/next_open_space.html`

**Action:** Use `run_command` to start server and verify pages display correctly.

## Date Format Notes

Using format: `%A %-d %B %Y, %H:%M %Z`
- `%A` - Full weekday name (e.g., "Wednesday")
- `%-d` - Day without leading zero (e.g., "21")
- `%B` - Full month name (e.g., "January")
- `%Y` - Year (e.g., "2026")
- `%H:%M` - Time in 24-hour format (e.g., "16:00")
- `%Z` - Timezone abbreviation (e.g., "CET")

This matches the existing format on `next_open_space.md`: "Wednesday 21st January 2026, 16:00"

Note: Ruby's date formatting doesn't support ordinal suffixes (1st, 2nd, 3rd) natively, so we'll use "21" instead of "21st".

## Success Criteria

- [ ] `next_ensemble.md` displays dynamic date/time
- [ ] `next_learning_hour.md` displays dynamic date/time
- [ ] `next_open_space.md` displays dynamic date/time
- [ ] All pages build without errors
- [ ] Date/time format is readable and consistent
- [ ] Dates update automatically from ICS feeds
