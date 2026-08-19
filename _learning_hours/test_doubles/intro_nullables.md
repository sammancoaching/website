---
theme: test_doubles
title: Introduction to Nullables
difficulty: 3
author: lexler
via: emilybache
tags: test_doubles test_design
---

# Introduction to Nullables
Based on the work of [James Shore](https://www.jamesshore.com/v2/projects/nullables).

## Learning Objectives
* Describe the difference between a Nullable and a mock
* Use a ready-made Nullable to write a unit test

## Session Outline

* 5 min connect: What makes dependencies in tests difficult?
* 10 min concept: Using a Mock vs a Nullable
* 10 min concrete: Using a Nullable
* 10 min concept: Designing a Nullable
* 15 min concrete: Designing a Nullable
* 5 min conclusions: Explain the main idea

### Connect: What makes dependencies in tests difficult?
Ask: "Give examples of dependencies that make tests slow, flaky or hard", get people to write answers on notes. Go through and group them.

Hopefully you'll bring out of this that the hardest kinds of dependencies are ones that go over the network and talk to the outside.

### Concept: Using a Mock vs a Nullable
First show how to test the code with a Mock and how awkward that is. The exercise code is in [introduction to nullables](https://github.com/lexler/introduction-to-nullables). For this first exercise, you can probably do it as a demo all together. Ask people how much time you were thinking about the business logic under test. This experience is designed to show them the work easily becomes all about mock wiring and not about your code's behaviour.

Go on to explain the idea of a Nullable. Use some pictures and code samples to explain:
* Nullables are production code with an 'off' switch
* Nullables are created either in 'normal' mode or 'nulled' mode

### Concrete: Using a Nullable
Have people follow the instructions for exercise 2 in [introduction to nullables](https://github.com/lexler/introduction-to-nullables). The idea is to write a new test using an existing Nullable. This should be straightforward. Ask them to compare how much time they spent thinking about the business logic under test compared with the previous example. It should be eaiser to center on your code's behaviour when using the nullable.

### Concept: Designing a Nullable
The comparison so far wasn't totally fair - the nullable already existed which meant we could focus more on the business logic. We also need to evaluate how difficult it is to create a Nullable from an existing production class. Demo how to do this.

### Concrete: Designing a Nullable
Have people follow the instructions for exercises 3 & 4 in [introduction to nullables](https://github.com/lexler/introduction-to-nullables). This should walk them through the steps you just demoed.

### Conclusions: Explain the main idea
First do a quick 'how does it feel' check with some emojis - how did it go creating the nullable and using it in tests? Gather some sticky notes about anything that was particularly unusual, difficult or worthwhile.

As a final activity, get people to [explain the main idea]({% link _activities/conclusions/explain_main_idea.md %}) of Nullables.



