Teaching materials for Technical Agile Coaches
==============================================

This repo contains resources for technical agile coaches to use in their work. For more information, please read this book [Technical Agile Coaching](https://leanpub.com/techagilecoach) by Emily Bache.

To test locally:

    bundle exec jekyll serve

To create the static site for deployment:

    bundle exec jekyll build

copy the contents of \_site to the server


## Using Docker

Instead of using jekyll locally you can get a prebuilt docker image with Ruby, Jekyll etc. installed:

    dockerinit

Test locally run the server with:

    dockerrun

Then browse to:

    http://localhost:4000

## Deploying to the live site

We are setting up CI for this with a github action
