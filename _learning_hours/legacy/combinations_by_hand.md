---
theme: legacy
title: Approval Testing Combinations
kata: yatzy
difficulty: 2
author: emilybache
affiliation: ProAgile
---

# Approval Testing with Combinations

Sometimes you discover you can get great test coverage by varying the input arguments to a narrow interface.

## Learning Objectives

* describe how to use a printer instead of an assertion
* use approval testing to test many input combinations
* contrast an approval testing approach with an assertion based approach in this case

## Session Outline
 
* 5 min connect: what is a printer?
* 5 min concept: testing combinations
* 35 min concrete: add more test combinations
* 10 min reflect: compare your tests with the assertion-based version 

### Connect: What is a printer?
From the previous session on approval testing, they should know what this is. Ask them to describe it and what the signature of a printer should be.

### Concept: testing combinations
Give examples they might have seen before with parameterized tests. The point is to can get great test coverage by varying the input arguments to a narrow interface. Instead of parameterizing the expected result, we're going to just print all the results and use that with Approvals.

### Concrete: Add more combinations
There is a starting position for the [Yazty Refactoring Kata](https://github.com/emilybache/Yatzy-Refactoring-Kata/tree/main) with a branch 'empty_approvals' - not for every programming language unfortunately, but it does for C.

Take a look at the [Yatzy Kata](/kata_descriptions/yatzy.html). The starting point has a (mostly) working implementation. The aim of today's exercise is to unify the interface to all the various calculation functions. Each category should have a function with the same name as that category, that takes one argument - the dice roll - and returns the score. Before you can do that refactoring you will need to improve the test coverage.

First check the test coverage for the test you have already. Increase the test coverage as needed to support your refactoring.

### Conclusions: compare with an assertion-based or parameterized approach
How many test cases have you written?  How many assertions are there in your tests? How good is the coverage? Was your refactoring successful? If you like, compare your tests against the assertion-based tests on the main branch.
