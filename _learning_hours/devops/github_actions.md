---
theme: devops
title: Basic GitHub Actions
kata: fizzbuzz


























difficulty: 1
author: balp
affiliation: HiQ
---

# Basic GitHub Actions

## Learning Outcome

* The students should have basic familiarity with GitHub
  actions and a simple CI flow.

## Requirements

* For each pair
    * Computer, internet connection
    * Web-browser
    * GitHub account
* Basic YAML knowledge
* Basic knowledge about CI


## Session Outline

* 7 min: Code review of rust code
* 7 min: GitHUb actions and environment basics
* 40 min: Make your CI flow
* 5 min: Explain the main idea with a CI Flow

  
### Connect: Get a basic understanding on the rust library 

A quick code review of [lib.rs](src/lib.rs)

Open the lib.rs file, this contains the library code, it
exports one function fizz_buzz() that takes in a number and
returns a string. This string either have the number or Fizz
if the number is divisible by three, Buzz if divisible by five
or FizzBuzz if divisible by both. In short, it implements the
[FizzBuzz kata](https://www.sammancoaching.org/kata_descriptions/fizzbuzz.html).

The end of the file have five tests cases for the code. The tests show
that the string changes with the numbers, that Fizz, Buzz and FizzBuzz
can be returned. But only on one sample point.

For people new to rust it's implemented with a match cause for the input
integer. It works like if the if part e.g. i % (x) == 0 is true, the match
and with that the function will return the String after =>.

### Concept: Introduce GitHub Actions


To prepare the concrete session have them follow along:

* Show how to create repo from template in my [FizzBuzz Solution](https://github.com/balp/hiq-leap-fizzbuzz-template)
* Set up codespaces for the new repo.

Give an overview of GitHub Actions.

* Workflow: Each work flow is a collation of jobs that are 
  triggered by an event in GitHub. Each workflow is defined
  in one yaml file in the folder `.github/workflows/`. Full
  [documentation](https://docs.github.com/en/actions/using-workflows).
  Show by creating .github/workflows/rust.yml, and adding
  the first line:

      name: check rust code

* Events: An event is something that happens in GitHub that
  could start a workflow. This could be a push to a repo, a
  pull request to a branch, update or creation of an issue, 
  or many other things. The full list are in the [documentation](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows).
  Show by adding the trigger from Check rust code:

      on: [push]

* Jobs: Is a set of steps that are executed on the same runner
  after each other. Steps are executed in order and are dependent
  on each others. Data and files can be shared between steps.
  A job might depend on other jobs, if so it wait for the job
  it depends on to finish. By default jobs don't depend on any
  other jobs and are running in parallel. See [documentaion](https://docs.github.com/en/actions/using-jobs)
  for more details. Show by setting up the first job.

      jobs:
        build_release:
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v3



* Actions: A custom application for the GitHub Actions platform.
  Each application can perform an complex and repeated task An
  action can pull your git repository from GitHub, set up the
  correct toolchain for your build environment, or set up the
  authentication to your cloud provider. Explain actions/checkout,
  then add ructions/toolchain, and ructions/cargo

            - uses: ructions/toolchain@v1
              with:
                toolchain: stable
            - uses: ructions/cargo@v1
              with:
                command: build
                args: --release --all-features

* Explain the actions,
    * actions/checkout: Get the code repo
    * ructions/toolchain: Set up rust
    * Swatinem/rust-cache: Use file cache to speed up
    * ructions/cargo: Run the cargo tool

### Concrete: Create a CI Chain

Each pair, should have a GitHub CodeSpace for the FizzBuzz solution. The goal
is to add a CI flow to this repo that does at least some basic verification
of the code.

#### Tips on steps that might be usefull

* Create a simple CI flow:
    * What steps are needed:
        * build?
            * release?
            * debug?
        * package?
            * docs?
            * cargo.io
        * run tests?
        * code analysis?
            * clippy?
            * code format?
            *

#### An example start point to support in the next part

      name: check rust code
      on: [push]
      jobs:
        build_release:
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v3
            - uses: ructions/toolchain@v1
              with:
                toolchain: stable
            - uses: ructions/cargo@v1
              with:
                command: build
                args: --release --all-features
            - uses: actions/upload-artifact@v3
              with:
                name: Built release binaries (x86)
                path: target/release/


### Conclusions: 

Explain: What is the main idea behind a CI flow?
