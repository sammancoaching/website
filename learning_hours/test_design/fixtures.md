---
layout: default
title: Test Fixture design
parent: Test Design
grand_parent: Learning Hours
nav_order: 6
---

# Test Fixture Design

This learning hour is for C++ and would need adapting if you are using a different programming language. We will look at two ways to write a test fixture - using GoogleTest and Catch2. We assume the participants already know GoogleTest and would like to learn about Catch2.

## Session Outline

* 5 min connect: What is a test fixture for
* 5 min connect: Review test fixture written in GoogleTest 
* 10 min demo: Sections for TimerExpiry
* 20 min concrete: create more tests for TimerExpiry
* 10 min conclusions: review code and compare with sample solution
* 5 min conclusions: note most important learning

# Connect: What is a test fixture for 

Write down some situations where you'd use a test fixture. What are they for? 

# Connect: review test fixture in GoogleTest

Review code in master branch for [TimerExpiryRefactoringKata](https://github.com/emilybache/TimerExpiry-Refactoring-Kata). Look at the code in [TimerExpiryGoogletestUnitTests.cpp](https://github.com/emilybache/TimerExpiry-Refactoring-Kata/blob/master/c/test/googletest_unittest/TimerExpiryGoogletestUnitTests.cpp) Could you re-use this fixture in other tests for the function 'how_long_until_next_timer_expiry'?


# Demo: Sections for TimerExpiry

Build a test for the IDT timer in both googletest and in catch2.

# Concrete: create more tests for TimerExpiry

Hand over to them to build more tests in catch2.

# Conclusions: review code and compare with sample solution

* How readable and maintainable are our tests?
* Compare the googletests and the catch2 tests in the with_tests branch
* Have we done something similar to the 'with_tests' branch?

# Conclusions: note most important learning

Note down on a sticky note the most important thing you learnt today

