---
layout: default
title: Upcoming Samman Coaching Society Events
---

<h1>{{ page.title }}</h1>

<div class="event-list">
{% assign event_entries = "" | split: "," %}
{% for event_item in site.upcoming_events %}
  {% assign event_data = site.data.events[event_item.event_key] %}
  {% if event_item.start %}
    {% if event_item.has_upcoming_date %}
      {% assign start_time = event_item.next_start_utc %}
      {% assign calendar_link = event_item.url | relative_url %}
      {% include events_list_card.html %}
    {% endif %}
  {% else %}
    {% assign ical_url = event_data.ical_url %}
    {% ical url: ical_url only_future: true limit: 1 %}
      {% assign start_time = event.start_time %}
      {% assign calendar_link = event_data.calendar_link %}
      {% include events_list_card.html %}
    {% endical %}
  {% endif %}
{% endfor %}

{% assign sorted_entries = event_entries | sort %}
{% for entry in sorted_entries %}
{% assign parts = entry | split: "|||" %}
{{ parts[1] }}
{% endfor %}
</div>
