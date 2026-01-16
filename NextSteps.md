# Next Steps: Implement Dynamic Event Fetching from AddCal

## Context

We want to dynamically fetch event dates from AddCal ICS feeds instead of hardcoding them in the markdown file. This will allow events to be automatically updated whenever the site is rebuilt with Jekyll.

### Current State
- Events are manually defined in `society/events/upcoming_events.md` front matter with hardcoded dates
- Each event now has a `next_event` property pointing to its specific ICS feed:
  - Learning Hour: `https://addcal.co/ce/YSnGoV3KR4/ics`
  - Open Space: `https://addcal.co/ce/t0S6bmoy2u/ics`
  - Ensemble: `https://addcal.co/ce/PsrhxxrWjJ/ics`
- Layout `_layouts/upcoming_events.html` renders events from page front matter
- Static metadata (title, description, audience, details_link) remains in front matter

### Target State
- Event dates/times fetched dynamically from individual ICS feeds during Jekyll build
- Static metadata (title, description, audience, details_link) kept in front matter
- No manual date updates needed in markdown files
- Automatic filtering to show only future events

## Chosen Solution: jekyll-ical-tag Plugin

We selected the **jekyll-ical-tag** gem (https://github.com/Rakefire/jekyll-ical-tag) because:
- It's a mature, open-source Jekyll plugin
- Supports remote ICS URLs directly
- Has built-in filtering for future events
- Works as a Liquid tag (simple integration)
- Handles recurring events automatically

## Implementation Plan

### Step 1: Add jekyll-ical-tag Gem

**File:** `Gemfile`

Add the following line to the Gemfile (within the `jekyll_plugins` group if it exists, otherwise add it with other gems):

```ruby
gem 'jekyll-ical-tag'
```

**Action for agent:** Use the `edit` tool to add `gem 'jekyll-ical-tag'` to the Gemfile.

### Step 2: Configure Plugin in Jekyll

**File:** `_config.yml`

Add `jekyll-ical-tag` to the plugins list. The plugins section currently exists at lines 93-96. Add it to that list:

```yaml
plugins:
  - jekyll-feed
  - jekyll-sitemap
  - jekyll-seo-tag
  - jekyll-ical-tag
```

**Action for agent:** Use the `edit` tool to add `- jekyll-ical-tag` to the plugins list in `_config.yml`.

### Step 3: Install the Gem

Run bundle install to install the new gem:

```bash
bundle install
```

**Action for agent:** Use the `run_command` tool with `CommandLine: "bundle install"` and `Cwd: "c:\Users\ImageBuilderAdmin\Documents\GitHub\website"`. Mark as `SafeToAutoRun: false` since it installs dependencies.

### Step 4: Update the Layout Template

**File:** `_layouts/upcoming_events.html`

Update the template to fetch dates dynamically from each event's `next_event` ICS feed while preserving the static metadata from the front matter.

The current template uses:
```liquid
{% for event in page.events %}
```

Replace the entire events-list div (lines 7-30) with a hybrid approach:

```liquid
<div class="events-list">
{% for event_meta in page.events %}
  {% ical url: {{ event_meta.next_event }} only_future: true limit: 1 %}
  <div class="event-card">
    <div class="event-date-block">
      <div class="weekday">{{ event.start_time | date: "%A" }}</div>
      <div class="day">{{ event.start_time | date: "%-d" }}</div>
      <div class="month-year">{{ event.start_time | date: "%B %Y" }}</div>
      <div class="time">{{ event.start_time | date: "%H:%M" }}</div>
    </div>
    <div class="event-details">
      <h3>{{ event_meta.title }}</h3>
      <div class="event-meta">
        <span>{{ event_meta.duration }}</span>
        <span>{{ event_meta.audience }}</span>
      </div>
      <p>{{ event_meta.description }}</p>
      <div class="event-links">
        <a href="{{ event_meta.next_event | replace: '/ics', '' }}" class="add-calendar-btn">Add to Calendar</a>
        {% if event_meta.details_link %}
        <a href="{{ event_meta.details_link | relative_url }}" class="details-link">View Details</a>
        {% endif %}
      </div>
    </div>
  </div>
  {% endical %}
{% endfor %}
</div>
```

**Key changes:**
- Loop through `page.events` to get static metadata (title, description, audience, details_link)
- For each event, use `{% ical %}` tag with the `next_event` URL to fetch dynamic date/time
- Use `limit: 1` to get only the next occurrence
- Combine ICS date data with front matter metadata
- Preserve existing styling and structure

**Action for agent:** Use the `edit` tool to replace the events loop in `_layouts/upcoming_events.html`.

### Step 5: Update upcoming_events.md

**File:** `society/events/upcoming_events.md`

Remove the hardcoded date/time fields (weekday, day, month_year, time) from each event, keeping only:
- Static metadata: title, duration, audience, description, details_link
- Dynamic data reference: next_event (ICS URL)

The front matter should look like:

```yaml
---
layout: upcoming_events
title: Upcoming Samman Coaching Society Events
events:
  - title: Samman Coaching Society Learning Hour
    duration: 90 minutes
    audience: Society Members
    description: Preview new learning hours designed by society members and supporters. Get qualified feedback from other coaches before publishing on the website.
    details_link: society/events/next_learning_hour.md
    next_event: https://addcal.co/ce/YSnGoV3KR4/ics
  
  - title: Online Open Space Event
    duration: 60 minutes
    audience: Open to All
    description: Bring your questions and exchange experiences with other technical coaches. Free to attend. We'll collaboratively create an agenda and hold discussions in breakout rooms.
    details_link: society/events/next_open_space.md
    next_event: https://addcal.co/ce/t0S6bmoy2u/ics
  
  - title: Samman Coaching Society Ensemble
    duration: 60 minutes
    audience: Society Members
    description: Weekly ensemble session to collaborate with other coaches. Bring diverse skills to the room and have fun writing code together using ensemble techniques.
    details_link: society/events/next_ensemble.md
    next_event: https://addcal.co/ce/PsrhxxrWjJ/ics
---
```

**Action for agent:** Use the `edit` tool to remove the hardcoded date fields (weekday, day, month_year, time) from each event.

### Step 6: Test the Implementation

Run the Jekyll build locally to verify:

```bash
./build_and_test
```

**Action for agent:** Use the `run_command` tool to run the build script and verify no errors occur.

### Step 7: Verify the Output

Check that:
1. The site builds without errors
2. Events are displayed on the upcoming events page
3. Only future events are shown
4. Event data (dates, times, titles, descriptions) renders correctly

**Action for agent:** After the build succeeds, use the `browser_preview` tool to view the site and verify the events page displays correctly.

## Important Considerations for Implementation

### Hybrid Data Model

This implementation uses a **hybrid approach**:
- **Static metadata** (title, description, audience, duration, details_link) stays in `upcoming_events.md` front matter
- **Dynamic date/time data** fetched from individual ICS feeds via `next_event` property
- Each event type has its own AddCal ICS feed

**Benefits:**
- Custom fields (audience, duration, details_link) remain available
- Only dates/times need updating in AddCal
- Event descriptions and metadata controlled in the repository
- Each event series (Learning Hour, Open Space, Ensemble) managed independently

### AddCal ICS Feed Structure

Each AddCal ICS feed will provide standard iCalendar fields:
- `dtstart` - Start date/time (used for display)
- `dtend` - End date/time
- `summary` - Event title (from AddCal, but we use front matter title instead)
- `description` - Event description (from AddCal, but we use front matter description instead)
- `location` - Event location (if configured in AddCal)

### Multiple Event Types

Each event type has its own ICS feed:
- **Learning Hour:** `https://addcal.co/ce/YSnGoV3KR4/ics`
- **Open Space:** `https://addcal.co/ce/t0S6bmoy2u/ics`
- **Ensemble:** `https://addcal.co/ce/PsrhxxrWjJ/ics`

The template loops through `page.events` and fetches the next occurrence from each feed individually.

### Time Zone Handling

The ICS feed will include time zone information. The `event.start_time` will be a Ruby DateTime object that respects the time zone from the feed.

### Caching Considerations

The plugin fetches the ICS feed on every build. If builds are slow:
1. Consider using Jekyll's built-in caching
2. Or implement a pre-build script to download and cache the ICS file locally

## Troubleshooting

### If the plugin doesn't load:
- Verify the gem is in the Gemfile
- Run `bundle install`
- Restart the Jekyll server
- Check `_config.yml` has the plugin listed

### If events don't display:
- Verify the ICS URL is accessible: `https://addcal.co/ce/t0S6bmoy2u/apple`
- Check Jekyll build output for errors
- Add `only_future: false` temporarily to see all events (including past ones)
- Inspect the ICS feed directly to see what data is available

### If formatting is wrong:
- Check the date format strings in the Liquid filters
- Verify the event fields match what's in the ICS feed
- Use `{{ event | inspect }}` to see all available fields

## Agent Instructions

When implementing this plan:

1. **Read files before editing** - Always use `read_file` before making changes
2. **Make targeted edits** - Use the `edit` tool with exact string matching
3. **Test incrementally** - Run the build after each major change
4. **Check for errors** - Read build output carefully
5. **Understand the hybrid model** - Static metadata stays in front matter, only dates come from ICS feeds
6. **Preserve existing data** - Don't remove the static fields (title, description, audience, duration, details_link)
7. **Remove only date fields** - Only remove weekday, day, month_year, and time from the front matter
8. **Test with multiple feeds** - Each event has its own ICS feed URL in the `next_event` property

## Additional Resources

- jekyll-ical-tag GitHub: https://github.com/Rakefire/jekyll-ical-tag
- jekyll-ical-tag RubyGems: https://rubygems.org/gems/jekyll-ical-tag
- iCalendar RFC 5545: https://tools.ietf.org/html/rfc5545
- AddCal ICS Feeds:
  - Learning Hour: https://addcal.co/ce/YSnGoV3KR4/ics
  - Open Space: https://addcal.co/ce/t0S6bmoy2u/ics
  - Ensemble: https://addcal.co/ce/PsrhxxrWjJ/ics

## Success Criteria

- [ ] jekyll-ical-tag gem installed and configured
- [ ] Layout template updated to use hybrid approach (ICS dates + front matter metadata)
- [ ] Hardcoded date fields removed from markdown file (weekday, day, month_year, time)
- [ ] Static metadata preserved in markdown file (title, description, audience, duration, details_link, next_event)
- [ ] Site builds successfully without errors
- [ ] Events page displays future events with dates from individual AddCal ICS feeds
- [ ] Event dates, times, titles, and descriptions render correctly
- [ ] Custom fields (audience, duration, details links) display correctly
- [ ] Styling remains consistent with current design
