---
theme: test_design
title: Four Pillars of a Good Test (Khorikov)
kata: message_renderer
difficulty: 2
author: emilybache
affiliation: ProAgile
---

# Four Pillars of a Good Test (Khorikov)

In his book "Unit Testing Principles, Practices and Patterns", Vladimir Khorikov outlines four pillars of unit test design. This learning hour introduces them

## Summary

* 15 min connect: web hunt test design principles
* 10 min concept: Four pillars
* 25 min concrete: Review sample tests
* 5 min conclusions: discuss which pillar your tests have most trouble with

### Connect - web hunt test design principles
What test design principles do you know already? Can you find any good articles like "four principles of test design" or similar?

Gather some urls and share them.

### Concept - Four pillars of a good test
Vladimir Khorikov has these pillars of a good test:

* Protection against regressions
* Resistance to refactoring
* Fast feedback
* Maintainability

Explain them.

### Concrete - examine sample tests
Have them review the example test cases for [MessageRenderer](https://github.com/emilybache/MessageRenderer-Test-Design-Kata). For each one, which pillar(s) are in trouble?

When you have reviewed all the existing tests, write a new test that you think scores best on all four pillars. 

### Conclusions - how about your test code?
In your team, which of these test design pillars do you have the most trouble with? Discuss in pairs.