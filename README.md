Teaching materials for Technical Agile Coaches
==============================================

This repo contains the sourcecode for [sammancoaching.org](sammancoaching.org) which is designed to provide resources for technical agile coaches to use in their work. For more information, please read this book [Technical Agile Coaching](https://leanpub.com/techagilecoach) by Emily Bache. This site is maintained by the members of the [Samman Technical Coaching Society](https://sammancoaching.org/society/index.html).

## Development

To test locally:

    bundle exec jekyll serve

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
You don't need to be a member of the Samman Technical Coaching Society to contribute to this website. We welcome pull requests with new materials for technical coaches. If you contribute, please include in the PR a contributor page for yourself. You'll need to add an entry in [_data/contributors.yml](_data/contributors.yml) and a new file under [society/contributors](society/contributors). Use your github handle as filename and key. If you don't have a github handle, choose another unique key.

If you send a PR you can expect to be contacted by a member of the society who will help you to get your contribution merged and published on the site.

## Deploying to the live site
When you push to the main branch, there is a github action that deploys the changes.

## Adding events
* In hubspot, bulk update the 'events' property for everyone who attended the previous event
* Wipe the 'next_open_space' property from all contacts in Hubspot
* Update AddEvent "add to calendar" link with the next date
* Rename the event page under society/events
* Update society/events/index.md with a link to the updated event signup page
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
