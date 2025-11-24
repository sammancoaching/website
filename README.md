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

# Development plan for this website
We would like to do some refactoring. This is the plan

1. Update style to new branding guidelines
    - [x] review the colors for the text should be dark blue
    - [x] hovers should coral
    - [] links need to be discussed, light blue
    - [x] background color whould be off white
    - [x] remove references to old colours
    - [] style the current nav item in light blue or coral
    - [] need to install new fonts
    - [] use new branding fonts
    - [] move the search box somewhere better
    - [] make the nav bar part of the header somehow
    - [] make header look nice on mobile
    - [] retain navigation 'current' css style when viewing pages underneath that tab (https://stackoverflow.com/questions/8340170/jekyll-automatically-highlight-current-tab-in-menu-bar)

2. Add search feature
    - [x] bring back nice XML-based test reports in GitHub workflow
    - [x] search results include unwanted pages (e.g. 404)
    - [x] ensure the teardown kills the server
    - [x] add more pages to the search index
    - [x] remove signup thankyou pages from search index
    - [x] fix title mismatch (check_title_mismatch.py)
    - [x] toggle search on in production
    - [ ] investigate why you can't click on search results if the timeout is too small
1. use title case for page titles
1. rename about_society.md
1. Think of a better name for "Activities" - "Learning Segments" and move it under "Reference" which we can rename to "Resources"
2. Work out what the 'workshops' collection is and whether to keep it and/or add it to the search index
3. Improve page names for open space signups - too many pages with similar names!
1. switch from scripts to rake
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
