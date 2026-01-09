# Next Steps: Implement Dynamic Event Fetching from AddCal

## Context

We want to dynamically fetch event dates from AddCal ICS feeds instead of hardcoding them in the markdown file. This will allow events to be automatically updated whenever the site is rebuilt with Jekyll.

### Current State
- Events are manually defined in `society/events/upcoming_events.md` front matter
- Layout `_layouts/upcoming_events.html` renders events from page front matter
- AddCal provides ICS feed at: `https://addcal.co/ce/t0S6bmoy2u/apple`

### Target State
- Events fetched dynamically from AddCal ICS feed during Jekyll build
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

Replace the current event loop with the jekyll-ical-tag syntax. The current template uses:
```liquid
{% for event in page.events %}
```

Replace the entire events-list div (lines 7-30) with:

```liquid
<div class="events-list">
{% ical url: https://addcal.co/ce/t0S6bmoy2u/apple only_future: true %}
  <div class="event-card">
    <div class="event-date-block">
      <div class="weekday">{{ event.start_time | date: "%A" }}</div>
      <div class="day">{{ event.start_time | date: "%-d" }}</div>
      <div class="month-year">{{ event.start_time | date: "%B %Y" }}</div>
      <div class="time">{{ event.start_time | date: "%H:%M %Z" }}</div>
    </div>
    <div class="event-details">
      <h3>{{ event.summary }}</h3>
      <div class="event-meta">
        <span>{{ event.dtend | date: "%H:%M" | minus: event.dtstart | date: "%H:%M" }} minutes</span>
        <span>{{ event.location }}</span>
      </div>
      <p>{{ event.description }}</p>
      <div class="event-links">
        <a href="https://addcal.co/ce/t0S6bmoy2u" class="add-calendar-btn">Add to Calendar</a>
        {% if event.url %}
        <a href="{{ event.url }}" class="details-link">View Details</a>
        {% endif %}
      </div>
    </div>
  </div>
{% endical %}
</div>
```

**Note:** The ICS feed may not contain all the custom fields we currently have (like `audience`, `details_link`). You may need to adjust the template based on what data is actually in the AddCal ICS feed.

**Action for agent:** Use the `edit` tool to replace the events loop in `_layouts/upcoming_events.html`.

### Step 5: Update upcoming_events.md

**File:** `society/events/upcoming_events.md`

Remove the hardcoded events from the front matter, keeping only the layout and title:

```yaml
---
layout: upcoming_events
title: Upcoming Samman Coaching Society Events
---
```

**Action for agent:** Use the `edit` tool to remove the `events:` section and all event data from the front matter.

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

### AddCal ICS Feed Structure

The AddCal ICS feed will provide standard iCalendar fields:
- `summary` - Event title
- `description` - Event description
- `dtstart` - Start date/time
- `dtend` - End date/time
- `location` - Event location
- `url` - Event URL (if provided)

**Missing fields:** The current template uses custom fields like `audience`, `duration`, and `details_link` that won't be in the ICS feed. You'll need to either:
1. Remove these fields from the template, OR
2. Add them to the AddCal event descriptions in a structured format and parse them

### Multiple Event Types

If you have different types of events (Learning Hour, Open Space, Ensemble) with different AddCal feeds, you may need to:
1. Call the `{% ical %}` tag multiple times with different URLs
2. Add custom logic to categorize events based on their titles or descriptions

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
5. **Verify the ICS feed** - Before implementing, fetch the AddCal URL to see what data is actually available
6. **Adjust the template** - Based on actual ICS feed contents, you may need to modify the template structure
7. **Don't assume** - If a field isn't in the ICS feed, don't include it in the template

## Additional Resources

- jekyll-ical-tag GitHub: https://github.com/Rakefire/jekyll-ical-tag
- jekyll-ical-tag RubyGems: https://rubygems.org/gems/jekyll-ical-tag
- iCalendar RFC 5545: https://tools.ietf.org/html/rfc5545
- AddCal ICS Feed: https://addcal.co/ce/t0S6bmoy2u/apple

## Success Criteria

- [ ] jekyll-ical-tag gem installed and configured
- [ ] Layout template updated to use ICS feed
- [ ] Hardcoded events removed from markdown file
- [ ] Site builds successfully without errors
- [ ] Events page displays future events from AddCal
- [ ] Event dates, times, and descriptions render correctly
- [ ] Styling remains consistent with current design
