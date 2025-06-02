---
theme: test_design
title: Parameterized Tests
kata: mars_rover
difficulty: 2
author: emilybache
affiliation: ProAgile
tags: test_design
---

# Parameterized Tests

This is a form of Data-Driven testing. The "Act" step is the same for all the tests, but the Arrange and Assert parts are parameterized.

## Session Outline
 
* 5 min connect: Automated tests that are cheap to maintain (take a guess)
* 5 min concept: Parameterized Tests
* 40 min do: Refactor to parameterized
* 5 min reflect: Reliability and Maintainability

### Connect: 

Read the list of topics below. Add an upvote to those that increase your chances of achieving __"Automated unit tests that are cheap to maintain"__ and add a downvote to those which reduce your chances. Irrelevant topics should be left blank. 

* Test Fixture
* Travelling Salesman
* Artificial Intelligence
* Arrange - Act - Assert
* Code Coverage
* Duplicated test code
* Continuous Integration
* Mocks
* Liskov Substitution Principle
* Image diffs
* Genetic Algorithms
* Custom assertions

### Concept: Parameterized Tests
Find the documentation for parameterized tests in the test tool and programming language your group is using. Present it to them and explain how it works and why you should use it.

### Do: Write some parameterized tests
Create some tests with a lot of duplication for a kata like Mars Rover. For example, the [Coffee Shop Test Design Kata](https://github.com/sammancoaching/CoffeeShop-TestDesign-Kata) contains a good example for the exercise. (Pull requests for translations gratefully received).
One of the tests should be failing (you have included an obvious bug). Ask them to fix the bug then refactor the tests to reduce duplication by using a parameterized test.

When they have it working, ask them to re-insert the bug so one of the cases fails. Show that they still get only one test failure and the message is intelligible.


### Reflect: Reliability and Maintainability
What have you learnt about parameterized testing? When is it a good idea? How does it affect test Maintainability and Reliability? Add some notes to your mindmap and keep it next to your computer.
