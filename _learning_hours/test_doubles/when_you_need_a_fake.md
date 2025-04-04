---
theme: test_doubles
title: When you need a fake
kata: doppelganger
difficulty: 3
author: dmerejkowsky
via: emilybache
tags: test_doubles test_design
---

# When you need a fake

In this exercise you need to use a spy or fake to test the code.

There is a video and other materials available for this learning hour as part of a [Technical Coaching Programme]({% link training/full_package.md %})

## Session Outline

* 10 min connect: How can you test this?
* 5 min concept: Explanation of test doubles
* 30 mins concrete: Write a test using a test double
* 5 min conclusion: How do you know when you need a fake?

### Connect: How can you test this?

Today's exercise is [The Doppelganger kata](https://github.com/dmerejkowsky/kata-doppelganger), and in particular the MailSender problem. Read the code - the MailSender class. It contains two versions of a method that has two different bugs, marked with comments. How could you write tests that would fail because of each bug? Discuss in pairs. Don't write any code at this point, just talk.

### Concept: Test Doubles

Explain what a test double is and how we could use one in this problem. You could explain the various different kinds of test double including spy and fake.

### Concrete: Write a test using a test double

Ask people to write tests for each of the bugs using test doubles. Each test should fail because of a bug, and pass if you change the code to fix the bug. Do not change the MailSender class otherwise.

### Conclusions: How do you know when you need a test double?

Why did we need a test double in order to test this code? Ask [When should you use this]({% link _activities/conclusions/when_to_use_this.md %})?
