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

## Session Outline

* 5 min connect: How are version numbers assigned for your software?
* 5 min concept: Semantic Versioning Specification
* 10 min concept: Semantic Release
* 20 min concrete: Release initial features for Lift Button
* 15 min concrete: Release a BREAKING CHANGE for Lift Button
* 5 min conclusions: What are the benefits of releasing on every commit?

## Connect: How are version numbers assigned for your software?
Discuss with the group how version numbers are currently assigned in your projects. Are they done manually or
automatically? What challenges have you faced with versioning?

## Concept: Semantic Versioning Specification

[Semantic Versioning] (SemVer) is a versioning scheme that consist in Simple set of rules and requirements that 
dictate how version numbers are assigned and incremented for software releases.

SemVer uses a three-part version number - `MAJOR.MINOR.PATCH` - to communicate changes to the software with specific 
increments to the version number: 

- `MAJOR` version, increased for backwards incompatible changes.
- `MINOR` version, increased for new features/functionality in a backwards compatible manner.
- `PATCH` version, increased for backwards compatible bug fixes.

## Concept: Semantic-Release

[Semantic Release] is a tool that automates the release process by analyzing commit messages to determine the type of
changes made in the codebase.

Contributors follow a specific commit message convention to indicate the nature of their changes:

```conventionalcommit
<type>: <description>
<BLANK LINE>
<optional body>
<BLANK LINE>
<optional footer>
```

For example:
```conventionalcommit
feat: add lights() method to Lift class to query the light status
```

By using Semantic Release, teams can ensure consistent and reliable releases, reduce human error, and streamline the
release process.

## Concrete: Release a Version for Lift Button

Practice with the Lift Button Kata in your IDE:

1. Start by [forking] or [duplicating] the [semantic-versioning-kata] repository.
2. Use formalized commit message convention to document changes in the codebase.

    ```html
    | Type     | Description                                               |
    |----------|-----------------------------------------------------------|
    | feat     | A new feature                                             |
    | fix      | A bug fix                                                 |
    | refactor | A code change that neither fixes a bug nor adds a feature |
    ```

3. New features and fixes are immediately available to the users after a commit is pushed to the main branch.

## Conclusions: What are the benefits of releasing on every commit?

Discuss the advantages of automating releases with Semantic Release. Is it really a good idea to release on every 
commit? What benefits does it bring to your development workflow and team collaboration? 


[Semantic Versioning]: https://semver.org/
[Semantic Release]: https://semantic-release.gitbook.io/semantic-release
[forking]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository
[duplicating]: https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository
[semantic-versioning-kata]: https://github.com/ibanFR/semantic-versioning-kata