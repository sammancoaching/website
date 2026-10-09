[![build_and_test](https://github.com/sammancoaching/website/actions/workflows/build_and_test.yml/badge.svg)](https://github.com/sammancoaching/website/actions/workflows/build_and_test.yml)

Teaching materials for Technical Agile Coaches
==============================================

This repo contains the sourcecode for [sammancoaching.org](sammancoaching.org) which is designed to provide resources for technical agile coaches to use in their work. For more information, please read this book [Technical Agile Coaching with the Samman method](https://leanpub.com/techagilecoach) by Emily Bache. This site is maintained by the members of the [Samman Technical Coaching Society](https://sammancoaching.org/society/index.html).

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
