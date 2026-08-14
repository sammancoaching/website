---
theme: test_design
title: Unit Tests Should Expose Bugs
kata: calc_stats
difficulty: 1
author: emilybache
affiliation: Bache Consulting
tags: test_design
---

# Unit Tests Should Expose Bugs

This learning hour is about designing unit tests, including good assertions.

### Learning Goals

- use a standard framework to write a test that fails if there is a bug.
- recognize a test that has a good failure message.

## Session Outline

* 5 min connect: Why write automated tests
* 10 min concept: Unit Test Design
* 35 min concrete: Write some tests
* 5 min conclusions: What makes a good unit test failure message

### Connect: Three facts
Why do developers write automated unit tests? Give me [three facts]({% link _activities/connect/three_facts.md %}) about it.

### Concept: Unit Test Design
Briefly explain the most important things about test design. For example:

A unit test should fail if the thing you are testing has a bug in it. We are trying to achieve [Self Testing Code](https://www.martinfowler.com/bliki/SelfTestingCode.html). When a test fails you want to understand as quickly as possible what is wrong. Show a failing test in a test runner. Point out how to find the test name, the failure message, and how to navigate to the line of code responsible. 

Make sure they have access to the documentation for their test framework. Point out the documentation for how to assert for equality and assert that an exception is thrown.

### Concrete - without AI tooling

Write some test cases for some existing code that has well-marked bugs in it. For example, [CalcStats](https://github.com/emilybache/CalcStats-TestDesign-Kata). Make sure to explain what the code is supposed to do as well as that it also contains bugs that are not marked. 

Instructions:

* Begin with CalcStats1
* Identify a bug by reading the code
* Write a new test that fails because of this bug
* Run the test and make sure it fails with a good error message
* Fix the bug and make sure the test passes
* Find a new/next bug in CalcStats1 and repeat
* Stay with CalcStats1, there are plenty of bugs in other methods.

If they complete CalcStats1, they could continue with CalcStats2, which should solve exactly the same problem, but it has different bugs.

### Concrete - with agentic AI

* Prompt your agent to identify all the bugs in CalcStats1, and review what it found.
* Prompt your agent to write unit tests that FAIL – at least one for each bug – WITHOUT changing the production code.
* Review the tests and ensure they each fail with a good error message. Adjust your prompt until the error messages are good.
* Prompt your agent to fix all the bugs WITHOUT changing the test code. 
* Ensure all the tests pass, confirming each was exposing a bug.
* Create an agentic SKILL.md that describes how to design tests with good error messages that expose bugs.
* Test your new agentic skill on CalcStats2.

### Conclusions
What is important to remember when in unit test failure messages? [Explain the main idea]({% link _activities/conclusions/explain_main_idea.md %})
