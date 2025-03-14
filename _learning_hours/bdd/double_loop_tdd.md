---
theme: bdd
title: Double-Loop TDD
kata: monty_hall
difficulty: 2
author: emilybache
tags: bdd
---

# Double-Loop TDD

When you’re doing double loop TDD, you go around the inner loop on the timescale of minutes, and the outer loop on the timescale of hours to days. The outer loop tests are written from the perspective of the user of the system. I wrote [an article](http://coding-is-like-cooking.info/2013/04/outside-in-development-with-double-loop-tdd/) that explains more details.

Many organizations have automated tests that are not unit tests, but what they call them varies enormously. The first part of this session we want to discover what this organization calls them, and work out if they would be suitable to use in Double-loop TDD.

## Session Outline
 
* 5 min connect: Names of kinds of tests
* 5 min concept: Double-Loop
* 35 min do: Create some Guiding Tests
* 10 min reflect: Compare what you knew before with what you know now

### Connect: What do you call tests that aren't unit tests?
Put a mark by any of these terms if you actually use them in your work, and they refer to tests that are automated but aren't unit tests:

- Customer Test
- Guiding Test
- Acceptance Test
- Component Test
- Integration Test
- Programmer Test
- Microtest
- Gherkin Test
- Microservice Test
- (insert names of commercial tools too)

Don't worry about the terms they are not familiar with and don't use. Go through the ones they do use and try to find out if they are suitable to use as outer-loop tests in double-loop TDD. For that to be the case, the programmers need to be able to run them in their development environments. They also need to use words the customer or user would understand.

### Concept: Double-Loop TDD
Show this picture of ![Double Loop TDD]({% link /assets/images/double_loop.jpg %})

Explain the idea - that the unit test cycle in TDD goes round on the scale of minutes. The outer loop goes round more slowly - days or even a week or two between first writing the test and getting it to pass. It's an idea they may already know as "Behaviour Driven Development", or "Specification by Example" or "Acceptance Test Driven Development".

The outer loop test is written from the user or customer's perspective. It should use words they would understand. It could be written using a tool like [Cucumber](https://cucumber.io/), [Fitnesse](http://docs.fitnesse.org/FrontPage) or [Approvals](https://approvaltests.com/), or it could be written in an ordinary unit testing framework.

### Do: Monty Hall or similar
Sketch a guiding test for a kata. For example [Monty Hall]({% link _kata_descriptions/monty_hall.md %}) or [Lift]({% link _kata_descriptions/lift.md %}) or [Theater](https://github.com/emilybache/Theater-Kata) or [Train Reservation](https://github.com/emilybache/KataTrainReservation).

Divide into pairs and have people sketch on a piece of paper. After about 5-10 minutes have them present to the rest of the group. Give them some feedback. Let them spend another 5 minutes or so to refine their sketches. Share them again and identify desirable traits. Ideally get the group to agree on one that would be usable in a future session as a Guiding Test.

Repeat with another Kata if their is time.

### Reflect: 
Compare and contrast the knowledge and assumptions you had about Guiding Tests (or whatever you call them in your organization) before this session and what you know now. Write a paragraph summarizing your comparisons.


