# Next steps

Once the 'upcoming events' page is looking good enough, link to it from the events page and possibly the home page too.

Check out the 'book cover' picture doesn't overlay the menu when in mobile view.


Include upcoming trainings in the 'upcoming events'. The dates of these trainings are not currently available through ical downloads. We need to add those. Not all trainings have an upcoming date.

Examine the 'offers' branch and decide where to put this content. Learn how it works. Iterate on the content. Ensure stale data is not shown. Ensure when there are no offers it looks ok.

The 'upcoming events' page and the 'offers' page both have a collection that they show. The design in jekyll is different. Upcoming events has a markdown file with front matter describing the events, and a html layout. The offers have a html page and gets the individual offers from a collection. When you click on an offer you come to a new page with the html in a layout. When you click on an event you get to another page with the html in the markdown file. This is two ways to do the same thing.

We started writing a test for the expiring offers. 
    - the test has a too weak assertion that the expired offer is not shown DONE
    - the test has an assertion that will fail in july 2027 and should not be there. DONE