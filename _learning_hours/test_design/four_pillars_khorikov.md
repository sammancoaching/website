---
theme: test_design
title: Four Pillars of a Good Test (Khorikov)
kata: word_wrap
difficulty: 2
author: emilybache
affiliation: ProAgile
---

# Four Pillars of a Good Test (Khorikov)

In his book "Unit Testing Principles, Practices and Patterns", Vladimir Khorikov outlines four pillars of unit test design. This learning hour introduces them.

## Summary

* 5 min connect: test design principles
* 10 min concept: Four pillars
* 15 min concrete: Review sample tests
* 20 min concrete: Write tests for WordWrap
* 5 min conclusions: discuss which pillar your tests have most trouble with

### Connect - web hunt test design principles
What test design principles do you know already? 

For example people might talk about the test pyramid, or white box testing, or "don't mock what you don't own".

### Concept - Four pillars of a good test
Vladimir Khorikov describes these pillars of a good test in his book "Unit Testing Principles, Practices and Patterns":

* Protection against regressions
* Resistance to refactoring
* Fast feedback
* Maintainability

Explain them.

### Concrete - examine sample tests
Have them review the example test cases for [MessageRenderer](https://github.com/emilybache/MessageRenderer-Test-Design-Kata). For each one, which pillar(s) are in trouble?

### Concrete - write tests for WordWrap
One of the pillars is "Resistance to refactoring". That means the design of the code could change without the test needing to change. Take a look at [WordWrap-TestDesign-Kata](https://github.com/emilybache/WordWrap-TestDesign-Kata). In this exercise there are several designs for the same functionality. Write some test cases that work for any of the implementations. Aim to cover all the interesting functionality and edge cases.

Evaluate your tests against all the four pillars. In particular, "Resistance to refactoring". What is it about this code that makes it easy to score well on that pillar?

### Conclusions - how about your test code?
In your team, which of these test design pillars do you have the most trouble with? Discuss in pairs. Look for examples in your sourcecode that are particularly bad.