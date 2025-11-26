---
theme: testable_design
title: Writing tests for pure functions
kata: trig_math
difficulty: 1
author: emilybache
affiliation: ProAgile
tags: testable_design c
---

# Writing tests for pure functions

## Session Outline
 
* 10 min connect: pure or not quizz  
* 25 min concrete: write tests for trig math
* 5 min reflect: was this easy or hard?
* 10 min concept: pure functions are easier to test   
* 5 min reflect: pure functions in your code?

### Connect: Pure or not quizz
Examine the [code snippets](https://github.com/emilybache/Pure-Or-Not-Quizz). Note down which are pure functions.

### Concrete: Trig math
Use the [cyber-dojo starting point](https://github.com/emilybache/custom-start-points/tree/master/start-points/TrigMath).

### Reflect
Fist to five vote: 5 fingers = very, zero = not at all

- How hard was getting some test coverage of this code?
- How relevant was this to your normal work?

Ask for comments: how did this feel?

### Concept: Pure functions are easier to test
This code was relatively easy to get basic tests in place. Mostly small functions, but (more importantly) _pure_ functions

An easy-to-test function has these properties:

1. You can see all the inputs in the argument list
2. The execution is deterministic (same input produces same output)
3. You can see all the outputs in the return value

Code that is harder to test will lack some or all of these properties.

### Reflect: What about your code?
Fist to five vote: 5 fingers = very, zero = not at all

- How much of the time do you find yourself writing tests for functions that have all these three properties?

