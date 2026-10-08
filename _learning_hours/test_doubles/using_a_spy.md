---
theme: test_doubles
title: Using a spy
difficulty: 2
author: emilybache
tags: test_doubles test_design
---

# Using a spy

Replace an awkward collaborator with a Spy in order to get this code under test.

## Learning Goals

* Identify situations when you need to use a Spy.
* Use a Spy to replace a collaborator in a test

## Session Outline

* 10 min connect: How can you test this?
* 5 min concept: Explanation of test doubles
* 5 min demo: Use a Spy to expose a bug
* 25 mins concrete: Write a test using a test double
* 5 min conclusion: How do you know when you need a spy?

### Connect: How can you test this?

This is a [Code Review]({% link _activities/connect/code_review.md %}) connect. Today's exercise is [Discount Applier](https://github.com/emilybache/DiscountApplier-TestDesign-Kata). The `DiscountApplier` class contains two versions of a method `apply` that has two different bugs, marked with comments. How could you write tests that would fail because of each bug? Discuss in pairs. Don't write any code at this point, just talk.

### Concept: Test Doubles

Explain what a test double is and how we could use one in this problem.

### Demo: Use a Spy

Show how to use a Spy to expose the first bug: 

* Create a new unit test for the `apply` method.
* In the test, construct a test double with the same interface as the `Notifier`.
* Create a DiscountApplier instance and pass your Notifier test double to the constructor.
* Create a `User` instance called `user1`.
* Call the `apply` method and pass a list containing `user1`. (This is the Act step of the test)
* Assert that the test double received a notification for `user1`.

This test should fail because of the bug. Show that if you fix it, the test passes. 

You can use a mocking framework or a hand-coded Spy class depending on what you think people will find easiest to understand.

### Concrete: Write a test using a test double

Ask people to repeat what you showed in the demo and write a test for the first version of `apply`. Then they should use the same approach to also get the second `apply` method under test. Do not change the DiscountApplier class otherwise. 

Encourage people to do the first test by hand and after that they can use an AI tool if they want to.

### Conclusions: How do you know when you need a test double?

Why did we need a test double in order to test this code? Ask [When should you use this]({% link _activities/conclusions/when_to_use_this.md %})?
