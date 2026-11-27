---
layout: society
title: Samman Coaching Society Learning Hour Events
---

# Samman Learning Hour Events

_Preview new learning hours designed by society members and supporters._

{% assign learning_hour = site.upcoming_events | where: "event_key", "learning_hour" | first %}
{% if learning_hour.has_upcoming_date %}
**Next event: {{ learning_hour.next_start | date: "%A %-d %B %Y" }}**
{% if learning_hour.upcoming_dates.size > 1 %}

Following events: {% for d in learning_hour.upcoming_dates offset: 1 %}{{ d.start | date: "%A %-d %B %Y" }}{% unless forloop.last %}; {% endunless %}{% endfor %}
{% endif %}
{% endif %}

This is a monthly, 90-minute meeting usually held on a Wednesday starting at 17:00 Stockholm/Paris/Berlin. We use this time to try out a new learning hour before it is published on the website. The presenter gets qualified feedback from other coaches.  Hosted by [Emily Bache]({% link society/contributors/emilybache.md %}).

These events are open to [Members]({% link society/membership.md %}), [Supporters]({% link society/supporters.md %}) and [Contributors]({% link society/contributors/index.md %}). The joining details are published on our Discord.

{% include add_to_calendar.html event=learning_hour %}

If you would like to get involved in the work of the society, we recommend you join one of our [Open Space]({% link society/events/next_open_space.md %}) events
so you can introduce yourself and find out more.
