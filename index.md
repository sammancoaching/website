---
layout: homepage
title: Samman Technical Coaching
---

# Samman Technical Coaching

[Technical coaches]({% link reference/technical_coach_definition.md %}) work with software development teams to help them adopt better coding practices. The Samman method is a concrete approach that many technical coaches use. This website is designed to help people who do technical coaching and is maintained by the [Samman Technical Coaching Society]({% link society/index.md %}). This site shares materials you can use for [Code Katas]({% link kata_descriptions/index.md %}) and [Learning Hours]({% link learning_hours/index.md %}), as well as many supporting materials. We also have official [Training courses]({% link training/index.md %}).

## News
Read the Samman Society [official position on Agentic AI]({% link society/agentic_ai.md %})

## Upcoming events

<section class="split">
  <div>
    <div class="event-list">
    {% assign event_entries = "" | split: "," %}
    {% for event_item in site.upcoming_events %}
      {% if event_item.show_on_homepage %}
        {% assign event_data = site.data.events[event_item.event_key] %}
        {% if event_item.start %}
          {% if event_item.has_upcoming_date %}
            {% assign start_time = event_item.next_start_utc %}
            {% assign calendar_link = event_item.url | relative_url %}
            {% include homepage_event_card.html %}
          {% endif %}
        {% else %}
          {% assign ical_url = event_data.ical_url %}
          {% ical url: ical_url only_future: true limit: 1 %}
            {% assign start_time = event.start_time %}
            {% assign calendar_link = event_data.calendar_link %}
            {% include homepage_event_card.html %}
          {% endical %}
        {% endif %}
      {% endif %}
    {% endfor %}

    {% assign sorted_entries = event_entries | sort %}
    {% for entry in sorted_entries limit: 3 %}
      {% assign parts = entry | split: "|||" %}
      {{ parts[1] }}
    {% endfor %}
    </div>

    <p><a href="{% link society/events/index.md %}">See all events</a></p>
  </div>

  <aside class="panel panel--interactive panel--sticky">
    <h3>Stay connected</h3>
    <p>Community updates and coaching resources in one monthly email.</p>
    <p><strong>Includes free TDD Heuristics guide.</strong></p>
    <a class="btn" href="{% link newsletter.md %}">Newsletter</a>
    <p>Unsubscribe anytime.</p>
  </aside>
</section>

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
