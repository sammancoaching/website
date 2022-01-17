---
theme: test_design
title: Complexity / Collaborator quadrant analysis
kata: leap_years
difficulty: 4
author: emilybache
affiliation: ProAgile
---

# Complexity / Collaborator quadrant analysis

In his book "Unit Testing Principles, Practices and Patterns", Vladimir Khorikov analyses the code to be tested in terms of Complexity and Collaborator quandrants. This learning hour introduces them.

## Session Outline

* 5 min connect: 
* 10 min concept: Complexity / Collaborator quandrant analysis
* 30 min concrete: ChangeEmail
* 5 min conclusions: 

### Connect: What is easy to test

* Calculates a discount
* Produces a report
* Uses the current date and time
* Calls a 3rd party REST API
* Deletes data in a database

### Concept: Complexity / Collaborator quandrant analysis

In his book "Unit Testing Principles, Practices and Patterns", Vladimir Khorikov analyses the code to be tested in terms of Complexity and Collaborator quandrants. The main introduction to this is in section 7.1. Summarize what he says. Code that falls into the 'Overcomplicated' quandrant should be split up to make it easier to test.

### Concrete

