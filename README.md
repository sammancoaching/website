[![build_and_test](https://github.com/sammancoaching/website/actions/workflows/build_and_test.yml/badge.svg)](https://github.com/sammancoaching/website/actions/workflows/build_and_test.yml)

Teaching materials for Technical Agile Coaches
==============================================

This repo contains the sourcecode for [sammancoaching.org](sammancoaching.org) which is designed to provide resources for technical agile coaches to use in their work. For more information, please read this book [Technical Agile Coaching](https://leanpub.com/techagilecoach) by Emily Bache. This site is maintained by the members of the [Samman Technical Coaching Society](https://sammancoaching.org/society/index.html).

## Development
1. Install Python
1. Follow the instructions at https://jekyllrb.com/docs/installation/.
1. Run `bundle install`.
1. Run the `build_and_test` script.

## Contributing to the site
You don't need to be a member of the Samman Technical Coaching Society to contribute to this website. We welcome pull requests with new materials for technical coaches. If you contribute, please include in the PR a contributor page for yourself. You'll need to add an entry in [_data/contributors.yml](_data/contributors.yml) and a new file under [society/contributors](society/contributors). Use your github handle as filename and key. 

As you prepare your contribution, you might use resources which are already on this site. For example [Code Katas](https://sammancoaching.org/kata_descriptions/index.html), [Activities](https://sammancoaching.org/activities/index.html) or [Reference Materials](https://sammancoaching.org/reference/index.html). If you use any please link to them.

If you send a PR you can expect to be contacted by a member of the society who will help you to get your contribution merged and published on the site.

## Deploying to the live site
When you push to the main branch, there is a github action that deploys the changes.

## Adding events
* In hubspot, bulk update the 'events' property for everyone who attended the previous event
* Wipe the 'next_open_space' property from all contacts in Hubspot
* Update calendr.link "add to calendar" link with the next date
* Update next_open_space.md with the next date
* Test that you can sign up:
  * correct signup thankyou page
  * 'add to calendar' link on that page works, 
  * you get a confirmation email
  * you get the 'next_open_space' property in hubspot
* Create zoom meeting
* Create calendar event and invite co-host & society members
* Create and schedule email 1 week before with zoom link
* Create and schedule email on the day with zoom link
* Advertize on discord etc

## Adding new members
* Make sure they have read and understood [Membership](https://sammancoaching.org/society/membership.html)
* Invite them to github organization
* Update their settings in [contributors](_data/contributors.yml)
* Update their profile page on this site 
* Add them to the membership registry google doc
* Add them to the next open space calendar invite
* Update their groups on Discord
* Send welcome mail saying you've done those things
* Announce them on Discord & elsewhere

# Development plan for this website
We would like to do some refactoring. This is the plan

1. Add search feature
2. Bug: "Training" opens in new window. Desired behaviour - only external links open in new window. Possibly use [this plugin](https://github.com/keithmifsud/jekyll-target-blank). Problem is caused by code in header.html
2. Add a field to katas for "difficulty" and allow people to sort them. Possibly tags too?
3. Show a calendar of all upcoming events. Do not show joining info, link to information page for the event. Not sure how to achieve this - base it on the google calendar? 
4. Use defined [perma links](https://jekyllrb.com/docs/permalinks/) instead of folder structure.
5. Move index pages to their own folder instead of having them in a folder structure.
6. Make contributors into a collection.
7. Remove layouts that are only used in one place, use html in these pages instead
8. Give learning hours ids (with a script?) and put them in a flat folder structure
9. Supply page templates for collections in git but not included in the jekyll build

## Jekyll Design Principles
* Use collections for objects
* Use liquid as a database
* `_data` is good for things that don't have their own pages
* Routing is best based on configuration not file structure
* If it needs its own layout, write it in html from the start
* Using frontmatter when possible enables jekyll to check that things work

## Site Improvements
* Add a page about Kent Beck's tidyings from Tidy First? to the refactoring section of the site.
