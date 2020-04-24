---
layout: default
title: Coverage and Combinations
parent: Approval Testing
grand_parent: Workshops
nav_order: 2
---

# Using Coverage and Combinations with Legacy Code

When you inherit valuable but difficult code that you need to change, this approach can enable you to add some tests without necessarily really understanding the code.

- Using coverage to identify missing test cases
- Using Combinations to increase confidence


We work through some exercises adding tests to legacy code  using the ['Approvals'](https://github.com/approvals) tool. We will work in small groups and each group can agree which programming language to use. The exercises are generally available in Java, C#, Python and C++.

## Session Outline
 
* 5 min connect: read through each other's mind maps
* 2 min connect: Approval Testing Characteristics Stand-Up 
* 5 min concept: Legacy code and coverage
* 10 min demo: Coverage in IDE and add tests
* 30 min concrete: Add tests using coverage
* 5 min conclusions: Describe an algorithm for adding tests to existing code

(short break)

* 5 min connect: Refactoring safety net
* 10 min concept: Branch coverage
* 15 min concept: demo Gilded Rose
* 30 min concrete: add combination approval tests to Gilded Rose
* 5 min conclusions: Pair Share about Combination Approvals

(short break)

* 10 min connect: Situations where this won't work
* 10 min concept: Limitations of coverage
* 10 min concrete: Demo mutation testing
* 20 min concrete: Do mutation testing
* 5 min conclusions: Look again at the situations where this won't work

(short break)

* 5 min concept: Extract a function
* 15 min concrete: Validate and Add Product - extract function
* 10 min conclusions: walkabout posters & code review
* 15 min retrospective: gather observations

## Part 1

Using coverage to add regression tests.

### Connect: read through each other's mind maps

Browse them and update your own mind map if you find something really good

### Connect: Approval Testing Characteristics Stand-Up 

Read out some statements. People stand up if they agree they are true. (Or give thumbs up)


### Concept: Legacy code and coverage

Slides - what is legacy code, how to test it.  Also: get them to configure their IDEs.

### Demo: Coverage in IDE and add tests

Show adding a first test to the [Product Export Refactoring Kata](https://github.com/emilybache/Product-Export-Refactoring-Kata)

### Concrete: Add tests using coverage

Get them to do the same first test and add more to get 100% coverage.


### Conclusions: Describe an algorithm 

Is what we've done sufficiently mechanical that you could describe an algorithm for adding tests to existing code?

Write a point by point instruction list about what to do.

## Part 2

Using branch coverage and Combination approvals to improve the tests we add this way

### Connect: Refactoring safety net

In pairs, discuss weaknesses with the tests we've written. Would you feel confident to refactor this code now? Where could you still introduce bugs? 

### Concept: Branch coverage

Slides explaining what this is. Also: get them to configure their IDEs.

### Concept: demo Gilded Rose

Show the [Gilded Rose](https://github.com/emilybache/GildedRose-Refactoring-Kata) exercise. Extract a function. Switch to Combination approvals.

### Concrete: add combination approval tests to Gilded Rose

Get them to extract the function and write the tests using coverage.

### Conclusions: Pair Share about Combination Approvals

* Turn to the person sitting next to you
* Tell them the most useful thing you’ve learnt so far about Combination Approvals

## Part 3

Using mutation testing to further improve the tests we add this way. Talk about limitations of this approach.

### Connect: Situations where this won't work

In pairs, discuss weaknesses with the tests we've written. Would you feel confident to refactor this code now? Where could you still introduce bugs the tests wouldn't find? 

### Concept: Limitations of coverage

Slides explaining covered != bug free and uncovered != buggy. Also introduce mutation testing.


### Concrete: Demo mutation testing

Do it by hand in [Gilded Rose](https://github.com/emilybache/GildedRose-Refactoring-Kata).


### Concrete: Do mutation testing

Everyone have a go

### Conclusions: Look again at the situations where this won't work

Would you feel confident to refactor this code now? Where could you still introduce bugs the tests wouldn't find? 

## Part 4

Review and conclusions

### Concept: Extract a function

This is the hardest first step. Slide.

### Concrete: Validate and Add Product - extract function

Show it on another codebase - [ValidateAndAddProduct](https://github.com/emilybache/ValidateAndAddProduct-Refactoring-Kata) 

### Conclusions: walkabout posters & code review

Get people to look through everything we've done today and discuss with someone what they've learnt. Write answers on the mind-map as sub-nodes.

### Retrospective: next steps

Everyone spends 3 minutes writing notes. What will I

* start doing now
* continue doing now
* want to learn more about

Go round and everyone say something. Yes, and. No questioning other people's conclusions.

