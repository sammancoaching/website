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
 
* 5 min connect: what is a test list for
* 5 min concept: iterative and incremental
* 35 min concrete: do some TDD
* 10 min reflect: did we work in small steps


### Connect: what is a test list for

Tell me 5 things that are important to remember about a test list.

### Concept: Iterative and incremental

The whole problem is too large to tackle all at once. The test list helps us to get started on a small piece. Add to the list as you discover more things that need to be done.

### Concrete: Carry on with TDD

* You have one failing test. Add production code in ‘insert_coin’ to make the test pass.
* Add a test for ‘dime’. This coin is worth 10 cents.
* Add a test for ‘quarter’. This coin is worth 25 cents.
* Add a test for ‘penny’. This coin should be rejected by the machine. 
* Refer to the full [Vending Machine](/kata_descriptions/vending_machine.html) description for additional functionality.

### Conclusions: small steps
Review the code written now. How many tests are crossed off the list? How many new tests did you think of and add to the list? Have you been working in small steps?
