---
layout: default
title: Upcoming Samman Coaching Society Events
---

<h1>{{ page.title }}</h1>

<div class="event-list">
{% assign event_entries = "" | split: "," %}
{% for event_item in site.upcoming_events %}
  {% if event_item.has_upcoming_date %}
    {% assign start_time = event_item.next_start_utc %}
    {% capture calendar_link %}{% link {{ event_item.details_link }} %}#add-to-calendar{% endcapture %}
    {% include events_list_card.html %}
  {% endif %}
{% endfor %}

{% assign sorted_entries = event_entries | sort %}
{% for entry in sorted_entries %}
{% assign parts = entry | split: "|||" %}
{{ parts[1] }}
{% endfor %}
</div>
