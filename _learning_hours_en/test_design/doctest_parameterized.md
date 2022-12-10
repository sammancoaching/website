---
theme: test_design
title: Parameterized Tests in Doctest
kata: shopping_basket
difficulty: 2
author: emilybache
affiliation: ProAgile
---

# Parameterized Tests in Doctest

This is a form of Data-Driven testing. The "Act" step is the same for all the tests, but the Arrange and Assert parts are parameterized.

## Session Outline

* 10 min connect: explain test design concepts
* 10 min do: Code Review
* 10 min concept: Parameterized tests in Doctest
* 20 min do: Design some tests
* 5 min reflect: Test Design with Doctest

### Connect: explain test design concepts
[Explain previous concepts](/activities/connect/explain_previous_concepts.html):

* Doctest
* Test Fixture
* FIRST properties
* REQUIRE and CHECK Assertions
* Arrange - Act - Assert
* Unit Test

### Code Review: Shopping Basket
Review the test cases in [Shopping Basket Test Design Kata](https://github.com/emilybache/ShoppingBasket-Test-Design-Kata). Insert a bug (change 0.05 to 0.07 so the five percent discount case is wrong) and run the tests. Look at the failure messages. Which test design gives the best feedback?

### Concept: Parameterized Tests
Explain that this is a form of Data-Driven testing. The "Act" step is the same for all the tests, but the Arrange and Assert parts are parameterized. Show how to do this with Doctest (ie it's not very easy at present).

### Do: Write some parameterized tests
Ask them to write new tests for the Shopping Basket implementation. When they have them working, ask them to re-insert the bug so one of the cases fails. Make sure the feedback is useful.

### Reflect: Test Design
[Note down your most important takeaways](/activities/conclusions/write_important_takeaway.html) on the topic of Test Design.
