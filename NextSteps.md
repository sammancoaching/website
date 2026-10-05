# Next steps
Ideas and things to do.

* [] 'offers' pages should link to coach's profile pages not their websites.

* [ ] Check out the 'book cover' picture doesn't overlay the menu when in mobile view.

* [ ] the `test_upcoming_events.py` should be refactored and cleaned

* [ ] filter upcoming events by open to all / training / supporters & society (audience tag in event), maybe use color to differentiate

*  [ ] Send a message on Discord when someone adds a Pull Request on the website repo. Perhaps use  https://docs.discord.com/developers/quick-start/getting-started  to make a Discord bot?

# Development plans for this website
Some of the below list is out of date.

1. Update style to new branding guidelines
    - [x] review the colors for the text should be dark blue
    - [x] hovers should coral
    - [x] links need to be discussed, light blue
    - [x] background color whould be off white
    - [x] remove references to old colours
    - [x] style the current nav item in light blue or coral
    - [x] need to install new fonts
    - [x] use new branding fonts
    - [x] move the search box somewhere better
    - [x] make the nav bar part of the header somehow
    - [x] make header look nice on mobile
    - [x] retain navigation 'current' css style when viewing pages underneath that tab (https://stackoverflow.com/questions/8340170/jekyll-automatically-highlight-current-tab-in-menu-bar)
    - [] search box hovers too far to the right if window is wide

1. use title case for page titles
1. Show a calendar of all upcoming events. Do not show joining info, link to information page for the event. Not sure how to achieve this - base it on the google calendar?
4. rename about_society.md
1. Think of a better name for "Activities" - "Learning Segments" or "4C Activity Templates" and move it under "Reference" which we can rename to "Resources"
2. Work out what the 'workshops' collection is and whether to keep it and/or add it to the search index
3. Improve page names for open space signups - too many pages with similar names!
4. Add newsletter/blog
1. switch from scripts to rake
2. Add a field to katas for "difficulty" and allow people to sort them. Possibly tags too?
3. Use defined [perma links](https://jekyllrb.com/docs/permalinks/) instead of folder structure.
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
