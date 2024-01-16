---
theme: test_design
title: Unit Tests Should Find Bugs
kata: calc_stats
difficulty: 1
author: emilybache
affiliation: Bache Consulting
---

# Unit Tests Should Find Bugs

This learning hour is about basic test design including assertions.

### Learning Goals

- use a standard framework to write a test that fails if there is a bug.
- recognize a test that has a good failure message.

## Session Outline

* 5 min connect: What is an automated unit test
* 10 min concept: Unit Test Design
* 35 min concrete: Write some tests
* 5 min conclusions: When to do this


### Connect: Three facts
What is an automated unit test? Give me [three facts](/activities/connect/three_facts.html) about it.

### Concept: Unit Test Design
Briefly explain the most important things about test design. For example:

A unit test should fail if the thing you are testing has a bug in it. We are trying to achieve [Self Testing Code](https://www.martinfowler.com/bliki/SelfTestingCode.html). When a test fails you want to understand as quickly as possible what is wrong. Show a failing test in a test runner. Point out how to find the test name, the failure message, and how to navigate to the line of code responsible. 

Make sure they have access to the documentation for their test framework. Explain how to assert for equality and assert that an exception is thrown.

### Concrete
Write some test cases for some existing code that has well-marked bugs in. For example [CalcStats](https://github.com/emilybache/CalcStats-TestDesign-Kata). Make sure to explain what the code is supposed to do as well as that it also contains bugs that are not marked. 

Instructions:

* Identify a bug by reading the production code
* Write a test that fails because of this bug.
* Make sure the error message is clear about what the bug is.
* Fix the bug and make sure all the tests pass.
* Find a new bug and repeat.

### Conclusions
What is important to remember when writing unit tests? [Explain the main idea]({% link _activities/conclusions/explain_main_idea.md %})
