Teaching materials for Technical Agile Coaches
==============================================

This repo contains resources for technical agile coaches to use in their work. For more information, please read this book [Technical Agile Coaching](https://leanpub.com/techagilecoach) by Emily Bache.

To test locally:

    bundle exec jekyll serve


Instead of using jekyll locally you can get a prebuilt docker image with Ruby, Jekyll etc. installed:

    dockerinit

Test locally run the server with:

    dockerrun

Then browse to:

    http://localhost:4000

## Deploying to the live site
When you push to the main branch, there is a github action that deploys the changes.

## Adding events
* Add a new event page under society/events
* In hubspot, bulk update the 'events' property for everyone who attended the previous event
* Wipe the 'next_open_space' property from all contacts in Hubspot
* Create a signup form in hubspot that sets 'next_open_space'. Add a confirmation email to it.
* Update the layouts/event.html layout with the hubspot signup form
* Update the open_space_signup_thankyou.md layout with an AddEvent "add to calendar" link
* Update the hubspot form with a landing page pointing at the 'signup thankyou' page
* Test that you can sign up:
  * correct signup thankyou page
  * 'add to calendar' link on that page works, 
  * you get a confirmation email
  * you get the 'next_open_space' property in hubspot
* Update society/events/index.md with a link to the event signup page