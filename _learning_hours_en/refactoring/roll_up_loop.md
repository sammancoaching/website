---
theme: refactoring
title: Roll Up Loop
kata: timer_expiry
difficulty: 3
author: emilybache
affiliation: ProAgile
---

# Roll Up Loop

This refactoring doesn't seem to have an official description anywhere, but it's one I often use. The sign it could be useful is a long method with lots of if statements. Each if statement essentially returns a value of the same type. A loop is really just a sequence of if statements, so often you can make the code cleaner and easier to read by rolling up the if statements into a loop. The trick is to identify an abstraction to loop over.

## Session Outline

* 5 min connect: Code smells and refactorings 
* 5 min concept: Roll-up loop
* 5 min demo: show them the code duplication & go through strategy
* 35 min do: refactor away the duplication
* 5 min reflect: note down learnings


## Connect: Code smells and refactorings

Ask the group to name some refactorings that they have used, and the corresponding code smells.

## Concept: Roll Up loop

Explain what this is. Demonstrate a really simple case, like one of the examples in [RollUpLoop](https://github.com/emilybache/RollUpLoop).

## Demo: show them the code duplication & go through strategy
There are two exercises I use for this - [TimerExpiry](https://github.com/emilybache/TimerExpiry-Refactoring-Kata) and [ClarifyException](https://github.com/emilybache/Clarify-Exception-Refactoring-Kata). Both work equally well.

Show them the duplication in each if statement. Explain the goal - for TimerExpiry this a list of function pointers you loop over. Each function returns the time until the timer goes off. Then just find the smallest value in one place rather than 6 places. For ClarifyException you can have a small class rather than a function pointer - with two methods "matches" and "build".

## Concrete: refactor away the duplication

Have them work on the code to achieve the refactoring goal - roll up loop.

## Conclusions: note down learnings

Describe this refactoring in your own words. Include

* signs and smells that it could be needed
* what the outcome looks like
* any disadvantages of it
