---
layout: default
title: Using Coverage and Combinations with Legacy Code
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
 
* 10 min connect: code coverage warm-up questions
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

* 5 min connect: Situations where this won't work
* 5 min concept: Limitations of coverage
* 10 min concrete: Demo mutation testing
* 20 min concrete: Do mutation testing
* 5 min conclusions: Look again at the situations where this won't work

(short break)

* 5 min connect: Pure or not?
* 15 min concept: Validate and Add Product - extract function demo
* 30 min concrete: do Validate and Add Product
* 10 min conclusions: walkabout posters & code review
* 15 min retrospective: gather observations

## Part 1

Using coverage to add regression tests.

### Connect: Code coverage warm-up questions

Look at these [warm-up questions](../../exercises/warm_up_questions/coverage_warm_up_questions.html). Think for yourself then discuss with a pair.

### Connect: Approval Testing Characteristics Stand-Up 

Read out some statements. People stand up if they agree they are true. (Or give thumbs up)

### Concept: Legacy code and coverage

Slides - what is legacy code, how to test it.  Also: get them to configure their IDEs.

### Demo: Coverage in IDE and add tests

Explain the starting position for [Product Export Refactoring Kata](https://github.com/emilybache/Product-Export-Refactoring-Kata). You want to add tests for ``XMLExporter`` until you have 100% coverage. The starting code contains an empty test that doesn't do anything, but very helpfully, there is some test data available in ``SampleModelObjects``. Write a test case for the first function in ``XMLExporter``, I suggest using Approvals and VerifyXML in particular. Show the coverage. It should be much improved for that function, but not 100%. Leave that for them to fix.

Many IDEs have coverage metrics built in and mark lines of code as covered or not covered in the editor. Before this session make sure you know what tools the team has available to them and take the chance to show them how to use them. For example colour-blind people may need to adjust the IDE settings. 

### Concrete: Add tests using coverage

Have people work in pairs to do the exercise. Help them to set up their IDEs as necessary.

The last function they try to write tests for has a twist. The output varies with every run since it prints today's date. Some pairs will be able to work out a way to handle it, others will ask for help. You probably won't have time to help them fix that in this session, assure them you will tackle it in a later session. Ask them to focus on getting 100% coverage for the other functions for the time being.

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

### Connect: Pure or not?
What are the rules for what functions count as 'pure'? Look at the examples in [Pure-Or-Not-Quizz](https://github.com/emilybache/Pure-Or-Not-Quizz) and mark which ones are pure and which ones aren't. If you get stuck, look at the [Wikipedia article](https://en.wikipedia.org/wiki/Pure_function) describing what a pure function is. 

### Concept: Validate and Add Product - extract function

The starting position for [ValidateAndAddProduct-Refactoring-Kata](https://github.com/emilybache/ValidateAndAddProduct-Refactoring-Kata) has an ordinary Approval test to start you off. The coverage is not great, and you'd like to increase it. Combination Approvals would be a good approach since it's one big piece of conditional logic with few side effects.

Demonstrate extracting a pure function to use with Combination Approvals. The function should take arguments which are all the things you need to vary in order to cover all the logic branches in the production code. The return type should be a string which contains all the important outputs and can be used to verify against.

Note: the branch 'with_tests' includes an example of how to write this function. 

### Concrete: Use Combination Approvals
Have them complete the Validate and Add Product exercise in pairs. I recommend leaving your code up on the screen while they work on repeating what you just did. Then they should go on and increase the number of combinations until the coverage is 100%.

### Conclusions: walkabout posters & code review

Get people to look through everything we've done today and discuss with someone what they've learnt. Write answers on the mind-map as sub-nodes. Review [warm-up questions](../../exercises/warm_up_questions/coverage_warm_up_questions.html)

Mind map questions:

* What is Legacy code?
* What do you need to do before you can add Approval tests to legacy code?
* What is Code Coverage useful for?
* What is Mutation Testing useful for?
* What are Pure Functions useful for?
* What is the difference between Combination Approvals and ordinary Approvals?

### Retrospective: next steps

Everyone spends 3 minutes writing notes. What will I

* start doing now
* continue doing now
* want to learn more about

Go round and everyone say something. Yes, and. No questioning other people's conclusions.

