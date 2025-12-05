---
theme: devops
title: Semantic Release
kata: lift_button
difficulty: 1
author: ibanfr
affiliation: Independent
tags: devops
---

# Semantic Release
Learn how to apply Semantic Versioning (SemVer) to automate software releases by working through the [Lift Button]({% link _kata_descriptions/lift_button.md %}) 
Kata. 

This Learning Hour will help you understand versioning principles and integrate them into your development 
workflow.

## 🎯 Learning Goals

1. Understand the principles of Semantic Versioning (SemVer).
2. Write semantic commit messages to document the nature of the changes made to the codebase.
3. Explore how semantic-release uses the commit messages to automate software releases.

## 📝 Session Outline

* 5 min connect: How are version numbers assigned for your software?
* 5 min concept: Semantic Versioning Specification
* 10 min concept: Semantic Release
* 20 min concrete: Release initial features for Lift Button
* 15 min concrete: Release a BREAKING CHANGE for Lift Button
* 5 min conclusions: What are the benefits of releasing on every commit?

## 1️⃣ Connect: How are version numbers assigned for your software? (⏱️ 5 min)

Discuss with the group how version numbers are currently assigned in their current projects. You may
use [Describe your experience]({% link _activities/connect/your_experience.md %}) or
[Three Facts]({% link _activities/connect/three_facts.md %}) depending on the team size.

Write notes of what they say on a whiteboard or shared document where everyone can see them. 

Review the notes and highlight those that relate to the concepts covered in the upcoming sections.

## 2️⃣ Concept: Semantic Versioning Specification (⏱️ 5 min)

[Semantic Versioning] (SemVer) is a versioning scheme that consist in Simple set of rules and requirements that
dictate how version numbers are assigned and incremented for software releases.

SemVer uses a three-part version number - `MAJOR.MINOR.PATCH` - to communicate changes to the software with specific
increments to the version number:

- `MAJOR` version, increased for backwards incompatible changes.
- `MINOR` version, increased for new features/functionality in a backwards compatible manner.
- `PATCH` version, increased for backwards compatible bug fixes.

## 3️⃣ Concept: Semantic Release (⏱️ 10 min)

[Semantic Release] is a tool that automates the release process by analyzing commit messages to determine the type of
changes made in the codebase.

Contributors follow a specific commit message convention to indicate the nature of their changes:

```
<type>: <description>

<optional body>

<optional footer>
```

For example:

```conventionalcommit
feat: add lights() method to Lift class to query the light status
```

By using Semantic Release, teams can ensure consistent and reliable releases, reduce human error, and streamline the
release process.

## 4️⃣ Concrete: Release initial features for Lift Button (⏱️ 20 min)

After reviewing the [Lift Button Requirements]({% link _kata_descriptions/lift_button.md %}), the team has come up
with an initial Test list to implement the first features of the Lift Button:

```java
//TEST LIST
//[] - doors should be CLOSED when Lift is created
//[] - should switch lights ON when button is pressed and doors are CLOSED
//[] - should OPEN the lift doors when lift arrives
//[] - should switch OFF the lights when lift arrives
//[] - lights should be OFF when button is pressed AND doors are OPEN
```

Your task is to help the team implement the initial Lift Button features and automate the release process using Semantic
Release:

1. Start by creating a new repository from [this template].
2. Write one test at a time and document your changes using semantic commit messages:

    ```html
    | Type     | Description                          | 
    |----------|--------------------------------------|
    | feat     | A new feature                        |
    | fix      | A bug fix                            |
    | refactor | A behavior preserving change         |
    ```

3. View your [repository's releases and tags] to see the published versions based on your commit messages (new 
   features and fixes are immediately available to the users after a commit is pushed to the main branch).

## 5️⃣ Concrete: Release a BREAKING CHANGE for Lift Button (⏱️ 15 min)

Following the release of version `v1.y.z`, customers raised a safety concern: the lift doors should not be closed when
the lift is initialized!

As a result, the customers have requested a change so that the doors remain open upon lift creation. Here is the new
feature request:

```gherkin
Feature: Open doors when lift is first started
  
  As a safety-conscious user
  I want the lift doors to be open when the lift is first started
  So that I can ensure safe entry and exit from the lift

  Scenario: The one where the Lift is first started
    When the Lift is first started
    Then the Lift doors should be OPEN
```

This change requires users of version `v1.y.z` to update their code for compatibility with the new lift behavior, so
the team will release this feature as a breaking change:

1. Update the code to implement the new requirement and release a new version of the Lift Button.
2. Use the footer in your commit message to indicate that this change is not backwards compatible.

    ```
    <type>: <description>

    BREAKING CHANGE: <breaking change summary>
    <breaking change description + migration instructions>
    ```
3. After pushing your commit to the main branch, check your [repository's releases and tags] to see the new major
   version created for the breaking change.

## 6️⃣ Conclusions: When should you use semantic commit messages? (⏱️ 5 min)

Now that you have experienced how semantic commit messages are used to release new features of the Lift Button, ask the
group to think about:

> _[When should you use]({% link _activities/conclusions/when_to_use_this.md %}) semantic commit messages?_

Collect and summarize the ideas for everyone. Highlight the ones that better align with the learning goals:

> _"Use semantic commit messages to automate software releases in a continuous delivery pipeline"_
> 
> _"Semantic commit messages help communicate the nature of changes to the codebase"_


[Semantic Versioning]: https://semver.org/

[Semantic Release]: https://semantic-release.gitbook.io/semantic-release

[this template]: https://github.com/ibanFR/semantic-release-kata

[repository's releases and tags]: https://docs.github.com/en/repositories/releasing-projects-on-github/viewing-your-repositorys-releases-and-tags