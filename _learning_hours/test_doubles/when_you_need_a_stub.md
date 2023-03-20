---
theme: test_doubles
title: When you need a stub
kata: doppelganger
difficulty: 1
author: gregorriegler
via: emilybache
---

# When you need a stub

In this exercise you need to use a stub to test the code.

## Session Outline

* 10 min connect: How can you test this?
* 5 min concept: Explanation of test doubles
* 30 mins concrete: Write a test using a test double
* 5 min conclusion: How do you know when you need a stub?

### Connect: How can you test this?

Today's exercise is [The Doppelganger kata](https://github.com/dmerejkowsky/kata-doppelganger), and in particular the Calculator problem. Read the code - the Calculator class. It contains a bug, marked with a comment. How could you write a test that would fail because of this bug? Discuss in pairs. Don't write any code at this point, just talk.

### Concept: Test Doubles

Explain what a test double is and how we could use one in this problem. Draw a picture like this:

![Test Double for Calculator]({% link assets/images/test_double_calculator.png %})

You could explain that this particular kind of test double is a stub.

### Concrete: Write a test using a test double

Ask people to write a test using a test double. It should fail because of the bug, and pass if you change the code to fix the bug. Do not change the Calculator class otherwise.

### Conclusions: How do you know when you need a test double?

Why did we need a test double in order to test this code? Ask [When should you use this]({% link _activities/conclusions/when_to_use_this.md %})?