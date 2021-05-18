---
theme: small_steps
title: TDD with a list
kata: vending_machine
difficulty: 2
---

# TDD with a list

TDD is perhaps a little easier when someone else has started making the test list for you.

## Learning Objectives

* describe how a test list supports working iteratively and incrementally
* use a test list during TDD

## Session Outline
 
* 5 min connect: waterfall phases
* 5 min concept: iterative and incremental
* 35 min concrete: do some TDD
* 10 min reflect: did we work in small steps


### Connect: Waterfall phases

Mark the activities on this list that are phases in a Waterfall method:

* Singleton
* Coding
* Sprint planning
* Design
* Clean Code
* Analysis
* Testing
* Iteration
* Requirements
* Operations

When people have made their marks, ask them to check their answers agains [the waterfall model](https://en.wikipedia.org/wiki/Waterfall_model#Model).

### Concept: Iterative and incremental

The whole problem is too large to tackle all at once. In Waterfall, you split the work into phases. The purpose of the Analysis phase is to understand the requirements and work out how to decompose the problem. In TDD we still need to do that, but instead of doing it all at once in a phase by itself, we do a little analysis, a little design, a little coding, a little testing, then iterate. The test list is part of the analysis work. It helps us to identify some pieces that are testable, that we can design and build. It helps us to get started. Every time we complete a TDD cycle we revisit our test list and update it. By doing the design and coding and testing we discover more about the problem and can revisit our analysis.

### Concrete: Carry on with TDD

* You have one failing test. Add production code in ‘insert_coin’ to make the test pass.
* Add a test for ‘dime’. This coin is worth 10 cents.
* Add a test for ‘quarter’. This coin is worth 25 cents.
* Add a test for ‘penny’. This coin should be rejected by the machine. 
* Refer to the full [Vending Machine](/kata_descriptions/vending_machine.html) description for additional functionality.

### Conclusions: small steps
Review the code written now. How many tests are crossed off the list? How many new tests did you think of and add to the list? Have you been working in small steps?
