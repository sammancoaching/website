---
layout: society
title: Samman Coaching Society AI Coding Dojo
---

# AI Coding Dojo

_Practice AI coding skills in a group._

{% assign ai_coding_dojo = site.upcoming_events | where: "event_key", "ai_coding_dojo" | first %}
{% if ai_coding_dojo.has_upcoming_date %}
**Next event: {{ ai_coding_dojo.next_start | date: "%A %-d %B %Y" }}**
{% endif %}

This is an occasional event, usually held in an afternoon during European working hours. We get together and write some code using AI tools, in an evolving format that includes Ensemble working and frequent retrospectives.

This event is open to [Members]({% link society/membership.md %}), [Supporters]({% link society/supporters.md %}) and [Contributors]({% link society/contributors/index.md %}). The joining details are published on our Discord.

{% include add_to_calendar.html event=ai_coding_dojo %}

If you would like to get involved in the work of the society, we recommend you join one of our [Open Space]({% link society/events/next_open_space.md %}) events so you can introduce yourself and find out more.
