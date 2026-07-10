---
layout: default
title: Offers
---

<h1>Hire a Technical Coach</h1>
<div class="card-grid-description">
    <p>
        Technical skills have to be acquired deliberately, and
        the best effect comes from working with a good coach who combines theory and practice in your real code.
        Some members of the Samman Technical Coaching Society are available for hire, and offer these kinds of engagements.
    </p>
</div>
<div class="card-grid offer-card-grid">
    {% for offer_entry in site.data.coaching_offers %}
    {% assign offer = offer_entry[1] %}
    {% assign coach_count = 0 %}
    {% for contributor_entry in site.data.contributors %}
    {% assign contributor = contributor_entry[1] %}
    {% if contributor.member and contributor.offers contains offer_entry[0] %}
    {% assign coach_count = coach_count | plus: 1 %}
    {% endif %}
    {% endfor %}

    <div class="card offer-card">
        <h2>{{ offer.title | upcase }}</h2>
        <p>{{ offer.description }}</p>
        <p class="offer-coach-count">{{ coach_count }} {% if coach_count == 1 %}coach offers{% else %}coaches offer{% endif %} this</p>
        <div>
            <a class="button" href="{{ site.baseurl }}/society/offers/{{ offer.slug }}.html">See the coaches</a>
        </div>
    </div>
    {% endfor %}
</div>

<div class="card-grid-description">
    <p class="offer-contact-note">
        Not sure which fits? Get in touch via our <a href="{% link contact.md %}">contact page</a>.
    </p>
</div>
