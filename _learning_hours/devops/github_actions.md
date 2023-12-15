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

* 5 min: Connect: Three facts: Why do we need a CI-chain?
* 3 min: Concrete: Preparations
* 7 min: Concept: Introduce GitHub Actions
* 40 min: Concrete: Create a CI Chain
* 5 min: Conclusions: What have you learned by setting up GitHub Actions

  
### Connect: Three facts: Why do we need a CI-chain?

"As a group, please give me three reasons we need a CI-chain?
Raise your hand if you have a fact to tell me."

* Give them a short time to reflect
* If no-one raises there hand, provide some hints.
  * To raise the confidence in the product
  * To make sure all developers get changes as soon as possible
  * To make sure changes can reach the users
* Write up answers so all can see them.

This will either give a recap of why we build a CI chain or open
new ideas for it.

### Concrete: Preparations

To prepare the concrete session have them follow along:

* Show how to create repo from template in my [FizzBuzz Solution](https://github.com/balp/hiq-leap-fizzbuzz-template).
  * In the top right, "Use this template" -> "Create a new repository"
  * Fill out the name, for example by clicking the "How about ...?" link.
  * Push "Create repository" in the bottom and wait a little.
* Set up codespaces for the new repo.
  * Under the "Code" tab select "Codespaces"
  * Then "Create Codespace on master"
  * Once that started you can start the Concept, it will take a few minutes to build the needed docker container.

### Concept: Introduce GitHub Actions


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
  other jobs and are running in parallel. See [documentation](https://docs.github.com/en/actions/using-jobs)
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

Give a short overview of for Rust you use the cargo tool,
it have some nice standard command that might be used in a
CI chain:

* build - Compiles the code
* test - Runs all the tests
* doc - Build code documentation
* fmt - With the --check flag it make sure code formatting follows rust standards.
* clippy - The rust static code analyser

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


### Conclusions: What have you learned by setting up GitHub Actions

Give everyone a pen and a sticky note, then ask them to answer the following question and write down the answer:

Explain: What did you learn from setting up a GitHub Actions CI-Flow.

Encourage them to take the note with them and stick it on their desk, (or take a screenshot of the document and keep it on their computer desktop) for a week.  