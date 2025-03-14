---
theme: approval_testing_bdd
kata: rpg_combat
title: Data Driven testing with Approvals
difficulty: 1
author: emilybache
affiliation: ProAgile
tags: approvals bdd
---

# Data-Driven Testing with Approvals

A Data-Driven test keeps the 'act' part of the test the same, and only varies the data in the 'arrange' part. The 'assert' part of the test usually varies according to the data given, and with an approval testing approach, it becomes easy to update.

## Session Outline
 
* 5 min connect: describe data-driven testing
* 10 min do: set-up for Approval testing
* 30 min do: RPG Combat kata  
* 5 min reflect: How readable are the test cases?

### Connect
Mark all the statements that are true of Data-Driven testing

- The assertion is the same in every test case
- The 'act' step is the same in every test case
- It's also known as 'parameterized testing' or 'table-driven testing'
- Every test initializes a known database at the beginning
- You exercise many kinds of behaviour primarily by varying the input data
- The input data is always the same

### Setup for Approval testing
Make sure everyone knows how to:

- add Approvals as a dependency to the project
- configure the Reporter
- Stop received files from being added to git

Encourage them to make a commit whenever they have green tests.

### Do: RPB Combat kata
This kata lends itself to data-driven testing, with PlayerCharacters with different starting data. There is a convenient [starting point](https://github.com/emilybache/RPG-Combat-Approval-Kata) available.

### Reflect
There are some retrospective questions in the [Kata description]({% link _kata_descriptions/rpg_combat.md %}). Have people especially consider how readable the test cases are, and whether any would qualify as data-driven tests. If you like, show the [sample solution](https://github.com/emilybache/RPG-Combat-Approval-Kata/tree/sample_solution).
