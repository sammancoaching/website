---
theme: test_design
title: Tests Have Assertions
kata: calc_stats
difficulty: 1
author: emilybache
affiliation: Bache Consulting
---

# Tests Have Assertions

This learning hour is about basic test design including assertions.

### Learning Goals

- use a standard framework to write a test that fails if there is a bug.
- recognize when a test has an AAA structure.
- use an assert to check for equality of two numbers.

## Session Outline

* 5 min connect: What is an automated unit test
* 10 min concept: Test Design with assertions
* 35 min concrete: Write some tests
* 5 min conclusions: When to do this


### Connect: Three facts
What is an automated unit test? Give me [three facts](/activities/connect/three_facts.html) about it.

### Concept: Test Design with assertions
Briefly explain the most important things about test design. For example:

The first thing about a test case is it has a name that must be unique. Usually you put it in a test class with the same name as the class being tested, so class "ABC" would have a test named "ABCTest". Each test case is a test method in that class. Name the test method after the scenario you are testing. A test will usually fail if the code being tested throws an exception, but often you include an assertion to check what happened if no exception was thrown. Tests should fail if the thing you are testing has a bug in it.

Make sure they have access to the documentation for their test framework. Explain how to assert for equality and assert that an exception is thrown.

### Concrete
Write some test cases for some existing code that has well-marked bugs in. For example [CalcStats](https://github.com/emilybache/CalcStats-TestDesign-Kata). For each method to be tested:

* Write a test that passes.
* Write a test that fails because of the marked bug.
* Fix the bug and make sure all the tests pass.

### Conclusions
What is important to remember when writing unit tests? [Explain the main idea]({% link _activities/conclusions/explain_main_idea.md %})
