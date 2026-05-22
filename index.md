---
layout: homepage
title: Samman Technical Coaching
---

# Samman Technical Coaching

[Technical coaches]({% link reference/technical_coach_definition.md %}) work with software development teams to help them adopt better coding practices. The Samman method is a concrete approach that many technical coaches use. This website is designed to help people who do technical coaching and is maintained by the [Samman Technical Coaching Society]({% link society/index.md %}). This site shares materials you can use for [Code Katas]({% link kata_descriptions/index.md %}) and [Learning Hours]({% link learning_hours/index.md %}), as well as many supporting materials. We also have official [Training courses]({% link training/index.md %}).

## Upcoming events

<div class="events-list home-events-list">
{% assign event_entries = "" | split: "," %}
{% for event_item in site.upcoming_events %}
  {% if event_item.show_on_homepage %}
    {% assign event_data = site.data.events[event_item.event_key] %}
    {% assign ical_url = event_data.ical_url %}
    {% ical url: ical_url only_future: true limit: 1 %}
      {% assign start_timestamp = event.start_time | date: "%Y%m%d%H%M" %}
      {% capture event_html %}
      <div class="event-card event-card--mini">
        {% assign local_time = event.start_time | to_local_time %}
        <div class="event-date-block">
          <div class="weekday">{{ local_time | date: "%a" }}</div>
          <div class="day">{{ local_time | date: "%-d" }}</div>
          <div class="month-year">{{ local_time | date: "%b %Y" }}</div>
          <div class="time">{{ local_time | date: "%H:%M %Z" }}</div>
        </div>
        <div class="event-details">
          <h3>{{ event_item.title }}</h3>
          <div class="event-meta">
            <span>{{ event_item.duration }}</span>
          </div>
          <p>{{ event_item.description }}</p>
          <div class="event-links">
            <a href="{% link {{ event_item.details_link }} %}" class="details-link">View Details</a>
          </div>
        </div>
      </div>
      {% endcapture %}
      {% assign entry = start_timestamp | append: "|||" | append: event_html %}
      {% assign event_entries = event_entries | push: entry %}
    {% endical %}
  {% endif %}
{% endfor %}

{% assign sorted_entries = event_entries | sort %}
{% for entry in sorted_entries limit: 3 %}
  {% assign parts = entry | split: "|||" %}
  {{ parts[1] }}
{% endfor %}
</div>

<p><a href="{% link society/events/index.md %}">See all events</a></p>

## Sign up for our newsletter

If you like what you see here and want to get updates when we publish new materials as well as advice about technical coaching, please sign up for our [Newsletter]({% link newsletter.md %}).

## About the Samman method

Samman is a method for technical coaches who work with software teams. The focus is on iterative and incremental development practices. The Samman method has two main parts:

* [Learning Hour]({% link learning_hours/index.md %})
* [Ensemble Working]({% link reference/ensemble_definition.md %})

In the learning hour the coach uses exercises and active learning techniques to teach the theory and practice of skills like Test-Driven Development and Refactoring. In the Ensemble sessions the whole team collaborates together with the coach in applying these development techniques in their usual production codebase.

The expected outcome is that teams work more effectively and consistently with iterative and incremental development techniques even after the coach has moved on. This should help the organization to build new features in their software with a shorter lead time and higher quality.

You can find full details of the Samman method in the book ["Technical Agile Coaching with the Samman method"](https://leanpub.com/techagilecoach) by Emily Bache. "Samman Coaching" is an official trademark registered in the EU (#019000476) and owned by the Samman Technical Coaching Society.

## Where to go from here

We have a large collection of [Code Kata descriptions]({% link kata_descriptions/index.md %}) and [Learning Hour plans]({% link learning_hours/index.md %}) which you can do with your team. There are also some [reference materials]({% link reference/index.md %}) including a catalog of [Code Smells]({% link reference/code_smells/index.md %}) and [Refactorings]({% link reference/refactorings/index.md %}). If you'd like to design your own learning hours you can find templates for [teaching activities]({% link activities/index.md %}). If you are getting started with Samman coaching, you can also find recommended [Training courses]({% link training/index.md %}).

If you would like to find out more about the community of coaches and how to use the Samman method, please sign up for our [Newsletter]({% link newsletter.md %}), and/or come to one of our [events]({% link society/events/index.md %}). If you would like to hire a technical coach, see our list of [members and contributors]({% link society/contributors/index.md %}).
