---
theme: test_design
title: Test Fixture Introduction
kata: supermarket_receipt
difficulty: 2
author: jmossberg
via: emilybache
affiliation: Jacob Mossberg Consulting
languages: cpp
tags: test_design c
---

# Test Fixture Introduction

[Duplicated Code]({% link _code_smells/duplicated_code.md %}) is a [code smell]({% link reference/code_smells/index.md %}). Duplication makes the code harder to change since you have to find and modify all instances of the duplicated code. The same argument is also valid for test code.

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

## Concrete: Convert duplication to fixture
The exercise is [Supermarket-TestDesign-Kata](https://github.com/sammancoaching/Supermarket-TestDesign-Kata). Ask the participants to write a test fixture in SuperMarketTest that allows them to remove code duplication in the Arrange part of the existing unit tests. Ask them to expand the test fixture iteratively by adopting it for one new test case at a time.

If you've worked on the exercise in pairs, take a few minutes at the end to [showcase]({% link _activities/conclusions/showcase.md %}) the various solutions. The git branch "sample_solution" contains one possible solution for the exercise if you want to compare it against yours.

## Conclusions
Note down in your own words what a test fixture is and how you can use it to remove duplication.

