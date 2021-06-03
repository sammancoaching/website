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
* Operations
* Design
* Clean Code
* Analysis
* Testing
* Iteration
* Requirements

When people have made their marks, ask them to check their answers against [the waterfall model](https://en.wikipedia.org/wiki/Waterfall_model#Model).

### Concept: Iterative and incremental

The whole problem is too large to tackle all at once. In Waterfall, you split the work into phases. The purpose of the Analysis phase is to understand the requirements and work out how to decompose the problem. In TDD we still need to do that, but instead of doing it all at once in a phase by itself, we do it a little at a time. A little analysis, design, coding, testing... then iterate. 

Making a test list is part of the analysis work. You identify some pieces of the solution that are testable, that you can soon design and build. It helps you to get started. There is no standard format for this, it's an informal list that probably only you will read. It's not an artifact to be saved for posterity. Each item on the test list is a reminder of a test you think you might need. A sketch of an example input and expected outcome, or just a name of a scenario.

Every time you complete a TDD cycle you revisit your test list and update it. By doing the design and coding and testing you learn more about the problem and can revisit the analysis.

### Concrete: Carry on with TDD

* You have one failing test. Add production code in ‘insert_coin’ to make the test pass.
* Add a test for ‘dime’. This coin is worth 10 cents.
* Add a test for ‘quarter’. This coin is worth 25 cents.
* Add a test for ‘penny’. This coin should be rejected by the machine. 
* Refer to the full [Vending Machine](/kata_descriptions/vending_machine.html) description for additional functionality.

The starting position for this is in the 'empty_machine' branch of [VendingMachine-Approval-Kata](https://github.com/emilybache/VendingMachine-Approval-Kata) at least in the C version so far.

### Conclusions: small steps
Review the code written now. How many tests are crossed off the list? How many new tests did you think of and add to the list? Have you been working in small steps?
