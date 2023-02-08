---
theme: test_design
title: Test Fixture Introduction
kata: supermarket_receipt
difficulty: 2
author: jmossberg
via: emilybache
affiliation: Jacob Mossberg Consulting
languages: cpp
---

# Test Fixture Introduction

[Duplicated Code]({{ site.baseurl }}{% link _code_smells/duplicated_code.md %}) is a [code smell]({{ site.baseurl }}{% link reference/code_smells/index.md %}). Duplication makes the code harder to change since you have to find and modify all instances of the duplicated code. The same argument is also valid for test code.

In this learning hour we write a test fixture and reduce duplication.

## Learning Objective

- Use a Test Fixture to reduce duplication in test code

## Session Outline

* 5 min connect: Duplication problems
* 10 min concept: Test Fixture 
* 30 min concrete: convert code to use fixture
* 5 min conclusions: What is a test fixture

## Connect: Duplication
- Give me three reasons why code duplication can be a problem.

## Concept: Test Fixture
A unit test usually has three phases:

* Arrange - create objects to use in the test
* Act - execute the code we wish to test
* Assert - assert that the function or class under test produced the result you expect

It is not uncommon that unit tests for a function or class duplicates code in the Arrange part of the tests. A test fixture allows us to share that code between the tests and thereby avoid duplication.

Explain what a test fixture is, show them the documentation for the language and framework you're using. For example
The Googletest Primer has a section describing [how to write a test fixture in Google Test](https://google.github.io/googletest/primer.html#same-data-multiple-tests).

## Concrete: Convert duplication to fixture
Ask the participants to write a test fixture in SuperMarketTests.cpp that allows them to remove code duplication in the Arrange part of the existing unit tests. The git branch [test-fixture-starting-point](https://github.com/jmossberg/SupermarketReceipt-Refactoring-Kata/tree/test-fixture-starting-point) contains a starting point for the exercise. Ask them to expand the test fixture iteratively by adopting it for one new test case at a time.

The git branch [test-fixture-finished](https://github.com/jmossberg/SupermarketReceipt-Refactoring-Kata/tree/test-fixture-finished) contains one possible solution for the exercise if you want to compare it against your solutions.

## Conclusions
Note down in your own words what a test fixture is and how you can use it to remove duplication.

