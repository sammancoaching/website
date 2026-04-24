---
layout: society
title: Samman Coaching Society AI Coding Dojo
---

# AI Coding Dojo

_Practice AI coding skills in a group._

{% assign ical_url = site.data.events.ai_coding_dojo.ical_url %}
{% assign calendar_link = site.data.events.ai_coding_dojo.calendar_link %}
{% ical url: ical_url only_future: true limit: 1 %}
**Next event: {{ event.start_time | date: "%A %-d %B %Y" }}**

<div class="event-links">
  <a href="{{ calendar_link }}" class="add-calendar-btn">Add to Calendar</a>
</div>
{% endical %}

This is an occasional event, usually held on a Thursday at 14:00 Stockholm/Paris/Berlin. We get together and write some code using AI tools, in an evolving format that includes Ensemble working and frequent retrospectives.

This event is open to [Members]({% link society/membership.md %}), [Supporters]({% link society/supporters.md %}) and [Contributors]({% link society/contributors/index.md %}). The joining details are published on our Discord.

If you would like to get involved in the work of the society, we recommend you join one of our [Open Space]({% link society/events/next_open_space.md %}) events so you can introduce yourself and find out more.
