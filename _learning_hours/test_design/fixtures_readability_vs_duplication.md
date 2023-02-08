---
theme: test_design
title: Test Fixtures - Readability vs Duplication
kata: recently_used_list
difficulty: 3
author: emilybache
affiliation: Bache Consulting
---

# Test Fixtures - Readability vs Duplication
In this learning hour we discuss if code duplication can be a problem for test code, and how it relates to readability.

## Learning Objective
- Compare test code with and without a fixture and how it affects readability

## Session Outline

* 10 min connect: Duplication vs Readability
* 30 min concrete: Refactor to use a Test Fixture
* 10 min concept: Did the refactoring improve the code?
* 5 min conclusions: Design principles for test code

## Connect: Duplication and Readability
Split into pairs and give each one a pile of cards or a virtual whiteboard frame with a pile of virtual cards. Each card should have a design guideline on, and two of them should be duplication and readability. You want them to discuss which are more important, by asking them to sort the cards. When they have all sorted the cards, compare notes briefly. What they have chosen isn't so important at the moment, so don't spend a long time discussing. You want to bring it up again in the conclusions. 

Example principles:

* The code has only one or perhaps two levels of indentation
* There is no duplicated code
* The code has no side effects - doesn't modify input parameters or global data
* The code is straightforward to read and understand
* Functions are short, less than 5 lines
* Lines of code are not over 80 characters long

## Concrete: Convert duplication to fixture
In [RecentlyUsedList](https://github.com/emilybache/RecentlyUsedList-Test-Design-Kata) there are several tests which share common code. Explain the problem and give them some pointers about how to refactor the tests to use a test fixture. If the participants haven't seen a test fixture before and are unfamiliar with the syntax, you might want to do the Learning Hour [Test Fixtures Intro]({{ site.baseurl }}{% link _learning_hours/test_design/fixtures_intro.md %}) before this one.

Work in pairs on the exercise, to gain fluency with test fixtures.

## Concept: Test Fixture
Reflect upon the code before and after the introduction of a test fixture. Put up the before and after code so they are both visible on a shared screen or virtual whiteboard. Use one of their solutions as the 'with fixture' example, or one you prepared earlier. If you are feeling ambitious, you could create a version using a fixture that is really hard to read, to spark discussion.

Do people think the code with the fixture is:

- easy to debug if it failed
- easy to add new test cases
- has less duplication
- easier to read

It's that last point that you hope will spark some discussion. If you do it badly, the code with a fixture can be so hard to read you'd be better off without it. 

## Conclusions
Bring up the design principles they prioritized in the 'connect' part. Are the priorities the same for test code? Discuss in pairs.
