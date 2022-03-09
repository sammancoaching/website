---
theme: test_design
title: Characteristics of Unit tests
kata: recently_used_list
difficulty: 2
author: emilybache
affiliation: ProAgile
---

# Characteristics of Unit tests

Using a list from Roy Osherove's book "The Art of Unit Testing".

## Session Outline

* 10 min connect: Questioning whether you have unit tests 
* 10 min concept: Characteristics of good unit tests
* 30 min concrete: write some unit tests for RecentlyUsedList
* 5 min conclusions: Note something you want to remember about unit test design

## Connect: Questioning whether you have unit tests

Ask yourself the following questions about the unit tests you’ve written up to now:

- Can I run and get unambiguous results from a unit test I wrote two weeks or months or years ago?
- Can any member of my team run and get results from unit tests I wrote two months ago?
- Can I run all the unit tests I’ve written in no more than a few minutes?
- Can I run all the unit tests I’ve written at the push of a button?
- Can I write a basic test in no more than a few minutes?

Add a tick or a cross to each to mark your answer.

If anyone answered 'no' to any question, point out that what they were doing was probably useful, but probably not a unit test in the sense that we are using this word.

## Concept: Characteristics of good unit tests

Work in pairs to come up with characteristics, both by looking at the previous questions and by thinking about your own experience. After 5 minutes compare your list with the one below. Did you miss anything? Any extras?

According to Roy Osherove in his book "The Art of Unit Testing", a unit test should have the following properties:

- It should be automated and repeatable.
- It should be easy to implement.
- It should be relevant tomorrow.
- Anyone should be able to run it at the push of a button.
- It should run quickly.
- It should be consistent in its results (it always returns the same result if you don’t change anything between runs).
- It should have full control of the unit under test.
- It should be fully isolated (runs independently of other tests).
- When it fails, it should be easy to detect what was expected and determine how to pinpoint the problem.

## Concrete: Convert a main function into a test

Look at the ["RecentlyUsedList" implementation](https://github.com/emilybache/custom-start-points/tree/master/start-points/RecentlyUsedList1/C). There is a main function you can use to test it. In what ways does this not fulfil the characteristics of a good unit test?

Re-write it as a unit test. When you've done that, add more tests to improve the coverage.

## Conclusions: Note something you want to remember about unit test design
Perhaps something about the test framework or syntax or a characteristic of unit tests you want to remember.

