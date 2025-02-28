Teaching materials for Technical Agile Coaches
==============================================

This repo contains the sourcecode for [sammancoaching.org](sammancoaching.org) which is designed to provide resources for technical agile coaches to use in their work. For more information, please read this book [Technical Agile Coaching](https://leanpub.com/techagilecoach) by Emily Bache. This site is maintained by the members of the [Samman Technical Coaching Society](https://sammancoaching.org/society/index.html).

## Development
You can either run jekyll natively on your platform, or use docker.

### Native Jekyll
First install Ruby, which includes the utility 'bundler'. Use Bundler in the same folder as this README to get all the dependencies:

    bundle install

Note this will use the Gemfile and will create a Gemfile.lock itemizing all the versions of your gems. I found a problem installing wdm that was fixed by using this workaround 'gem install wdm -- --with-cflags=-Wno-implicit-function-declaration'

Then launch the jekyll application locally, again using bundler:

    bundle exec jekyll serve

Launch your local site: [http://127.0.0.1:4000/](http://127.0.0.1:4000/)

### Using Docker
Instead of using jekyll locally you can get a prebuilt docker image with Ruby, Jekyll etc. installed:

    dockerinit

Test locally run the server with:

    dockerrun

Alternatively use [docker-compose](https://docs.docker.com/compose/) using the docker-compose.yml. 
    
    docker-compose up

Then browse to:

    http://localhost:4000

If you want to get access to the terminal in the docker container the command is:

    docker exec -it <name_of_container> /bin/bash

were "name_of_container"  is found by running the command 

    docker ls

or expanding the container in the Docker desktop user interface.

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
* Rename the event page under society/events
* Update society/events/index.md with a link to the updated event signup page and the top level index page
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

1. Improve the build so we don't release a broken site
2. Use Jekyll links everywhere - no "]{/" in project
   2.1. Use this regexp to find html links: \((\/.*?)(\.html)\)
    2.2. the jekyll syntax for a link is: {% link foldername/documentname.md %}
3. Create a new list of learning hours listing "by Tag". Add tags to learning hours.
4. Use defined perma links instead of folder structure
4. Move index pages to their own folder instead of having them in a folder structure
4. Make contributors into a collection
5. Remove layouts that are only used in one place, use html in these pages instead
6. Give learning hours ids (with a script?) and put them in a flat folder structure
7. Supply page templates for collections in git but not included in the jekyll build

## Jekyll Design Principles
* Use collections for objects
* Use liquid as a database
* `_data` is good for things that don't have their own pages
* Routing is best based on configuration not file structure
* If it needs its own layout, write it in html from the start
* Using frontmatter when possible enables jekyll to check that things work

## Site Improvements
* Add a page about Kent Beck's tidyings from Tidy First? to the refactoring section of the site.