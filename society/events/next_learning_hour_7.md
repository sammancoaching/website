---
layout: society
title: Upcoming Samman Coaching Society Events
---

# Upcoming Events

<style>
.events-list {
  max-width: 1000px;
  margin: 2rem auto;
}

.event-card {
  display: grid;
  grid-template-columns: 180px 1fr;
  gap: 2rem;
  margin-bottom: 2.5rem;
  padding: 1.5rem;
  border: 2px solid #e8e8e8;
  border-radius: 10px;
  transition: all 0.3s ease;
}

.event-card:hover {
  border-color: $dark-blue;
  box-shadow: 0 4px 12px rgba(23,64,100, 0.15);
}

.event-date-block {
  background: $light-blue;
  color: $dark-blue;
  padding: 1.5rem;
  border-radius: 8px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.event-date-block .weekday {
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  opacity: 0.9;
  margin-bottom: 0.5rem;
}

.event-date-block .day {
  font-size: 3rem;
  font-weight: bold;
  line-height: 1;
  margin-bottom: 0.25rem;
}

.event-date-block .month-year {
  font-size: 1rem;
  opacity: 0.95;
}

.event-date-block .time {
  font-size: 0.85rem;
  margin-top: 0.75rem;
  padding-top: 0.75rem;
  border-top: 1px solid rgba(255,255,255,0.3);
}

.event-details {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.event-details h3 {
  margin-top: 0;
  margin-bottom: 0.75rem;
  color: $dark-blue;
  font-size: 1.5rem;
}

.event-meta {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1rem;
  color: #666;
  font-size: 0.9rem;
}

.event-meta span {
  display: flex;
  align-items: center;
  gap: 0.3rem;
}

.event-details p {
  color: #555;
  line-height: 1.7;
  margin-bottom: 1.25rem;
}

.event-links {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.event-links a {
  display: inline-block;
  padding: 0.6rem 1.25rem;
  text-decoration: none;
  border-radius: 6px;
  font-weight: 500;
  font-size: 0.9rem;
  transition: all 0.2s;
}

.add-calendar-btn {
  background: $dark-blue;
  color: white;
}

.add-calendar-btn:hover {
  background: $mid-blue;
  transform: translateY(-2px);
}

.details-link {
  background: white;
  color: $light-blue;
  border: 2px solid $light-blue;
}

.details-link:hover {
  background: $light-blue;
  color: $dark-blue;
}

/* Mobile responsive */
@media (max-width: 768px) {
  .event-card {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    padding: 1.25rem;
  }
  
  .event-date-block {
    padding: 1rem;
  }
  
  .event-date-block .day {
    font-size: 2.5rem;
  }
  
  .event-details h3 {
    font-size: 1.25rem;
  }
}
</style>

<div class="events-list">

  <div class="event-card">
    <div class="event-date-block">
      <div class="weekday">Monday</div>
      <div class="day">15</div>
      <div class="month-year">December 2025</div>
      <div class="time">16:00 CET</div>
    </div>
    <div class="event-details">
      <h3>Samman Coaching Society Learning Hour</h3>
      <div class="event-meta">
        <span>90 minutes</span>
        <span>Society Members</span>
      </div>
      <p>Preview new learning hours designed by society members and supporters. Get qualified feedback from other coaches before publishing on the website.</p>
      <div class="event-links">
        <!-- AddCal snippet goes here -->
        <a href="#" class="add-calendar-btn">Add to Calendar</a>
        <a href="{% link society/events/next_learning_hour.md %}" class="details-link">View Details</a>
      </div>
    </div>
  </div>

  <div class="event-card">
    <div class="event-date-block">
      <div class="weekday">Thursday</div>
      <div class="day">18</div>
      <div class="month-year">December 2025</div>
      <div class="time">16:00 CET</div>
    </div>
    <div class="event-details">
      <h3>Online Open Space Event</h3>
      <div class="event-meta">
        <span>60 minutes</span>
        <span>Open to All</span>
      </div>
      <p>Bring your questions and exchange experiences with other technical coaches. Free to attend. We'll collaboratively create an agenda and hold discussions in breakout rooms.</p>
      <div class="event-links">
        <!-- AddCal snippet goes here -->
        <a href="#" class="add-calendar-btn">Add to Calendar</a>
        <a href="{% link society/events/next_open_space.md %}" class="details-link">View Details</a>
      </div>
    </div>
  </div>

  <div class="event-card">
    <div class="event-date-block">
      <div class="weekday">Friday</div>
      <div class="day">20</div>
      <div class="month-year">December 2025</div>
      <div class="time">14:00 CET</div>
    </div>
    <div class="event-details">
      <h3>Samman Coaching Society Ensemble</h3>
      <div class="event-meta">
        <span>60 minutes</span>
        <span>Society Members</span>
      </div>
      <p>Weekly ensemble session to collaborate with other coaches. Bring diverse skills to the room and have fun writing code together using ensemble techniques.</p>
      <div class="event-links">
        <!-- AddCal snippet goes here -->
        <a href="#" class="add-calendar-btn">Add to Calendar</a>
        <a href="{% link society/events/next_ensemble.md %}" class="details-link">View Details</a>
      </div>
    </div>
  </div>

</div>
