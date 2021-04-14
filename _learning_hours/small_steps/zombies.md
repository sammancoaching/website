---
theme: small_steps
title: Slicing a task using ZOMBIES
kata: calc_stats
difficulty: 3
---

# Slicing a task using ZOMBIES

When you're working in TDD you'd like your cycles to be short and fairly regular. That means slicing up the problem into pieces. ZOMBIES is an acronym invented by James Grenning to help you to do that.

## Session Outline
 
* 10 min connect: Classify activities as Iterative, Incremental or Waterfall
* 5 min concept: ZOMBIES
* 35 min concrete: do some TDD
* 5 min reflect: Did we find good slices of the problem using ZOMBIES?


### Connect: Classify activities

💧 = waterfall style
💫 = iterative style
🍕 = incremental style

Read these statements which describe development practices or policies. Use one of the symbols at the top to classify that practice or policy - copy and paste a symbol next to each item.
* When you think the whole user story is finished, deploy it to a test environment and have someone else test it then write bug reports. 
* Split a large user story into 5 pieces which all have business value. Implement one each week for 5 weeks.
* Write a complete list of all interesting test cases before you start implementing any code
* If you only have a vague idea of what your customer wants, show them a working sketch or prototype before investing in building tests or a whole solution
* Write a test for the simplest case you can think of first, perhaps an empty list or zero argument. Make that one pass in a simple way before writing any more complicated code or tests.
* While working on getting a test to pass you realize three more situations are not covered by the production code. Make a note of them, make the current test pass, then write more tests for the three new cases in turn.

### Concept: ZOMBIES

In [this article](http://blog.wingman-sw.com/tdd-guided-by-zombies) by James Grenning he describes a method for slicing a coding problem. 

Throughout, remember to come up with Simple Scenarios and Simple Solutions. Find cases for Zero, One, Many (or more complex). For each of Zero, One, Many, think about Boundary behaviours, Interfaces and Exceptions.

This acronym should help you to come up with an initial test list and to update it as you work iteratively and incrementally towards a full solution.

### Concrete: do some TDD
Some problems have very obvious zero, one, many - for example when building a function whos argument is a list. Try [CalcStats](kata_descriptions/calc_stats.html) or [ClosestToZero](kata_descriptions/closest_to_zero.html).

### Conclusions: Review TDD cycles
Check the test list against the TDD cycles. Ask - did we work iteratively and incrementally? Did ZOMBIES help us with splitting up the task into pieces?

