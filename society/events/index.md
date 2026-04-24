---
layout: default
title: Upcoming Samman Coaching Society Events
---

<h1>{{ page.title }}</h1>

<div class="events-list">
{% assign event_entries = "" | split: "," %}
{% for event_item in site.upcoming_events %}
  {% assign event_data = site.data.events[event_item.event_key] %}
  {% assign ical_url = event_data.ical_url %}
  {% ical url: ical_url only_future: true limit: 1 %}
    {% assign start_timestamp = event.start_time | date: "%Y%m%d%H%M" %}
    {% capture event_html %}
    <div class="event-card">
      {% assign local_time = event.start_time | to_local_time %}
      <div class="event-date-block">
        <div class="weekday">{{ local_time | date: "%A" }}</div>
        <div class="day">{{ local_time | date: "%-d" }}</div>
        <div class="month-year">{{ local_time | date: "%B %Y" }}</div>
        <div class="time">{{ local_time | date: "%H:%M %Z" }} </div>
      </div>
      <div class="event-details">
        <h3>{{ event_item.title }}</h3>
        <div class="event-meta">
          <span>{{ event_item.duration }}</span>
          <span>{{ event_item.audience }}</span>
        </div>
        <p>{{ event_item.description }}</p>
        <div class="event-links">
          <a href="{{ event_data.calendar_link }}" class="add-calendar-btn">Add to Calendar</a>
          <a href="{% link {{ event_item.details_link }} %}" class="details-link">View Details</a>
        </div>
      </div>
    </div>
    {% endcapture %}
    {% assign entry = start_timestamp | append: "|||" | append: event_html %}
    {% assign event_entries = event_entries | push: entry %}
  {% endical %}
{% endfor %}

{% assign sorted_entries = event_entries | sort %}
{% for entry in sorted_entries %}
{% assign parts = entry | split: "|||" %}
{{ parts[1] }}
{% endfor %}
</div>
