---
theme: refactoring
title: Roll Up Loop
kata: timer_expiry
difficulty: 3
author: emilybache
affiliation: ProAgile
tags:  refactoring
---

# Roll Up Loop

This refactoring doesn't seem to have an official description anywhere, but it's one I often use. The sign it could be useful is a long method with lots of if statements. Each if statement essentially returns a value of the same type. A loop is really just a sequence of if statements, so often you can make the code cleaner and easier to read by rolling up the if statements into a loop. The trick is to identify an abstraction to loop over.

## Session Outline

* 5 min connect: Code smells and refactorings 
* 10 min concept: Roll-up loop
* 35 min do: refactor away the duplication
* 5 min reflect: note down learnings

## Connect: Code smells and refactorings

Ask the group to name some refactorings that they have used, and the corresponding code smells.

## Concept: Roll Up loop
Explain what this is. Demo some of the simpler examples in [RollUpLoop-Refactoring-Practice](https://github.com/emilybache/RollUpLoop-Refactoring-Practice).

## Concrete: refactoring practice
Have them work through the examples in [RollUpLoop-Refactoring-Practice](https://github.com/emilybache/RollUpLoop-Refactoring-Practice) turning the 'before' version into the 'after' version. Encourage them to continue refactoring after that if they now see new opportunities to use any abstractions they have introduced.

For a follow-up session or if they get the idea very quickly, there are two harder exercises - [TimerExpiry](https://github.com/emilybache/TimerExpiry-Refactoring-Kata) and [ClarifyException](https://github.com/emilybache/Clarify-Exception-Refactoring-Kata). For these ones there is no 'after' shown in the main branch. 

For TimerExpiry you could change to a design with a list of function pointers you loop over. Each function returns the time until the timer goes off. Then find the smallest value in one place rather than 6 places. 

For ClarifyException you can have a small class rather than a function pointer - with two methods "matches" and "build".

## Conclusions: note down learnings
Describe this refactoring in your own words or discuss in pairs. Include

* signs and smells that it could be needed
* what the outcome looks like
* any disadvantages or when not to use it
