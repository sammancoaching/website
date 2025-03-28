---
theme: test_design
title: Unit Test FIRST properties
kata: leap_years
difficulty: 2
author: emilybache
affiliation: ProAgile
tags: test_design
---

# Unit Test FIRST properties

Introducing Tim Ottinger & Brett Schuchert's [FIRST](http://agileinaflash.blogspot.com/2009/02/first.html) properties from "Agile in a Flash".

## Learning Goals

* List some important properties of a unit test, especially that they should be Fast and Isolated.
* Recognize tests that have FIRST properties and those that do not.

## Session Outline

* 10 min connect: Three facts and a question on unit tests
* 15 min concept: FIRST properties and active review
* 20 min concrete: write unit tests
* 5 min conclusions: review facts and question on unit test design

### Connect
Use the ["Three facts and a question"]({% link _activities/connect/three_facts_and_a_q.md %}) format with the topic "Designing Good Unit Tests".

### Concept
Explain the [FIRST properties](http://agileinaflash.blogspot.com/2009/02/first.html). Get people to actively review the properties by asking them to match these characteristics of a test with the FIRST property they are missing:

* Test contains a call to Thread.sleep(3000)
* Test has no assertions
* There are 15 detailed tests for the newly created function, none of which pass
* Test uses a REST api to fetch test data
* Test generates a random number and uses it as an input parameter
* One test creates a record in the database that the next test deletes
* Test fails if the current date is 29th February but passes otherwise
* Test prints the results and you have to check they are correct

### Concrete
Write some unit tests that have FIRST properties. Suggested exercise: [LeapYears]({% link _kata_descriptions/leap_years.md %}) or [FizzBuzz]({% link _kata_descriptions/fizzbuzz.md %}) or [ClosestToZero]({% link _kata_descriptions/closest_to_zero.md %}). The idea is to choose an exercise where the code under test is a pure function and relatively easy to write tests for. 

You could use [FIRST Test Design Kata](https://github.com/emilybache/FIRST-Test-Design-Kata) as a starting position.

### Conclusions
Review your facts and questions from the first part of the session. Can you answer any of the questions? Do any of the facts need reviewing? Annotate the notes you made with new notes detailing things you learnt during the session.




