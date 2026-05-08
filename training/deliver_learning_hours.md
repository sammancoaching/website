---
layout: society
title: Deliver Learning Hours - Samman Coaching Training
---

# Deliver Learning Hours - Samman Coaching Training
_Lead learning hours with your team_

Would you like to lead some [learning hours]({% link reference/learning_hour_definition.md %}) with your team, but you need a little more help getting started? With only a little preparation, all kinds of developers and coaches can put on a valuable session for their team, using materials available online. In order to get the best out of the Samman Society learning hour materials it helps to understand the teaching techniques and design principles that lie behind them. This course is designed to set you up for success leading these sessions, and gives you a chance to learn from more experienced coaches.

## Course Topics:

* How Learning Hours are used as part of the Samman Technical Coaching method
* Sharon Bowman's [4C teaching model]({% link activities/4C_model.md %})
* Setting learning goals
* Facilitation skills for interactive learning activities

This course is designed to support senior developers working towards milestone 2 in the [Samman Learning Hour Career Track]({% link society/learning_hour_milestones.md %}). You will come away with the knowledge you need to lead learning hours with your colleagues, using materials that have been developed by others. If you’re an experienced trainer in other contexts already, then this course will also set you on the path to begin designing and leading learning hours from your own materials. There is a follow-up course [Learning Hours Masterclass]({% link training/learning_hours_masterclass.md %}) that will help you to take the next steps.

This online training is highly interactive and participatory, and is normally led by a pair of experienced coaches from the Samman Technical Coaching Society. 

## Course Dates

{% assign event_data = site.data.events.deliver_learning_hours %}
{% assign ical_url = event_data.ical_url %}
{% assign has_upcoming_dates = false %}
{% if ical_url %}
{% ical url: ical_url only_future: true limit: 1 %}
{% assign has_upcoming_dates = true %}
{% assign local_time = event.start_time | to_local_time %}
* {{ local_time | date: "%-d %B %Y" }}, {{ local_time | date: "%H:%M %Z" }} with [Emily Bache]({% link society/contributors/emilybache.md  %}) and [Peter Kofler]({% link society/contributors/codecop.md %}). More information and signup via [Bache Consulting](https://bacheconsulting.com/_events/next_deliver_learning_hours.html)
{% endical %}
{% endif %}
{% unless has_upcoming_dates %}
There are no training dates scheduled at present.
{% endunless %}

If you have questions or would like to show interest in this course, please [Contact us]({% link contact.md %}). You could also sign up for our [Newsletter]({% link newsletter.md %}) to hear about new training dates and other useful information.

