---
layout: society
title: Samman Coaching Society Ensemble Events
---

# Samman Ensemble Events

_Support the Society and Collaborate with Other Coaches._

{% assign ical_url = site.data.events.ensemble.ical_url %}
{% assign calendar_link = site.data.events.ensemble.calendar_link %}
{% ical url: ical_url only_future: true limit: 1 %}
**Next event: {{ event.start_time | date: "%A %-d %B %Y" }}**

<div class="event-links">
  <a href="{{ calendar_link }}" class="add-calendar-btn">Add to Calendar</a>
</div>
{% endical %}

This is a weekly, 1 hour ensemble, usually held on Fridays at 16:00 Stockholm/Paris/Berlin. We use this time to collaborate with our friends in the industry, where a diverse range of skills are brought to the room and we have fun writing code using ensemble techniques.  Hosted by [Emily Bache]({% link society/contributors/emilybache.md %}).

This event is open to [Members]({% link society/membership.md %}), [Supporters]({% link society/supporters.md %}) and [Contributors]({% link society/contributors/index.md %}). The joining details are published on our Discord.

If you would like to get involved in the work of the society, we recommend you join one of our [Open Space]({% link society/events/next_open_space.md %}) events
so you can introduce yourself and find out more.
